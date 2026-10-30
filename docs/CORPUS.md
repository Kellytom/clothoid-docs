# The recovered corpus

The project did not start from a blank page. It started from two old ornament
pages, recovered as data: the Stage II plates and the LAC (log-aesthetic) page.
The source repository is private and large, and none of its photographs are
published.

## What was recovered

| Corpus | Plates | Ends or spines |
|---|---|---|
| Stage II terminals | 20 | 88 ends |
| LAC terminals | 31 | 62 ends |
| Stage II spirals | 20 | 90 spines |
| LAC spirals | 31 | 31 spines |

## Terminals

Each terminal is a cut end: join, tip, join. Its JSON carries `spans` (cubic
segments), `tip`, `end` (`near` or `far`), `plate`, the measured
`taper_fraction`, the `full_width`, a ready-made `d` path, and a `framework`:

```json
"framework": {
  "anchor": [1610.0, -2563.0],
  "heading": [0.707, 0.707],
  "units": "page, +y up",
  "sense": "outward"
}
```

The taper fraction is measured between the rails, not assumed: the medians are
17 per cent on Stage II and 18 on the LAC page.

## Spirals

Each recovered spine keeps the page's own cubics and a `data-span` tag: `line`,
`arc`, `euler`, `logaesthetic`, `reflected`, `hyperbezier`, `member`. Fitting one
clothoid per span gives the parity numbers: median error per chord is 0.00% for
`line`, 0.01% for `euler` and `logaesthetic`, 0.02–0.03% for the rest, and
`hyperbezier` diverges as it must (35.8% median).

## Units and orientation

Everything is stored as found on the page: **y down**. The app is **y up**, and
the terminal frameworks are converted to +y up. Convert before quoting.

## Regenerating

`scripts/extract-terminals.py` and `scripts/extract-spirals.py` fetch the pages,
write the JSON and build the galleries. The terminal extractor can add
frameworks without refetching:

```sh
.venv/bin/python scripts/extract-terminals.py --frameworks-only
```
