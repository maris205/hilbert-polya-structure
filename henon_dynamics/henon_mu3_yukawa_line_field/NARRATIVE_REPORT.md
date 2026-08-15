# HCS-C56 research narrative

Status: **DOCS_FINAL_NO_MORE_EDITS; exact narrative for the project
RELEASE_FROZEN.**

## From a Yukawa tensor to a new arithmetic object

HCS-C55 produced an exact four-variable Yukawa cubic over \(\mathbf Q\) and
proved that its projective zero locus is a smooth geometrically irreducible
cubic surface. HCS-C56 asks a question that C55 did not answer: how does
absolute Galois act on the 27 lines of that particular surface?

The shift is substantial. The input is still the frozen C55 cubic, but the
new object is its Fano scheme

$$
F_1(Y)\subset\operatorname{Gr}(2,4).
$$

Its arithmetic can be much richer than the equation of \(Y\). A smooth cubic
surface always has 27 geometric lines, yet those lines can split into many
Galois orbits and can require fields with very different normal closures.
Smoothness alone therefore predicts neither connectedness nor a maximal
Galois group.

## The certified exact description

The prefreeze calculation presents the entire line scheme as

$$
F_1(Y)\cong\operatorname{Spec}(E),\qquad
E=\mathbf Q[d]/(g),\qquad [E:\mathbf Q]=27,
$$

where \(g\) is irreducible. Thus the 27 geometric lines are the conjugates of
one closed point rather than several rational or lower-degree components.

The field \(E\) records one line together with its conjugates, and it is not
Galois. The distinct normal closure \(K\) is the common splitting field in
which every line is defined. The exact result is

$$
\operatorname{Gal}(K/\mathbf Q)\cong W(E_6),\qquad
|W(E_6)|=51840.
$$

Keeping \(E\) and \(K\) separate is essential: their roles and expected
degrees are different.

## Why the proof is scheme-theoretic

On the standard Grassmann chart \(U_{01}\), a line is written using four
parameters \(a,b,c,d\). Restricting the cubic to that line gives four exact
equations. The certificate provides a degree-27 eliminant in \(d\), three
linear back-substitutions, and direct zero remainders in all four equations.

That calculation initially constructs a closed subscheme only inside the
chart open. The global bridge uses the geometry of the Fano scheme: the
classical total of 27 and the simple-zero theorem make \(F_1(Y)\) finite
étale. Every open of a finite étale scheme is open-and-closed, so the chart
subscheme is also globally closed. Equality of rank 27 then identifies it
with the complete line scheme. Complementary-chart unit ideals provide a
second convention guard, but they do not replace this global argument.

## Why four modular factorizations matter

Irreducibility is proved without trusting a one-line computer-algebra
verdict. At four good primes the certificate stores every monic factor,
multiplies the factors back, checks squarefreeness, and derives the possible
degrees of a rational factor from subset sums. Since the intersection of the
four subset-sum sets is \(\{0,27\}\), no proper rational factor exists.

This establishes connectedness and transitivity. It does not yet establish
full \(W(E_6)\) without the separate Coxeter-parity gate.

## The maximal Galois step

The incidence-preserving action on the 27 lines lies in \(W(E_6)\). A
Frobenius element with cycle type

$$
(2,5,5,5,10)
$$

has an order-five power. Elsenhans--Jahnel's subgroup criterion then reduces
the transitive possibilities to the simple index-two subgroup \(U\) and the
full Weyl group. The exact enumeration proves that every element of the same
target type lies outside \(U\), using determinant in the \(E_6\) reflection
representation.

Ordinary permutation sign on the 27 letters cannot perform this test: every
element of \(W(E_6)\) acts by an even permutation there. The exact enumeration
finds all 5184 target-type elements outside \(U\), with zero inside it.

## Picard and line consequences

Over an algebraic closure a smooth cubic surface has Picard rank seven. The
full Weyl action fixes only the canonical line in the rational Picard space,
so its invariant rank is one. Hochschild--Serre then identifies the
arithmetic Picard rank with that invariant rank after tensoring with
\(\mathbf Q\); it does not assert integral equality of Picard groups.

Connectedness has an elementary but strong consequence. Any finite extension
\(L/\mathbf Q\) over which one line is defined receives an embedding of a
conjugate of the degree-27 field \(E\). Hence

$$
27\mid[L:\mathbf Q].
$$

In particular the surface has no \(\mathbf Q\)-line. This says nothing by
itself about \(\mathbf Q\)-points or rationality of the surface.

## What is new, and what is not claimed

The exact prefreeze mathematical contribution of C56 is an arithmetic
fingerprint of one distinguished cubic surface: its connected line field,
maximal incidence-compatible Galois closure, and Picard ranks. A bounded
search through 2026-08-15 did not locate a prior computation of this exact
surface and field. That statement is query-bounded and is not an exhaustive
novelty theorem.

C56 does not claim:

- a rational point or rational parametrization;
- a Hasse-principle or Brauer--Manin result;
- a zeta function, automorphy theorem, or functional equation;
- a motive, VHS, or Calabi--Yau realization;
- the same Galois group for every Yukawa or Hénon cubic surface.

## Current state

The theorem, derivation, proof, methodology, source audit, and exact machine
replay pass at code/results prefreeze.  The instance-specific eliminant,
modular factors, Weyl enumeration, independent checker, 2684/2684 rebound
suite, and 15/15 tests are part of that milestone.  The official final paper
build and documentation audit pass.  The project is `RELEASE_FROZEN` at
implementation commit `b32402f1dd276a2684d3e849dae26150ebb595e1`, while the
machine evidence remains `PREFREEZE_CODE_RESULTS_PASS`.  The provenance commit
remains null/external.  The 46-entry self-excluding full-project manifest is
verified externally as a release-wide integrity ledger and is not a theorem
premise.
