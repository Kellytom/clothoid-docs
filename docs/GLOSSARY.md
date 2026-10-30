# Glossary

The two sides of the project use different words for overlapping ideas. This
page defines each word as the code uses it, then maps the two vocabularies. The
short canonical list is in [Vocabulary](VOCABULARY.md); this page is the longer,
plainer version.

## The curve engine (`clothoid_lab`)

| Word | Means |
|---|---|
| **Piece** | One drawing: named traces, an optional mirror, layers, and declared contacts. It is the container, not a claim that the ornament is finished. |
| **Trace** | One full line inside a piece: a spine, its optional ribbon width, its terminals, and its mirror rule. |
| **Segment** | One piece of a design's centre line: a clothoid arc stated by `kappa0`, `kd` and `length`. |
| **Contact** | A *declared* legal touch or crossing. The clearance report allows a crossing only where a contact covers it. |
| **Section** | A reading, not a shape: one station across a full line, with the spine point, tangent, width and the two rails. |
| **Bundle** | The design box: a named set of full lines that must not touch, with an internal clearance and a footprint. The box is for placement, not clipping. |
| **Terminal** | The umbrella for how a line ends: caps (which close without turning past 120°) and tapers. |

## The spine layer (`pythagorean-spiral`)

| Word | Means |
|---|---|
| **Anchor** | One node's exact point and exact heading. Every node has one, not only the start. |
| **Node framework** | That anchor plus its tangent and normal: the datum a branch, cap or terminal attaches to. A view of the anchor, not a second store. |
| **Spine** | The drawn curve through the anchors: equal chords, each turned by a whole number of triangle angles. Not "skeleton". |
| **Knot** | A span boundary where two cubics meet. It is a location, not a guarantee that the join is smooth. |
| **Rail** | An offset edge giving the spine width. In the spine layer it is a miter offset of exact points; rational for small chains. |
| **Cusp** | A quarter turn made by swapping coordinates, `(x, y) -> (-y, x)`: exact, and the only way to get a true right angle. |

## How the vocabularies line up

| Purpose | Engine | Spine layer | Plain English |
|---|---|---|---|
| Where a line starts and which way it points | design `anchor` | anchor | the same idea; the spine's is always rational |
| The path before width | the trace's spine | spine | the backbone line |
| Where two pieces meet | segment join | knot (span boundary); node framework at a branch | a location, with an attachment datum on the spine side |
| The width's edges | offset rails | miter rails | lines pushed outward to make a ribbon |
| A finished drawing | `Piece` | a placed spine with rails | the spine has no `Piece` equivalent yet |
| A group that must not touch | `Bundle` | no equivalent yet | a design box on the engine side |

Two mismatches are worth stating rather than papering over: the spine layer has
no finished-drawing container, and no bundle. Both are promotion-gate work.

## G0, G1 and G2

| Grade | Meaning | Where it is true here |
|---|---|---|
| **G0** | The ends touch; directions differ. A corner or a spike. | a cusp, or a declared corner |
| **G1** | Directions match; curvature steps. | the engine's joins, by construction |
| **G2** | Directions and curvature match. | where a width law or a blend supplies it; not at every corner |

The spine layer adds a different kind of guarantee: at a shared node the two
sides read the *same stored point and heading*, so the join is exact before any
curve is drawn. The drawn cubics are still an interpolation, within about 1.4%
of the ideal curvature law.

## Words to avoid

- **Skeleton** — say spine.
- **Hermite** — say interpolated spine, except in one parenthesis.
- **Frame** for the attachment datum — say node framework. "Frame" still means
  the render frame (`--frame WxH`) or coordinate axes.
