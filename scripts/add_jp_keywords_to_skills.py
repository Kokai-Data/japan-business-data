"""One-off script: append 日本語 keyword suffix to each SKILL.md description.
Run from any cwd: `py scripts/add_jp_keywords_to_skills.py`.
Idempotent: if description already contains "日本語 keyword:", skip.
"""

import os
import re

MAP = {
    "authority-strip-formatter": "出典階層 / 4 階層 出典 / 引用層 / authority strip 整形 / ACBS 4 層",
    "edinet-company-ir-tracker": "上場企業 IR / IR 追跡 / EDINET 開示 / 有価証券報告書 取得 / 上場企業 disclosure 追跡",
    "edinet-document-fetch": "EDINET 文書取得 / 開示書類 ダウンロード / 有価証券報告書 binary 取得 / 開示文書 PDF 取得",
    "edinet-document-search": "EDINET 文書検索 / 有価証券報告書 検索 / 開示書類 検索 / 金商法開示 検索",
    "evidence-citation-builder": "出典 構築 / 引用 構築 / evidence 引用 / citation 取得 / record_id から出典取得",
    "gbizinfo-company-search": "会社検索 / 法人検索 / 企業検索 / 会社名から法人番号 / 法人名で企業検索",
    "gbizinfo-entity-lookup": "法人情報取得 / 企業情報検索 / 法人番号で企業調査 / 商談相手調査 / 経営情報取得 / 会社プロファイル取得",
    "get-egov-laws-data": "条文取得 / 法令本文 / e-Gov 法令データ / 法律全文取得 / law_id で条文取得",
    "jgrants-subsidy-detail": "補助金詳細 / 補助金情報 取得 / J-Grants 詳細 / subsidy_id で詳細取得",
    "jgrants-subsidy-search": "補助金検索 / 補助金 一覧 / 補助金スキャン / 業種別補助金 / J-Grants 検索",
    "kokai-competitor-brief-prompt": "競合 brief プロンプト / 競合調査 frame / 競合 brief framework",
    "kokai-due-diligence-prompt": "デューデリ プロンプト / 企業調査 frame / DD frame / デューデリジェンス framework",
    "kokai-subsidy-fit-prompt": "補助金マッチ プロンプト / 補助金 fit frame / 3 軸 fit framework",
    "kokai-subsidy-landscape-prompt": "補助金スキャン プロンプト / 補助金 landscape frame / Top-N 補助金 framework",
    "nta-corporate-name-search": "国税庁 法人名検索 / 法人番号取得 by 名前 / NTA 法人検索 / 名前から法人番号",
    "nta-corporate-number-lookup": "国税庁 法人番号 lookup / 異動履歴 確認 / 解散合併 確認 / 法人 master 取得 / NTA 法人番号",
    "search-egov-laws": "法令検索 / 日本法令 検索 / e-Gov 法令 / 法律 keyword 検索 / 業法 確認",
    "search-procurement-portal": "調達公告検索 / 入札公告 検索 / 官公需 検索 / CFT 検索 / 公共調達 検索",
    "shigyo-boundary-disclaimer": "士業 boundary / 士業 disclaimer / 専門家確認 disclaimer / 弁護士 / 行政書士 / 中小企業診断士 / 公認会計士 / 税理士 確認 disclaimer",
}

ROOT = r"C:\Users\keiji\Projects\kokai-oss-repo\plugins"

ok, skip, unknown = 0, 0, 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    if "SKILL.md" not in filenames:
        continue
    skill_name = os.path.basename(dirpath)
    if skill_name not in MAP:
        print(f"UNKNOWN_SKILL: {skill_name}  path={dirpath}")
        unknown += 1
        continue
    keywords = MAP[skill_name]
    suffix = f" 日本語 keyword: {keywords}."
    path = os.path.join(dirpath, "SKILL.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "日本語 keyword:" in content:
        print(f"SKIP_ALREADY: {path}")
        skip += 1
        continue
    new_content, n = re.subn(
        r"^(description: .+)$",
        lambda m: m.group(1) + suffix,
        content,
        count=1,
        flags=re.MULTILINE,
    )
    if n != 1:
        print(f"WARN_NO_MATCH: {path}")
        skip += 1
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"OK: {path}")
    ok += 1

print(f"\nDONE: ok={ok}, skip={skip}, unknown={unknown}")
