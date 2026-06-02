---
name: proposal-prep
description: /proposal-prep <13-digit 法人番号 OR company name> — generate a 1-page Japanese company proposal brief
---

# /proposal-prep

Run the `proposal-prep-jp` agent workflow on the provided Japanese company.

Argument: 13-digit 法人番号 (corporate number) OR company name.

If a company name is provided, the agent will call `search_company` first to confirm the corporate number with the user.

Usage:

- `/proposal-prep <13-digit 法人番号>` (direct, fastest)
- `/proposal-prep <company name>` (search candidates, then user confirms)

The brief includes:

- Header: company name + 法人番号
- 事業概要 (cited from gBizINFO records)
- 直近トピック (cited from J-Grants subsidies, certifications, awards)
- 支援ニーズ仮説 (cited from subsidy landscape signals)
- 4-layer authority strip
- 士業 boundary disclaimer
