# Paper 14 Phase-2 global-topology symbolic proof ledger

Status: **COMPLETE — AUTHORIZED SYMBOLIC PROOF ONLY**  
Version: `P14-P2-PROOF-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Proof verdict: **PASS WITH A TYPED G3 INFINITE-COINFINITE SOURCE STOP — C0/M0/m0**  
Standalone disposition: **HOLD pending independent mathematical and
nonredundancy review**  
Controls, Route A/B, manuscript, release, Git, and public synchronization:
**not authorized / false**

## 1. Exact authorization and evidence binding

The only write authorized by the Phase-1 gate is this ledger.  Immediately
before proof work, the gate and every input that it binds were independently
rehashed:

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/phase1_final_gate.md` | `fb645cfbb21e299d78f698699ccb2abe1c5b68b4c64e7c3efc32521fe7dc297c` | exact match |
| `notes/papers14_18_batch_design_lock.md` | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | exact match |
| `notes/research_protocol.md` | `a3ee049f27d29bb276553edcee8fbb019125b96c3e90b82f800a9706a106d7ab` | exact match |
| `notes/candidate_lock.md` | `8cbbd9e63f53c8f821f940405c6f5a41f34a5242ab9ea24be1fb87b47ae9b096` | exact match |
| `notes/phase1_amendment_v1.md` | `931d0c83528d1e05b467cf8f378b8798d2e14170c9505bcaeb5566de0a8cae16` | exact match |
| `notes/phase1_source_topology_precheck.md` | `05fb9f622c348839514d4d69760e491e7d2afdf4eb9f14687d5e0ce05d1229cb` | exact match |
| `notes/phase1_methodology_review.md` | `581e2ad01156d80f6b91febaa431d81352c47431de8a0fd865d9c71993861bf4` | exact match |
| `notes/phase1_devils_source_review.md` | `5f2e85b211b159b0333cf28ce64c83cb76eb9abb4ac7f8f00cfcacf258462b86` | exact match |

The relevant proved-owner and primary-source bytes were also rehashed:

| Artifact | SHA-256 | Use and ceiling |
|---|---|---|
| Paper-9 manuscript | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | actual fixed-prime owner and inherited indiscreteness only |
| Paper-9 proof audit | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | open suspension quotient, saturated restriction, and fixed-packet proof |
| Paper-10 manuscript | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` | generic tagged-coproduct consequences only |
| Paper-10 proof audit | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | abstract coproduct and direct `T0` universal property |
| retained Deninger arXiv-v4 PDF | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | primary definitions, topology, packets, and collective periodic closure |
| local Deninger source audit | `a4785e0fd56cb4e24211ea4d8f0e78a83ccdd6c942dc6572c87b2c1230ae521a` | locator and owner cross-check; not an external authority |

The retained PDF has 119 reader pages, is unencrypted, and its text layer was
read at the load-bearing physical pages 27, 31--39, 40--52.  The source chain
used below is Definition 4.1 and Proposition 4.2; Theorems 5.2 and 6.1;
Lemma 7.1, Proposition 7.4, Theorem 7.10 and its warning; and Claim 8.1,
Theorem 8.2, and Lemma 8.3.  No coordinate bijection in equations (37)--(39)
is treated as a homeomorphism.

## 2. Owner notation and closure conventions

Fix the source-permitted finite-kernel class `E_f` and put

```text
check_X = check_X_0(C)_{E_f},
Y       = check_X x R_{>0},
(P,u)q  = (F_q P,q^{-1}u),
rho     : Y -> X_susp=Y/Q_{>0}.
```

For a rational prime `p`, let

```text
C_p      = C_p^{E_f} subset check_X,
Z_p      = C_p x R_{>0},
Gamma_p  = rho(Z_p).
```

Let `P` denote the set of rational primes.  For every `S subset P`, set

```text
C_S = union_{p in S} C_p,
U_S = union_{p in S} Gamma_p,
Per = U_P.
```

All these subsets carry the actual source-inherited topology.  A coproduct
appears only as the domain of the canonical comparison map in G1.

We fix the specialization convention explicitly:

```text
x <=_sp y  iff  x belongs to closure({y}).
```

All closure arguments use neighborhoods or nets.  In an arbitrary topological
space, `x in closure(A)` if and only if there is a net in `A` converging to
`x`: direct the neighborhoods of `x` by reverse inclusion and choose one
point from each nonempty intersection.  No first-countability assumption is
used below.

## 3. Two general quotient and product lemmas

### Lemma 3.1 — open-quotient closure identity

If `q:E->B` is an open continuous surjection, then for every `A subset B`,

```text
q^{-1}(closure_B(A)) = closure_E(q^{-1}(A)).                 (3.1)
```

**Proof.**  Continuity gives the right-to-left inclusion.  Conversely, if
`e` is outside the right side, an open neighborhood `V` of `e` misses
`q^{-1}(A)`.  Because `q` is open, `q(V)` is an open neighborhood of `q(e)`.
It misses `A`: if `a=q(v)` were in `A`, then `v` would belong to
`q^{-1}(A)`, contrary to the choice of `V`.  Thus `q(e)` is outside
`closure(A)`.  This proves (3.1).  The argument is neighborhood-valid in
every space.  QED.

Paper 9 proves that `rho` is open: the saturation of an open `V subset Y` is
the union of the homeomorphic translates `Vq`.  The same argument applies to
the Galois orbit maps because the compact Galois group acts by
homeomorphisms.

### Lemma 3.2 — exact pre-suspension reduction

For every `S subset P`,

```text
rho^{-1}(closure_X_susp(U_S))
   = closure_Y(C_S x R_{>0})
   = closure_check_X(C_S) x R_{>0}.                          (3.2)
