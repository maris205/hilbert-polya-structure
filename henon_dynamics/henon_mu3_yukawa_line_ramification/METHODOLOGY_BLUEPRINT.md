# HCS-C58 methodology blueprint

Status: **THEOREM_TARGET_LOCKED; PREFREEZE_CODE_RESULTS_PASS;
POSTREFRESH_PASS; FORMAL_DOCS_PASS; PAPER_PENDING;
NOT_RELEASED.**

## 1. Methodological principle

C58 is a proof-guided exact local-to-global project. Every theorem sentence
must decompose into:

1. a frozen upstream object;
2. a universal theorem with an exact locator;
3. an exact local or finite-group calculation;
4. a written bridge from the calculation to the theorem;
5. an independent replay;
6. a negative mutation that would fail if the bridge were wrong.

The Phase-1 calculations selected the target; the official project-local
tuple now certifies the machine layer. This remains a prepaper, non-release
authority.

## 2. Evidence layers

### Layer A: frozen upstream objects

G0 must import, without mutation:

- the HCS-C55 primitive cubic surface and divided-discriminant inputs;
- the HCS-C56 degree-27 field polynomial, line action, field certificate,
  and \(W(E_6)\)-normal-closure theorem;
- the HCS-C57 two degree-36 resolvers, double-six action, and exact group
  generators.

The two resolver identities are imported symmetrically, but their C58 local
roles are asymmetric: theta alone is `KRASNER_CERTIFIED_AUTHORITY`; delta is
`BOUNDED_NON_RESULT_NONDEPENDENCY`, neither a dependency nor corroboration.

The importer must record complete hashes, persistent paths, upstream layered
statuses, and fresh checker replays. Prefix-only or temporary-path authority
is forbidden.

### Layer B: universal mathematics

The written proof uses:

- Serre's lower ramification filtration and tame action on graded quotients;
- Serre, *Local Fields*, Chapter II §2, Exercises 1--2, printed p. 30, for the
  Krasner/Hensel factor-stability criterion (not any C58 instance bound);
- the Artin conductor formula and conductor--discriminant identity;
- Picard--Lefschetz at a transverse ordinary quadratic singularity;
- Saito's divided-discriminant/determinant relation;
- elementary Galois discriminant induction.

GAP's `U4(2).2` Table-of-Marks convention and CTblLib 1.3.1 fix reproducible
subgroup/character identifiers; software tables do not supply the instance
classification theorem.

These sources do not choose a C58 subgroup or compute a frozen local field.

### Layer C: exact local arithmetic

For \(p=3,5,181,997,2346241\), the project must normalize:

\[
(\deg P_i,e_i,f_i,d_i)
\]

for every local factor, together with:

- field-discriminant contribution \(f_i d_i\);
- local power-index valuation;
- maximal-order basis or an equivalent certified order;
- the exact source polynomial and transformation.

At \(p=2\), a global or local maximal-order witness proves exponent zero. At
the tame C3 primes, theta at `[20,30,40]` clears bounds 24/24 and certifies
degrees `(3,6,9,18)`; delta's bounds 840/408 are not cleared at 40. At the
wild primes, theta at `[900,950,1000]` clears p=3 bounds 886/538 and p=5
bounds 746/246. At reflection primes, four-chart elimination, Hensel lift,
valuation-one smoothing, regularity, and Picard--Lefschetz are geometric
authority and must not be mislabeled as an \(e/f\) computation.

### Layer D: exact finite-group classification

The 27-line and 36-double-six actions are independent carriers. A candidate
must satisfy simultaneously:

- decomposition-orbit patterns;
- inertia-orbit refinements;
- normality of each ramification subgroup;
- cyclic tame quotient;
- elementary-abelian positive graded quotients;
- branchwise different equations;
- Serre's tame-character action.

The exhaustive p=3 D/I list is `(140,140,1)`, `(142,142,1)`,
`(206,140,2)`, `(206,142,2)`; ToM 206 is D-only. The deep-profile inventory
ToM `6x2,7,8` is solved in exact `Fraction` arithmetic, yielding formal
solutions `(7,-18),(1,6),(7,-18)` and selecting only ToM 7. Serre inversion
then leaves `(D,I)=(140,140),(206,140)`. At p=5, hits 147/247/295 reduce to
the unique pair `(147,147,1)` by Sylow-5 normality.

### Layer E: character and global closure

For each subgroup \(H\) in a filtration, recompute

\[
\dim V_6^H,\qquad \dim V_{20}^H.
\]

Then derive, with exact rational arithmetic,

\[
\operatorname{Sw}_p(V)
=\sum_{i\ge1}\frac{|I_i|}{|I_0|}
  \operatorname{codim}V^{I_i},
\]

\[
a_p(V)=\operatorname{codim}V^{I_0}+\operatorname{Sw}_p(V).
\]

Every rational term must sum to an integer, and every branchwise permutation
conductor must reproduce the direct local different.

### Layer F: independent hostile verification

The checker must reconstruct claims from primitive inputs rather than compare
the producer's booleans. It must reject:

