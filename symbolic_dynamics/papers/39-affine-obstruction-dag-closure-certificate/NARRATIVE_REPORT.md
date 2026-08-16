# Paper 39 narrative report — SD-C41

## Working title

**Relative Exhaustion of an Affine Symbolic Branch: A Typed Obstruction DAG
and Registry Handoff**

## One-sentence contribution

From a content-addressed retrospective encoding of the known Paper-35--38
affine repair history, Paper 39 gives a typed, machine-auditable proof that
each of the 16 encoded requests is either assigned a previously proved
obstruction or classified as an explicit category-changing exit.

## Research status in one paragraph

Paper 39 is a closure/audit meta-object, not a fifth affine construction.  Its
finite contract was assembled after the predecessor outcomes were known and
frozen before the Paper-39 checker.  The contract contains 14 repair classes,
16 stable request tokens, and 17 internal transition tags.  A 22-node/28-edge
expanded proof DAG retains the proof-level types; a 6-node/5-edge structural
spine supports execution and communication.  The paper proves relative
exhaustion only for this encoding.  It does not show that every conceivable
affine or symbolic mechanism fails, that the repair universe was prospectively
complete, or that a historical registry entry is an unevaluated successor.

## The story

### Act I — repeated negative results need typed memory

Papers 35--38 tested four different affine objects.  Their outcomes cannot be
combined coordinatewise: an arithmetic source at one node, a primitive ledger
at a second, a determinant at a third, and a marker at a fourth do not form a
candidate.  Object, marker, operator owner, and determinant owner must travel
together or reset under a separately proved transport theorem.  No such
transport theorem exists across the predecessor changes.

The methodological problem is therefore narrower than finding another
mechanism.  It is to decide whether the already authorized repair requests
have all been accounted for without silently conflating failures, exits, and
ownership categories.

### Act II — a finite typed graph turns history into a theorem domain

Paper 39 treats the hashed predecessor packages as data.  It normalizes the
literal Paper-38 prohibition list into 14 top-level classes and a finite
16-token request universe.  Every token carries its class, instance scope,
disposition, witness path, and endpoint.  Every graph node records the inherited
obligation, source object, marker, operator owner, determinant owner, exact
obstruction, forbidden escape, and terminal code.  Every edge records typed
field transfer or reset.

The expanded graph contains 22 nodes and 28 edges.  Its edge partition is
exact: 17 internal transitions, 5 closure edges, 3 token-associated exits, one
auxiliary non-domain firewall, and two governance guards.  The six-node spine
is not a smaller proof.  It is a many-to-one executable projection whose fibers
remain explicit in `DAG_BRIDGE.json`.

### Act III — endpoint classification closes only the encoded branch

For a candidate state `c`, Paper 39 retrospectively consolidates pre-existing
Route/source fields as

```text
Good(c) = Intrinsic(c) and Rec(c) and Selective(c)
          and OwnedDet(c) and MarkerOK(c) and Controls(c).
```

The closure theorem uses a total classification map, not a generic graph-
termination claim.  Each obstructed token ends at a specified endpoint with a
nonempty set of failed `Good` coordinates.  Each exit token ends at a typed
boundary with an empty failed-`Good` set.  EXIT is never counted as evidence
for `not Good`.

The resulting class census is `6 OBSTRUCTED / 6 EXIT_ONLY / 2 MIXED`; the
token census is `8 OBSTRUCTED / 8 EXIT`.  Hence every recorded request is
classified.  Every in-domain candidate endpoint fails `Good`, while an EXIT
token asserts only category-changing nonmembership and is not a candidate on
which `Good` is evaluated.  Since Paper 39 itself owns no arithmetic source,
primitive ledger, operator, determinant, or marker, its strict Route tuple is
all FAIL and Route B stays locked.  The realized governance action is to
return control to the pre-existing global registry without ranking or
selecting an entry.

## Claims–evidence matrix

