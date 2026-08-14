# HCS-C56 implementation checklist

Status: **DOCS_FINAL_NO_MORE_EDITS; FINAL READ-ONLY AUDIT PASS; project
RELEASE_FROZEN.**

Checked boxes record completed written, certified prefreeze, official-build,
final read-only audit, implementation-commit, and frozen-release work.

## A. Ownership and source identity

- [x] Create a project separate from HCS-C55.
- [x] Restrict the documentation lane to root formal documents, paper
  sources, and the root Route record.
- [x] Record that code, results, top-level registries, and codex_prompt are
  outside this lane's ownership.
- [x] Record the exact layered C55 release contract.
- [x] Resolve the authoritative C55 files from committed objects.
- [x] Verify live bytes against those committed objects.
- [x] Replay the frozen C55 checker before importing any coefficient.
- [x] Reconstruct the ordered primitive 20-row cubic and check degree,
  uniqueness, content, and sign convention.
- [x] Store the final C55 source-lock tuple in a fail-closed C56 payload.

## B. Global surface and Fano scheme

- [x] Define \(F_1(Y)\) as the zero scheme of the section of
  \(\operatorname{Sym}^3(\mathcal S^\vee)\) on
  \(\operatorname{Gr}(2,4)\).
- [x] Separate the total count of 27 from the simple-zero input.
- [x] Lock Kass--Wickelgren Theorem 2/Corollaries 53--54 to their exact
  roles.
- [x] Rebuild the imported surface and independently recheck smoothness.
- [x] Derive all six standard Grassmann chart systems from the imported
  sparse cubic.
- [x] Verify that the global line scheme is finite étale of rank 27.

## C. Main-chart exact algebra

- [x] Store a primitive degree-27 eliminant \(g(d)\).
- [x] Store primitive linear back-substitutions for \(a,b,c\), with nonzero
  leading constants.
- [x] Substitute the back-solutions into all four line equations.
- [x] Clear denominators canonically and recompute four zero remainders.
- [x] Prove that the induced map into \(F_1(Y)\cap U_{01}\) is a closed
  immersion.
- [x] Write the required global step: finite étaleness makes
  \(F_1(Y)\cap U_{01}\) open-and-closed in \(F_1(Y)\).
- [x] Use equal finite rank 27 to certify equality with the global Fano
  scheme.
- [x] Independently certify the five complementary-chart unit ideals.

## D. Irreducibility and field distinction

- [x] Write the complete subset-sum lemma for modular factor degrees.
- [x] At each selected prime, verify good reduction and survival of the
  leading coefficient.
- [x] Store all monic factors and multiplicities and multiply them back.
- [x] Recompute \(\gcd(\bar g,\bar g')=1\).
- [x] Recompute all factor-degree subset-sum sets.
- [x] Require their intersection to be exactly \(\{0,27\}\).
- [x] Conclude irreducibility of \(g\), hence that
  \(E=\mathbf Q[d]/(g)\) is a degree-27 field.
- [x] Keep \(E\) distinct from its normal/splitting closure \(K\).
- [x] Verify directly that \(K\) is the least normal field defining all 27
  lines.

## E. Weyl group and Picard lattice

- [x] Audit Elsenhans--Jahnel Fact 3, Remarks 4--5, Lemma 8, Algorithm 10,
  and Remarks 11--13.
- [x] Lock the parity convention to the determinant in the \(E_6\)
  reflection representation.
- [x] Forbid ordinary \(S_{27}\) sign as a substitute; every element of
  \(W(E_6)\) acts evenly on the 27 lines.
- [x] Construct the seven-dimensional Picard lattice, canonical class, six
  simple roots, reflections, and 27 line classes.
- [x] Verify preservation of the form, canonical class, line set, and
  incidence.
- [x] Enumerate 51840 group elements and the 25920-element determinant
  kernel \(U\).
- [x] Verify transitivity on the 27 lines.
- [x] Enumerate every element of cycle type \((2,5,5,5,10)\): require 5184
  total, 0 inside \(U\), and 5184 outside \(U\).
- [x] Apply Elsenhans--Jahnel Lemma 8 only after irreducibility and an
  order-five witness are certified.
- [x] Compute the fixed subspace of the Picard representation and require
  dimension one.
- [x] State the Hochschild--Serre conclusion only after tensoring with
  \(\mathbf Q\), with torsion cokernel rather than integral surjectivity.

## F. Independent verification

- [x] Use a checker that imports no producer module.
- [x] Rebuild the C55 source, cubic, chart equations, and direct remainders.
- [x] Rebuild complete modular factors, gcds, degree sets, and subset sums.
- [x] Rebuild the Picard lattice and Weyl group independently.
- [x] Derive every theorem boolean from semantic data.
- [x] Compare the entire canonical payload and reject unknown or missing
  fields.
- [x] Reject floats, noncanonical integers, duplicate keys, booleans in
  integer slots, optimized execution, and oversized inputs.

## G. Adversarial and runner gates

- [x] Classify every scalar leaf as central semantic, independently derived,
  or chronology-only.
- [x] Mutate every scalar leaf, rebind exposed hashes, and require semantic
  rejection where applicable.
- [x] Add targeted cold-process mutations for source, chart, factors,
  parity, group counts, fixed rank, and theorem booleans.
- [x] Test rollback after every promotion move with both pre-existing and
  absent targets.
- [x] Prove default check mode preserves bytes and nanosecond mtimes.
- [x] Verify cwd independence and deterministic output.

## H. Claim firewalls

- [x] No rational point on \(Y\) is claimed.
- [x] No \(\mathbf Q\)-rationality or stable-rationality claim is made.
- [x] No Hasse-principle or Brauer--Manin conclusion is made.
- [x] No motive, VHS, Calabi--Yau, automorphy, or zeta-function conclusion is
  made.
- [x] No theorem for generic Yukawa or Hénon cubic surfaces is claimed.
- [x] No global novelty claim is inferred from the bounded search.
- [x] No temporary architecture, source download, or audit hash is release
  authority.

## I. Documentation, paper, and provenance

- [x] Complete the exact prefreeze theorem, derivation, proof, methodology,
  experiment plan, and primary-source audit.
- [x] Record the historical prefreeze checkpoint before commits, the official
  build, or the release-wide full successor existed.
- [x] Replace conditional exact premises after the certified handoff.
- [x] Draft the paper from the certified formal package.
- [x] Run the source-level independent semantic, source, and novelty audit.
- [x] Stabilize paper sources before any official build.
- [x] Run the official clean build and audit log, destinations, fonts, text,
  and page visuals.
- [x] Generate main.txt and a compilation report.
- [x] Backfill exact paper, report, and Route provenance; bind implementation
  commit `b32402f1dd276a2684d3e849dae26150ebb595e1`, keep the provenance
  commit null/external, and bind the external self-excluding full-project
  manifest without embedding its digest.
- [x] Run the final read-only release audit.
- [x] Close its final-audit gate at project `RELEASE_FROZEN` while retaining
  documentation `DOCS_FINAL_NO_MORE_EDITS` and machine evidence
  `PREFREEZE_CODE_RESULTS_PASS`.  The separately verified full-project
  manifest is the release-wide integrity ledger; the provenance commit remains
  null/external.
