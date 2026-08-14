# Proof package — Paper 32 / SD-C34

## Main claim

Let \(R_n=\mathbb Z/n\mathbb Z\), \(X_n=P^1(R_n)\), and let the matrices
\[
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 R=\begin{pmatrix}0&-1\\1&1\end{pmatrix}
\]
act projectively on every \(X_n\).  Connect the cusp \(c_n=[1:0]_n\) in
both directions to \(c_{2n}\) and \(c_{3n}\).  Give a within-\(n\) edge roof
\(\log n\) and either cross edge between \(n\) and \(kn\) the roof
\(\log(kn)\), \(k\in\{2,3\}\).  Then:

1. \(|X_n|=n\prod_{p\mid n}(1+p^{-1})\), and \(|X_n|=n+1\) exactly for
   prime \(n\);
2. every state for every modulus lies on both an \(S\)- and an
   \(R\)-marked recurrent orbit;
3. every \(n\ge2\) gives a simple primitive nonbacktracking cusp cycle
   \(n,2n,6n,3n,n\) through a composite top modulus;
4. the original uninduced graph-step operator is trace class and
   trace-norm holomorphic for \(\operatorname{Re}s>2\), hence owns an ordinary
   Fredholm determinant;
5. the determinant is not prime-selective, and restricting it to blocks with
   \(|X_n|=n+1\) inserts a completed primality gate;
6. matched semiring presentations transport the full construction, whereas
   arbitrary finite \(C_2*C_3\) actions reproduce its universal recurrence.

The positive prime-selective claim is false.  The corrected result is a
source-specific obstruction theorem with honest analytic ownership.

## Definitions and assumptions

A pair \((a,b)\in R_n^2\) is **unimodular** if
\(ua+vb=1\) for some \(u,v\in R_n\).  The projective line is the quotient of
unimodular pairs by simultaneous multiplication by a unit.  All states,
edges, roofs, and the free edge marker are fixed before independent arithmetic
labels are evaluated.  No terminal selector, induced return map, signed
cancellation, target-zero data, or Route-B object is admitted.

## Lemma 1 — local projective-line count

For a prime power \(q=p^a\),
\[
 |P^1(\mathbb Z/q\mathbb Z)|=q+q/p.
\]

**Proof.**  The ring \(A=\mathbb Z/q\mathbb Z\) is local with maximal ideal
\(pA\).  A pair is unimodular precisely when one coordinate is a unit.  If
the second coordinate is a unit, the class has a unique representative
\([t:1]\) with \(t\in A\), giving \(q\) classes.  If the second coordinate
is a nonunit, the first must be a unit and the class has a unique
representative \([1:u]\) with \(u\in pA\), giving \(q/p\) further classes.
The families are disjoint because their second coordinates are respectively
units and nonunits.  ∎

## Lemma 2 — Chinese-remainder multiplicativity

For finite commutative rings \(A,B\),
\[
 P^1(A\times B)\cong P^1(A)\times P^1(B).
\]

**Proof.**  A pair over \(A\times B\) is unimodular exactly when both
coordinate pairs are unimodular.  Units and simultaneous unit scaling are
also componentwise.  Taking equivalence classes gives the asserted
bijection.  ∎

## Proposition 3 — exact static field defect

For every \(n\ge2\),
\[
 |X_n|=\psi(n)=n\prod_{p\mid n}\left(1+\frac1p\right),
\]
and \(\psi(n)=n+1\) if and only if \(n\) is prime.

**Proof.**  Apply the Chinese remainder theorem and Lemmas 1--2 to the
prime-power factors of \(n\).  When \(n=p\), the formula gives \(p+1\).  If
\(n\) is composite and \(p\mid n\), then \(n/p\ge2\), and positivity of the
remaining factors gives
\[
 \psi(n)\ge n(1+1/p)=n+n/p\ge n+2.
\]
Thus a composite cannot have \(\psi(n)=n+1\).  ∎

## Lemma 4 — universal modular relations

On every \(X_n\),
\[
 S_n^2=I,\qquad R_n^3=I.
\]

