# Final Proposal

## Title

**Support Size and Finite-Rank Torus Escape for Generalized Hénon Maps**

## One-sentence contribution

For generalized Hénon maps with a nonzero constant and at least two actual
nonconstant monomials, two transitions already give a coefficient-uniform
finite-rank torus bound; this is sharp and contrasts exactly with the absorbed
support-one threshold of four transitions.

## Exact setup

Let `char K=0`, let

`1<=e_1<...<e_s=d`,

and let every `a,c,b_1,...,b_s` be in `K*`.  Set

`P(X)=c+sum_j b_j X^(e_j)`,

`H(x,y)=(P(x)+ay,x)`,

and let `Gamma<=K*` have finite rank `r`.  Define `T_m` using states from time
zero through time `m`.

For `q>=2`, put

`A(q,R)=(8q)^(4q^4(q+R+1))`,

`S_q=d(A(q,2r)+2^q-q-2)`,

`S_*=max_{2<=q<=s+1} S_q`.

Define the component budget by the two explicit subset sums

`M(e)=2(2^s-1)`

`     + sum_{J subset [s], |J|>=2}(e_maxJ-e_minJ)`

`     + sum_{nonempty J subset [s]} e_maxJ`.

The identity

`M(e)=2^(s+1)-2+sum_k(2^k-2^(s-k))e_k`

and the inequality

`M(e)<=2(2^s-1)+d(2^(s+1)-s-2)`

are checks, not alternative definitions.

## Primary claims

### PC1: support at least two

If `s>=2`, then

`#T_2 <= d A(s+2,3r)+M(e)S_*`.

### PC2: sharpness

For every prescribed support with `s>=2`, take rational coefficients
`a=b_j=1`, `c=-s`, and `Gamma=<2>`.  Then

`(1,2^n) -> (2^n,1)`,

so `T_1` is infinite.  The universal threshold is exactly two transitions.

### PC3: absorbed support-one comparison

For `P(X)=c+bX^d` with `d>=2`,

`#T_4 <= 4d A(3,3r)+81d^2`,

and for every `d>=2` a number-field rank-one example has infinite `T_3`.
Choose `b=1`, `a=-1`, `c^(d-1)=-1`, and
`Gamma=<2,c,-1>`; with `Q_t=(t,t^d)` the scalar chain in recurrence order is

`t^d, t, c, -t, (-t)^d`.

## Proof spine

1. Apply Amoroso--Viada Theorem 6.2 only after embedding the arbitrary
   characteristic-zero field and group into an algebraic closure; original
   solutions inject and rank is preserved or bounded as required.
2. Prove the sparse-image lemma with a rank-`2r` tuple group.  Count
   nondegenerate tuples by `A(q,2r)`, use a degree-`d` power fiber, and union
   over the `2^q-q-2` possible proper zero subsets of size at least two.
3. Normalize the first recurrence using
   `Z=z/c`, `U=-au/c`, and `M_j=-b_jv^(e_j)/c`.  Its nondegenerate tuple group
   has rank at most `3r`.
4. Split every zero subsum into GZ, GU, R0, or R1.  GZ/GU are sparse graphs.
   R0/R1 give finite `v`-root sets with the two subset-sum degree budgets.
5. Close every root fiber using
   `w=(c+a rho)+sum b_jz^(e_j)`.  It has `s+1` terms, or `s>=2` terms after
   constant cancellation.
6. Use a union bound so simultaneous zero subsums are overcounted safely.
7. For support one, reproduce the A/B/C transition table.  Only `BA` and `CB`
   are free after two labels; only compatible `CBA` remains free after three;
   every fourth label gives at most `d^2` states.

No coefficient is assumed to belong to `Gamma`, and no scientific computation
enters the proof.

## Literature position

Amoroso--Viada is the unique proof input; ESS is its historical quantitative
predecessor.  Krieger et al. Theorem 1.7 concerns monic `S`-integral
one-variable image sets, while Theorem 1.8 and Corollary 1.9 concern a local
exceptional coefficient and its one-orbit number-field consequence.
Bell--Ghioca Theorem 1.1 fixes one orbit and a finitely generated subgroup; its
regular-map clause makes only the zero-density residual finite, and the Hénon
restriction to the torus is generally rational.  Ji--Xie--Zhang v2 Theorem 1.8
and Corollary 1.9 give cyclotomic periodic-point non-density, not finiteness.
Mello--Yasufuku's front results require `Hyp_epsilon` for
`epsilon >= (1+c)/2`, while its Vojta route uses sufficiently small epsilon and
additional divisor assumptions; that mismatch is not used or resolved here.
Kim--Krieger--Postolache--Szeto Theorem A is an odd-`d>2`, degree-at-most-`d`
rational construction with `(d-4)^2` points, and Theorem B is the
`d=1 mod 6` integer-cycle construction of length `(8d+10)/3`.  All are boundary
comparisons only.  A bounded
primary-source search through 2026-08-17 found no direct collision, but supports
no global priority claim.

## Essential boundaries

- If `c=0`, `P=X^d+X` and `a=-1` give infinite `T_2` through
  `(t,t^d)->(t,t)->(t^d,t)`.
- If `a=0`, `P=-1+X+X^2` gives
  `(1,t)->(1,1)->(1,1)`.
- If `s=1`, PC3 replaces PC1.
- Zero displayed `b_j` must be deleted before support is counted.

There is no positive-characteristic, affine-conjugacy-invariant, optimal-
constant, effective-enumeration, height, periodic-classification, or priority
claim.

In particular, the proposal does not turn an arithmetic-progression theorem
into finiteness, non-density into cardinality, a conditional epsilon-range
statement into an unconditional theorem, or selected periodic constructions
into bounds for all rational or integral periodic points.

## Absorption and lifecycle

The support-one predecessor is identified by terminal-review SHA-256
`9cfb8b2cb492dc6bea84231a81c8f7b7c698eea5299a357d066339180b14260d`
and PDF SHA-256
`4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414`.
It is fully absorbed and may not be submitted in parallel.

This proposal is **AUTHOR COMPLETE / PENDING INDEPENDENT SOURCE REVIEW**.  It
does not authorize manuscript creation, experiment execution, or submission.
