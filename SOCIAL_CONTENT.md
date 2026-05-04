# product-init — Social Media Content Pack

---

## Twitter/X Launch Thread

**Tweet 1 (hook)**
43% of startups die without PMF. Not from bad code. From building the wrong thing.

I built a system that won't let that happen. One command. 9 hard gates. A shipped product at the end.

🧵

---

**Tweet 2**
`/product-init "build an HR assessment tool"`

That's the input. Three questions later, the AI drafts the full spec. Then the gates run.

You don't touch anything until they're green.

---

**Tweet 3**
The 9 gates:

```
1 ▸ Discovery Constitution
2 ▸ Statement of Work
3 ▸ Design
4 ▸ Build
5 ▸ QA (unit + integration + E2E)
6 ▸ UAT
7 ▸ Deploy
8 ▸ Handoff
9 ▸ Warranty
```

Each one has a Python audit script. CRITICAL findings block the next gate. No skipping.

---

**Tweet 4**
Gate 1 isn't "what are we building."

It's "who gets fired if this fails, what job are they hiring it for, and what does failure look like in production."

Christensen's JTBD + Cagan's four-risk model baked into a prompt you can't override.

---

**Tweet 5**
Gate 5 is where most AI tools die quietly.

unit tests → integration tests → E2E

All three. All green. Or the gate doesn't open. Not "good enough." Green.

---

**Tweet 6**
What we built with it in one session:

Assessment. — an AI-powered HR interview tool.
- Dark cinematic interview room UI
- Live 15-minute sessions
- Scored PDF reports across 4 dimensions
- Live on Vercel

One session.

---

**Tweet 7**
v0 gives you a button.
Bolt gives you a layout.
Lovable gives you a vibe.

product-init gives you: tests green, CI wired, prod URL, handoff package signed.

Different category.

---

**Tweet 8**
The handoff package at Gate 8:

- Architecture decision records
- Runbook
- Rollback procedure
- Signed-off by audit script

Not a README. A contract.

---

**Tweet 9**
Gate 9 is Warranty.

72-hour monitoring window post-deploy. Error rate, latency, uptime. Script checks all three.

If anything spikes, it blocks the session from closing. Most tools call that "done." This calls it "pending."

---

**Tweet 10**
Runs on:
- Claude Code
- Codex CLI
- OpenClaw / Hermes

Any AI runtime that can execute shell. No platform lock.

---

**Tweet 11**
The research stack it's built on:

📖 CB Insights — 43% PMF failure rate
📖 Christensen — JTBD
📖 Basecamp — Shape Up
📖 Amazon — PR-FAQ
📖 Cagan — four-risk model

These aren't vibes. They're gates with passing criteria.

---

**Tweet 12 (CTA)**
product-init is a Claude Code skill. Open source. Free to use.

If you've ever shipped something fast and watched it die slow, this is what I built instead.

→ github.com/mturac/product-init

---

## 5 Standalone Hooks

**Hook 1 — PMF stat**
43% of startups don't fail from bad code.

They fail from building the wrong thing perfectly.

One system that won't let you start Gate 2 until Gate 1 is green.

---

**Hook 2 — Multi-runtime**
Claude Code, Codex CLI, OpenClaw, Hermes.

One skill. Any AI runtime that executes shell. No platform lock. Your workflow, not mine.

---

**Hook 3 — Hard gates**
"Good enough" is a CRITICAL finding.

product-init has a Python audit script for that. It blocks Gate 5 until every test suite is green. Not mostly. Green.

---

**Hook 4 — Before/after**
Before: ship fast, iterate on what's broken in prod.

After: nine gates, each blocked by an audit script, prod URL live, handoff signed, warranty window clean.

Same speed. Different definition of done.

---

**Hook 5 — Audit scripts**
The audit scripts don't give feedback.

They return pass or fail. CRITICAL findings stop the pipeline. There's no "acknowledge and continue."

That's the feature.

---

## Short-form Video Script (60 seconds)

**[0:00–0:05]** Terminal on screen
> "One command. One session. A shipped product."

