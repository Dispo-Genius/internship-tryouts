# Polaris Image 2 Photo Intelligence

## Summary

Build a lightweight real-estate photo intelligence pipeline. Given a property
photo tour, produce one schema-valid JSON output covering every input photo ID.

This is a public, sanitized tryout version of a real Covent problem. The goal is
not to copy Covent internals. The goal is to show that you can design, build,
validate, and explain a practical pipeline for messy property photos.

## Problem

Real-estate teams receive long photo tours with mixed exterior, interior,
smartphone, professional, blurry, partial, duplicate, and low-information
images. A useful system must turn those tours into structured output without
dropping, duplicating, or inventing photo IDs.

The output should be useful for downstream product surfaces such as gallery
grouping, hero photo selection, property summaries, routing hard cases to a VLM,
and quality checks.

## Scope

Build a system that:

- Accepts a JSON input with `property_id` and `photos[]`.
- Emits a JSON output with top-level `photos`, `spaces`, `property`, and
  `warnings`.
- Includes exactly one output record for every input photo ID.
- Groups photos into displayable spaces.
- Chooses a listing hero photo and per-space hero photos.
- Classifies simple per-photo fields such as room role, condition, image
  quality, and capture source.
- Includes a validator and sample run command.
- Includes a benchmark or evaluation report against your own labeled sample set.

You may use heuristics, embeddings, open-source models, hosted VLM APIs, or a
hybrid approach. If you use hosted APIs, document cost, latency, and how you
would avoid running expensive models on every photo in production.

## Out Of Scope

- Do not use private Covent data.
- Do not commit secrets, API keys, or scraped private images.
- Do not claim production accuracy without evidence.
- Do not hardcode the sample output.

## Public Schema Contract

Use `schema/polaris_image_2_public_contract.json` as the minimum output
contract. You may add fields, but the required fields must remain valid.

## Sample Data

This repo includes tiny synthetic contract examples under `sample-data/`. Those
examples are for validating JSON shape and ID coverage; the image URLs are
placeholders by design.

For model or visual-quality work, add your own public-safe image set using
public-domain/licensed photos, generated images, or images you have permission
to use. Document the source and license/permission in your submission.

## Acceptance Criteria

A strong approved submission must:

- Run from a clean checkout with documented commands.
- Produce valid JSON for the sample input.
- Pass the provided validator:
  `python3 projects/polaris-image-2-photo-intelligence/scripts/validate_output.py --input <input.json> --output <output.json>`.
- Preserve exact input photo IDs with no missing, duplicate, or hallucinated
  references.
- Include at least one non-trivial full-tour sample output.
- Include a short evaluation report with metrics and failure analysis.
- Explain whether your system is cheap-path only, VLM-only, or hybrid routed.
- Explain cost and latency expectations.
- Include a writeup with what you would improve with more time.

## Suggested Milestones

1. Parser and validator.
2. Per-photo classifier baseline.
3. Space grouping and hero selection.
4. Full JSON compiler.
5. Evaluation report and writeup.
6. Optional VLM/router layer for hard cases.

## Submission Location

Place code submissions under:

```text
projects/polaris-image-2-photo-intelligence/submissions/<your-github-handle>/
```

Your folder should include:

- `README.md`
- `WRITEUP.md`
- runnable source code
- sample outputs
- validation or benchmark commands

## Data Safety

Do not include private Covent data, customer images, scraped private images,
teacher labels, internal prompts, Slack exports, API keys, or local-machine
paths. Public submissions should be reproducible using only public-safe inputs.
