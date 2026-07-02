# proposal-prep-jp

Self-contained agent plugin for preparing 1-page Japanese company proposal briefs.

## Install

```bash
claude plugin install proposal-prep-jp@kokai
```

## What it does

Generates a 1-page brief on a target Japanese company using:

- gBizINFO entity profile (cited)
- J-Grants subsidy landscape signals (cited)
- Kokai 4-layer authority strip
- 士業 boundary disclaimer

## Dependencies

- MCP server: `kokai` (`https://mcp.kokai.ai/functions/v1/mcp-server`) — bundled via this plugin's `.mcp.json`, works standalone (no other plugin required). Optional: set the `KOKAI_MCP_CLIENT_ID` env var to any unique string for a personal anonymous identity instead of the shared default (see the `kokai-data` plugin README).

Skills used:

- `gbizinfo-entity-lookup`
- `gbizinfo-company-search`
- `kokai-due-diligence-prompt`
- `kokai-subsidy-landscape-prompt`
- `authority-strip-formatter`
- `shigyo-boundary-disclaimer`

## Boundary

Output is signal / 確認材料 / context — NOT a decision. Subsidy 適格性 / 申請可否 / legal judgment requires a certified Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士).

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