- a changed \(p=3\) deep-layer count;
- central instead of inversion action;
- the size-480 instead of size-80 tame \(C_3\);
- one changed \(e,f,d\) row;
- a missing reflection witness;
- a wrong global exponent.
- delta promoted to authority or corroboration;
- a deleted D/I pair, ToM 206 treated as inertia, or deep ToM 6/8 selected;
- any omitted Hensel/regularity/Picard--Lefschetz reflection link;
- subgroup ToM 5 conflated with element-class index 17, or CTblLib drift;
- any `NO_BAD_EULER_OR_ROOT_NUMBER` forbidden claim.

Changing \(|D_3|=18\) to \(36\) must leave inertia-sensitive results
unchanged while the Euler-factor firewall remains active.

## 3. G0--G7 workflow

### G0: SOURCE_LOCK

Bind every frozen input and replay the upstream checkers. Reject reordered
field roles, \(E=K\), or any local file whose polynomial does not match C56.

### G1: BAD_PRIME_EXHAUSTION

Reproduce the divided discriminant by two independent exact implementations.
Its nine-prime surface envelope is
`{2,3,5,181,283,997,1801,2346241,q}`; the exact ramified support of both
\(E\) and \(K\) deletes 2, and the `Disc(E)` exponent vector on the envelope
is `(0,46,36,18,6,18,6,18,6)`. Bind the 27-element order basis and its
discriminant, including the core-free bridge proving p=2 unramified in K.

### G2: LOCAL_ORDER_EXACT

Parse the normalized local arithmetic table. Verify

\[
\sum_i f_i d_i=v_p(\operatorname{Disc}E)
\]

at every arithmetic prime. Polynomial discriminants may be used only for the
explicit theta Krasner inequalities above; they cannot substitute for field
differents or field discriminants. Delta cannot supply a theorem leaf.

### G3: DUAL_ACTION_CLASSIFY

Rebuild \(W(E_6)\), both permutation actions, all 350 subgroup classes,
normalizers, orbit refinements, and every D/I pair. Output every survivor
before applying G4.

### G4: FILTERED_INERTIA

Solve the lower-layer lengths from branchwise differents using exact
`Fraction` arithmetic and the full ToM `6x2,7,8` inventory. At p=3, apply
Serre IV.2 Proposition 9 to final \(G_7/G_8\), reject central ToM 142, and
retain exactly `(D,I)=(140,140),(206,140)`. Record
\(|D_3|\in\{18,36\}\) as an explicit nondependency. At reflection primes,
require the complete Hensel/regularity/Picard--Lefschetz bridge and ToM 2.

### G5: CHARACTER_CONDUCTOR

Compute fixed dimensions and local Swan/Artin pairs. Check both the 27-line
and degree-36 permutation conductors orbit by orbit.

### G6: GLOBAL_INFINITY

Derive

\[
v_p(\operatorname{Disc}K)
=\frac{51840}{|I_0|}
  \sum_{i\ge0}(|I_i|-1)
\]

and the global formulas. Recompute the real-root counts and separately select
subgroup ToM 5 and `CharacterTable("U4(2).2")` element-class index 17 (size
540, centralizer 96) under CTblLib 1.3.1.

### G7: REPLAY_SCOPE

Run the independent checker, strict schema, complete mutation suite, scoped
manifest, temporary-artifact scan, and exact
`NO_BAD_EULER_OR_ROOT_NUMBER` scan. G7 certifies code/results prefreeze only;
it cannot claim paper or release completion.

## 4. Slow-computation policy

The default replay should consume normalized raw local outputs and verify
them exactly. Multi-minute PARI regeneration belongs to an explicit slow
target with resource bounds and logs; it must not be silently rerun inside
the default checker.

This split is honest only if:

- raw outputs are byte-bound;
- their input polynomial and command semantics are recorded;
- the checker independently verifies every compact consequence;
- regeneration remains documented and available.

## 5. Written/machine interface

Machine-certified:

- exact input identities;
- theta authority inequalities and delta nondependency;
- finite orbit and subgroup data;
- exhaustive D/I pairs and ToM `6x2,7,8` Fraction selection;
- local order rows and different sums;
- fixed dimensions and conductor arithmetic;
- global exponent arithmetic;
- root counts and cycle types;
- reflection Hensel booleans and separate archimedean subgroup/element indices;
- hostile mutation rejection.

Written proof:

- application of Serre Proposition 9;
- application of the full Hensel-to-Picard--Lefschetz bridge at reflection primes;
- good-reduction/unramifiedness implication outside the support;
- conductor--discriminant implications;
- the logical meaning of the \(D_3\) ambiguity;
- theta/delta authority semantics and the
  `NO_BAD_EULER_OR_ROOT_NUMBER` boundary.

Neither side may silently absorb the other.

## 6. Current milestone

The official code/results tuple passed all eight G0--G7 gates, 45 tests, its
mandatory nonmutating replay, and the independent `POSTREFRESH_PASS` audit. It
binds certificate `456a4813...`, payload `fba2df...`, schema `ccbc20eb...`,
check `64454700...`, evidence `e374d3...`/`0e0b3f...`, and manifest
`a1874229...`, with counts code/results/live/scoped `14/8/22/21` and leaf
counts `1149/1199`. The independent hostile review of the updated formal
documents also passes; paper and release remain pending.
