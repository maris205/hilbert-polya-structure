# Hostile Review A — P115

## Review status and decision

- Role: independent nonauthor reviewer. I did not participate in this draft.
- Review target: the existing author-stage manuscript and its existing support files.
- Review-B firewall: no Review B file was read or used.
- Provisional decision: **GO_INTERNAL_AFTER_REPAIR**.
- External status: **HOLD**. No external release, novelty, or priority claim is
  authorized by this review.

All displayed formulas survived reconstruction, edge-case attack, and fresh
exhaustive control. I found no counterexample to the iterate, image/fibre,
depth, Frobenius-cycle, zeta, lattice, or recovery theorems. The blocking
repairs are instead structural and owner-facing: the map's semilinearity should
be explicit at definition time; “entire functional graph” is stronger than the
actual census supplied; and the bibliography omits the direct general temporal
owner for finite linear systems as well as a close primary Cartier-decimation
source.

## Reconstruction from the definition

Write `sigma(c)=c^p` on `F_q`, `q=p^a`. The map is additive and
`sigma^(-1)`-semilinear:

```text
C(lambda f + g) = sigma^(-1)(lambda) C(f) + C(g).
```

It is therefore `F_p`-linear, but generally not `F_q`-linear when `a>1`.
From this starting point:

1. Induction gives
   `C^t(sum c_j x^j) = sum_(p^t j <= n) sigma^(-t)(c_(p^t j)) x^j`.
   At `t=0` this is the identity. If `p^t>n`, only `j=0` remains.
2. Put `r_t=floor(n/p^t)`. The output coordinates `0,...,r_t` are arbitrary,
   each with one forced source coefficient; the other `n-r_t` input
   coordinates are free. Hence the image has `q^(r_t+1)` points and every
   nonempty fibre has `q^(n-r_t)` points. Targets of degree above `r_t` have
   empty fibre.
3. A positive index `j=p^v u`, `p` not dividing `u`, survives as a positive
   coefficient through time `v` and is discarded at time `v+1`; Frobenius
   twisting cannot create or destroy zero. Therefore a nonconstant polynomial
   has depth `1+max v_p(j)` over its occupied positive indices. At time `t`,
   entry into the constant core is equivalent to vanishing of precisely the
   `floor(n/p^t)` positive coefficients indexed by multiples of `p^t`. This
   yields the stated CDF and shells.
4. The images eventually equal the constant subspace `K`. A periodic point
   lies in every sufficiently deep image, hence in `K`; on `K`, the map is
   `sigma^(-1)`. The fixed field of `sigma^m` inside `F_(p^a)` has
   `p^gcd(a,m)` elements. Möbius inversion on divisors of `a` gives exact
   period points and division by the period gives cycles; their Euler product
   is the stated Artin--Mazur zeta function.
5. For `n_L=floor(alpha p^L)`, `1<=alpha<p`, one has
   `p^L <= n_L < p^(L+1)`, so the maximum depth is `L+1`. For fixed `k` and
   `L>=k-1`, the CDF exponent reduces by
   `floor(floor(x)/M)=floor(x/M)` to `floor(alpha p^(k-1))`. Thus the tail is
   not merely convergent but eventually exact.
6. From `F_m=#Fix(C^m)`, `F_1=p`; the maximum is `p^a=q`, first attained at
   `m=a`; and `|X|=q^(n+1)` recovers `n`. This also works for `a=1` and `n=0`.

There is also a useful structural reconstruction not stated in the paper. For
each positive index write `j=u p^v` with `p` not dividing `u`, and change
coordinates by

```text
d_(u p^v) = sigma^(-v)(c_(u p^v)).
```

Then the positive chain for each `u` becomes an untwisted nilpotent shift
`d_(u p^v) <- d_(u p^(v+1))`, while the constant coordinate remains
`sigma^(-1)`. Over `F_p`, the map is therefore conjugate to the direct product
of inverse Frobenius and explicit nilpotent Jordan chains. This is the natural
way to substantiate an “entire functional graph” claim and to expose the exact
relationship with the classical linear finite-dynamics literature.

## Targeted hostile boundary audit