**[0:05–0:12]** Type the command
> "I type: `/product-init 'build an HR assessment tool'`. Three questions come back."

**[0:12–0:20]** Gates firing (fast scroll, green checkmarks)
> "I answer them. Nine gates run automatically — Discovery, Spec, Design, Build, QA, UAT, Deploy, Handoff, Warranty."

**[0:20–0:30]** Gate 5 test runner
> "Gate 5 is where most AI tools fall apart. Unit tests, integration tests, E2E — all three suites, all green. No skipping."

**[0:30–0:42]** Live product (interview room, dashboard, report)
> "What came out: Assessment. AI-powered interview tool. Dark interview room. Live sessions. Scored PDF reports."

**[0:42–0:50]** Browser → prod URL
> "Live on Vercel. One session. All gates passed."

**[0:50–1:00]** Closing
> "v0 gives you a component. product-init gives you a product. Open source. Link in bio."

---

## Screenshot Captions

**home-desktop.png**
"Hire on evidence, not on a feeling."
Four scored dimensions. One session. No gut calls dressed up as process.

**screen-interview.png**
This is what Gate 3 produces when Gate 1 did its job.
Dark cinematic interview room. AI interviewer live. 15 minutes on the clock. Every question tied to the job spec. Not a template. A product.

**dashboard.png**
This is what the hiring manager sees.
Not a transcript. Not "cultural fit: good." Scored. Comparable. Exportable.
Built in one session because the spec was locked before the first line of code.

**report.png**
Problem Solving 91 / Communication 84 / Technical 88 / Cultural 82.
These aren't vibes. Weighted scores, validated in UAT, signed off before Gate 7 opened.

**create.png**
Gate 1 asks: what job is the hiring manager hiring this form to do?
The answer is in the field labels. Only what belongs in the appetite.

---

## Product Hunt

**Tagline**
product-init — from raw idea to shipped product, in one session, through 9 hard gates.

**Description (260 chars)**
Type your idea. Answer 3 questions. Nine Python-audited gates run: Discovery → SoW → Design → Build → QA → UAT → Deploy → Handoff → Warranty. CRITICAL findings block progress. No skipping. Works on Claude Code, Codex CLI, Hermes.

---

## LinkedIn Post

**We built a full AI-powered HR assessment tool in one session. Here's the system that made it possible.**

Last quarter I watched a team spend six weeks building a candidate evaluation platform. Solid engineers. Decent spec. Shipped on time.

Dead in three months.

Not because the code was bad. Because nobody had validated that hiring managers would change their workflow to use it. Classic PMF miss. CB Insights has it at 43% — the single biggest cause of startup failure, ahead of running out of money, ahead of team problems.

I've been on the wrong side of that number. I decided to build a system that makes it structurally harder to get there.

**What product-init is**

It's a single Claude Code skill. You type `/product-init "build an HR assessment tool"` and three questions come back. From your answers, the AI drafts the rest. Then nine gates run, in sequence, each one blocked by a Python audit script with actual pass/fail criteria.

**The nine gates**

Gate 1 is the Discovery Constitution. Before a single line of code is specced, the system runs Christensen's JTBD framework and Cagan's four-risk model. CRITICAL findings block Gate 2. No override flag.

Gate 2 is the Statement of Work. Basecamp's Shape Up vocabulary: appetite, not deadline. Amazon's PR-FAQ format. The audit script checks that every success metric is measurable.

Gate 5 is QA. Unit tests, integration tests, E2E — all three suites, all green. Not "mostly green." This is where most AI-generated codebases fail silently.

Gate 8 is Handoff. Architecture decision records, runbook, rollback procedure. Not a README. A contract.

Gate 9 is Warranty. 72-hour monitoring window. If any metric spikes, the session stays open.

**What we built with it**

Assessment. — an AI-powered HR interview tool. Dark cinematic interview room. Live 15-minute sessions. Scored PDF reports across four dimensions. Live on Vercel. One session. All gates passed.

**The 43% failure rate isn't a mystery. It's a gap between "we shipped" and "we validated." product-init closes that gap with a script.**

→ github.com/mturac/product-init
