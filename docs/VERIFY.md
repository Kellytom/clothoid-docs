# Verification

Four checks, each answering a different question.

## 1. The engine's tests

```sh
.venv/bin/python -m unittest discover tests
```

215 tests. They cover the model, segments, terminals, pieces, junctions,
clearance, the web API, auth and the board's principle cards. They are the
definition of "the engine works". Carried at 215 on 2026-10-27; the tree has
been clean under `web/`, `clothoid_lab/`, `csrc/` and `tests/` since.

## 2. The spine layer's tests

```sh
cd pythagorean-spiral && ../.venv/bin/python -m unittest discover -s tests -t .
```

139 tests: closure, the exponent dial, joins and forks, rails, the float hybrid,
placement, the exact curl's frozen digest. Last run 2026-10-29, all pass.

## 3. Parity between local and remote

```sh
.venv/bin/python scripts/check-parity.py
```

Compares the served assets, presets, caps, SVG and report between the local and
deployed copies. It needs both to be up, and it is never run from a handoff.

## 4. The layout gate

```sh
node scripts/check-web.mjs
```

Renders the docs pages and the app at 900, 390 and 320 pixels wide and fails on
horizontal overflow. It launches its own headless Chrome; `scripts/shot.mjs`
drives the persistent one on CDP 9223 for one-off screenshots.

## What passing does not mean

The tests say the code does what it says, not that the drawing is good. The
measured fit of the drawn cubics to the chain, the transfer gap of a cap, and
the veil's opacity are reported as numbers in the studies; they are not tests,
and they should be read.
