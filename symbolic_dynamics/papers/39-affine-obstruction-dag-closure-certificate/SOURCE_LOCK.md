# Paper 39 source lock — SD-C41

## Identity

- Working title: **Relative Exhaustion of an Affine Symbolic Branch: A Typed
  Obstruction DAG and Registry Handoff**.
- Intended authority path: `39-affine-obstruction-dag-closure-certificate`.
- Candidate ID: `SD-C41`.
- Family: Symbolic Dynamics.
- Object type: closure/audit meta-object; **not** a new dynamical mechanism.
- Route framework: strict Route A v0.2; Route B locked.
- Freeze date: 2026-08-16.

This working source lock lives only in `/tmp`. It does not edit, pre-empt, or
seal any authority-repository artifact.

## 1. Exact question

Let the Paper-39 affine candidate domain be exactly the retrospective finite
typed encoding assembled from the hashed Papers 35--38 artifacts after their
outcomes were known and frozen before the Paper-39 checker. Do the four sealed
affine papers cover every repair tag admitted by that encoding, so that no
further affine successor is permitted without leaving it? If so, does the
frozen global
Symbolic Dynamics registry contain a non-affine candidate whose definition
was independently source-locked before evaluation?

The target is a **theorem relative to frozen data and a frozen repair
alphabet**. It is not a theorem that every conceivable affine, symbolic,
operator-algebraic, or geometric construction is impossible.

## 2. Frozen source corpus

The mathematical authority inputs are the final `SOURCE_LOCK.md`,
`PROOF_PACKAGE.md`, `DERIVATION_PACKAGE.md`, `ROUND2_CLUES.md`, and strict
Route-A card for each of Papers 35--38. The relevant SHA-256 values are:

| Paper | Source lock | Proof package | Derivation package | Round-2 clues | Route card |
|---|---|---|---|---|---|
| 35 / `SD-C37` | `c0c05c9b2044fcccbca3abe9fc448f1372c8ba9a73565fae8d563229cf0f65d5` | `d5c11c0edbbaf0b09eb6314ba252783b1725d41f38d34f4df1ebc9a4db72b5c6` | `fdc5bc43c111f51fba11410ad2d2727cbc0e3580443b08a2ab18556041f4067f` | `ededcb2c27db698f5b935260261d0611710f068cbb87d3730f89e0fa915dd0b1` | `8d4447c276a38348bbe57a4892b4006e27beb45bf63e1f68a18f61d0690ac2f2` |
| 36 / `SD-C38` | `0743f1f118b71436ee773a353116b8ac420e3aa3ffa46cf13ed1d1129835ccb5` | `b9d3cf29f86f6d4a2899f18e4b15891ba6a7ffd8ab88351cc57147ac1e820267` | `c748d3d2f1ed01e2bb7525847aba344abe7e1d0ed5a10d7c199af765206da2cd` | `3248dade75b48b633f9d7531b3dd7bca10729c91bee1bfc846b594ea6f1bd977` | `ef12a609c68a0e610493baabf6fbb68e1a4907d8ac7becb4a3912da9ddfe7f61` |
| 37 / `SD-C39` | `d725f03caffc6c5fab916314df25097b7383af7494287052496516deab0dcb4e` | `6b292c2292b7f44273c4b99103797395db4b7ff76d69ec6252f09a590294db5e` | `1fc0c70d07e4fe881fc8ded0e71f033602e8c5fd29fb9708958ce234998a58b5` | `e703b5b660024edb243ba3ba587c3cb0a668d298e7edce8198a22d186629c2ab` | `d63a26da338b471a57c86039cc3fbaf788ae02b15848eb3fb3ff3662e05f930a` |
| 38 / `SD-C40` | `febaeb0b1db1a0713bbb68cf99110d7ecf2df8b39caf3ee9f311598f45fa6a7a` | `fdb49515d5baafc2baa00e5e3d510d940c6af813f8a32ce56e3116171f7b6d73` | `18c07306c64297338d6b85b4f830ce0ccd15317ec0ee22f0e57823064171307a` | `db192ac628caa13ca781d7878a423adf7958cbcb7dc11ef610ed85fb78de4d50` | `8cfd24e900da820827a44ab00e436cd0e1a04c6e04dd7b1b837bb58b7881b7be` |

The independent evaluation hashes additionally used are
`c45b419d445d365eb2d13ee4e471dd40bf8407540cfbd466be2d3a47d39b66cd`
for Paper 37 and
`984187abd5fced5e42c334763127ced28329fc4d9fbefe4d06b31427f509a434`
for Paper 38.

The registry-handoff sources are:

