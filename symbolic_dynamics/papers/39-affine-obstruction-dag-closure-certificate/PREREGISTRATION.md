# Paper 39 retrospective checker freeze — SD-C41

## 1. Status of this document

This is a checker-freeze record, not a claim that Paper 39 was prospectively
preregistered before the outcomes of Papers 35--38 were known.  The predecessor
outcomes were already available when the finite Paper-39 encoding was assembled.
The encoding below was then frozen before the Paper-39 checker was run.

Only literal predecessor source fields, the Paper-38 prohibition list, and the
pre-existing Route-A criterion may be called predecessor-frozen.

## 2. Frozen question

Let `Good = I and R and S and D and M and C`, where the six coordinates are the
pre-existing intrinsic-source, recurrence, selectivity, determinant-ownership,
marker, and control obligations.  For the exact finite request universe
`Sigma_16`, does every token normalize to either:

1. an in-contract expanded-DAG path with an endpoint carrying a nonempty set of
   failed `Good` coordinates; or
2. a typed contract exit that receives no obstruction credit?

If the classification is total, the permitted conclusion is relative closure
of this encoded affine branch.  No universal affine no-go follows.

## 3. Frozen finite domain

The repair alphabet has exactly 14 classes:

```text
affine_cayley_representation
finite_rank_local_system
character
grading
quotient
induced_shift
first_return_map
bass_serre_splitting
valuation_tree
boundary_model
modular_phase
basepoint_damping
finite_total_weight_retrofit
groupoid_trace
```

The request universe has exactly 16 tokens:

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

No `OTHER_INSTANCE`, implicit family completion, or arbitrary compound-repair
token is admitted.

## 4. Frozen graph objects

Two graph granularities must remain distinct:

- the executable **structural spine**, with 6 nodes and 5 edges; and
- the **expanded proof DAG**, with 22 nodes, 28 edges, and 17 internal tags.

Their relationship is a total many-to-one projection with explicit auditable
fibers.  It is not injective.  Every expanded edge has typed endpoints and a
strictly increasing rank.

The 28 expanded edges are partitioned exactly into 17 internal transitions,
5 closure edges, 3 token-associated contract exits, 1 auxiliary non-domain
firewall, and 2 governance guards.

## 5. Endpoint-obstruction rule

Closure is certified by a total token-classification map, not by reflexive
reachability rhetoric.  Each obstructed token has a specified endpoint whose
failed-`Good` set is nonempty.  Each exit token has a specified boundary/exit
endpoint and an empty failed-`Good` set.  EXIT is never evidence for `not Good`.

The frozen class census is:

```text
6 OBSTRUCTED / 6 EXIT_ONLY / 2 MIXED
```

The frozen token census is:

```text
8 OBSTRUCTED / 8 EXIT
```

## 6. Special firewall and transfer constraints

Expanded edge `E22 : N37N -> NX` is an auxiliary historical firewall outside
the 14-class/16-token domain.  Its class and token fibers are empty.  It retains
historical boundary evidence but contributes zero exhaustiveness or failed-
`Good` credit.

Expanded edge `E07` projects to structural edge `E36_37`.  The following four
candidate-state fields are all `RESET` under `P37_SOURCE_LOCK_SD_C39`:

```text
object
marker
operator_owner
determinant_owner
```

The marker is redeclared, not transported.  Historical provenance is non-state
audit metadata jointly bound by the edge endpoints, E07 authority, embedded
P36/P37 hashes, and packet locks.  It is not a fifth candidate-state field.

## 7. Frozen decision rule

If and only if all finite-domain, endpoint, ownership, projection, firewall,
and source-hash checks pass, record:

```text
CLOSE_ENTIRE_AFFINE_BRANCH
(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

Because the historical non-affine registry predicate is nonempty, the realized
governance code is:

```text
RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY
```

If that predicate were empty, and only then, the conditional fallback would be:

```text
STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR
```

The handoff performs no ranking, proposal, reclassification, or Paper-40
authorization.  The phrase "unspent successor" remains undefined and is not
silently added as a predicate.

## 8. Countermodel and adversarial validity checks

The paper must retain counterexamples showing why the theorem cannot be made
universal: finite directed cycles can satisfy recurrence, nilpotent/noninvertible
coefficients can delete factors outside the frozen invertible-local-system
family, damping can change the operator category, and proper tree lattices can
support determinant theories outside the frozen full-tree object.

Machine checks must separately reject at least the following corruptions:

- missing or duplicated graph records;
- missing, duplicated, or misclassified request tokens;
- EXIT rows granted obstruction credit;
- E22 granted class/token coverage or stripped of firewall typing;
- any `E36_37` carry/equivalence substitution for a RESET field;
- a false prospective-preregistration or predecessor-independence claim;
- registry insertion, ranking, or false-empty classification; and
- any new Paper-39 symbolic mechanism.

## 9. Integrator boundary

Experiment hashes, assertion counts, reproducibility certificates, and result
ledgers are not frozen by this writer.  They may be copied into the narrative
and manuscript only after an explicit integrator authority FINAL declaration.
Before that declaration, the paper records only the mathematical/source hashes.

## 10. Successor obligation

Paper 39 authorizes no next experiment.  Root or registry governance may later
source-lock a genuinely candidate-specific, non-affine Paper-40 object.  Such a
lock must occur independently after the Paper-39 seal and cannot be inferred
from this registry handoff.
