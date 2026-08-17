# Proof package

## Definitions

Let `W={0,1}*`.  With `L`, `R`, `M_w`, and `h(w)` as in `SOURCE_LOCK.md`,
write `w ~_0 w0` for the generating relation of the source direct limit and
`w ~_cyc v` when two nonempty equal-length words differ by cyclic rotation.
Let `lambda(n)=(-1)^Omega(n)` be the Liouville function.

## Lemma 0 — matrix formula matches the frozen recursion

**Statement.** For every word `u`,

\[
 h(u0)=h(u),\qquad h(u1)=h(u)+h(\bar u).
\]

**Proof.** Write `M_u=[[a,b],[c,d]]`.  The first columns of `M_uL` and
`M_uR` are `(a,c)^T` and `(a+b,c+d)^T`, respectively.  Hence
`h(u0)=a+c` and `h(u1)=a+b+c+d`.  With
`J=[[0,1],[1,0]]`, `JLJ=R` and `JRJ=L`, so
`M_bar(u)=JM_uJ`.  Thus `h(bar(u))=b+d`, proving the formula.  QED.

## Theorem 1 — the stable-state quotient is not right-autonomous

**Statement.** There is no map `A_1:W/~_0 -> W/~_0` satisfying
`A_1([w])=[w1]` for every rooted word `w`.

**Proof.** The defining relation gives `[epsilon]=[0]`.  If `A_1` existed,
then `[1]=A_1([epsilon])=A_1([0])=[01]`.  Lemma 0 implies that `h` is
constant on `~_0` classes.  But exact multiplication gives `h(1)=2` and
`h(01)=3`.  Hence `[1]!=[01]`, a contradiction.  QED.

**Quantifier note.** The theorem rules out the canonical right append-one
action on this quotient.  It does not rule out every self-map on the set or
an action on the full matrices.

## Theorem 2 — the rooted clock has no necklace descent with powers

**Statement.** There is no function `N` on binary necklaces such that
`N([w]_cyc)=h(w)` for every nonempty word.  Independently, `h` does not obey
`h(w^r)=h(w)^r` for all words and repetitions.  Consequently
`T=log h` cannot be both a cyclic orbit clock and temporally additive under
word powers.

**Proof.** The words `01` and `10` are cyclic rotations, but

\[
 h(01)=\mathbf1^TLRe_1=3,
 \qquad h(10)=\mathbf1^TRLe_1=2.
\]

Therefore a representative-independent `N` cannot exist.  For the power
law, `h(1)=2` and `h(11)=3`, so `h(11)!=h(1)^2`.  Taking logarithms preserves
the inequality because all values are positive.  QED.

**Quantifier note.** The theorem concerns the exact `h` clock and ordinary
word powers.  It does not rule out the cyclic matrix trace, eigenvalue clocks,
or other changed projections.

## Theorem 3 — the Liouville observable is not a scalar orbit character

**Statement.** The function `ell(w)=lambda(h(w))` neither descends to binary
necklaces nor satisfies `ell(w^r)=ell(w)^r`.  In particular, no one-letter
multiplicative character equals `ell` on every rooted word.

**Proof.** The cyclic rotations `001` and `010` have labels `4` and `3`, so
`ell(001)=lambda(4)=+1` and `ell(010)=lambda(3)=-1`.  Thus necklace descent
fails.  Also `ell(1)=lambda(2)=-1`, whereas
`ell(11)=lambda(3)=-1 != (+1)=ell(1)^2`, so repetition fails.

For the final assertion, a one-letter character has the form
`chi(w)=alpha^(#0(w)) beta^(#1(w))`.  Equality on `0` and `1` forces
`alpha=1` and `beta=-1`; equality on `11` would then require
`1=beta^2=ell(11)=-1`, impossible.  QED.

**Quantifier note.** This rules out the literal scalar observable and all
one-letter multiplicative characters.  It does not quantify over arbitrary
matrix-valued or history-dependent cocycles on an enlarged state space.

## Theorem 4 — exact state-inventory determinant identity

**Statement.** Assume the source multiplicity theorem
`#{x in S_K:h(x)=n}=phi(n)`.  For `Re(s)>2`, the diagonal operator
`Q_s e_x=h(x)^(-s)e_x` is trace class and

\[
 \operatorname{Tr}Q_s=\frac{\zeta(s-1)}{\zeta(s)}.
\]

Its owned determinant is entire in `u` and, for `|u|<1`, satisfies

\[
 -\log\det(I-uQ_s)
 =\sum_{r\ge1}\frac{u^r}{r}
   \frac{\zeta(rs-1)}{\zeta(rs)}.
\]

Therefore the partition function is the first trace-log coefficient, not the
whole determinant; moreover `det(I-Q_s)=0`.

**Proof.** Put `sigma=Re(s)>2`.  The trace norm is
`sum_n phi(n)n^(-sigma)`, which converges and equals the positive real zeta
ratio.  The complex trace follows by absolute convergence.  Standard
trace-class Fredholm theory gives the product and entire dependence on `u`.
For `|u|<1=1/||Q_s||`, expand `-log(I-uQ_s)` in norm and take traces:

\[
 -\log\det(I-uQ_s)
 =\sum_{r\ge1}\frac{u^r}{r}\operatorname{Tr}(Q_s^r).
\]

The multiplicity theorem gives
`Tr(Q_s^r)=sum_n phi(n)n^(-rs)=zeta(rs-1)/zeta(rs)`; here
`Re(rs)>2` for every positive integer `r`.  Finally `phi(1)=1` and the
`n=1` eigenvalue is one, so the determinant product contains `(1-u)` and
vanishes at `u=1`.  QED.

**Novelty note.** This theorem is included to type the actual operator.  The
general partition-trace principle is prior internal work and receives no new
credit.

## Corollary 5 — bounded repair trilemma

**Statement.** Within the declared repairs in `SOURCE_LOCK.md`, one must give
up at least one of: the rooted `h` clock, cyclic primitive objects, temporal
powers, the literal Liouville phase, or same-object dynamical determinant
ownership.

**Proof.** Keeping `h` and quotienting by rotations contradicts Theorem 2.
Keeping `lambda o h` as a scalar phase contradicts Theorem 3.  Keeping the
trailing-zero state quotient with the full binary right action contradicts
Theorem 1.  Using the diagonal operator yields Theorem 4's inventory marker,
not a binary return operator.  The remaining declared repairs replace `h` by
matrix trace/eigenvalue data or enlarge the state and therefore relinquish the
frozen source object/clock.  QED.

## Dependency and circularity audit

- Lemma 0 uses only exact matrix multiplication.
- Theorems 1--3 use Lemma 0 and words of length at most three.
- Theorem 4 uses only the independently sourced multiplicity theorem and
  standard trace-class Fredholm algebra.
- Corollary 5 is a finite case split over explicitly declared repairs.
- No theorem assumes a Riemann zero, the desired Route verdict, Paper-40
  corrections, or the absence of a construction it is meant to prove.

## Sanity checks

- `tr(LR)=tr(RL)=3` is a positive cyclic control; the failure belongs to
  `h`, not matrix multiplication generally.
- The Perron eigenvalue of a fixed positive matrix obeys the power law under
  matrix powers; the failure belongs to the rooted label, not temporal powers
  generally.
- `Q_s` has a valid determinant; the A2 failure is dynamical ownership, not a
  blanket assertion that no determinant can be written.

