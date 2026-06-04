---
name: edinet-company-ir-tracker
description: Get recent EDINET disclosures for one Japanese company (by 法人番号 OR edinetCode) clustered into Kokai signal overlays — annual / quarterly / extraordinary / TOB / large-shareholding / governance / event. Auto-resolves 法人番号 → EDINET code. Use for M&A target diligence, investment research, listed-company DD prep. 日本語 keyword: 上場企業 IR / IR 追跡 / EDINET 開示 / 有価証券報告書 取得 / 上場企業 disclosure 追跡.
---

## When to use

Use this skill when:

- The user provides a 法人番号 (13-digit) and you want to see if the company is listed + all their recent IR activity in one call.
- You're prepping for an M&A target call and need a fast cluster view of annual / quarterly / TOB / large-shareholding / governance disclosures.
- Investor / analyst use case: monitor a portfolio company's filings clustered by signal type.
- You want **Kokai signal overlay** (not raw EDINET timeline) — clustered into actionable groups instead of a flat list.

## How to invoke

Call the kokai MCP server's `get_edinet_company_disclosures` tool:

```json
{
  "name": "get_edinet_company_disclosures",
  "arguments": {
    "corporateNumber": "<13-digit 法人番号>",
    "edinetCode": "<E12345 form, alternative to corporateNumber>",
    "lookbackDays": 30,
    "limit": 50
  }
}
```

- **`corporateNumber` OR `edinetCode`** (one required). If both, `edinetCode` wins (skips resolver).
- **`lookbackDays`**: default `30`, max `90` (auto-clamped). Phase 2 will extend to 365 once EDINET code master is imported.
- **`limit`**: default 50, max 100.

## Output structure

```json
{
  "corporateNumber": "...",
  "edinetCode": "E12345",
  "filerName": "...",
  "resolveStatus": "resolved",
  "documents": [/* all recent docs, submitDateTime desc */],
  "signal": {
    "annualReports": [/* 有価証券報告書 (docTypeCode=120, 130) */],
    "quarterlyReports": [/* 四半期 (140, 150) + 半期 (160, 170) */],
    "largeHolderReports": [/* 大量保有 (350, 360) */],
    "tobReports": [/* TOB (240-320) */],
    "correctionReports": [/* 訂正 (130, 150, 170, 190, etc.) */],
    "governanceReports": [/* 内部統制 (235, 236) */],
    "eventDisclosures": [/* 臨時報告書 (180, 190) */]
  },
  "source_authority": "official",
  "attribution_text": "出典: 金融庁 EDINET"
}
```

### `resolveStatus` values

- `"resolved"`: 法人番号 → EDINET code 解決成功、上場企業確認
- `"unresolved"`: 法人番号 を渡したが lookback 内 IR なし or 上場企業でない (empty signal、200 で graceful degrade)
- `"skipped"`: edinetCode を直接渡したので resolver は skip

## Kokai signal overlay (raw EDINET API では出ない layer)

EDINET の raw `/documents.json` は 1 日単位の flat list を返すだけ。本 skill は:

1. **法人番号 → EDINET code auto resolve** (国税庁 法人番号 SoT 直結、JCN field match)
2. **lookback 期間内の全 IR 書類を 1 query で集約** (caller が 30 日 loop する必要なし)
3. **docTypeCode で signal cluster 分類** (M&A target diligence の判断 layer)
4. **訂正報告書 / 不開示 / 取下げ event signal** (governance / 信頼性 signal)
5. **4 公的 SoT cross-reference 可能** (国税庁 法人番号 → gBizINFO 企業 profile → J-Grants 補助金 → EDINET IR)

## Differentiation from other Kokai sources + skills

| Use case | 適切な skill |
|---|---|
| 法人特定 + 業界 / 地域 / 規模 | `gbizinfo-company-search` |
| 法人 master + 異動履歴 (全法人) | `nta-corporate-number-lookup` |
| 補助金交付実績 + 適格性 | `jgrants-subsidy-search` + `subsidy-fit-jp` agent |
| **上場企業 IR 全書類 timeline + signal cluster** | **`edinet-company-ir-tracker` (this)** |
| EDINET 単日書類一覧 (date 別 query) | `edinet-document-search` (本 skill より low-level) |
| EDINET 書類本体 binary | `edinet-document-fetch` (this の後続 step) |

## Boundary

- Output is signal / 確認材料 / context — **NOT investment advice**.
- 投資判断 / 法的判断 / 税務判断 requires a certified financial advisor / 公認会計士 / 弁護士 / 税理士.
- 4-layer authority strip: EDINET data is L1 `source_authority: "official"` (公式 cite_required)、Kokai 側 signal cluster は L2 `kokai_normalized`、AI agent 要約は L3 `ai_summary`、推論は L4 `ai_estimate`。
- `resolveStatus: "unresolved"` は「上場企業でない可能性が高い」signal だが、確定情報ではない (lookback 短い + EDINET 提出タイミングの偶然で false negative ありえる)。確定には 90 日 lookback or `edinet-document-search` で直接確認。
- Public records only — EDINET data is open disclosure, not insider information.
