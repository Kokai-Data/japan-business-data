---
name: edinet-document-fetch
description: Download a single EDINET disclosure document binary (PDF / XBRL ZIP / CSV) by docID. Returns a time-limited signed URL from Kokai's private storage proxy. Use after `search_edinet_documents` to retrieve the actual filing for citation or analysis. 日本語 keyword: EDINET 文書取得 / 開示書類 ダウンロード / 有価証券報告書 binary 取得 / 開示文書 PDF 取得.
---

## When to use

Use this skill when:

- You have a `docID` from a prior `search_edinet_documents` call and need the actual document binary.
- The user wants to view a specific 有価証券報告書 PDF, 四半期報告書 XBRL, or 大量保有報告書 file.
- You're building a citation with a direct link to the source document.
- XBRL parsing or financial-statement extraction (manual / external tool) is the next step.

## How to invoke

Call the kokai MCP server's `get_edinet_document` tool:

```json
{
  "name": "get_edinet_document",
  "arguments": {
    "docID": "<8-char docID from search_edinet_documents>",
    "type": "2"
  }
}
```

### `type` parameter (FSA 公式 §3-2-1)

| Code | Format | Content |
|---|---|---|
| `1` | ZIP | 提出本文書 + 監査報告書 (**XBRL 含む**) |
| `2` | PDF | 提出本文書 + 監査報告書 (PDF 形式、最も読みやすい) |
| `3` | ZIP | 代替書面・添付文書 |
| `4` | ZIP | 英文ファイル |
| `5` | ZIP | CSV (XBRL→CSV 変換版) |

### Size caps (Phase 1 limits)

- PDF (type=2): **50 MB**
- ZIP (type=1/3/4/5): **100 MB**

Oversize → tool returns `edinet_document_too_large` error with `sizeBytes` / `maxBytes` literal (Phase 2 で大型書類対応検討)。

## Output structure

```json
{
  "docID": "S1000001",
  "type": "2",
  "format": "pdf",
  "storageBucket": "edinet-documents",
  "storagePath": "S1000001/2/<timestamp>.pdf",
  "signedUrl": "https://...supabase.co/storage/v1/object/sign/edinet-documents/...",
  "sizeBytes": 1234567,
  "source_authority": "official",
  "attribution_text": "出典: 金融庁 EDINET",
  "boundary": {
    "signedUrlSource": "kokai_storage_proxy",
    "signedUrlTtlSeconds": 3600,
    "sourceAuthority": "edinet_official",
    "kokaiModification": "none",
    "canonicalSourceUrl": "https://disclosure2.edinet-fsa.go.jp"
  }
}
```

**Important**: `signedUrl` is a **Kokai Storage proxy** with a **1-hour TTL**. The actual document content is unmodified from EDINET (`kokaiModification: "none"`). For canonical citation in long-lived documents, link to `canonicalSourceUrl` (EDINET 閲覧サイト) instead.

## Boundary

- Output is signal / 確認材料 / context — **NOT investment advice**.
- The signed URL is for **read access only** (Kokai does not redistribute beyond the original requester).
- 投資判断 / 法的判断 / 税務判断 requires a certified financial advisor / 公認会計士 / 弁護士 / 税理士.
- EDINET disclosure 内容 はそのまま信頼できるが、Kokai は contents を解釈・要約していない (要約 / 推論は AI agent 側責任で `source_authority: ai_summary / ai_estimate` 4-layer authority strip に明示)。
- Public records only.
