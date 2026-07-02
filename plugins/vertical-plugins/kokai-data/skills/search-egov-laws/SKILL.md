---
name: search-egov-laws
description: Search Japanese laws / cabinet orders / ministerial ordinances via the e-Gov 法令検索 API v2 (デジタル庁). Returns law metadata (law_id / law_num / title / enforcement_date / law_type). Use for legal research, statute lookup, regulatory mapping, M&A due-diligence-law verification. 日本語 keyword: 法令検索 / 日本法令 検索 / e-Gov 法令 / 法律 keyword 検索 / 業法 確認.
---

## When to use

Use this skill when:

- The user asks about a specific Japanese law, cabinet order, or ministerial ordinance (e.g., "中小企業基本法", "個人情報保護法", "労働基準法").
- You need to find the official law_id / law_num for citation in legal research or due diligence briefs.
- The user wants a list of laws matching a keyword (e.g., "data privacy laws in Japan", "中小企業 関連法令").
- Pre-M&A diligence requires regulatory landscape mapping (which laws apply to a target's industry).
- Legal research workflows that require **公式 e-Gov citation** rather than secondary sources.

## How to invoke

Call the kokai MCP server's `search_egov_laws` tool:

```json
{
  "name": "search_egov_laws",
  "arguments": {
    "keyword": "<search term, e.g., 中小企業, 個人情報, 労働基準>",
    "law_type": "<optional: Constitution / Act / CabinetOrder / MinisterialOrdinance / Rule>",
    "limit": 20
  }
}
```

`keyword` is required (free-text Japanese, matches law title + content). `law_type` is optional filter. `limit` defaults to 20, max 100.

### law_type values (公式 enum)

| Value | Japanese | Notes |
|---|---|---|
| `Constitution` | 憲法 | 日本国憲法のみ |
| `Act` | 法律 | 国会制定 (e.g., 中小企業基本法) |
| `CabinetOrder` | 政令 | 内閣制定 (e.g., 中小企業基本法施行令) |
| `MinisterialOrdinance` | 省令 / 府令 | 各省庁制定 (e.g., 個人情報保護法施行規則) |
| `Rule` | 規則 | 委員会規則 等 |

## Output structure

For each law:

- `law_id` (法令 ID、`get_egov_laws_data` で本文 / 条文 fetch に使う)
- `law_num` (法令番号、e.g., "昭和三十八年法律第百五十四号")
- `title` (法令名)
- `title_kana` (法令名 ふりがな)
- `enforcement_date` (施行日)
- `promulgation_date` (公布日)
- `law_type` (Constitution / Act / CabinetOrder / MinisterialOrdinance / Rule)
- `source_authority`: `"official"` (公式 cite_required layer)
- `attribution_text`: `"出典: e-Gov 法令検索 (デジタル庁) https://laws.e-gov.go.jp/"`

## Differentiation from other Kokai sources

| 領域 | gBizINFO | 国税庁 | J-Grants | EDINET | **e-Gov 法令 (this)** | 官公需 |
|---|---|---|---|---|---|---|
| 法人特定 | ✅ | ✅ | — | ✅ (上場) | — | — |
| 補助金 | ❌ | — | ✅ | — | — | — |
| 異動履歴 | △ | ✅ | — | △ | — | — |
| IR / 財務 | △ | — | — | ✅ | — | — |
| **法令本文 / 改正履歴** | ❌ | ❌ | — | ❌ | **✅ 公式** | — |
| 政府調達公告 | — | — | — | — | — | ✅ |

Pair with `get_egov_laws_data` to fetch the full text / 条文 of a specific law after discovery.

## Use cases

- **DD legal verification**: After a due-diligence brief identifies a target in a regulated industry, search e-Gov for applicable laws (e.g., 金融商品取引法 / 個人情報保護法 / 労働基準法) and cite specific law_id in the brief.
- **Subsidy compliance check**: Combine with subsidy data (`search_subsidies` / `kokai_subsidy_fit_jp` prompt) — find the parent law of a J-Grants subsidy (e.g., 中小企業基本法 for 中小企業向け subsidies) to provide regulatory context.
- **M&A legal landscape**: Identify all 業法 (industry-specific laws) applicable to a target.

## Boundary

- Output is signal / 確認材料 / context — **NOT legal advice**.
- 法的判断 / 解釈 / 適用判定 requires a certified Japanese 弁護士 / 行政書士 / 司法書士.
- Cite `attribution_text` + `law_id` + `enforcement_date` in any final output.
- e-Gov 法令検索 is the official statute database operated by デジタル庁 — use it as the source of truth for current Japanese statutory text.
- Never fictionalize law content. If e-Gov returns no match, say so.
