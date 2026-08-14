# Derivation package — Paper 32 / SD-C34

## Target and invariant object

The derivation asks whether projective residue dynamics can satisfy Paper
31's nonterminal obligation and still produce a prime-selective determinant.
The invariant object is fixed from the start:
\[
 \mathcal H=\bigoplus_{n\ge2}\ell^2(P^1(\mathbb Z/n\mathbb Z)),\qquad
 B_s=B_s^{\rm mod}+C_s.
\]
It is uninduced, retains one free marker per original graph edge, and contains
both within-modulus modular transitions and cross-modulus cusp
correspondences.  No projected or first-return comparison operator is
promoted to primary ownership.

## Assumptions

- The source is the finite-full-shift alphabet sum/product semiring with
  successor, quotient/remainder, congruence, and entropy.
- \(R_n=\mathbb Z/n\mathbb Z\) is reconstructed by source congruence.
- States are unit-scaling classes of unimodular pairs.
- The matrices \(S,R\), cusp \(c_n=[1:0]_n\), multipliers 2 and 3, roofs,
  and marker are frozen before the census.
- All primary weights are nonnegative for real \(s>2\).
- No terminal projector, prime table, fitted coefficient, target zero, or
  Route-B object is available.

## Derivation map

1. Construct \(R_n\) and \(X_n=P^1(R_n)\) from source equations.
2. Count \(X_n\) and isolate the static field defect.
3. Compute the projective relations of \(S,R\) before choosing weights.
4. Audit downward and bidirectional cross-modulus orientations.
5. Freeze the graph-step operator and bound both trace-norm series.
6. Form the ordinary determinant only after same-object ownership is proved.
7. Compare the primitive ledger against prime/composite, random-action,
   matched-clone, and inherited bare-UFD controls.
8. Apply the strict Route-A gates in their preregistered order.

## Step 1 — source quotient and projective states

The source quotient/remainder relation gives each residue as a unique class
modulo \(n\).  Addition and multiplication are alphabet operations followed
by remainder.  A state is a pair \((a,b)\) for which
\[
 ua+vb=1\pmod n
\]
for some residues \(u,v\), modulo simultaneous multiplication by a unit.
This definition does not classify the modulus.

## Step 2 — static defect

For a prime power \(q=p^a\), the local representatives
\([t:1]\), \(t\in\mathbb Z/q\mathbb Z\), and
\([1:u]\), \(u\in p\mathbb Z/q\mathbb Z\), give
\(q+q/p\) points.  Chinese remaindering yields
\[
 \psi(n)=|X_n|=n\prod_{p\mid n}(1+p^{-1}).
\]
Consequently
\[
 \delta(n):=\psi(n)-(n+1)=0
 \quad\Longleftrightarrow\quad n\text{ is prime}.
\]
The defect is structural but static: it has not yet changed the periodic
ledger.

## Step 3 — universal within-modulus recurrence

Direct multiplication gives
\[
 S^2=-I,qquad R^3=-I.
\]
Since scalar \(-I\) is projectively trivial,
\[
 S_n^2x=x,qquad R_n^3x=x
\]
for every state \(x\in X_n\) and every modulus.  Thus every state belongs to
an \(S\)-orbit of length one or two and an \(R\)-orbit of length one or
three.  The labels distinguish the two return families even if a vertex
sequence degenerates.  The mechanism establishes the desired overlap but
does so equally for primes and composites.

## Step 4 — cross-modulus orientation

A downward-only residue edge strictly decreases the positive integer modulus;
within-block edges preserve it.  Such an edge cannot occur in a closed path,
so the cross-modulus arithmetic is transient in every power trace.

Bidirectional cusp edges instead give
\[
 c_n\to c_{2n}\to c_{6n}\to c_{3n}\to c_n.
\]
The vertices are distinct, no consecutive operations are inverse, the path
is simple and primitive, and \(6n\) is composite.  The family overlaps since
the diamonds based at \(n\) and \(2n\) share two cusps.  Hence the natural
reduction/correspondence skeleton has an exact dichotomy: transient arithmetic
or recurrent composite flood.

