"""A chain as a ribbon: exact miter rails with a taper at the ends.

    python3 examples/ribbon.py > ribbon.svg
"""
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pythagorean-spiral"))
from pythagorean_spiral import design, ribbon  # noqa: E402
from pythagorean_spiral.triples import thinnest  # noqa: E402

path = design.lobe(thinnest(3125), 8)
poly = [(float(x), -float(y)) for x, y in
        ribbon.outline(path.nodes, Fraction(1, 8), taper=3)]
pts = " ".join(f"{x:.3f},{y:.3f}" for x, y in poly)
print(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-120 -40 260 220" '
      f'width="600"><rect x="-120" y="-40" width="260" height="220" fill="#fffdf7"/>'
      f'<polygon points="{pts}" fill="#2e2413"/></svg>')