| Claim | Evidence | Status | Manuscript location |
|---|---|---|---|
| C1. The Paper-39 theorem domain is finite, explicit, and retrospective. | `SOURCE_LOCK.md` §§2,5; `DAG_BRIDGE.json` token and class records; hash locks. | Proved for the encoded bytes. | Introduction; contract section. |
| C2. The expanded proof graph is a typed DAG with 22 nodes, 28 edges, and a strict rank. | `DERIVATION_PACKAGE.md` §§3--5; `DAG_BRIDGE.json` edge records and ranks. | Proved. | Typed-DAG section; Appendix A. |
| C3. Every one of the 16 tokens is assigned either obstruction evidence or a typed exit, with no catch-all token. | `PROOF_PACKAGE.md` Step 6; `QUANTIFIER_AUDIT.md` §§1--2; bridge token records. | Proved relative to `Sigma_16`. | Main theorem. |
| C4. Exit evidence is disjoint from failed-`Good` evidence; E22 earns zero closure credit. | Endpoint classification map; E22 empty fibers and historical path; DA concession. | Proved. | Main theorem; boundary section. |
| C5. The 6/5 spine and 22/28 proof DAG are linked by a total projection with auditable fibers. | `DAG_BRIDGE.json`; projection and rank checks. | Proved; projection is not injective. | Contract section; Figure 1. |
| C6. E36_37 resets four candidate-state fields under Paper 37; provenance is non-state metadata. | Expanded E07, bridge transfer constraint, Paper-37 hash, DA report. | Proved. | Ownership firewall; Figure 3. |
| C7. The executable audit reconstructs the finite classification and rejects adversarial mutations. | Integrator-owned authority FINAL result block. | **Verified: 535/535 main, 278/278 independent, and 29/29 mutations rejected by each evaluator.** | Audit section. |
| C8. The strict Route tuple is all FAIL, Route B is locked, and registry return performs no ranking. | `ROUTE_A_EVALUATION.yaml`; source/proof/quantifier packages. | Proved as protocol consequence. | Route and limitations section. |
| C9. The exact architecture has qualified integration novelty, not primitive-method novelty. | `LITERATURE_AUDIT.md`, especially ETP, Dardashti, Murali et al., and proof-DAG comparisons. | Qualified, moderate-confidence literature result. | Related work. |

## Mathematical backbone

### Typed history

The invariant is

```text
H_35:38 = (V, E, type, owner, obstruction, status),
```

not any predecessor phase space.  A node is admissible only when its object,
marker, operator owner, determinant owner, obstruction, and control fields are
read from one source-owned record.  An edge may carry an audit obligation, but
candidate identity changes require typed resets.

### Relative closure theorem

Let `normalize` be the finite table encoded by the 16 request-token records.
For every token `q`:

- if `normalize(q)` has disposition `OBSTRUCTED`, its recorded endpoint has a
  nonempty failed-`Good` set;
- if it has disposition `EXIT`, its endpoint is outside the contract and has
  an empty failed-`Good` set.

The two cases are exhaustive and disjoint over the recorded token IDs.  Thus
no recorded request remains unclassified, and every in-contract candidate
datum fails `Good`.  EXIT records are nonmembership statements rather than
candidate failures.  These are the two separate closure conclusions.

### Four inherited proof kernels

1. **Object fork (Paper 35).** Positive recurrence, inverse-edge symmetry, and
   Hashimoto non-backtracking dynamics fail different selectivity, relation,
   or ownership obligations.  No row provides the entire `Good` conjunction.
2. **Filling and clock (Paper 36).** Complete filling removes the recurrence
   to be selected; quotient and prequotient objects do not share determinant
   ownership; the unit marker does not descend.
3. **Finite coefficients (Paper 37).** Invertible holonomy cannot delete a
   scalar factor.  Graded constructions leak mixed factors or erase every
   closed orbit under full saturation.
4. **Frozen-splitting tree (Paper 38).** The full-tree periodic ledger is empty,
   the undamped operator is noncompact, and orbital/groupoid alternatives
   change ownership categories or remain generic.

