# Agent Red-Team Regression Kit

Small red-team and regression test kit for AI agents that use tools, browse interfaces, or follow multi-step workflows.

This project is designed for portfolio-safe AI safety, red teaming, and tool-use evaluation proof. It uses synthetic scenarios only.

## What It Tests

- Prompt injection resistance.
- Tool-call boundary violations.
- Unsafe shortcut recommendations.
- Data exfiltration attempts.
- Hallucinated permissions.
- Missing human-confirmation steps.
- Multi-step workflow drift.

## Quick Start

```bash
python -m redteam_kit.scenarios examples/scenarios.json
```

## Skills Demonstrated

- AI red teaming
- Prompt injection testing
- Tool-use safety evaluation
- LLM evaluation
- Risk taxonomy design
- Python regression testing
- High-signal bug reporting

## Portfolio Note

The test cases are synthetic and safe to publish. They demonstrate red-team thinking without exposing confidential client prompts or production traces.
