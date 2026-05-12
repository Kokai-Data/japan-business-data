---
name: meeting-prep
description: /meeting-prep <13-digit 法人番号 OR company name> — invoke the meeting-prep-jp agent
---

# /meeting-prep

Invoke the `meeting-prep-jp-agent` for the provided Japanese company.

See [agent system prompt](../agents/meeting-prep-jp-agent.md) for full workflow.

Usage:

- `/meeting-prep <13-digit 法人番号>` — direct (fastest)
- `/meeting-prep <company name>` — search candidates, confirm with user

Returns: cited 1-page meeting brief with 4-layer authority strip + 士業 boundary disclaimer.
