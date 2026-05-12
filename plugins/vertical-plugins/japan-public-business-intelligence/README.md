# japan-public-business-intelligence

Vertical plugin: shared skills and MCP connector for Japanese public business intelligence (gBizINFO, J-Grants, kokai evidence index).

## Install

```bash
claude plugin install japan-public-business-intelligence@kokai-for-public-business-intelligence-jp
```

## What it provides

- **11 skills** covering:
  - gBizINFO entity / company search (2 skills)
  - J-Grants subsidy search / detail (2 skills)
  - Evidence citation (1 skill)
  - 4 high-level prompts (due-diligence, subsidy-fit, subsidy-landscape, competitor-brief)
  - 2 common skills (authority-strip-formatter, shigyo-boundary-disclaimer)
- **5 slash commands**: `/meeting-prep`, `/subsidy-fit`, `/due-diligence`, `/competitor-brief`, `/subsidy-landscape`
- **1 MCP server connection**: `kokai` at `https://mcp.kokai.ai/functions/v1/mcp-server`

## Boundary

Kokai outputs are signal / 確認材料 / context, not decisions. Final 適格性 / 申請可否 / legal judgment requires a certified Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士).

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
