# Independent hostile review A — P137 Round 0

**Review date:** 2026-09-01 UTC  
**Reviewer role:** independent; the reviewer did not author the manuscript  
**Scope:** theorem reconstruction, counterexample search, verifier replay,
isolated build, source/owner subtraction, internal-collision firewall, and PDF
artifact audit  
**Disposition:** **PASS** at the internal theorem/artifact gate  
**External status:** **HOLD_EXTERNAL**

No manuscript, bibliography, verifier, canonical transcript, or PDF was changed
during this review.  The only paper-local output of the review is this file.

## 1. Severity-indexed findings

### Critical

**C-A-01 — group/type rule and recurrence: PASS.**  Reconstructing the map
factor by factor gives

```text
p^r C_(p^a)       = C_(p^(a-r)) for a>r, and 0 otherwise,
C_(p^a)[p^r]      = C_(p^min(a,r)).
```

Thus a part `a<=r` is retained and a part `a>r` becomes `(r,a-r)`.
The update has length `r+c`, where `c` is the number of parts exceeding
`r`.  Every nonfixed step therefore strictly raises length, while the
weight stays fixed.  This proves termination and excludes every nontrivial
cycle.  The recurrent set is exactly the fixed set `lambda_1<=ell(lambda)`.
No counterexample was found, including `a=r`, `a=2r`, and the zero-group
convention.

**C-A-02 — pointwise marker budget, sharp clock, and uniqueness: PASS.**
Tagging the initial parts leaves one positive residual for every initial tag.
Every split at time `t` creates a part of weight `r_t`; because
`r_(t+1)>r_t`, that marker can never split again.  Hence

```text
n >= r_0 + sum_(t<d) c_t r_t
  >= r_0(d+1) + binom(d,2).
```

Taking `r_0>=1` gives `T_d<n`, and the largest possible `d` is

```text
D(n)=ceil((sqrt(8n+1)-3)/2).
```

For the cyclic source, induction gives

```text
F^t((n)) = sort(n-T_t,t,t-1,...,1).
```

The state is nonfixed for `t<D(n)` and fixed at `t=D(n)`.  If a maximizer
had `r_0>=2`, the pointwise bound would force
`n>=T_(D(n)+1)+1`, contradicting `n<=T_(D(n)+1)`.  Therefore `(n)` is the
unique deepest source.  The triangular-boundary cases and `n=1`, where
`D(1)=0`, are consistent.

**C-A-03 — every-target fibre and image criterion: PASS.**  For a target of
length `L` and a candidate source rank `r`, the number of splits is forced to
be `c=L-r`; hence `ceil(L/2)<=r<=L`.  Removing `c` indistinguishable marker
copies of `r` leaves exactly `r` residual parts.  Every residual `j>r` is a
forced split remainder.  Choosing the remaining `c-h` remainders by
multiplicity among `j<=r` gives exactly

```text
[u^(c-h)] product_(j=1)^r (1+u+...+u^q_j).
```

The reverse construction sends a selected remainder `j` to the unique large
source part `r+j` and retains every unselected residual.  It is inverse to
marker removal and introduces no binomial factor among identical copies.
Positivity is equivalent to `m_r>=c` and `sum_(j>r)m_j<=c`; sufficiency uses
the fact that the bounded products have contiguous degree support from zero
through the number of available low residual copies.

### Major

**M-A-01 — fixed-type OGF: PASS.**  At fixed length `r`, subtracting one
from each positive part identifies the fixed types with partitions inside an
`r` by `(r-1)` rectangle.  The weight shift is `z^r`, so the summand
`z^r [2r-1 choose r]_z` is correct.  The `1` term is precisely the empty
type, while the main theorem is explicitly scoped to `n>=1`.

**M-A-02 — adversarial boundary probes: PASS.**  An independently written
brute-force decoder (not importing `code/verify.py`) compared the stated
fibre formula with literal source enumeration over all 914 target partitions
of weights `1..16`.  It also checked the following deliberately awkward
targets:

| target | issue exercised | exact preimages |
|---|---|---|
| `()` | `n=0` convention | `()` under the conventional extension |
| `(1)` | `n=1`, `r=L`, `c=0` | `(1)` |
| `(4,1,1)` | outside image; failed marker and high-remainder tests | none |
| `(5,2,1)` | forced remainder `j>r` | `(7,1)` |
| `(2,2,2,1)` | repeated marker value and a remainder equal to `r` | `(4,3)`, `(2,2,2,1)` |
| `(3,2,1)` | simultaneous `r=L,c=0` and smaller-rank preimage | `(5,1)`, `(3,2,1)` |

These probes specifically cover `r=L`, `c=0`, multiple copies of `r`, and
the forced `j>r` sector.  No overcount or missing source was found.

**M-A-03 — internal collision firewall: PASS.**  Direct inspection of the
internal papers confirms that the shared words “partition”, “split”, and
“fibre” do not conceal a theorem collision.

