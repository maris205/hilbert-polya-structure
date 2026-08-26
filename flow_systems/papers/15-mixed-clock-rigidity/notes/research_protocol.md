# Paper 15 research protocol

Status: **PHASE-1 USER-CONFIRMED / INDEPENDENT REVIEW REQUIRED**  
Version: `P15-P1-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Working title: **Mixed Prime-Clock Standardization and Global Scaling Rigidity**  
Route B, proof implementation, controls, Route A, manuscript, release, and
Git/public synchronization: false

Batch design lock:

```text
sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
```

## 1. Research question

Paper 12 standardizes a nonempty coproduct of transitive real torsors when
every orbit has the same stabilizer `H=L Z`.  Paper 15 asks for the exact
mixed-lattice version and its prime-clock application:

> Can the actual globally indiscrete carrier with orbit-dependent cocompact
> stabilizers be standardized canonically, can all strict and globally
> scaled equivariant isomorphisms be classified, and does the unlabeled
> family `L_p=log(p)` admit any nontrivial common positive rescaling combined
> with a permutation of primes?

The substantive arithmetic theorem is the last clause.  A componentwise
standardization or wreath-product description alone is routine background.

## 2. Generic mixed-lattice owner

Let `X` be a nonempty globally indiscrete set with a right `R`-action.  Let
`Q=X/R` be the bare nonempty orbit set.  For every orbit `q in Q`, require

```text
Stab(x)=H_q=L_q Z,  L_q>0,  for every x in q.
```

The value `L_q` is literal positive real data determined by the action, not
an external label.  Write this category provisionally as `C_mix`.

Morphisms have three separately registered variances:

- strict: `F(x.t)=F(x).t`;
- globally `c`-scaled, `c>0`: `F(x.t)=F(x).(c t)`;
- unmarked: algebraic orbit-groupoid isomorphisms with no fixed time map.

No statement may move between these variances without an explicit functor.

## 3. Section-free standardization

On each orbit `O`, define the proposed standard topology without selecting a
basepoint: a subset `U subset X` is open precisely when each intersection
`U cap O` pulls back to an open subset of `R` along any orbit map
`t -> x.t`.  The global topology is the topological coproduct of the orbit
topologies.

Proof obligations include:

1. basepoint independence for every orbit;
2. joint continuity of the right `R`-action;
3. Hausdorffness and openness of orbit components;
4. uniqueness among Hausdorff compatible topologies with jointly continuous
   action and open orbits;
5. an exact equivalence with nonempty topological coproducts of standard
   torsors `R/H_q`, allowing repeated and unequal lattices; and
6. global indiscretization as the correctly typed inverse on the actual
   source category.

This construction is explicit standardization.  It is not inherited actual
topology and not a separated reflection.

## 4. Isomorphism classification

If a globally `c`-scaled isomorphism sends orbit `q` to `sigma(q)`, the
required stabilizer equation is

```text
H_{sigma(q)} = c H_q,
equivalently L_{sigma(q)}=c L_q.
```

The protocol requires both directions, the exact composition/inverse laws,
and the translation freedom within each target torsor.  Any semidirect or
wreath splitting that chooses orbit origins is noncanonical and must be
identified as such.  The canonical statement is an extension by the full
product of component rotations over the permutation group preserving the
appropriate length relation.

## 5. Prime-clock owner and rigidity theorem

The fixed application does **not** collapse a prime packet to one orbit.
Let `Q_Per=Per_Ef/R` be the bare set of all actual periodic orbits and use
the disjoint length-fibre partition

```text
Q_Per = disjoint_union_{p in P} Q_p,
L_q=log(p) and H_q=(log p)Z for q in Q_p.
```

Every `Q_p` is nonempty; its known cardinality is companion-owned and is not
needed for the rigidity argument.  A globally scaled isomorphism permutes
all individual orbits.  Because every source orbit in one `Q_p` has the same
length and multiplication by `c>0` is injective on positive lengths, it must
send the entire fibre `Q_p` bijectively onto a unique fibre `Q_{sigma(p)}`.
Thus it induces, rather than assumes, a permutation of prime length classes.

The proposed central theorem is:

```text
If c>0 and the induced sigma:P->P is a bijection satisfying
log(sigma(p)) = c log(p) for every prime p,
then c=1 and sigma is the identity.
```

The proof may use the prime number theorem only through an exact audited
statement.  The permitted counting reduction is

```text
pi(y)=pi(y^(1/c))
```

for all sufficiently relevant `y`, followed by a rigorous asymptotic
contradiction for `c!=1`.  If a shorter elementary proof is used, all
number-theoretic hypotheses must still be explicit.

This application is a theorem about the mixed standardized marked owner.  It
does not change the actual topology, select primes from a generic clock
family, or define a trace/operator/determinant.

## 6. Candidate claim ledger

| ID | Candidate claim | Phase-1 status |
|---|---|---|
| P15-1 | Section-free mixed-lattice standard topology and uniqueness. | SPECIFIED / UNPROVED |
| P15-2 | Equivalence with nonempty coproducts of standard torsors with varying lattices. | SPECIFIED / UNPROVED |
| P15-3 | Strict automorphism extension and choice boundary. | SPECIFIED / UNPROVED |
| P15-4 | Classification of globally scaled isomorphisms by `L_{sigma(q)}=cL_q`. | SPECIFIED / UNPROVED |
| P15-5 | Prime-clock global scaling rigidity. | CENTRAL / UNPROVED |
| P15-6 | Explicit generic/composite/geometric-clock controls and counterexamples. | DESIGN UNAUTHORIZED |

## 7. Nonredundancy and stop rules

- If P15-1--P15-4 reduce to Paper 12 plus standard component bookkeeping and
  P15-5 is absent, the disposition is `NOTE_OR_MERGE`.
- The project cannot claim that an individual `log(p)` is newly recovered;
  Paper 12 already owns the marked stabilizer.  The candidate delta is
  rigidity of the entire unlabeled prime-clock family under one common
  global scale.
- A permutation with orbit-dependent scales is outside the central theorem
  and must be an explicit countercontrol.
- Mixed stabilizers alone do not authorize higher cohomology, an Arveson
  invariant, or Paper-16 credit.

Standalone eligibility requires P15-1--P15-5, an exact nearest-precedent
audit, and an independent finding that the PNT rigidity conjunction is not a
routine restatement of Papers 12--13.

## 8. Phase gates

Independent methodology/nonredundancy, mathematical devil/domain, and
primary-source reviews must all pass before proof implementation.  PNT
source bytes or an authoritative official manifestation must be frozen
before the final proof gate.  Controls, Route, manuscript, and release have
separate later gates.  Route B and Git/public synchronization remain false.
