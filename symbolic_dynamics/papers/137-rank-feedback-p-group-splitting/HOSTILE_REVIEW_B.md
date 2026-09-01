# Independent hostile review B — P137 Round 1 freeze

**Review date:** 2026-09-01 UTC  
**Reviewer role:** independent hostile reviewer; the reviewer did not author the manuscript  
**Scope:** frozen-contract alignment, independent theorem reconstruction, hostile boundary probes, canonical verifier byte replay, isolated rebuild, primary-source/owner subtraction, internal collision firewall, and PDF/page/font/metadata/anonymity audit  
**Round-A delta:** `main_round1.pdf`, `main.pdf`, and `main_round0_original.pdf` are byte-identical, so Round A passed an unchanged artifact  
**Disposition:** **PASS** at the internal theorem/artifact gate  
**External status:** **HOLD_EXTERNAL**

No manuscript, bibliography, verifier, or PDF artifact was edited during this
review. The only paper-local output of Round B is this file.

## 1. Severity-indexed findings

### Critical

**C-B-01 — frozen contract alignment and literal operator: PASS.** The main
theorem in the manuscript and in `main_round1.pdf` still matches the frozen
P137 contract with no broadening: the literal type rule is `a<=r -> (a)` and
`a>r -> (r,a-r)` with the rank recomputed after each iterate; recurrent states
are exactly fixed states; the fixed OGF is the stated Gaussian-binomial sum;
the sharp clock is
`D(n)=ceil((sqrt(8n+1)-3)/2)` with explicit orbit
`F^t((n))=sort(n-T_t,t,t-1,...,1)`; and the every-target fibre is the
rank-summed coefficient formula with the stated image criterion. Reconstructing
the group/type passage from the cyclic factors again gives
`p^r C_(p^a) = C_(p^(a-r))` for `a>r` and `0` otherwise, together with
`C_(p^a)[p^r] = C_(p^min(a,r))`, so the keep/split rule and order preservation
remain correct.

**C-B-02 — marker budget, sharp clock, and uniqueness: PASS.** Rebuilding the
proof from scratch gives the same tagged-residual picture as the manuscript.
When a tagged residual larger than the current rank `r_t` splits, the new part
`r_t` is a permanent marker because later ranks are strictly larger. At terminal
time there are therefore `c_t` disjoint markers of weight `r_t` from each
transition together with one positive residual for each initial tag, which
forces

```text
n >= r_0 + sum_(t<d) c_t r_t >= r_0(d+1) + binom(d,2).
```

The cyclic orbit again gives the sharp witness, and the `r_0>=2` exclusion
forces uniqueness of `(n)`. As an additional hostile control, an independently
written brute-force script that did **not** import `code/verify.py` checked the
pointwise budget, the global maximum, the unique deepest source, and the
explicit cyclic orbit for every partition of weights `1..22`; no counterexample
appeared.

**C-B-03 — every-target fibre and image boundary: PASS.** The inverse proof
survives hostile reconstruction. For a fixed source rank `r`, the number of
splits is forced to be `c=L-r`, so `ceil(L/2)<=r<=L`. After removing `c`
marker copies of `r`, every residual part `>r` is a forced split remainder and
the remaining `c-h_r` remainders are chosen only by multiplicity among sizes
`<=r`, giving exactly

```text
[u^(c-h_r)] product_(j=1)^r (1+u+...+u^(q_j^(r))).
```

The reverse map is unambiguous: each selected remainder `j` pairs with one
removed marker to reconstruct the unique large source part `r+j`, while every
unselected residual remains an unsplit source part. This produces a bijection
rank by rank and introduces no spurious binomial factor among identical target
copies. An independent brute-force decoder, again not importing the shipped
verifier, matched the claimed fibre counts and image predicate for every target
partition of weights `1..20`, including fixed targets (`c=0`), repeated marker
values, and forced-high-remainder cases.

### Major

**M-B-01 — canonical verifier replay and control transcript: PASS.** A fresh
replay of `PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py` compared byte for
byte with `code/verification_output.txt` (`cmp=0`). The replay again terminated
with

```text
TOTAL_ASSERTIONS=18504770
STATUS=PASS
```

so the frozen control transcript still matches the current verifier exactly.

**M-B-02 — isolated build and frozen-byte identity: PASS.** A fresh isolated
build from only `main.tex` and `references.bib` in a temporary directory
completed with the standard four stages and reproduced the current paper PDF
byte for byte. The rebuilt PDF, `main.pdf`, `main_round1.pdf`, and
`main_round0_original.pdf` all share the same SHA-256 hash
`7f21edb43343eb6889816c875c6a840fe0c2992de5364e299af536294b3bd5f0`.
Thus Round B is reviewing the same frozen artifact that Round A cleared.

**M-B-03 — primary-source subtraction and collision firewall: PASS.** The five
bibliography entries still describe owned background rather than residual
claims, and their metadata remain consistent with the cited official records:
Fuchs/Springer for finite abelian-group structure, Andrews/Cambridge for
Ferrers and Gaussian-polynomial partition theory, Delaunay--Jouhet/Elsevier for
`p^ell`-torsion statistics on partition-indexed finite abelian groups,
Eliahou--Erickson/Elsevier for a distinct multiplicity-description partition
dynamics, and Baalbaki--Bonanno--Del Vigna--Garrity--Isola/Springer for a
distinct continued-fraction-type partition map. None of those sources owns the
state-dependent operator `G -> p^d(G)G direct_sum G[p^d(G)]`, the permanent
marker budget, the unique sharp triangular clock, or the present every-target
one-step fibre theorem. The internal firewall documents also still separate
P137 cleanly from P126, P135, and P115 by carrier, update rule, temporal
silhouette, and proof engine. This remains an internal subtraction/collision
pass only; it is not an external novelty or priority certificate.

### Minor

**N-B-01 — page, font, metadata, and anonymity audit: PASS.** `pdfinfo` on
`main_round1.pdf` reports five A4 pages, PDF 1.5, no encryption, no forms, no
JavaScript, no custom metadata, and no metadata stream. `Author`, `Title`,
`Subject`, and `Keywords` metadata are blank; `Creator` and `Producer` are only
the generic `LaTeX with hyperref` and `pdfTeX-1.40.22`. `pdffonts` lists 33
rows, all embedded, subsetted, and Unicode-mapped. A binary-string scan found
no local path, username, host name, or machine identifier. Every page was
rasterized and visually inspected; there is no clipping, collision, malformed
display, or non-anonymous visible author line. The only visible author string
is `Anonymous`, and the bibliography on page 5 is legible and expected.

**N-B-02 — Round-A completeness audit: PASS with one clarification.** Round A
covered all required gates and its overall PASS disposition stands. The only
clarification worth recording is procedural: a truly fresh four-stage TeX build
does show the usual undefined-reference and undefined-citation warnings on the
first and second passes before BibTeX and the final settle, so warning scans
must be interpreted on the settled pass rather than on intermediate logs. After
the third `pdflatex` pass, the build is clean, and this does not change the
artifact verdict.

## 2. Final gate

There are **zero critical REPAIR items, zero major REPAIR items, and zero minor
REPAIR items**. The frozen Round-1 package passes this independent hostile
review B. No external action is cleared by that result: novelty, priority,
authorship, posting, submission, owner contact, and public release all remain
out of scope. The mandatory external status remains **HOLD_EXTERNAL**.
