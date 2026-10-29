# The ornaments source

The private `ornaments` repository holds the original pages the project was
recovered from: the Stage II plates, the LAC (log-aesthetic) page, and the old
half-stroke grammar (`ornament_set.js`). It is roughly 159 MB of images and is
not published here.

What *is* published is the recovered corpus, as JSON, in `docs/`:

- `docs/terminals/stage-two.json` - 20 plates, 88 ends.
- `docs/terminals/lac.json` - 31 plates, 62 ends.
- `docs/spirals/stage-two.json` - 20 plates, 90 spines.
- `docs/spirals/lac.json` - 31 plates, 31 spines.

Coordinates are page units as found, which is y-down; the app is y-up. The
taper fraction in each terminal is measured between the rails, not assumed
(17 per cent median on Stage II, 18 on the LAC page).

The twenty fleur studies (P01-P20) are the subpage of the board; only study 01
has been ported, at its old parameter values.
