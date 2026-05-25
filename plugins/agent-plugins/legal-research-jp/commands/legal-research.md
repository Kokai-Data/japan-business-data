---
name: legal-research
description: /legal-research <keyword | law_id> — invoke the legal-research-jp agent for Japanese statute search or full-text fetch
---

# /legal-research

Invoke the `legal-research-jp-agent` for Japanese legal research from e-Gov 法令検索 (デジタル庁).

See [agent system prompt](../agents/legal-research-jp-agent.md) for full workflow.

Usage:

- `/legal-research <keyword>` — search Japanese laws by keyword (e.g., `/legal-research 中小企業`, `/legal-research 個人情報保護`)
- `/legal-research <law_id>` — fetch full statute text + chapter / article structure for a specific law (e.g., `/legal-research 338AC0000000154`)

Returns: cited list of candidate laws OR verbatim statute text + 4-layer authority strip + 弁護士 / 行政書士 / 司法書士 boundary disclaimer.

## Boundary

Output is **verbatim 公式 statute text** — NOT legal advice, interpretation, or 適用判定. 法令解釈 / 法的助言 / 訴訟戦略 requires certified Japanese 弁護士 / 行政書士 / 司法書士.
