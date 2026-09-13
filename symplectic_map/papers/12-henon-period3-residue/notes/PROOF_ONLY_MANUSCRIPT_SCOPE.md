# Proof-Only Manuscript Scope

## Control state

- Candidate and lifecycle ID: `henon_period3_residue_proof_note_v1`
- Mode: proof-only specialist note
- Current status: `READY_FOR_INDEPENDENT_PROOF_ONLY_HANDOFF_REVIEW`
- Registered evidence used: `false`
- Manuscript authorized: `false`, pending independent proof-only handoff review
- Finalization authorized: `false`
- Consumed v1 disposition:
  `REGISTERED_AUDIT_TERMINAL_FAIL / NO_RERUN / NO_RAW_RESULT / NO_RESULT_PASS`
- v1 manuscript: withheld

The independent handoff reviewer must use the exact bound files and write only
`notes/INDEPENDENT_PROOF_ONLY_HANDOFF_REVIEW.md`. The required future verdict
is `PROOF_ONLY_HANDOFF_PASS`. This scope does not pre-authorize that verdict.

## Proof-only authority

Every theorem statement below is derived solely from
`notes/PROOF_PACKAGE.md` at SHA-256
`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`,
under the independent `SOURCE_LOCK_PASS` in
`notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` at SHA-256
`5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11`.
The source lock is
`2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2`.

`SOURCE_LOCK_PASS` is proof/source authority within the frozen normalized and
formal-scheme scope. It is not registered-result authority, manuscript
authority, finalization authority, or a proof of universal nonvanishing.

## C1--C18 and PC1--PC2 proof-only matrix

In the table, `PENDING_HANDOFF_PROOF_ONLY` means that the claim is supported
by the immutable proof package and source review, but cannot enter a
manuscript until the fresh proof-only handoff review passes. It never means
registered certification.

| ID | Proof-only statement | Required proof location or dependency | Current status |
|---|---|---|---|
| C1 | Work is in the normalized monic-centered Jacobian-minus-one Hénon category over characteristic zero. | assumptions and normal-form scope | `PENDING_HANDOFF_CONTEXT_ONLY` |
| C2 | On the length-\(2m\) fixed scheme, multiplication by \(q=p'\) has formal spectrum \(0^{\times 2m}\), with \(q^2=0\). | Step 1; nonreduced quotient algebra | `PENDING_HANDOFF_PROOF_ONLY` |
| C3 | The exact formal period-two trace multiset is \(2^{\times((2m)^2-2m)}\). | Step 1; product fixed scheme and diagonal subtraction | `PENDING_HANDOFF_PROOF_ONLY` |
| C4 | Within normalized moduli, \(f_{m,a}\sim f_{m,b}\) iff \(a^{2m-1}=b^{2m-1}\). | Step 2; normalized root-of-unity action and converse | `PENDING_HANDOFF_PROOF_ONLY` |
| C5 | The cyclic equations encode \(\operatorname{Fix}(f^3)\) at \(\varepsilon=1\), and their Jacobian determinant is \(q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2)\). | Step 3 | `PENDING_HANDOFF_PROOF_ONLY` |
| C6 | The cyclic quotient is monic free of rank \((2m)^3\) over the parameter ring. | Step 4; standard monomial basis | `PENDING_HANDOFF_PROOF_ONLY` |
| C7 | \(S_m=\operatorname{Tr}(t_\varepsilon^m)=\operatorname{Res}(t_\varepsilon^{m+1})\) for the frozen complete-intersection convention. | Step 4; prior trace/residue theorem specialized here | `PENDING_HANDOFF_PROOF_ONLY_PRIOR_METHOD` |
| C8 | Weighted homogeneity initially permits exactly four invariant monomials in \(S_m(a,\varepsilon)\). | Step 5 | `PENDING_HANDOFF_PROOF_ONLY` |
| C9 | The coefficient of \(a^{3(2m-1)}\) vanishes. | Step 6; separated algebra and nilpotence | `PENDING_HANDOFF_PROOF_ONLY` |
| C10 | The coefficient of \(a^{2(2m-1)}\varepsilon^m\) vanishes. | Step 7's three local branches plus Step 10's exact diagonal branch | `PENDING_HANDOFF_PROOF_ONLY` |
| C11 | \(S_m(a,\varepsilon)=C_m\varepsilon^{3m}+D_ma^{2m-1}\varepsilon^{2m}\). | C7--C10 | `PENDING_HANDOFF_PROOF_ONLY` |
| C12 | \(C_m=0\) for odd \(m\). | Step 8; coordinate reversal | `PENDING_HANDOFF_PROOF_ONLY` |
| C13 | The frozen nested-binomial expression equals \(D_m\) for every \(m\ge2\). | transparent Step 9 in full, including (9.14), transfer flow, and separate \(j=0\) case | `PENDING_HANDOFF_PROOF_ONLY` |
| C14 | The formal fixed contribution to the \(m\)-th period-three moment is zero. | Step 10; \(q^2=0\) and \(t_\varepsilon^m=0\) | `PENDING_HANDOFF_PROOF_ONLY` |
| C15 | Every normalized monic-centered quartic with formal fixed-point trace multiset \(0^4\) has \(p=(x^2-L)^2\). | Step 11; root multiplicity partition and centering | `PENDING_HANDOFF_PROOF_ONLY` |
| C16 | On that quartic fiber, \(S_2^{(3)}(L)=-1296000-1572864L^3\). | Step 12's direct tensor-Laurent slope derivation and direct constant ledger | `PENDING_HANDOFF_PROOF_ONLY` |
| C17 | The formal exact-period-three pointwise length is 60 and the cyclewise moment is \(-432000-524288L^3\). | Step 13 local multiplicity, then formal subtraction and division by three | `PENDING_HANDOFF_PROOF_ONLY` |
| C18 | Period three is the minimal conjugacy separator on the complete normalized quartic fiber whose formal fixed-point trace multiset is \(0^4\). | C2--C4 and C15--C17; normalized scope only | `PENDING_HANDOFF_PROOF_ONLY_SCOPED_MINIMALITY` |
| PC1 | On the complete normalized quartic fiber with formal fixed-point trace multiset \(0^4\), the family is \(f_L=(y+(x^2-L)^2,x)\); periods one and two are blind, while the formal exact-period-three second trace moment is \(-384(3375+4096L^3)\), the first separating moment and an affine coordinate on the normalized conjugacy fiber. | principally C1--C7 and C14--C18; Step 12 is independent of the all-\(m\) collapse | `PENDING_HANDOFF_PROOF_ONLY_AGGREGATE` |
| PC2 | For every symbolic integer \(m\ge2\), the formal period-three moment has the two-term law with the frozen finite nested-binomial formula for \(D_m\), and \(C_m=0\) for odd \(m\). | C1--C14 | `PENDING_HANDOFF_PROOF_ONLY_AGGREGATE` |

