# P157 Hostile Review B — independent Round-1 falsification

**Review date:** 2026-09-02 UTC  
**Calibration:** `NOT_CALIBRATED`  
**External state:** `HOLD_EXTERNAL`  
**Independence boundary:** this reviewer did not author P157 and did not
perform Hostile Review A.  The review began with the frozen theorem contract
and the current Round-1 manuscript.  Review A was read only after the first
mathematical derivation, to identify the repairs that then had to be checked.
No author file was edited during this review; this report is the only
paper-local addition.

## Verdict

**REVISE — 0 Critical / 0 Major / 1 Minor.**

The mathematical package survives a fresh derivation.  The pointwise clock,
temporal CDF, sharp height, all three normalized-unit quotient regimes,
full and endpoint fibres, and image size are correct as stated.  Both
Review-A wording repairs are present in `main.tex`, in the current PDF, and
in the Round-1 PDF.  Two author-verifier replays match the frozen transcript,
and a separate inline implementation found no counterexample.

The sole finding is build provenance.  Every settled source-only build emits

```text
pdfTeX warning (font expansion): font should be expanded before its first use
```

and the same line is retained at `main.log:643` and in all three Round-1
pdfLaTeX logs.  This contradicts the zero-warning statements in `BUILD.md`
and `IMPROVEMENT_LOG.md`.  The warning does not alter the mathematical result
or visibly damage the PDF, so it is Minor rather than Major, but the protocol
requires zero unresolved findings for internal acceptance.

## Strongest counter-argument

After the classical idempotent-lifting polynomial and quadratic improvement
are assigned zero contribution credit, the forward half is an elementary
valuation calculation.  A skeptical reader can therefore argue that the
paper's residual value depends entirely on the one-step inverse atlas and
that any hidden failure in its lifting multiplicities would collapse the
paper-sized package.  The vulnerable interfaces are exactly the ones a
compressed argument might blur: the reduced fibres are one, two, and four
rather than uniformly four; the output class changes from `7 mod 8` at
source valuation one to `3 mod 8` thereafter; and the reduced fibre must be
multiplied by exactly `2^v`, not by a quotient-dependent guess, when the
forgotten source bits are restored.

That attack does not succeed.  An exact two-branch lift proves the fourfold
law only for `N>=3`; direct reduction gives the separate `N=1,2` laws; and
the reduction from odd units modulo `2^(n-v)` to odd units modulo `2^N` has
kernel size `2^v`.  Literal enumeration independently reproduces every
target fibre, including zero fibres.  The residual theorem is thus narrow
but mathematically intact.

## Fresh theorem derivation

### Selected-error clock, CDF, and height

For either parity basin, write the selected even error as `e`.  The exact
identities

```text
F(x)=x^2(3-2x),
1-F(x)=(1-x)^2(1+2x),
F(1-x)=1-F(x)
```

show that parity is preserved and that the new selected error is
`e^2(3-2e)`.  Its cofactor is odd.  With the stipulated truncated valuation,
this gives

```text
v_2(e(F^t(x))) = min(n, 2^t v_2(e(x)))
```

by induction, and the limiting endpoint is the original parity `x mod 2`.
Entry by time `t` is equivalent to divisibility of the initial error by
`2^a`, where `a=ceil(n/2^t)`.  Each parity basin contains `2^(n-a)` such
states, so their disjoint union has

```text
A_(n,t) = 2^(n-ceil(n/2^t)+1).
```

Consecutive CDF differences give the displayed shell polynomial.  A
valuation-one error realizes the least `t` with `2^t>=n`, hence the global
height is `ceil(log_2 n)`.  Every state is absorbed at one of the two fixed
endpoints, so no other state is recurrent.

The small moduli are consistent rather than implicit exceptions:

| modulus | CDF/height consequence | image consequence |
|---|---|---|
| `n=1` | both states enter at time zero; height `0` | image `{0,1}`; both endpoint fibres have size `1` |
| `n=2` | two endpoints at time zero and two other states at time one; height `1` | no nonendpoint valuation stratum; both endpoint fibres have size `2` |
| `n=3` | height `2` | first `N=1`, `v=1` stratum appears; image size `4` and every positive fibre has size `2` |

