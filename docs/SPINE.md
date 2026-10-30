# The spine layer guide

The spine layer (`pythagorean-spiral/`) builds the skeleton that ribbons, leaves
and flourishes hang on. It works in whole numbers and fractions taken from right
triangles, so a chain can be reasoned about exactly instead of drifting by
rounding.

## 1. How whole-number triangles create curves

A computer turning a line by 30.5° uses a decimal sine and cosine. Over dozens
of steps those decimals accumulate error, and a loop stops meeting its start.

The spine layer takes its rotations from **Pythagorean right triangles**, such as
3-4-5. The acute angle of that triangle has sine 3/5 and cosine 4/5, exactly, so
turning a point is

```text
(x, y)  ->  ((4x - 3y) / 5, (3x + 4y) / 5)
```

with no trigonometry and no rounding. Chain those rotations and every heading,
and every node, is a fraction.

## 2. What is exact, and what is not

| Feature | How it works | Status |
|---|---|---|
| Turn schedule | a list of whole numbers, one per chord | exact |
| Loop closure | the turn numbers sum to zero | exact, and proved |
| Sharp 90° corners | a coordinate swap, `(x, y) -> (-y, x)` | exact |
| Mirrors and symmetry | `x -> -x` through an axis | exact |
| Node coordinates | fractions over powers of the hypotenuse | exact for small chains |
| Node coordinates at scale | doubles past a few hundred chords | measured, ~1e-13 |
| The drawn curve | cubics fitted across the chords | approximation, see below |

Two rules follow:

- **Closure.** A chain ends on an axis exactly only when its total turn
  coefficient is zero. Niven's theorem is why no other exact landing exists: the
  tangent of a rational multiple of pi is 0 or ±1, and a Pythagorean angle is
  never one of those. When the numbers do cancel, the loop closes with no gap.
- **Right angles.** A 90° corner cannot be reached by accumulating small turns.
  It is made by a **cusp**, the swap above, which is exact even in the float
  path.

The drawn curve is an interpolation, not the chain: measured on the curl study,
the cubics sit within about 1.4% of the ideal curvature law (rms 0.8%), which is
the chain's own resolution.
Do not describe the drawn result as exact geometry.

## 3. The words

| Word | Means |
|---|---|
| Anchor | One node: its exact point and its exact heading. Every node has one, not just the start. |
| Spine | The drawn curve through the anchors: equal chords, each turned by a whole number of triangle angles. |
| Node framework | The anchor plus its tangent and normal: what a branch or a cap attaches to. |
| Knot | A span boundary where two cubics meet. |
| Rails | The two offset edges that give the spine width: a miter offset, rational for small chains. |

## 4. When to use the spine layer, and when not

Use it when the *plan* has to be exact: a loop that must close, a design that
must sit on a grid, a mirror that must be a true mirror, a join that must be
proved rather than fitted.

Use the web app when you want the drawn clothoid curve: smooth, G2-capable, with
widths and a clearance report, exported as SVG.

They are not yet wired together. The spine layer is a library, not a page: the
promotion gate in the plan lists the four conditions that would make the app use
it.

## 5. Walkthrough: an S-curve ribbon

1. **Triangle and step.** `for_angle(3.0)` returns the triangle `39-760-761`,
   whose angle is 2.9376°, and we take 6 mm chords.

2. **Turn schedule.** `+1, +2, +3, +4, +5, -5, -4, -3, -2, -1`. It curls one
   way, reverses, and its numbers sum to zero, so the exit is exactly east with
   no angle drift.

3. **Step through the points.** Starting at (0, 0) facing east, each chord
   applies its whole-number turn and steps 6 mm. The headings are fractions
   whose denominator is a power of 761 — one factor per turn, not a single 761
   — so every joint is an exact rational point.

   ```python
   from fractions import Fraction
   from pythagorean_spiral import place, ribbon
   from pythagorean_spiral.spiral import Spiral
   from pythagorean_spiral.triples import for_angle

   tri = for_angle(3.0)                    # 39-760-761, alpha 2.9376 deg
   path = Spiral(tri, Fraction(6))         # 6 mm chords
   path.extend([1, 2, 3, 4, 5, -5, -4, -3, -2, -1])

   assert path.coeff == 0                  # the plan closes
   assert path.heading.axis_name() == "east"
   ```

   Ten chords, a peak heading of 44.06°, and a final point of
   (56.05, 16.15) in millimetres.

4. **Smooth the corners.** The drawn curve is not the polygon: each span is a
   cubic whose end tangents come from the chord headings, and whose arms are
   solved (the arc rule by default, Menger curvature opt-in). A curvature
   reversal is kept as a **sharp corner** by default, and a single-chord span is
   drawn as its chord, so a cubic is never asked to un-bulge inside one span.
   In the curl study the fit sits within about 1.4% of the ideal curvature law
   (rms 0.8%) — the chain's own resolution. It is an interpolation, not a second exact curve.

5. **Add ribbon thickness.** The width is the *total* width, so 10 mm means
   5 mm each side. The rail is a miter offset of the exact points, with a
   rational taper at the ends:

   ```python
   outline = ribbon.outline(path.nodes, Fraction(10), taper=2)
   ```

   The outline has one point per rail per node — 22 points here. One caveat:
   the offset does **not** detect a pinched or self-crossing rail. Where the
   width exceeds the inside radius the rail folds through itself, and the
   drawing shows it; clearance is measured separately, by `piece_clearance()`
   in the main package, not here.

6. **Place it on the sheet.** The largest uniform scale that fits 200 × 250 with
   an 8 mm margin, snapped to thousandths:

   ```python
   ints, scale = place.fit(outline, box=(200, 250), margin=8)
   ```

   The scale is 0.942 for the 10 mm ribbon, and the drawing occupies
   8.0–192.0 mm across and 8.0–37.1 mm up. Every point is an integer, so the
   file can be stored, mirrored and compared without a float deciding where a
   corner is.

That is the whole method: exact plan, rational rails, and one rational
placement.