```

Consequently,

```text
closure_X_susp(U_S)
   = rho(closure_check_X(C_S) x R_{>0}).                     (3.3)
```

**Proof.**  The set `C_S` is `Q_{>0}`-invariant, so
`rho^{-1}(U_S)=C_S x R_{>0}`.  Lemma 3.1 gives the first equality.  For any
spaces `A,B`, subset `D subset A`, and `B` as the whole second factor,
`closure_{A x B}(D x B)=closure_A(D) x B`: one inclusion follows from the
continuous first projection, and the other from the product-neighborhood
criterion.  This gives the second equality.  Applying the surjection `rho`
to (3.2) gives (3.3).  QED.

Equations (3.2)--(3.3) are the exact owner-preserving ambient-closure
reduction used in G3.  They do not identify the remaining pre-suspension
closure by fiat.

## 4. `P14-0`: descended base map and full fibres

### Theorem 4.1 — source descent and full-fibre identity

There is a unique continuous map

```text
pi : X_susp -> Spec Z,
pi([P,u]) = pr(P),                                           (4.1)
```

and, for every rational prime `p`,

```text
Gamma_p = pi^{-1}((p)).                                     (4.2)
```

In particular, every `Gamma_p` is closed in `X_susp`, and distinct packets
are disjoint.

**Proof.**  Deninger's Proposition 4.2 makes `E_f` invariant under the
permitted power maps and gives

```text
pr : check_X -> Spec Z
```

with the rational Frobenius action trivial on the base.  Section 7 gives
continuity first in the pointwise-convergence stage, then through the Galois
quotient and the Frobenius inductive limit.  Therefore
`(P,u) -> pr(P)` is continuous on `Y` and constant on every diagonal
`Q_{>0}` orbit.  The universal property of the quotient topology gives the
unique continuous map (4.1).

For a finite point `(p)`, Section 5 defines `C_p` as the full checked base
fibre, not as a selected orbit.  Theorem 5.2 says that the frozen `E_f`
subsystem retains this full fibre.  Hence

```text
pr^{-1}((p)) = C_p.
```

Taking the diagonal suspension of this invariant equality gives

```text
pi^{-1}((p))
 = (pr^{-1}((p)) x R_{>0})/Q_{>0}
 = (C_p x R_{>0})/Q_{>0}
 = Gamma_p.
