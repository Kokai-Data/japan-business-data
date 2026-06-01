# japan-public-business-intelligence

Vertical plugin: shared skills and MCP connector for Japanese public business intelligence (gBizINFO, J-Grants, kokai evidence index).

## Install

```bash
claude plugin install japan-public-business-intelligence@japan-business-data
```

## What it provides

- **13 skills** covering (Sprint 7p-2 で 2 件追加、計 13):
  - gBizINFO entity / company search (2 skills)
  - J-Grants subsidy search / detail (2 skills)
  - **国税庁 法人番号 公表 Web-API: corporate-number lookup + name search (2 skills、Sprint 7p-2 追加)**
  - Evidence citation (1 skill)
  - 4 high-level prompts (due-diligence, subsidy-fit, subsidy-landscape, competitor-brief)
  - 2 common skills (authority-strip-formatter, shigyo-boundary-disclaimer)
- **5 slash commands**: `/meeting-prep`, `/subsidy-fit`, `/due-diligence`, `/competitor-brief`, `/subsidy-landscape`
- **1 MCP server connection**: `kokai` at `https://mcp.kokai.ai/functions/v1/mcp-server`

## 3-Source Authority Chain (Sprint 7p-2 完成)

Kokai のデータ Authority Chain は **3 つの公式 SoT** で構成:

1. **gBizINFO (経済産業省)** — Japanese company business intelligence (financials, employees, certifications, shareholders)
2. **J-Grants (中小企業庁 + デジタル庁)** — Japanese government subsidies (eligibility, deadlines, max amount, application forms)
3. **国税庁 法人番号 公表 Web-API** — Authoritative corporate-number master + change history (社名変更 / 移転 / 合併 / 解散)

→ AI agent が引用する際に「3 公式 SoT 統合」と明示可能、AI HYVE / N-3 等の単一 source 競合との明確 differentiator。

## Boundary

Kokai outputs are signal / 確認材料 / context, not decisions. Final 適格性 / 申請可否 / legal judgment requires a certified Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士).

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
