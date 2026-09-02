# P158 Hostile Review B — Round-1 cold audit

**Review date:** 2026-09-02 UTC  
**Calibration:** `NOT_CALIBRATED`; `criteria_binding_unavailable`  
**Decision:** **ACCEPT_INTERNAL / HOLD_EXTERNAL**  
**Findings:** **0 Critical / 0 Major / 0 Minor**

## Independence and review boundary

This is a cold review of the frozen theorem contract and the current Round-1
author package.  Review A was not used as mathematical or computational
evidence.  The multiplication separator and literal successive-intersection
lane named in the review brief were treated only as claims requiring fresh
verification.  No author file was modified during this audit.

The decision is internal only.  It does not establish novelty, priority,
ownership completeness, or permission to circulate.  The manuscript's
`HOLD_EXTERNAL` status remains binding.

Reviewed fingerprints:

- `main.tex`: SHA-256
  `31eb5758fb9ba5d2be985a9e4fbffa7a2cfbd4b3515457f6c6220e42bb78fb8f`;
- `verify_p158.py`: SHA-256
  `a1b20733927f31c417d475ec7566050ef812d17be123a7306b7587a6a453c44a`;
- `references.bib`: SHA-256
  `615f06f2391dedb1711918455e5bade526f3c0c74700ec265a8f91423a6f680b`.

## 1. Theorem contract reconstructed from first principles

### 1.1 Complement history and absorption

Because

\[
E(G_t)=\bigcap_{s=1}^{t}E(C_s),
\]

an edge `uv` survives exactly when the two endpoint bits differ at every
epoch.  For binary bits, coordinatewise inequality is equivalent to
`c_t(u)=overline{c_t(v)}`.  This is a pathwise statement and does not depend
on probabilistic averaging.

There are `R=2^(t-1)` unordered complementary word pairs.  The graph is empty
exactly when no such pair is occupied on both sides.  For one distinguished
pair, the admissible labelled allocation is empty or a nonempty set placed
on either one of its two sides, with EGF

\[
1+2(e^x-1)=2e^x-1.
\]

Taking the product over the `R` distinguished pairs gives

\[
A_R(n)=n![x^n](2e^x-1)^R
      =\sum_{j=0}^{R}(-1)^{R-j}{R\choose j}2^j j^n.
\]

There are `2^(tn)` equally likely labelled histories, hence
`P(T<=t)=A_R(n)/2^(tn)`.  Since the edge sets are decreasing,
`{T<=t}={G_t=empty}` and the first-hit mass is `F_t-F_(t-1)`, with
`F_0=0`.

For each fixed edge, after choosing one endpoint history freely, exactly one
of the `2^t` histories at the second endpoint is complementary.  Therefore
`P(uv in G_t)=2^(-t)`.  A union bound gives
`P(T>t)<=binom(n,2)2^(-t)`.  The bound tends to zero, and the positive-integer
tail identity gives

\[
E[T]=1+\sum_{t\geq1}(1-F_t)
\leq 1+{n\choose2}.
\]

Thus the CDF, first-hit law, tail, almost-sure absorption, and mean formula in
the manuscript all follow with the contract's indexing and no missing
`t=0` term.

### 1.2 Every-target fibre

One complementary word pair contributes either only isolates (one side
occupied) or one connected nontrivial complete bipartite component (both
sides occupied).  Distinct nontrivial components cannot reuse the same word
pair: doing so would create cross edges and merge them.  Thus a target can be
in the image only if its nontrivial components are complete bipartite and
`r<=R`.

For a target with `r` such components and `z` isolates:

1. inject the `r` labelled components into the `R` complementary pairs:
   `(R)_r` choices;
2. orient the unique bipartition of each connected component inside its
   assigned pair: `2^r` choices;
3. allocate the labelled isolates to the remaining `R-r` pairs without using
   both sides of any pair: `A_(R-r)(z)` choices.

These data are uniquely recovered from a realizing history, so there is no
overcount.  The fibre is exactly

\[
(R)_r 2^r A_{R-r}(z).
\]

If `r=R` and `z>0`, the residual factor is `A_0(z)=0`; every word pair has
already been consumed, and either word available to an isolate would join it
to the occupied opposite side.  Conversely, when `r<R`, an isolate allocation
exists, and when `z=0`, `A_(R-r)(0)=1`.  This proves both directions of the
image criterion, including every zero-fibre class rather than only observed
targets.

At the mandatory boundary `n=5,t=2`, `R=2`.  Two disjoint edges plus one
isolate have `r=2,z=1`, hence

\[
(2)_2\,2^2A_0(1)=0.
\]

A separate literal-cut enumeration of all `4^5=1,024` histories found zero
realizations of a fixed labelled representative and image size `121`.

### 1.3 Image EGF

On a labelled block of size `s>=2`, a nontrivial complete bipartite graph is
a nonempty proper subset modulo complementation, giving `2^(s-1)-1` choices.
Its labelled EGF is therefore