- Session-4 preregistration and source lock:
  `681757d86d882384eb5bdbdddba11e04aeb69228bae98707b404535b753e3d25`;
- Session-4 candidate registry:
  `0e29fcfd37c3f048573ff3d705961de65ceb57a7421d5272ccaa586367a5d86c`;
- global Symbolic Dynamics README snapshot:
  `5f11a14308836a9e5b92d4996beff483ef077a3ead5a55e52b8bf111c5ed7a24`.

The pre-existing Route-A criterion source is
`symbolic_dynamics/skills/route-a-evaluator.md`, SHA-256
`29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a`.
In particular, the Paper-38 source lock and Round-2 clue hashes are
`febaeb0b1db1a0713bbb68cf99110d7ecf2df8b39caf3ee9f311598f45fa6a7a`
and `db192ac628caa13ca781d7878a423adf7958cbcb7dc11ef610ed85fb78de4d50`.

No claim in Paper 39 may be stronger than the conjunction of these frozen
inputs.

### Freeze-timing boundary

Paper 39 is a **retrospective closure encoding**: the outcomes of Papers
35--38 were already known when this 14-class/16-token/17-transition encoding
was assembled. The Paper-38 source lock and Round-2 clues had already frozen
the instruction to close this branch and return to the registry, and the
Route-A criterion predates the Paper-39 checker. This package freezes the
Paper-39 encoding before its own checker/evaluation run. It does **not** claim
that the Paper-39 repair universe or the `Good` conjunction was preregistered
before every Paper-35--38 failure.

## 3. Invariant object

The invariant object is the typed obstruction history

$$
\mathcal H_{35:38}
=\bigl(\mathcal V,\mathcal E,\operatorname{type},\operatorname{owner},
\operatorname{obstruction},\operatorname{status}\bigr),
$$

not any Cayley graph, local system, tree, transfer operator, or Euler product.
An ownership label is part of the type. In particular, an operator or
determinant owned at one node is not transported across an object-changing
edge unless a frozen source explicitly proves that transport.

## 4. Success predicate

For a typed candidate state $c$, define

$$
\operatorname{Good}(c)
=\operatorname{Intrinsic}(c)\wedge\operatorname{Rec}(c)
\wedge\operatorname{Selective}(c)\wedge\operatorname{OwnedDet}(c)
\wedge\operatorname{MarkerOK}(c)\wedge\operatorname{Controls}(c).
$$

Here:

- `Intrinsic` means no prime table, accepted-support table, target zero,
  terminal projector, or post-result parameter choice enters the source;
- `Rec` means a nonempty primitive ledger with repetition compatibility;
- `Selective` means a source-proved arithmetic sector that fails matched
  generic controls;
- `OwnedDet` means one declared operator on the same declared state space owns
  the claimed determinant in the declared determinant category;
- `MarkerOK` means the free marker counts the frozen primitive step and is not
  replaced by a specialization, first return, quotient clock, or fugacity;
- `Controls` means all frozen balanced, composite, mutation, generic, and
  `PROVES_TOO_MUCH` controls are survived.

No coordinate may be borrowed from a different node.

### Pre-existing criterion-field map

The six `Good` conjuncts are a typed consolidation of pre-existing Route and
source-lock fields, not new success criteria invented by the Paper-39
checker.

| `Good` conjunct | Pre-existing Route/source field(s) | Frozen interpretation used here |
|---|---|---|
| $I$ / `Intrinsic` | Route A0 `arithmetic_origin`; source-lock `allowed_data`, `forbidden_data`, parameter provenance | Source-derived object with no prime/support/target oracle or post-result parameter choice. |
| $R$ / `Rec` | Route A1 primitive-ledger and repetition requirements; source-lock `object`, `dynamics`, `clock` | Nonempty primitive family with compatible powers/repetitions on the declared object. |
| $S$ / `Selective` | Route A0/A1 arithmetic-sector requirement; adversarial generic/composite controls | A retained source-proved arithmetic sector that fails matched generic controls. |
| $D$ / `OwnedDet` | Route A2; source-lock `operator_object`, `determinant_convention`, `regularization_order` | One declared operator on the same declared space owns the determinant in its declared category. |
| $M$ / `MarkerOK` | Source-lock `clock`, `main_theorem_marker`, `normalization` | One free marker counts the frozen step and is not replaced by a quotient clock, first return, or fugacity. |
| $C$ / `Controls` | Route `adversarial_controls`, `proves_too_much_risk`, blocking conditions and stop rule | Balanced, composite, mutation, generic, and `PROVES_TOO_MUCH` controls are survived. |

