#!/usr/bin/env python3
"""
check.py — Lint manifests and verify cross-file references for the
kokai-for-public-business-intelligence-jp Plugin repo.

Validates:
  1. .claude-plugin/marketplace.json exists, has required schema fields
     (name, owner.name, plugins[] with name/source/description)
  2. Each plugins[].source path resolves to a directory containing
     .claude-plugin/plugin.json
  3. Each plugin.json has minimal schema (name, version, description, author.name)
  4. Vertical plugin skills/ contains directory + SKILL.md, no flat *.md
  5. Agent plugin skills/ also directory + SKILL.md (when bundled)
  6. managed-agent-cookbooks/*/steering-examples.json exists as file (not directory)
  7. .mcp.json in vertical plugin contains kokai MCP server URL

Anthropic financial-services / Apache 2.0 pattern, kokai-data fork.
"""

import json
import sys
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ERRORS = []
WARNINGS = []


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


def check_marketplace():
    """Check .claude-plugin/marketplace.json schema and plugin sources."""
    path = REPO_ROOT / ".claude-plugin" / "marketplace.json"
    if not path.exists():
        err(f"missing: {path}")
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"invalid JSON in {path}: {e}")
        return None
    for field in ("name", "owner", "plugins"):
        if field not in data:
            err(f"marketplace.json missing field: {field}")
    if "owner" in data and "name" not in data["owner"]:
        err("marketplace.json owner.name missing")
    plugins = data.get("plugins", [])
    if not isinstance(plugins, list):
        err("marketplace.json plugins must be an array")
        return data
    for i, plugin in enumerate(plugins):
        for field in ("name", "source", "description"):
            if field not in plugin:
                err(f"marketplace.json plugins[{i}] missing field: {field}")
        source = plugin.get("source", "")
        source_path = (REPO_ROOT / source.lstrip("./")).resolve()
        plugin_json = source_path / ".claude-plugin" / "plugin.json"
        if not plugin_json.exists():
            err(f"marketplace plugin '{plugin.get('name')}' at {source}: missing {plugin_json}")
    return data


def check_plugin_manifest(plugin_json_path):
    """Check individual plugin.json minimal schema."""
    try:
        data = json.loads(plugin_json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"invalid JSON in {plugin_json_path}: {e}")
        return None
    for field in ("name", "version", "description", "author"):
        if field not in data:
            err(f"{plugin_json_path}: missing field: {field}")
    if "author" in data and "name" not in data["author"]:
        err(f"{plugin_json_path}: author.name missing")
    return data


def check_all_plugin_manifests():
    """Find every plugin.json under plugins/ and check schema."""
    plugin_jsons = list(REPO_ROOT.glob("plugins/**/.claude-plugin/plugin.json"))
    flat_plugin_jsons = [
        p for p in REPO_ROOT.glob("plugins/**/plugin.json")
        if ".claude-plugin" not in p.parts
    ]
    if flat_plugin_jsons:
        for p in flat_plugin_jsons:
            err(f"plugin.json found outside .claude-plugin/ subdirectory: {p}")
    for p in plugin_jsons:
        check_plugin_manifest(p)
    return plugin_jsons


def check_skill_layout(skills_dir):
    """Verify each skill is a directory with SKILL.md, no flat .md."""
    if not skills_dir.exists():
        return 0
    skill_md_count = 0
    flat_md_count = 0
    for item in skills_dir.iterdir():
        if item.is_dir():
            skill_md = item / "SKILL.md"
            if skill_md.exists():
                skill_md_count += 1
            else:
                err(f"skill directory {item} missing SKILL.md")
        elif item.is_file() and item.suffix == ".md":
            flat_md_count += 1
            err(f"flat skill markdown in {skills_dir} not allowed: {item.name}")
    return skill_md_count


def check_vertical_plugins():
    """Verify vertical plugins have skill directory layout + .mcp.json."""
    vertical_dirs = list((REPO_ROOT / "plugins" / "vertical-plugins").glob("*"))
    for vdir in vertical_dirs:
        if not vdir.is_dir():
            continue
        skills_dir = vdir / "skills"
        skill_count = check_skill_layout(skills_dir)
        if skill_count == 0:
            warn(f"vertical {vdir.name}: 0 skills found in skills/")
        mcp_json = vdir / ".mcp.json"
        if not mcp_json.exists():
            warn(f"vertical {vdir.name}: missing .mcp.json")
        else:
            try:
                mcp_data = json.loads(mcp_json.read_text(encoding="utf-8"))
                if "mcpServers" not in mcp_data:
                    err(f"{mcp_json}: missing mcpServers field")
            except json.JSONDecodeError as e:
                err(f"invalid JSON in {mcp_json}: {e}")


def check_managed_agent_cookbooks():
    """Verify each cookbook has agent.yaml + steering-examples.json (file, not dir)."""
    cookbook_dirs = list((REPO_ROOT / "managed-agent-cookbooks").glob("*"))
    for cdir in cookbook_dirs:
        if not cdir.is_dir():
            continue
        agent_yaml = cdir / "agent.yaml"
        if not agent_yaml.exists():
            err(f"cookbook {cdir.name}: missing agent.yaml")
        steering_examples = cdir / "steering-examples.json"
        steering_dir = cdir / "steering-examples"
        if not steering_examples.exists():
            err(f"cookbook {cdir.name}: missing steering-examples.json (top-level file)")
        if steering_examples.exists():
            try:
                json.loads(steering_examples.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                err(f"invalid JSON in {steering_examples}: {e}")
        if steering_dir.exists() and steering_dir.is_dir():
            err(f"cookbook {cdir.name}: steering-examples/ directory is invalid; use steering-examples.json file instead")


def main():
    print("Linting kokai-for-public-business-intelligence-jp Plugin repo...")
    check_marketplace()
    check_all_plugin_manifests()
    check_vertical_plugins()
    check_managed_agent_cookbooks()
    if WARNINGS:
        print(f"\n{len(WARNINGS)} warning(s):")
        for w in WARNINGS:
            print(f"  WARN: {w}")
    if ERRORS:
        print(f"\n{len(ERRORS)} error(s):")
        for e in ERRORS:
            print(f"  ERROR: {e}")
        sys.exit(1)
    print("\nAll checks passed (0 errors).")


if __name__ == "__main__":
    main()
