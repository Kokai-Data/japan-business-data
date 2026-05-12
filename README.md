# Kokai for Public Business Intelligence — Japan

Plugin templates and managed-agent cookbooks for working with **Japanese public business intelligence** — corporate registries (gBizINFO / 国税庁), government subsidies (J-Grants), and AI-citable evidence — using Claude.

This is the **Japan-market equivalent of [Anthropic's `financial-services` agent templates](https://github.com/anthropics/financial-services)**, focused on Japanese public canonical data sources. It is open source under Apache License 2.0 and packages [Kokai Data](https://kokai.ai) (an AI-citable public business intelligence MCP server) as Claude plugins and managed agents.

## Disclaimer

Kokai provides **signal / 確認材料 / context, not decisions**. Subsidy 適格性, 申請可否, legal, tax, or professional judgments are out of scope and must be verified by a certified Japanese 士業 (registered advisor: 行政書士, 中小企業診断士, 公認会計士, or 税理士). Never fictionalize company or subsidy facts — use only Kokai tool/prompt outputs and cited public sources.

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

## Repository layout

```
kokai-for-public-business-intelligence-jp/
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

## Getting started — 3 paths

### Path 1: Claude Code (CLI)

```bash
claude plugin marketplace add kokai-data/kokai-for-public-business-intelligence-jp
claude plugin install japan-public-business-intelligence@kokai-for-public-business-intelligence-jp
claude plugin install meeting-prep-jp@kokai-for-public-business-intelligence-jp
```

### Path 2: Claude Cowork (UI)

1. Open Claude Cowork plugin manager
2. Add this repo URL (this plugin is intended for submission to the Claude plugin marketplace)
3. Enable the agents / verticals you need

### Path 3: Claude Managed Agents (API)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
scripts/deploy-managed-agent.sh kokai-due-diligence-jp
```

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
| kokai | `https://mcp.kokai.ai/functions/v1/mcp-server` | gBizINFO + J-Grants + 国税庁 (planned) |

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
