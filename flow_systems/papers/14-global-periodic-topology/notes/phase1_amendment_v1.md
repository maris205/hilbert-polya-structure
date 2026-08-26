# Paper 14 Phase-1 amendment v1 — all-prime topology and nonredundancy

Status: **ACTIVE / INDEPENDENT EXACT-BYTE RE-LOCK REQUIRED**  
Version: `P14-P1-AMENDMENT-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)

This amendment binds:

```text
batch design lock
  sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
research protocol
  sha256:a3ee049f27d29bb276553edcee8fbb019125b96c3e90b82f800a9706a106d7ab
candidate lock
  sha256:8cbbd9e63f53c8f821f940405c6f5a41f34a5242ab9ea24be1fb87b47ae9b096
source-topology precheck
  sha256:05fb9f622c348839514d4d69760e491e7d2afdf4eb9f14687d5e0ce05d1229cb
methodology review
  sha256:58a5642bcd7d7e36107dc179c3868fe043d878e8b370e3e58ea3be4fd7374448
```

It closes only the methodology review's `C0/M2/m2` findings.  Unmodified
owner, source, proxy, proof, control, Route, and release boundaries in the
base protocol remain binding.

## 1. P14-0 — descended base map and full fibres

The proof must begin with the source projection

```text
pr : check_X_0(C)_{E_f} -> Spec Z.
```

The `Q_{>0}` action is trivial on `Spec Z`, so `pr` is invariant and the
candidate descended map is

```text
pi : X_susp=(check_X_0(C)_{E_f} x R_{>0})/Q_{>0} -> Spec Z,
pi([P,u])=pr(P).
```

`P14-0` must prove continuity, well-defined descent, and the full-fibre
identity

```text
Gamma_p = pi^{-1}((p))
```

for the frozen finite-kernel class.  The two-prime closed-fibre theorem may
not be invoked before `P14-0` is proved.

## 2. Exact all-prime theorem signature

Let `P` be the set of rational primes, let

```text
Per_Ef = union_{p in P} Gamma_p,
```

with the actual subspace topology, and let

```text
J : coproduct_{p in P} Gamma_p -> Per_Ef
```

be the canonical continuous bijection induced by component inclusions.

The central all-prime claims are now:

### P14-G1 — canonical comparison

Determine whether `J` is open and therefore a homeomorphism.  If it is not,
classify the precise additional cross-packet open-set condition on
`Per_Ef`.  Finite-subfamily homeomorphisms do not decide this claim.

### P14-G2 — arbitrary relative subfamilies

For every `S subset P`, compute in the **relative owner** `Per_Ef`

```text
closure_Per(union_{p in S} Gamma_p)
```

and classify exactly when the union is open, closed, or clopen.  The answer
must include empty, finite nonempty, cofinite, and infinite coinfinite
branches.

### P14-G3 — ambient closure

Separately compute, or give sharp source-level upper and lower bounds for,

```text
closure_X_susp(union_{p in S} Gamma_p).
```

No relative closure is promoted to this ambient owner.  If a full ambient
classification is not source-decidable, the proof must mark it
`SOURCE_UNDERDETERMINED` and state the exact missing data.  An infinity-
sensitive relative theorem under P14-G2 can still be evaluated separately.

### P14-G4 — quotient and universal property

Define the canonical packet-index map

```text
kappa : Per_Ef -> P,       kappa(x)=p iff x in Gamma_p.
```

Give `P` the quotient topology induced by `kappa`, compute it, and prove the
universal `T0` property only after P14-G1--G2.  `P_discrete`, the Zariski
closed-point subspace of `Spec Z`, and an abstract bare prime set are three
different proposed targets until a theorem identifies them.

## 3. Expanded controls

In addition to the finite controls, register:

```text
TAGGED-COPRODUCT-ALL:
  coproduct_{p in P} Gamma_p with the stipulated topological-sum topology;

COFINITE-INDEX-CONTROL:
  indiscrete fibres indexed by P with the cofinite topology on P;

DISCRETE-INDEX-CONTROL:
  the same fibres indexed by discrete P.
```

The controls have identical finite restrictions.  Therefore any finite-only
test is analytically incapable of distinguishing the central all-prime
branches and cannot validate P14-G1--G4.

## 4. Claim-delta matrix required by the final proof

The proof audit must complete the following fields for every central claim:

| Claim | Exact premise owner | P9 inherited part | P10 inherited generic part | Deninger/source part | New P14 step | Direct substitution? | Infinity-sensitive? | Ambient-owner content? | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| P14-0 | source suspension | none | none | projection definitions | descent/full-fibre proof | audit | no | yes | pending |
| finite `p,q` theorem | actual two-packet subspace | fibre indiscreteness | finite coproduct consequences | closed fibres | source comparison | audit | no | yes | pending |
| P14-G1 | actual `Per_Ef` | fixed fibres | abstract coproduct theorem | global ambient topology | infinite canonical-map test | audit | yes | yes | pending |
| P14-G2 | relative `Per_Ef` | fixed fibres | abstract component-union formulas | global neighborhoods | arbitrary-subfamily closure | audit | yes | relative | pending |
| P14-G3 | ambient `X_susp` | none | none | ambient source topology | infinite ambient closure | audit | yes | yes | pending |
| P14-G4 | quotient of actual `Per_Ef` | fixed-fibre collapse | generic `T0` facts | source index map | quotient topology/universal proof | audit | yes | yes | pending |

No row may be labeled new merely because Papers 9--10 did not print the
same sentence.

## 5. Revised standalone rule

The following package cannot by itself earn `STANDALONE_PASS`:

```text
Per_Ef homeomorphic to coproduct_p Gamma_p,
K0(Per_Ef) homeomorphic to discrete P,
and any direct P10 consequence of those statements.
```

Standalone eligibility requires at least one central infinity-sensitive or
ambient-owner theorem whose proof is not direct substitution of a source
closed-fibre lemma, Paper-9 indiscreteness, and Paper-10's abstract coproduct
classification.  Examples of qualifying *types* of result include a
non-discrete global index topology, an arbitrary infinite-subfamily closure
theorem, or a sharp ambient closure/underdetermination theorem.  This list
does not predetermine which statement is true.

An independent post-proof nonredundancy review and bounded external
precedent search remain mandatory.  If the infinity-sensitive/ambient delta
is absent, disposition is `TECHNICAL_NOTE_OR_MERGE`; allocation of the
batch's sole Technical Note slot is not automatic.

## 6. Scope narrowing

The base protocol's P14-6 is demoted to a non-theorem comparison remark.
This version proves claims only for `Spec Z`, rational-prime closed points,
and the frozen `E_f` subsystem.  Extension to another arithmetic scheme
requires a new versioned owner/source lock.

## 7. Authorization boundary

This amendment authorizes only independent exact-byte re-lock reviews.
Proof implementation remains false until methodology, source, and
devil/domain reviewers all pass the amended tuple.  Controls, Route A/B,
manuscript, release, Git, and public synchronization remain blocked/false.

