---
name: subsidy-landscape
description: /subsidy-landscape <industry-or-use-purpose> — scan top-N Japanese subsidies for an industry / use purpose theme
---

# /subsidy-landscape

Run the `subsidy-landscape-jp` agent workflow for a given industry or use-purpose theme.

Argument: `<industry>` or `<use_purpose>` (at least one required)

Use case: sector / strategy theme landscape brief (NOT individual application advice).

Output:

- Top-N subsidies with title / target area / deadline / max amount / cite_required source URL
- 3-axis signal per subsidy: regional / industry / scale fit
- Landscape summary: ranking, regional distribution, authority signals

## Boundary

- Output is **landscape signal**, NOT individual application advice.
- For company-specific fit analysis, use `/subsidy-fit` command.
- Final 適格性 / 申請可否 verification requires a certified Japanese 士業.
