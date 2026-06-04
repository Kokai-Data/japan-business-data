---
name: edinet-document-search
description: Search Japanese securities disclosure documents (有価証券報告書 / 四半期 / 半期 / 臨時 / 大量保有 / 公開買付 / 内部統制 等) from FSA EDINET v2 API. Filter by date, docTypeCode, edinetCode, or 法人番号. Use for IR research, M&A signal tracking, listed company DD prep. 日本語 keyword: EDINET 文書検索 / 有価証券報告書 検索 / 開示書類 検索 / 金商法開示 検索.
---

## When to use

Use this skill when:

- The user wants to see what disclosures a listed Japanese company filed recently.
- You need a date-bounded list of all 有価証券報告書 / 四半期報告書 / 大量保有報告書 / 公開買付届出書 etc. filed on a specific day or in a 90-day window.
- The user provides a 法人番号 (13-digit corporate number) and you want to confirm whether the company is listed (= has EDINET disclosures) before pulling further IR details.
- You're tracking 訂正報告書 / 取下書 events for signal monitoring.
- Pre-meeting research where past 開示履歴 matters (IR depth, governance signal).

## How to invoke

Call the kokai MCP server's `search_edinet_documents` tool:

```json
{
  "name": "search_edinet_documents",
  "arguments": {
    "date": "<YYYY-MM-DD>",
    "dateFrom": "<YYYY-MM-DD>",
    "dateTo": "<YYYY-MM-DD>",
    "docTypeCodes": ["120", "140", "350"],
    "edinetCode": "<E12345>",
    "corporateNumber": "<13-digit 法人番号>",
    "limit": 50
  }
}
```

Pass `date` for a single day OR `dateFrom` + `dateTo` for a range (max 90 days). `docTypeCodes`, `edinetCode`, `corporateNumber` are optional filters (combine freely). `corporateNumber` is auto-resolved to `edinetCode` via 30-day lookback (max 90).

### Main docTypeCode (FSA 公式)

| Code | Document |
|---|---|
| 030 | 有価証券届出書 |
| 120 | **有価証券報告書 (annual)** |
| 130 | 訂正有価証券報告書 |
| 140 | **四半期報告書** |
| 150 | 訂正四半期報告書 |
| 160 | 半期報告書 |
| 180 | **臨時報告書 (extraordinary event)** |
| 235 | **内部統制報告書 (J-SOX)** |
| 240 | **公開買付届出書 (TOB)** |
| 350 | **大量保有報告書 (>5% holder)** |
| 360 | 訂正大量保有報告書 |

Full code list: 公式仕様書 ESE140206 別紙1 (`https://disclosure2dl.edinet-fsa.go.jp/guide/static/disclosure/download/ESE140327.xlsx`)

## Output structure

For each document:

- `docID` (8 chars、書類管理番号、`get_edinet_document` で本体 download に使う)
- `edinetCode` (E12345 形式、提出者)
- `secCode` (証券コード、e.g. "7203")
- `JCN` (法人番号 13 桁、国税庁 SoT 直結)
- `filerName` (提出者商号)
- `docTypeCode` + `docDescription`
- `submitDateTime` / `periodStart` / `periodEnd`
- `xbrlFlag` / `pdfFlag` / `csvFlag` (本体取得 type 選択 hint)
- `withdrawalStatus` / `docInfoEditStatus` / `disclosureStatus` (修正・取下げ・不開示 signal)
- `legalStatus` (1=縦覧中 / 2=延長期間中 / 0=閲覧期間満了)
- `source_authority`: "official" (公式 cite_required layer)
- `attribution_text`: "出典: 金融庁 EDINET (https://disclosure2.edinet-fsa.go.jp)"

## Differentiation from other Kokai sources

| 領域 | gBizINFO | 国税庁 (NTA) | J-Grants | **EDINET (this)** |
|---|---|---|---|---|
| 法人特定 | ✅ (商業企業) | ✅ (全法人 master) | — | ✅ (上場企業のみ) |
| 補助金 | ❌ | — | ✅ | — |
| 異動履歴 | △ | ✅ | — | △ (訂正報告書) |
| **IR / 財務 / 株主** | △ (公開財務のみ) | ❌ | — | **✅ official** |
| **大量保有 disclosure** | ❌ | ❌ | — | **✅ official** |
| **TOB / M&A signal** | ❌ | ❌ | — | **✅ official** |

Pair with `edinet-company-ir-tracker` for company-level cluster view, or with `get_edinet_document` to download the binary file.

## Boundary

- Output is signal / 確認材料 / context — **NOT investment advice**.
- 投資判断 / 法的判断 / 税務判断 requires a certified financial advisor / 公認会計士 / 弁護士 / 税理士.
- Cite `attribution_text` + `submitDateTime` + EDINET source in any final output.
- Never fictionalize. If EDINET returns 0 documents for a corporate number, the company is likely not listed (or has no disclosures in the lookback window).
- Public records only — EDINET data is open disclosure, not insider information.
