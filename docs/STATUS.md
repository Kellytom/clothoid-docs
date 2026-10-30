# Status

What works today, and what does not. This page is a summary; the dated detail is
in `HANDOFF.md`.

## Working

- **The app**, locally at `127.0.0.1:8000`: presets, caps, the design editor, the
  report, SVG and JSON download, and the clearance check.
- **The deployed copy**: HTTP 401 without the shared token, 200 with it; every
  route except `/health` is gated, and `/api/render` is rate-limited.
- **The engine**: 36 caps, terminals with seven shapes, junctions and fillets,
  sections, bundles, clearance.
- **The spine layer**: exact plans, closure, cusps, joins, mirrors, rails,
  placement, a float hybrid at 20,000 chords, and the 150 terminal frameworks.
- **The caps transfer**: 36 caps re-expressed on the spine with a median gap of
  0.44% of their length (worst 10.06% at 2-unit chords).

## Not wired

- **The spine layer is not imported by `clothoid_lab`.** Four conditions promote
  it; see `WORK.md`.
- **Terminals have frameworks but nothing consumes them yet** beyond the
  extractor and the transfer study.
- **Turned terminals** (past 120°) and a **clothoid junction blend** are not
  built.
- **The cloud study's figures** are partly omitted from the public copy because
  they embed photographs.

## Checks

Engine tests 215, spine tests 139, layout gate green, parity its own check. The
dates and carried values live in `HANDOFF.md`.
