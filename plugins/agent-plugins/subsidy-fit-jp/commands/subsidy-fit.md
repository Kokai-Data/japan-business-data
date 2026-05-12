---
name: subsidy-fit
description: /subsidy-fit <13-digit 法人番号> <J-Grants subsidy_id> — invoke the subsidy-fit-jp agent
---

# /subsidy-fit

Invoke the `subsidy-fit-jp-agent` for a Japanese company × subsidy pair.

See [agent system prompt](../agents/subsidy-fit-jp-agent.md) for full workflow.

Usage:

- `/subsidy-fit <corporate_number> <subsidy_id>` — direct

Returns: 3-axis fit signal (regional / industry / scale) with cited reasoning + 4-layer authority strip + 士業 boundary disclaimer.

## Boundary

Output is **signal / 確認材料 / context**, NOT eligibility judgment. Final 適格性 / 申請可否 requires a certified Japanese 士業.
