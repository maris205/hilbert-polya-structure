# Independent internal review — symmetry-only clock admission screen

**Screen ID:** `ASFS-SCOUT-20260919-SYM01`  
**Status reviewed:** `SYMMETRY-ONLY CLOCK UNIQUENESS REFUTED; NO NEW OWNER — STOP / FORK`  
**Disposition:** PASS for this bounded methodological conclusion; no mathematical revision requested.  
**Review type:** internal model review, not external peer review or formal verification.

## 1. Frozen scope and input binding

This review concerns the [screen card](../candidate-card.md) and the full
[manuscript](../paper.md). It does not admit a new dynamical owner, replace
the uniform owner of 276, or evaluate A0/A1/A2, T0–T3 or Route B.

- Original version-1 card SHA256:
  `4ab5c913594ae82e731c40151cb77b3f3756db5a73fee91630a03d8a550a052d`.
- Compared final manuscript SHA256:
  `c15456f3dde5dfe0fe2ad5e246157fcb002e7056784211cec8f54cc7e1c080cd`.
- The card subsequently received an administrative `Appended audit outcome`.
  The original bytes before that appended section, not the later outcome,
  are the frozen mathematical input. The complete appended card SHA256 is
  `d00f9b636c5b62b0ba514183ba7d5f7e472e7bbb7f562221dbb94ddeff93bc82`.

The source is the entire unchanged directed marked graph: every hub,
scan root, escape vertex, parallel edge and infinite path is retained.
The tested group is ALL directed incidence automorphisms, without an
assumption that numeric vertex names or port labels are fixed. U and W
remain different measured/time owners over the same source groupoid.

The bounded method follows the ARS freeze-first / three-checkpoint review
workflow. No numerical runs, orbit census, new weight family, full
automorphism classification, literature expansion or source modification
was used. Manuscript §5's three other scout lanes were not independently
audited in this review; their archival dispositions are not additional
mathematical evidence for the symmetry result.

## 2. Checkpoint 1 — independent raw-card derivation

This checkpoint was completed and communicated to root before reading
the manuscript. The raw-card derivation gave the following results.

1. **Hubs are fixed without preserved labels.** Counting marked edge
   identities, H_n is the unique vertex of outgoing degree n for each
   n≥2. Every other vertex has outgoing degree 1. Hence every incidence
   automorphism fixes every H_n.
2. **Port 0 is intrinsic.** At H_2 it is the unique self-loop. The other
   H_2 edge then fixes E_0, and the deterministic ray fixes all E_k.
   At H_n, n≥3, port 0 is the unique outgoing edge whose target has
   outgoing degree 1 and is not E_0. Other targets are hubs or E_0.
   This covers composites as well as primes and does not require fixing
   or classifying all late scan roots.
3. **Both positive laws are invariant.** U assigns reciprocal outgoing
   degree. W assigns 1/2 to the intrinsically fixed scan edge and equal
   probabilities 1/[2(n−1)] to the remaining H_n edges. Deterministic
   edges have probability 1. All probabilities are preserved by every
   incidence automorphism, even when parallel marks permute.
4. **Root qualification.** Writing Φ_a for the edgewise path action,
   the rooted probability laws satisfy `(Φ_a)_* μ_v = μ_(av)`.
   A moved scan-root law is not individually fixed as a measure on X.
   The full countable coproduct measure IS invariant because each root
   has mass 1. Cylinder uniqueness is applicable root by root, with a
   countable finite-measure cover; infinite total mass causes no gap.
5. **The induced action belongs to each existing owner.** Φ_a is a
   cylinder homeomorphism commuting with the shift. It maps
   `(ξ,k,η)` to `(Φ_a ξ,k,Φ_a η)`, preserves prefix bisections and all
   groupoid operations, and does not require the shift to be onto.
   For an arrow `βζ → αζ`, the IMAGE derivative is
   `J=P_α/P_β`, so `c=−log P_α+log P_β`. Prefix products are invariant;
   the clock is therefore invariant separately for U and W. The lifts
   `(ξ,u)→(Φ_a ξ,u)` and `(g,u)→(ag,u)` preserve the real extension and
   commute with its time translations. No automorphism arrows or new
   quotient have been added.
