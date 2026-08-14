# PREREGISTRATION — SD-C18

**Candidate:** SD-C18

**Project:** `16-equivariant-cycle-index-determinant`

**Freeze date:** 2026-08-14

**System family:** Symbolic Dynamics only

**Data policy:** no Riemann-zero data, no fitted phases, no spectral root
search

## Research question

Can the nonzero atom-permutation character hidden by the scalar Koszul-subset
determinant be retained in a natural cycle-index/Burnside determinant that is
both compatible with temporal powers and realizable as a character-resolved
Fredholm determinant after the arithmetic specialization \(x_p=p^{-s}\)?

## Frozen objects

For a finite label set \(P\),

\[
 E(P)=2^P\setminus\{\varnothing\},\quad
 x_S=\prod_{p\in S}x_p,\quad
 \epsilon(S)=(-1)^{|S|+1},
\]

\[
 b_P(x)=\sum_{S\ne\varnothing}\epsilon(S)x_S
       =1-\prod_{p\in P}(1-x_p).
\]

The rank-one edge-state transfer and the diagonal comparison lift are frozen
as

\[
 A_x=u_P\otimes\ell_x,
 \qquad \ell_x(e_S)=\epsilon(S)x_S,
\]

\[
 D_xe_S=x_Se_S.
\]

The two trace ledgers are kept separate:

\[
 \operatorname{tr}A_x^r=b_P(x)^r,
 \qquad
 \operatorname{str}D_x^r=b_P(x_1^r,\ldots,x_n^r).
\]

Signs under temporal power are carried by the nontrivial \(C_2\) character
line \(\tau\), with \(\psi^r(\tau)=\tau^r\).

## Frozen claims

### C1 — formal equivariant lift

Squarefree primitive cyclic words form a multigraded \(S_P\)-set and hence a
Burnside/species/cycle-index ledger.  At \(|P|=3\), the signed residual is

\[
 \mathcal R_3=[S_3/S_3]+[S_3/C_3]-[S_3/C_2],
\]

with marks \((0,0,3,1)\), and linearizes to

\[
 R_3=\mathbf1\oplus\mathbf{sgn}-\mathbf{Std},
 \qquad \chi_{R_3}=(0,0,3).
\]

### C2 — power persistence

No Adams power \(r>1\) contributes at squarefree multidegree \((1,1,1)\).
The \(pqr\) residual cannot be erased by a higher-power preimage.  The
\(C_2\) carrier, rather than the integer coefficient \(-1\), preserves the
correct scalar sign under every temporal power.

### C3 — fixed-fiber symmetry obstruction

The rank-one family satisfies

\[
 \rho(g)A_x\rho(g)^{-1}=A_{g\cdot x}.
\]

After \(x_p=p^{-s}\) with \(\operatorname{Re}s>0\), the fixed operator has
trivial label-permutation stabilizer.  Equal weights restore symmetry, but
the image of \(A_x\) is the trivial line and every nontrivial isotype
determinant equals one.

### C4 — standard analytic lift obstruction

For all \(n\ge2\) and \(r\ge2\),

\[
 [x_1^{r-1}x_2]b_P(x)^r=r,
 \qquad
 [x_1^{r-1}x_2]b_P(x_1^r,\ldots,x_n^r)=0.
\]

Moreover,

\[
 \operatorname{sdet}(I-D_x)
 =\prod_{S\ne\varnothing}(1-x_S)^{\epsilon(S)}
\]

contains mixed factors and is not \(\prod_p(1-x_p)\).

### C5 — character-readout incompatibility

At squarefree degree \(pqr\), a linear character/mark readout sees motion
only if it is nonzero on \(R_3\).  Such a readout introduces a mixed term in
the primitive trace-log ledger.  Exact preservation of the pure Euler
trace-log forces the readout to kill \(R_3\).

### C6 — finite-to-infinite boundary

Zero-specialization defines a formal projective cycle-index family.  The
canonical raw edge-state rank-one maps do not form a bounded intertwining
inductive system.  For the prime-subset diagonal operator,

\[
 D_s\in\mathcal S_q\quad\Longleftrightarrow\quad
 q\operatorname{Re}s>1.
\]

Trace class therefore exists only in a half-plane where the determinant is
already the wrong mixed-subset product.

## Frozen finite certificates

- squarefree primitive cyclic counts for \(n=2,\ldots,7\):
  \(2,6,26,150,1082,9366\);
- positive and negative scalar counts agree for every frozen \(n\);
- \(S_3\) character \((0,0,3)\), irreducible class
  \(\mathbf1+\mathbf{sgn}-\mathbf{Std}\), and marks \((0,0,3,1)\);
- exact ghost witness for \(n=2,\ldots,8\), \(r=2,\ldots,8\);
- full distinct-weight stabilizer is trivial; full equal-weight stabilizer is
  \(S_n\);
- zero-specialization is checked for \(2\to1,\ldots,8\to7\);
- representative \(n=2\) values at \(x_1=1/4,x_2=1/9\): pure determinant
  \(2/3\), diagonal superdeterminant \(24/35\).

These finite checks certify definitions and small character calculations.
The general statements are carried by proofs, not extrapolation.

## Controls

The same formal identities are applied to:

1. tensor atoms with prime entropy weights;
2. composite-only label inventories;
3. shuffled weights;
4. distinct random rational weights;
5. arbitrary free-commutative formal atoms.

Reproduction by all controls triggers `PROVES_TOO_MUCH`.  It is not counted
as arithmetic selectivity.

## Refutation rules

- A nonidentity permutation commuting with the fixed distinct-weight
  \(A_x\) refutes C3.
- A nonzero eigenvalue of the equal-weight rank-one map on a nontrivial
  isotype refutes C3.
- Equality of \(b(x)^r\) and \(b(x^r)\) for a frozen witness monomial refutes
  C4.
- Equality of the diagonal superdeterminant and the pure Euler determinant
  for any \(n\ge2\) refutes C4.
- A higher Adams preimage of multidegree \((1,1,1)\) refutes C2.
- Failure of zero-specialization refutes the formal projective statement.
- A character readout that both detects isolated \(R_3\) and has zero mixed
  trace-log coefficient refutes C5.

## Frozen route and status vocabulary

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
GO_FORMAL_EQUIVARIANT_LEDGER
STOP_CHARACTER_FREDHOLM_FIBERS
STOP_STANDARD_SUPERTRACE_INTERPRETATION
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH
ROUTE_B_LOCKED
```

The scalar rank-one shadow has an exact determinant inherited from the
preceding paper, but the preregistered candidate is the resolved object.
Coordinates from these two data types may not be combined.
