# Changelog

All notable changes to this repository follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) conventions.

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