**Proof.**  Direct multiplication gives
\[
 S^2=-I,\qquad
 R^2=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},\qquad
 R^3=-I.
\]
Both matrices have determinant one and preserve unimodularity.  The scalar
\(-I\) multiplies both coordinates by the unit \(-1\), hence acts trivially
on a projective class.  ∎

## Proposition 5 — universal overlapping primitive support

For every \(n\ge2\) and every \(x\in X_n\), the labelled grammar has an
\(S\)-primitive orbit of length one or two through \(x\) and an
\(R\)-primitive orbit of length one or three through \(x\).

**Proof.**  Lemma 4 makes the least positive \(S\)-return time divide two and
the least positive \(R\)-return time divide three.  The least return words are
primitive.  Their generator labels differ, and both visit \(x\).  The proof
never inspects whether \(n\) is prime, a prime power, or a mixed composite.
∎

This proposition meets the shared-state requirement and simultaneously
refutes primitive prime separation before weights.

## Proposition 6 — reduction/recurrence dichotomy

One-way cross-modulus reduction contributes no periodic orbit.  The frozen
bidirectional cusp correspondence contributes a primitive nonbacktracking
four-cycle through a composite modulus for every \(n\ge2\).

**Proof.**  Along a one-way edge from \(kn\) to \(n\), the positive integer
modulus strictly decreases.  Within-modulus edges keep it fixed.  No closed
path can therefore use a downward-only cross edge.

For bidirectional edges, the four distinct cusps
\[
 c_n\to c_{2n}\to c_{6n}\to c_{3n}\to c_n
\]
exist by the multipliers 2 and 3.  The cyclic operation word is
\(\times2,\times3,\div2,\div3\); no edge immediately reverses its predecessor,
including at the cyclic boundary.  The path is simple, hence not a proper
repetition, and is primitive.  Its top modulus \(6n\) is composite.  The
diamonds based at \(n\) and \(2n\) share \(c_{2n}\) and \(c_{6n}\), so the
cross-modulus recurrence is overlapping rather than a disjoint collection of
blocks.  ∎

## Theorem 7 — honest same-object Fredholm ownership

Let \(P_{S,n},P_{R,n}\) be the permutation operators on \(\ell^2(X_n)\), and
write
\[
 J^+_{k,n}=|c_{kn}\rangle\langle c_n|,\qquad
 J^-_{k,n}=(J^+_{k,n})^*.
\]
On \(\mathcal H=\bigoplus_{n\ge2}\ell^2(X_n)\), define
\[
 B_s^{\rm mod}=\bigoplus_{n\ge2}n^{-s}(P_{S,n}+P_{R,n}),
\]
\[
 C_s=\sum_{n\ge2}\sum_{k\in\{2,3\}}(kn)^{-s}
 (J^+_{k,n}+J^-_{k,n}),\qquad B_s=B_s^{\rm mod}+C_s.
\]
Then \(B_s\) is trace class and trace-norm holomorphic for
\(\operatorname{Re}s>2\).  Consequently
\[
 D_{\rm PR}(s,z)=\det(I-zB_s)
\]
is the ordinary Fredholm determinant of the same uninduced graph-step
operator, entire in \(z\) and holomorphic in \(s\) on that half-plane.

**Proof.**  A permutation on a \(d\)-dimensional Hilbert space is unitary and
has trace norm \(d\).  With \(\sigma=\operatorname{Re}s\), Proposition 3 gives
\[
 \|B_s^{\rm mod}\|_1
 \le2\sum_{n\ge2}\psi(n)n^{-\sigma}.
\]
For each prime-power factor,
\(1+p^{-1}\le1+p^{-1}+\cdots+p^{-a}\), hence
\(\psi(n)\le\sigma_1(n)\).  The absolutely convergent identity
\[
 \sum_{n\ge1}\sigma_1(n)n^{-\sigma}
 =\zeta(\sigma)\zeta(\sigma-1)
\]
holds for \(\sigma>2\), proving trace-class convergence of the direct sum.
Each \(J^\pm\) has rank and trace norm one, so
\[
 \|C_s\|_1\le
 2(2^{-\sigma}+3^{-\sigma})\sum_{n\ge2}n^{-\sigma},
\]
which converges already for \(\sigma>1\).  Both operator series converge
locally uniformly in trace norm on \(\operatorname{Re}s>2\).  Termwise
holomorphy therefore makes \(s\mapsto B_s\) trace-norm holomorphic.  The
standard trace-class determinant theorem yields the stated determinant and
analyticity.  No return map or comparison operator has replaced \(B_s\).  ∎

