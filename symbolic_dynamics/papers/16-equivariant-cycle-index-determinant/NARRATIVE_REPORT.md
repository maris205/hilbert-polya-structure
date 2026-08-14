# NARRATIVE REPORT — SD-C18

## One-sentence contribution

SD-C18 retains the nonzero atom-permutation class hidden by the scalar
tensor-subset determinant, then proves that its canonical character-resolved
realizations cannot simultaneously preserve the pure Euler trace-log,
commute with distinct arithmetic weights, and retain nontrivial recurrent
motion.

## Research question

Paper 15 ended with a precise survivor.  At squarefree content \(pqr\), the
positive and negative primitive sets had equal cardinality but unequal
\(S_3\)-actions.  Scalar dimension saw zero; the residual character was

\[
 \mathbf1\oplus\mathbf{sgn}-\mathbf{Std}.
\]

The natural next question was whether this lost representation data could be
kept as a cycle-index or Burnside-valued determinant and then read through a
nontrivial character fiber.  The new candidate takes that question seriously
rather than dismissing the residual as an artifact.

## Central thesis

The formal equivariant lift exists and is informative, but its arithmetic
Fredholm interpretation fails for structural reasons.  Burnside marks and
characters resolve genuine primitive-cycle motion before dimension.  Once
the atom variables are specialized to distinct weights \(p^{-s}\), however,
atom permutation ceases to commute with the fixed transfer.  Restoring the
symmetry by equalizing weights leaves a rank-one map with only a trivial
isotype.  Keeping all subset lines through a diagonal operator restores a
standard equivariant power ledger, but that ledger is \(b(x^r)\), not
\(b(x)^r\), and its superdeterminant contains mixed subset factors.  A
character readout that detects the first residual therefore cannot preserve
the pure Euler trace-log.

## Claim–evidence chain

### Claim 1: the formal lift retains information

Squarefree primitive cyclic words are cyclic ordered set partitions, so the
atom-permutation action is canonical.  At \(pqr\), the Burnside class is

\[
 [S_3/S_3]+[S_3/C_3]-[S_3/C_2].
\]

Its marks \((0,0,3,1)\) and character \((0,0,3)\) are nonzero.  Dimension
zero is therefore a lossy readout rather than an equivariant cancellation.
The \(C_2\) color line supplies the correct sign under Adams powers, and no
higher Adams term has squarefree multidegree \((1,1,1)\).  The formal ledger
deserves a genuine `GO`.

### Claim 2: arithmetic specialization breaks fixed-fiber symmetry

The rank-one transfer satisfies semilinear covariance

\[
 \rho(g)A_x\rho(g)^{-1}=A_{g\cdot x}.
\]

This is a family symmetry.  Character Fredholm factors require a symmetry of
one operator.  Commutation holds only when \(x_{gp}=x_p\).  For
\(x_p=p^{-s}\), \(\operatorname{Re}s>0\), distinct magnitudes force the
stabilizer to be trivial.  Central character projectors are therefore not
invariant fibers of the arithmetic transfer.

### Claim 3: symmetry restoration erases the desired motion

Equal weights make the rank-one map equivariant.  Its image is nevertheless
the invariant line spanned by the sum of all subset edges.  Every nontrivial
isotype is killed, and every corresponding determinant is one.  The move
that restores the group action simultaneously removes the character signal.

### Claim 4: the standard representation-preserving operator changes the determinant

The diagonal subset operator keeps each subset line and admits a standard
supertrace.  Its powers give \(b(x^r)\), while the scalar full-shift transfer
gives \(b(x)^r\).  The coefficient of \(x_1^{r-1}x_2\) is \(r\) in the
latter and zero in the former.  The mismatch holds for every \(r\ge2\).

Exponentiating the diagonal ghosts yields

\[
 \prod_{S\ne\varnothing}(1-x_S)^{(-1)^{|S|+1}},
\]

