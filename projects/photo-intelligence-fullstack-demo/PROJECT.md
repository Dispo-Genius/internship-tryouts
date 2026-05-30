# Photo Intelligence Full-Stack Demo

## Summary

Build a full-stack demo where a user can upload a property photo set, run a
photo intelligence pipeline, and review the resulting schema-valid output in a
polished UI.

This is the highest-signal tryout for full-stack engineers. It combines product
taste, frontend state handling, backend/API design, file handling, model or
heuristic inference, validation, and deployment judgment.

## Problem

Property teams need a practical way to turn messy photo tours into structured
property intelligence. The hard part is not only classification. The product
also needs a good upload flow, clear processing states, a trustworthy output
viewer, validation errors, and an API boundary that could grow into production.

Your task is to build a working demo that feels credible end to end.

## Required User Flow

1. User creates or opens a property analysis session.
2. User uploads multiple property photos.
3. App shows upload/processing state.
4. Backend runs a photo classification pipeline.
5. Backend returns schema-valid JSON and a validation report.
6. Frontend renders:
   - photo gallery
   - per-photo labels
   - grouped spaces
   - selected listing hero
   - validator status and warnings
   - raw JSON viewer or download

## Scope

Build a full-stack app with:

- A frontend upload/review workspace.
- A backend API for session creation, upload, analysis, and result retrieval.
- Local file storage or object-storage-compatible abstraction.
- A cheap-path classifier, heuristic classifier, open-source model, or optional
  hosted VLM integration.
- Deterministic validation for photo ID coverage and schema shape.
- Sample seed data and at least one saved demo result.
- Clear loading, empty, error, processing, success, and invalid-output states.
- A concise deployment note.

The pipeline does not need to beat production accuracy. It does need to be
runnable, inspectable, and honest.

## Plus Points

These are not required, but they are strong signals:

- Drag-and-drop upload with thumbnail previews.
- Batch analysis for 10+ photos.
- A queue/job abstraction instead of blocking the request thread.
- A confidence or uncertainty display.
- Side-by-side raw JSON and visual review.
- A validator report with actionable error messages.
- A hybrid design where cheap classification handles easy photos and a VLM route
  is reserved for hard/uncertain cases.
- A deployed demo link.
- Basic auth or share-token protection for demo sessions.
- Tests around API contracts and validator behavior.

## Out Of Scope

- No private Covent data.
- No customer images.
- No secrets or paid API keys committed to the repo.
- No requirement to replicate Covent internals.
- No requirement to use the real Polaris Image 2 training labels.

## Acceptance Criteria

A strong approved submission must:

- Run from a clean checkout with documented setup commands.
- Let a reviewer upload multiple images and run analysis locally.
- Preserve every uploaded photo ID exactly once in the output.
- Produce output matching the public contract from
  `projects/polaris-image-2-photo-intelligence/schema/polaris_image_2_public_contract.json`.
- Show validator success/failure in the UI.
- Include backend validation that rejects or flags malformed outputs.
- Include at least one automated test for the validator or API contract.
- Include a `WRITEUP.md` covering architecture, API design, data/model choices,
  deployment plan, limitations, and next steps.

## Suggested API Shape

You can choose your own implementation, but this is a good starting point:

```text
POST /api/sessions
POST /api/sessions/:id/photos
POST /api/sessions/:id/analyze
GET  /api/sessions/:id/result
GET  /api/sessions/:id/photos/:photoId
```

## Suggested Tech

Use what you know well. Good options:

- Next.js full-stack app
- FastAPI + React/Vite
- Node/Express + React/Vite
- SQLite or file-backed JSON storage
- Local filesystem storage for images

Document tradeoffs if your stack would need changes for production.

## Sample Inputs

Use public-safe photos only. Good sources:

- self-created test photos
- generated images
- public-domain/licensed property/interior photos

Document source and permission. Include a small seed set if redistribution is
allowed; otherwise include a script or instructions to reproduce your sample.

## Submission Location

Place code submissions under:

```text
projects/photo-intelligence-fullstack-demo/submissions/<your-github-handle>/
```

Your folder should include:

- `README.md`
- `WRITEUP.md`
- runnable frontend/backend source code
- sample output JSON
- validation/test commands
- screenshots or demo video link

## Data Safety

Use public-safe images only. Do not include private Covent data, customer
photos, teacher labels, internal prompts, Slack exports, API keys, service
tokens, or local-machine paths.