```

The points `(p)` are pairwise distinct and closed in `Spec Z`, proving the
last assertions.  QED.

Disposition: `P14-0=PROVED` on the exact `Spec Z`, `E_f`, source-suspension
owner.

## 5. Finite packet theorem

### Theorem 5.1 — actual topology of every finite packet union

Let `F subset P` be nonempty and finite.  Then the actual subspace `U_F` is
homeomorphic under the canonical component map to

```text
coproduct_{p in F} Gamma_p.
```

Its open sets are exactly `U_S` for `S subset F`.  For every
`x in Gamma_p`,

```text
closure_X_susp({x}) = Gamma_p.                              (5.1)
```

Thus two points of `U_F` are topologically indistinguishable exactly when
they lie in the same packet, there is no cross-prime specialization, and the
Kolmogorov quotient of `U_F` is the discrete finite space `F`.

For two distinct primes `p,q`, the four opens are exactly

```text
empty, Gamma_p, Gamma_q, Gamma_p union Gamma_q.
```

**Proof.**  Theorem 4.1 makes every packet ambient closed.  In the finite
union `U_F`, the complement of `Gamma_p` is the finite union of the other
closed packets, so `Gamma_p` is relatively clopen.  Paper 9 proves that each
actual inherited `Gamma_p` is nonempty indiscrete.  Therefore an open subset
of `U_F` meets each component either in the empty set or in the whole
component; conversely every component union is open.  This is exactly the
finite coproduct topology.

For (5.1), ambient closedness gives
`closure_X_susp({x}) subset Gamma_p`.  Indiscreteness gives
`closure_Gamma_p({x})=Gamma_p`; the subspace closure identity puts the whole
packet in the ambient singleton closure.  Equality follows.  Formula (5.1),
not a sequence characterization, proves the specialization statements under
the convention fixed in Section 2.  QED.

This theorem is an actual-owner result, but its derivation is the direct
source-closed-fibre plus Paper-9 finite consequence identified by the
Phase-1 gate.  It carries no standalone credit by itself.

## 6. The all-prime source separation lemma

The finite theorem cannot distinguish discrete from cofinite index topology.
The following source evaluation does.

Let `dot_X(C)_{E_f}` denote Deninger's initial pre-Galois pointwise stage,
and let `dot_X_0(C)_{E_f}` be its Galois quotient.  The initial stage embeds
as an open subspace of the Frobenius colimit, every rational Frobenius map on
the colimit is a homeomorphism, and the Galois quotient is open.

### Lemma 6.1 — a source-open isolator for each prime packet

For every rational prime `p`, there is a `Q_{>0}`-invariant open subset
`W_p subset check_X` such that

```text
W_p intersection (union_{q in P} C_q) = C_p.                (6.1)
```

Consequently there is an ambient open subset `O_p subset X_susp` satisfying

```text
O_p intersection Per = Gamma_p.                            (6.2)
```

**Proof.**  At the pre-Galois pointwise stage, extend each multiplicative
character by zero as in Deninger's Section 7 and define

```text
V_p = {P in dot_X(C)_{E_f} : |P(p)| < 1/2}.                 (6.3)
```

Evaluation at the rational integer `p` is continuous in the exact product
topology, so `V_p` is open.  It is Galois invariant because every source
automorphism fixes the base integer `p`.  Its image `V_{p,0}` in the initial
Galois quotient is therefore open.

Now restrict (6.3) to a finite-field fibre.  On the fibre over `(p)`, the
integer `p` is zero, so `P(p)=0`.  On a fibre over `(q)` with `q!=p`, the
residue of `p` is a nonzero element of the torsion group
`overline(F_q)^times`.  Every character sends it to a root of unity, hence
`|P(p)|=1`.  Thus, among all finite-field fibres, (6.3) cuts out exactly the
`p`-fibre.  This is the required zero-versus-unit-modulus evaluation on the
source owner.

Regard `V_{p,0}` as an open subset of the colimit and set

```text
W_p = union_{r in Q_{>0}} F_r(V_{p,0}).                     (6.4)
```

Each `F_r` is a homeomorphism, so `W_p` is open; (6.4) is visibly
`Q_{>0}`-invariant.  Every point of `C_p` can be moved by some positive
integer Frobenius into the initial stage and then lies in `V_{p,0}`.  Hence
`C_p subset W_p`.  Conversely, Frobenius preserves the base point.  If a
point of a finite packet `C_q` lies in one translate in (6.4), moving it back
to the initial stage produces a point in `V_{p,0}` over `(q)`; the
zero/unit-modulus calculation forces `q=p`.  This proves (6.1) through the
raw, Galois, colimit, and rational-action levels without transporting a
coordinate topology.

The set `W_p x R_{>0}` is open and saturated for the diagonal rational
action.  Its image

```text
O_p = rho(W_p x R_{>0})
```

is open because `rho` is open.  Rational orbits preserve the base prime, so
(6.1) descends exactly to (6.2).  QED.

The sets `O_p` may contain generic, nonperiodic points.  Only their exact
intersection with `Per` is claimed; this distinction is essential in G3.

## 7. `P14-G1`: canonical all-prime comparison

### Theorem 7.1 — the actual periodic locus is the topological sum

The canonical continuous bijection

```text
J : coproduct_{p in P} Gamma_p -> Per
```

is open and hence is a homeomorphism.

**Proof.**  Lemma 6.1 shows that each `Gamma_p=O_p intersection Per` is open
in `Per`.  Paper 9 makes it indiscrete.  Hence an open subset of the
coproduct domain is a union of whole packet components.  Its image under `J`
is the same union of relatively open packets and is open in `Per`.  Thus `J`
is open.  It is continuous by the coproduct universal property and bijective
because the packets are disjoint and exhaust `Per`.  QED.

This conclusion was not inferred from finite restrictions.  The
infinity-sensitive input is the all-prime source-open family (6.2).  The
generic coproduct consequences after that owner comparison remain Paper-10
mathematics.

Disposition: `P14-G1=PROVED_HOMEOMORPHISM`.

## 8. `P14-G2`: every relative prime subfamily

### Theorem 8.1 — arbitrary-subfamily relative closure

For every `S subset P`,

```text
closure_Per(U_S) = U_S,                                    (8.1)
```

and `U_S` is open, closed, and clopen in `Per`.

**Proof.**  Lemma 6.1 makes every packet relatively open.  Therefore `U_S`,
an arbitrary union of packets, is open.  Its complement in `Per` is
`U_{P\S}`, another arbitrary union of relatively open packets.  Thus `U_S`
is also closed, proving (8.1).  QED.

The required branches are not merged:

| Branch for `S` | Relative closure | Open | Closed | Clopen |
|---|---|---|---|---|
| `S=empty` | `empty` | yes | yes | yes |
| finite nonempty | `U_S` | yes | yes | yes |
| cofinite proper | `U_S` | yes | yes | yes |
| infinite coinfinite | `U_S` | yes | yes | yes |
| `S=P` | `Per` | yes | yes | yes |

For later use, the subspace closure identity gives the exact firewall

```text
closure_X_susp(U_S) intersection Per = U_S.                (8.2)
```

Equation (8.2) does not say that `U_S` is ambient closed.

Disposition: `P14-G2=PROVED_FOR_ALL_SUBFAMILIES`.

## 9. `P14-G3`: ambient closure, exact branches, and sharp source stop

### 9.1 The source-owned unitary ceiling

Let

```text
check_Unit_{E_f}
  = check_X_0(S^1) intersection check_X_0(C)_{E_f},

