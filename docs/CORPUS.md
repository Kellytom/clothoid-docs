# The recovered corpus

The project began as two ornament pages drawn with cubic Bézier curves: the
Stage II plates and the LAC (log-aesthetic) page. We cut their ends and their
centre lines out and stored them as data. The source repository and its
photographs are private; no photograph is published here.

## Three things: a span, a spine, a plate

These words are used throughout, and they nest:

- A **span** is one cubic Bézier between two nodes: a single piece of a line.
- A **spine** is a run of spans — the whole centre line of one drawn band.
- A **plate** is one page of the source: it holds one or more spines.

So a span is a piece, a spine is the line made of those pieces, and a plate is
the sheet that holds several lines.

## Which curve family a spine is

Each **spine** is tagged with the family it approximates. The tag is on the
spine, not on the span and not on the plate.

| Tag | In plain words |
|---|---|
| `line` | a straight run |
| `arc` | part of a circle |
| `euler` | an Euler spiral, which is the clothoid this project draws |
| `logaesthetic` | a family whose bend follows a fixed aesthetic ratio |
| `reflected` | a mirrored copy of another spine |
| `hyperbezier` | a different family altogether; it is *not* a clothoid |
| `member` | one member of a group, such as a leaf in a set |

Plates are not sorted by family. On Stage II, **19 of the 20 plates mix
families**; the only single-family plate is Fig. 7, which is `euler` throughout.
The LAC page is the opposite: every plate there is one family by construction —
30 `logaesthetic` plates and one `arc` plate. There is no plate that is only
lines, and none that is only arcs on Stage II.

## What was recovered

| From | Plates | Spines | Spans | Ends |
|---|---|---|---|---|
| Stage II | 20 | 90 | 586 | 88 |
| LAC page | 31 | 31 | 306 | 62 |

On Stage II the spines divide as euler 37, logaesthetic 16, line 12,
hyperbezier 8, member 8, arc 6 and reflected 3.

## How close each family is to a clothoid

Fitting one clothoid to each spine gives a parity number: the typical error as a
fraction of one chord. `line`, `arc`, `euler` and `logaesthetic` are within a few
hundredths of a percent. `hyperbezier` is the exception at 35.8 per cent, which
is expected — it is a different kind of curve, and the measurement is there to
show that rather than to hide it.

## What an end record holds

An **end** is one cut end of a band: the join where it leaves the work, the tip,
and the join where it returns. Each one is stored as a few cubic spans plus:

| Field | In plain words |
|---|---|
| `spans` | the cubic pieces of the end |
| `end` | which end of the band it is, `near` or `far` |
| `plate` | which plate it came from |
| `taper_fraction` | how much of the band the narrowing takes |
| `full_width` | the band's width before narrowing |
| `d` | a ready-made path for drawing it |
| `framework` | the point and outward direction where it was cut |

The taper is measured between the two edges, not guessed: the middle value is
17 per cent of the band on Stage II and 18 per cent on the LAC page.

The framework looks like this, and is already converted to y upward:

```json
"framework": {
  "anchor": [1610.0, -2563.0],
  "heading": [0.707, 0.707],
  "units": "page, +y up",
  "sense": "outward"
}
```

`anchor` is where the end was cut; `heading` points away from the work, the
direction a cap or another stroke would continue.

## Units and direction

Everything is stored as it was found on the page: **y increases downward**. The
app is **y increases upward**, and the frameworks have been converted. Convert
before quoting any coordinate.

## Rebuilding the data

`scripts/extract-terminals.py` and `scripts/extract-spirals.py` read the pages,
write the JSON and build the galleries. The terminal extractor can refresh the
frameworks without fetching the pages again:

```sh
.venv/bin/python scripts/extract-terminals.py --frameworks-only
```
