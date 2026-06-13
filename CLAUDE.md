# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

`parish-scripts` ("Church Files") is currently a **document repository**, not a
code project. There is no build system, package manifest, source tree, or test
suite yet — only Markdown documents and supporting assets. Treat tasks here as
documentation/content work unless and until code is introduced.

Current contents:
- `swing-analysis/swing-scorecard.md` — a manual baseball swing-analysis
  checklist (the bulk of the meaningful content).
- `keypad2.pdf` — a binary asset (~860 KB); do not attempt to edit it as text.
- `README.md` — one-line description only.

The `.gitignore` excludes `node_modules/`, `.env`, and `*.log`, signalling that
Node-based tooling is anticipated. If/when you add it, create the corresponding
`package.json` and document the build/lint/test commands in this file.

## Key domain context: the swing scorecard

`swing-analysis/swing-scorecard.md` is the most important document and is
deliberately written as a **dual-purpose spec**:

1. A low-tech, by-eye checklist a rec-league hitter uses today (the
   "Wizard-of-Oz" manual workflow).
2. The product spec for a future automated pose-estimation tool — every "You
   see" cue is meant to map to something a model can measure, and every
   threshold is a tunable number.

When working on this file or building tooling from it, preserve that mapping:
the document is organized around **6 named "swing-killers"**, each scored
**OK / Minor / Major**, with a fixed structure (What / You see / Quick check /
Cue / Drills) and a designated camera angle (face-on vs. behind). Keep that
structure and the numeric thresholds intact — they are the de-facto schema any
future automated scorer should follow. The document's own stance is to "catch
the big, obvious swing-killers," not to chase precision; honor that scope and
its honest caveats (rotational-vs-linear coaching disagreements) rather than
presenting thresholds as settled fact.

## Workflow conventions

- Work happens on feature branches named `claude/<topic>`; changes reach `main`
  via pull request (see the merged PR #1 in the history). Do not commit directly
  to `main`.
- Commit messages are short and imperative ("Add manual rec-league swing
  scorecard (v0)").

## When adding code

This repo has no established stack yet. Before introducing one, prefer the
direction the `.gitignore` already implies (Node/JavaScript). Whatever you
choose, update this file with the actual build, lint, test, and single-test
commands so future sessions don't have to re-derive them.
