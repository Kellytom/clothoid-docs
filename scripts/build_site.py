"""Assemble the MkDocs source tree and build the site.

    python3 scripts/build_site.py

Markdown is pulled from docs/, pythagorean-spiral/docs/ and context/; the
generated HTML is copied to site_src/generated/ and linked from one page.
Nothing is edited on the way through.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "site_src"


def fresh() -> None:
    if SRC.exists():
        shutil.rmtree(SRC)
    SRC.mkdir()


def copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> int:
    fresh()
    copy(ROOT / "README.md", SRC / "index.md")
    for name in ("CONTRIBUTING.md", "CHANGELOG.md", "CODE_OF_CONDUCT.md",
                 "LICENSE.md"):
        copy(ROOT / name, SRC / name)
    for name in ("PLAN.md", "VOCABULARY.md", "ORNAMENTS.md", "GRID8.md"):
        copy(ROOT / "context" / name, SRC / name)

    (SRC / "docs").mkdir()
    for p in sorted((ROOT / "docs").glob("*.md")):
        copy(p, SRC / "docs" / p.name)
    # generated pages live under generated/; point the docs' links there
    for p in sorted((SRC / "docs").glob("*.md")):
        text = p.read_text()
        text = re.sub(r"\]\((?!https?:)([A-Za-z0-9_-]+\.html)\)",
                      r"](../generated/\1)", text)
        p.write_text(text)

    (SRC / "spine").mkdir()
    for p in sorted((ROOT / "pythagorean-spiral" / "docs").glob("*.md")):
        copy(p, SRC / "spine" / p.name)

    fig_src = ROOT / "pythagorean-spiral" / "docs" / "fig"
    fig_dst = SRC / "spine" / "fig"
    fig_dst.mkdir()
    # the cloud figures that embed photographs are not published
    skip = {"cloud-tone.svg", "cloud-veil.svg", "cloud-layers.svg"}
    for p in sorted(fig_src.glob("*.svg")):
        if p.name not in skip:
            shutil.copy2(p, fig_dst / p.name)

    for p in sorted((SRC / "spine").glob("*.md")):
        text = p.read_text()

        def keep(match):
            target = SRC / "spine" / match.group(2)
            if target.exists():
                return match.group(0)
            return f"*({match.group(1)}: figure omitted in the public copy)*"

        p.write_text(re.sub(r"!\[([^\]]*)\]\((fig/[^)]+)\)", keep, text))

    gen = SRC / "generated"
    gen.mkdir()
    pages = []
    for p in sorted((ROOT / "docs").glob("*.html")):
        copy(p, gen / p.name)
        pages.append(("docs", p.name))
    for sub in ("terminals", "spirals"):
        d = ROOT / "docs" / sub
        if d.is_dir():
            shutil.copytree(d, gen / sub)
            if (d / "index.html").exists():
                pages.append((sub, "index.html"))
    for p in sorted((ROOT / "pythagorean-spiral" / "docs").glob("*.html")):
        copy(p, gen / ("spine-" + p.name))
        pages.append(("spine", p.name))

    lines = ["# Generated pages", "",
             "These are committed build output, linked rather than rebuilt here.",
             "Their generators are listed in `docs/README.md`.", ""]
    for sub, name in pages:
        href = f"generated/{sub}/{name}" if sub in ("terminals", "spirals") else (
            f"generated/spine-{name}" if sub == "spine" else f"generated/{name}")
        lines.append(f"- [{name}]({href})")
    (SRC / "generated.md").write_text("\n".join(lines) + "\n")

    cmd = [sys.executable, "-m", "mkdocs", "build", "-f", str(ROOT / "mkdocs.yml")]
    print(" ".join(cmd))
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
