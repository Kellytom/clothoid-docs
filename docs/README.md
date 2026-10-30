# docs

What is in this folder, which pages are generated, and where new writing belongs.

## Start here

| File | What it is |
|---|---|
| `HANDOFF.md` | Current truth: local, remote, tests, git, risks, next move. Written by `/fhandoff`; do not hand-edit the state lines. |
| `HANDOVER.md` | Durable reference: architecture, deploy, security, decisions. Long on purpose. |
| `BACKLOG.md` | Execution detail for W01–W26 (the work items on the board). |
| `REVIEW.md` | Architecture and print review; act after the current work. |
| `ARCHITECTURE.md` | How the engine and the spine layer fit, and what is not wired yet. |
| `WEB-GUIDE.md` | The browser workbench: controls, the design recipe, the status line, the limits. |

## Handwritten reference

| File | Subject |
|---|---|
| `PHILOSOPHY.md` | What a glyph is: parts, full lines, sections, joints. |
| `CLEARANCE.md` | The clearance/crossing rule and its limits. |
| `JUNCTION.md` | Junctions: vocabulary, fillet, what comes next. |
| `PRIMAL.md` | Fire, water, earth, air: the primal ornaments and their gate. |
| `caps.md` | Cap families and the 120° rule. |
| `clothoid-grid-3125.md` | The 3125 lattice and the old source pages. |
| `web.md` | The web MVP. |
| `PROJECT.md`, `TODO.md` | Older planning, kept for history. Do not treat as current. |

## Generated — change the generator, never the page

| Page | Generator |
|---|---|
| `ornament-board.html` | `scripts/board/build-board.mjs` |
| `fleur-studies.html` | `scripts/board/build-board.mjs` |
| `piece-model.html` | `scripts/piece_sandbox.py` |
| `fleur-study-01.html` | `scripts/study_01.py` |
| `primal.html` | `scripts/primal.py` |
| `principles.html` | `scripts/principles.py` |
| `terminals/index.html`, `terminals/*.json` | `scripts/extract-terminals.py` |
| `spirals/index.html`, `spirals/*.json` | `scripts/extract-spirals.py` |
| `HANDOVER.html` | mirror of `HANDOVER.md`, kept in step by hand |

## Conventions

- The app is **+y up**, page 200 × 250 mm. Recovered page data is stored as
  found, which is y-down — say so when you quote it.
- `W` numbers are work items and `P` numbers are plates; do not renumber them.
- Generated pages carry links back to the board; keep that shape when adding
  one.
- The spike has its own docs and its own generators:
  `pythagorean-spiral/docs/` (`EXPLAINER`, `GALLERY`, `EXTREMES`, `TRANSFER`,
  `CLOUD`, `CLOUD-FORM`), each with an HTML twin and a `scripts/*.py` source.
- New handwritten docs go here as `docs/<subject>.md`. New generated docs get a
  script, a line in the table above, and a note in the script's docstring.
