# Changelog

All notable changes to this repository follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) conventions.

## [0.9.0] — 2026-07-02 — Out-of-the-box MCP connection fix (401) + skills audit fixes

### Fixed

- **🔴 Critical: MCP connection no longer fails with HTTP 401 out of the box** (`missing_mcp_client_identity`). The kokai MCP server requires a client identity header on every request (including `initialize`), but the shipped `.mcp.json` sent a bare URL — so **all skills were broken for new users** (existing users with an identity never noticed). `.mcp.json` now sends `x-kokai-beta-client-id: ${KOKAI_MCP_CLIENT_ID:-kokai-plugin-shared-default}` — works immediately with a shared anonymous identity; set the `KOKAI_MCP_CLIENT_ID` env var to any unique string for a personal anonymous workspace. Verified live: `initialize` and `tools/list` both return 200 with the default. (kokai-data 0.2.0 → 0.3.0)
- **🔴 Critical: agent plugins now bundle the kokai MCP server** — all 7 agent plugins (`proposal-prep-jp` / `subsidy-fit-jp` / `due-diligence-jp` / `competitor-brief-jp` / `subsidy-landscape-jp` / `legal-research-jp` / `procurement-discovery-jp`) previously declared no MCP server at all and only worked if `kokai-data` happened to be installed alongside (contradicting their "Self-contained" READMEs). Each now ships the same `.mcp.json` (identity headers included) and works standalone. README Dependencies sections updated accordingly. (all agent plugins 0.1.0 → 0.2.0)
- **`nta-corporate-number-lookup` output docs**: `terms_of_use` description said "cite gBizINFO terms" (copy-paste leftover) — corrected to the actual server response (出典: 国税庁法人番号公表サイト attribution + 国税庁 SoT disclaimer). Fixed in the vertical source and re-synced to `due-diligence-jp` / `competitor-brief-jp`.
- **Internal memory-file reference removed from `evidence-citation-builder`** Boundary section (a private dev memory filename had leaked into the distributed SKILL.md in 3 plugins) — replaced with the plain design statement.
- **士業 boundary disclaimer now includes 弁護士 / 司法書士** (Japanese + English verbatim blocks). The disclaimer scopes out legal judgment but omitted lawyers from the advisor list — inconsistent for `legal-research-jp`, whose agent names 弁護士 / 司法書士 explicitly. Fixed in the shared template and synced to all plugins.
- Internal Sprint numbers removed from `legal-research-jp` README.

### Changed

- **Cross-skill references unified to kokai MCP tool / prompt names** (single-install safe): SKILL.md guidance no longer points at skill or agent names that may not be bundled in the installed plugin (e.g. `jgrants-subsidy-search` skill, `subsidy-fit-jp` agent). References now use MCP tool names (`search_subsidies` / `get_subsidy_detail` / `get_nta_corporate_record` / `search_edinet_documents` / `get_edinet_document` / `get_edinet_company_disclosures` / `search_egov_laws` / `get_egov_laws_data` / `search_company` / `search_nta_corporate_name` / `get_entity_profile`) and MCP prompt names (`kokai_subsidy_fit_jp`), which always resolve because every plugin now bundles the MCP server.
- `scripts/sync-agent-skills.py`: added `legal-research-jp` and `procurement-discovery-jp` bundles — their skill copies were previously maintained by hand outside the sync flow and could drift from the vertical source.

## [0.8.0] — 2026-06-04 — Marketplace renamed to `kokai` (brand-first) + displayName cleanup

### Changed

- **Marketplace renamed** `japan-business-data` to **`kokai`** (brand-first). Install handle is now `<plugin>@kokai` (e.g. `/plugin install kokai-data@kokai`) so the marketplace tab in the plugin directory reads as the brand. The GitHub repo stays `Kokai-Data/japan-business-data` (`/plugin marketplace add Kokai-Data/japan-business-data` still works). Future regional siblings would be brand-first too (e.g. `kokai-us`).
- **Plugin displayNames cleaned** -- removed the redundant `Kokai Data:` prefix (the brand already shows on each catalog card via the marketplace owner). Cards now read as `<Japanese label> (English)`, Japanese-primary with an English aid for the two-sided audience (Japanese professionals + English-speaking AI builders).
- **Action for existing users**: remove the old marketplace (`/plugin marketplace remove japan-business-data`), then re-add it (`/plugin marketplace add Kokai-Data/japan-business-data`) so it registers under the new `kokai` handle; re-install plugins under `@kokai`.

## [0.7.2] — 2026-06-02 — `meeting-prep-jp` → `proposal-prep-jp` rename

### Changed

- **Plugin renamed `meeting-prep-jp` → `proposal-prep-jp`**; slash commands `/商談準備` (and English `/meeting-prep`) → `/提案準備` (and `/proposal-prep`); displayName `商談準備 (Meeting Prep)` → `提案準備 (Proposal Prep)`; agent `meeting-prep-jp-agent` → `proposal-prep-jp-agent`. 完全置換 — 旧 `/商談準備`・`/meeting-prep` の後方互換 alias は廃止。Hero persona (士業・コンサルの提案業務) と整合。
- **Action for existing users**: uninstall the old `meeting-prep-jp` plugin and install `proposal-prep-jp@japan-business-data`.
- 汎用 trigger (`面談準備` / `meeting prep` / `打合せ準備` / `営業前リサーチ` 等) は自然言語 auto-invoke の discoverability のため維持。共有 skill (`gbizinfo-entity-lookup` の `商談相手調査` keyword 等) は変更なし。

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
