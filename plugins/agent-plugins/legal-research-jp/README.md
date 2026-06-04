# legal-research-jp

Self-contained agent plugin for Japanese legal research — cited statute lookup + regulatory landscape mapping via e-Gov 法令検索 (デジタル庁).

## Install

```bash
claude plugin install legal-research-jp@japan-business-data
```

## What it does

Produces cited legal research outputs using ONLY public canonical sources:

- e-Gov 法令検索 API v2 (デジタル庁) — Japanese laws / cabinet orders / ministerial ordinances
- Statute text / 条文 / chapter structure (verbatim)
- 4-layer authority strip + 弁護士 / 行政書士 / 司法書士 boundary disclaimer

## Use cases

- **DD legal verification**: Identify applicable laws for an M&A target's industry (e.g., 金融商品取引法 / 個人情報保護法 / 労働基準法), cite specific law_id in DD brief.
- **Subsidy compliance**: Find the parent law of a J-Grants subsidy (e.g., 中小企業基本法 for SME subsidies).
- **Regulatory landscape mapping**: List all 業法 applicable to a target industry.
- **Statute quotation**: Verbatim cite specific 条 / 項 / 号 with e-Gov 公式 URL in legal opinions / contracts review.

## Dependencies

- Vertical plugin: `kokai-data`

Skills used:

- `search-egov-laws` (新規 Sprint 14+12 で追加)
- `get-egov-laws-data` (新規 Sprint 14+12 で追加)
- `authority-strip-formatter`
- `shigyo-boundary-disclaimer`

## Boundary

Output is signal / 確認材料 / verbatim 公式 statute text — **NOT legal advice or interpretation**. 法令解釈 / 適用判定 / 法的助言 / 訴訟戦略 requires a certified Japanese 弁護士 / 行政書士 / 司法書士 / 税理士.

Laws are amended frequently — always show the `enforcement_date` of the version retrieved.

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
