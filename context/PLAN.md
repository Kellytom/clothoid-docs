# The plan

## Objective

A usable design tool for ornament: exact clothoid geometry, a 200 x 250 mm
sheet with +y up, and class I/II cap families. A local MVP and a public
remote MVP exist; the public URL stays private.

## The brief behind it

A cathedral has no single artwork problem; it has one per piece. The
proposal is a veil rather than a repair: tone every photograph into one
narrow palette of light tans and grays, then put a layered, semi-transparent
cloud in front. The cloud is the constant; the works stay different behind
it. The cloud is also a theological choice: at the Transfiguration, the
baptism, the temple and Fatima it shelters the action rather than explaining
it.

## Order of work

1. **W01 piece model** - `Piece`, `Trace`, multi-trace render.
2. **W02 terminals** - caps and tapers; the 120 degree limit defines a cap.
3. **W03 fleur grammar** - study 01 ported, then `fleur_canonical()`.
4. **W04 twenty parameter sets.**
5. **Primals** - earth, water, air, fire, in that order (fire needs the
   turned terminals).
6. **Archetypes** - fleur, acanthus, palmette.

## The spine layer

`pythagorean-spiral/` is a second curve system: an Euler polygon of equal
chords whose headings match a clothoid at the nodes. Its points, joins and
mirrors are rational, so it is the exact *plan* layer; it is not a clothoid
and does not replace the engine. It is central to the curve work and off
nothing, but it is not yet imported by the package.

Promotion gate - all four must hold:

1. `clothoid_lab` imports a chain and builds a `Piece`/`Trace` from its anchors.
2. One spine renders on the 200 x 250 sheet, +y up, through `svg.document`.
3. `piece_clearance()` measures it, and a declared contact or join passes.
4. One W03 study is drawn entirely from Pythagorean chains.

## Non-goals

No restoration, no repainting, no claim that the works match. Reference
photographs are measurement input, not publication. The engine stays for the
transcendental curve; the chain stays for the plan; a converter sits between.
