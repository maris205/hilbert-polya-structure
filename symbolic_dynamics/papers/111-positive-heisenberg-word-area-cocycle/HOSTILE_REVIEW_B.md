# Independent hostile review B — P111

Review date: 2026-08-29 UTC.  Scope: the full manuscript, bibliography,
proof/evidence ledgers, verifier and stored output, LaTeX build, and rendered
PDF.  This is an independent hostile pass, not final QA.  Public release
remains **HOLD**.

## Verdict and severity

**GO_INTERNAL / HOLD_EXTERNAL.**  The stated theorem package is **PROVABLE
AS STATED**.

- **CRITICAL: 0.**
- **MAJOR: 0.**
- **MINOR: 1, repaired.**  The internal collision paragraph covered P70,
  P99, and P104 but omitted P93, although the batch firewall lists its random
  cocycle vocabulary as adjacent.  I added the update-rule distinction to
  `main.tex`, `README.md`, and `CLAIMS_EVIDENCE.md`: P93 is a symbolic
  prefix/shift stack map reduced to a reflected one-dimensional walk, whereas
  P111 is a positive Heisenberg matrix product with a quadratic chronological
  pair statistic.

## From-zero proof reconstruction

### Product orientation and finite-word law

The multiplication identity

```text
H(a,b,c) H(a',b',c') = H(a+a', b+b', c+c'+a b')
```

was recomputed directly.  Under the declared chronological convention
`M_n=A_n...A_1`, left multiplication by `X` changes `(J,K,C)` to
`(J+1,K,C+K)`, while left multiplication by `Y` changes it to
`(J,K+1,C)`.  Therefore the central coordinate counts `Y` letters earlier
than a later `X`; there is no hidden reversal of word order.

At fixed `J_n=j`, appending `Y` contributes no area and appending `X`
contributes `n-j`, giving

```text
G(n,j;z)=G(n-1,j;z)+z^(n-j)G(n-1,j-1;z).
```

This is the correct Gaussian-binomial recurrence for the chosen orientation.
Multiplying each slice by `p^j q^(n-j)` gives the biased PGF, including
`p=0,1` under the stated `0^0=1` convention.

### Moments, strong law, and CLT

Logarithmic differentiation at `z=e^t` gives the conditional cumulants
`j(n-j)/2` and `j(n-j)(n+1)/12`.  Independently, writing
`Z_ij=(1-B_i)B_j`, the three covariances for `i<j<k` are exactly

```text
p^3 q,   p q^3,   -p^2 q^2.
```

All disjoint pairs are independent, so their sum yields

```text
Var(C_n)=binom(n,2)pq(1-pq)+2 binom(n,3)pq(1-3pq),
```

which algebraically equals the boxed finite-time variance.

For `eta_k=B_k-p`, direct expansion gives the displayed linear part with
weight `k-1-p(n-1)` and the degenerate quadratic remainder.  The ordinary
strong law plus summation by parts makes the linear term `o(n^2)` almost
surely; the identity for the remainder gives the same order.  For the CLT,
the largest triangular-array summand is `O(n)` while the row standard
deviation is `Theta(n^(3/2))`, so Lindeberg is eventually automatic.  The
remainder has `E|R_n|<=npq`, hence vanishes after `n^(3/2)` scaling.  The
limiting variance is

```text
pq(1-3pq)/3 = pq(3p^2-3p+1)/3 > 0
```

for every interior bias.  The endpoint variables are deterministically
zero and are correctly separated.

### Norm boundary and pressure

The Frobenius identity is literally
`3+J_n^2+K_n^2+C_n^2`.  The area strong law therefore forces quadratic
norm growth in the interior; pure `X` or pure `Y` products have norm of
linear order.  Equivalence of fixed finite-dimensional norms preserves the
two logarithmic exponents.

For a word with `j` letters `X`, the maximum area is `j(n-j)` and requires
the unique ordered word `Y^(n-j)X^j`.  Balancing gives
`floor(n^2/4)` and total maximizer probability `(pq)^floor(n/2)`, including
the two odd-length maximizers.  Area zero has the `n+1` monotone words
`X^jY^(n-j)`.  These events cost only `exp(-O(n))`, so the maximum-event
and zero-event lower bounds survive the `n^2` logarithmic scale.  They prove
`theta/4` for positive tilt and zero for nonpositive tilt.  The almost-sure
area law gives the pathwise value `theta pq/2`; the strict gap has the
correct sign for both positive and negative tilt.

## Ownership and P1–P106 collision gate

The DOI records for Canfield--Janson--Zeilberger (including the corrigendum),
Işlak--Özdemir, and Diaconis--Hough were checked against publisher or author
records.  The first owns fixed-content Mahonian/Gaussian-polynomial
asymptotics, the second supplies nearby iid random-word subsequence moment
and CLT methods, and the third gives broad Heisenberg/unitriangular
random-walk limit theory.  Targeted searches did not identify a source for
the exact positive two-generator biased conjunction or its `n^2` pressure
kink.  Search absence is not evidence of priority, and direct-owner risk
remains material.

The internal neighbours are separated at the update-rule level:

- P70 uses weighted shifts and convolution nullities on finite Heisenberg
  quotients;
- P93 uses random prefix/shift maps on symbolic stacks;
- P99 uses one deterministic shear on finite-index integer sublattices;
- P104 uses contracting monomial matrices and `n`-scale singular-value
  pressure.

None shares P111's phase, positive generator law, central word-area
observable, or quadratic pressure scale.

## Exact-control replay

I freshly ran `python3 code/verify.py` and compared stdout byte for byte with
`code/verify.out`.  The diff was empty.  The run passed **421,285 exact
assertions**, including all 131,071 binary words through length 16,
Gaussian slices, biased exact moments, shared-index covariance, centered
decomposition, endpoints, extrema, and pressure bounds.  Python syntax
checking also passed.  The verifier is finite falsification evidence and is
not used to infer any limit theorem.

## Build and visual replay

After the collision repair I ran
`pdflatex -> bibtex -> pdflatex -> pdflatex`.  The rebuilt artifact has:

- 7 A4 pages, 314,127 bytes, PDF 1.5;
- zero undefined citations/references, warnings, overfull boxes, underfull
  boxes, BibTeX warnings, or unresolved sentinels;
- all 21 font entries embedded, subsetted, and Unicode-mapped;
- 24,556 bytes under `pdftotext -layout`;
- all seven pages visually inspected with no clipping, overlap, malformed
  display, or illegible bibliography.  References begin on page 7.

## Residual risks

1. The strongest residual risk is direct ownership and contribution density:
   the normal form and Gaussian slice are elementary/owned, while broad
   Heisenberg CLTs already exist.  Only the exact biased synthesis, endpoint
   exponent boundary, and quadratic-pressure calculation remain in scope.
2. The pressure is for the central area observable at `n^2` scale, not a
   conventional generalized Lyapunov exponent.  The manuscript states this,
   but external presentation must preserve the distinction.
3. No novelty, priority, specialist-contact, or release conclusion is
   authorized.

Final decision: **GO_INTERNAL / HOLD_EXTERNAL**.
