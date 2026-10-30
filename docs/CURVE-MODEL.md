# The curve model

The engine draws one line at a time. You give it a starting point, a direction,
and a list of pieces; each piece bends by a stated amount, and that bend changes
steadily along the piece. It then wraps the line in a drawing so it can have
thickness, shaped ends, a mirror image, and a list of places it is allowed to
touch something else.

## The recipe: a design

```json
{"anchor": {"x": 40, "y": 80, "angle": 0},
 "segments": [{"kappa0": 0, "kd": 0.002, "length": 40}]}
```

| Field | In plain words |
|---|---|
| `anchor` | Where the line starts, and which way it points. |
| `segments` | The pieces of the line, in order. |
| `kappa0` | How tightly the line is bending at the start of this piece. |
| `kd` | How quickly that bend changes along the piece. |
| `length` | How long the piece is. |

"Curvature" is only how tight the bend is: a small number is nearly straight, a
large one is a tight curl. `kappa0: null` means "carry on with the bend the
previous piece ended with", so the line does not jolt at the join.

Distances are millimetres, angles are radians, zero points east, and y increases
upward.

## The drawing: a piece

A **Piece** is the whole drawing. It holds named **traces**, an optional mirror
image (which can be overridden per trace), layers, and a list of declared
**contacts**.

A **Trace** is one full line: its centre line, an optional thickness, the shapes
at its two ends, and whether it is mirrored.

`render_piece()` builds every trace once and writes a single SVG, so the sheet,
the scale and the upward direction are decided in one place.

## The ends

**Terminal** is the general word for how a line ends.

- A **cap** closes an end without the line turning more than 120°: `butt` (cut
  square), `point` (sharp), `arc` (a 5 mm dome), `round` (a half-width dome).
- A **taper** narrows the line over a length: `taper`, `cone`, and `bulb` (the
  old Stage II width curve, not a wrapped ornament bulb).

Ends that turn further than 120° are *turned terminals*. They are not built yet.

## Corners and joins

A **fillet** rounds a corner with a short arc that touches both sides. The line
and the arc meet in the same direction, but the bend suddenly becomes tighter
where the arc starts and looser where it ends.

A **junction** is a branch meeting a trunk, with a declared place for them to
merge. It carries the corner, the gap that must survive inside the fork, the
rounding or blend, the taper, and the declared contacts. A clothoid blend, which
would remove the sudden change in bend, is planned.

## Reading a line across its width

A **Section** is a slice across a line at one place: the centre point, the
direction, the width, and the two edges.

A **Bundle** is a box of named full lines that must not touch, with a stated
minimum gap and a footprint. The box is for placing the group, not for clipping
it.

## Gaps between lines

Clearance is the smallest distance between two drawn lines, plus a list of
places where they cross. A crossing is allowed only where a **Contact** says it
is intended. Every measurement carries a small margin of error, so the report
says *pass*, *warning* or *violation* rather than pretending the last tenth of a
millimetre is known.

## Joins, in plain words

| Grade | What it means |
|---|---|
| **G0** | The ends touch, but the lines point in different directions: a corner. |
| **G1** | They point the same way, so there is no corner, but the bend changes suddenly. |
| **G2** | They point the same way *and* bend by the same amount: no visible change at all. |

The engine's joins are G1. G2 appears where a width law or a blend supplies it,
and not at every corner.