Unit_{E_f}
  = rho(check_Unit_{E_f} x R_{>0}).                         (9.1)
```

The intersection is taken on the exact Galois-quotient Frobenius-colimit
owner.  Deninger's Theorem 8.2, specialized to `Spec Z`, states at the raw
level that the closure of all finite-field finite-kernel points is the
unitary locus.  The `Spec Z` case is unconditional in the source because the
number-ring instance of Claim 8.1 is known; the source records that the
eligible maximal ideals are infinite, indeed of positive Dirichlet density.

Intersecting the source equality with the `E_f` subspace and then applying
the open Galois and suspension quotient closure identities gives

```text
closure_X_susp(Per) = Unit_{E_f}.                           (9.2)
```

The set in (9.1) is closed: the unitary locus is closed in the pointwise
topology and remains closed through the colimit; its product preimage is
closed and saturated, and the quotient-topology criterion makes its image
closed.  Equation (9.2) is Deninger-owned source content, not a new Paper-14
collective-closure theorem.

### 9.2 Universal exact reduction and sharp bounds

For every `S subset P`, equations (3.2)--(3.3), (8.2), and (9.2) give

```text
U_S
  subset closure_X_susp(U_S)
  subset Unit_{E_f} \ U_{P\S},                              (9.3)

closure_X_susp(U_S) intersection Per = U_S.                (9.4)
```

The upper bound is sharp at the owner level: inclusion in `Unit_{E_f}`
follows because `U_S subset Per`, while every excluded packet has the
ambient open isolator `O_q` from Lemma 6.1 disjoint from `U_S`.

More exactly, the only possible new limit points in (9.3) lie over the
generic point `(0)` of `Spec Z`.  Every finite-base `E_f` point belongs to
its full `C_p` fibre by Theorem 5.2, so no other finite-base stratum remains.

### 9.3 Exact empty, finite, all-prime, and cofinite branches

The following branches are completely determined:

1. `S=empty`:

   ```text
   closure_X_susp(U_S)=empty.
   ```

2. `S` finite nonempty: Theorem 4.1 makes every `Gamma_p` closed, so a finite
   union is closed and

   ```text
   closure_X_susp(U_S)=U_S.                                (9.5)
   ```

3. `S=P`: equation (9.2) gives

   ```text
   closure_X_susp(U_P)=Unit_{E_f}.                         (9.6)
   ```

4. `S` cofinite: write `F=P\S`, with `F` finite.  Then

   ```text
   closure_X_susp(U_S)=Unit_{E_f} \ U_F.                   (9.7)
   ```

**Proof of (9.7).**  The upper inclusion is (9.3).  Points in packets indexed
by `S` are already in `U_S`.  It remains to consider a generic-base point of
`Unit_{E_f}`.  At an initial raw representative, a basic pointwise
neighborhood specifies finitely many character evaluations.  Deninger's
Lemma 8.3 constructs an approximating finite-field finite-kernel point by
choosing a maximal ideal from the eligible set in Claim 8.1.  In the
number-ring case used for `Spec Z`, that eligible set is infinite (indeed
positive-density).  Only finitely many maximal ideals of the finite number
field used by the finite constraints can lie over the finitely many rational
primes in `F`.  An eligible maximal ideal can therefore be chosen over a
prime in `S`.

Thus every basic neighborhood of the raw generic unitary representative
meets an `S`-packet.  Direct the basic neighborhoods by reverse inclusion and
choose one such point from each; this gives a net of `S`-packet points
converging to the representative.  The open Galois quotient, Frobenius
homeomorphisms, product with the unrestricted time factor, and the open
suspension quotient carry the closure statement to the exact owner.  Hence
every generic-base point in the right side of (9.7) belongs to the left
side.  QED.

The cofinite theorem is genuinely infinite and ambient: it is not visible in
any finite restriction, and it modifies the collective density proof while
preserving the finitely excluded packet isolators.

### 9.4 Exact incidence criterion for arbitrary `S`

For a generic unitary raw point `a` moved into an initial Frobenius stage,
let

```text
N(a;T,epsilon)
```

denote a basic pointwise neighborhood determined by a finite set `T` of
source-ring elements and positive tolerances.  Define the source-feasible
prime set

```text
Elig(a;T,epsilon)
 = {q in P : N(a;T,epsilon) contains an E_f finite-field
             point whose base point maps to (q) in Spec Z}.                (9.8)
