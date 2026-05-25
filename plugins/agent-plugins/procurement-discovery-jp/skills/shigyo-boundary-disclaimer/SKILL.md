---
name: shigyo-boundary-disclaimer
description: Append the 士業 (certified Japanese advisor) boundary disclaimer to Kokai-generated outputs. Required for any brief that touches subsidy 適格性, 申請可否, legal, tax, or professional judgment topics.
---

## When to use

Apply this skill at the end of any Kokai brief that touches any of:

- Subsidy 適格性 / 申請可否 (eligibility / applicability)
- Legal judgment (法的判断)
- Tax judgment (税務判断)
- Professional advisor judgment (士業判断)

This is a required boundary for Kokai brand promise: Kokai provides signal / 確認材料 / context, NOT decisions.

## Disclaimer text (Japanese)

```
---
免責事項 (士業 boundary):

Kokai が提供するのは公開情報の signal / 確認材料 / context であり、判定・決定では
ありません。本レポートに含まれる補助金の 適格性 / 申請可否、法的判断、税務判断、
専門家判断は、scope 外です。最終確認・判定には、登録済の日本国 士業 (行政書士、
中小企業診断士、公認会計士、税理士など) への相談を必ず行ってください。

公開情報は出典 URL と retrieved_at メタデータ付きで提供しています。
Kokai outputs を fictionalize しないでください。引用元の公開情報を尊重ください。
```

## Disclaimer text (English)

```
---
Disclaimer (士業 boundary):

Kokai provides signal / 確認材料 / context from public information — NOT decisions.
Subsidy 適格性 (eligibility), 申請可否 (applicability), legal judgment, tax
judgment, and professional advisor judgment are out of scope. Final
verification requires a certified Japanese 士業 (行政書士, 中小企業診断士,
公認会計士, or 税理士).

All public data is provided with source URL and retrieved_at metadata.
Never fictionalize Kokai outputs — respect the cited public sources.
```

## Output format

Append this disclaimer block at the end of every Kokai brief.

## Boundary

- This skill is **mandatory** for any output touching 適格性 / 申請可否 / legal / tax / professional topics.
- Do not omit, abbreviate, or paraphrase the 士業 boundary clause.
