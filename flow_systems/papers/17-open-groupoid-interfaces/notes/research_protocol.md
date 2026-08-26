# Paper 17 research protocol

Status: **PHASE-1 USER-CONFIRMED / INDEPENDENT REVIEW REQUIRED**  
Version: `P17-P1-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Working title: **Topos and Quantale Interfaces for Indiscrete Real-Action Groupoids**  
Route B, proof implementation, controls, Route A, manuscript, release, and
Git/public synchronization: false

Batch design lock:

```text
sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
```

## 1. Research question

Papers 9--11 show that the actual fixed-prime packet action groupoid lies
outside the previously registered Hausdorff/LCH completion frameworks and
that one author-defined convolution interface forgets the action.  Paper 17
tests two frameworks whose advertised domains include open non-Hausdorff
groupoids:

> What information about an indiscrete real-action groupoid survives in its
> equivariant-sheaf/classifying topos and in its open-groupoid quantal frame,
> and how do those outputs compare with the standard periodic-circle
> groupoid?

This is an exact-domain theorem, not an assertion that every sheaf, stack,
locale, or noncommutative interface must collapse.

## 2. Generic actual owner

Let `X` be a nonempty set with the global indiscrete topology and any right
action of the usual additive group `R`.  Use the range-first groupoid

```text
G_X = X rtimes R,
r(x,t)=x,
s(x,t)=x.t,
(x,t)(x.t,u)=(x,t+u),
(x,t)^(-1)=(x.t,-t).
```

The arrow topology is the product topology on `X x R`; composable pairs use
`X x R^2`.  The source and range maps are proposed to be open, but this is a
proof obligation under the exact framework definitions.

Fixed-prime application:

```text
X = Gamma_p_actual,
Stab(x)=(log p)Z for every x.
```

The application may use only Paper-9 actual topology and Paper-12 literal
stabilizer/mark.  It may not import the standard circle topology.

## 3. Equivariant-sheaf/topos branch

The source audit must select one exact definition of the classifying topos
or category of equivariant sheaves for an open topological groupoid.

Candidate obligations:

1. prove `Sh(X_ind)` and classify its étale spaces without hidden
   Hausdorffness;
2. type the groupoid action on an étale object;
3. determine whether connectedness of `R` forces every induced action on
   the discrete sheet set to be trivial;
4. compute the resulting equivariant-sheaf category/topos; and
5. test whether orbit count, action, stabilizer, or the numerical value of
   `log p` is recoverable.

The protocol does **not** freeze the answer as `Set`.  Counterexamples from
nontrivial étale objects, isotropy actions, or a different exact classifying
topos must be reported rather than normalized away.

## 4. Open-quantal-frame branch

For the exact open groupoid, compute the frame of arrow opens and its
groupoid operations.  The proposed coordinate calculation is

```text
O(G_X^(1)) ~= O(R),
U * V = U+V,
U^* = -U,
```

where the first equality relies on `X` being nonempty and globally
indiscrete.  The proof must check the quantale multiplication convention,
openness of the relevant structure maps, joins, units or support maps, and
whether the framework assigns more than the bare arrow-open quantale.

The central comparison asks whether two different actions on the same
indiscrete carrier produce isomorphic registered quantale outputs.  Trivial,
transitive-periodic, and nontransitive actions are mandatory controls.

## 5. Standard owner comparison

For one standard periodic orbit

```text
O_L=R/(LZ),              G_L=O_L rtimes R,
```

the protocol asks for the corresponding topos and quantale information.
The comparison must distinguish:

- abstract isotropy `LZ` as a group, which is isomorphic to `Z` for all
  `L>0`;
- the strict time-marked embedding `LZ -> R`, which retains `L`; and
- unmarked equivalence or dilation, which may erase the numerical length.

No Cartan/Weyl, C*-completion, or twist theorem is inherited from an
unfrozen Paper-13 draft.

## 6. Candidate claim ledger

| ID | Candidate claim | Phase-1 status |
|---|---|---|
| P17-1 | `G_X` is an open topological groupoid in each selected source domain. | SOURCE/PROOF REQUIRED |
| P17-2 | Exact classification of equivariant sheaves and retained invariants. | CENTRAL / UNPROVED |
| P17-3 | Exact open-quantal-frame computation and action-blindness test. | CENTRAL / UNPROVED |
| P17-4 | Actual-versus-standard comparison with strict/unmarked variance. | SPECIFIED / UNPROVED |
| P17-5 | Fixed-prime application and trivial/nontransitive controls. | BLOCKED BY P17-1--4 |
| P17-6 | Deterministic finite locale/action controls, if meaningful. | DESIGN UNAUTHORIZED |

## 7. Source and novelty boundary

Mandatory primary strata include Moerdijk's topological-groupoid topos,
Forssell's open topological groupoids, and Protin--Resende's quantales of
open groupoids.  The audit must bind exact hypotheses, definitions, theorem
locators, and any local compactness, sobriety, étale, Hausdorff, or choice
requirements.

The following statements are prohibited:

- all non-Hausdorff groupoid frameworks collapse;
- a classifying topos is the same as a quotient topological space;
- a quantale output is automatically a C*-algebra or trace owner;
- a zero exact-package search hit proves priority; or
- the standard owner inherits actual topology.

## 8. Standalone and merge rule

Topos and quantale branches stay together.  Either branch alone is likely a
standard indiscrete-space calculation.  Standalone eligibility requires:

1. exact-domain admission of the actual groupoid;
2. both complete computations;
3. an actual/standard marked comparison; and
4. a theorem-level explanation of why these valid point-free interfaces do
   or do not cross the Paper-11 action-retention gate.

If the conjunction remains routine after source subtraction, Paper 17 may be
the batch's sole Technical Note.  If either source domain does not admit the
actual owner, the protocol must be version-amended rather than switching
silently to a proxy.

## 9. Phase gates

Independent methodology/nonredundancy, source/domain, and devil reviews are
mandatory before proof authorization.  No source PDF may enter a public
payload.  Controls, Route, manuscript, and release use later gates.  Route B
and Git/public synchronization remain false.
