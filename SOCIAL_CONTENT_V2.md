# product-init — Social Content v2 (Research-Backed)

## Research findings applied

| Viral tool | What actually worked | Applied here |
|---|---|---|
| htmx | Meme strategy + tribal identity ("you don't need React") | Contrarian position: "vibe-coding without product structure IS the new tech debt" |
| Bun | Benchmark numbers designed to be screenshot-worthy | Gate audit output as the "benchmark" — pass/fail is the number |
| shadcn/ui | One counterintuitive claim ("this is not a component library") | "This is not a project scaffolder" |
| Boris Cherny | Specific numbers + 100% claim + challenges identity | "3 products shipped, 0 spec docs written manually" |
| Railway | Named the void (Heroku death) | Name the void: "vibe-coding has a PMF-shaped hole" |
| Zed | Credibility transfer + waitlist scarcity | Research citations are credibility (CB Insights 43%) |

---

## LAUNCH TWEET (single tweet, cold launch)

```
I've shipped 3 products this month.

I wrote zero product specs, test configs, or CI setups manually.

One command. 9 hard gates. A deployed URL at the end.

github.com/mturac/product-init
```

**Why this works:** Boris Cherny formula. "I did X without doing Y" + specific number + one-sentence mechanism + link. No thread. No explanation. The link does the work.

---

## THE CONTRARIAN IDENTITY TWEET (this is the htmx play)

```
Vibe-coding without a product spec isn't moving fast.

It's building the wrong thing at the speed of AI.

43% of startups die from this. Not from bad code.
```

**No link. No CTA. Pure position statement.**
Reply 48h later: "I built a system that makes it structurally impossible to start building before the product is validated. 9 hard gates. Thread →"

---

## THE BORIS CHERNY FORMAT (numbers tweet)

```
This month:
- 3 products shipped
- 9 gates passed per product
- 0 CRITICAL audit findings unresolved
- 1 session each

I didn't write a single test config or deploy script manually.

product-init — Claude Code skill
```

---

## THE OUTPUT TWEET (show don't tell)

```
This is what /product-init looks like after Gate 5:

[GIF: terminal showing unit tests → integration tests → E2E, all green, gate unlocking]

Not "mostly passing."
Not "known flake, ignore."
Green.
```

**Annotation on GIF:** Each frame shows a different test suite finishing. Audio: keyboard clicks. 15 seconds max.

---

## THE COUNTERINTUITIVE CLAIM (shadcn play)

```
product-init is not a project scaffolder.

A scaffolder gives you files.
This gives you a reason to have files.

The spec comes before the code. Always.
```

---

## THE COMPETITOR COMPARISON (Bun play — designed to be debatable)

```
v0 → UI components
Bolt → full-stack app
Lovable → polished UI
Cursor → AI code editor
product-init → the thing before all of those

Different category.
```

---

## SHOW HN POST (second-day move, after Twitter traction)

**Title:** `Show HN: product-init – Claude Code skill that gates your build behind product validation`

**Body:**
```
Hi HN,

I built product-init after watching too many well-engineered products die because 
nobody validated the problem first. CB Insights puts "no market need" at 43% of 
startup failures — not bad code, not running out of money. Wrong product.

product-init is a Claude Code skill (works on Codex CLI and OpenClaw too). When 
you type /product-init "build an HR assessment tool", it runs 9 gates in sequence:

  Gate 1: Discovery Constitution (JTBD + four-risk model — blocks Gate 2 until green)
  Gate 2: Statement of Work (Shape Up appetite, Amazon PR-FAQ format)
  Gate 3: Design (every screen must map to a job from Gate 1)
  Gate 4: Build
  Gate 5: QA (unit + integration + E2E — all three, all green)
  Gate 6: UAT (real human signs off)
  Gate 7: Deploy (HTTP 200 to prod URL, not "it should be fine")
  Gate 8: Handoff (ADRs, runbook, rollback — a contract, not a README)
  Gate 9: Warranty (72-hour monitoring window, error rate + latency + uptime)

CRITICAL findings block the next gate. There is no --skip flag.

I dogfooded it last week and shipped an AI-powered HR interview tool in one session. 
Live at demorpoject.vercel.app. All 9 gates passed. Handoff package signed.

The audit scripts are plain Python. No magic. The methodology is public:
CB Insights, Christensen JTBD, Basecamp Shape Up, Amazon PR-FAQ, Cagan four-risk.

GitHub: github.com/mturac/product-init
```

