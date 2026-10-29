# Building the documentation

Two kinds of page live here: Markdown that a person writes, and HTML that a
script generates. This file says which is which and what each script needs.

## Requirements

- Python 3.10+ for the spine layer and every example. The spine package is
  standard library only — no pip install.
- Node 20+ only for the ornament board generator, which is not in this
  repository (it needs the private board data); its output is committed.

## Pages that rebuild here

From this directory:

```sh
python3 pythagorean-spiral/scripts/explainer.py    # EXPLAINER.md + explainer.html + figures
python3 pythagorean-spiral/scripts/gallery.py      # GALLERY.md + gallery.html
python3 pythagorean-spiral/scripts/extremes.py     # EXTREMES.md + extremes.html
python3 pythagorean-spiral/scripts/cloud_form.py   # CLOUD-FORM.md + cloud-form.html
```

`transfer.py` and `cloud.py` are not runnable here: the first reads the cap
files from the private `out/caps/`, the second reads photographs from the
private `reference/` and needs Pillow. Their Markdown and HTML are committed.

## Pages that only rebuild in the full repository

`docs/ornament-board.html`, `docs/fleur-studies.html`, `docs/piece-model.html`,
`docs/fleur-study-01.html`, `docs/primal.html`, `docs/principles.html`,
`docs/terminals/` and `docs/spirals/` are built by scripts that need the native
clothoid engine, the recovered data, or the ornament source pages. They are
included as build output; change them by changing those scripts, never the page.

## Examples

```sh
python3 examples/curl.py    > /tmp/curl.svg
python3 examples/ribbon.py  > /tmp/ribbon.svg
python3 examples/frames.py
```

Each example is self-contained and prints either SVG or a few measured lines.
Read them beside `pythagorean-spiral/docs/EXPLAINER.md`.

## Viewing

```sh
python3 -m http.server 8000
```

Then open <http://127.0.0.1:8000/>. The published copy uses GitHub Pages; the
generated pages in `docs/` are plain HTML and can be opened directly.
