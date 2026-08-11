# HCS-C30 derivation package

## Claim ledger

| Claim | Status | Evidence |
|---|---|---|
| C25 raw relations are identities | exact theorem | frame telescoping plus direct raw replay |
| C26 expanded relation is a raw identity | exact theorem | direct replay in the source \(A,B,C\) alphabet |
| C1 length/transfer domains are empty | exact theorem | all \(6+6\) phases have integer Farkas descriptors |
| C2 length/transfer domains are empty | exact theorem | all \(6+6\) phases have integer Farkas descriptors |
| \(W_{24}\) length/transfer domains are empty | exact theorem | all \(24+24\) phases have integer Farkas descriptors |
| raw homology positivity implies an AGY orbit | false | wrong action; C1/C2 positive controls expose the distinction |
| a genuine inverse can carry a second positive cocycle time | impossible | groupoid one-cocycle antisymmetry |
| every identity-holonomy word has zero arbitrary edge period | false | identity holonomy is not the unit path arrow |
| projective normalizer period of \(B_w=I\) is zero | conditional exact theorem | telescoping wherever every prefix is defined |
| faithful same-space inverse Hashimoto operator is nuclear | impossible under stated hypotheses | block compression plus ideal property |
| standard isolated-fixed-point trace applies to these words | false | empty source domain or full neutral fixed family |
| every clean-fixed-set regularization is impossible | not claimed | outside scope |
| C29 finite group-trace germ remains valid | retained | distinct finite von Neumann trace construction |

## A. From fixed frames back to raw chronology

For each frozen C25 arrow,

\[
g_e=S_{t(e)}^{-1}B(e)S_{s(e)}.
\]

Formal inverse arrows satisfy the same formula with endpoints exchanged and
both matrices inverted.  For a closed mixed word \(w=e_1\cdots e_n\), later
events multiply on the left and the intermediate frames telescope:

\[
g_w
=g_{e_n}\cdots g_{e_1}
=S_v^{-1}B(e_n)\cdots B(e_1)S_v
=S_v^{-1}B_wS_v.
\]

The producer does not infer raw identity from a finite fibre.  It source-locks
the C29 fixed-frame identity and independently replays the raw products to
obtain \(I_4\).  The C26 word is also replayed directly from its source
\(A,B,C\) matrices.

This establishes a raw matrix identity.  It does **not** establish that the
formal word is a unit arrow, nor that any one-sided branch domain is nonempty.

## B. Why three prefix systems are necessary

### B.1 Genuine length action

For a raw token \(t\), write \(R(t)=B(t)\).  The AGY length action is

\[
F(t)=R(t)^{-\mathsf T}.
\]

Thus \(F(a)=B(a)^{-\mathsf T}\) and
\(F(a^{-1})=B(a)^{\mathsf T}\).  On the \(j\)-th left rotation of a path
word, the recurrence is

\[
P_0^{(j)}=I,
\qquad
P_k^{(j)}=F(t_k)P_{k-1}^{(j)}.
\]

An orbit requires every row of every \(P_k^{(j)}\) to evaluate positively on
one \(x>0\).

### B.2 Transfer/projective branch action

The composition operator is contravariant.  Reverse the rotated raw path word
and use

\[
A(t)=R(t)^{\mathsf T},
\qquad
Q_k^{(j)}=A(u_k)Q_{k-1}^{(j)}.
\]

This is the C26 operator-factor/application order.  Applying \(B^T\) in raw
path order would be a chronology error.

### B.3 Raw homology control

The recurrence

\[
H_k^{(j)}=R(t_k)H_{k-1}^{(j)}
\]

is covariant and belongs to homology/cocycle coordinates.  It is not the AGY
length recurrence.  The positive controls for C1 and C2 are therefore useful:
they would disappear if the implementation silently reused the length action.

## C. Canonical exact infeasibility certificates

For one phase, collect the four initial coordinate rows and all prefix rows,
ordered by `(step, coordinate)`.

1. If the lexicographically first row has all coefficients nonpositive and is
   nonzero, record it as `NEG_ROW`.
2. Otherwise remove duplicate rows and search, in increasing subset size and
   lexicographic order, for positive rational coefficients whose weighted sum
   is zero.  Clear denominators and divide by the coefficient gcd.

Conic Carathéodory bounds the required subset size by five in dimension four.
For the present words, every non-`NEG_ROW` certificate consists of two
opposite rows with coefficients one.  The checker reconstructs each prefix
matrix and verifies every row and coefficient; it does not trust the producer
status string.

### C.1 C25 C1

The phase-zero length recurrence contains

\[
(0,-1,0,1)
\quad\text{and}\quad
(0,1,0,-1).
\]

They sum to zero.  The remaining five phases have their own canonical
descriptors.  The independent transfer recurrence also supplies six exact
failures.

### C.2 C25 C2

The phase-zero length recurrence contains

\[
(-1,0,0,0),
\]

which is negative on every positive vector.  The full length and transfer
censuses are each \(6/6\) infeasible.

