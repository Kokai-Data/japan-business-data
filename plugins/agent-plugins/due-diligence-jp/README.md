# due-diligence-jp

Self-contained agent plugin for 1-page Japanese company due diligence briefs.

## Install

```bash
claude plugin install due-diligence-jp@japan-business-intelligence
```

## What it does

Produces a 1-page DD brief on a target Japanese company using ONLY public canonical sources:

- gBizINFO entity (financials, capital, employees, certifications, shareholders)
- Evidence refs (cite_required source URLs)
- Kokai 4-layer authority strip
- 士業 boundary disclaimer

## Dependencies

- Vertical plugin: `japan-public-business-intelligence`

Skills used:

- `gbizinfo-entity-lookup` / `gbizinfo-company-search`
- `evidence-citation-builder`
- `kokai-due-diligence-prompt`
- `authority-strip-formatter`
- `shigyo-boundary-disclaimer`

## Boundary

Output is signal / 確認材料 / context — NOT a decision. DD conclusions / investment decisions / legal judgment require certified Japanese 士業 (公認会計士 / 弁護士 / 行政書士).

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
