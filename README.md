# Kokai for Public Business Intelligence — Japan

**AI-citable Japanese public business intelligence** for **all AI agents** — **4-source Authority Chain**: corporate registries (gBizINFO + 国税庁 法人番号 公表 Web-API), government subsidies (J-Grants), and **listed-company IR (EDINET 金融商品取引法開示書類)** with 士業 + investment-disclaimer boundary safety. **For AI builders (Claude / Cursor / Codex / OpenAI App Server / all MCP clients), Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士), investment professionals, and M&A advisors.**

This is the **Japan-market equivalent of [Anthropic's `financial-services` agent templates](https://github.com/anthropics/financial-services)**, focused on Japanese public canonical data sources. It is open source under Apache License 2.0 and packages [Kokai Data](https://kokai.ai) (an AI-citable public business intelligence MCP server) as both **a universal MCP server (for all AI clients)** and **Claude plugins + managed agents (for Anthropic ecosystem sugar)**.

## Architecture — Universal MCP server + Anthropic Plugin sugar (2 layers)

Kokai Data follows a **2-layer architecture** for AI agent ecosystem neutrality:

| Layer | What | Who can use it |
|---|---|---|
| **L1: Universal MCP server** | `https://mcp.kokai.ai/functions/v1/mcp-server` — implements MCP spec 2025-06-18 | **All MCP clients**: Claude Code / Claude Cowork / Claude Managed Agents / Claude.ai (connectors layer) / Cursor / Codex / OpenAI App Server / any custom MCP client. Setup via `.mcp.json` config (no Plugin required). |
| **L2: Anthropic Plugin sugar** (this repo) | `Kokai-Data/japan-business-intelligence` — bundles Skills, slash commands, managed-agent cookbook, and auto-registers the MCP server | **Anthropic ecosystem users**: Claude Code (CLI + Desktop App) / Claude Cowork / Claude Managed Agents. Plugin install auto-configures everything (no manual `.mcp.json` editing). |

**Non-Claude clients (Cursor / Codex / etc.) do NOT need to install this Plugin** — they connect to the MCP server directly via their own `.mcp.json` (see Path 4 below). The Plugin layer is purely Anthropic-ecosystem distribution sugar (auto-install / auto-update / Skills auto-invocation).

This dual approach matches Kokai's brand promise: **AI agent ecosystem neutral**, not tied to any single AI provider.

## Disclaimer

Kokai provides **signal / 確認材料 / context, not decisions**. Subsidy 適格性, 申請可否, legal, tax, or professional judgments are out of scope and must be verified by a certified Japanese 士業 (registered advisor: 行政書士, 中小企業診断士, 公認会計士, or 税理士). Never fictionalize company or subsidy facts — use only Kokai tool/prompt outputs and cited public sources.

## Who is this for

**This Plugin is for**:

- **AI agents / AI builders** (Claude Code / Claude Cowork / Cursor / Codex / OpenAI App Server) needing **AI-citable Japanese public business intelligence** with verifiable government sources for citation-required outputs.
- **Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士)** preparing meeting briefs, due diligence, competitor research, and subsidy fit analysis — with **automatic 士業 boundary disclaimers** that prevent AI from rendering professional judgments.
- **Investment professionals / M&A advisors** doing Japanese target diligence with **registry change history** (社名変更 / 移転 / 合併 / 解散) from 国税庁 公式 master data.
- **Government / public sector developers** building citizen-facing AI tools requiring **official source attribution** (cite_required + signal-not-decision layer).

**This Plugin is NOT for**:

