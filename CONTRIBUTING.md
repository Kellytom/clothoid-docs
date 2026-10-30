# Contributing

## What to write

Markdown in `docs/`, or in `pythagorean-spiral/docs/` for the spine layer.
One subject per file. Add a row to `docs/README.md` when the file is new.
Do not edit a generated page: change its script (the table in `docs/README.md`
names them).

## Voice

- Plain and measured. Say what is exact and what is approximated.
- Every number should be reproducible: from a test, a script, or a measurement
  you name. Do not round-trip a claim through prose.
- British spelling. No marketing voice, no emoji, no exclamation marks.
- Prefer one worked example to three adjectives.
- Name the thing the way `context/VOCABULARY.md` does.

## Structure

1. What this is, in the first two sentences.
2. The mechanism, with the failure modes stated.
3. Numbers, in a table or a code block.
4. What is not done, and why.

## Plain English first

Every section opens with a sentence a non-specialist can read: what the thing is
for, or what goes wrong without it. Then the technical detail.

- Define a term the first time it appears, in a short clause or a parenthesis.
- Keep internal names out of prose, or gloss them at once: "gate" (the four
  conditions), "parity" (the local and deployed copies agree), "miter" (the
  corner where two offset edges meet), "digest" (a fingerprint of the old
  output).
- Prefer the physical description: "the line bends more tightly" before
  "curvature increases".
- Keep the tables; they serve the reader who already knows the terms.

## Checking

```sh
make examples                      # the three snippets still run
python3 -m http.server 8000        # view the pages
```

If you changed the spine package, run its tests from the full repository. If
you changed a generated page, rebuild it from its script and commit both.

## Review checklist

- [ ] The claim is true of the code in this repository.
- [ ] Exact and approximate are distinguished.
- [ ] Numbers are sourced, and units are stated (+y up; page units y-down where
      the recovered data is quoted).
- [ ] Generated pages were not edited by hand.
- [ ] Links resolve, and no private deployment detail is quoted.
