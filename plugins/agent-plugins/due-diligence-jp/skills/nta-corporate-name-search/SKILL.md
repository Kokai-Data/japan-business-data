---
name: nta-corporate-name-search
description: Search Japanese corporate registry by name via the National Tax Agency (国税庁) Web-API. Returns corporations with 13-digit corporate numbers. Use when gBizINFO does not have the company or for cross-validation. 日本語 keyword: 国税庁 法人名検索 / 法人番号取得 by 名前 / NTA 法人検索 / 名前から法人番号.
---

## When to use

Use this skill when:

- The user provides a Japanese company name (2+ characters).
- gBizINFO's `search_company` returned no results, or you want to cross-validate.
- You want to find corporations not registered in gBizINFO (small / newly-formed / non-METI-tracked entities).
- You need the 国税庁公式 corporate-number master view (definitive 法人番号 SoT).

## How to invoke

Call the kokai MCP server's `search_nta_corporate_name` tool:

```json
{
  "name": "search_nta_corporate_name",
  "arguments": {
    "name": "<company name, 2+ chars>",
    "prefecture": "<optional prefecture code, e.g., '13' for 東京都>",
    "kind": "<optional 法人区分, e.g., '301' for 株式会社>"
  }
}
```

### 法人区分 (kind) codes

| Code | Label |
|---|---|
| 101 | 国の機関 |
| 201 | 地方公共団体 |
| 301 | 株式会社 |
| 302 | 有限会社 |
| 303 | 合名会社 |
| 304 | 合資会社 |
| 305 | 合同会社 |
| 399 | その他の設立登記法人 |
| 401 | 国外所在の法人 等 |
| 499 | 人格のない社団等 |

## Output structure

For each result, present:

- 13-digit 法人番号
- name (商号又は名称)
- furigana (フリガナ)
- en_name (英語名称、登録ある場合のみ)
- location (都道府県 + 市区町村 + 丁目番地)
- post_code
- kind_label (法人区分 ラベル)
- process_label (現在 process status)
- assignment_date (法人番号指定年月日)
- is_latest (最新フラグ)

After identifying the target company, call the `get_nta_corporate_record` tool with the 法人番号 to get full record + change history.

## Differentiation from gBizINFO

- gBizINFO `search_company` returns business intelligence (industry / scale)
- NTA `search_nta_corporate_name` returns authoritative master data (name / address / 法人区分)
- For cross-validation: call both and compare. Disagreement signals data freshness or scope issues.

## Boundary

- Output is signal / 確認材料 / context — NOT a decision.
- Active corporations only by default (closed entities excluded via `close=0` flag).
- For dissolved / merged corporation detection, use `get_nta_corporate_record` with the 法人番号 directly.