\[
B(x)=\frac{(e^x-1)^2}{2}.
\]

An unordered set of `j` such components contributes `B(x)^j/j!`.  Isolates
form an arbitrary labelled set, contributing `e^x`, only for `j<R`; at
`j=R` the isolate set must be empty.  This reconstructs exactly

\[
n![x^n]\left(e^x\sum_{j=0}^{R-1}\frac{B(x)^j}{j!}
              +\frac{B(x)^R}{R!}\right).
\]

As a direct coefficient pressure test, at `n=5,t=2` the `j<2` lane contributes
`91` images and the isolate-free `j=2` lane contributes `30`, totaling `121`,
in agreement with the independent literal enumeration.

## 2. Round-1 repair verification

### Multiplication separator

The source contains `(2)_2\,2^2A_0(1)=0`, not a comma-separated expression.
Page 2 of the rebuilt PDF visibly renders `(2)_2 2^2 A_0(1)=0`; text
extraction and raster inspection show no comma.  The correction is therefore
effective in both source and final artifact.

### Literal successive-intersection lane

The two pathwise computations are now genuinely distinct algorithms:

- `literal_intersection_mask` starts from the complete edge mask, constructs
  each epoch's cut by comparing extracted endpoint bits, and intersects the
  surviving mask epoch by epoch;
- `graph_mask` performs no successive intersection and instead tests whether
  the XOR of the two complete history words is the all-ones mask.

For every history, the verifier compares these masks before adding the graph
to the fibre counter.  The seven frozen boxes contain

`4+8+256+4096+1024+32768+4096 = 42,252`

histories.  The assertion increase from `35,278` to `77,530` is exactly
`42,252`, so there is one new literal/compressed equality assertion per
history.  Shared use of the deterministic edge ordering is bookkeeping, not
a shared implementation of the update rule.

## 3. Author verifier replay

I ran

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_p158.py
```

twice in fresh processes.  Both stdout files were byte-identical to one
another and to `verification_output.txt`.  All three have SHA-256

`3e69dfb7d0653c140f2945a6fe4888afc569756a25acf20c1e7eaf2d9f432f0d`.

Each ends with `ASSERTIONS=77530` and `STATUS=PASS`.  Code inspection confirms
that the audit enumerates all word assignments in the seven frozen boxes,
then every labelled simple target mask in each box; it compares observed and
predicted fibres including zero fibres, checks total mass, image size through
a separate component recurrence, the empty fibre, the first edge moment,
CDF monotonicity, and the temporal union bound.  Enumeration is correctly
described as finite counterexample pressure, not proof.

## 4. Source boundary and citations

The three citations are used only to subtract standard neighborhoods:
complete-bipartite graph coverings, the bicluster target class, and random
`s`-intersection graphs.  Publisher/arXiv records agree with the titles,
authors, venues, years, pages, and DOI/arXiv identifiers in `references.bib`.
In particular, the cited random-intersection model places edges through
shared items, whereas P158 retains edges through exact full-history
complementarity.  The manuscript explicitly awards these areas zero
contribution credit and says the bounded screen does not establish novelty or
ownership completeness.  This is the correct source ceiling.

## 5. Two source-only builds and PDF audit

Two independent temporary directories were each initialized with only
`main.tex` and `references.bib`, then built with
`pdflatex; bibtex; pdflatex; pdflatex`.  The two resulting PDFs are
byte-identical to each other, to current `main.pdf`, and to
`main_round1.pdf`:

- SHA-256:
  `2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5`;
- size: `371,703` bytes;
- pages and media: `4`, A4 (`595.276 x 841.89 pt`).

The settled pass of each isolated build and the retained Round-1 settled log
contain zero selected LaTeX/package/pdfTeX/BibTeX warnings, undefined
references or citations, rerun requests, bad boxes, multiply defined labels,
or errors.  Expected first/intermediate-pass reference messages resolve by
the settled pass; both `.blg` files report `warning$ -- 0`.

`pdfinfo` reports blank title, author, subject, and keywords; no custom
metadata stream, form, JavaScript, embedded file, or encryption; and no
suspect flag.  All 28 `pdffonts` rows are embedded, subsetted, and Unicode
mapped.  Raster inspection of all four pages found no clipping, overlap,
malformed glyph, broken equation, unresolved marker, or illegible reference.
The visible author is only `Anonymous`, and `HOLD_EXTERNAL` is explicit on
page 4.

## 6. Findings and disposition

### Critical

None.

### Major

None.

### Minor

None.

The theorem statement matches the frozen contract; the complement-history,
absorption, every-target, zero-boundary, and image-EGF proofs close; both
specified Round-1 repairs are real; the enlarged verifier is reproducible;
and the four-page PDF is source-reproducible and clean.  The package therefore
passes Hostile Review B for **ACCEPT_INTERNAL**.  It remains **HOLD_EXTERNAL**
because this review does not convert the bounded owner screen into external
clearance.
