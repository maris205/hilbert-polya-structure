# Preregistration — Paper 32 / SD-C34

Date frozen: 2026-08-15 UTC

## Question

Can a source-natural, nonterminal and shared-state recurrent grammar on finite
residue objects separate prime primitive cycles before weighting while its
original uninduced graph-step operator owns an ordinary Fredholm determinant?

## Frozen source and candidate

Retain Paper 31's finite-full-shift alphabet sum/product semiring, successor,
quotient/remainder, congruence, and entropy.  For every \(n\ge2\), reconstruct
\(\mathcal R_n=\mathbb Z/n\mathbb Z\) and its projective line
\(X_n=P^1(\mathcal R_n)\).  Freeze the two projective transformations
\[
 S[a:b]=[-b:a],\qquad R[a:b]=[-b:a+b],
\]
and add bidirectional cusp correspondences between \(c_n=[1:0]_n\) and
\(c_{2n},c_{3n}\).  Every state retains both transitions.  There is no
accept/reject terminal and no recurrent block is selected by a static field
test.

Within-modulus roofs are \(\log n\); either direction of a cross edge between
\(n\) and \(kn\), \(k=2,3\), has roof \(\log(kn)\).  One free marker \(z\)
counts each original graph edge.  Graph, roofs, states, signs, and marker are
frozen before arithmetic labels and analytic evaluation.

## Information boundary

Allowed information is the source semiring and congruence, exact residue-ring
arithmetic implementing it, source-defined units and unimodular pairs, the
fixed matrices and cusp, deterministic cutoffs/seeds, exact hashes, matched
isomorphic relabels, and independent evaluator-only classification after the
candidate graph is enumerated.

Forbidden information is a supplied prime, prime-power, factor,
accepted-support, atom-color, orbit-projector, von Mangoldt, or target-zero
table; candidate-side primality/factorization; any terminal accept/reject
edge; use of \(|X_n|=n+1\) to create/delete recurrent blocks; fitted
coefficients; root matching; Riemann-zero ordinates; first return or induction
that changes the original marker; post-control graph/roof/sign changes; and
Route B.

## Primitive-ledger gates

1. Prove the complete unweighted primitive ledger before assigning analytic
   credit to roofs or determinants.
2. Require marker-distinct recurrent families to share actual states, rather
   than use a disjoint direct sum of prime-coded cycles.
3. Audit prime, prime-power, mixed-composite, seeded random-action, matched
   finite-semiring, and inherited bare-UFD controls.
4. Treat a recurrence mechanism reproduced by arbitrary finite permutations
   satisfying \(a^2=b^3=1\) as `PROVES_TOO_MUCH`.
5. Treat the static equality \(|X_n|=n+1\) as diagnostic only.  If it gates
   recurrence, classify the repair as a forbidden terminal selector.
6. Downward-only cross-modulus structure receives no periodic credit if it is
   transient; bidirectional structure must pass a complete mixed-cycle audit.

## Operator-ownership gates

1. Compactness and determinant class must be proved for the same uninduced
   graph-step operator carrying the original marker.
2. Trace-class estimates must include both the direct sum of finite projective
   blocks and all cross-modulus cusp edges.
3. The parameter \(s\) changes weights on one fixed graph; it may not select
   components.
4. A formal Euler or orbit product is not called a Fredholm determinant
   without trace-class ownership.
5. An honest determinant that contains composite primitive cycles passes A2
   but cannot retroactively pass A1.

## Frozen controls

- all moduli \(2\le n\le192\), independently stratified after census;
- 43 primes, 14 prime-power composites, and 134 mixed composites;
- exact projective counts and labelled traces through order eight;
- all canonical cusp diamonds visible through the cutoff;
- 48 seeded finite \(C_2*C_3\) actions;
- one genuine matched finite-semiring relabel per modulus, transporting the
  complete operation tables and induced graph;
- inherited bare polynomial-UFD failure of ordinary alphabet addition;
- source-oracle scan and byte-identical repeat run.

Finite controls audit implementation.  They do not replace infinite proofs.

## Falsification logic

- `GO_NONTERMINAL_SHARED_RECURRENCE` requires no accept/reject state and
  overlapping recurrent families on shared projective states.
- `A1_FAIL` follows if prime powers or mixed composites retain any primitive
  support before weights.
- `COMPOSITE_DIAMOND_FLOOD` follows if the frozen cusp correspondences produce
  \(n\to2n\to6n\to3n\to n\) for every \(n\).
- `STOP_STATIC_FIELD_DEFECT_PROJECTOR` follows if prime-only support can be
  obtained only by \(\mathbf1_{\{|X_n|=n+1\}}\).
- `A2_ANALYTIC_DETERMINANT` requires the original \(B_s\) to be trace class
  on an explicit half-plane with the marker unchanged.
- `PROVES_TOO_MUCH_AT_GROUP_PRESENTATION_LEVEL` follows if random
  \(C_2*C_3\) actions reproduce the overlap mechanism.
- `CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH` follows when A2 is
  honest but the complete primitive ledger fails A1 for structural reasons.

## Frozen outcome

The candidate is genuinely nonterminal, recurrent, shared-state, and
same-object trace class.  It nevertheless fails prime separation before
weighting because \(S^2=-I\) and \(R^3=-I\) act projectively as the identity
for every modulus, while bidirectional cusp edges create an infinite
composite-diamond family.  The static projective count recognizes primes but
can influence recurrence only through a forbidden terminal block projector.
Thus the strict record is

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

The overall decision is `ROUTE_A_REJECTED`, Route B is `LOCKED`, and the
branch action is `CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH`.
