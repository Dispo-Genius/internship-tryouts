# Property Insights Review UI

## Summary

Build a polished frontend workspace for reviewing property intelligence signals.
The app should help an operator inspect a property, compare conflicting signals,
and decide what needs follow-up.

This is a public, mock-data tryout version of the kind of operational UI Covent
builds. The goal is to show frontend taste, state handling, accessibility,
component discipline, and evidence-backed delivery.

## Problem

Property intelligence products often combine signals from listings, photos,
transaction history, maps, owner records, and model-generated summaries. Those
signals can conflict. A good internal UI should make the conflict obvious,
preserve source evidence, and help a human make a confident decision quickly.

Your task is to build a compact review workspace that feels like a real product,
not a landing page. It should be dense, calm, scannable, and useful for repeated
operator work.

## Scope

Build a frontend app that includes:

- A property header with address, status, estimated value, and confidence.
- A signal review panel with at least 6 mock signals across categories such as
  valuation, ownership, sale history, property condition, photo quality, and map
  marker formatting.
- A conflict or anomaly state for at least 2 signals.
- A source/evidence drawer or detail panel for a selected signal.
- Review actions such as `Approve`, `Needs follow-up`, and `Dismiss`.
- Filtering or segmented controls for signal status/category.
- Loading, empty, error, and reviewed states.
- Responsive layouts for desktop and mobile.

Use mock data only. No backend is required.

## Out Of Scope

- No auth.
- No real Covent data.
- No paid APIs.
- No private maps, customer screenshots, or internal screenshots.
- No backend persistence requirement. Local state is enough.

## Acceptance Criteria

A strong approved submission must:

- Run from a clean checkout with documented setup and run commands.
- Render a usable first screen with the review workspace itself, not a marketing
  page.
- Use realistic mock data and make conflicting signals easy to spot.
- Include loading, empty, error, selected-detail, and reviewed states.
- Provide keyboard-accessible controls and visible focus states.
- Avoid layout overlap at common mobile and desktop widths.
- Include a short visual QA section with screenshots or screen recording links.
- Include a writeup explaining component structure, state model, and design
  tradeoffs.

## Suggested Stack

Any modern frontend stack is acceptable. We care more about judgment than
framework choice. Good options:

- Next.js or Vite React
- TypeScript
- Tailwind or a small tokenized CSS system
- Playwright or Vitest/Testing Library for focused checks

## Suggested Mock Signal Shape

You can use your own schema, but this shape is enough:

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
- How you handled responsive layout.
- What accessibility checks you performed.
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