PC1 and PC2 are paper-level aggregates, not replacements for atomic C1 and
C2. No claim in this matrix receives computational support from R100.

## Required transparent presentation of Step 9

The manuscript must not compress the coefficient certificate into “a
computer algebra expansion” or cite a finite check in place of the proof. It
must expose, in a checkable order:

1. the four-branch normal-form recurrence (R), reduction-state coefficient
   (9.1), base cases (9.2), and terminating recurrence (9.3), including all
   signs and total-degree decreases;
2. uniqueness/order independence through the Laurent coefficient (9.4) and
   reciprocal expansion (9.5), explaining why interleavings are not extra
   summands;
3. the expansion (9.6), pre-collapse coefficient \(\mathcal C_{m,j}\)
   in (9.7), assembly (9.8), recurrence certificate (9.9), admissibility
   conditions (9.10)--(9.11), signed multiplicity (9.12), and exhaustive
   Laurent sum (9.13);
4. the local signed fiber identity (9.14), proved by coefficient extraction
   from \((1-z)^N(1-2z+z^2)^{-n-1}\), with the generalized-binomial
   convention stated explicitly;
5. the congruence (9.17), sum rule (9.18), unique distinguished coordinate
   (9.19), incoming-transfer bijection (9.20), local factors and guarded
   ranges (9.21), and orientation sign in (9.22);
6. the \(j\ge1\) collapse (9.23)--(9.24) and the genuinely separate
   \(j=0\) flow classification (9.25), including the vanishing
   exceptional pattern (9.26); and
7. the conclusions (9.27)--(9.28), immediately followed by the statement
   that universal \(D_m\ne0\) remains open.

Omitting the local identity, transfer-flow bijection, or separate \(j=0\)
case makes the proof opaque and violates this scope.

## Required transparent presentation of Step 12

The quartic identity must be proved from the source package, not attributed
to an engine. The manuscript must:

1. label the specialization of the Step-9 formula as a cross-check rather
   than registered evidence;
2. present the independent source-level tensor-Laurent derivation based on
   (12.1), including why only the stated denominator patterns contribute to
   the slope;
3. present the direct normal-form recurrence (12.2) and the finite
   top-coefficient ledger used to obtain the constant term;
4. combine those two source derivations into
   \(S_2^{(3)}(L)=-1296000-1572864L^3\); and
5. avoid “dual-engine agreement,” “registered verification,” “reproduced by
   R100,” or any equivalent computational language.

Here “independent” means independent derivations inside the immutable proof,
not two successful runtime tracks.

## Required transparent presentation of Steps 10 and 13

