# Weil–étale topoi: a formal prime-orbit clock without a prime-symbolic dynamical bridge

**Paper ID:** `023-weil-etale-topos-flow`  
**Candidate ID:** `ATF-20260914-WET01`  
**Date / status:** `2026-09-14; BROADENED-CARRIER EXTERNAL CONTROL`  
**Audit state:** `T0/T1 ESTABLISHED AS TOPOS DATA; T2 FORMAL REPETITION ESTABLISHED; TRACE WEIGHT AND T3 OPEN; ASFS Route A/B NOT APPLICABLE / NOT INVOKED`

## Abstract

This breadth screen freezes the Weil–étale topos of `Spec Z` as an
arithmetic-topos flow (`ATF`) control. The source's canonical morphism to the
classifying topos `B_R` encodes a flow, while a closed embedding associated to
the Weil group of `(p)` encodes a closed object of length `log p`. Its cyclic
parameter gives formal repetitions `r log p`. Unlike a point-set suspension,
this is categorical orbit data. It has no transfer/determinant owner in the
same object and no established coding from the project's sieve-symbolic source.
It is therefore a separate external control, not a refinement or replacement
of `ALF-20260913-DEN01`.

## 1. Frozen same-object ledger

The object is the compactified number-ring topos `Xbar_W` for
`Xbar=overline(Spec Z)` together with Morin's canonical morphism

```text
f : Xbar_W -> B_R.
```

For a finite closed point `(p)`, freeze the source's closed embedding

```text
i_p : B_(W_Fp) -> Xbar_W
```

over `B_R`. The induced homomorphism `W_Fp -> R` sends the cyclic generator to
`log p`; consequently its `r`th power has time `r log p`. This is one
topos-theoretic object and one action encoding. It is not a smooth manifold,
a map, a roof, a mapping torus, or a point-set orbit space.

## 2. T1 and T2: what the source actually owns

For `Spec Z`, the finite closed points are exactly `(p)`. The source treats the
closed embedding `i_p` as the analogue of a closed orbit of length `log p`.
The cyclic Weil group supplies the formal repetition parameter. Thus the
following source-level chain is established:

```text
(p) -> B_(W_Fp) -> Xbar_W,      r -> r log p.
```

This differs materially from the Deninger `ALF` carrier: it neither chooses a
circle in a compact packet nor identifies one. Accordingly, no multiplicity,
primitive-orbit, fixed-point, or trace weight is inferred here.

## 3. Source and lineage controls

Morin's result is framed as a topos translation of properties expected of a
conjectural arithmetic dynamical system. It does not construct a semiconjugacy
from the prime indicator, squarefree closure, or primorial gap recursion of the
prior-work path. The only currently documented relation is the identity of the
arithmetic labels `(p)`.

This is insufficient under the repository's lineage gate. A parallel source
control is that Flach–Morin relate Weil–étale cohomology to zeta special values
subject to analytic assumptions; that statement neither creates a dynamical
trace formula on `Xbar_W` nor fixes packet/primitive weights. Borrowing it
would violate the same-object rule.

## 4. Gate assessment

| Broadened audit | Evidence for this exact object | Status | Limitation / decision |
| --- | --- | --- | --- |
| T0 | `Xbar_W`, `f:Xbar_W -> B_R` | established as topos data | not a point-set flow |
| T1 | `(p)` and `i_p`, period `log p` | established as topos data | no sieve-symbolic dynamics |
| T2 | cyclic `W_Fp` gives `r log p` | formal repetition established | primitive ledger and weight open |
| T3 | no same-object transfer/trace/determinant | OPEN | do not import zeta cohomology |
| Route A/B | nonclassical external control | NOT APPLICABLE / NOT INVOKED | prohibited |

## 5. Decision

**Decision: `STOP AS EXTERNAL CONTROL; FORK`.** This carrier is a useful
benchmark because it natively makes prime periods and repetitions categorical,
but it cannot advance without a real prime-symbolic dynamical bridge and a
same-object trace owner. Future broad screens should test whether a
sieve-derived groupoid can map functorially into such a topos without adding a
prime list or selecting orbit representatives.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and source lock](evidence/README.md)
- [Prior sieve source control](../019-primorial-gap-recursion-control/paper.md)
- [Distinct Deninger ALF control](../022-deninger-alf-specz/paper.md)
