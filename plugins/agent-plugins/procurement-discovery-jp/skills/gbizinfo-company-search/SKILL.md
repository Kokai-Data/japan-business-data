---
name: gbizinfo-company-search
description: Search for a Japanese company by name (Japanese / kana / Latin / hiragana, 2+ chars) when you do not have the 13-digit 法人番号. Returns matches from the gBizINFO registry.
---

## When to use

Use this skill when:

- The user provides a company name in any of these forms: Japanese kanji, katakana, hiragana, or Latin romanization (2+ characters).
- You need to identify the 13-digit 法人番号 before pulling detailed data.

## How to invoke

Call the kokai MCP server's `search_company` tool:

```json
{
  "name": "search_company",
  "arguments": {
    "name": "<company name, 2+ chars>",
    "limit": 5
  }
}
```

The classifier accepts:

- Japanese kanji (株式会社…)
- Katakana (メルカリ など)
- Hiragana (かわぐち など)
- Latin (KAWAGUCHI / Mercari など)

## Output format

For each candidate, present:

- Company name
- 13-digit 法人番号
- Location (本社所在地)
- Source URL (cite_required)

Confirm the candidate with the user before drilling deeper.

## Boundary

- Output is signal / 確認材料 / context — NOT a decision.
- If multiple matches exist, present all and let the user disambiguate. Do not pick on their behalf.