The detailed rowwise evidence remains owned by the hashed P35--P38 locks,
proofs, derivations, clues, and Route cards listed above.

## 5. Retrospective Paper-39 affine encoding

The Paper-38 Round-2 prohibition list is normalized to the following exact
fourteen-class repair alphabet:

$$
\begin{aligned}
\mathcal A_{14}=\{&\texttt{affine\_cayley\_representation},
\texttt{finite\_rank\_local\_system},\texttt{character},
\texttt{grading},\texttt{quotient},\texttt{induced\_shift},\\
&\texttt{first\_return\_map},\texttt{bass\_serre\_splitting},
\texttt{valuation\_tree},\texttt{boundary\_model},
\texttt{modular\_phase},\\
&\texttt{basepoint\_damping},
\texttt{finite\_total\_weight\_retrofit},
\texttt{groupoid\_trace}\}.
\end{aligned}
$$

The finite request universe is the following exact sixteen-token set
$\Sigma_{16}$:

```text
AFFINE_CAYLEY_FROZEN_FAMILY
FINITE_RANK_LOCAL_SYSTEM_FROZEN_FAMILY
CHARACTER_FROZEN_FAMILY
GRADING_FROZEN_FAMILY
QUOTIENT_FROZEN_FAMILY
MODULAR_PHASE_FROZEN_FAMILY
INDUCED_SHIFT_EXIT
FIRST_RETURN_MAP_EXIT
VALUATION_TREE_EXIT
BOUNDARY_MODEL_EXIT
BASEPOINT_DAMPING_EXIT
FINITE_TOTAL_WEIGHT_RETROFIT_EXIT
FROZEN_ASCENDING_HNN_BASS_SERRE_SPLITTING
ALTERNATIVE_BASS_SERRE_SPLITTING_EXIT
FROZEN_TREE_LATTICE_GROUPOID_IMPORT
ALTERNATIVE_GROUPOID_CATEGORY_EXIT
```

There are six theorem-covered frozen family tokens, six explicit exit-only
tokens, and two tested/exit token pairs for the two mixed classes. No
`OTHER_INSTANCE` token exists, and $\Sigma_{16}$ is not closed under arbitrary
composition.

The expanded DAG refines the tested endpoint families into seventeen internal
transition tags: full and sliced positive sources, formal symmetrization,
Hashimoto reduction, quotient, diagonal Gibbs, prime Fock, complete filling,
scalar superlift, ordinary and graded coefficient forks, normal-closure
saturation, the full tree canonical for the frozen ascending-HNN
splitting/presentation, canonical modular weight, tree-lattice boundary,
orbital boundary, and marker comparison. These internal tags are proof
refinements, not extra top-level repair classes.

Let $\mathcal P_{\rm fr}$ be the nonempty typed audit-provenance paths from
the root through those internal edges. For a path $p$ ending at $v$, the
candidate datum belongs only to the source-frozen endpoint family $X_v(r)$;
earlier nodes record provenance and obligations. The theorem domain is

$$
\mathfrak C_{\rm aff}(r)
=\coprod_{p\in\mathcal P_{\rm fr}}\{p\}\times X_{\operatorname{end}(p)}(r).
$$

An edge with a reset is historical succession to a separately typed object,
not cumulative composition of the two endpoint mechanisms.

This rule survives coarse projection. Expanded `E07` projects to
structural-spine `E36_37`, but the projection carries only inherited
obligations and historical provenance. Its object, marker, operator owner, and
determinant owner all remain `RESET` under the independently frozen Paper-37
source lock. The target edge marker is redeclared; it is not transported from
the Paper-36 filled/control object. No `CARRY_WITH_EQUIVALENCE` interpretation
is permitted without a separately hashed transport theorem, and none exists.

The class-coverage statuses are:

- tested representative with a proved obstruction:
  `affine_cayley_representation`, `finite_rank_local_system`, `character`,
  `grading`, `quotient`, and the canonical `modular_phase`;
- tested canonical representative plus forbidden alternative instances:
  `bass_serre_splitting` and `groupoid_trace`/tree-lattice-category import;
- explicit object/marker/operator contract exits:
  `induced_shift`, `first_return_map`, `valuation_tree`, `boundary_model`,
  `basepoint_damping`, and `finite_total_weight_retrofit`.

KMS/GNS/Fock/prime-basis/support projectors, arbitrary infinite-dimensional
completions, target data, changed markers, regularized determinant relabelling,
and Route B are named among the explicit prohibition/exit records or are
globally forbidden data. They are not additional theorem-proved no-go classes,
and no catch-all normalization of future constructions is asserted.