which already for two labels contains \((1-x_1x_2)^{-1}\).  This is a valid
superdeterminant of a different operator, not a resolved factorization of the
pure Euler determinant.

### Claim 5: the analytic limit does not rescue the ledger

The diagonal prime-subset operator is mathematically clean:

\[
 D_s\in\mathcal S_q\quad\Longleftrightarrow\quad
 q\operatorname{Re}s>1.
\]

For \(\operatorname{Re}s>1\), standard Fredholm determinants exist.  They
still yield the mixed-subset product.  The analytic threshold belongs to the
wrong determinant.  The rank-one raw edge maps, meanwhile, fail to
intertwine under canonical label-set embeddings and their norms diverge.
Only the formal zero-specialization projective family survives.

## Strongest result

The strongest result is the character-readout incompatibility at \(pqr\).
The squarefree coefficient is isolated from higher powers.  If a linear
readout is nonzero on
\(R_3=\mathbf1+\mathbf{sgn}-\mathbf{Std}\), its primitive trace-log has a
mixed \(x_px_qx_r\) coefficient.  The pure Euler trace-log contains no mixed
monomial.  Hence an exact Euler readout must kill \(R_3\), while a readout
that sees the first resolved motion cannot preserve the Euler ledger.

This finite theorem exposes the whole obstruction without asymptotics,
regularization, or target-zero data.

## Counterarguments and answers

### “A Burnside-valued zeta already solves the problem.”

It solves the formal packaging problem, which is why the paper records
`GO_FORMAL_EQUIVARIANT_LEDGER`.  It does not supply a group action commuting
with the fixed prime-weighted transfer.  The distinction between a
semilinear family and a fixed equivariant map is load-bearing.

### “Use equal weights and specialize later.”

Equal weights create an equivariant rank-one map whose nontrivial isotypes are
zero.  Specializing afterward changes the operator and breaks commutation.
There is no fixed character factor transported through that step.

### “Use the diagonal operator instead.”

The diagonal lift is honest, trace class in a proved half-plane, and easy to
resolve.  Its power traces and determinant are not those of the scalar
full-shift transfer.  Calling its mixed product the pure Euler determinant
would combine incompatible data types.

### “A more sophisticated equivariant extension might work.”

Possibly.  The paper does not rule it out.  A genuine group cocycle acting in
a fiber independently of the arithmetic roof is the next in-family option.
It must be frozen as a new candidate and tested against the same mixed-term
and arbitrary-inventory controls.

## Controls and arithmetic selectivity

The finite Burnside, ghost, stabilizer, and diagonal determinant identities
hold for arbitrary formal labels.  Composite, shuffled, random, and free
commutative inventories reproduce them.  These controls show that the
mechanism belongs to the subset grammar, not uniquely to rational primes.

The tensor source still matters: it supplies intrinsic atoms and entropy
weights, which earns A0.  It does not make the character residual
arithmetically selective.  Accordingly the candidate receives both
`A0_ANALYTIC_ARITHMETIC_ORIGIN` and `PROVES_TOO_MUCH`.

## Route decision

The resolved candidate, not its scalar shadow, is evaluated:

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
```

A1 is weak because the formal primitive ledger and nonzero character motion
are genuine but do not give an orbitwise prime/prime-power selector.  A2
fails because no character-resolved arithmetic Fredholm determinant preserves
the declared Euler ledger.  A3 and A4 fail because there is no completed
functional equation, divisor theorem, Weil compression, unitary carrier, or
self-adjoint lift.  The scalar shadow had A2 in the previous candidate, but
that coordinate cannot be spliced into SD-C18.

## Paper conclusion

The paper advances the Session 4 program by resolving a plausible escape
route rather than merely repeating a scalar obstruction.  Representation
data does survive scalar cancellation, and the formal Burnside lift is worth
keeping.  The same data does not become an arithmetic character Fredholm
fiber in the canonical realization.  The next viable symbolic candidate
must move the finite-group action from base-label relabeling to a genuine
fiber cocycle while preserving the arithmetic roof and passing controls.
