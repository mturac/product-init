# product-init

AI-first turnkey product delivery skill. It enforces an 8-gate pipeline
(Discovery -> SoW -> Build -> Real Wiring -> QA -> Deploy -> UAT/Warranty -> Handoff)
through a set of audit scripts under `scripts/`. Each audit returns structured
findings (severity, gate, check, evidence, fix) and a non-zero exit code when
any HIGH or CRITICAL issue is present.

## Install

The skill ships with a vendored virtualenv:

```
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
```

That is the venv the orchestrator already uses (`.venv/bin/python3`). No
global Python state is mutated.

## Run an audit

```
.venv/bin/python3 -B scripts/audit_constitution.py --project-dir /path/to/project
```

Every audit accepts `--project-dir <dir>` and `--json`. `audit_qa.py` is an
aggregator that runs all eight Gate 5 sub-audits and merges their findings.

## Auto-trigger

The keywords and phrases that auto-trigger this skill are documented in
`SKILL.md` (the canonical entry point). Look there for routing details.

## Dogfood CI

`.github/workflows/dogfood.yml` materializes a known-good fixture under
`/tmp/fixture` and asserts that gate1 and gate2 audits exit 0, plus a
syntax check across every `scripts/*.py`.
