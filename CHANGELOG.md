# Changelog

All notable changes to this repository follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) conventions.

## [0.7.1] — 2026-06-01 — Marketplace renamed → `japan-business-data`

### Changed

- **Marketplace renamed** `japan-business-intelligence` → **`japan-business-data`** (and GitHub repo `Kokai-Data/japan-business-intelligence` → `Kokai-Data/japan-business-data`). Install handle is now `<plugin>@japan-business-data` — shorter, and aligned with Anthropic's domain-style marketplace naming (`financial-services` / `life-sciences`). Plugin names are unchanged (e.g. `japan-public-business-intelligence`). Old GitHub URLs auto-redirect.
- **Action for existing users**: re-add the marketplace (`/plugin marketplace add Kokai-Data/japan-business-data`) and re-install plugins under the new `@japan-business-data` identity; remove the old `japan-business-intelligence` marketplace.

## [0.7.0] — 2026-05-26 — 日本語 slash command alias 追加 (Approach B + C combined)

### Added

- **日本語 slash command alias 14 件** (vertical plugin 7 + 各 agent plugin 7) — `/商談準備` (alias of `/meeting-prep`) / `/企業調査` (alias of `/due-diligence`) / `/補助金マッチ` (alias of `/subsidy-fit`) / `/競合調査` (alias of `/competitor-brief`) / `/補助金スキャン` (alias of `/subsidy-landscape`) / `/法令調査` (alias of `/legal-research`) / `/調達公告検索` (alias of `/procurement-discovery`).
- 各 agent.md `triggers` に日本語 keyword 追加 (7 件、各 5-7 keyword: 商談準備 / 打合せ準備 / 営業前リサーチ / 商談相手の調査 / 企業調査 / デューデリ / 法人調査 / 補助金マッチ / 補助金マッチング / 補助金 候補確認 / 競合調査 / 競合分析 / 競合他社 リサーチ / 補助金スキャン / 補助金 一覧 / 業種別補助金 / 補助金マップ / 法令調査 / 法律検索 / 条文取得 / e-Gov 法令 / 業法 確認 / 調達公告検索 / 公共調達 検索 / CFT 検索 / B2G リサーチ 等)、自然言語 auto-invoke 強化。
- 各 SKILL.md `description` 末尾に日本語 keyword suffix 追加 (59 SKILL.md mirror、19 unique skill)。
- `scripts/add_jp_keywords_to_skills.py` — one-off automation script (idempotent、`日本語 keyword:` 二重追加防止 + `re.subn` 安全 match)。

### Changed

- **後方互換維持**: 既存英語 command (`/meeting-prep` 等) は touch せず、英語 triggers / description も削除なし — Plugin install 後に英語 7 + 日本語 7 = **14 commands 表示** (Keijiro 手動 verify 待ち)。
- `marketplace.json` 全 8 plugin description に日本語名 + 英語 alias 併記 + 士業セーフティ表現整合 (signal / 確認材料 / 提示者 phrasing)。
- `README.md` に **「日本語 slash commands (日本人ユーザー向け alias)」section 追加** (Agents section の後、Use cases section の前)。

### Sprint mapping (本体 repo Nihonbashi-AI-Lab/kokai)

| Sprint | Source | Repo change |
|---|---|---|
| 14+14 (2026-05-26) | OSS Plugin 日本語化 (内部 task、Approach B + C combined) | 14 new alias commands + 7 agent.md triggers + 59 SKILL.md description suffix + marketplace.json/README.md polish + add_jp_keywords_to_skills.py |

### 士業セーフティ表現の維持 (memory `feedback_pack_naming_professional_safety.md` 準拠)

全 14 日本語 alias は「判定 / 決定」表現を避け、「準備 / 調査 / マッチ / スキャン / 検索」phrasing に統一。各 alias 末尾 Boundary section で Kokai は判定者ではなく signal 提示者である旨を明示、士業 (中小企業診断士 / 行政書士 / 公認会計士 / 税理士 / 弁護士 / 司法書士) 確認前提を維持。

## [0.6.0] — 2026-05-26 — 6-source Authority Chain 完成