- Real-time market data or pricing (use Bloomberg / Refinitiv, or [`anthropics/financial-services`](https://github.com/anthropics/financial-services) for Western markets).
- Non-Japanese companies (use `anthropics/financial-services` for that).
- Final eligibility / legal / tax / professional judgments — these always require a certified Japanese 士業.

## What's in this repo

| Category | Count | Examples |
|---|---|---|
| Agent plugins (self-contained workflows) | 5 | meeting-prep-jp, subsidy-fit-jp, due-diligence-jp, competitor-brief-jp, subsidy-landscape-jp |
| Vertical plugin (shared skill bundle + MCP connector) | 1 | japan-public-business-intelligence |
| Managed-agent cookbook (Claude Managed Agents deployment template) | 1 | kokai-due-diligence-jp |

## Agents (5 named templates)

| Agent | Function |
|---|---|
| `meeting-prep-jp` | 1-page brief for a Japanese company before a meeting (cited public data) |
| `subsidy-fit-jp` | 3-axis fit signal (regional / industry / scale) for a Japanese company × subsidy pair |
| `due-diligence-jp` | 1-page due diligence brief on a Japanese company (gBizINFO entity + evidence refs) |
| `competitor-brief-jp` | 3-tier competitor brief (overview / scale / certifications) for a Japanese company |
| `subsidy-landscape-jp` | Top-N Japanese subsidies for an industry / use-purpose theme (landscape scan) |

## Use cases (concrete examples)

### 1. Meeting preparation in 30 seconds

> "Tell me about 株式会社サンプル製造 (法人番号 1234567890123) before my meeting"

→ The `meeting-prep-jp` agent invokes `gbizinfo-entity-lookup` + `nta-corporate-number-lookup` and produces a 1-page brief with cited financials, employees, certifications, registry change history, and a 4-layer authority strip + 士業 boundary disclaimer.

### 2. M&A due diligence with registry change history

> "Run due diligence on 法人番号 7000012050002 including past name changes and mergers"

→ The `due-diligence-jp` agent combines gBizINFO financial profile + **国税庁 公式 異動履歴** (社名変更 / 移転 / 合併 / 解散 events) + evidence refs + 4-layer authority strip. Useful when raw gBizINFO data omits change history that 国税庁 公式 master uniquely provides.

### 3. Subsidy fit signal (regional × industry × scale)

> "Is the 中小企業庁 IT 導入補助金 a fit for 株式会社サンプル製造?"

→ The `subsidy-fit-jp` agent combines gBizINFO company profile + J-Grants subsidy detail → 3-axis fit **signal** (regional / industry / scale). **Always includes 士業 boundary**: final 適格性 / 申請可否 verification requires a certified 行政書士 or 中小企業診断士 — Kokai itself never renders eligibility decisions.

## Repository layout

```
japan-business-intelligence/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   ├── agent-plugins/
│   │   ├── meeting-prep-jp/
│   │   ├── subsidy-fit-jp/
│   │   ├── due-diligence-jp/
│   │   ├── competitor-brief-jp/
│   │   └── subsidy-landscape-jp/
│   └── vertical-plugins/
│       └── japan-public-business-intelligence/
├── managed-agent-cookbooks/
│   └── kokai-due-diligence-jp/
├── scripts/
├── README.md
├── LICENSE
├── TRADEMARKS.md
└── NOTICE
```

## Getting started — 4 paths

### Path 1A: Claude Code (CLI)

```bash
claude plugin marketplace add Kokai-Data/japan-business-intelligence
claude plugin install japan-public-business-intelligence@japan-business-intelligence
claude plugin install meeting-prep-jp@japan-business-intelligence
```

### Path 1B: Claude Code Desktop App (Windows / macOS, no CLI required)

1. Open Claude Code Desktop App → sidebar **Customize**
2. Under **個人用プラグイン (Personal plugins)** click the **`+`** button
3. Select **プラグインを作成 → マーケットプレイスを追加 (Create plugin → Add marketplace)**
4. Enter repository: `Kokai-Data/japan-business-intelligence` (or full URL `https://github.com/Kokai-Data/japan-business-intelligence`)
5. After the marketplace is added, install the plugins you need (the `japan-public-business-intelligence` vertical plugin + any agent plugins like `meeting-prep-jp`, `due-diligence-jp`, etc.)

This is the most user-friendly path for users not comfortable with CLI. The Plugin auto-registers the kokai MCP server, so no `.mcp.json` editing is required.

### Path 2: Claude Cowork (UI)

1. Open Claude Cowork plugin manager
2. Add this repo URL (this plugin is intended for submission to the Claude plugin marketplace)
3. Enable the agents / verticals you need

### Path 3: Claude Managed Agents (API)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
scripts/deploy-managed-agent.sh kokai-due-diligence-jp
```

### Path 4: Non-Anthropic MCP clients — direct MCP server connection (no Plugin install)

If you use **Cursor**, **Codex**, **OpenAI App Server**, or any other MCP-compatible client, you don't need to install this Plugin. Connect directly to the kokai MCP server via your client's MCP config (`.mcp.json` or equivalent):

```json
{
  "mcpServers": {
    "kokai": {
      "url": "https://mcp.kokai.ai/functions/v1/mcp-server"
    }
  }
}
```

The MCP server exposes all kokai tools (gBizINFO / J-Grants / 国税庁 法人番号 / **EDINET 金融商品取引法開示書類**) directly. You won't get the Skills / slash commands bundled in this Plugin, but you get full data access via the MCP tools (4-source Authority Chain + signal overlay).

**Skills + slash commands** (e.g., `/meeting-prep`, `/due-diligence`) are Anthropic-ecosystem-specific sugar bundled in this Plugin — they're convenience layers for Claude Code / Cowork / Managed Agents, not part of the MCP protocol. Non-Anthropic clients build their own workflows on top of the raw MCP tools.

## How it fits together

- **Agents** are workflows that own end-to-end processes (e.g., meeting prep).
- **Skills** are reusable expertise (e.g., `gbizinfo-entity-lookup`) living in the vertical plugin, bundled into agents.
- **Commands** are explicitly-triggered slash commands (e.g., `/meeting-prep`).
- **MCP servers** (declared in `.mcp.json`) wire to external data; here, the [kokai MCP server](https://mcp.kokai.ai/functions/v1/mcp-server) provides Japan public business intelligence.
- **Managed-agent cookbooks** package the same skills as deployable templates for Claude Managed Agents API.

## Vertical plugin

| Plugin | Focus | MCP server |
|---|---|---|
| `japan-public-business-intelligence` | Japanese corporate registries, subsidies, evidence citations | [kokai](https://mcp.kokai.ai) |

## MCP integrations

| MCP server | URL | Source |
|---|---|---|
| kokai | `https://mcp.kokai.ai/functions/v1/mcp-server` | gBizINFO + J-Grants + 国税庁 法人番号 + **EDINET 金融商品取引法開示書類 (Sprint 14+8 で integration 完了、2026-05-19、ESE140206 Version 2 準拠)** |

### 4-Source Authority Chain

1. **gBizINFO** (経済産業省) — company business intelligence (financials / employees / certifications / shareholders)
2. **J-Grants** (中小企業庁 + デジタル庁) — government subsidies (eligibility / deadlines / max amount / application forms)
3. **国税庁 法人番号 公表 Web-API** — authoritative corporate-number master + change history (社名変更 / 移転 / 合併 / 解散)
4. **EDINET (金融庁)** — listed-company IR (有価証券報告書 / 四半期 / 半期 / 臨時 / 大量保有 / 公開買付 / 内部統制 等) + Kokai signal cluster overlay (annual / quarterly / large-shareholding / TOB / governance / event / correction)

→ AI agent が引用する際に「**4 公式 SoT 統合 + AI-citable signal overlay**」と明示可能。Japan 公的データの法人特定 + 補助金 + 異動履歴 + 上場企業 IR まで 1 接続で full coverage、AI HYVE / N-3 (単一 source 競合) や Anthropic finance-agents (西洋金融 vertical) との明確 differentiator。

## Boundary (士業 safety, REQUIRED)

All outputs include a **4-layer authority strip**:

1. 公式 (official) — cite_required
2. Kokai normalized — cite_required
3. AI summary
4. AI estimate

Subsidy 適格性, 申請可否, legal, tax, or professional judgments are out of scope. Final 適格性 verification must be done by a certified Japanese 士業.

## Customization

Each agent / vertical plugin is a directory with markdown skills and JSON manifests. Fork this repo, edit the markdown files, and re-install with `claude plugin install`. See [Anthropic's plugin documentation](https://docs.claude.com/en/discover-plugins) for details.

## Contributing

1. Fork the repo
2. Run `python3 scripts/check.py` to lint manifests and verify cross-file references
3. Open a PR

## License

Apache License 2.0 — see [LICENSE](./LICENSE).

See [TRADEMARKS.md](./TRADEMARKS.md) for trademark notice and third-party brand allowlist policy.
