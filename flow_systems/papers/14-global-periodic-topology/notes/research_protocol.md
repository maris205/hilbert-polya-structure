# Paper 14 research protocol

Status: **PHASE-1 USER-CONFIRMED / INDEPENDENT REVIEW REQUIRED**  
Version: `P14-P1-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Working title: **Global Topology of the Rational-Witt Periodic Locus**  
Route B, proof implementation, controls, Route A, manuscript, release, and
Git/public synchronization: false

Batch design lock:

```text
papers14_18_batch_design_lock.md
sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
```

## 1. Research question

Let `Y=check_X x R_{>0}` be the exact finite-kernel pre-suspension owner,
with the diagonal `Q_{>0}` action and open quotient map
`rho:Y->Y/Q_{>0}` used by Paper 9.  For a rational prime `p`, let

```text
Z_p=C_p^{E_f} x R_{>0},       Gamma_p=rho(Z_p).
```

Paper 9 computes the inherited topology of one `Gamma_p`; Paper 10 studies
an explicitly copied tagged coproduct.  Paper 14 asks instead:

> What is the inherited subspace topology on the actual union of two or
> more distinct prime packets inside `Y/Q_{>0}`?  Which cross-prime closure
> and specialization relations occur, and what is the resulting global
> Kolmogorov quotient of the periodic locus?

The question is source-topological.  A hand-made disjoint union is a
negative control, not the candidate owner.

## 2. Exact owners

### 2.1 Source ambient owner

```text
check_X = check_X_0(C)_{E_f}
Y       = check_X x R_{>0}
(P,u)q  = (F_q P, q^{-1}u),  q in Q_{>0}
X_susp  = Y/Q_{>0}
```

All topologies and inclusions are those inherited from Deninger's frozen
finite-kernel construction.  The admissible class `E_f` is fixed; Paper 14
does not claim that the source uniquely selects it among all admissible
classes.

### 2.2 Prime packets and unions

```text
Z_p       = C_p^{E_f} x R_{>0}
Gamma_p   = rho(Z_p) subset X_susp
Gamma_pq  = Gamma_p union Gamma_q,  p != q
Per_Ef    = union_{p prime} Gamma_p
```

`Gamma_pq` and `Per_Ef` carry actual subspace topologies from `X_susp`.
No coproduct topology, compact-product topology on `U_p/H_p`, or orbitwise
standard topology is imported.

### 2.3 Controls

- `TAGGED-COPRODUCT-PQ`: the topological disjoint union of the already
  defined fixed-prime packets;
- `COPIED-INDISC-PQ`: two copied indiscrete components with declared labels;
- `SAME-PRIME-COPY`: two formal copies of one `Gamma_p`;
- finite toy quotient actions whose saturation and specialization can be
  enumerated exactly.

Controls carry no source-topology credit.

## 3. Candidate claim ledger

| ID | Candidate claim | Phase-1 status |
|---|---|---|
| P14-1 | Give an exact prequotient criterion for closure and specialization between saturated subsets `Z_p` and `Z_q`. | SPECIFIED / UNPROVED |
| P14-2 | Determine the inherited topology of `Gamma_pq` for every `p!=q`. | FAIL-FAST / UNPROVED |
| P14-3 | Decide whether each `Gamma_p` is open, closed, locally closed, or specialization-linked inside `Per_Ef`. | BLOCKED BY P14-2 |
| P14-4 | Compute the specialization preorder and `T0` reflection of `Per_Ef`. | BLOCKED BY P14-2 |
| P14-5 | Compare the actual union with `TAGGED-COPRODUCT-PQ` and prove equality or strict mismatch. | BLOCKED BY P14-2 |
| P14-6 | State exactly which conclusions extend from rational primes to finite-residue-field closed points. | SOURCE AUDIT REQUIRED |
| P14-7 | Design deterministic finite saturation/specialization controls after the symbolic proof. | UNAUTHORIZED |

P14-2 may have a positive classification, a collapse theorem, or a precise
source-underdetermination result.  It may not be replaced by an asserted
coproduct.

## 4. Proof obligations

1. Work before quotienting whenever possible: resolve closure using the
   topology of `check_X`, the `Q_{>0}` action, and saturation under `rho`.
2. Distinguish convergence of raw characters, Galois-orbit points, colimit
   points, and suspended quotient points.
3. Prove that every sequence/net used stays in its claimed prime packet or
   crosses packets in the claimed manner.  A density theorem proved only
   within one fixed-prime fibre is insufficient.
4. Use nets rather than sequences unless first countability or an adequate
   sequentiality theorem is proved on the exact domain.
5. Keep `Gamma_p` as the actual inherited packet.  Its set model
   `(U_p/H_p)x(R_{>0}/p^Z)` supplies no topology.
6. Treat compactness as open-cover compactness unless Hausdorffness is
   separately proved.
7. Prove functoriality of the `T0` quotient only after the actual
   specialization preorder is known.

## 5. Fail-fast decision

`GO_TO_FULL_PROOF` requires an exact source-level lemma that decides
`Gamma_pq` for arbitrary distinct primes.

`SOURCE_UNDERDETERMINED` is mandatory if current source definitions do not
decide the cross-prime topology without adding a new topology, atlas, or
coordinate choice.  That is a legitimate result but is not automatically a
standalone paper.

`NOTE_OR_MERGE` is mandatory if the only theorem is the fixed-prime Paper-9
indiscreteness result plus a formal coproduct.

## 6. Standalone and novelty gate

A standalone center must contain a cross-prime theorem on the actual ambient
owner and at least one of:

- a nontrivial cross-prime specialization classification;
- an actual global `T0` quotient not stipulated by labels; or
- a sharp impossibility theorem proving that the ambient source data cannot
  determine the proposed global topology within a declared class.

Novelty wording is capped at
`NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH`.  Deninger's current
paper and technical arXiv version, Morishita's current comparison, and all
Papers 1--13 internal owners are mandatory search strata.

## 7. Phase gates

Before proof authorization, three independent reports must pass on the exact
bytes of this protocol and the batch lock:

1. methodology/nonredundancy;
2. devil/domain and source-topology attack;
3. primary-source feasibility.

Controls require a later exact design lock and independent review.  Route A
requires a final proved owner registry.  Route B remains false.  No
manuscript or release action is authorized by this protocol.
