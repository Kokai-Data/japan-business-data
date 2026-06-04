# Kokai for Public Business Intelligence — Japan

**AI-citable Japanese public business intelligence** for **all AI agents** — **6-source Authority Chain**: corporate registries (gBizINFO + 国税庁 法人番号 公表 Web-API), government subsidies (J-Grants), **listed-company IR (EDINET 金融商品取引法開示書類)**, **statutory law (e-Gov 法令検索, デジタル庁)**, and **government procurement (官公需情報ポータル, 中小企業庁)** with 士業 + investment-disclaimer boundary safety. **For AI builders (Claude / Cursor / Codex / OpenAI App Server / all MCP clients), Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士 / 弁護士 / 司法書士), investment professionals, M&A advisors, and B2G sales / consulting teams.**

This is the **Japan-market equivalent of [Anthropic's `financial-services` agent templates](https://github.com/anthropics/financial-services)**, focused on Japanese public canonical data sources. It is open source under Apache License 2.0 and packages [Kokai Data](https://kokai.ai) (an AI-citable public business intelligence MCP server) as both **a universal MCP server (for all AI clients)** and **Claude plugins + managed agents (for Anthropic ecosystem sugar)**.

## Architecture — Universal MCP server + Anthropic Plugin sugar (2 layers)

Kokai Data follows a **2-layer architecture** for AI agent ecosystem neutrality:

| Layer | What | Who can use it |
|---|---|---|
| **L1: Universal MCP server** | `https://mcp.kokai.ai/functions/v1/mcp-server` — implements MCP spec 2025-06-18 | **All MCP clients**: Claude Code / Claude Cowork / Claude Managed Agents / Claude.ai (connectors layer) / Cursor / Codex / OpenAI App Server / any custom MCP client. Setup via `.mcp.json` config (no Plugin required). |
| **L2: Anthropic Plugin sugar** (this repo) | `Kokai-Data/japan-business-data` — bundles Skills, slash commands, managed-agent cookbook, and auto-registers the MCP server | **Anthropic ecosystem users**: Claude Code (CLI + Desktop App) / Claude Cowork / Claude Managed Agents. Plugin install auto-configures everything (no manual `.mcp.json` editing). |

**Non-Claude clients (Cursor / Codex / etc.) do NOT need to install this Plugin** — they connect to the MCP server directly via their own `.mcp.json` (see Path 4 below). The Plugin layer is purely Anthropic-ecosystem distribution sugar (auto-install / auto-update / Skills auto-invocation).

This dual approach matches Kokai's brand promise: **AI agent ecosystem neutral**, not tied to any single AI provider.

## Naming

| | |
|---|---|
| **Brand** | Kokai Data |
| **Marketplace handle** | `kokai` |
| **GitHub repository** | `Kokai-Data/japan-business-data` |
| **Plugin (recommended install)** | `kokai-data` |
| **MCP server** | `mcp.kokai.ai` |
| **Trade sub-brand** | Kokai Trade |

The recommended install is the **`kokai-data`** plugin (`/plugin install kokai-data@kokai`) — the brand-bearing core plugin that bundles the MCP server, slash commands, and skills. The marketplace handle is `kokai` (brand-first); the GitHub repo stays `Kokai-Data/japan-business-data`.

## Migration from legacy plugin name

The core plugin was renamed from `japan-public-business-intelligence` to `kokai-data` (for brand visibility in the Claude Code plugin list). If you installed the legacy plugin, please re-install:

1. Uninstall the legacy plugin `japan-public-business-intelligence` (or remove it in the GUI plugin list).
2. Install the new plugin: `/plugin install kokai-data@kokai`.

Your existing slash commands (`/企業調査`, `/提案準備`, etc.) work the same after re-install.

## Disclaimer

Kokai provides **signal / 確認材料 / context, not decisions**. Subsidy 適格性, 申請可否, legal interpretation, 訴訟戦略, bid eligibility, tax, or professional judgments are out of scope and must be verified by a certified Japanese 士業 (registered advisor: 行政書士 / 中小企業診断士 / 公認会計士 / 税理士 / 弁護士 / 司法書士). Never fictionalize company, subsidy, statute, or procurement facts — use only Kokai tool/prompt outputs and cited public sources.

## Who is this for

**This Plugin is for**:

- **AI agents / AI builders** (Claude Code / Claude Cowork / Cursor / Codex / OpenAI App Server) needing **AI-citable Japanese public business intelligence** with verifiable government sources for citation-required outputs.
- **Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士 / 弁護士 / 司法書士)** preparing meeting briefs, due diligence, competitor research, subsidy fit analysis, **legal research / 法令調査**, and **B2G procurement discovery** — with **automatic 士業 boundary disclaimers** that prevent AI from rendering professional judgments.
- **Investment professionals / M&A advisors** doing Japanese target diligence with **registry change history** (社名変更 / 移転 / 合併 / 解散) from 国税庁 公式 master + **上場企業 IR** (EDINET 有価証券報告書 / TOB / 大量保有) + **applicable 業法 verification** (e-Gov 法令検索).
- **B2G sales / consulting teams** identifying fresh **government procurement opportunities** (Call for Tender / 公告) by industry + region from 官公需情報ポータル.
- **Government / public sector developers** building citizen-facing AI tools requiring **official source attribution** (cite_required + signal-not-decision layer).

