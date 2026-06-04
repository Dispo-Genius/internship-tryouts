# Judging Rubric

We judge submissions by the artifact first. Time spent is useful context, but it
is not the main score.

## What To Include In A Submission

Every submission should include:

- runnable artifact
- setup, run, validation, and benchmark commands
- `WRITEUP.md`
- self-reported start time, finish time, and approximate focused hours
- screenshots and a walkthrough video when relevant
- cost and deployment report for any backend, model, or hosted-service project

Self-reported time helps us understand pace and scope judgment. We do not need
perfect time tracking. A good-faith estimate is enough.

## General Scorecard

| Category | Weight | What We Look For |
| --- | ---: | --- |
| Correctness and output quality | 30 | Does it do the requested job? Are outputs valid, useful, and accurate enough for the stated approach? |
| End-to-end completeness | 20 | Can we run it from a clean checkout? Are the main flows implemented rather than described? |
| Code quality and maintainability | 20 | Clear structure, typed/validated boundaries, readable code, small modules, good naming, no brittle hardcoding. |
| Product judgment and UX | 15 | Does the experience feel useful, polished, and matched to the user workflow? Are edge states handled? |
| Validation, tests, and evidence | 10 | Focused tests, validator output, benchmark notes, screenshots/video, and honest failure analysis. |
| Communication and writeup | 5 | Clear tradeoffs, what was cut, what would come next, and how AI/tools were used. |

## Bonus Points

Bonus points do not rescue a broken core submission. They help distinguish
strong, complete submissions from excellent ones.

| Bonus Area | Max | What Earns It |
| --- | ---: | --- |
| Design taste and product polish | 10 | A calm, dense, operator-ready UI; strong visual hierarchy; responsive layouts; thoughtful empty/loading/error states; no marketing-page filler. |
| Video intelligence ambition | 10 | Meaningful room/space chaptering, timestamp quality, video-to-photo sync, frame/evidence inspection, and useful handling of ambiguous segments. |
| Model and routing judgment | 8 | Clear cheap-path versus VLM/video-model routing, confidence thresholds, fallback behavior, latency/cost tradeoffs, and no unnecessary paid calls. |
| Production readiness | 8 | Credible deploy plan, storage/background-job design, observability, secrets handling, retry/idempotency strategy, and realistic cost model. |
| Evaluation depth | 8 | Labeled sample set, metrics, failure analysis, confusion examples, and comparison against a simple baseline. |
| Communication artifact quality | 6 | Clear walkthrough video, screenshots, architecture diagram, and concise writeup that makes the candidate's reasoning easy to review. |

Maximum bonus: 50 points.

## Strong Signals

- The project runs with the documented commands.
- Validation failures are understandable and actionable.
- The output is not hardcoded to the sample.
- The candidate can explain why they chose the architecture.
- The candidate can explain how they would deploy it and what it would cost to
  run.
- The UI handles loading, empty, error, and success states.
- The candidate reports limitations honestly.
- The candidate keeps private data and secrets out of the repo.

## Red Flags

- The project does not run.
- The core flow is mostly a mock or a static screenshot.
- The output is hardcoded to the sample input.
- Photo IDs are dropped, duplicated, or invented.
- The UI overlaps or breaks on normal viewport sizes.
- Secrets, private data, local paths, or private links are committed.
- The writeup hides uncertainty or makes unsupported accuracy claims.

## Project-Specific Notes

### Polaris Image 2 Photo Intelligence

Primary judging questions:

- Can a reviewer upload or load multiple property photos and run analysis?
- Does the output preserve every input photo ID exactly once?
- Does it pass the public validator?
- Does the UI expose validator status, warnings, and raw output clearly?
- Does it chapter walkthrough videos into useful room/space segments?
- Does it sync video chapters with the still photos and grouped spaces?
- Are per-photo labels plausible and useful?
- Are spaces and hero photos reasonable?
- Are generated titles and descriptions clear enough for a reviewer or listing
  workflow?
- Is there a real evaluation report, not just a happy-path sample?
- Is the system honest about whether it is cheap-path, image/video-model-only,
  or hybrid?
- Does the submission include a walkthrough video, deployment plan, and cost
  report?

Extra credit:

- Excellent design taste: the UI feels like a real internal review tool, with
  scannable density, strong hierarchy, tasteful media presentation, and complete
  interaction states.
- Strong video-model work: reliable chapter boundaries, meaningful room labels,
  synced still-photo evidence, and clear handling of uncertain or mixed-room
  clips.
- Meaningful benchmark set and confusion/error analysis.
- Queued/job-style processing.
- Deployed demo.
- Confidence or uncertainty display.
- Hybrid cheap classifier plus VLM/video-model routing design.
- Latency and cost estimate grounded in the selected architecture.
- Deterministic compiler/validator separation.
- Frame extraction or embedding-based alignment between video segments and
  still photos.

### Property Insights Review UI

Primary judging questions:

- Is the review workflow obvious within the first screen?
- Are conflicts and source evidence easy to scan?
- Are filters, detail states, and review actions complete?
- Does it work on desktop and mobile?
- Are controls keyboard-accessible?

Extra credit:

- strong design taste and visual polish without sacrificing density
- screenshot or video QA across viewports
- clean component/state architecture
- strong empty/error/loading/reviewed states

## Time Spent

We ask candidates to report:

- start date/time
- finish date/time
- approximate focused hours
- any reused prior work
- major AI/tooling assistance

Fast is good only when the artifact is good. Slow is acceptable when the
candidate shows depth, learning, and strong judgment. The time report is context
for calibration, not a stopwatch contest.
