# Work items, plates and the board

The project keeps three lists, and they are easy to confuse.

- **P** numbers are **plates**: pictures on the ornament board. There are 85.
- **W** numbers are **work items**: jobs to be done. There are 26.
- **D** numbers are **decisions**: choices already made, with the reasons. There
  are 11.

The board is `docs/ornament-board.html`, built by
`scripts/board/build-board.mjs`; the twenty fleur studies are its subpage.
`BACKLOG.md` holds the detail behind each work item.

## The plates

| Range | What they are |
|---|---|
| P01–P20 | the twenty fleur studies |
| P21–P65 | catalogue ornaments |
| P66–P92 | class I caps |
| P93–P101 | class II leaves |
| P102–P105 | presets |

## The order of work

1. **W01 — the piece model.** One drawing holding several named lines. Done.
2. **W02 — the ends.** Caps and tapers, with the 120° rule for what counts as a
   cap. The main shapes are done; turned ends are not.
3. **W03 — the fleur grammar.** Study 01 ported to the new model. The next
   action is the canonical fleur.
4. **W04 — the twenty parameter sets.**
5. **The primals** — earth, water, air, fire, in that order, because fire needs
   the turned ends.
6. **The archetypes** — fleur, acanthus, palmette.

## What would make the spine layer part of the tool

The spine layer is central to the curve work, but it is not connected to the app
yet. Four conditions promote it, and all four must hold:

1. The engine can read a spine and build a drawing from its points.
2. One spine is drawn on the 200 × 250 mm sheet, upward, by the normal writer.
3. The clearance check measures it, and one declared touch passes.
4. One fleur study is drawn entirely from these chains.

Until then, "central" describes the intention, not the software.

The gate is repeated in `PLAN` and `ARCHITECTURE` on purpose: it decides the
order of work.
