---
name: procurement-discovery
description: /procurement-discovery <query> — search Japanese government procurement notices (Call for Tender, 公告) from 官公需情報ポータル (中小企業庁)
---

# /procurement-discovery

Search Japanese government procurement notices (Call for Tender, 公告) via 官公需情報ポータル (中小企業庁) REST + XML API. Phase 1 = bid notice **discovery only** (received bids / outcomes are not in the public API).

Usage:

- `/procurement-discovery <keyword>` — search by free-text keyword (e.g., `/procurement-discovery システム開発`)
- `/procurement-discovery organization=<name>` — search by issuing organization (e.g., `/procurement-discovery organization=中小企業庁`)
- `/procurement-discovery lg_code=<code>` — search by local government code

Returns cited list of CFT notices + 4-layer authority strip + 行政書士 / 中小企業診断士 / 弁護士 boundary disclaimer.

Calls `search-procurement-portal` Skill (公式 官公需情報ポータル API, 中小企業庁).

## Phase 1 scope

- ✅ project names, issuing organizations, industry categories, procedure types, CFT issue dates
- ❌ awarded results / 落札価格 / supplier 履歴 (NOT in official API; deferred to Phase 2)

## Boundary

Output is **signal / 確認材料** — NOT bid advice or 適格性 judgment. 入札判断 / 適格性判断 / 契約交渉 requires certified Japanese 行政書士 / 中小企業診断士 / 弁護士.
