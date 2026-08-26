# Papers 14--18 batch design lock

Status: **USER-CONFIRMED / PHASE 1 COMPLETE / PROTOCOL FREEZE AUTHORIZED**  
Version: `P14-18-BATCH-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Route B: false  
Git/public release: false

## 1. User authorization and exact scope

The user accepted the recommended five-paper agenda with the message

> 按推荐方案继续

This confirms exactly five new projects, numbered Papers 14--18.  It does
not authorize Git operations, public synchronization, submission, or a
claim that any proposed theorem is already true.  It authorizes Phase-1
protocol freezing and bounded proof/source fail-fast work.

The publication rule is fail-closed:

- at most one of the five projects may finish as a Technical Note;
- every other project requires an independent `STANDALONE_PASS`;
- a project that reduces to a standard lemma plus companion substitution is
  merged, stopped, or replaced rather than padded into a paper.

## 2. Active upstream evidence tuple

The following current bytes are the owner and nonredundancy baseline:

```text
P9 manuscript
  24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
P9 proof audit
  c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8
P10 manuscript
  27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315
P10 proof audit
  efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a
P11 manuscript
  eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002
P11 proof audit
  03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28
P12 manuscript
  c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163
P12 proof audit
  c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab
P13 manuscript
  c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701
P13 proof audit
  e2f8fb8df4f3418fb3ff0fb60c87f9c7a4ae26cc7470c8c14aec3f86f6df1a63
Papers 9--13 final batch audit
  6aa915a9e85153957b269448ba23b56716c4f64d18e6b3c85f904d73b0001aea
```

These hashes are premise receipts, not citation substitutes.  Papers 1--8
remain mandatory whenever a proposed claim uses their source, trace,
operator, or no-splice boundaries.

## 3. Five registered projects

### Paper 14 — global periodic-locus topology

Working directory: `papers/14-global-periodic-topology/`.

Compute, from the actual full rational-Witt suspension, the inherited
topology on the union of fixed-prime periodic packets.  The first gate is the
two-prime subspace.  Only after that gate may the project classify the global
specialization preorder and Kolmogorov quotient.

### Paper 15 — mixed prime-clock standardization and rigidity

Working directory: `papers/15-mixed-clock-rigidity/`.

Extend the Paper-12 same-carrier construction from one common lattice to a
family of cocompact lattices.  Classify strict and globally scaled
equivariant isomorphisms, then test the prime-clock family
`L_p=log(p)`.  The substantive gate is global scaling rigidity, not a
wreath-product formula.

### Paper 16 — Arveson reconstruction of the prime clock

Working directory: `papers/16-arveson-prime-recovery/`.

On the Paper-15 standardized owner, recover orbit components as minimal
nonzero invariant ideals and recover each clock from its restricted Arveson
spectrum.  External prime labels may be used only to state the arithmetic
application after the unlabeled reconstruction theorem.

### Paper 17 — open-groupoid topos and quantale interfaces

Working directory: `papers/17-open-groupoid-interfaces/`.

Test the actual indiscrete action groupoid in frameworks that genuinely
admit open non-Hausdorff groupoids.  The candidate center is an exact
comparison of equivariant-sheaf/topos and open-quantal-frame information
with the standard-circle owner.  The two interfaces remain one paper; they
may not be split into two routine notes.

### Paper 18 — packet Haar descent and same-map trace dichotomy

Working directory: `papers/18-packet-haar-trace/`.

Classify the coordinate transitions used to describe the fixed-prime packet
by `U_p/H_p` and determine whether normalized Haar descends without a hidden
choice.  A positive branch must construct the measured owner,
disintegration, representation, and trace on one named map.  A negative
branch must classify the descent obstruction.  No determinant is permitted
at this stage.

## 4. Dependency graph

```text
P14 global source topology --------> P18 Haar descent / trace dichotomy

P15 mixed marked rigidity ---------> P16 Arveson clock reconstruction