**Day-of rules:** Post 9am ET Tuesday/Wednesday. Reply to every comment in first 2 hours. Have 3 prepared answers: "why not just use a checklist?", "what if the spec is wrong?", "does this work without Claude Pro?"

---

## MEME STRATEGY (htmx long-game)

**Recurring format to build tribal identity:**

```
[image: developer confidently vibe-coding]
Caption: me shipping before Gate 1 is green
```

```
Ship fast → fail from PMF
(same thing)
```

```
"our AI wrote 50,000 lines in a week"
also us: [no users]

Gate 1 would have caught this.
```

```
Claude Code skill that asks "who is this for"
before it writes a single line: product-init

Claude Code skill that just builds whatever
you described: everything else
```

---

## VIDEO SCRIPT v2 (upgraded — Boris Cherny formula)

**[0:00–0:03]** Black screen, white text:
> "I shipped 3 products this month. I didn't write a single spec document manually."

**[0:03–0:08]** Terminal appears. Cursor blinks.
> Voice: "One command."
> Type: `/product-init "build an HR assessment tool"`

**[0:08–0:15]** Three questions flash. Answers typed.
> Voice: "Three questions. The AI drafts the rest."

**[0:15–0:28]** Fast-cut: each gate label flashes, audit script runs, green checkmark.
> Voice: "Nine gates. Each one has a Python script. CRITICAL findings block the next gate."
> On screen: `Gate 5: unit ✓ integration ✓ E2E ✓`

**[0:28–0:40]** Cut to live product. Interview room. Dashboard. Report.
> Voice: "This is what came out. One session."

**[0:40–0:50]** Browser bar: `demorpoject.vercel.app` → 200 OK.
> Voice: "Gate 7 checks the prod URL. Not 'it works locally.' Two hundred."

**[0:50–0:58]** Terminal again. Single line:
> `CRITICAL: 0  HIGH: 0  All gates: green`
> Voice: "43% of startups die from no PMF. This is the system I built to not be one of them."

**[0:58–1:00]** Text: `product-init — github.com/mturac/product-init`

---

## SCREENSHOT CAPTIONS v2 (upgraded)

**home-desktop.png**
```
"Hire on evidence, not on a feeling."

This app didn't exist 24 hours ago.

/product-init → 9 gates → prod URL.
The spec came before the first component.
```

**screen-interview.png**
```
LIVE. 15:34. AI interviewer running.

This screen exists because Gate 3 asked:
"what job is the hiring manager hiring this for?"

The dark cinematic UI isn't a design choice.
It's what happens when the design gate knows
who's in the room.
```

**dashboard.png**
```
Scores: 84. 91. Pending. Complete.

Not vibes. Not gut calls.
Four weighted dimensions, validated in UAT
before Gate 7 opened.

Built in one session with product-init.
```

**report.png**
```
Problem Solving: 91
Communication: 84
Technical: 88
Cultural Alignment: 82

Each dimension traced back to a job-to-be-done
captured in Gate 1.

This is what it looks like when the spec
comes before the code.
```

**create.png**
```
The form only has the fields that belong in the appetite.

Shape Up discipline: if it's not in the golden path,
it's not in the MVP.

Gate 2 blocked the rest.
```

---

## CONTENT CALENDAR (first 2 weeks)

| Day | Platform | Format | Content |
|-----|----------|--------|---------|
| Day 1 morning | Twitter/X | Single tweet | LAUNCH TWEET (numbers + link) |
| Day 1 evening | Twitter/X | Thread | 9-gate walkthrough with terminal screenshots |
| Day 2 morning | HN | Show HN | Full Show HN post |
| Day 2 | Twitter/X | Single tweet | THE CONTRARIAN (no link) |
| Day 3 | LinkedIn | Long post | "We built a full HR tool in one session" story |
| Day 4 | Twitter/X | GIF | Gate 5 test runner (output tweet) |
| Day 5 | Twitter/X | Single tweet | COMPETITOR COMPARISON |
| Day 7 | Twitter/X | Meme | First tribal identity meme |
| Day 8 | Twitter/X | Thread | "The research behind product-init" (CB Insights + JTBD + Shape Up) |
| Day 10 | Product Hunt | Launch | After HN traction validates the positioning |
| Day 14 | Twitter/X | Single tweet | THE COUNTERINTUITIVE CLAIM (shadcn play) |

**Rule: never post two "features" in a row. Alternate: position → demo → story → meme → position.**
