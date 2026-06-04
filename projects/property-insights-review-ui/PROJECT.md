# Property Insights Review UI

## Summary

Build a polished frontend workspace for reviewing property intelligence cases.
The app should help an operator move through a queue, inspect a property,
compare conflicting signals, review source evidence, and decide what needs
follow-up.

This is the frontend/product-taste tryout. It is intentionally separate from
the Polaris photo/video intelligence project: no model pipeline is required.
The goal is to show UI judgment, information hierarchy, state handling,
accessibility, component discipline, and evidence-backed delivery.

## Problem

Property intelligence products combine signals from listings, photos,
transaction history, maps, owner records, valuation models, risk notes, and
operator-entered context. Those signals often disagree. A good internal UI
should make the conflict obvious, preserve source evidence, and help a human
make a confident decision quickly.

Your task is to build a compact review workspace that feels like a real product,
not a landing page. It should be dense, calm, scannable, and useful for repeated
operator work. The first screen should be the working review queue itself.

## Scope

Build a frontend app that includes:

- A review queue with multiple property cases.
- A property header with address, priority, status, estimated value, confidence,
  and key facts.
- A signal review panel with categories such as valuation, ownership, sale
  history, condition, photos, maps, risk, and listing notes.
- A conflict or anomaly state for at least 3 signals.
- A source/evidence drawer or detail panel for a selected signal.
- Review actions such as `Approve`, `Needs follow-up`, `Dismiss`, and
  `Escalate`.
- Filtering or segmented controls for signal status/category.
- Queue-level summary counts for open conflicts, reviewed cases, and priority.
- A compact activity or decision trail showing what the reviewer changed.
- Loading, empty, error, and reviewed states.
- Responsive layouts for desktop and mobile.

Use mock data only. No backend is required. The included
`mock-data/property_review_cases.json` file is the baseline dataset; you can
reshape it in your app as long as the same review scenarios remain visible.

## Out Of Scope

- No auth.
- No real Covent data.
- No paid APIs.
- No private maps, customer screenshots, or internal screenshots.
- No backend persistence requirement. Local state is enough.
- No requirement to use the PhotoTours fixtures from the Polaris project.

## Acceptance Criteria

A strong approved submission must:

- Run from a clean checkout with documented setup and run commands.
- Render a usable first screen with the review queue itself, not a marketing
  page or generic dashboard.
- Use the included multi-case mock data and make conflicting signals easy to
  spot.
- Let a reviewer switch between cases without losing local review state.
- Show source evidence clearly for each selected signal.
- Provide review actions that visibly update status, counts, or the decision
  trail.
- Include loading, empty, error, selected-detail, and reviewed states.
- Include category/status filters that are useful on the provided dataset.
- Provide keyboard-accessible controls and visible focus states.
- Avoid layout overlap at common mobile and desktop widths.
- Include visual QA screenshots or a short screen recording across desktop and
  mobile widths.
- Include a writeup explaining the review workflow, component structure, state
  model, accessibility checks, and design tradeoffs.

## Bonus Points

This project should reward taste and operator empathy. Strong bonus signals:

- Exceptional information hierarchy: the reviewer can identify the property,
  biggest conflict, source evidence, and next action within seconds.
- Dense but calm design: compact enough for repeated internal work without
  looking cluttered or decorative.
- Thoughtful conflict visualization: severity, source disagreement, and
  recommended action are visible without excessive reading.
- Fast workflow: keyboard-friendly navigation, useful filters, persisted local
  state, and low-friction review actions.
- Strong responsive behavior: mobile is reorganized for review, not merely
  squeezed.
- Design-system discipline: consistent tokens, spacing, focus states, and
  reusable components.
- Visual QA: before/after notes, screenshots, and explicit viewport checks.

## Suggested Stack

Any modern frontend stack is acceptable. We care more about judgment than
framework choice. Good options:

- Next.js or Vite React
- TypeScript
- Tailwind or a small tokenized CSS system
- Playwright or Vitest/Testing Library for focused checks

## Suggested Mock Signal Shape

The provided `mock-data/property_review_cases.json` file includes multiple
cases. You can use your own schema, but each signal should preserve this kind of
information:

```json
{
  "id": "sale-price-conflict",
  "category": "sale_history",
  "title": "Duplicate same-price sale events",
  "status": "conflict",
  "severity": "high",
  "summary": "Two adjacent sale events share the same price but disagree on date.",
  "evidence": [
    { "label": "Sale event A", "value": "$305,000 on 2022-03-01" },
    { "label": "Sale event B", "value": "$305,000 on 2022-03-02" }
  ],
  "recommendedAction": "Verify canonical closing date before showing timeline."
}
```

## Writeup

Your `WRITEUP.md` should explain:

- What user workflow you optimized for.
- How you structured components and state.
- How your review actions and filters work.
- How you handled responsive layout.
- What accessibility checks you performed.
- Where your design intentionally chose density, hierarchy, or restraint.
- What you would add with another week.

## Submission Location

Place code submissions under:

```text
projects/property-insights-review-ui/submissions/<your-github-handle>/
```

Your folder should include:

- `README.md`
- `WRITEUP.md`
- runnable source code
- screenshots or screen recording links
- validation/test commands

## Data Safety

Use mock data only. Do not include private Covent data, customer screenshots,
internal screenshots, Slack exports, secrets, API keys, or local-machine paths.
