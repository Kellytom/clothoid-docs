"""A branch on a stored node, proved by equality rather than measured.

    python3 examples/frames.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pythagorean-spiral"))
from pythagorean_spiral import design  # noqa: E402
from pythagorean_spiral.triples import thinnest  # noqa: E402

path = design.lobe(thinnest(3125), 6)
anchor, branch = design.fork(path, 5, steps=5)
design.joined(path, branch, 5)
print("anchor", tuple(float(v) for v in anchor[0]))
print("branch leaves at", branch.headings[0].degrees, "deg")
print("same rational point:", branch.nodes[0] == path.nodes[5])
