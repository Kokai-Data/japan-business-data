---
name: get-egov-laws-data
description: Fetch the full text / 条文 / chapter structure of a specific Japanese law from e-Gov 法令検索 API v2 (デジタル庁). Use after search-egov-laws to retrieve actual statute body, article-by-article. Returns structured law content (chapters / articles / paragraphs) with public 公式 citation.
---

## When to use

Use this skill when:

- You have a `law_id` from `search-egov-laws` and need the actual statute text.
- The user asks "what does Article X of the Y Act say?" (e.g., "個人情報保護法 第15条").
- DD / legal research requires verbatim citation of statute text.
- You need to quote specific provisions in a due diligence brief or subsidy-fit analysis.
- Regulatory mapping requires the full chapter / article structure (法令の章立て).

## How to invoke

Call the kokai MCP server's `get_egov_laws_data` tool:

```json
{
  "name": "get_egov_laws_data",
  "arguments": {
    "law_id": "<law_id from search-egov-laws, e.g., 338AC0000000154>"
  }
}
```

`law_id` is required (obtained from `search-egov-laws` results).

## Output structure

- `law_id` (input echoed)
- `law_num` (法令番号)
- `title` (法令名)
- `enforcement_date` / `promulgation_date`
- `chapters` (array of 章): each with `chapter_num`, `chapter_title`, `articles` (array of 条)
- Each article (条): `article_num`, `article_title`, `paragraphs` (array of 項), `items` (号)
- `revision_info` (改正履歴 summary if available)
- `source_authority`: `"official"` (公式 cite_required)
- `attribution_text`: `"出典: e-Gov 法令検索 (デジタル庁) https://laws.e-gov.go.jp/law/<law_id>"`
- `source_url`: direct e-Gov URL for the law's HTML view

## Workflow pattern (paired with search-egov-laws)

```
1. User asks about a Japanese law topic
   ↓
2. search-egov-laws (keyword search) → list of candidate laws (10-20)
   ↓
3. User / agent selects one law_id
   ↓
4. get-egov-laws-data (law_id) → full statute text + structure
   ↓
5. Quote specific 条 / 項 / 号 with attribution_text + source_url
```

## Differentiation from third-party sources

e-Gov 法令検索 is the **only official statutory database** for Japanese law. Third-party services (jurist sites, commentary platforms) provide interpretation but not 公式 text. When AI agent needs cite_required statute text:

- ✅ e-Gov (this skill) — 公式, current, デジタル庁 maintained
- ❌ Wikipedia / commentary sites — not cite_required for legal opinion

## Boundary

- Output is verbatim statute text + structure — **NOT legal advice or interpretation**.
- 法令解釈 / 適用判定 / 法的助言 requires a certified Japanese 弁護士 / 行政書士 / 司法書士.
- Cite `attribution_text` + `law_id` + 条番号 + `enforcement_date` for any quoted provisions.
- Laws are amended frequently — always show the `enforcement_date` of the version retrieved.
- Never fictionalize statute text. If a law has been repealed (廃止), the API may not return it; in that case, note this and recommend lawyer consultation for historical research.