**This Plugin is NOT for**:

- Real-time market data or pricing (use Bloomberg / Refinitiv, or [`anthropics/financial-services`](https://github.com/anthropics/financial-services) for Western markets).
- Non-Japanese companies (use `anthropics/financial-services` for that).
- Final eligibility / legal / tax / professional judgments — these always require a certified Japanese 士業.
- Procurement bid outcomes / 落札結果 / 受注実績 / 価格 signals (NOT in 官公需 official API; consult commercial DB like 帝国データバンク 入札情報 or hire a 中小企業診断士).

## What's in this repo

| Category | Count | Examples |
|---|---|---|
| Agent plugins (self-contained workflows) | **7** | proposal-prep-jp, subsidy-fit-jp, due-diligence-jp, competitor-brief-jp, subsidy-landscape-jp, **legal-research-jp**, **procurement-discovery-jp** |
| Vertical plugin (shared skill bundle + MCP connector) | 1 | kokai-data (19 skills) |
| Managed-agent cookbook (Claude Managed Agents deployment template) | 1 | kokai-due-diligence-jp |

## Agents (7 named templates)

| Agent | Function | Authority source |
|---|---|---|
| `proposal-prep-jp` | 1-page brief for a Japanese company before a meeting (cited public data) | gBizINFO + 国税庁 |
| `subsidy-fit-jp` | 3-axis fit signal (regional / industry / scale) for a Japanese company × subsidy pair | gBizINFO + J-Grants |
| `due-diligence-jp` | 1-page due diligence brief on a Japanese company (gBizINFO entity + evidence refs + EDINET IR) | gBizINFO + 国税庁 + EDINET |
| `competitor-brief-jp` | 3-tier competitor brief (overview / scale / certifications) for a Japanese company | gBizINFO + 国税庁 |
| `subsidy-landscape-jp` | Top-N Japanese subsidies for an industry / use-purpose theme (landscape scan) | J-Grants |
| **`legal-research-jp`** | Japanese statute lookup + verbatim 条文 fetch from e-Gov 法令検索 | **e-Gov 法令 (デジタル庁)** |
| **`procurement-discovery-jp`** | Japanese government procurement (Call for Tender) discovery (Phase 1 = notice discovery only) | **官公需情報ポータル (中小企業庁)** |

## 日本語 slash commands (日本人ユーザー向け alias)

英語 slash commands は日本人ユーザーには意味が把握しにくいため、**日本語 alias を並列追加** (OSS rev 0.7.0)。両方が動作 (後方互換維持、英語 command も touch せず)。

| 日本語 | 英語 alias | 機能 |
|---|---|---|
| `/提案準備` | `/proposal-prep` | 提案前 1 ページ ブリーフ生成 (gBizINFO + 国税庁 + J-Grants landscape) |
| `/企業調査` | `/due-diligence` | 1 ページ デューデリ brief (gBizINFO + 国税庁 + EDINET 上場時) |
| `/補助金マッチ` | `/subsidy-fit` | 3 軸 (地域 / 業種 / 規模) fit signal (Kokai は判定者ではなく signal 提示者) |
| `/競合調査` | `/competitor-brief` | 3-tier 競合 brief (概観 / 規模 / 認定) |
| `/補助金スキャン` | `/subsidy-landscape` | Top-N 補助金 landscape scan (signal overlay 形式) |
| `/法令調査` | `/legal-research` | 日本法令 keyword 検索 + 条文 verbatim 取得 (e-Gov, デジタル庁) |
| `/調達公告検索` | `/procurement-discovery` | 政府調達 公告 discovery (Phase 1 = CFT only, 官公需情報ポータル) |

**自然言語でも auto-invoke 可能** (例: 「提案準備して」「企業調査お願い」「○○ 法人の経営情報取得」「医薬品関連の法令を調査して」「システム開発の公共調達を検索」)。日本語 keyword は agent.md `triggers` (7 件、各 5-7 keyword 追加) と vertical + agent SKILL.md `description` (59 mirror、19 unique skill) に組み込み済。

### 士業セーフティ表現

全 14 alias は「判定 / 決定」表現を避け、「準備 / 調査 / マッチ / スキャン / 検索」phrasing で統一。Kokai は判定者ではなく **signal / 確認材料 提示者**、士業 (中小企業診断士 / 行政書士 / 公認会計士 / 税理士 / 弁護士 / 司法書士) 確認前提。

## Use cases (concrete examples)

### 1. Proposal preparation in 30 seconds

> "Tell me about 株式会社サンプル製造 (法人番号 1234567890123) before my meeting"

→ The `proposal-prep-jp` agent invokes `gbizinfo-entity-lookup` + `nta-corporate-number-lookup` and produces a 1-page brief with cited financials, employees, certifications, registry change history, and a 4-layer authority strip + 士業 boundary disclaimer.

### 2. M&A due diligence with registry change history + 上場企業 IR

> "Run due diligence on 法人番号 7000012050002 including past name changes, mergers, and any EDINET filings"

→ The `due-diligence-jp` agent combines gBizINFO financial profile + **国税庁 公式 異動履歴** (社名変更 / 移転 / 合併 / 解散 events) + **EDINET 有価証券報告書 / 大量保有 / TOB** disclosures + evidence refs + 4-layer authority strip. Useful when raw gBizINFO data omits change history that 国税庁 公式 master uniquely provides, or when target is listed and IR depth matters.

### 3. Subsidy fit signal (regional × industry × scale)

> "Is the 中小企業庁 IT 導入補助金 a fit for 株式会社サンプル製造?"

→ The `subsidy-fit-jp` agent combines gBizINFO company profile + J-Grants subsidy detail → 3-axis fit **signal** (regional / industry / scale). **Always includes 士業 boundary**: final 適格性 / 申請可否 verification requires a certified 行政書士 or 中小企業診断士 — Kokai itself never renders eligibility decisions.

### 4. Legal research — verbatim 条文 + 業法 mapping for DD

> "What does Article 15 of the 個人情報保護法 say? Also, list all 業法 applicable to a 医薬品 manufacturer"

→ The `legal-research-jp` agent invokes `search-egov-laws` (keyword search) + `get-egov-laws-data` (full statute fetch) from e-Gov 法令検索 (デジタル庁). Output is **verbatim 公式 statute text** with `law_id` + `enforcement_date` + e-Gov URL citation. **Never legal interpretation** — final 法的判断 / 訴訟戦略 requires certified Japanese 弁護士 / 行政書士 / 司法書士.

### 5. B2G sales lead discovery — government procurement notices

> "Show me recent システム開発 procurement notices issued by 中小企業庁 or 東京都"

→ The `procurement-discovery-jp` agent invokes `search-procurement-portal` from 官公需情報ポータル (中小企業庁). Returns CFT notices with `project_name` / `organization_name` / `category` / `procedure_type` / `cft_issue_date` / `source_url`. **Phase 1 scope**: discovery only. **Phase 2 (受注実績 / 落札結果 / 落札価格 / supplier 履歴) NOT in official API** — direct user to commercial DB or 中小企業診断士 consultation for outcomes.

## Repository layout

```
japan-business-data/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   ├── agent-plugins/
│   │   ├── proposal-prep-jp/
│   │   ├── subsidy-fit-jp/
│   │   ├── due-diligence-jp/
│   │   ├── competitor-brief-jp/
│   │   ├── subsidy-landscape-jp/
│   │   ├── legal-research-jp/             # ← Sprint 14+12 (e-Gov 法令、デジタル庁)
│   │   └── procurement-discovery-jp/      # ← Sprint 14+13 (官公需、中小企業庁)
│   └── vertical-plugins/
│       └── kokai-data/
│           ├── commands/                  # 7 slash commands (proposal-prep / due-diligence / subsidy-fit / competitor-brief / subsidy-landscape / legal-research / procurement-discovery)
│           └── skills/                    # 19 shared skills
├── managed-agent-cookbooks/
│   └── kokai-due-diligence-jp/
├── scripts/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── TRADEMARKS.md
└── NOTICE
```

## Getting started — 4 paths

### Path 1A: Claude Code (CLI)

```bash
claude plugin marketplace add Kokai-Data/japan-business-data
claude plugin install kokai-data@kokai
claude plugin install proposal-prep-jp@kokai
# New Sprint 14+12/14+13 plugins:
claude plugin install legal-research-jp@kokai
claude plugin install procurement-discovery-jp@kokai
```

### Path 1B: Claude Code Desktop App (Windows / macOS, no CLI required)

1. Open Claude Code Desktop App → sidebar **Customize**
2. Under **個人用プラグイン (Personal plugins)** click the **`+`** button
3. Select **プラグインを作成 → マーケットプレイスを追加 (Create plugin → Add marketplace)**
4. Enter repository: `Kokai-Data/japan-business-data` (or full URL `https://github.com/Kokai-Data/japan-business-data`)
5. After the marketplace is added, install the plugins you need (the `kokai-data` vertical plugin + any agent plugins like `proposal-prep-jp`, `due-diligence-jp`, `legal-research-jp`, `procurement-discovery-jp` etc.)

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

The MCP server exposes all kokai tools (gBizINFO / J-Grants / 国税庁 法人番号 / EDINET / **e-Gov 法令検索** / **官公需情報ポータル**) directly. You won't get the Skills / slash commands bundled in this Plugin, but you get full data access via the MCP tools (6-source Authority Chain + signal overlay).

**Skills + slash commands** (e.g., `/proposal-prep`, `/due-diligence`, `/legal-research`, `/procurement-discovery`) are Anthropic-ecosystem-specific sugar bundled in this Plugin — they're convenience layers for Claude Code / Cowork / Managed Agents, not part of the MCP protocol. Non-Anthropic clients build their own workflows on top of the raw MCP tools.

## How it fits together

- **Agents** are workflows that own end-to-end processes (e.g., proposal prep, legal research, procurement discovery).
- **Skills** are reusable expertise (e.g., `gbizinfo-entity-lookup`, `search-egov-laws`, `search-procurement-portal`) living in the vertical plugin, bundled into agents.
- **Commands** are explicitly-triggered slash commands (e.g., `/proposal-prep`, `/legal-research`, `/procurement-discovery`).
- **MCP servers** (declared in `.mcp.json`) wire to external data; here, the [kokai MCP server](https://mcp.kokai.ai/functions/v1/mcp-server) provides Japan public business intelligence.
- **Managed-agent cookbooks** package the same skills as deployable templates for Claude Managed Agents API.

## Vertical plugin

| Plugin | Focus | MCP server |
|---|---|---|
| `kokai-data` | Japanese corporate registries, subsidies, listed-company IR, statutory law, government procurement, evidence citations | [kokai](https://mcp.kokai.ai) |

## MCP integrations

| MCP server | URL | Source |
|---|---|---|
| kokai | `https://mcp.kokai.ai/functions/v1/mcp-server` | gBizINFO + J-Grants + 国税庁 法人番号 + **EDINET 金融商品取引法開示書類** + **e-Gov 法令検索 (デジタル庁)** + **官公需情報ポータル (中小企業庁)** |

### 6-Source Authority Chain

1. **gBizINFO** (経済産業省) — company business intelligence (financials / employees / certifications / shareholders).
2. **J-Grants** (中小企業庁 + デジタル庁) — government subsidies (eligibility / deadlines / max amount / application forms).
3. **国税庁 法人番号 公表 Web-API** — authoritative corporate-number master + change history (社名変更 / 移転 / 合併 / 解散).
4. **EDINET** (金融庁) — listed-company IR (有価証券報告書 / 四半期 / 半期 / 臨時 / 大量保有 / 公開買付 / 内部統制 等) + Kokai signal cluster overlay (annual / quarterly / large-shareholding / TOB / governance / event / correction).
5. **e-Gov 法令検索** (デジタル庁) — Japanese statutory law (Constitution / Acts / Cabinet Orders / Ministerial Ordinances / Rules) with full statute text + chapter / article structure.
6. **官公需情報ポータル** (中小企業庁) — government procurement (Call for Tender notices, 公告) — project names / issuing organizations / industry categories / bid procedure types / CFT issue dates. Phase 1 = discovery only; awarded results deferred to Phase 2.

→ AI agent が引用する際に「**6 公式 SoT 統合 + AI-citable signal overlay**」と明示可能。Japan 公的データの法人特定 + 補助金 + 異動履歴 + 上場企業 IR + 統治法令 + 政府調達公告まで 1 接続で full coverage、AI HYVE / N-3 (3-source 競合) や Anthropic finance-agents (西洋金融 vertical) との明確 differentiator。

## Boundary (士業 safety, REQUIRED)

All outputs include a **4-layer authority strip**:

1. 公式 (official) — cite_required
2. Kokai normalized — cite_required
3. AI summary
4. AI estimate

Subsidy 適格性, 申請可否, 法令解釈 / 訴訟戦略, 入札判断 / 適格性判断, legal, tax, or professional judgments are out of scope. Final verification must be done by a certified Japanese 士業 (行政書士 / 中小企業診断士 / 公認会計士 / 税理士 / 弁護士 / 司法書士).

## Customization

Each agent / vertical plugin is a directory with markdown skills and JSON manifests. Fork this repo, edit the markdown files, and re-install with `claude plugin install`. See [Anthropic's plugin documentation](https://docs.claude.com/en/discover-plugins) for details.

## Contributing

1. Fork the repo
2. Run `python3 scripts/check.py` to lint manifests and verify cross-file references
3. Open a PR

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for Sprint-by-Sprint history (Sprint 14+8 EDINET / 14+12 e-Gov 法令 / 14+13 官公需 etc.).

## License

Apache License 2.0 — see [LICENSE](./LICENSE).

See [TRADEMARKS.md](./TRADEMARKS.md) for trademark notice and third-party brand allowlist policy.
