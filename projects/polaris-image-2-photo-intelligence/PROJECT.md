# Polaris Image 2 Photo and Video Intelligence

## Summary

Build a lightweight real-estate photo and video intelligence pipeline with a
review demo. Given a property tour with photos and optional walkthrough videos,
produce one schema-valid JSON output covering every input photo ID, chapter the
videos by room/space, sync video segments to photos, and make the result easy to
inspect in a polished UI.

This is a public, sanitized tryout version of a real Covent problem. The goal is
not to copy Covent internals. The goal is to show that you can design, build,
validate, deploy, and explain a practical system for messy property photos.

## Problem

Real-estate teams receive long photo tours with mixed exterior, interior,
smartphone, professional, blurry, partial, duplicate, and low-information
images. They also receive walkthrough videos that may sweep through multiple
rooms without clean labels. A useful system must turn those tours into
structured output without dropping, duplicating, or inventing photo IDs, and it
must help reviewers understand which parts of a video correspond to each
room/space.

The output should be useful for downstream product surfaces such as gallery
grouping, hero photo selection, property summaries, routing hard cases to a VLM,
operator review, video chaptering, and quality checks.

The hard part is not only classification. A credible product also needs a good
input flow, processing states, a trustworthy output viewer, validation errors,
and an API boundary that could grow into production.

## Required User Flow

1. User creates or opens a property analysis session.
2. User loads one of the included PhotoTours property tours or uploads multiple
   property photos and optional walkthrough videos.
3. App shows upload/loading/processing state.
4. Backend or local service runs a photo/video intelligence pipeline.
5. Pipeline returns schema-valid JSON and a validation report.
6. Frontend renders:
   - photo gallery
   - per-photo labels
   - grouped spaces
   - walkthrough video player with room/space chapters
   - chapter-to-photo sync or evidence links
   - selected listing hero
   - generated titles and descriptions for spaces, photos, and video chapters
   - validator status and warnings
   - raw JSON viewer or download

## Scope

Build a full-stack app or equivalent runnable product demo that:

- Accepts a JSON input with `property_id` and `photos[]`, and can use the
  included PhotoTours fixture as a realistic seed dataset.
- Emits a JSON output with top-level `photos`, `spaces`, `property`, and
  `warnings`.
- Includes exactly one output record for every input photo ID.
- Accepts optional `videos[]` inputs and emits a video extension with chapter
  ranges, room/space labels, synced photo IDs, titles, descriptions, and
  warnings.
- Groups photos into displayable spaces.
- Chooses a listing hero photo and per-space hero photos.
- Classifies simple per-photo fields such as room role, condition, image
  quality, and capture source.
- Chapters walkthrough videos by room/space, including start/end timestamps.
- Syncs each meaningful video chapter to the most relevant still photos and
  spaces.
- Generates concise titles and descriptions for each space and video chapter.
- Includes a frontend upload/load and review workspace.
- Includes an API boundary for session creation, upload/load, analysis, and
  result retrieval, unless your stack is intentionally local-only and explains
  that tradeoff.
- Uses local file storage, SQLite, JSON storage, or an object-storage-compatible
  abstraction.
- Includes a validator and sample run command.
- Includes a benchmark or evaluation report against your own labeled sample set.
- Includes a cost report, deployment plan, and walkthrough video.

You may use heuristics, embeddings, frame extraction, open-source image/video
models, hosted VLM/video APIs, or a hybrid approach. If you use hosted APIs,
document cost, latency, and how you would avoid running expensive models on
every photo, frame, or video in production.

## Out Of Scope

- Do not use private Covent data.
- Do not commit secrets, API keys, or scraped private images.
- Do not claim production accuracy without evidence.
- Do not hardcode the sample output.

## Public Schema Contract

Use `schema/polaris_image_2_public_contract.json` as the minimum output
contract. You may add fields, but the required fields must remain valid.

## Sample Data

This repo includes both tiny synthetic contract examples and a realistic
PhotoTours URL fixture under `sample-data/`.

- `sample_input.json` and `sample_output.json` are for validating JSON shape and
  ID coverage. The image URLs are placeholders by design.
- `phototours_100_properties.json` includes 100 older PhotoTours property tours
  with addresses, lightweight property metadata, and real remote photo URL
  references. Use it for realistic photo tour shape, visual review, evaluation,
  and demo seed data.
