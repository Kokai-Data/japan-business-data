# kokai-due-diligence-jp (Managed Agent Cookbook)

Headless Japanese company due diligence agent for Claude Managed Agents API. Suitable for batch / overnight DD jobs on multiple Japanese companies.

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
scripts/deploy-managed-agent.sh kokai-due-diligence-jp
```

## Architecture

3-subagent orchestration (Anthropic financial-services pattern):

1. **company-resolver**: name / 法人番号 → verified corporate_number
2. **evidence-collector**: corporate_number → gBizINFO entity + subsidies + evidence_refs
3. **brief-composer**: evidence_bundle → 1-page cited brief with authority strip + 士業 disclaimer

## MCP server dependency

- `kokai` at `https://mcp.kokai.ai/functions/v1/mcp-server`
- Tools: `search_company`, `get_entity_profile`, `search_subsidies`, `get_subsidy_detail`, `get_evidence_refs`
- Prompts: `kokai_due_diligence_jp`, `kokai_competitor_corporate_brief_jp`

## Security notes

- All tool calls audit-logged in Claude Console
- All outputs cited from public canonical sources only
- 士業 boundary disclaimer in every brief
- Long-running sessions for multi-hour batch jobs supported

## Steering examples

See [steering-examples.json](./steering-examples.json) for handoff_request and response examples.

## Boundary

Output is signal / 確認材料 / context — NOT a decision. DD conclusions / investment decisions / legal judgment require certified Japanese 士業 (公認会計士 / 弁護士 / 行政書士).

## License

Apache License 2.0 — see repo root [LICENSE](../../LICENSE).
