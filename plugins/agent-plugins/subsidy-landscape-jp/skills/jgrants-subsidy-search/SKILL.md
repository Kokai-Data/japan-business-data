---
name: jgrants-subsidy-search
description: Search J-Grants public registry for Japanese government subsidies by keyword (industry / theme / use purpose, 2+ chars). Returns matches with id, title, target area, deadline, and max amount. 日本語 keyword: 補助金検索 / 補助金 一覧 / 補助金スキャン / 業種別補助金 / J-Grants 検索.
---

## When to use

Use this skill when:

- The user asks about subsidies relevant to an industry, theme, or use purpose.
- You need to identify candidate subsidies before drilling into details.

## How to invoke

Call the kokai MCP server's `search_subsidies` tool:

```json
{
  "name": "search_subsidies",
  "arguments": {
    "keyword": "<industry / theme / use purpose, 2+ chars>",
    "industry": "<optional industry code>",
    "use_purpose": "<optional use purpose>",
    "target_area_search": "<optional prefecture>"
  }
}
```

## Output format

For each subsidy, present:

- J-Grants subsidy ID
- Title
- Target area (prefecture / national)
- Deadline range (acceptance_start / acceptance_end)
- Max amount (subsidy_max_limit)
- Institution name (公募元)
- Source URL (cite_required)

## Constraints

- The `target_area_search` field returns regional subsidies; clarify with the user whether they want national-only, prefecture-specific, or all.
- Subsidies returned are signal / 確認材料 — fit / 適格性 must be verified separately (e.g. via the kokai MCP server's `kokai_subsidy_fit_jp` prompt).

## Boundary

- Output is signal / 確認材料 / context — NOT eligibility judgment.
- Final 申請可否 / 適格性 verification requires a certified Japanese 士業 (行政書士 / 中小企業診断士).