P17 open-groupoid interfaces        (independent exact-domain branch)
```

P18 may cite P15--P16 only as comparisons.  It may not borrow their standard
topology or analytic invariant.  P16 may not claim an actual-topology
invariant: its owner is the explicitly standardized Paper-15 record.

## 5. Common owner firewall

1. Actual, bare, abstract compact-quotient, standardized, copied, proxy, and
   condensed/localic owners are distinct records.
2. Paper 9 is the current owner of the actual fixed-prime indiscrete packet,
   orbit, and quotient topology.  Superseded Paper-8 actual-Hausdorff
   attribution may not be revived.
3. Paper 10 owns collapse through separated observables and the trivial
   actual Borel algebra.  Replacing the codomain name does not create a new
   interface.
4. Paper 11 owns the action-blind global-QC shadow.  Any new analytic functor
   must distinguish the rational-Witt action from a declared trivial or
   nontransitive control.
5. Paper 12 owns common-lattice standardization and the degree-one invariant
   diagonal.  A componentwise bar-complex or wreath calculation is not a new
   center.
6. Paper 13 owns real-line gauge collapse and the generic constant-diagonal
   completion/corona lemma.  Another generic `c0`-sum instance is
   `NOTE_OR_MERGE`.
7. A scalar, trace, determinant, operator, topology, or measure coordinate
   cannot be donated from a different owner.
8. Target Euler coefficients, Riemann zeros, or desired prime weights cannot
   be used to select a measure, regularization, operator, or normalization.

## 6. Mandatory fail-fast and standalone gates

| Paper | Fail-fast gate | Standalone-bearing delta |
|---|---|---|
| 14 | exact topology of `Gamma_p union Gamma_q` is source-decidable | cross-prime closure/specialization theorem absent from P9--P10 |
| 15 | mixed-lattice category and scaled variance are correctly typed | prime-clock global scaling rigidity; routine automorphism algebra is insufficient |
| 16 | component ideals and restricted Arveson spectra are intrinsic | unlabeled recovery of every `L` and the fixed-prime clock |
| 17 | all cited frameworks accept the exact open non-Hausdorff groupoid | joint topos/quantale theorem plus actual-vs-standard comparison |
| 18 | auxiliary coordinate changes form an exact auditable class | choice-independent descent and same-map trace, or a complete canonicality obstruction |

If Paper 14 is source-underdetermined, it records that exact result and P18
cannot treat a tagged coproduct as the source-global periodic locus.  If
Paper 15 fails, Paper 16 is blocked.  If Paper 17 reduces to ordinary sheaves
on an indiscrete space without a substantive equivariant comparison, it is
the sole allowed Technical Note at most.  If Paper 18 cannot close coordinate
transitions, its trace branch is false rather than pending by assumption.

## 7. Evidence, computation, and review policy

- Primary or official sources are mandatory for mathematical framework and
  current-source claims.  Search-negative statements use only
  `NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH`.
- Source PDFs, if later retained for audit, remain under `notes/sources/` and
  are excluded from any public payload.
- Deterministic controls are designed only after the symbolic theorem and
  owner/domain review pass.  Controls never prove an infinite theorem.
- Each protocol requires independent methodology, devil/domain, and source
  review before proof authorization.
- Each final proof requires independent mathematical and standalone review.
- Route A evaluates only proved, owner-typed results.  Route B remains false
  for every project unless a later versioned gate explicitly reopens it.
- Manuscript, release, Git, archive, and public synchronization remain false
  until their downstream gates are separately satisfied.

## 8. Interaction and revision budget

The batch uses one user checkpoint at Phase 1 (now closed), one only if a
project must be replaced, and one final five-paper handoff.  Each paper is
limited to two substantive protocol/proof repair cycles and three purely
integrity/typesetting relocks.  Exceeding a cap requires a recorded scope
reduction rather than silent iteration.

No monetary or exact token estimate is asserted because the execution
environment exposes neither an invoice rate nor a reliable future token
meter.  The qualitative budget is five full theoretical-paper pipelines,
with proof, bounded source audit, deterministic controls where meaningful,
Route evaluation, bilingual abstract, PDF build, citation audit, independent
peer review, and release hold.
