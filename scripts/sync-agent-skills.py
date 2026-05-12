#!/usr/bin/env python3
"""
sync-agent-skills.py — Propagate skills from vertical-plugin to agent-plugins.

Each agent-plugin uses a subset of vertical-plugin skills, copied into
the agent's own skills/ directory (Anthropic financial-services pattern).

Source of truth: plugins/vertical-plugins/japan-public-business-intelligence/skills/
Destination: plugins/agent-plugins/<slug>/skills/

Configuration: AGENT_SKILL_BUNDLES below defines which skills each agent gets.
"""

import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VERTICAL_SKILLS = (
    REPO_ROOT / "plugins" / "vertical-plugins" / "japan-public-business-intelligence" / "skills"
)
AGENT_PLUGINS_DIR = REPO_ROOT / "plugins" / "agent-plugins"

AGENT_SKILL_BUNDLES = {
    "meeting-prep-jp": [
        "gbizinfo-company-search",
        "gbizinfo-entity-lookup",
        "kokai-due-diligence-prompt",
        "kokai-subsidy-landscape-prompt",
        "authority-strip-formatter",
        "shigyo-boundary-disclaimer",
    ],
    "subsidy-fit-jp": [
        "gbizinfo-company-search",
        "gbizinfo-entity-lookup",
        "jgrants-subsidy-detail",
        "kokai-subsidy-fit-prompt",
        "authority-strip-formatter",
        "shigyo-boundary-disclaimer",
    ],
    "due-diligence-jp": [
        "gbizinfo-company-search",
        "gbizinfo-entity-lookup",
        "evidence-citation-builder",
        "kokai-due-diligence-prompt",
        "authority-strip-formatter",
        "shigyo-boundary-disclaimer",
    ],
    "competitor-brief-jp": [
        "gbizinfo-company-search",
        "gbizinfo-entity-lookup",
        "kokai-competitor-brief-prompt",
        "authority-strip-formatter",
        "shigyo-boundary-disclaimer",
    ],
    "subsidy-landscape-jp": [
        "jgrants-subsidy-search",
        "kokai-subsidy-landscape-prompt",
        "authority-strip-formatter",
        "shigyo-boundary-disclaimer",
    ],
}


def sync_agent_skills(agent_slug, skill_names):
    agent_skills_dir = AGENT_PLUGINS_DIR / agent_slug / "skills"
    agent_skills_dir.mkdir(parents=True, exist_ok=True)
    for skill_name in skill_names:
        src = VERTICAL_SKILLS / skill_name
        dst = agent_skills_dir / skill_name
        if not src.exists():
            print(f"  ERROR: source skill {src} does not exist")
            return False
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"  synced {skill_name} -> {agent_slug}")
    return True


def main():
    print("Syncing vertical skills to agent-plugins...")
    all_ok = True
    for agent_slug, skill_names in AGENT_SKILL_BUNDLES.items():
        print(f"\n[{agent_slug}]")
        if not sync_agent_skills(agent_slug, skill_names):
            all_ok = False
    if not all_ok:
        print("\nSync FAILED.")
        sys.exit(1)
    print("\nAll agent skills synced successfully.")


if __name__ == "__main__":
    main()