## Step 5 — frozen weighted operator

Let \(P_{S,n},P_{R,n}\) denote the two permutation operators.  Put
\[
 B_s^{\rm mod}=\bigoplus_{n\ge2}n^{-s}(P_{S,n}+P_{R,n})
\]
and
\[
 C_s=\sum_{n\ge2}\sum_{k\in\{2,3\}}(kn)^{-s}
 \bigl(|c_{kn}\rangle\langle c_n|+|c_n\rangle\langle c_{kn}|\bigr).
\]
The exponent comes from the frozen roof of the corresponding original edge.
The marker \(z\) counts each application of \(B_s\); it is not compressed by
first return.

## Step 6 — trace-class ownership

With \(\sigma=\operatorname{Re}s\),
\[
 \|B_s^{\rm mod}\|_1
 \le2\sum_{n\ge2}\psi(n)n^{-\sigma}
 \le2\sum_{n\ge2}\sigma_1(n)n^{-\sigma}.
\]
Since
\[
 \sum_{n\ge1}\sigma_1(n)n^{-\sigma}
 =\zeta(\sigma)\zeta(\sigma-1),
\]
the modular direct sum is trace class for \(\sigma>2\).  Every cusp map is
rank one, giving
\[
 \|C_s\|_1
 \le2(2^{-\sigma}+3^{-\sigma})\sum_{n\ge2}n^{-\sigma},
\]
which converges for \(\sigma>1\).  Both majorants are locally uniform on
closed half-planes inside \(\sigma>2\).  Therefore \(s\mapsto B_s\) is
trace-norm holomorphic there and
\[
 D_{\rm PR}(s,z)=\det(I-zB_s)
\]
is an ordinary same-object Fredholm determinant, entire in \(z\).

## Step 7 — owned composite terms

For real \(s>2\), nonnegative entries prevent cancellation.  The \(SS\) word
contributes
\[
 \psi(n)n^{-2s}
\]
to \(\operatorname{Tr}(B_s^2)\), and \(RRR\) contributes
\(\psi(n)n^{-3s}\) to \(\operatorname{Tr}(B_s^3)\).  The cusp diamond has
weight
\[
 (2n)^{-s}(6n)^{-s}(6n)^{-s}(3n)^{-s}=(216n^4)^{-s}.
\]
These contributions are present before the determinant is formed and for
every composite modulus.

## Step 8 — why the static repair is terminal

The only immediate prime-only block repair is
\[
 Q=\bigoplus_{n\ge2}\mathbf1_{\{\delta(n)=0\}}I_{\ell^2(X_n)}.
\]
Because \(\delta(n)=0\) is equivalent to primality, \(Q\) completes the
global field test before recurrence is admitted.  It is selector-equivalent
to the terminal branch closed in Paper 31 and violates the frozen candidate.

## Step 9 — controls and route record

An isomorphic semiring relabel transports units, projective classes, matrices,
cusps, roofs, operator, and determinant.  Exact agreement is required by
naturality.  Conversely, any finite permutations \(a,b\) with
\(a^2=b^3=I\) reproduce recurrence through every state, showing that the
within-block mechanism is a generic presentation compiler.  The inherited
bare polynomial-UFD clone remains outside the enriched source because
ordinary polynomial addition cannot respect \(2=1+1\).

The strict record is

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL).

A2 is a genuine advance over Paper 31.  A1 nevertheless fails earlier, at the
unweighted primitive transition algebra.  No A3 continuation, intrinsic Weil
compression, A4 self-adjoint carrier, or zero correspondence is available.

## Open boundary

This derivation does not rule out a source-derived quotient representation or
cycle homology that annihilates \(S^2\), \(R^3\), and the cusp diamonds before
weights.  It does rule out relabelling the static field defect as emergent
recurrence.  Paper 33 must decide the remaining quotient/twist question on
the same object or close the full semiring-residue family.
