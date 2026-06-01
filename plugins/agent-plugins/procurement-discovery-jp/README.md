# procurement-discovery-jp

Self-contained agent plugin for Japanese government procurement (Call for Tender, 公告) discovery via 官公需情報ポータル (中小企業庁).

## Install

```bash
claude plugin install procurement-discovery-jp@japan-business-data
```

## What it does

Discovers Japanese government procurement notices (bid opportunities) using ONLY public canonical sources:

- 官公需情報ポータル (中小企業庁) REST + XML API
- Project names / 公告名, issuing organizations / 発注機関, industry categories / 業種分類, bid procedure types / 入札方式
- 4-layer authority strip + 行政書士 / 中小企業診断士 / 弁護士 boundary disclaimer

## Phase 1 vs Phase 2 promise

**Phase 1 (this plugin)** — Call for Tender (CFT) discovery only:
- ✅ project names + issuing organizations + industry categories + CFT issue dates + procedure types

**Phase 2 (future, NOT in this plugin)** — these are NOT in the official API:
- ❌ 受注実績 / 落札結果 / 落札価格 / 予定価格 / supplier 履歴

For Phase 2 data, consult a commercial procurement DB (e.g., 帝国データバンク 入札情報) or hire a 中小企業診断士 / 行政書士.

## Use cases

- **B2G sales lead discovery**: Sales team identifies fresh procurement opportunities by industry + region for proactive outreach.
- **M&A market mapping**: When evaluating a target selling to government, discover potential customer pipeline (which agencies issue RFPs in target's space).
- **Subsidy + procurement combo**: Companies receiving J-Grants IT 導入補助金 might also bid on related government IT contracts.
- **Industry trend signal**: Aggregate procurement notices by category to spot government spending trends.

## Dependencies

- Vertical plugin: `japan-public-business-intelligence`

Skills used:

- `search-procurement-portal` (新規 Sprint 14+13 で追加)
- `gbizinfo-company-search` (発注機関 cross-ref)
- `nta-corporate-name-search` (法人特定 of issuing organization's affiliated 法人)
- `authority-strip-formatter`
- `evidence-citation-builder`
- `shigyo-boundary-disclaimer`

## Boundary

Output is **signal / 確認材料 / context** — NOT bid advice, eligibility judgment, or 適格性 verification. 入札判断 / 適格性判断 / 法的判断 requires certified Japanese 行政書士 / 中小企業診断士 / 弁護士.

Phase 1 scope is enforced by the official API — never fabricate 受注実績 / 落札結果 / 価格 signal in agent outputs.

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
