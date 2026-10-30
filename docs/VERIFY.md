# Verification

Four checks, each answering a different question.

## 1. Does the engine still do what it says?

```sh
.venv/bin/python -m unittest discover tests
```

215 tests: the model, pieces, ends, junctions, clearance, the web API, the
password gate, and the work board's principle cards. This is the definition of "the
engine works". The count is carried from 2026-10-27; nothing under `web/`,
`clothoid_lab/`, `csrc/` or `tests/` has changed since.

## 2. Does the spine layer still do what it says?

```sh
cd pythagorean-spiral && ../.venv/bin/python -m unittest discover -s tests -t .
```

139 tests: closure, the exponent dial, joins and forks, rails, large drawings,
placement, and a frozen digest of the old curl so it cannot change by accident.
Last run 2026-10-29, all passing.

## 3. Do the local and deployed copies agree?

```sh
.venv/bin/python scripts/check-parity.py
```

It compares the served files, presets, caps, drawing and report between the two
copies. Both must be running. It is its own check and is never run during a
handoff.

## 4. Do the pages fit the screen?

```sh
node scripts/check-web.mjs
```

Draws the documentation pages and the app at 900, 390 and 320 pixels wide, and
fails if anything sticks out sideways. It starts its own headless Chrome;
`scripts/shot.mjs` uses the long-running one on port 9223 for single screenshots.

## What passing does not mean

The tests show the code does what it claims. They do not judge the drawing. How
closely the drawn curves follow the chain, how far a transferred cap drifts, and
how opaque the veil is are reported as numbers in the studies — read them; they
are not tests.
