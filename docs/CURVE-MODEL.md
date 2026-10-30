# The curve model

The engine draws one thing: a **Design** — an anchor and a list of
**segments** — then wraps it in a **Piece** so it can gain width, terminals,
mirrors and contacts.

## Design and segment

```json
{"anchor": {"x": 40, "y": 80, "angle": 0},
 "segments": [{"kappa0": 0, "kd": 0.002, "length": 40}]}
```

A segment is a clothoid arc: curvature runs linearly in arc length,
`kappa(s) = kappa0 + kd * s`. `kappa0: null` continues the previous segment's
end curvature, which is what makes a G2 join. Units are millimetres, `angle` is
radians, 0 is east, and y increases upward.

## Piece and trace

A **Piece** is one drawing: named **traces**, an optional mirror with per-trace
override, layers, and declared **contacts**. A **Trace** is one full line: a
spine, an optional ribbon width, its terminals, and its mirror rule.
`render_piece()` builds every trace once and writes one SVG, so the page, the
frame and the y-flip are decided in a single place.

## Terminals

**Terminal** is the umbrella. A **cap** closes an end without turning the stroke
past 120°: `butt`, `point`, `arc` (a 5 mm dome), `round` (a half-width dome).
A **taper** narrows over a length: `taper`, `cone`, and `bulb` (the Stage II
width law, not the wrapped ornament bulb). Hairpins and wrapped bulbs turn past
the limit, so they are *turned terminals*, and they are not built yet.

## Junctions and fillets

A **junction** is a branch meeting a trunk with a declared merge: it carries the
corner, the clearance that must survive through the crotch, the fillet or blend,
the taper, and the contacts. A **fillet** is the tangent arc at a corner: G1 by
construction, with a curvature step at each touch point. A clothoid blend, which
would remove the step, is planned.

## Section and bundle

A **Section** is a reading, not a shape: one station across a full line, with
the spine point, tangent, width and the two rails. A **Bundle** is the design
box: named full lines that must not touch, with an internal clearance and a
footprint.

## Clearance

`piece_clearance()` measures the minimum gap between inks and lists crossings.
A crossing is allowed only where a **Contact** declares it legal. Measurements
carry a 2·tol band, so the report says *violation*, *warning* or *pass* rather
than pretending the last tenth of a millimetre is known.

## The grades

| Grade | Means | Here |
|---|---|---|
| G0 | ends touch, directions differ | a corner, a cusp |
| G1 | directions match, curvature steps | every engine join, by construction |
| G2 | directions and curvature match | only where a width law or blend supplies it |
