# The recovered corpus

The project did not begin with a blank page. It began with two old ornament
pages: the Stage II plates and the LAC (log-aesthetic) page. We cut their ends
and centre lines out and stored them as data. The original pages and their
photographs are private, and none of the photographs are published here.

## What was recovered

| From | Plates | What was taken |
|---|---|---|
| Stage II | 20 | 88 ends, 90 spines |
| LAC page | 31 | 62 ends, 31 spines |

A **spine** here means the centre line of a drawn band. An **end** is one cut
end of a band: the join where it leaves the work, the tip, and the join where it
returns.

## What an end record holds

Each end is stored as a few cubic curve pieces (`spans`) plus a note of which end
it is (`near` or `far`), which plate it came from, how much of the band the taper
takes (`taper_fraction`), the full width, a ready-made path (`d`), and a
**framework**:

```json
"framework": {
  "anchor": [1610.0, -2563.0],
  "heading": [0.707, 0.707],
  "units": "page, +y up",
  "sense": "outward"
}
```

In plain words: `anchor` is the exact point where the end was cut, `heading` is
the direction pointing away from the work, and both are given with y increasing
upward so they match the app.

The taper is measured, not guessed: the middle value is 17 per cent of the band
on Stage II and 18 per cent on the LAC page.

## What a spine record holds

Each spine keeps the page's own curve pieces and a label saying what kind of
curve it is: `line`, `arc`, `euler`, `logaesthetic`, `reflected`, `hyperbezier`,
or `member`.

Fitting one clothoid to each piece gives the parity numbers used in the studies.
Typical error is a hundredth of a percent of a chord; `hyperbezier` is the
exception, at 35.8 per cent, because it is a different kind of curve.

## Units and direction

Everything is stored as it was found on the page: **y increases downward**. The
app is **y increases upward**, and the frameworks have already been converted.
Convert before quoting any coordinate.

## Rebuilding the data

`scripts/extract-terminals.py` and `scripts/extract-spirals.py` read the pages,
write the JSON and build the galleries. The terminal extractor can also add or
refresh frameworks without fetching the pages again:

```sh
.venv/bin/python scripts/extract-terminals.py --frameworks-only
```
