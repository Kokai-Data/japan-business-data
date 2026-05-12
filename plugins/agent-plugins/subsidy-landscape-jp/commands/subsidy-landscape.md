---
name: subsidy-landscape
description: /subsidy-landscape <industry-or-use-purpose> — invoke the subsidy-landscape-jp agent
---

# /subsidy-landscape

Invoke the `subsidy-landscape-jp-agent` for an industry or use-purpose theme.

See [agent system prompt](../agents/subsidy-landscape-jp-agent.md) for full workflow.

Usage:

- `/subsidy-landscape <industry-or-use-purpose>` — direct

Returns: top-N subsidies brief with cited J-Grants source URLs + landscape summary + 4-layer authority strip + 士業 boundary disclaimer.

## Boundary

Output is **landscape signal** — sector / strategy theme brief, NOT individual application advice. For company-specific fit analysis, use `/subsidy-fit`. Final 適格性 / 申請可否 verification requires a certified Japanese 士業.
