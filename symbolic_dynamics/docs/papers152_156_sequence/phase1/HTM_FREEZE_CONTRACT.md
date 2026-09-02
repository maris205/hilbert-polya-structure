# HTM final freeze contract — repeated meets on a homogeneous rooted tree

**Contract date:** 2026-09-02 UTC.  
**Formula status:** `COHERENT AS STATED`.  
**Paper-value verdict:** **`KILL_PAPER_VALUE / DO_NOT_DRAFT`**.  
**External status:** `HOLD_EXTERNAL`.  
**Scope effect:** no paper number, manuscript, novelty claim, priority claim, or
release clearance.

This contract deliberately **downgrades** the earlier
`PASS_OWNER_THIN` formula gate.  No formula has failed.  The failure is value:
after Brown's left-regular-band framework and the elementary iid-prefix
calculation receive zero credit, the inverse and extremal steps are too short
to carry an independent note, and their theorem silhouette is too close to the
already occupied P151 package.

## 1. Literal system and invariant object

Fix `h>=1` and integers `b_1,...,b_h>=2`.  The vertices of the fixed
level-homogeneous rooted tree are mixed-radix words, and its leaves have length
`h`.  Fix one leaf `v`, set `X_0=v`, sample iid uniform leaves `U_1,U_2,...`,
and update

```text
X_t = X_{t-1} meet U_t = LCA(X_{t-1},U_t).
```

Write

```text
D_t=depth(X_t),       B_k=product_{j=1}^k b_j,
T=inf{t>=1:D_t=0},    A=sum_{t>=0}D_t.
```

The invariant object organizing every permitted formula is the nested family
of depth cylinders containing `v`.  The abstract semigroup product is not the
claim-bearing object.

## 2. Absolute theorem ceiling

The following are the only three results that could be stated as main
theorems if HTM were ever reopened.  They are frozen here to prevent later
claim inflation; this list does **not** authorize a draft.

### HTM-A — exact depth layers and their all-time transform

Associativity of meet gives

```text
X_t=LCA(v,U_1,...,U_t).
```

For every `t>=0` and `1<=k<=h`,

```text
P(D_t>=k)=B_k^(-t).                                  (A1)
```

For `t>=1`, differencing (A1) gives the complete depth law.  Tail summation
then gives, for `|z|<1`,

```text
sum_{t>=0} z^t E[y^{D_t}]
 = 1/(1-z)
   + sum_{k=1}^h (y^k-y^(k-1))/(1-z/B_k).            (A2)
```

Only the explicit tree-cylinder specialization is eligible.  A generic finite
resolvent, LRB spectrum, convolution formula, or random-product identity is
forbidden contribution language.

### HTM-B — exact known-time inverse and its sharp information boundary

If a positive integer time `t` is known and the exact full law of `D_t` is
given, then the support recovers `h` and

```text
B_k=P(D_t>=k)^(-1/t),
b_1=B_1,       b_k=B_k/B_{k-1}.                       (B1)
```

The theorem must include all negative statements in Section 6: time zero is
uninformative, unknown time has perfect-power ambiguity, the root clock sees
only `b_1`, nonuniform sampling recovers cylinder masses rather than branching
factors, and irregular trees have no single level profile.

### HTM-C — depth-area formula and fixed-multiset factor-order extrema

Tonelli and (A1) give

```text
E A = sum_{k=1}^h B_k/(B_k-1)
    = h + sum_{k=1}^h 1/(B_k-1).                     (C1)
```

For a fixed multiset of branching factors, nondecreasing order uniquely
maximizes `E A`, nonincreasing order uniquely minimizes it, and uniqueness is
modulo permutations of equal factors.  The proof is the adjacent exchange

```text
1/(Pa-1) - 1/(Pb-1),
```

which is positive exactly when `a<b`.

### Supporting result only — root clock

The clock formula

```text
P(T>t)=b_1^(-t),
E[z^T]=(b_1-1)z/(b_1-z),
E T=b_1/(b_1-1),
Var(T)=b_1/(b_1-1)^2
```

may appear only as a lemma/control.  It cannot be advertised as a fourth main
axis because it is geometric and is blind to `b_2,...,b_h`.

## 3. Shortest proof-dependency graph

```text
literal meet update
    |
    v
associative iid product identity
    |
    v
nested cylinder event {D_t>=k}
    |
    +--------------------+----------------------+------------------+
    |                    |                      |
    v                    v                      v
exact tails (A1)    first-level hazard      Tonelli over (t,k)
    |                    |                      |
    +---------+          v                      v
    |         |       geometric T          area identity (C1)
    v         v                                  |
layer law  time OGF (A2)                         v
    |                                        one adjacent swap
    v                                            |
known-t inverse (B1)                             v
                                             sharp factor order
```

This graph is also the decisive value warning: after the cylinder event is
written down, every claimed branch is a one-step operation.

## 4. Owner zero-credit ledger

The later paper, if any, would have to subtract the following in its opening
page rather than burying them in related work.

