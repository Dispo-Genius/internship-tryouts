# Judging Rubric

We judge submissions by the artifact first. Time spent is useful context, but it
is not the main score.

## What To Include In A Submission

Every submission should include:

- runnable artifact
- setup, run, validation, and benchmark commands
- `WRITEUP.md`
- self-reported start time, finish time, and approximate focused hours
- screenshots, video, or deployed demo when relevant

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

## Strong Signals

- The project runs with the documented commands.
- Validation failures are understandable and actionable.
- The output is not hardcoded to the sample.
- The candidate can explain why they chose the architecture.
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

- Does the output preserve every input photo ID exactly once?
- Does it pass the public validator?
- Are per-photo labels plausible and useful?
- Are spaces and hero photos reasonable?
- Is there a real evaluation report, not just a happy-path sample?
- Is the system honest about whether it is cheap-path, VLM-only, or hybrid?

Extra credit:

- meaningful benchmark set
- confusion/error analysis
- latency and cost estimate
- deterministic compiler/validator separation

### Property Insights Review UI

Primary judging questions:

- Is the review workflow obvious within the first screen?
- Are conflicts and source evidence easy to scan?
- Are filters, detail states, and review actions complete?
- Does it work on desktop and mobile?
- Are controls keyboard-accessible?

Extra credit:

- screenshot or video QA across viewports
- clean component/state architecture
- strong empty/error/loading/reviewed states

### Photo Intelligence Full-Stack Demo

Primary judging questions:

- Can a reviewer upload multiple images and run analysis?
- Are frontend, backend, storage, analysis, and validation boundaries clear?
- Does the output match the public contract?
- Does the UI expose validator status and raw output?
- Is the implementation credible as a production seed?

Extra credit:

- queued/job-style processing
- deployed demo
- confidence/uncertainty display
- hybrid cheap classifier plus VLM routing design
- API contract tests

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