6. **The decisive clock comparison is on unchanged packets.** A prime
   scan C_p has primitive edge length p−1 (the p=2 self-loop included).
   Its turn probability is 1/p under U and 1/2 under W. Hence its least
   positive time is log p or log 2, respectively, with all repetitions
   retained. At p=2 they agree; p=3 already separates them. Distinct
   prime marked tails do not merge just because W gives equal times.
   The H_3 scan cylinder also has different positive measures, 1/3
   and 1/2, so this is not solely a null-path change of clock values.
7. **Returnability supplies the declared general obstruction.** For a
   fixed vertex v, the outgoing edges admitting a finite return to v
   form an invariant subset: transport a return path by a and use its
   inverse for the converse. Self-loops allow an empty continuation.
   A nonempty proper subset obstructs transitivity on outgoing edges.
   At a prime hub only port 0 returns. At a composite hub every port
   is nonreturning; this lemma alone does not identify its scan port.
   The independent incidence argument in item 2 already covers it.

The raw verdict was that two distinct positive, equally root-normalized,
full-Aut-invariant laws defeat symmetry-only clock uniqueness. No new
family or exhaustive group computation is needed for that counterexample.

## 3. Checkpoint 2 — full manuscript comparison

The manuscript was read in full only after checkpoint 1 was completed.
Its actual SHA matches the binding in §1. No mathematical discrepancy
with the independent derivation was found.

- Proposition 1 uses the equivalent target-degree proof: S_(n,2) has
  incoming degree exactly 1, whereas E_0 has infinitely many incoming
  marked edges. This is correct for every retained H_n, n≥3, and its
  H_2 self-loop argument handles the boundary case separately.
- Proposition 2 asserts global coproduct measure invariance, using
  preserved edge weights and equal root masses. It does not assert that
  every moved rooted probability law is individually invariant.
- The IMAGE orientation, logarithmic sign, prefix-refinement cancellation,
  groupoid action and real-extension action are consistent. On a prefix
  bisection the stated derivative is a continuous version of the Borel
  derivative. Strictly positive cylinder measures give full support;
  null periodic paths do not permit changing a continuous version there
  arbitrarily while preserving its values almost everywhere.
- Corollary 3 uses the same full marked graph and primitive packet
  convention, not a selected cycle subsystem. All transient prefixes
  and phases cancel from closed clocks. The comparison retains separate
  U/W ownership and does not confuse equal lengths with equal packets.
- The general test in §4 is only a necessary obstruction to an indicated
  transitivity argument. The manuscript does not use it to classify
  all automorphisms or to decide every possible arithmetic symmetry.
- The conclusion and disclosure preserve the positive engineering result
  of 276, reject only the stated symmetry-only uniqueness argument, and
  issue no new owner-level or formal Route coordinates.

## 4. Checkpoint 3 — final adverse review

The strongest apparent escape routes do not invalidate this scoped result.

**Unlabelled or parallel-edge symmetries:** numeric labels were not fixed
by assumption; hub fixing and scan-port fixing follow from incidence.
Possible permutations of the other marks preserve both frozen laws.

**Moving roots or non-surjectivity of the shift:** neither defeats the
coproduct invariance or the induced groupoid action. Rooted covariance is
the correct intermediate statement; a graph automorphism is a bijection
of the full path space even when the shift itself is not onto.

**Null cycles or an alternative clock representative:** the full-support
continuous prefix version fixes the stated clock at the null recurrent
paths. Moreover U and W already disagree on a positive cylinder. This
is not an arbitrary reassignment of an almost-everywhere clock.

**A stronger meaning of arithmetic naturalness:** a further specified
compatibility or normalization principle might distinguish U and W.
It is not supplied by invariance under the graph automorphisms tested
here. The present counterexample proves no universal naturalness no-go,
selects no preferred alternative weight, and refutes no broader category.

No blocking or nonblocking correction to the reviewed mathematical
manuscript is requested. The final disposition is **STOP / FORK for the
symmetry-only uniqueness argument; no new owner**. T3, geometric lifts,
coarse quotient topology and Route B remain outside this review.

The reviewer and root used the same inherited model and shared project
context; a bounded auxiliary incidence/weight check also used that model.
The raw-card derivation preceded manuscript reading, but the subsequent
comparison and communicated findings were not blind. This process can
catch local errors; it is not external peer review, formal verification
or evidence of independent error probabilities. ARS supplied the staged
scope/comparison/adverse-check discipline, not mathematical authority.