```

This definition is independent of a chosen Galois lift up to the Galois
action, and moving between Frobenius stages transports the same criterion by
a homeomorphism while preserving the base prime.

By the neighborhood/net closure criterion and the two open-quotient closure
identities, a generic unitary suspended point `x` belongs to
`closure_X_susp(U_S)` if and only if, for one (equivalently every) raw lift
`a` after moving it into an initial stage,

```text
S intersection Elig(a;T,epsilon) is nonempty                (9.9)
```

for every basic finite-evaluation neighborhood.  Therefore (9.3) can be
sharpened to the exact formula

```text
closure_X_susp(U_S)
 = U_S union {generic x in Unit_{E_f} : x satisfies (9.9)}. (9.10)
```

Deninger's Claim 8.1 and Lemma 8.3 construct explicit infinite subsets of
`Elig(a;T,epsilon)` for generic `a`; this proves (9.7) because a cofinite `S`
meets them.  Their quantifiers do not say that an arbitrary prescribed
infinite coinfinite `S` meets every such set.

### 9.5 Infinite-coinfinite stop

For arbitrary infinite coinfinite `S`, the frozen source does not provide an
`S`-relative refinement of Claim 8.1/Lemma 8.3.  The exact missing datum is:

```text
for each generic unitary source point a and every finite-evaluation
neighborhood, whether the prescribed S meets the corresponding feasible
rational-prime set Elig(a;T,epsilon).                       (9.11)
```

Infinitude of `S` is insufficient: the eligible sets can encode order,
splitting, and congruence conditions and need not be cofinite.  Neither the
finite-packet theorem nor Deninger's unrestricted choice of a suitable prime
settles (9.11).  No additional topology, atlas, coordinate model, or
Chebotarev assumption is inserted here.

Accordingly:

```text
P14-G3(empty/finite)             = EXACT_CLOSED_U_S
P14-G3(cofinite)                 = EXACT_UNIT_MINUS_EXCLUDED_PACKETS
P14-G3(all primes)               = EXACT_Deninger_UNIT_OWNER
P14-G3(infinite coinfinite)      = EXACT_INCIDENCE_FORMULA_AND_BOUNDS
                                   + SOURCE_UNDERDETERMINED_FOR_CLASSIFICATION
