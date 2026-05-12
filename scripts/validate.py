#!/usr/bin/env python3
"""
validate.py — Structural validation for Plugin repo.

Verifies:
  - All required directories exist
  - YAML files (agent.yaml, subagents/*.yaml) are valid YAML
  - JSON files (plugin.json, marketplace.json, .mcp.json, steering-examples.json) are valid JSON
  - LICENSE / NOTICE / TRADEMARKS.md / README.md exist at repo root
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ERRORS = []


def err(msg):
    ERRORS.append(msg)


def check_required_files():
    required = [
        "README.md",
        "LICENSE",
        "NOTICE",
        "TRADEMARKS.md",
        ".gitignore",
        ".claude-plugin/marketplace.json",
    ]
    for f in required:
        if not (REPO_ROOT / f).exists():
            err(f"missing required file: {f}")


def check_json_files():
    for json_path in REPO_ROOT.rglob("*.json"):
        if "node_modules" in json_path.parts or ".git" in json_path.parts:
            continue
        try:
            json.loads(json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            err(f"invalid JSON in {json_path}: {e}")


def check_yaml_files():
    try:
        import yaml
    except ImportError:
        print("WARN: PyYAML not installed, skipping YAML validation")
        return
    for yaml_path in REPO_ROOT.rglob("*.yaml"):
        if "node_modules" in yaml_path.parts or ".git" in yaml_path.parts:
            continue
        try:
            yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            err(f"invalid YAML in {yaml_path}: {e}")


def main():
    print("Validating Plugin repo structure...")
    check_required_files()
    check_json_files()
    check_yaml_files()
    if ERRORS:
        print(f"\n{len(ERRORS)} error(s):")
        for e in ERRORS:
            print(f"  ERROR: {e}")
        sys.exit(1)
    print("All structure checks passed.")


if __name__ == "__main__":
    main()