### Added — 2 new agent plugins + 3 new vertical skills + 2 new slash commands

- **Agent plugin**: `legal-research-jp` — Japanese legal research from e-Gov 法令検索 (デジタル庁). Cited statute lookup + verbatim 条文 fetch + 4-layer authority strip + 弁護士 / 行政書士 / 司法書士 boundary disclaimer.
- **Agent plugin**: `procurement-discovery-jp` — Japanese government procurement (Call for Tender) discovery from 官公需情報ポータル (中小企業庁). Phase 1 scope = bid notice discovery only (project names / issuing organizations / categories / procedure types / CFT issue dates). Phase 2 (awarded results / supplier history / price signals) deferred — NOT in official API.
- **Vertical plugin skills** (3 new): `search-egov-laws` / `get-egov-laws-data` / `search-procurement-portal` added to `japan-public-business-intelligence` shared skill bundle.
- **Slash commands** (2 new): `/legal-research` + `/procurement-discovery` added to vertical plugin.

### Changed

- README: 4-source → **6-source Authority Chain** (gBizINFO + J-Grants + 国税庁 法人番号 + EDINET + **e-Gov 法令** + **官公需情報ポータル**).
- Agent plugins count: 5 → **7** (added `legal-research-jp` + `procurement-discovery-jp`).
- Org repo description + topics updated for 6-source claim (added `egov-laws` / `procurement-portal` / `legal-research` / `public-procurement` topics).
- MCP server `tools/list`: 13 → **14 tools** (`search_procurement_portal` added; e-Gov tools were added in 0.5.0).
- Vertical plugin marketplace description: 3-source claim → 6-source.

### Sprint mapping (本体 repo Nihonbashi-AI-Lab/kokai)

| Sprint | Source | Repo change |
|---|---|---|
| 14+12 (2026-05-22) | **e-Gov 法令検索 v2** (デジタル庁) | `search-egov-laws` + `get-egov-laws-data` skills + `legal-research-jp` agent |
| 14+13 (2026-05-26) | **官公需情報ポータル** (中小企業庁) | `search-procurement-portal` skill + `procurement-discovery-jp` agent |

## [0.5.0] — 2026-05-19 — EDINET 上場企業 IR integration (4-source Authority Chain)

### Added

- **Agent plugin EDINET 統合**: 4-source Authority Chain (gBizINFO + J-Grants + 国税庁 法人番号 + **EDINET 金融商品取引法開示書類**) claim 化.
- EDINET skills (3): `edinet-document-search` / `edinet-document-fetch` / `edinet-company-ir-tracker`.
- `due-diligence-jp` bundle に EDINET skill 統合 (上場企業 DD で 有価証券報告書 / 四半期 / 大量保有 / TOB / 内部統制 verification).

### Sprint mapping

| Sprint | Source | Repo change |
|---|---|---|
| 14+8 (2026-05-19) | EDINET v2 (金融庁) | 3 EDINET skills + due-diligence-jp 上場対応 |

## [0.4.0] — 2026-05-18 — Repo rename + 3-source claim establishment

### Changed

- Repo transferred to **Kokai-Data org** and renamed to `japan-business-intelligence`.
- 3-source Authority Chain (gBizINFO + J-Grants + **国税庁 法人番号 公表 Web-API**) claim established.

### Sprint mapping

| Sprint | Source | Repo change |
|---|---|---|
| 7p-2 (2026-05-18) | 国税庁 法人番号 公表 Web-API | `nta-corporate-name-search` + `nta-corporate-number-lookup` skills |

## [0.3.0] and earlier

5 initial agent plugins (`meeting-prep-jp` / `subsidy-fit-jp` / `due-diligence-jp` / `competitor-brief-jp` / `subsidy-landscape-jp`) + vertical plugin (`japan-public-business-intelligence`) + managed-agent cookbook (`kokai-due-diligence-jp`).

2-source baseline: gBizINFO + J-Grants.

---

For Sprint-by-Sprint architectural decisions and Phase roadmap, see the private development log at [Nihonbashi-AI-Lab/kokai](https://github.com/Nihonbashi-AI-Lab/kokai) (Kokai Data internal repo).
