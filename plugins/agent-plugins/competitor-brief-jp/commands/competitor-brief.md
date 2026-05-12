---
name: competitor-brief
description: /competitor-brief <13-digit 法人番号> — invoke the competitor-brief-jp agent
---

# /competitor-brief

Invoke the `competitor-brief-jp-agent` for a Japanese company.

See [agent system prompt](../agents/competitor-brief-jp-agent.md) for full workflow.

Usage:

- `/competitor-brief <corporate_number>` — direct

Returns: 3-tier competitor brief (overview / scale / certifications) with cited reasoning + 4-layer authority strip + 士業 boundary disclaimer.

## Boundary

Output is signal / 確認材料 / context — NOT a decision. M&A valuation / market share judgment / strategy decisions require professional advisors.