MISSING_SOURCE_DATUM             = S-relative finite-approximation incidence
```

`SOURCE_UNDERDETERMINED_FOR_CLASSIFICATION` means that the frozen source does
not supply the arithmetic incidence theorem needed to simplify (9.10); it
does not mean that the already defined topology is non-unique.  This is a
theorem-level fail-close, not a search-negative novelty claim.

## 10. `P14-G4`: quotient topology and universal `T0` property

Define

```text
kappa : Per -> P,
kappa(x)=p iff x in Gamma_p.                                (10.1)
```

### Theorem 10.1 — discrete packet index and Kolmogorov universality

The quotient topology induced by `kappa` is the discrete topology on `P`.
Moreover `kappa` is the Kolmogorov-reflection unit: for every `T0` space `T`
and continuous map `f:Per->T`, there is a unique continuous
`f_bar:P_discrete->T` such that

```text
f = f_bar o kappa.                                          (10.2)
```

The topological-indistinguishability and mutual-specialization classes in
`Per` are exactly the packets `Gamma_p`.

**Proof.**  For every `S subset P`,

```text
kappa^{-1}(S)=U_S,
```

which is open by Theorem 8.1.  Hence every subset of the quotient is open
and the quotient topology is discrete.  Within one packet, Paper-9
indiscreteness makes all points indistinguishable.  Points in different
packets are separated by the relatively clopen packet of either point, so
the indistinguishability classes are exactly the packet fibres.

If `f:Per->T` is continuous and `T` is `T0`, its restriction to every
indiscrete `Gamma_p` is constant.  Define `f_bar(p)` to be that constant.
Then (10.2) holds and surjectivity of `kappa` forces uniqueness.  Every map
from the discrete space `P` is continuous, so `f_bar` is continuous.  This
proves the direct universal property after, rather than before, computing
the quotient topology.  QED.

The quotient is thus identified with `P_discrete`, not with the cofinite
closed-point subspace of `Spec Z`.  The continuity of
`pi|Per:Per->Spec Z` is compatible with this: it factors through the
continuous identity map from `P_discrete` to the cofinite prime subspace.

Disposition: `P14-G4=PROVED_DISCRETE_UNIVERSAL_T0`.

## 11. Completed claim-delta matrix

| Claim | Exact premise owner | P9 inherited part | P10 inherited generic part | Deninger/source part | New P14 step | Direct substitution? | Infinity-sensitive? | Ambient-owner content? | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| `P14-0` | source suspension | none | none | invariant base map; full finite-field fibres; suspension | prove continuous descent and exact suspended fibre identity | no as an owner proof, but elementary from source definitions | no | yes | **PROVED; no standalone weight alone** |
| finite `p,q` theorem | actual finite packet union | actual packet indiscreteness and singleton packet closure lower bound | finite coproduct consequences | closed, disjoint full fibres | actual finite-subspace comparison and closure formula | **yes**, after `P14-0` | no | yes, but finite | **PROVED; direct-chain/merge weight** |
| `P14-G1` | actual `Per` | fixed fibres indiscrete | topology of an abstract tagged sum after comparison | pointwise topology, open Galois/colimit/suspension maps | zero/unit evaluation; all-stage invariant open isolators; openness of `J` | owner arrow **no**; later coproduct consequences **yes** | yes | yes: ambient opens isolate relative packets | **PROVED; expressly insufficient alone for standalone** |
| `P14-G2` | relative `Per` | fixed fibres | component-union formula once G1 holds | global source neighborhoods from G1 | arbitrary-complement argument for every `S`, including infinite coinfinite | yes after G1/P10 | yes in quantifier, but formal after isolators | relative only | **PROVED; no independent standalone weight** |
| `P14-G3` | ambient `X_susp` | none | none | Theorem 8.2 collective unitary closure; Claim 8.1/Lemma 8.3 approximation | exact open-quotient reduction; packet-exclusion bound; cofinite-minus-finite ambient theorem; exact `S`-incidence criterion | cofinite theorem **no**; all-prime endpoint is source-owned | yes | yes | **FINITE/COFINITE/ALL EXACT; INFINITE-COINFINITE SOURCE STOP; standalone-eligible delta only pending review** |
| `P14-G4` | quotient of actual `Per` | within-packet collapse | generic direct `T0` factorization for a tagged coproduct | source packet index and disjointness | compute actual quotient topology after G1--G2 | yes after actual owner arrow | yes only through G1 | actual quotient owner, generic UMP | **PROVED; insufficient alone for standalone** |

No row is called new merely because Papers 9--10 did not print the same
sentence.  The only potential standalone-bearing result is the ambient
cofinite-subfamily theorem and the exact arbitrary-`S` incidence boundary;
their weight is not self-certified here.

## 12. Falsifier and regression ledger

| Attack | Result | Proof location |
|---|---|---|
| infer all-prime topology from finite restrictions | **REFUTED / NOT USED** | Lemma 6.1 supplies an actual all-prime evaluation family |
| import the topology of `U_p/H_p` or a standard circle | **REFUTED / NOT USED** | all opens are built before quotienting from source evaluations |
| confuse raw, Galois, colimit, and suspension points | **PASS** | Lemma 6.1 tracks the open through all four levels |
| use a sequence as a general closure criterion | **REFUTED / NOT USED** | Sections 2, 3, and 9 use neighborhoods/nets |
| promote relative closure to ambient closure | **REFUTED / NOT USED** | (8.2) is separated from (9.3)--(9.10) |
| identify discrete prime quotient with cofinite `Spec Z` subspace | **REFUTED** | Theorem 10.1 distinguishes the two topologies |
| cite Deninger 8.2 for arbitrary prescribed `S` | **REFUTED / FAIL-CLOSED** | Sections 9.4--9.5 expose the missing incidence quantifier |
| restate Deninger's all-periodic closure as new P14 work | **REFUTED** | (9.2) is explicitly source-owned |
| claim a search-negative theorem | **REFUTED / NOT USED** | no precedent-search verdict is issued here |

## 13. Severity and machine verdict

### Critical findings

None.

### Major findings

None.  The authorized package permits a sharp G3 bound and typed source stop
instead of an invented arbitrary-subfamily classification.

### Minor findings

None.  The specialization convention, all quotient directions, and every
relative/ambient owner are explicit.

### Machine-readable verdict

```text
P14_PHASE2_PROOF_LEDGER=COMPLETE
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
P14_0=PROVED
FINITE_PACKET_THEOREM=PROVED_FOR_EVERY_NONEMPTY_FINITE_SUBFAMILY
AMBIENT_SINGLETON_CLOSURE=PROVED_EQUALS_FIXED_PRIME_PACKET
P14_G1=PROVED_CANONICAL_MAP_OPEN_HOMEOMORPHISM
P14_G2=PROVED_ALL_SUBFAMILIES_RELATIVELY_CLOPEN
P14_G3_EMPTY_FINITE=PROVED_EXACT
P14_G3_COFINITE=PROVED_EXACT_UNIT_MINUS_EXCLUDED_PACKETS
P14_G3_ALL_PRIMES=PROVED_EXACT_SOURCE_UNITARY_OWNER
P14_G3_INFINITE_COINFINITE=EXACT_INCIDENCE_FORMULA_AND_SHARP_BOUNDS
P14_G3_INFINITE_COINFINITE_CLASSIFICATION=SOURCE_UNDERDETERMINED
P14_G3_MISSING_DATUM=S_RELATIVE_FINITE_APPROXIMATION_INCIDENCE
P14_G4=PROVED_DISCRETE_KOLMOGOROV_UNIVERSAL_PROPERTY
NET_OR_NEIGHBORHOOD_VALIDITY=PASS
FINITE_TO_INFINITE_INFERENCE_USED=false
RELATIVE_TO_AMBIENT_PROMOTION_USED=false
PROXY_TOPOLOGY_USED=false
STANDALONE_PASS=false
STANDALONE_REVIEW_REQUIRED=true
INDEPENDENT_MATHEMATICAL_REVIEW_REQUIRED=true
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

Final proof verdict: **PASS WITH A TYPED G3 INFINITE-COINFINITE SOURCE STOP —
C0/M0/m0.**  The proof closes `P14-0`, the finite theorem, G1, G2, and G4;
it closes G3 exactly for empty, finite, cofinite, and all-prime branches and
gives the exact incidence formula plus sharp owner bounds for arbitrary
infinite coinfinite subfamilies.  Independent mathematical and
standalone/nonredundancy reviews remain mandatory before any downstream gate.
