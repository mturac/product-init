#!/usr/bin/env python3
"""Materialize a known-good gate1+gate2 fixture project for the dogfood CI."""
from __future__ import annotations

import sys
from pathlib import Path

FILES = {
    "PRODUCT.md": """---
name: Fixture Product
description: Dogfood fixture for product-init audits
golden_path_step: 1
version: 0.1.0
---

# Product

## Golden Path

A user signs up, uploads one CSV, and downloads a scored shortlist.

## Persona

Recruiter at a 50-person agency, screens 200 CVs/week, lives in Gmail.

## Outcome Metric

Time-to-shortlist drops from 6 hours to 30 minutes per role.

## Current Alternative

Manual review in Excel.

## 10-minute Success

User completes upload + download within 10 minutes of signup.

## Riskiest Assumption

Recruiters trust an AI score enough to skip first-round phone screens.

## Four-Risk Snapshot (value, usability, feasibility, viability)

Value medium, usability high, feasibility high, viability medium.
""",
    "SPEC.md": """---
name: Fixture Spec
description: Scope and acceptance for fixture
golden_path_step: 1
version: 0.1.0
---

# Spec

## Scope

Single golden-path slice: signup -> upload CSV -> view shortlist.

## Acceptance

AC-1 user uploads CSV under 10 MB. AC-2 shortlist renders in under 5 seconds.
""",
    "PLAN.md": """---
name: Fixture Plan
description: Shape-up pitch for fixture
golden_path_step: 1
version: 0.1.0
---

# Plan

## Appetite

4 weeks. Budget: $15k.

## Kill Criteria

- If recruiter NPS for the score is below 4/10 at week 2, kill.
- If model latency exceeds 8s p95, kill.

## Rabbit Holes

Avoid building a custom auth layer; use a managed provider.

## Deferred

- RBAC for multi-tenant orgs
- compliance audit log retention beyond 30 days
- marketplace listing on partner portals
- multi-region deploy
- observability beyond Sentry default
- integrations with ATS vendors

## Discovery Cadence / Weekly Touchpoint

Weekly recruiter call every Wednesday 30 min.
""",
    "TASKS.md": """---
name: Fixture Tasks
description: Active MVP task list
golden_path_step: 1
version: 0.1.0
---

# Tasks

- T1 implement signup with magic link
- T2 implement CSV upload endpoint
- T3 implement scoring pipeline
- T4 implement shortlist UI
""",
    "COMPETITIVE_BENCHMARK.md": """---
name: Fixture Benchmark
description: v0/Bolt/Lovable/Railway snapshot
golden_path_step: 1
version: 0.1.0
---

# Benchmark

## v0

Strong on UI generation; weak on data pipelines.

## Bolt

Good for quick prototypes; deploy story unclear for production CSV ingestion.

## Lovable

Polished templates; limited backend customization.

## Railway

Solid hosting baseline for our managed Postgres + worker.
""",
}


def main() -> int:
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/fixture")
    target.mkdir(parents=True, exist_ok=True)
    for name, body in FILES.items():
        (target / name).write_text(body, encoding="utf-8")
    print(f"fixture built at {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
