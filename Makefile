PY ?= python3

.PHONY: examples spike-docs serve

examples:
	@mkdir -p out
	$(PY) examples/curl.py > out/curl.svg
	$(PY) examples/ribbon.py > out/ribbon.svg
	$(PY) examples/frames.py

spike-docs:
	$(PY) pythagorean-spiral/scripts/explainer.py
	$(PY) pythagorean-spiral/scripts/gallery.py
	$(PY) pythagorean-spiral/scripts/extremes.py
	$(PY) pythagorean-spiral/scripts/cloud_form.py

serve:
	$(PY) -m http.server 8000