## Proposition 8 — composite terms in the owned trace ledger

For positive real \(s>2\), the trace ledger of \(B_s\) has strictly positive
within-modulus contributions from every composite \(n\), together with the
primitive cross-modulus diamonds of Proposition 6.

**Proof.**  All matrix entries are nonnegative.  In
\(\operatorname{Tr}(B_s^2)\), the labelled word \(SS\) fixes all \(\psi(n)\)
states and contributes \(\psi(n)n^{-2s}\).  The word \(RRR\) contributes
\(\psi(n)n^{-3s}\) to \(\operatorname{Tr}(B_s^3)\).  The diamond based at
\(n\) has edge-weight bases \(2n,6n,6n,3n\), hence weight
\[
 (2n)^{-s}(6n)^{-s}(6n)^{-s}(3n)^{-s}=(216n^4)^{-s}>0.
\]
Every statement applies to composite \(n\); positivity prevents cancellation
on the frozen real axis.  ∎

## Proposition 9 — matched-presentation transport

Any isomorphism of the complete semiring/congruence source transports
\(X_n\), the \(S,R\) actions, cusp edges, roofs, \(B_s\), and its determinant
exactly.

**Proof.**  A source isomorphism preserves zero, one, addition,
multiplication, units, and the equation \(ua+vb=1\).  It maps unimodular pairs
to unimodular pairs and commutes with unit scaling, so it induces a bijection
of projective lines.  The formulas for \(S,R\), the cusp, cross edges, and
roofs use only those transported operations and fixed source constants.  The
induced unitary on \(\mathcal H\) conjugates the operators.  Fredholm
determinants are invariant under unitary conjugacy.  ∎

## Proposition 10 — generic presentation compiler

Let \(Y\ne\varnothing\) be finite, and let permutations \(a,b\) of \(Y\)
satisfy \(a^2=b^3=I\).  Their labelled action graph has marker-distinct
recurrent words through every state.

**Proof.**  The least return time under \(a\) divides two and the least return
time under \(b\) divides three.  The two generator labels distinguish the
return words.  No ring structure occurs in the argument.  ∎

## Corollary 11 — projective-residue recurrence trilemma

The frozen grammar simultaneously has a source-natural static prime
criterion, universal nonterminal shared-state recurrence, and an honest
same-object Fredholm determinant.  Its recurrent ledger is not
prime-selective.  Repair by
\[
 Q=\bigoplus_{n\ge2}\mathbf1_{\{|X_n|=n+1\}}I_{\ell^2(X_n)}
\]
is exactly a completed primality projector.

**Proof.**  Proposition 3 identifies the coefficient of \(Q\) with the prime
indicator.  Propositions 5, 6, and 8 show composite primitive support before
that projection.  Theorem 7 gives same-object ownership, Proposition 9 gives
matched-clone transport, and Proposition 10 shows that the presentation-level
recurrence proves too much.  ∎

The strict route record is therefore

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

with `ROUTE_A_REJECTED`, Route B locked, and branch action
`CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH`.

## Boundaries

The proof does not classify every semiring grammar, signed cocycle,
supersymmetric determinant, reduced homology, or representation-theoretic
quotient.  It proves no continuation to the critical line, functional
equation, Weil criterion, fixed self-adjoint carrier, zero correspondence, or
Riemann-hypothesis statement.  A source-natural cycle quotient that kills the
three universal cycle families without a block selector remains the exact
Paper 33 question.
