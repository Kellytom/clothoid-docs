"""Build a curl and write it as an SVG polyline.

    python3 examples/curl.py > curl.svg
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pythagorean-spiral"))
from pythagorean_spiral import design  # noqa: E402

path = design.curl(200.0, 6.0, 1.0)
x, y = path.final
print(f"chords {len(path.turns)}  triangle {path.triangle}  "
      f"final ({float(x):.3f}, {float(y):.3f})  {path.heading.axis_name()}",
      file=sys.stderr)

pts = " ".join(f"{px:.3f},{-py:.3f}" for px, py in path.floats())
print(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 -220 240 240" '
      f'width="600"><rect x="-20" y="-220" width="240" height="240" fill="#fffdf7"/>'
      f'<polyline points="{pts}" fill="none" stroke="#2e2413" '
      f'stroke-width="1.5"/></svg>')
