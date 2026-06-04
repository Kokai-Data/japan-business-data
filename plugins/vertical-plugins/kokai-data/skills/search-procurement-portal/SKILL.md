---
name: search-procurement-portal
description: Search Japanese government procurement notices (Call for Tender, 公告) from the 官公需情報ポータル (中小企業庁) REST + XML API. Phase 1 = CFT discovery only (project name, issuing organization, category, procedure type). Phase 2 (future) = awarded results, supplier history, price signals are NOT included. Use for sales lead discovery, bid opportunity research, government client targeting. 日本語 keyword: 調達公告検索 / 入札公告 検索 / 官公需 検索 / CFT 検索 / 公共調達 検索.
---

## When to use

Use this skill when:

- The user (sales / consultant / 行政書士 / 中小企業診断士) asks "what procurement notices has 〇〇 自治体 issued recently?"
- You need to discover bid opportunities by category (e.g., "システム開発", "建設", "物品調達") or by issuing organization (省庁 / 自治体).
- M&A target research requires understanding a company's potential government clients (which agencies publish RFPs in the target's industry).
- Subsidy-fit-jp follow-up: identify government procurement that complements a subsidy program.
- Pre-meeting research with a sales lead in B2G (business-to-government) space.

## How to invoke

Call the kokai MCP server's `search_procurement_portal` tool:

```json
{
  "name": "search_procurement_portal",
  "arguments": {
    "query": "<free-text keyword (項目横断), e.g., システム開発>",
    "project_name": "<公告名 partial match>",
    "organization_name": "<発注機関 partial match, e.g., 中小企業庁 or 東京都>",
    "lg_code": "<自治体コード, e.g., 130001 for 東京都>",
    "category": "<業種分類, optional>",
    "procedure_type": "<入札方式, optional: 一般競争 / 指名競争 / 随意契約>",
    "count": 20
  }
}
```

**Required** (one of): `query` / `project_name` / `organization_name` / `lg_code`. `category` and `procedure_type` are optional filters (cannot be used alone, public API constraint).

`count` defaults to 20, Kokai defensive cap = 100 (official max = 1000).

## Output structure

For each procurement notice:

- `result_id` (ResultId、internal ID)
- `key` (Key、`source_url` fallback 用)
- `project_name` (公告名)
- `organization_name` (発注機関)
- `cft_issue_date` (公告日 = Call for Tender Issue Date)
- `category` (業種分類, e.g., システム開発 / 建設 / 物品調達)
- `procedure_type` (入札方式)
- `source_url` (公告 detail page URL, fallback: `https://www.kkj.go.jp/api/?Key=<Key>`)
- `phase_scope`: `{ phase: 1, included: "...", deferred_to_phase_2: "..." }`
- `source_authority`: `"official"` (公式 cite_required layer)
- `attribution_text`: `"出典: 官公需情報ポータル (中小企業庁) https://www.kkj.go.jp"`

## Phase 1 vs Phase 2 promise (重要)

**Phase 1 (this skill)** — Call for Tender (CFT) discovery only:
- ✅ project names / 公告名
- ✅ issuing organizations / 発注機関 (中央省庁 + 自治体)
- ✅ industry categories / 業種分類
- ✅ bid procedure types / 入札方式
- ✅ CFT issue dates / 公告日

**Phase 2 (future, NOT in this skill)** — these are NOT available from the official API:
- ❌ 受注実績 (awarded results / who won)
- ❌ 落札結果 / 落札価格 (winning bid amount)
- ❌ 予定価格 (estimated/expected amount)
- ❌ supplier 履歴 (historical winners)

For Phase 2 data, AI agent must direct the user to consult a commercial procurement database (e.g., 帝国データバンク 入札情報) or hire a 中小企業診断士 / 行政書士 for manual research.

## Differentiation from other Kokai sources

| 領域 | gBizINFO | 国税庁 | J-Grants | EDINET | e-Gov 法令 | **官公需 (this)** |
|---|---|---|---|---|---|---|
| 法人特定 | ✅ | ✅ | — | ✅ (上場) | — | — |
| 補助金 (受給側) | ❌ | — | ✅ | — | — | — |
| 異動履歴 | △ | ✅ | — | △ | — | — |
| IR / 財務 | △ | — | — | ✅ | — | — |
| 法令本文 | ❌ | ❌ | — | ❌ | ✅ | — |
| **政府調達公告 (発注側)** | ❌ | ❌ | — | ❌ | — | **✅ 公式** |

Pair with `gbizinfo-company-search` (cross-ref 発注機関 → 関連企業) or with `nta-corporate-name-search` (法人特定 of issuing organization's affiliated 法人).

## Use cases

- **Sales lead discovery**: B2G sales team identifies fresh procurement opportunities by industry + region.
- **M&A target market mapping**: When evaluating a target that sells to government, discover their potential customer pipeline.
- **Subsidy + procurement combo**: A company receiving an IT 導入補助金 (J-Grants) might also bid on related government IT contracts (官公需).
- **Industry trend signal**: Aggregate procurement notices by category to spot government spending trends (e.g., increased DX 関連 RFPs in 2026).

## Boundary

- Output is signal / 確認材料 / context — **NOT bid advice or eligibility judgment**.
- 入札判断 / 適格性判断 / 法的判断 requires a certified Japanese 中小企業診断士 / 行政書士 / 弁護士.
- Cite `attribution_text` + `cft_issue_date` + `source_url` for any referenced notice.
- Phase 1 scope is enforced by the official API (受注実績 / 落札結果 / 価格 signal are not in the response body). Never fabricate these fields.
- Never claim a procurement notice's "outcome" — the API only provides notice metadata, not results.
- 官公需 portal is operated by 中小企業庁 (SME Agency) for the Japanese government public procurement system.