- `phototours_video_walkthroughs_100_properties.json` includes 100 PhotoTours
  property tours with both photo URL references and walkthrough video URL
  references. Use it for video chaptering, photo/video sync, title generation,
  and richer review UI work.

Do not commit downloaded image copies unless you have explicit permission and a
clear reason. URL references are enough for this tryout.

## Acceptance Criteria

A strong approved submission must:

- Run from a clean checkout with documented commands.
- Let a reviewer load a PhotoTours property tour or upload multiple images and
  videos, then run analysis locally.
- Produce valid JSON for the sample input and at least one PhotoTours property
  tour.
- Pass the provided validator:
  `python3 projects/polaris-image-2-photo-intelligence/scripts/validate_output.py --input <input.json> --output <output.json>`.
- Preserve exact input photo IDs with no missing, duplicate, or hallucinated
  references.
- Preserve exact input video IDs when videos are present.
- Include at least one non-trivial full-tour sample output.
- Include at least one video walkthrough sample output with timestamped
  chapters.
- Sync each video chapter to one or more photos, spaces, or an explicit
  `no_match` warning.
- Generate titles and descriptions for spaces and video chapters.
- Show validator success/failure in the UI.
- Include backend or service-level validation that rejects or flags malformed
  outputs.
- Include at least one automated test for the validator, API contract, or JSON
  compiler.
- Include a short evaluation report with metrics and failure analysis.
- Explain whether your system is cheap-path only, image/video-model-only, or
  hybrid routed.
- Explain cost and latency expectations.
- Include a deployment plan covering hosting, storage, background jobs, secrets,
  observability, and expected operating constraints.
- Include a walkthrough video explaining the system end to end.
- Include a writeup with architecture, API design, data/model choices,
  deployment plan, limitations, and what you would improve with more time.

## Bonus Points

The core bar is a runnable, validated product demo. Bonus points reward work
that makes the submission feel closer to a real production seed:

- Design taste: a polished, dense review UI with strong media layout, clear
  hierarchy, responsive behavior, and complete empty/loading/error states.
- Video intelligence: accurate room/space chaptering, timestamped evidence,
  chapter-to-photo sync, and graceful handling of ambiguous walkthrough clips.
- Model judgment: a clear explanation of cheap-path, image-model, video-model,
  VLM, or hybrid routing choices, including confidence thresholds and fallback
  behavior.
- Production readiness: realistic deployment architecture, background jobs,
  storage, observability, secrets handling, retry behavior, and cost model.
- Evaluation depth: labeled examples, metrics, baseline comparison, failure
  analysis, and representative screenshots or video captures.
- Communication quality: a concise walkthrough video, screenshots, architecture
  diagram, and writeup that make the system easy to judge quickly.

## Suggested Milestones

1. Parser and validator.
2. Per-photo classifier baseline.
3. Space grouping, hero selection, titles, and descriptions.
4. Video frame extraction or video-model baseline.
5. Video chaptering and photo/video sync.
6. Session/upload or fixture-load flow.
7. Full JSON compiler and review UI.
8. Evaluation report, cost report, deployment plan, and walkthrough video.
9. Optional VLM/router layer for hard cases.

## Suggested API Shape

You can choose your own implementation, but this is a good starting point:

```text
POST /api/sessions
POST /api/sessions/:id/photos
POST /api/sessions/:id/videos
POST /api/sessions/:id/analyze
GET  /api/sessions/:id/result
GET  /api/sessions/:id/photos/:photoId
GET  /api/sessions/:id/videos/:videoId
```

## Suggested Tech

Use what you know well. Good options:

- Next.js full-stack app
- FastAPI + React/Vite
- Node/Express + React/Vite
- SQLite or file-backed JSON storage
- Local filesystem storage for uploaded images

Document tradeoffs if your stack would need changes for production.

## Submission Location

Place code submissions under:

```text
projects/polaris-image-2-photo-intelligence/submissions/<your-github-handle>/
```

Your folder should include:

- `README.md`
- `WRITEUP.md`
- runnable source code
- sample outputs for at least one PhotoTours property
- sample output with video chapters when using the video fixture
- validation or benchmark commands
- cost/deployment report
- walkthrough video link

## Data Safety

Do not include private Covent data, customer images, scraped private images,
teacher labels, internal prompts, Slack exports, API keys, service tokens, or
local-machine paths. Public submissions should be reproducible using only
public-safe inputs and the included URL fixture.