| Attack | Result | Reason |
|---|---|---|
| Semilinearity | **PASS mathematically; under-specified in exposition** | `C(lambda f)=sigma^(-1)(lambda)C(f)` and `C^t` is `sigma^(-t)`-semilinear. The manuscript eventually says `F_p`-linear/not `F_q`-linear, but should state the law next to the definition. |
| `t=0` | **PASS** | `r_0=n`, the iterate and image are the identity/full phase, fibres are singletons, and the CDF counts the `q` constants: probability `q^(-n)`. |
| `n=0` | **PASS** | The phase equals `K`, every state has depth zero, every iterate is inverse Frobenius, and the recovery formula returns `n=0`. |
| `p^t>n` | **PASS** | `r_t=0`; the image consists of `q` constants and each nonempty fibre has `q^n` points. |
| Depth CDF and shells | **PASS** | Exactly `floor(n/p^t)` selected positive coordinates must vanish; consecutive CDF differences and the top-chain count are correct. |
| Frobenius exact periods | **PASS** | Periods divide `a`; for `d|a`, `p^d=sum_(e|d) A_e`, so the displayed Möbius formula is correct. |
| Zeta | **PASS** | Full-map periodic points are exactly constants; transient states contribute no fixed points, and the finite cycle Euler product follows. |
| Lattice floor identity | **PASS** | The identity is valid for real `x` and positive integer `M`; all exponent and `L>=k-1` conditions are present. |
| Parameter recovery | **PASS** | `F_1=p`, equality `F_m=q` occurs exactly for `a|m`, and the phase exponent is `n+1`; no exception occurs at `a=1` or `n=0`. |
| “Entire functional graph” | **NOT YET ESTABLISHED AS A STRUCTURE THEOREM** | The paper gives a strong census but not an explicit component/tree isomorphism or conjugacy decomposition. Add the chain product above or narrow the claim. |

## Findings by severity

### CRITICAL

None. No displayed theorem was falsified.

### MAJOR (math)

1. **The advertised object exceeds the proved structural output.** Introduction
   lines 84--86 asks for the “entire functional graph,” and the abstract says
   “complete finite dynamics,” but the results enumerate iterates, images,
   uniform fibres, depths, and cycles without stating the connected-component
   or rooted-tree decomposition. These statistics do not, in general, constitute
   a functional-graph isomorphism theorem. Action: either (a) add the explicit
   `F_p` conjugacy to inverse Frobenius times the nilpotent `p`-adic index chains,
   then spell out how components are obtained from core cycles, or (b) replace
   “entire/complete functional graph” by “exact temporal census.”

No repair is required to the numerical formulas themselves.

### MAJOR (owner-scope)

