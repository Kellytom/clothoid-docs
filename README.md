# clothoid-lab — documentation

This is the documentation subset of the private `clothoid-lab` repository,
published so that writers and reviewers can read the reasoning without access
to the deployment, the reference photographs, or the local tooling.

## What is here

- `docs/` — the current truth (`HANDOFF.md`), the durable reference
  (`HANDOVER.md`), the work backlog, and the subject notes: philosophy,
  clearance, junctions, primals, caps, the 3125 lattice, the web MVP.
- `docs/README.md` — which pages are handwritten and which are generated, and
  which script owns each generated page.
- `pythagorean-spiral/docs/` — the spine layer's own documents: the explainer,
  the gallery, the extremes, the transfer study, and the cloud studies.
- `AGENTS.md` — the working rules for agents in the full repository.

## What is not here

- The generated HTML twins, figures, and JSON data (they are build output of
  the scripts named in `docs/README.md`).
- `reference/` photographs, `out/`, and `vendor/`.
- Deployment identifiers, which are replaced with `<private deployment>`,
  `<gcp-project>` and `<billing-account>`.

## Reading order

1. `docs/README.md`
2. `docs/HANDOFF.md` — state and next move, carried from the private repo
3. `docs/HANDOVER.md` — architecture, only where durable
4. `docs/BACKLOG.md`, then the subject notes

The spine layer is a separate curve system from the clothoid engine: an Euler
polygon whose headings match a clothoid at the nodes, with rational points,
joins and mirrors. `pythagorean-spiral/docs/EXPLAINER.md` is the long version.

## Assets and examples

`assets/css/` holds the shared stylesheet and the app CSS; `examples/` holds
three runnable snippets (curl, ribbon, frames). `BUILDING.md` says which
pages rebuild here and which need the private repository.

## Repository layout

| Path | What it holds |
|---|---|
| `docs/` | Current truth, durable reference, backlog, subject notes, generated HTML. |
| `pythagorean-spiral/` | The spine layer: package, generators, its own docs and figures. |
| `clothoid_lab/` | The engine's Python: Piece, Trace, Contact, Section, Bundle, grammar. |
| `web/` | The local web MVP: stdlib server and static page. |
| `context/` | The plan, the vocabulary, the ornaments corpus, the house conventions, the board source. |
| `examples/` | Three runnable snippets. |
| `assets/css/` | The shared stylesheet and the app CSS. |

Project conventions: `CONTRIBUTING.md`. Licence: `LICENSE.md` (CC BY 4.0 for
prose and figures, MIT for code). Changes: `CHANGELOG.md`.