### Normalized-unit image and reduced fibres

For a nonzero even source `x=2^v w`, with `w` odd,

```text
F_n(x)=2^(2v) h_v(w),
h_v(w)=w^2(3-2^(v+1)w).
```

Thus a nonzero even output has valuation `2v<n`.  Put `N=n-2v`.  Direct
reduction gives:

- `N=1`: the unique odd output class, with one reduced predecessor;
- `N=2`: `3 mod 4`, with both odd residues as predecessors;
- `N>=3, v=1`: `7 mod 8`;
- `N>=3, v>=2`: `3 mod 8`.

For the last two cases, split odd inputs as `w=r+4z`, with `r` equal to `1`
or `3`, and define

```text
Phi_(v,r)(z) = (h_v(r+4z)-h_v(r))/8.
```

This is integral.  The derivative valuations at odd `w` are respectively
`1`, `1`, and at least `3`.  Substitution of `delta=4*2^j` into the exact
cubic Taylor identity shows

```text
Phi(z+2^j)-Phi(z) = 2^j mod 2^(j+1).
```

Hence each `r` branch permutes every truncated quotient.  When `N>=3`, `z`
ranges modulo `2^(N-2)` while the variable output bits range modulo
`2^(N-3)`: each branch contributes two predecessors and the two branches
contribute four.  This establishes both the image condition and the precise
`1/2/4` reduced-fibre split.

### Full fibres, endpoint fibres, and image size

The source unit is defined modulo `2^(n-v)`, whereas its normalized target
depends only on reduction modulo `2^N`.  Since

```text
(n-v)-N = v,
```

each reduced predecessor has exactly `2^v` source lifts, all still odd and
all giving distinct exact-valuation sources modulo `2^n`.  The full
nonendpoint fibre is therefore

```text
2^(v+min(N-1,2)).
```

The zero fibre consists exactly of multiples of `2^ceil(n/2)` and has size
`2^floor(n/2)`; reflection gives the same result over one.  A prescribed odd
class modulo eight has `2^(N-3)` members for `N>=3`, while each of `N=1,2`
has one admissible unit.  Summing disjoint valuation strata, doubling by
reflection, and adding the endpoints yields

```text
|im F_n| = 2 + 2 sum_(1<=v<n/2) 2^max(0,n-2v-3).
```

No odd-prime or general-ring conclusion is used in this derivation.

## Review-A repair verification

| Review-A item | Source-level check | Rendered/Round check | Result |
|---|---|---|---|
| M1, eponym and attribution | `main.tex:26` uses the neutral polynomial title; lines 33–35 and 54–64 call Burban–Drozd a record of a known construction and explicitly deny an origination claim; the subtraction table says “direct record” and “zero-credit prior input.” | Text extraction from Round 0 and Round 1 shows the eponymic title was replaced, the “known” and “not an origination claim” qualifiers were added, and owner-language in the table was neutralized.  Page 1 and page 2 visibly contain those repairs. | **CLOSED** |
| M2, unqualified completeness | `main.tex:35–37` says “complete temporal and one-step inverse atlas”; the theorem label at line 78 uses the same bounded scope; lines 312–317 repeat the one-map/one-step ceiling. | The scoped abstract and theorem label are visible on pages 1–2, and page 4 states the one-step scope and non-hit limitation. | **CLOSED** |

`main.pdf` and `main_round1.pdf` are byte-identical.  Their distinct Round-0
predecessor remains preserved.  The repairs changed prose only: the theorem,
proof, author verifier, frozen transcript, and assertion count remain the
contracted versions.

## Exact-control replay

### Author verifier

