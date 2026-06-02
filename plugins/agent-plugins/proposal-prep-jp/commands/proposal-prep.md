---
name: proposal-prep
description: /proposal-prep <13-digit 法人番号 OR company name> — invoke the proposal-prep-jp agent
---

# /proposal-prep

Invoke the `proposal-prep-jp-agent` for the provided Japanese company.

See [agent system prompt](../agents/proposal-prep-jp-agent.md) for full workflow.

Usage:

- `/proposal-prep <13-digit 法人番号>` — direct (fastest)
- `/proposal-prep <company name>` — search candidates, confirm with user

Returns: cited 1-page proposal brief with 4-layer authority strip + 士業 boundary disclaimer.
