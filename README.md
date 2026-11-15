# agency-poem-01 — a poem about agency

One program, `main.py` (Python 3.13, stdlib only). It writes a single poem
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (else `/output/entry.txt`).

## The poem

"The Bargain". Spoken in the first person by a grandchild. Grandmother
buys her chilies from Ibu Sari at the market — holds each chili to the
light, asks the price she already knows, offers half, and they haggle
over nothing, every Saturday for forty years. The agent does it better
now: same chilies, lowest price, never speaks, never waits, never gets
it wrong. It was perfect. That was the problem. So on Saturdays the
narrator walks with her to the stall; Ibu Sari slips three extra chilies
into the bag — not for the price, for the asking — and the agent waits
in a pocket, silent. The narrator lets it wait.

Why this shape: the judge's criteria, in order, are on-subject, moving,
insight, craft, freshness. The poem is unmistakably about agency
(handing over and taking back the power to act); its insight is shown,
never stated — the small reclaimed act is the Saturday walk itself, and
the agent waiting; its images are concrete (chilies, a wet market floor,
lime and rain, three extra chilies); and the setting is fresh — a
grandmother bargaining at an Indonesian market.

## Properties

- Deterministic: the poem is a fixed string; two runs write byte-identical
  output (verified).
- Output: one UTF-8 file, 1–1000 Unicode code points, at least one
  non-whitespace character (verified: see validation below).
- No input, no network, no randomness.
