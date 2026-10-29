# Vocabulary

Two systems, one glossary. Use these words exactly; do not introduce synonyms
in new prose.

## The model (clothoid_lab)

| Word | Means |
|---|---|
| `Piece` | One drawing: named traces, optional mirror, layers, contacts. |
| `Trace` | One full line in a piece: a spine plus its rails and width. |
| `Contact` | A declared legal touch between two inks. |
| `Section` | One station across a full line: spine, tangent, width, rails. |
| `Bundle` | A named set of full lines that must not touch, with a footprint. |
| `Cap` | A terminal that closes the end without turning past 120 degrees. |
| `Terminal` | The umbrella: caps and tapers, including turned ends. |

## The spine layer (pythagorean-spiral)

| Word | Means |
|---|---|
| Spine | The drawn curve through the anchors. Not "skeleton", not "Hermite". |
| Anchor | The exact point and its exact heading. |
| Node frame | That anchor plus its tangent and normal: the datum a branch attaches to. |
| Knot | A span boundary where two cubics meet. |

## Rules

- Say **interpolated spine**, not Hermite, except in one parenthesis.
- A node frame is a *view* of an anchor, not a second store: the normal is the
  heading turned a quarter turn.
- Heading is signed; tangent is not. Say which one a function takes.
- "Frame" alone means axes (coordinate, Frenet); never use it for the set of
  nodes. The collective is "the node frames", or "the frame field" in
  differential-geometry prose.
- 90 degree corners are cusps, exact as a swap. 30 and 45 degrees are not in
  any Pythagorean rotation group and stay approximate.
