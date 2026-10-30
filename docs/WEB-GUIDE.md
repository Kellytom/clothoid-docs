# Web application guide

The web tool in `web/` is a small workbench for drawing curves: open it, edit a
design, see the drawing and a short report, download an SVG. It is a Python
server in front of the C++ clothoid engine (Enrico Bertolazzi and Marco Frego).

## Opening it

Run the server from the repository root:

```sh
.venv/bin/python web/server.py
```

Then open <http://127.0.0.1:8000/>. Locally no password is asked. On the
deployed copy every route except `/health` asks for the shared token; there is
no fixed username — the server accepts the token in **either** the username or
the password field. The token is not in this repository.

## How it works

1. You pick a preset or type a design on the left.
2. The browser posts the design to `/api/render`.
3. The engine builds the clothoid segments, joins them, applies the width and
   offset, and returns an SVG.
4. The drawing appears on the right with a status line and a report.

## The controls

| Control | Id | What it does |
|---|---|---|
| Preset | `#preset` | A ready-made design: bracket, ogee, petal, S-curve. Choosing one resets the width to 10 mm. |
| Cap | `#cap` | A recovered class I/II end. Choosing one also sets the width to 10 mm, except the pointed leaves (`cap-pt-*`), where the width is cleared so the point stays sharp instead of getting a flat rail end. |
| Page width / height | `#pagew`, `#pageh` | The sheet in millimetres; default 200 × 250. Coordinates start at the bottom-left and y increases upward. |
| Ribbon width | `#width` | Thickness in millimetres. Blank draws the centre line only; a number expands it to a ribbon. |
| Design | `#design` | The JSON recipe, described below. |
| Render | `#render` | Redraw now. Typing redraws after a short pause; ⌘ + Return or Ctrl + Enter redraws immediately. |
| SVG | `#downloadSvg` | Download the drawing. |
| JSON | `#downloadJson` | Download the recipe. |
| load file… | `#loadFile` | Load a recipe back into the design box. |
| hide / show | `#toggleReport` | Show or hide the report under the drawing. |

## The design recipe

```json
{
  "anchor": {"x": 40.0, "y": 80.0, "angle": 0.0},
  "segments": [
    {"length": 40.0, "kd": 0.002, "kappa0": 0.0},
    {"length": 40.0, "kd": -0.002, "kappa0": null}
  ]
}
```

- `anchor` is where the curve starts and which way it points. `angle` 0 points
  east; positive turns anticlockwise, in radians.
- `length` is the segment's arc length in millimetres.
- `kd` is how fast the curvature changes, per millimetre squared. Positive
  turns left, negative turns right, zero is a straight line.
- `kappa0` is the curvature at the segment's start. `null` means "continue from
  the previous segment's end curvature", which is what makes a G2 join; a
  number forces a step there.

## The status line

| Badge | Meaning |
|---|---|
| `G2` | Curvature is continuous across every join: the bend does not jump. |
| `G1` | Directions meet, but curvature steps at a join — a visible tightening or loosening. |
| `check joins` | Two segments do not even meet in direction. |
| `check report` | The render or a measurement failed; open the report for the reason. |

The line also counts segments, the cubic spans drawn, and any corners.

## Limits

The server refuses, with a message rather than a freeze:

- fewer than 1 or more than 200 segments;
- a width of zero or more than 100 mm;
- a page side of zero or less.

The render tolerance and split are fixed by the app (0.02 and 2), not exposed as controls.

## Walkthrough: an S-curve

1. Leave the sheet at 200 × 250.
2. Set the anchor to `{"x": 40.0, "y": 80.0, "angle": 0.0}`.
3. First segment: `{"length": 40.0, "kd": 0.002, "kappa0": 0.0}`. It curves
   gently up and left.
4. Second segment: `{"length": 40.0, "kd": -0.002, "kappa0": null}`. It leaves
   with the first segment's end curvature and bends back, so the join is G2 and
   the badge should say so.
5. Type `8.0` into the width, press Render, then SVG.

That is the whole tool: a recipe, a drawing, a report, and two downloads.