The manuscript must keep two obligations separate:

- **Step 10, moment:** on the fixed algebra,
  \(t_\varepsilon=q^3+3\varepsilon^2q\) and \(q^2=0\), so the
  fixed \(m\)-th moment vanishes for \(m\ge2\).
- **Step 13, multiplicity:** the transverse \((u,v)\)-Jacobian is
  invertible; formal elimination leaves
  \(3p(\alpha+\delta)+O(\delta^{2r-1})\), of exact order
  \(r\). Hence the fixed support has its full scheme length inside
  \(\operatorname{Fix}(f^3)\).

Only after the multiplicity argument may the manuscript subtract formal
lengths \(64-4=60\). Only after pointwise exact-period subtraction may it
divide by three to state the cyclewise moment. Zero fixed moment alone is not
a length argument.

## Exact provenance wording

Any proof-only manuscript must include the substance of all three paragraphs
below without strengthening them.

> All theorem claims in this note are derived from the source-locked proof
> package at SHA-256
> `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`,
> which received the independent source verdict `SOURCE_LOCK_PASS` at review
> SHA-256
> `5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11`.
> They do not use registered computational evidence.

> The sole v1 registered audit was consumed and ended
> `REGISTERED_AUDIT_TERMINAL_FAIL`; no rerun is permitted, no raw result
> exists, and no result gate passed. A static forensic analysis attributes the
> failure with approximately 0.98 confidence to a deterministic Track Q
> scalar-versus-pair endpoint defect, but the child stderr was not preserved.
> No scientific mismatch was recorded, and that absence is not evidence of
> agreement.

> Cantat--Dujardin already supply the quartic obstruction family and its
> period-one/two blindness; Friedland--Milnor supply normalized Hénon
> background; multidimensional residue, quotient-trace, and formal periodic
> cycle machinery are prior methods. The contribution claimed here is limited
> to the source-proved formal period-three law and coefficient certificate and
> the sharp minimal-separator theorem on the complete normalized quartic
> fiber. The bounded no-hit search is not a historical-priority proof.

## Forbidden registered statements

The manuscript, abstract, captions, tables, supplements, metadata, and press
language must not state or imply any of the following:

- that R100, the registered audit, Track Q, Track R, or the adjudicator passed;
- that two registered engines agreed or independently reproduced a value;
- that any theorem was computationally, experimentally, or empirically
  certified by the consumed audit;
- that a raw result, result manifest, result review, or result-pass artifact
  exists;
- that registered coefficient diagnostics matched at either locked index;
- any numerical value of `D8`, `D9`, `E8`, or `E9`;
- any trend, parity theorem, sign theorem, or nonvanishing inference from the
  locked tuple or historical development checks;
- that “no scientific mismatch” means scientific agreement;
- that the defect was observed in a retained traceback or confirmed by rerun;
- that the deployment pass is a result pass; or
- the conditional terminal wording from the old claims matrix as though all
  of its source, deployment, registered-result, and integrity gates had passed.

No figure or table may be derived from code, preexecution, runtime, staging,
raw-result, result-manifest, or registered diagnostic material.

## Nonclaims

The proof-only note must explicitly preserve these boundaries:

- universal \(D_m\ne0\) for every \(m\ge2\) is open;
- PC2 does not prove period-three separation in every degree;
- the quartic family and period-one/two blindness are not new;
- the result does not cover all quartic Hénon maps;
- no global \(P(4)=3\) is proved;
- no global conjugacy classification or multiplier-rigidity theorem is proved;
- global residues, quotient traces, dynatomic/formal-cycle methods, and
  low-period Hénon algebra are not claimed as new;
- bounded search supports no historical-priority or universal absence claim;
- no unstable/saddle multiplier, arithmetic height/finiteness, prime/zero,
  transfer/Fredholm, or Euler-product conclusion is claimed; and
- no finite diagnostic, historical check, or failed runtime is evidence for
  an all-\(m\) theorem.

## Handoff gate

The independent reviewer must verify at least:

1. all 20 matrix rows against the immutable proof and claims matrix;
2. the complete Step-9 transparency chain, especially (9.14), the
   distinguished coordinate, transfer flow, and \(j=0\) case;
3. Step 12 as two source-level derivations, with no runtime substitution;
4. Step 10 moment versus Step 13 multiplicity and the order of subtraction;
5. every provenance paragraph and forbidden registered statement;
6. exact nonclaims and bounded novelty roles;
7. the allowed-input and forbidden-input closure in
   `experiments/proof_only_manuscript_lock.json`; and
8. that no candidate import, scientific computation, patch, rerun, value
   recovery, manuscript, or finalization occurred during this redisposition.

Until that review passes, this package authorizes review only. It does not
authorize manuscript drafting or finalization.

