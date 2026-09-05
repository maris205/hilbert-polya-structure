# Deterministic compilation and PDF audit

Executed on 2026-09-05 with LuaLaTeX, epoch 1788566400 and two independent
fresh directories per round, each with two passes. Each pair agrees byte
for byte. The final main.pdf equals Round 2 exactly.

| Round | Pages | Embedded and subset fonts | PDF SHA-256 |
|---|---:|---:|---|
| 0 | 3 | 9 | `251cf57a7286dcdde9e42ceab88eb9c9945f4637d3464370d64cad333416258c` |
| 1 | 5 | 9 | `403bb2ec258685501018fb3cd2a7b86ad5295f220677d8bd51c6279ce5784265` |
| 2 | 6 | 11 | `fd1a887fcc68daacf271eff3d6f36318407a20f17e06a61f0cb748fbc52cbef3` |

All 14 pages across the three rounds rasterize. Every font is embedded and
subset, including the Chinese font. Text extraction contains no nonprinting
control codes, unresolved references, citation placeholders or stale markers.
Each round contains six English and six Chinese keywords. Round-dependent
theorem sections are checked for presence and absence, and page counts
strictly increase with substantive additions.

The settled logs are preserved without content rewriting in
compile_round0.txt, compile_round1.txt and compile_round2.txt. They contain no
layout, missing-glyph, undefined-reference or citation warnings. The initial
build exposed missing ASCII semicolons in the Chinese fallback font and an
underfull reference paragraph. Chinese keywords now use full-width semicolons,
and the bibliography uses local ragged-right paragraph layout. The L1 section
bookmark has a plain-text alternate. No warning was suppressed.

There is no venue-specific page limit and no claim of submission or acceptance.

The independent paper author visually inspected all six final pages and
identified a scope sentence whose negation was on the preceding page. It
was rewritten with the independent sentence "Route B remains disabled" and
the scope paragraph was kept together. Conditional-text punctuation spacing
was also corrected. All three rounds were then rebuilt and audited again;
the hashes in this report refer to those corrected PDFs.
