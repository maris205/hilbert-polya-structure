# SD-C13 Proof Package

## Claim

For tensor-prime atom loops with a fixed finite-dimensional unitary fiber and
a faithful positive normalized trace, exact preservation of every positive
Euler repetition coefficient forces every visible fiber to be the identity.
Ordinary trace exactness forces the fiber to be one-dimensional.  Adding a
finite recurrent triangle or a finite positive family of parallel primitive
returns cannot hide all mixed repetitions.  Graded matched sectors can keep
the target moments only by cancelling the moving sector from the
superdeterminant.

## Status

PROVABLE AS STATED under the frozen finite-fiber, positive-trace, and
edge-separated hypotheses.

The proof is a scoped no-go theorem.  It does not exclude infinite diffuse
fibers, rank-dependent virtual coefficients, or a different symbolic
determinant, and it does not authorize Route B.

## Assumptions

- `F_p` is the tensor-prime full-shift atom with entropy `log p`.
- `U_p` is a unitary in one fixed finite matrix algebra `M_d(C)`.
- `tau_d=d^(-1)Tr` is faithful and positive.
- Exact ledger means coefficientwise equality for every atom and every
  repetition, not equality after a finite truncation or specialization.
- Recurrent cycles are first audited with independent edge/atom variables.
- Parallel primitive contributions have positive multiplicity; phase is
  carried by unitary eigenvalues rather than signed external coefficients.

## Notation

- `T_s=direct-sum_p p^(-s)U_p`.
- `Phi=sum_p tau_d`.
- `D_tau(s,z)=exp[-sum_(r>=1)z^r Phi(T_s^r)/r]`.
- `M=xyz` is the formal monomial of a directed triangle.

## Proof Strategy

Faithfulness converts the first normalized unitary moment into a squared
norm.  Newton identities handle the ordinary trace.  A finite positive
spectral measure cannot have every positive moment equal to zero because its
finite Vandermonde system is invertible.  The same argument applies to the
sum of finitely many positive path measures.  Finally, direct cancellation
of an identical even/odd sector proves that a graded escape is determinant
invisible.

## Dependency Map

1. The trace-ideal and determinant theorem uses the diagonal symbolic transfer.
2. The exact-ledger stop uses normalized-trace rigidity atom by atom.
3. Ordinary determinant rigidity uses the first `d` Newton identities.
4. Triangle and parallel-path survival use finite positive moment visibility.
5. The graded boundary follows from the explicit Berezinian quotient.

## Proof

### Step 1: tracial determinant

For `sigma=Re(s)>0`, `|T_s|=direct-sum_p p^(-sigma)I_d`; hence

```text
T_s in L^q(Phi)  iff  sum_p p^(-q sigma)<infinity  iff  q sigma>1.
```

In particular `T_s` is `Phi`-trace class for `sigma>1`, and

```text
Phi(T_s^r)=sum_p p^(-rs)tau_d(U_p^r).
```

The trace-log converges absolutely for `sigma>1` and
`|z|2^(-sigma)<1`, giving the frozen analytic determinant.

### Step 2: faithful normalized moment rigidity

If `tau_d(U)=1`, then

```text
tau_d((I-U)^*(I-U))=2-tau_d(U)-tau_d(U*)=0.
```

The normalized matrix trace is faithful, so `U=I_d`.  Thus exactness at the
first repetition already kills every visible finite Bloch phase.

For a general positive state `phi`, the same calculation proves only that
the GNS cyclic vector is fixed.  Equivalently, the state-visible spectral
measure is `delta_1`.  A nonfaithful state may hide a nontrivial unitary in a
null sector, but its moment determinant cannot see that sector.

### Step 3: ordinary trace rigidity

Suppose `Tr(U^r)=1` for `r=1,...,d`.  If `e_k` are the elementary symmetric
functions of the eigenvalues, Newton's identities and `e_0=1` give
`e_1=1` and inductively `e_k=0` for every `2<=k<=d`.  If `d>=2`, this says
`det(U)=e_d=0`, contradicting unitarity.  Therefore `d=1`, and the first
moment gives `U=1`.

### Step 4: finite positive mixed-cycle visibility

Let the distinct eigenvalues of a unitary `W` be
`lambda_1,...,lambda_m` with normalized multiplicity weights `w_j>0`.
If `tau(W^k)=0` for `k=1,...,m`, then

```text
sum_j w_j lambda_j^k=0,  k=1,...,m.
```

The coefficient matrix is a Vandermonde matrix multiplied by the invertible
diagonal `diag(lambda_j)`.  It is invertible, forcing every `w_j=0`, a
contradiction.  Hence some `k<=m<=d` is visible.

A directed triangle has three cyclic starting points, so the coefficient of
`M^k` in `Phi(L^(3k))` is `3 tau(W^k)`.  It survives for some `k<=d`.
For finitely many parallel primitive returns, combine their positive spectral
measures; the same Vandermonde proof excludes vanishing of every repeated
coefficient.  Independent formal monomials make the conclusion stronger:
different cycles cannot cancel coefficientwise at all.

### Step 5: graded boundary

For arbitrary unitary `V`, put `U_even=1 direct-sum V` and `U_odd=V`.  Then

```text
Str(U^r)=1,
Ber(I-aU)=det(I-aU_even)/det(I-aU_odd)=1-a.
```

Thus the moving `V` sector cancels from both the all-order supertrace and the
superdeterminant.  It is not a determinant-visible Bloch escape.

Therefore the claim follows. ∎

## Corrections or Missing Assumptions

- A nonfaithful positive state does not force the full matrix unitary to be
  identity; it fixes only the state-visible sector.
- Infinite-dimensional diffuse tracial fibers can have all positive moments
  zero.  They are outside SD-C13 and are not excluded here.
- Signed or virtual path multiplicities invalidate the positivity premise;
  the graded theorem records the resulting invisibility rather than a general
  no-go statement.
- Equality after setting independent path variables equal is weaker than the
  primitive ledger and is not accepted as exactness.

## Open Risks

- The theorem decides the finite positive fiber branch, not all possible
  symbolic cocycles.
- The exact untwisted tensor-prime determinant remains confined to its honest
  Euler half-plane in this paper.
- No functional equation, Gamma completion, divisor theorem, or fixed
  self-adjoint generator is supplied.

## Conservative Route evaluation

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
GO_POSITIVE_MOMENT_RIGIDITY
STOP_BLOCH_ESCAPE
STOP_SCOPED / PROVES_TOO_MUCH
ROUTE_B_LOCKED
```

`A1_FAIL` refers to the nontrivial-Bloch target: the twisted determinant is
analytic, but some prime repetition coefficient or a mixed primitive cycle
is wrong.  The trivial fiber retains the earlier untwisted ledger but adds no
phase mechanism.
