# competitor-brief-jp

Self-contained agent plugin for 3-tier competitor brief (Japanese company).

## Install

```bash
claude plugin install competitor-brief-jp@kokai
```

## What it does

Produces a 3-tier competitor brief (overview / scale / certifications) for a Japanese company using ONLY gBizINFO public canonical sources:

- Overview tier: business summary, products, founding date, headquarters
- Scale tier: employees, capital, sales, total assets, growth trajectory
- Certifications tier: えるぼし / くるみん / ISO / 業種別認証
- Kokai 4-layer authority strip
- 士業 boundary disclaimer

## Use cases

- Competitive landscape research
- Peer comparison
- M&A target benchmarking

## Dependencies

- MCP server: `kokai` (`https://mcp.kokai.ai/functions/v1/mcp-server`) — bundled via this plugin's `.mcp.json`, works standalone (no other plugin required). Optional: set the `KOKAI_MCP_CLIENT_ID` env var to any unique string for a personal anonymous identity instead of the shared default (see the `kokai-data` plugin README).

Skills used:

- `gbizinfo-entity-lookup` / `gbizinfo-company-search`
- `kokai-competitor-brief-prompt`
- `authority-strip-formatter`
- `shigyo-boundary-disclaimer`

## Boundary

Output is signal / 確認材料 / context — NOT a decision. M&A valuation / market share judgment / strategy decisions require professional advisors (financial advisor / consultant / 公認会計士).

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
