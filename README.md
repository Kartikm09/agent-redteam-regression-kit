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
PYTHONPATH=src python -m redteam_kit.scenarios examples/scenarios.json
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

## Verification

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

The CLI exits 1 when observed flags differ from a fixture's expected flags, or
when no scenarios are supplied. Matching negative examples are successful
regression checks. Phrase matching is case-insensitive, remains heuristic and
does not prove comprehensive prompt-injection resistance or live tool safety.
