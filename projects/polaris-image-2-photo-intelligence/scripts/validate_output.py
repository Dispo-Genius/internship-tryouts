#!/usr/bin/env python3
"""Lightweight public validator for Polaris Image 2 tryout submissions."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PHOTO_ROLES = {"exterior", "kitchen", "living_area", "bedroom", "bathroom", "utility", "other", "unknown"}
CONDITIONS = {"EXCELLENT", "GOOD", "FAIR", "POOR", "SEVERE", None}
IMAGE_QUALITIES = {"good", "partial", "blurry", "bad"}
CAPTURE_SOURCES = {"professional", "smartphone", "unknown"}
SPACE_TYPES = {
    "exterior",
    "yard",
    "kitchen",
    "living_room",
    "dining_room",
    "bedroom",
    "bathroom",
    "utility",
    "garage",
    "other",
    "unknown",
}
CONFIDENCE = {"low", "medium", "high"}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def input_photo_ids(payload: dict[str, Any]) -> list[str]:
    return [str(photo.get("photo_id")) for photo in payload.get("photos", [])]


def validate(input_payload: dict[str, Any], output_payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    expected_ids = input_photo_ids(input_payload)
    expected_set = set(expected_ids)

    if output_payload.get("property_id") != input_payload.get("property_id"):
        errors.append("property_id does not match input")

    photos = output_payload.get("photos")
    if not isinstance(photos, list):
        errors.append("photos must be an array")
        photos = []

    output_ids = [str(photo.get("id")) for photo in photos if isinstance(photo, dict)]
    if len(output_ids) != len(set(output_ids)):
        errors.append("photos contains duplicate ids")
    if set(output_ids) != expected_set:
        errors.append(
            f"photos ids do not match input: missing={sorted(expected_set - set(output_ids))} "
            f"extra={sorted(set(output_ids) - expected_set)}"
        )

    for photo in photos:
        if not isinstance(photo, dict):
            errors.append("photo entry is not an object")
            continue
        pid = str(photo.get("id"))
        if photo.get("visible_room_role") not in PHOTO_ROLES:
            errors.append(f"photo {pid}: invalid visible_room_role")
        if photo.get("condition_level") not in CONDITIONS:
            errors.append(f"photo {pid}: invalid condition_level")
        if photo.get("image_quality") not in IMAGE_QUALITIES:
            errors.append(f"photo {pid}: invalid image_quality")
        if photo.get("capture_source") not in CAPTURE_SOURCES:
            errors.append(f"photo {pid}: invalid capture_source")
        if not isinstance(photo.get("tags"), list):
            errors.append(f"photo {pid}: tags must be an array")

    spaces = output_payload.get("spaces")
    if not isinstance(spaces, list):
        errors.append("spaces must be an array")
        spaces = []

    space_ids = {str(space.get("id")) for space in spaces if isinstance(space, dict)}
    referenced_space_photos: list[str] = []
    for space in spaces:
        if not isinstance(space, dict):
            errors.append("space entry is not an object")
            continue
        sid = str(space.get("id"))
        if space.get("space_type") not in SPACE_TYPES:
            errors.append(f"space {sid}: invalid space_type")
        if space.get("condition_level") not in CONDITIONS:
            errors.append(f"space {sid}: invalid condition_level")
        if space.get("confidence") not in CONFIDENCE:
            errors.append(f"space {sid}: invalid confidence")
        photos_in_space = [str(pid) for pid in space.get("photos", [])]
        referenced_space_photos.extend(photos_in_space)
        if str(space.get("hero_photo_id")) not in photos_in_space:
            errors.append(f"space {sid}: hero_photo_id is not in space photos")
        for pid in photos_in_space:
            if pid not in expected_set:
                errors.append(f"space {sid}: unknown photo id {pid}")

    cwt = ((output_payload.get("property") or {}).get("canonical_write_targets") or {})
    listing_hero = str(cwt.get("listing_hero_photo_id"))
    if listing_hero not in expected_set:
        errors.append("listing_hero_photo_id is not an input photo id")

    display_spaces = cwt.get("display_spaces")
    if not isinstance(display_spaces, list):
        errors.append("property.canonical_write_targets.display_spaces must be an array")
        display_spaces = []

    referenced_display_photos: list[str] = []
    for display_space in display_spaces:
        if not isinstance(display_space, dict):
            errors.append("display space entry is not an object")
            continue
        did = str(display_space.get("id"))
        source_space_ids = [str(sid) for sid in display_space.get("source_space_ids", [])]
        photos_in_display = [str(pid) for pid in display_space.get("photos", [])]
        referenced_display_photos.extend(photos_in_display)
        for sid in source_space_ids:
            if sid not in space_ids:
                errors.append(f"display space {did}: unknown source_space_id {sid}")
        if str(display_space.get("hero_photo_id")) not in photos_in_display:
            errors.append(f"display space {did}: hero_photo_id is not in display photos")
        for pid in photos_in_display:
            if pid not in expected_set:
                errors.append(f"display space {did}: unknown photo id {pid}")

    if sorted(referenced_display_photos) != sorted(expected_ids):
        errors.append("display_spaces photos must cover every input photo exactly once")

    if not isinstance(output_payload.get("warnings"), list):
        errors.append("warnings must be an array")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    errors = validate(load_json(args.input), load_json(args.output))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
