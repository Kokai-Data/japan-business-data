# subsidy-fit-jp

Self-contained agent plugin for 3-axis subsidy fit signal (Japanese company × J-Grants subsidy pair).

## Install

```bash
claude plugin install subsidy-fit-jp@japan-business-data
```

## What it does

Computes 3-axis fit signal (regional / industry / scale) using ONLY public canonical sources:

- gBizINFO entity (company prefecture / industry / employees / capital)
- J-Grants subsidy detail (target_area_search / industry / target_number_of_employees / use_purpose)
- Kokai 4-layer authority strip
- 士業 boundary disclaimer

## Dependencies

- Vertical plugin: `kokai-data`

Skills used:

- `gbizinfo-company-search` / `gbizinfo-entity-lookup`
- `jgrants-subsidy-detail`
- `kokai-subsidy-fit-prompt`
- `authority-strip-formatter`
- `shigyo-boundary-disclaimer`

## Advanced / Beta (default では使わない)

`prepare_subsidy_eligibility_context` (kokai MCP server gated beta tool、x-kokai-beta-client-id header 必須) は、default workflow から除外。advanced user / gated beta access user は、kokai support に問い合わせ後 explicit に invoke 可能。default install では activate しない。

## Boundary

Output is **signal / 確認材料 / context**, NOT eligibility judgment. Final 適格性 / 申請可否 verification requires a certified Japanese 士業 (行政書士 / 中小企業診断士).

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
