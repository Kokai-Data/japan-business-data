---
name: competitor-brief
description: /competitor-brief <13-digit 法人番号> — generate a 3-tier competitor brief (overview / scale / certifications) for a Japanese company
---

# /competitor-brief

Run the `competitor-brief-jp` agent workflow on the provided Japanese company.

Argument: `<corporate_number>` — 13-digit 法人番号

Use cases:

- Competitive landscape research
- Peer comparison
- M&A target benchmarking

The brief presents 3 tiers:

1. **Overview tier**: business summary, products, founding date, headquarters
2. **Scale tier**: employee count, capital, sales, total assets, growth trajectory
3. **Certifications tier**: えるぼし / くるみん / ISO / 業種別認証 等

All data cited from gBizINFO records (source_url + retrieved_at).

## Boundary

- Output is signal / 確認材料 / context — NOT a decision.
- M&A valuation / market share judgment / strategy decisions require professional advisors.