1. Kenneth Brown,
   [*Semigroups, rings, and Markov chains*](https://arxiv.org/abs/math/0006145),
   directly owns random multiplication on finite left-regular bands, including
   the spectral framework.  A meet-semilattice is a commutative LRB, and HTM
   is literally a leaf-supported random product.
2. Brown's
   [author-hosted survey](https://pi.math.cornell.edu/~kbrown/papers/toronto.pdf)
   owns the same semigroup/ring method and examples.
3. Ayyer--Schilling--Steinberg--Thiéry,
   [arXiv:1401.4250](https://arxiv.org/abs/1401.4250), own generic convolution,
   absorption, and Möbius formulas for LRB/R-trivial walks.  Rhodes--Schilling,
   Pang, and Nestoridi further subtract generic semigroup expansion, lumping,
   and stopping-time language.
4. Fuchs--Steel,
   [arXiv:2501.09270](https://arxiv.org/abs/2501.09270), are a same-observable
   MRCA-depth neighbour.  Generic MRCA/LCA sampling language receives no
   contribution credit.
5. The minimum-of-iid-prefix-depth calculation, geometric series, Tonelli,
   taking positive roots, and adjacent-swap sorting are elementary proof tools
   and receive zero credit independently of citation ownership.

Forbidden claims include “a new semigroup walk,” “new spectral method,” “new
random-product formula,” “first random-LCA law,” and “robust tree
identifiability.”  A bounded owner non-hit is not a novelty finding.

## 5. Internal-paper collision firewall

| occupied item | apparent collision | mandatory separation | value consequence |
|---|---|---|---|
| P128, translation--GCD depth fibres | both are terminating meet-semilattice folds | P128 is the deterministic orbit meet `x meet sigma(x)` and its contribution is an Euler product plus target fibres; HTM is iid leaf meet and has only depth-cylinder probabilities | generic semilattice folding and product identities are zero credit; HTM cannot use the meet formalism as separation value |
| P148, even-level plane-tree contraction | rooted-tree carrier, depth loss, absorption | P148 changes the tree by deleting odd levels and promoting ordered blocks; HTM keeps the tree fixed and moves one ancestor state by LCA | “tree contraction” and binary height-clock language are forbidden; the literal maps are not conjugate |
| P151, unequal-spider first passage | random tree dynamics with an all-time transform, inverse boundary, and fixed-mass extremizers | P151 uses a nontrivial unequal-arm continuant factorization, leaf-marked first passage, variance, and tomography boundary; HTM uses nested iid cylinders and a one-summand exchange | this is the decisive portfolio collision: transform + elementary inverse + elementary extremizer is not enough to create a separated new short note |

P151 is a theorem-silhouette collision rather than a literal-map collision.
That distinction prevents a false conjugacy claim, but it does not rescue HTM's
paper value.

## 6. Mandatory boundaries and counterexamples

Every future treatment must visibly include all of the following.

- **Time zero:** `D_0=h` deterministically, so no branching profile is
  recoverable from the depth layer.
- **Unknown time:** profile `(4,9)` at time one and profile `(2,3)` at time two
  both have tails `(1/4,1/36)`.  Thus (B1) is a known-time theorem only.
- **Clock blindness:** profiles `(2,2)` and `(2,3)` have identical root-clock
  laws; the clock does not identify the full profile.
- **Nonuniform sampling:** (A1) becomes a statement about nested cylinder
  masses, not integer branching factors.
- **Irregular tree:** no global level vector `(b_1,...,b_h)` need exist.
- **Height one:** increasing and decreasing orders coincide, so the extremal
  theorem is tautological.
- **Equal factors:** uniqueness is only modulo exchanges of equal entries.
- **Unary root factor:** allowing `b_1=1` destroys the positive root hazard and
  makes the corresponding area term divergent; the domain `b_i>=2` is
  essential.

## 7. Title and abstract claim ceiling

The strongest admissible title, if the system were ever reopened, is:

> **Depth layers and factor-order area in a repeated tree-meet chain**

The abstract could say only that, on a fixed level-homogeneous rooted tree with
uniform leaf sampling, the repeated meet depth has explicit nested-cylinder
layers, one known positive-time layer determines the branching profile, and
the expected accumulated depth has sharp fixed-multiset ordering extrema.  It
must state that the semigroup-walk framework and generic absorption machinery
are established background.

The abstract may not lead with the LRB representation, the geometric root
clock, generic spectra/resolvents, or a claim about arbitrary/nonuniform trees.
It may not use “novel,” “first,” or an absence-of-prior-work formulation.

## 8. Final hostile value attack

**Strongest counter-argument.**  Brown already owns the literal algebraic
framework.  Once that is removed, (A1) is the probability that iid leaves all
fall in one fixed cylinder; (A2) is a geometric-series sum; (B1) takes roots
and ratios; and (C1)'s extremizer changes one summand under an adjacent swap.
The entire residual proof spine fits in a few elementary paragraphs and
introduces no proof engine not already visible in the first formula.  Moreover,
P151 has just occupied the stronger tree-random-dynamics silhouette of temporal
transform, inverse boundary, and fixed-mass extrema.

**Adjudication.**  The counter-argument succeeds.  Combining three correct
elementary corollaries does not create paper-sized value after the direct
framework owner and the internal silhouette are subtracted.

```text
FORMULAS = PASS
OWNER POSITION = PASS_OWNER_THIN
PAPER VALUE = KILL_PAPER_VALUE
DRAFT = FORBIDDEN
EXTERNAL = HOLD_EXTERNAL
```

Re-entry requires a genuinely new all-parameter axis, such as a nontrivial
irregular/nonuniform inverse with a sharp identifiability boundary or a dynamic
extremal theorem not reducible to ordering one prefix-product summand, followed
by a fresh owner gate.  Merely adding moments, spectra, or more finite examples
does not reopen HTM.

## 9. Frozen evidence

The independent focused verifier and transcript remain read-only evidence:

```text
verify_htm_btb_focused_audit.py
HTM_BTB_FOCUSED_AUDIT_VERIFICATION.txt
PASS assertions=204949
```

The HTM lanes check literal mixed-radix layers, independent finite-resolvent
values, clock moments, known-time reconstruction, unknown-time ambiguity,
area, all audited factor-order extrema, and the `h=1/b_1=1` boundaries.  A cold
replay on 2026-09-02 was byte-identical.  Exact computation supports formula
correctness only; it does not alter the kill verdict.
