# subsidy-landscape-jp

Self-contained agent plugin for Japanese subsidy landscape scan (sector / strategy theme).

## Install

```bash
claude plugin install subsidy-landscape-jp@japan-business-data
```

## What it does

Scans top-N Japanese government subsidies for a given industry or use_purpose theme using J-Grants public registry. Each subsidy cited by J-Grants URL.

Output includes:

- Top-N subsidies list with title / target area / deadline / max amount
- Landscape summary (regional distribution / authority signals / theme signals)
- Kokai 4-layer authority strip
- 士業 boundary disclaimer

## Use cases

- Sector / strategy theme landscape brief
- Industry subsidy intelligence
- Cross-prefecture subsidy comparison

## Dependencies

- Vertical plugin: `kokai-data`

Skills used:

- `jgrants-subsidy-search`
- `kokai-subsidy-landscape-prompt`
- `authority-strip-formatter`
- `shigyo-boundary-disclaimer`

## Boundary

Output is **landscape signal** — sector / strategy theme brief, NOT individual application advice. For company-specific fit analysis, use the `subsidy-fit-jp` agent.

Final 適格性 / 申請可否 verification requires a certified Japanese 士業 (行政書士 / 中小企業診断士).

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
