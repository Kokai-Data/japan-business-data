---
name: due-diligence
description: /due-diligence <13-digit 法人番号> — invoke the due-diligence-jp agent
---

# /due-diligence

Invoke the `due-diligence-jp-agent` for a Japanese company.

See [agent system prompt](../agents/due-diligence-jp-agent.md) for full workflow.

Usage:

- `/due-diligence <corporate_number>` — direct

Returns: cited 1-page DD brief with 4-layer authority strip + 士業 boundary disclaimer.

## Boundary

Output is signal / 確認材料 / context — NOT a decision. DD conclusions / investment decisions / legal judgment require certified Japanese 士業.
