# The curve model

The engine draws one line at a time. You give it a starting point, a direction,
and a list of segments; each segment bends by a stated amount, and that bend
changes steadily along its length. It then wraps that line in a complete drawing
so it can have thickness, shaped ends, a mirror image, and a list of places where
it is permitted to touch another line.

## The recipe: a `Design`

At the data level a curve is a JSON object with an anchor and an ordered list of
segments:

```json
{
  "anchor": {"x": 40.0, "y": 80.0, "angle": 0.0},
  "segments": [{"length": 40.0, "kd": 0.002, "kappa0": 0.0}]
}
```

| Field | Meaning |
|---|---|
| `anchor` | Where the line starts on the sheet (`x`, `y`), and which way it points (`angle`). |
| `segments` | The pieces of the line, in drawing order. |
| `length` | How long this segment is along the curve, in millimetres. |
| `kd` | How quickly the bend changes along the segment (`dκ/ds`). Positive turns left, negative turns right, zero is straight. |
| `kappa0` | How tightly the line is bending at the start of this segment. |

> **What curvature means.** It is a number for how tight the bend is: small is
> nearly straight, large is a tight curl. Setting `"kappa0": null` means "carry
> on with the bend the previous piece ended with", so the line does not jolt at
> the join.

Coordinates and units:

- distances in **millimetres**;
- angles in **radians**;
- angle `0.0` points **east**;
- **+y increases upward** from the bottom of the sheet.

## The drawing: a `Piece`

- **`Piece`:** the top-level drawing. It holds named traces, an optional global
  mirror (overridable per trace), layers, and a list of declared contacts.
- **`Trace`:** one full line: its centreline path, its ribbon width, the shapes
  at its two ends, and whether it is mirrored.

`render_piece()` builds every trace once and writes one SVG, so the sheet (the
standard 200 × 250 mm page), the scale and the upward +y orientation are decided
in a single place.

## The ends: terminals

**Terminal** is the general word for how a stroke finishes.

- **Caps** close a line without turning it more than 120°: `butt` (cut square),
  `point` (sharpened), `arc` (a 5 mm dome), `round` (a half-width dome).
- **Tapers** narrow the line over a set distance: `taper` (linear), `cone`
  (pointed), and `bulb` (the legacy Stage II width profile, not an ornamental
  wrapped bulb).
- **Turned terminals** curl back further than 120° — a volute eye, a scroll, a
  coiled end. *Planned; not built.*

## Corners, joins and junctions

- **Fillet:** rounds an angular corner with a short circular arc that touches
  both edges. The line and the arc meet in the same direction (G1), but the bend
  changes abruptly where the arc starts and where it ends.
- **Junction:** a branch meeting a trunk at a declared merge. A junction carries
  the corner, the gap that must survive inside the fork, the rounding or blend,
  the taper, and the contacts where the strokes are allowed to touch.
- **Clothoid blend:** the easing transition that would remove the sudden change
  in bend at a junction. *Planned; not built.*

## Measuring across the line: `Section` and `Bundle`

- **`Section`:** one slice across a line at a point along its length: the
  centreline point, the direction, the width, and the left and right edges.
- **`Bundle`:** a group of named lines that must keep a stated minimum gap and
  not touch. It has a footprint for placing the group as one unit; the footprint
  does not clip anything.

## Gaps and collisions: clearance

Clearance measures the closest distance between two strokes and lists
everywhere they cross.

- **Intended touches.** Two lines may touch or cross only where a `Contact` is
  declared. A contact has a point, a radius, the two line names, and it waives
  the clearance rule *inside* its radius only; outside, the rule applies.
- **Unintended collisions.** A crossing with no contact is reported as an
  interference.
- **Tolerances.** Every measurement carries a small margin, so the report says
  **pass**, **warning** or **violation** instead of pretending to know the last
  hundredth of a millimetre.

## How lines meet

| Grade | Name | In plain words |
|---|---|---|
| **G0** | positional | The ends touch, but the lines point in different directions: a corner or kink. |
| **G1** | tangent | They point in the same direction, so there is no corner, but the tightness of the bend changes suddenly. |
| **G2** | curvature | They point the same way *and* bend by the same amount: an invisible transition. |

**What the engine actually does.** By construction, every join in
`clothoid_lab` is **G1**. True **G2** appears only where a width law or a
deliberate blend provides it; an unblended corner or junction still has a
curvature step, and the reports say so.
