---
name: kokai-subsidy-landscape-prompt
description: Use the kokai MCP server's `kokai_subsidy_landscape_scan_jp` prompt to scan top-N Japanese subsidies for an industry or use-purpose theme. 日本語 keyword: 補助金スキャン プロンプト / 補助金 landscape frame / Top-N 補助金 framework.
---

## When to use

Use this skill when:

- The user asks for a sector / strategy theme landscape (NOT individual application advice).
- You want a top-N subsidies overview for an industry or use_purpose.

## How to invoke

Request the kokai MCP server's `kokai_subsidy_landscape_scan_jp` prompt:

```json
{
  "name": "kokai_subsidy_landscape_scan_jp",
  "arguments": {
    "industry": "<optional industry name or code>",
    "use_purpose": "<optional use purpose>"
  }
}
```

At least one of `industry` or `use_purpose` is required.

The prompt returns thinking instructions + embedded resources for landscape brief.

## Output format

- List top-N subsidies with title / target area / deadline / max amount / cite_required source URL
- 3-axis signal per subsidy: regional / industry / scale fit
- Landscape summary: ranking, regional distribution, authority signals

## Boundary

- Output is **landscape signal**, NOT individual application advice.
- For company-specific fit analysis, use the kokai MCP server's `kokai_subsidy_fit_jp` prompt.
- Final 適格性 / 申請可否 verification requires a certified Japanese 士業.