One expanded edge has a different status. `E22` retains the Paper-37
post-result instruction not to retry “another” matrix, character, fiber rank,
nilpotent automaton, auxiliary representation, or arbitrary completion. It is
an **auxiliary non-domain firewall**, not an element of the exact
$\mathcal A_{14}$ repair-tag set and not an instance in $\Sigma_{16}$. Its
English nouns do not create alternative instances of the six pure-obstruction
classes. Accordingly, `E22` has no request token, no $\Gamma$ class-coverage
role, and no failed-`Good` role. It is retained only as hashed Paper-37
historical boundary evidence and points to `NX` as a nonmembership sink.
Its separate canonical history path is `H_NX_E22`, with canonical-string
SHA-256
`1231fe11f42c13ec3a7925d68d89f066b1deb2460f57924ecb76dd3d3490850a`;
it is not in the request-classification path map.

Thus “exhaustive” has three finite, coordinated meanings: all fourteen class
labels have dispositions; all sixteen frozen instance tokens have an explicit
tested-or-exit classification; and every endpoint state in
$\mathfrak C_{\mathrm{aff}}$ has a proved obstruction. It does not quantify
over an unnamed universe of affine ideas, unlisted instances, or arbitrary
compound repairs. Coordinatewise assembly requires a new source lock; Paper
39 neither admits nor refutes it.

## 6. Typed node and edge schema

Every node record must contain

$$
(\mathrm{id},\mathrm{kind},\mathrm{obligation},\mathrm{source\ object},
\mathrm{marker},\mathrm{operator\ owner},\mathrm{determinant\ owner},
\mathrm{obstruction},\mathrm{control},\mathrm{forbidden\ escape},
\mathrm{terminal\ code}).
$$

Every edge record must contain

$$
(\mathrm{id},\mathrm{tail},\mathrm{head},\mathrm{repair\ tag},
\mathrm{inherited\ obligation},\mathrm{tail\ source\ object},
\mathrm{target\ object/marker\ carry\ or\ reset},
\mathrm{operator/determinant\ ownership\ rule},\mathrm{exact\ obstruction},
\mathrm{coverage\ witness},\mathrm{forbidden\ escape},
\mathrm{terminal\ code}).
$$

In the compact edge ledger, `tail` is a foreign key to the tail node's
literal `source object` field; the adjacent transfer field records the target
object and marker carry/reset rule. Thus the source object is neither inferred
from prose nor silently transported.

The complete ledgers are frozen in `paper39_DERIVATION_PACKAGE.md`.
The terms **structural spine** (6 nodes/5 edges) and **expanded proof DAG**
(22 nodes/28 edges) are not interchangeable. The latter partitions into 17
internal transitions, 5 closure edges, 3 token-associated contract exits, 1
auxiliary non-domain firewall (`E22`), and 2 governance guards. Their complete
per-ID projection and fourteen-class coverage bridge, including all sixteen
stable instance tokens, is frozen in `paper39_DAG_BRIDGE.json`.
The bridge's `projection_transfer_constraints.E36_37` record makes the `E07`
reset rule machine-checkable at structural-spine granularity.

## 7. Frozen theorem target

### Relative affine-branch closure theorem

For every integer $r\ge2$ and every candidate state
$c\in\mathfrak C_{\mathrm{aff}}(r)$,

$$
\neg\operatorname{Good}(c).
$$

For this statement, $\operatorname{end}(c)$ is the endpoint node of the
nonempty audit-provenance path carried by $c$,
$\mathcal V_{\rm obs}$ is the image of the seventeen internal head map, and
$F(v)$ is the nonempty set of failed `Good` coordinates recorded at endpoint
$v$. The proof establishes endpoint-obstruction totality

$$
\operatorname{end}(c)\in\mathcal V_{\rm obs},\qquad
F(\operatorname{end}(c))\ne\varnothing,
$$

and then proves the corresponding disjunction of failed conjuncts. This is not
advertised as graph termination: outgoing edges may be historical resets to
new endpoint objects.

The balanced case $r=1$ is a boundary control: it removes the unequal-length
marker obstruction in Paper 36 and makes the Paper-38 action image discrete,
but it does not produce a retained recurrent quotient, a proper
finite-stabilizer action, or a locally finite orbital ledger.

The theorem is proved by a total tag-to-node coverage map on the frozen
contract. It is **not** proved by extrapolating finite experiments and is
**not** a universal impossibility theorem.

## 8. Registry predicate and realized decision

For the frozen repository snapshot, `HistoricallyLockedNonAffine(c)` means:

1. $c$ occurs in the global Symbolic Dynamics candidate registry;
2. a candidate-specific object, clock/determinant convention, tests, and stop
   rule were frozen before that candidate's numerical result was inspected;
