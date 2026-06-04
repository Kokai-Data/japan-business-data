---
name: kokai-competitor-brief-prompt
description: Use the kokai MCP server's `kokai_competitor_corporate_brief_jp` prompt to prepare a 3-tier competitor brief (overview / scale / certifications) for a Japanese company. 日本語 keyword: 競合 brief プロンプト / 競合調査 frame / 競合 brief framework.
---

## When to use

Use this skill when:

- The user asks for competitive landscape research, peer comparison, or M&A target benchmarking.
- You have a 13-digit 法人番号 (corporate number) for the target company.

## How to invoke

Request the kokai MCP server's `kokai_competitor_corporate_brief_jp` prompt:

```json
{
  "name": "kokai_competitor_corporate_brief_jp",
  "arguments": {
    "corporate_number": "<13-digit 法人番号>"
  }
}
```

The prompt returns thinking instructions + embedded resources for 3-tier brief.

## Output format

Present the 3 tiers:

1. **Overview tier**: business summary, products, founding date, headquarters
2. **Scale tier**: employee count, capital, sales, total assets, growth trajectory
3. **Certifications tier**: えるぼし / くるみん / ISO / 業種別認証 等

Cite gBizINFO records by source_url + retrieved_at metadata.

## Boundary

- Output is signal / 確認材料 / context — NOT a decision.
- M&A valuation / market share judgment / strategy decisions require professional advisors (financial advisor / consultant / 公認会計士).
