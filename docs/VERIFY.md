# Verification

Four checks. Each answers one practical question, and each can fail on its own.

## 1. Does the curve engine still work?

```sh
.venv/bin/python -m unittest discover tests
```

215 tests: curve geometry, pieces, ends, junctions, clearance, the web API, the
shared-token gate, and the work board's principle cards. When they pass, the
engine still does what it says.

*Status:* carried from 2026-10-27; nothing under `web/`, `clothoid_lab/`,
`csrc/` or `tests/` has changed since.

## 2. Does the spine layer still work?

```sh
cd pythagorean-spiral && ../.venv/bin/python -m unittest discover -s tests -t .
```

139 tests: exact closure, the exponent dial, joins and forks, the rails, large
drawings in ordinary decimals, placement, and a frozen digest of the legacy curl
so its shape cannot drift by accident.

*Status:* last run 2026-10-29, all passing.

## 3. Do the local and deployed copies match?

```sh
.venv/bin/python scripts/check-parity.py
```

Compares the served files, presets, caps, the drawing and the report between the
local server and the deployed copy. Both must be running. This is a standalone
audit and is never run during a handoff.

## 4. Do the pages fit small screens?

```sh
node scripts/check-web.mjs
```

Draws the documentation pages and the app at 900, 390 and 320 pixels wide, and
fails if anything overflows sideways. It starts its own headless Chrome; single
screenshots use `scripts/shot.mjs` and the long-running browser on port 9223.

## What passing does not mean

Passing shows the code follows its rules without crashing or breaking an
invariant. It says nothing about how the result looks:

- how naturally a curve sweeps along its chords;
- how closely a transferred cap matches its source plate;
- how a veil or a fill reads to the eye.

Those are recorded as measured studies in the documentation. Read the numbers
there; they are evidence, not tests.