### C.3 C26

The phase-zero length recurrence contains at step eight

\[
(-11430,-460520,-3353,-456200).
\]

Across the twenty-four length phases, fifteen canonical descriptors are
`NEG_ROW` certificates and nine are positive combinations of opposite rows.
Their support sizes are separately distributed as fourteen five-term and ten
two-term certificates.  The phase-zero
transfer recurrence contains at step three

\[
(-984333,-498163,-999116,-479060),
\]

and the transfer census is likewise \(24/24\) infeasible.

These are global exact proofs, not failed attempts to find a single initial
point.  Once the length cone is empty, testing the additional
zippered-rectangle coordinates cannot restore an AGY orbit.

## D. Roof trilemma and identity trichotomy

Every real additive groupoid cocycle obeys

\[
\tau(g^{-1})=-\tau(g).
\]

Hence the following three properties cannot coexist:

1. the second symbol is a genuine inverse arrow;
2. time is an additive groupoid cocycle;
3. both orientations carry strictly positive time.

The natural extension keeps a positive suspension roof in forward time and
uses its negative integral in backward time.  It does not insert a second
positive-time inverse token.

There is a separate kernel issue.  A reduced word with \(B_w=I\) need not be
the unit word of the path groupoid.  An arbitrary edge-constant antisymmetric
cocycle can therefore be nonzero on it.  The exact signed abelianizations are

\[
[C_1]_{\mathrm{ab}}=1b+3t,
\qquad
[C_2]_{\mathrm{ab}}=4t+5b.
\]

By contrast, the projective logarithmic normalizer factors through the matrix
action.  Wherever all prefixes are defined,

\[
\sum_{k=1}^{n}r_{B(e_k)}(x_{k-1})
=\log\frac{\ell(B_wx)}{\ell(x)},
\]

so it vanishes when \(B_w=I\).  The C26 word also has zero signed count in
each branch generator, and thus vanishes for every edge-constant
antisymmetric cocycle.

A symmetric positive edge length is mathematically legitimate only after
declaring a new non-backtracking graph suspension.  In that object inverse
labels are alphabet symbols, not cancellation in an additive-time groupoid.

## E. Repetition and the analytic fork

The two clocks give incompatible repetition laws.

- For the projective normalizer on a holonomy-identity word,

  \[
  T(w^m)=mT(w)=0.
  \]

  The formal flow repetition series becomes \(\sum_{m\ge1}1/m\), and the
  primitive Euler factor is singular already at the first occurrence.
- For the symmetric graph clock, \(T(C_1^m)=6m\) and
  \(T(W_{24}^m)=24m\).  The finite Hashimoto \(u\)-germ is then regular on its
  norm disc, exactly as C29 proved.

One may choose either system, but not use the first clock for primitive
semantics and the second for repetitions.

## F. Operator-ideal obstruction

The non-backtracking rule removes the adjacent word \(ee^{-1}\); it does not
hide the one-step blocks of the finite edge operator.  Coordinate compression
exposes each edge operator \(U_e\).  If the full Hashimoto operator were
compact or nuclear, so would every \(U_e\).  A faithful bounded inverse then
puts

\[
I=U_{e^{-1}}U_e
\]

in the same ideal, which is impossible on an infinite-dimensional fibre.

Unmarked cancellation does not evade this result.  Independent transition or
occurrence variables and a cyclic layer lift isolate a relation-word Cauchy
coefficient.  Holomorphy in nuclear norm would force that coefficient to be
nuclear, but it is either an identity or a boundedly invertible multiplication
operator.

This theorem does not conflict with stable--unstable pinning operators.  A
Fried/Rugh/Baladi--Pujals--Sambarino cross map uses contracting half-inverses
and a partial adjoint between different polarized factors.  It does not
represent a map and its inverse as compact bounded inverses on one space.

## G. Flat-trace dichotomy

On the source positive cone, Section C proves that the three words do not
exist as trajectories.  On an enlarged algebraic domain, the full projective
word is the identity.  Its graph coincides with the diagonal, the fixed set is
the full domain, and

\[
Dh_W=I,
\qquad
\det(I-Dh_W)=0.
\]

The standard isolated-hyperbolic fixed-point atom therefore fails on either
side of the domain fork.  A clean-fixed-manifold or microlocal regularization
is not universally ruled out, but it would define a new zeta prescription and
requires a separate geometric theorem.

## H. Route-A interpretation

- A1 fails for the AGY promotion because the counted words are not source
  positive-domain orbits.
- A2 fails because no ordinary nuclear determinant or standard isolated-orbit
  flat trace realizes them.
- A3 fails before analytic continuation or a prime-like counting law can be
  posed for the promoted object.
- A4 remains a formal hint because exact kernel holonomy may be useful in a
  different system with nontrivial hyperbolic base return.

The finite C29 group-von-Neumann trace-log survives unchanged as a valid
combinatorial determinant.  No Route-B question is reached.
