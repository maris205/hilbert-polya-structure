# Independent devil's-advocate handoff

## Requested decision

Independently return exactly one of:

```text
DA_ACCEPT_PREAUTHORITY
DA_ACCEPT_WITH_MINOR_REPAIRS
DA_HOLD_MAJOR
DA_REJECT_DUPLICATE_OR_FALSE
```

Do not authorize authority integration. A positive DA decision is necessary
but not sufficient; root governance remains separate.

## Highest-risk issues

1. **Novelty ceiling.** Source proximality is explicitly known, and every
   later step is elementary. Test whether even the source-specific typed
   closure is already explicit in primary literature.
2. **Factor quantifiers.** Verify compactness, metrizability, surjectivity,
   continuity, full \(\mathbb Z\)-equivariance, and homeomorphism assumptions.
3. **CRT quantifiers.** Check that fresh distinct primes can be assigned to
   every point-coordinate pair and that each missing residue forces a zero.
4. **Periodic separation.** Check both another-fixed-point and least-period
   greater-than-one cases.
5. **Primitive typing.** Ensure traversals \(z^r\) are never counted as new
   primitive atoms.
6. **Operator ownership.** Ensure \([1]\) is described only as a periodic-core
   ledger realization.
7. **Retrospective selection.** Recompute the C02/C03/C05 rule and reject any
   prospective or outcome-independent interpretation.
8. **Route strictness.** Validate the exact live v0.2 keys, statuses, tuple,
   and every artifact path relative to the declared `preauthority` base.

## Mandatory proof replay

Reprove without relying on the package's conclusion:

1. \(X_{\rm sf}\) is compact and shift invariant.
2. The pair-window CRT system is solvable for every pair and every \(L\).
3. Agreement on larger central windows implies product-metric convergence.
4. A continuous factor of a compact proximal system is proximal.
5. A proximal system containing a fixed point has no other periodic point.
6. The factor fixed counts are exactly one for every iterate.
7. The Artin--Mazur exponential and the \([1]\) determinant both give
   \(1-z\) after inversion.

One lawful factor with a nontrivial periodic point rejects the main theorem.

## Mandatory controls

- For arbitrary finite \(P_0\), verify the point supported on
  \(1+Q\mathbb Z\), \(Q=\prod_{p\in P_0}p^2\), including its least period,
  every missing-residue condition, and the empty-set case. Then verify
  \((0111)^{\mathbb Z}\) for the modulus-four approximant.
- Verify the point factor.
- Verify that a product with an external periodic system changes the source
  and is an extension.
- Verify Paper 3's warning that aperiodicity alone is insufficient.
- Verify that a changed aperiodic/measure zeta is not Artin--Mazur repair.

## Literature collision tasks

Inspect at minimum:

- Sarnak's squarefree-flow theorem;
- Bartnicka--Kasjan--Kułaga-Przymus--Lemańczyk on proximality;
- Kasjan--Keller--Lemańczyk on the window view;
- Gundlach--Klüners v2 on factor systems of power-free admissible shifts;
- references cited by those sources for factors or unique minimal systems.

Search the exact combination `squarefree admissible shift + every factor +
periodic point/fixed point/Artin-Mazur`. If the exact theorem is published,
apply `STOP_DUPLICATE` even though the local proof is correct.

## Integrity replay

1. Verify every line of `SOURCE_HASHES.sha256` through the declared portable
   ID resolver.
2. Verify every immutable hash in `RESEARCH_LOCK.json`.
3. Verify `SHA256SUMS.txt` against the package.
4. Confirm that both manifests are C-sorted, unique, newline terminated, and
   self-excluding.
5. Confirm no host-absolute path or trailing whitespace occurs.
6. Confirm all Route artifact paths exist relative to
   `papers/43-squarefree-factor-periodic-rigidity/preauthority`.
7. Confirm P39 91/91 and the P40--P42 seals without treating them as rankings.

## Expected Route decision

```text
candidate_id = SD-C45 proposed
tuple = (A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)
overall = ROUTE_A_REJECTED
route_b_invocation_allowed = false
```

The DA should hold the package if any schema label, evidence status, artifact
path, or overall implication is inconsistent with live Route-A v0.2.

## Reviewer independence note

Cross-model review transport was unavailable to the Phase-1 worker, and all
collaboration slots were occupied during research. This handoff is therefore
the first required independent adversarial pass for Paper 43.
