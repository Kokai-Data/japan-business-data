---
name: legal-research
description: /legal-research <keyword | law_id> — search Japanese laws (e-Gov 法令検索) or fetch full statute text
---

# /legal-research

Search Japanese laws / cabinet orders / ministerial ordinances via e-Gov 法令検索 (デジタル庁) — or fetch full statute text + chapter / article structure for a specific law_id.

Usage:

- `/legal-research <keyword>` — search by keyword (e.g., `/legal-research 中小企業`, `/legal-research 個人情報保護`)
- `/legal-research <law_id>` — fetch full statute (e.g., `/legal-research 338AC0000000154`)

Returns cited list of candidate laws OR verbatim 条文 + 4-layer authority strip + 弁護士 / 行政書士 / 司法書士 boundary disclaimer.

Calls `search-egov-laws` and / or `get-egov-laws-data` Skills (公式 e-Gov API v2, デジタル庁).

## Boundary

Output is **verbatim 公式 statute text** — NOT legal advice / interpretation / 適用判定. 法令解釈 / 法的助言 / 訴訟戦略 requires certified Japanese 弁護士 / 行政書士 / 司法書士.