Paper 39 does not re-prove these kernels as new theorems.  It types their
assumptions and endpoints and proves coverage of the finite request encoding.

## Two graph granularities

### Structural spine

```text
N35_OBJECT_FIREWALL
  -> N36_CELLULAR_CANCELLATION
  -> N37_COEFFICIENT_SATURATION
  -> N38_TREE_ORBITAL_TRILEMMA
  -> N39_AFFINE_BRANCH_CLOSED
  -> N_REGISTRY_HANDOFF
```

The spine communicates the predecessor sequence and supports the executable
prototype.  It must never be described as containing all proof distinctions.

### Expanded proof DAG

The expanded graph resolves the branches within each predecessor and includes
the auxiliary exit and governance nodes.  It has 22 named nodes and 28 typed
edges.  Every edge strictly raises a frozen rank.  All expanded identifiers,
edge endpoints, fibers, request paths, and endpoint classes survive in the
bridge artifact.

## Two boundary cases that control the paper

### E22 — historical firewall with zero coverage credit

`E22 : N37N -> NX` records a Paper-37 prohibition against searching an
unspecified new character, rank, representation, or completion.  Because the
finite request universe deliberately contains no arbitrary-instance token,
E22 lies outside `A_14` and `Sigma_16`.  Its token and class fibers are empty.
It keeps historical evidence without helping prove coverage.

### E07 / E36_37 — reset, not transport

The move from the Paper-36 filled/control object to the independently locked
Paper-37 unquotiented coefficient object is a reset.  Object, marker, operator
owner, and determinant owner all reset under `P37_SOURCE_LOCK_SD_C39`.  The
edge cannot be read as “unfill, then add coefficients.”  The bridge carries
only the inherited audit obligation and jointly binds historical provenance as
non-state metadata.

## Countermodels that enforce the scope

- A finite directed cycle supplies recurrence outside the predecessor affine
  objects; therefore the DAG is not a universal symbolic no-go.
- A nilpotent or noninvertible coefficient can delete factors outside the
  frozen invertible-local-system family; therefore the coefficient theorem is
  family-relative.
- Radial damping can create a summable operator only by changing the frozen
  undamped object/operator category; it is an exit, not a refutation.
- Proper tree lattices admit determinant theories under hypotheses absent from
  the frozen full-tree action; Paper 38 cannot be universalized to all trees.

These examples are not repairs of the encoded candidates.  They are witnesses
that the theorem must retain its domain restriction.

## Literature position

The generic ingredients are established.  Assumption-relative no-go reasoning,
classical obstruction theory, finite obstruction sets, counterexample-guided
refinement, proof certificates, and typed dependency DAGs all have substantial
prior art.  The Equational Theories Project is the closest functional
predecessor for completion of a frozen finite mathematical graph.  Murali,
Trivedi, and Zamani already use “closure certificate” for a different
dynamical-verification object.  Paper 39 therefore uses “typed affine-program
closure audit” or “retrospective obstruction-coverage audit” in prose.

The surviving novelty claim is configuration-level: no source found in the
bounded audit combines this exact content-addressed historical repair encoding,
heterogeneous object/marker/operator typing, category exits, finite coverage
checker, and registry handoff.  Confidence is moderate and conditional on the
executable audit matching the frozen bridge.

## Figure narrative

1. **Figure 1 — from structural spine to expanded proof DAG.**  A skim reader
   should see both granularities, the 14/16/17 counts, and the terminal registry
   handoff without mistaking the projection for an isomorphism.
2. **Figure 2 — total request classification.**  The 14 classes and 16 tokens
   flow into obstructed, exit-only, and mixed columns.  Failed-`Good` evidence
   and category exits are visually disjoint.
3. **Figure 3 — ownership and zero-credit firewalls.**  E07/E36_37 displays four
   RESET fields; E22 displays empty coverage fibers.  The two cases prevent the
   most tempting false readings of the theorem.

