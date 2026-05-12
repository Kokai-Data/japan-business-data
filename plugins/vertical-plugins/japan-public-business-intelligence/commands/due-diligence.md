---
name: due-diligence
description: /due-diligence <13-digit 法人番号> — generate a 1-page Japanese company due diligence brief from public canonical sources
---

# /due-diligence

Run the `due-diligence-jp` agent workflow on the provided Japanese company.

Argument: `<corporate_number>` — 13-digit 法人番号

Use cases:

- M&A target screen
- Pre-investment research
- Pre-meeting client brief

The brief uses ONLY public canonical sources via the kokai MCP server (gBizINFO entity + evidence refs) and includes:

- 4-layer authority strip (公式 / Kokai normalized / AI summary / AI estimate)
- cite_required for the top 2 layers
- 士業 expert-review boundary message

## Boundary

- Output is signal / 確認材料 / context — NOT a decision.
- DD conclusions / investment decisions / legal judgment require certified Japanese 士業.