3. $c\notin\mathfrak C_{\mathrm{aff}}$.

The Session-4 preregistration and source lock supplies six witnesses:
`SD-C01`, `SD-C02`, `SD-C03`, `SD-C04`, `SD-C05`, and `SD-C06`. Therefore

$$
\{c:\operatorname{HistoricallyLockedNonAffine}(c)\}\ne\varnothing.
$$

The realized terminal code is consequently

```text
RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY
```

This is a governance handoff only. It does not select, rank, revive, combine,
or re-evaluate any of the six candidates. Each already has a Route-A record.

The conditional fallback is frozen as

```text
if the historically source-locked non-affine registry witness set were empty:
    STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR
```

That antecedent is false in the observed snapshot.

## 9. Strict Route-A lock

Paper 39 contributes no new arithmetic source, recurrent ledger, determinant,
global analytic structure, or lift. It may not inherit the affine papers'
structural $A0$ coordinate. Its strict tuple is

```text
(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
branch: CLOSE_ENTIRE_AFFINE_BRANCH
realized_terminal: RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY
conditional_empty_registry_terminal: STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR
```

The closure theorem is a valid mathematical output; it is not Route-A
mechanism credit.

## 10. Mandatory adversarial checks

The proof package must retain the following sharp boundaries.

1. A finite directed cycle has a nonempty primitive ledger and a
   finite-dimensional Fredholm determinant, refuting any universal symbolic
   no-cycle/non-Fredholm claim.
2. A noninvertible nilpotent matrix deletes an ordinary determinant factor,
   showing why Paper 37 quantifies over invertible parallel transport.
3. Root-dependent summable damping can change compactness on an infinite tree,
   showing why Paper 38 quantifies only over the canonical modular cocycle.
4. A proper discrete tree action with finite stabilizers may admit a
   tree-lattice determinant, showing why the frozen $BS(1,r)$ action
   hypotheses matter.
5. At $r=1$, unit marker descent and a discrete action image do not repair
   recurrence, properness, or local finiteness.
6. Historical registry nonemptiness is not the same predicate as the
   existence of an unevaluated live successor.

## 11. ARS Phase-1 methodology blueprint

1. **Theorem-relative paradigm.** State the conclusion as
   $\forall r\ge2\;\forall c\in\mathfrak C_{\mathrm{aff}}(r)$, not as a
   universal no-go.
2. **Retrospective encoding as data.** Assemble the Paper-39 domain from the
   hashed predecessor sources, proofs, derivations, clue ledgers, Route cards,
   and registry locks, then freeze it before the Paper-39 checker.
3. **Typed graph construction.** Make object, marker, operator, determinant
   category, and ownership fields part of each vertex and edge type.
4. **Coverage criterion.** Provide a total class relation from each of the
   fourteen frozen repair classes to one or more tested obstruction nodes,
   explicit contract exits, or both for mixed canonical/alternative classes;
   enumerate the exact sixteen instance tokens; and separately require a
   single typed head for each of the seventeen internal transition tags.
   Auxiliary historical-firewall edges such as `E22` must have empty
   class/token fibers and cannot earn coverage credit.
5. **Countermodel validity.** Test the theorem against out-of-contract models
   that defeat overbroad conclusions and against in-contract matched generic
   controls that expose `PROVES_TOO_MUCH` mechanisms.
6. **Retrospective freeze and stop rule.** Acknowledge that predecessor
   outcomes were known, then freeze the Paper-39 graph, sixteen tokens, Route
   tuple, handoff predicate, and empty-registry fallback before the Paper-39
   checker run; no post-checker repair search is permitted.
7. **Explicit limitation.** The result closes one named affine branch under
   one named contract. It neither classifies all affine mathematics nor
   supplies a new non-affine candidate.

## 12. Paper 40 boundary

Paper 39 does not authorize Paper 40. Root/registry governance alone may
independently source-lock a Paper-40 candidate after Paper 39 is sealed. Such
a lock must precede evaluation and must freeze, at minimum:

- a non-affine source object and phase space;
- intrinsic arithmetic origin;
- primitive and repetition semantics;
- one free marker and its relation to the dynamical step;
- operator, function space, determinant category, and ownership proof target;
- parameter provenance, generic controls, forbidden data, and stop rule;
- a proof that no coordinate is imported from a closed affine node or from a
  different historical registry candidate.

The undefined phrase “unspent successor” is not silently added to Paper 38's
historical-existence predicate. If future governance wants that stronger
predicate, it must be defined and source-locked prospectively.