## Authority FINAL integration evidence

The following is the sole integrator-declared authority result block.  It
supports implementation fidelity only and remains distinct from the inherited
infinite mathematical theorems.

```text
Integrator status: FINAL / CLEAN
main evaluator: 535/535; sha256=041461feaf8d34c9974606b9856be5ba5fc6c26f62c88ba38b041998bfd82394
independent evaluator: 278/278; sha256=21bb9b3f623215875bdf93670165da41ff5c42f7e5ccb25cc19a432f7c048398
science projection: sha256=77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93
adversarial mutations: 29/29 rejected by each evaluator; sha256=f5fee0209155d06c8e16aedbf44ed2003f29115ad76b7f06bafe8be8a6d26f56
Route evaluation: 14/14; json_sha256=f0d7f98e06e50b1605642fda3abc47b253103c79119886fa5a5b1b0e5c6b2902
fixed Route YAML: sha256=9cda64c6ddf6bfbb865cb576b1a7475e2ce477c3627102e31862ec4c647ebc4e
analysis summary: sha256=acf6dfefcead90b84eb0f28f43c60bf94ad0512389a7ce50d458d6b08e87560a
integrity audit: 224/224; sha256=3c8aed949d8300e327bc265cd23b982b47397981ac379fef99a6d302360d7ac6
ledger audit: 65/65; sha256=be32c6dcf43050307668d583425c67226e2edbb6231120977448e8b4e778e067
exact result set: 36; sha256=69dcf722a5187dfb576a2a607b72f019cd471273c5090277db8e994e09a382dd
exact text set: 67; sha256=e92eddfec5be91fb74a617ed08c7f532e856cbc08c51d14887eafd9ee39358c5
sealed-state controls: 11/11 rejected; sha256=f12f9890d761e5cffe62f70a743cbc0a4749fe90237aa391033321581197181a
paired audit states: A=PENDING+manifest_absent; B=identical_lowercase_nonzero_40hex+exact_self_excluding_manifest; mixed_states=REJECT
managed outputs: 39
managed aggregate: sha256=ac09cd2c3be39e4d6d6ce754b5648d8a2abf7fd7fb9848db984558ff33dc82b3
experiment report: sha256=86f2184b00e25085c18abeab99ef58815290100c42cb267ea33d16f6439d4dcd
locks: research=24f180a30990c3cd581f0732dabeb641dac9e962b17300883a28f77a3844e43a; prototype=c78ca2e09dd026860533f36b94d538397ec0ba20f40980eb9dadfd2dea011762; dependency=44b432ce9f83986bb0f42fa44a3de23eef5b7910d68b5e234166212a451691dd
reproducibility: fresh A/B, cold C, hidden-provenance clone, dummy sealed-B normal/hidden audit identity, and two full-runner passes; changed_paths=0
census: spine=6/5; expanded=22/28; tags=17; classes=14 (6/6/2); tokens=16 (8/8); registry=6; new/ranked/proposed=0/0/0
```

## Limitations

1. The 14-class/16-token encoding is retrospective and outcome-informed.
2. Hashes prove byte identity, not prospective completeness or mathematical
   truth of every predecessor theorem.
3. The coverage theorem says nothing about arbitrary new instances, compound
   repairs, or mechanisms outside the enumerated tokens.
4. The global-registry predicate is snapshot-relative; “unspent successor” is
   undefined.
5. The literature search is vocabulary- and index-dependent and yields only a
   qualified, moderate-confidence novelty judgment.
6. Paper 39 contributes no Route-A arithmetic coordinate and no new operator.

## Terminal and successor obligation

The realized terminal is
`RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY`.  Historical entries
are classification witnesses, not ranked live candidates.  The empty-registry
fallback is conditional and inactive.  Paper 40 requires a new, independently
source-locked, candidate-specific non-affine object created by root or registry
governance after the Paper-39 seal.
