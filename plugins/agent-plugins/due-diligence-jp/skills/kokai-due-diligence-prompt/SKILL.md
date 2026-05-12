---
name: kokai-due-diligence-prompt
description: Use the kokai MCP server's `kokai_due_diligence_jp` prompt to prepare a 1-page Japanese company DD brief from public canonical sources.
---

## When to use

Use this skill when:

- The user asks for a due diligence brief, pre-investment research, or pre-meeting client brief on a Japanese company.
- You have a 13-digit 法人番号 (corporate number).
- You want a structured brief with thinking instructions and ACBS authority/cite_required/expert-review boundary already embedded.

## How to invoke

Request the kokai MCP server's `kokai_due_diligence_jp` prompt:

```json
{
  "name": "kokai_due_diligence_jp",
  "arguments": {
    "corporate_number": "<13-digit 法人番号>"
  }
}
```

The prompt returns a `messages` array with:

- Thinking instructions (how to organize the response)
- Embedded resources (gBizINFO entity + evidence refs)
- 4-layer authority strip
- 士業 expert-review boundary message

## Output format

Follow the thinking instructions returned by the prompt. The output should:

- Header: company name + 法人番号
- Sections cited from gBizINFO records + evidence refs
- 4-layer authority strip at footer
- 士業 boundary disclaimer

## Boundary

- Output is signal / 確認材料 / context — NOT a decision.
- DD conclusions / investment decisions / legal judgment require certified Japanese 士業 (公認会計士 / 弁護士 / 行政書士).
