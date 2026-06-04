# kokai-data

Vertical plugin: shared skills and MCP connector for Japanese public business intelligence (gBizINFO, J-Grants, kokai evidence index).

## Install

```bash
claude plugin install kokai-data@kokai
```

## What it provides

- **19 skills** covering:
  - gBizINFO entity / company search (2 skills)
  - J-Grants subsidy search / detail (2 skills)
  - 国税庁 法人番号 公表 Web-API: corporate-number lookup + name search (2 skills)
  - **EDINET (金融庁): document search / fetch + company IR tracker (3 skills)**
  - **e-Gov 法令検索 (デジタル庁): law search + full statute fetch (2 skills)**
  - **官公需情報ポータル (中小企業庁): procurement portal search (1 skill)**
  - Evidence citation (1 skill)
  - 4 high-level prompts (due-diligence, subsidy-fit, subsidy-landscape, competitor-brief)
  - 2 common skills (authority-strip-formatter, shigyo-boundary-disclaimer)
- **7 slash commands**: `/proposal-prep`, `/subsidy-fit`, `/due-diligence`, `/competitor-brief`, `/subsidy-landscape`, `/legal-research`, `/procurement-discovery` (各日本語 alias あり)
- **1 MCP server connection**: `kokai` at `https://mcp.kokai.ai/functions/v1/mcp-server`

## 6-Source Authority Chain

Kokai のデータ Authority Chain は **6 つの公式 SoT** で構成:

1. **gBizINFO (経済産業省)** — Japanese company business intelligence (financials, employees, certifications, shareholders)
2. **J-Grants (中小企業庁 + デジタル庁)** — Japanese government subsidies (eligibility, deadlines, max amount, application forms)
3. **国税庁 法人番号 公表 Web-API** — Authoritative corporate-number master + change history (社名変更 / 移転 / 合併 / 解散)
4. **EDINET (金融庁)** — listed-company IR (有価証券報告書 / 四半期 / 大量保有 / TOB / 内部統制)
5. **e-Gov 法令検索 (デジタル庁)** — Japanese statutory law (full statute text + 条文 structure)
6. **官公需情報ポータル (中小企業庁)** — government procurement (Call for Tender notices, 公告)

→ AI agent が引用する際に「6 公式 SoT 統合」と明示可能、AI HYVE / N-3 等の単一 source 競合との明確 differentiator。

## Boundary

Kokai outputs are signal / 確認材料 / context, not decisions. Final 適格性 / 申請可否 / legal judgment requires a certified Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士).

## License

Apache License 2.0 — see repo root [LICENSE](../../../LICENSE).