1. **The cited generic owner is not the most direct structural owner.** Since
   `C` is an `F_p`-linear endomorphism of a finite-dimensional `F_p`-space,
   René A. Hernández Toledo, *Linear Finite Dynamical Systems*, Comm. Algebra
   33 (2005), 2977--2989,
   [DOI 10.1081/AGB-200066211](https://doi.org/10.1081/AGB-200066211), applies
   directly and advertises a complete dynamics description via nilpotent and
   bijective components. Older transition-graph ownership includes K. C. Wang,
   [DOI 10.1016/0016-0032(67)90115-9](https://doi.org/10.1016/0016-0032(67)90115-9).
   Reis 2023 counts distinct graph types and does not replace these direct
   structural citations. Action: cite/subtract the direct temporal theory and
   present the present result as an explicit Cartier specialization.
2. **A close direct Cartier-decimation source is missing.** Sangtae Jeong,
   *Cartier Operators on Compact Discrete Valuation Rings and Applications*,
   J. Korean Math. Soc. 55 (2018), 101--129,
   [DOI 10.4134/JKMS.j170046](https://doi.org/10.4134/JKMS.j170046), studies
   coefficient-decimating Cartier maps on `F_q[[T]]`, their shift behavior, and
   related perfect-field variants. It does not appear to give this bounded
   temporal census, but it is a primary operator neighbor that must be compared
   rather than omitted.
3. The owner subtraction must say explicitly that restriction of scalars puts
   the full map inside classical **linear** finite dynamics. Merely noting that
   the map is not `F_q`-linear risks suggesting it falls outside that theory.
   The image/kernel, nilpotent--bijective split, periodic core, and generic
   functional-graph decomposition receive zero credit; only the closed
   specialization and chosen lattice consequences can remain in residual scope.

### MINOR

1. State the semilinearity equation and its `t`-fold version immediately after
   (2.1). This makes all later `F_p`-rank language transparent.
2. Define `Per(C)` when it first appears; only `Core(C)` and `tau` are formally
   defined in the conventions section.
3. The second “independent” route uses the same selected-coordinate formula in
   its factorization. It is an independent rank count, not a fully independent
   derivation of the iterate. Tighten that wording.
4. The `1,917,054` figure is a raw assertion count, not that many independent
   mathematical tests: after checking vector equality, the verifier checks each
   coordinate equality again. Keep the number, but do not use its magnitude as
   a strength metric.

## Zero-credit ledger and residual scope

The following receive **zero novelty/priority credit** in this review:

- the Cartier/section-operator coefficient selector and its semilinearity;
- composition of residue-zero selectors and the displayed iterate formula as a
  direct induction;
- rank--nullity, affine kernel cosets, uniform fibres, and decreasing images;
- the nilpotent-plus-bijective decomposition of a finite linear system;
- fixed subfields of Frobenius and their exact-period Möbius inversion;
- conversion from cycles/fixed points to an Artin--Mazur Euler product;
- the nested-floor identity and the algebraic extraction of parameters from
  `F_1`, the maximum fixed count, and phase cardinality as elementary steps.

The bounded search did not locate a paper stating the exact degree-bounded
Cartier specialization with this CDF, lattice-tail formula, and parameter
signature in one theorem package. That absence is **not** evidence of novelty.

Direct temporal owner found: **YES for the general `F_p`-linear dynamical
engine**; **no exact bounded-Cartier temporal owner located in this bounded
audit**.

## Fresh exact-control audit

Executed from the repository root:

```text
fresh=$(mktemp /tmp/p115_verify.XXXXXX.txt)
python3 papers/115-bounded-cartier-operator-dynamics/code/verify.py > "$fresh"
cmp -s "$fresh" papers/115-bounded-cartier-operator-dynamics/code/verification_output.txt
wc -l -c "$fresh"
tail -n 3 "$fresh"
```

Results:

- verifier exit: `0`;
- `cmp` exit: `0` — fresh stdout is byte-for-byte identical to stored stdout;
- stdout: 14 lines, 1,072 bytes;
- terminal assertion: `PASS: 1,917,054 exact assertions`;
- literal fields: `F_2`, `F_3`, `F_4`, `F_8`, `F_9`, `F_16`, each with an
  additional exhaustive `n=0` lane;
- lattice control: 33 rational `(p,a,alpha)` lanes through `L=9`.

The verifier uses actual polynomial-basis fields, checks Frobenius identities,
and independently compares literal images, fibres, depths, cycles, fixed counts,
and two zeta expansions. Its targeted counterexample guards correctly reject
false `F_q`-linearity, degree-only depth, and fixed-core-only zeta. It is finite
falsification evidence, not a proof or owner certificate.

## Fresh build, warning/font scan, and all-page visual inspection

The build was performed in an isolated temporary directory; no author artifact
was touched:

```text
build=$(mktemp -d /tmp/p115_build.XXXXXX)
cp papers/115-bounded-cartier-operator-dynamics/{main.tex,references.bib} "$build"/
(cd "$build" && \
  pdflatex -interaction=nonstopmode -halt-on-error main.tex && \
  bibtex main && \
  pdflatex -interaction=nonstopmode -halt-on-error main.tex && \
  pdflatex -interaction=nonstopmode -halt-on-error main.tex)
rg 'LaTeX Warning|Package .*Warning|Overfull|Underfull|Font Warning|undefined references|multiply defined' "$build/main.log"
pdffonts "$build/main.pdf"
pdftoppm -png -r 150 "$build/main.pdf" "$build/page"
```

Results:

- all LaTeX/BibTeX stages exited `0`;
- PDF: 5 A4 pages, PDF 1.5, 379,547 bytes;
- final log: 0 warnings, 0 overfull boxes, 0 underfull boxes, 0 undefined
  citations/references;
- BibTeX diagnostics: 0 warnings/errors;
- all reported fonts are embedded and subsetted;
- all five pages were rendered and individually inspected at 150 dpi;
- visual result: no clipping, collision, missing glyph, blank page, malformed
  box, or unreadable reference. Density is high but acceptable for a compact
  five-page note.

## Bounded owner-search record

The primary-source search used exact-title and phrase combinations for
`Cartier operator dynamics`, `Cartier operator functional graph`, `Cartier
operator periodic points`, `zero-residue Cartier operator`, `semilinear
functional graph finite field`, and `linear finite dynamical systems`, plus a
one-hop reference audit from Bridy, Reis, and the direct linear-dynamics
sources. Publisher/DOI pages and author/arXiv texts were preferred. This was a
bounded search and cannot certify absence.

## Repair gate

Internal GO requires:

1. state semilinearity explicitly and define `Per`;
2. either prove the chain/Jordan product decomposition or narrow “entire
   functional graph” to the actual census;
3. cite and subtract Hernández Toledo/Wang and Jeong, and explain restriction
   of scalars to `F_p`;
4. keep all generic linear, Cartier, Frobenius, Möbius, and zeta ingredients at
   zero credit;
5. retain external **HOLD** and do not infer novelty from the bounded search.

With those repairs, the exact specialized formulas are suitable for continued
internal development.
