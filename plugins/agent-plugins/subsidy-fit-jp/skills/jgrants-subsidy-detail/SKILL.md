---
name: jgrants-subsidy-detail
description: Get detailed J-Grants subsidy information (full eligibility criteria, deadlines, max amount, application form URLs) by subsidy_id from `jgrants-subsidy-search`. 日本語 keyword: 補助金詳細 / 補助金情報 取得 / J-Grants 詳細 / subsidy_id で詳細取得.
---

## When to use

Use this skill when:

- You have a J-Grants subsidy ID from `jgrants-subsidy-search`.
- You need full details: eligibility criteria, application forms, contact info, deadlines, max amount.

## How to invoke

Call the kokai MCP server's `get_subsidy_detail` tool:

```json
{
  "name": "get_subsidy_detail",
  "arguments": {
    "subsidy_id": "<J-Grants subsidy ID, e.g., a0WJ200000XXXXXX>"
  }
}
```

## Output format

The response includes a normalized record with:

- Subsidy title and overview
- Target eligibility (target_number_of_employees, industry, use_purpose, target_area_search)
- Subsidy rate (subsidy_rate)
- Max amount (subsidy_max_limit)
- Acceptance period (workflow[].acceptance_start_datetime / acceptance_end_datetime)
- Application documents (application_guidelines, application_form)
- Detail page URL (front_subsidy_detail_page_url) — cite_required
- Contact info (問合せ先)

## Boundary

- Output is signal / 確認材料 / context — NOT eligibility judgment.
- Application form preparation, eligibility verification, and 申請 / 適格性 judgment require a certified Japanese 士業 (行政書士 / 中小企業診断士).
- Cite the J-Grants `front_subsidy_detail_page_url` in your output.
