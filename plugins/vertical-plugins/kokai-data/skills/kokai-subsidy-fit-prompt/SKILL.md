---
name: kokai-subsidy-fit-prompt
description: Use the kokai MCP server's `kokai_subsidy_fit_jp` prompt to prepare a 3-axis fit signal (regional / industry / scale) for a Japanese company x subsidy pair. 日本語 keyword: 補助金マッチ プロンプト / 補助金 fit frame / 3 軸 fit framework.
---

## When to use

Use this skill when:

- The user has a target Japanese company AND a target J-Grants subsidy.
- You want a structured fit signal (NOT eligibility judgment) on whether the subsidy may fit the company.

## How to invoke

Request the kokai MCP server's `kokai_subsidy_fit_jp` prompt:

```json
{
  "name": "kokai_subsidy_fit_jp",
  "arguments": {
    "corporate_number": "<13-digit 法人番号>",
    "subsidy_id": "<J-Grants subsidy ID>"
  }
}
```

The prompt returns thinking instructions + embedded resources + 3-axis fit analysis framework.

## Output format

Present the 3-axis fit signal:

1. **Regional fit**: Does the subsidy's target_area_search include the company's prefecture?
2. **Industry fit**: Does the subsidy's industry tag align with the company's industry?
3. **Scale fit**: Does the company's employee count / capital fit the subsidy's target_number_of_employees range?

For each axis, output `fit` / `partial fit` / `no fit` / `insufficient data` with cited reasoning.

## Boundary (critical)

- Output is **signal / 確認材料 / context — NOT eligibility judgment**.
- Final 適格性 / 申請可否 verification requires a certified Japanese 士業 (行政書士 / 中小企業診断士).
- The kokai MCP server's `prepare_subsidy_eligibility_context` tool (gated beta, x-kokai-beta-client-id header required) is **NOT** called by this skill in default workflow. It is referenced only in advanced / beta appendices.