Two fresh processes ran

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_p157.py
```

and produced byte-identical output.  Each output is byte-identical to
`verification_output.txt`:

- assertions: `2,563,880`;
- terminal status: `PASS`;
- transcript SHA-256:
  `f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1`;
- verifier SHA-256:
  `9e259f6f6de3bb8a0ad5aae13e1c73f73c49d4cb4f62943e81e5ec1fe52950b9`;
- no `__pycache__` or `.pyc` file was created.

The program exhausts every state and target through `n=17` and the odd-unit
maps for `v=1..6`, `N=1..11`.  Its fibre comparison includes targets of
indegree zero.

### Independent control

A separate inline Python implementation did not import or invoke
`verify_p157.py`.  It enumerated all states and every literal target for
`n=1..16`; recomputed parity, reflection, one-step valuation, full orbit
depth, endpoint, temporal CDF beyond the maximum depth, endpoint fibres,
every target fibre including zero fibres, total image, and fibre mass; and
independently enumerated all normalized-unit maps for `v=1..8`, `N=1..12`.
Two runs produced the same 1,258,799-check transcript, with SHA-256
`429c508c8b36b91bd220cdde167b355f6e450356a05d065c376839c0d087ed75`
and terminal `STATUS=PASS`.

These computations provide finite counterexample pressure only.  They do not
prove the all-parameter theorem or establish novelty, priority, source
completeness, or external-release readiness.

## Source-only build and PDF audit

Two fresh directories were populated with only `main.tex` and
`references.bib`.  Each was built by

```text
pdflatex -> bibtex -> pdflatex -> pdflatex
```

and then given one further settling pass.  The two final PDFs, both
pre-settling copies, `main.pdf`, and `main_round1.pdf` are all byte-identical:

- 4 A4 pages;
- 331,596 bytes;
- SHA-256
  `f054f639f4c9ba9d462c183f417597390223b18ca3f74ba5907c39637ba4743e`.

The immutable Round-0 artifact remains 331,521 bytes at SHA-256
`4188a459ad233e8a6a55d5706648617e833ea0f7771d324a368352182a2f9c0d`.

The settled PDF has blank Title, Author, Subject, and Keywords metadata; no
metadata stream, encryption, JavaScript, or suspect flag; and standard LaTeX
Creator/pdfTeX Producer fields.  All 25 font rows are embedded, subsetted,
and Unicode mapped.  The single bibliography entry is cited and resolved.
There are no settled undefined citations/references, rerun requests,
overfull boxes, underfull boxes, or build errors.

All four pages were rasterized at 144 dpi and inspected individually.  The
neutral title, formulas, cases, table, proof endings, declarations, and
reference are legible; no clipping, overlap, malformed glyph, blank page, or
anonymity leak was found.

## Finding

### Critical

None.

### Major

None.

### Minor

#### M1 — settled font-expansion warning contradicts the Round-1 build record

- **Evidence anchor:** log: `main.log:643`,
  `build_round1_pdflatex_1.log:88`,
  `build_round1_pdflatex_2.log:88`, and
  `build_round1_pdflatex_3.log:88` each contain
  “pdfTeX warning (font expansion): font should be expanded before its first
  use”; both independent cold builds reproduce it on every settled pass.
- **Contradicted record:** `BUILD.md:61–62` and
  `IMPROVEMENT_LOG.md:32–33` assert zero warnings.
- **Confidence:** 5/5 — literal retained-log inspection plus two independent
  source-only reproductions.
- **Impact:** build provenance is inaccurate, but the PDF is deterministic,
  visually clean, and mathematically unchanged.  This is therefore a Minor
  artifact defect.
- **Minimum repair:** separate `microtype` from the combined package line and
  load it with
  `\usepackage[protrusion=true,expansion=false]{microtype}`; rebuild the
  Round-2/current artifact; retain Round 0 and Round 1 as history; replace the
  retained build logs and update the zero-warning statements to the actually
  verified result.  Re-run the source-only settling and PDF checks.  No
  theorem, proof, verifier, transcript, or attribution change is requested.

## Decision boundary

P157 is **not yet `ACCEPT_INTERNAL`** because internal acceptance requires
zero unresolved findings.  Close M1 with a warning-free Round-2 build and
accurate build ledger, then perform the prescribed closure check.  This
review grants no permission for posting, submission, circulation, author or
specialist contact, or any other external action.
