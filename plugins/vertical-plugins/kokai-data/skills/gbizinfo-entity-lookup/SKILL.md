---
name: gbizinfo-entity-lookup
description: Look up a Japanese company's detailed profile (financials, capital, employees, certifications) from gBizINFO via the kokai MCP server. Use when you have a 13-digit 法人番号. 日本語 keyword: 法人情報取得 / 企業情報検索 / 法人番号で企業調査 / 商談相手調査 / 経営情報取得 / 会社プロファイル取得.
---

## When to use

Use this skill when:

- The user provides a 13-digit Japanese 法人番号 (corporate number).
- You need company details: financials (sales / income / capital / total assets), employee count, certifications (えるぼし / くるみん / etc.), major shareholders, workplace data.

## How to invoke

Call the kokai MCP server's `get_entity_profile` tool with the 13-digit corporate number:

```json
{
  "name": "get_entity_profile",
  "arguments": {
    "corporate_number": "<13-digit 法人番号>",
    "include_categories": true
  }
}
```

## Constraints (important)

- gBizINFO `categories.subsidy` and `categories.procurement` fields are mostly null for Japanese companies — use this for entity identification (法人番号 / name / location), NOT for subsidy history.
- For subsidy data, use the `search_subsidies` + `get_subsidy_detail` MCP tools instead.
- The result includes the ACBS 4-layer authority strip; the gBizINFO data is `公式` (official) layer and `cite_required`.

## Output format

Cite gBizINFO records by their `source_url` and `retrieved_at` metadata in your final output.

## Boundary

- Output is signal / 確認材料 / context — NOT a decision.
- For 法人適格性 / 申請可否 / legal judgment, recommend a certified Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士).