- P126 is an **ordered-composition** monoid morphism with the fixed local
  rule `m -> (floor(m/2),ceil(m/2))`; its residual theorem is an all-iterate
  canonical kernel, suffix decoder, and product formula for iterated fibres.
  P137 is an **unordered p-group-type** map whose subtraction threshold is
  recomputed from the current rank; its core results are a triangular entry
  clock and a rank-summed one-step inverse decoder.
- P135 is a centralizer-derived multiplicity rule
  `j^1 -> 1^j`, `j^2 -> j^2`, `j^m -> jm` for `m>=3`.  It has mergers and
  genuine two-cycles, and its tail bound is deliberately nonsharp.  P137 is
  split-only, has no nontrivial recurrence, and proves a unique sharp
  maximizer.

The manuscript also correctly declines generic ownership of marker proofs,
partition dynamics, and coefficient extraction.  The firewall is adequate
for internal progression; it is not an external novelty certificate.

### Minor

**N-A-01 — five-source metadata and owner subtraction: PASS.**  The
bibliographic fields agree with the publisher/author records checked during
this review:

1. Fuchs, *Abelian Groups*, Springer Monographs in Mathematics, Springer
   Cham (2015), DOI `10.1007/978-3-319-19422-6` —
   [Springer record](https://link.springer.com/book/10.1007/978-3-319-19422-6).
2. Andrews, *The Theory of Partitions*, Encyclopedia of Mathematics and its
   Applications 2, Cambridge University Press (1984), DOI
   `10.1017/CBO9780511608650` —
   [Cambridge record](https://www.cambridge.org/core/books/theory-of-partitions/7BC70DD4C1A06AA6179CEDEAD2F0C2DC).
3. Delaunay--Jouhet, *Advances in Mathematics* 258 (2014), 13--45, DOI
   `10.1016/j.aim.2014.02.033` —
   [publisher record](https://www.sciencedirect.com/science/article/pii/S0001870814000942)
   and [author arXiv record](https://arxiv.org/abs/1208.6397).
4. Eliahou--Erickson, *Discrete Mathematics* 313(4) (2013), 422--433, DOI
   `10.1016/j.disc.2012.11.014` —
   [publisher record](https://www.sciencedirect.com/science/article/pii/S0012365X12005067).
5. Baalbaki--Bonanno--Del Vigna--Garrity--Isola, *The Ramanujan Journal* 63
   (2024), 873--915, DOI `10.1007/s11139-023-00791-5` —
   [Springer record](https://link.springer.com/article/10.1007/s11139-023-00791-5).

The subtraction is substantively correct: Fuchs owns the group-structure
background; Andrews owns the Ferrers/Gaussian machinery; Delaunay--Jouhet
own finite-abelian-p-group torsion statistics and partition-indexed
machinery; Eliahou--Erickson own a distinct multiplicity-description
iteration; and Baalbaki et al. own a distinct continued-fraction/Farey
partition map.  None of those five sources supplies the recomputed-rank
operator, marker budget, sharp clock, or the displayed all-target decoder.
An exact-expression search also returned no direct owner, but this remains a
bounded non-hit and contributes no novelty or priority evidence.

**N-A-02 — verifier, build, PDF, and anonymity: PASS.**

- A fresh canonical replay compared byte for byte with
  `code/verification_output.txt` (`cmp=0`) and ended with
  `TOTAL_ASSERTIONS=18504770` and `STATUS=PASS`.
- A fresh isolated four-stage build from only `main.tex` and
  `references.bib` exited zero.  Its PDF was byte-identical to the paper PDF,
  SHA-256
  `7f21edb43343eb6889816c875c6a840fe0c2992de5364e299af536294b3bd5f0`.
- A settled warning scan found no LaTeX/package warnings, bad boxes,
  undefined references/citations, duplicate labels, or rerun requests.  The
  apparent loose-regex hit was only the package-identification line for
  `rerunfilecheck`, not a warning.
- `pdfinfo` reports five A4 pages, no encryption, forms, JavaScript, custom
  metadata, or metadata stream; title, subject, keywords, and author metadata
  are blank.  The only visible author string is `Anonymous`.
- All 33 font rows are embedded, subsetted, and Unicode-mapped.
- Every page was rasterized at 120 dpi and inspected.  There is no clipping,
  collision, malformed display, orphaned heading, or illegible reference.
  The whitespace after the five references on page 5 is intentional.
- Text and binary-string scans exposed no local path, username, or machine
  identifier.

## 2. Final gate

There are **zero critical REPAIR items, zero major REPAIR items, and zero
minor REPAIR items**.  The Round-0 manuscript passes this independent
theorem/artifact review.  This verdict does not clear novelty, priority,
authorship, posting, submission, owner contact, or public release.  The
mandatory external status remains **HOLD_EXTERNAL**.
