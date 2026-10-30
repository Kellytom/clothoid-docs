# The recovered corpus

The project began with two historical ornament sources drawn with cubic Bézier
curves: the **Stage II plates** and the **LAC (log-aesthetic curve) page**. We
extracted their terminal ends and centrelines into structured data. The source
repository and its photographs are private; no photograph is published here.

## Spans, spines and plates

These three words nest from part to whole:

- A **span** is one cubic Bézier between two nodes — one piece of a line.
- A **spine** is an ordered run of continuous spans — the complete centreline of
  one drawn band.
- A **plate** is one source sheet or layout, holding one or more spines.

In one line: **span (a piece) → spine (a line) → plate (a sheet)**.

## Curve families

Each **spine** is tagged with the curve family it approximates. The tag belongs
to the whole spine, not to a single span or plate.

| Tag | In plain words |
|---|---|
| `line` | a straight run |
| `arc` | part of a circle |
| `euler` | an Euler spiral: the clothoid this project draws |
| `logaesthetic` | a curve whose rate of bending follows a fixed aesthetic ratio |
| `reflected` | a mirrored copy of another spine |
| `hyperbezier` | a different curve family from the source page; **not** a clothoid |
| `member` | one stroke inside a composite group, such as a leaf in a cluster |

### How the plates are distributed

- **Stage II:** 19 of the 20 plates mix families. The only single-family sheet is
  **Fig. 7**, which is `euler` throughout. No plate is only lines or only arcs.
- **LAC page:** every plate is single-family by design — 30 `logaesthetic`
  plates and one `arc` plate.

## What was recovered

| Source | Plates | Spines | Spans | Ends |
|---|---:|---:|---:|---:|
| Stage II | 20 | 90 | 586 | 88 |
| LAC page | 31 | 31 | 306 | 62 |

Across the 90 Stage II spines: `euler` 37, `logaesthetic` 16, `line` 12,
`hyperbezier` 8, `member` 8, `arc` 6, `reflected` 3.

## How close each family is to a clothoid

Fitting one clothoid to each spine gives a parity measurement: the typical
(median) error as a fraction of one chord, and the worst case.

| Family | Typical error | Worst |
|---|---|---|
| `line` | 0.00% | — |
| `arc` | 0.02% | — |
| `euler` | 0.01% | 0.12% |
| `logaesthetic` | 0.01% | 0.16% |
| `member`, `reflected` | 0.03% | — |
| `hyperbezier` | 35.8% | 78 chords |

`hyperbezier` is expected to diverge: it is a different kind of curve, and the
measurement records that rather than smoothing it over.

## What an end record holds

An **end** is one cut end of a band: the join where it leaves the body, the tip,
and the join where it returns. Each record holds a few cubic spans and:

| Field | Meaning |
|---|---|
| `spans` | the cubic pieces that form the end |
| `end` | which end of the band it is: `near` or `far` |
| `plate` | the source plate it came from |
| `taper_fraction` | how much of the band the narrowing takes |
| `full_width` | the band's width before the taper |
| `d` | a ready-to-render SVG path |
| `framework` | the point and outward direction where it was cut |

> **The taper is measured, not assumed.** It is taken between the two edges of
> the band; the median is 17 per cent of the band on Stage II and 18 per cent on
> the LAC page.

### The cut framework

Frameworks are stored already converted to +y upward, so they match the app:

```json
"framework": {
  "anchor": [1610.0, -2563.0],
  "heading": [0.707, 0.707],
  "units": "page, +y up",
  "sense": "outward"
}
```

`anchor` is the point where the end was cut; `heading` points away from the
work, the direction a cap or another stroke would continue.

## Units and direction

Everything else is stored as it was found on the page: **y increases downward**.
The app is **y increases upward**, and the frameworks have been converted.
Convert before quoting any other coordinate.

## Rebuilding the data

`scripts/extract-terminals.py` and `scripts/extract-spirals.py` read the pages,
write the JSON and build the galleries. The terminal extractor can refresh the
frameworks without fetching the pages again:

```sh
.venv/bin/python scripts/extract-terminals.py --frameworks-only
```
