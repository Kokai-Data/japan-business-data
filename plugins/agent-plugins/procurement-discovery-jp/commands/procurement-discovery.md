---
name: procurement-discovery
description: /procurement-discovery <query> — invoke the procurement-discovery-jp agent for Japanese government procurement (Call for Tender) discovery
---

# /procurement-discovery

Invoke the `procurement-discovery-jp-agent` for Japanese government procurement (Call for Tender, 公告) discovery via 官公需情報ポータル (中小企業庁).

See [agent system prompt](../agents/procurement-discovery-jp-agent.md) for full workflow.

Usage:

- `/procurement-discovery <keyword>` — search by free-text keyword (e.g., `/procurement-discovery システム開発`)
- `/procurement-discovery organization=<name>` — search by issuing organization (e.g., `/procurement-discovery organization=東京都`)
- `/procurement-discovery lg_code=<code>` — search by local government code

Returns: cited list of Call for Tender notices + 4-layer authority strip + 行政書士 / 中小企業診断士 / 弁護士 boundary disclaimer.

## Phase 1 scope

This skill covers Call for Tender (CFT) **discovery only**:
- ✅ project names / 公告名, issuing organizations / 発注機関, categories, procedure types, CFT issue dates
- ❌ awarded results / 受注実績 / 落札結果 / 落札価格 / 予定価格 / supplier 情報 (NOT in official API)

For Phase 2 data, consult commercial procurement DB (帝国データバンク 入札情報) or 中小企業診断士 / 行政書士.

## Boundary

Output is **signal / 確認材料** — NOT bid advice or 適格性 judgment. 入札判断 / 適格性判断 / 契約交渉 requires certified 行政書士 / 中小企業診断士 / 弁護士.
