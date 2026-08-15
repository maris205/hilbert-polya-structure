# Independent Manuscript Review — Round 1

Review date: 2026-08-14 UTC  
Candidate: `cat_torsion_primitive_divisor_capacity_v1`  
Manuscript: *A Primitive-Divisor Audit of Prime-Order Torsion Periods for Hyperbolic Toral Automorphisms*  
Reviewer role: fresh independent mathematical, domain, reproducibility, and devil's-advocate reviewer  
Recommendation: **MINOR REVISION**  
Confidence: **5/5** for the internal mathematics and artifact audit; **4/5** for literature completeness because this review was intentionally offline  
Overall score: **90/100 (9.0/10)**

## Executive assessment

The scientific core passes.  I found no Critical or Major defect in the
uniform carrier theorem, the negative-trace parity conversion, the sharp
standard-cat classification, the torsion-order obstruction, or the frozen
one-shot evidence chain.  In particular, the manuscript correctly avoids
the false all-even index-
\(n\) shortcut for negative trace: odd requested periods use primitive
index \(2n\), periods divisible by four use index \(n\), and
\(n=2k\) with odd \(k\) uses index \(k=n/2\).  The small half-indices
\(7,9,11\) and the proof that the primitive prime is not two are exposed at
the point where they are needed.

The primitive-kernel lemma really gives exact, rather than merely dividing,
period.  The standard cat proof correctly separates primitive-divisor
exceptions from carrier exceptions and closes the latter as
\(\{1,6,12\}\); the modulo-five nilpotent calculation supplies twenty
period-ten points and two cycles.  The clock section also proves its stated
group-theoretic and topological facts and keeps raw labels, Birkhoff sums,
return-time normalization, and derivative monodromy distinct.

The remaining changes are bounded: correct one signed-eigenvalue notation,
strengthen the directly relevant ordinary-period literature bridge, and
reconcile one stale citation-ledger checkbox before freezing the revised
package.  None requires a new experiment, candidate execution, change to a
frozen result, or alteration of a core theorem.

## Review scope and immutable bindings

This was a read-only review of the bound source, PDF, source lock, proof
package, raw result, result manifest, official reports, citation ledger,
bibliography, figure package, and prior independent integrity reports.  I did
not run the candidate or test suite, compute a period above twelve, access a
network service, external prime table, generated prime target, or Riemann-zero
data, or modify a source, figure, result, code, or source-lock artifact.

The following live hashes reproduce the pre-review bindings:

| Role | SHA-256 |
|---|---|
| manuscript source | `072be061acbd4ef00ecc3220449a1f872c430200becdb4e127b706d09da36ee2` |
| pre-review PDF | `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8` |
| source lock | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` |
| proof package | `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af` |
| raw exact result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| final result manifest | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |
| independent result-integrity review | `5f544f637ccbe9e9f584cfdd41a3188ab76153670bd5d3cdbc881ea5cbf2229d` |
| independent plan/figure/citation review | `a5e2eab53b97765bee6cedc004f4e77a29c0647c5a0186c2cd8eda7bc8262655` |
| citation-verification ledger | `7c984ced5d1ac9a22b61795d080393f9e8c83dabe04e2f4b612560f04fbdf779` |
| bibliography | `f4567be30ef6b8d6e0bc1a3a8f6a294499221de51de4064e864cbbe448b79775` |
| figure manifest | `e292df2cd1d9d2c19675bc36cf30ed75e88e730fca17c7cd47420285be07fb2c` |

I independently reproduced all 14 non-self file hashes in the V2 result
manifest and the exact 11-entry final `results/` inventory.  The execution
JUnit is 21/21 pass at
`2a0844152eea6d9184d374a6e33c3c4be72fce8deb60296c77650027104348cc`;
the analyzer JUnit is 27/27 pass at
`fac25a2d332d68f6a2374b14f57d0f9dcacd5ea27c2c7581766b8c84d00499a0`.
The raw result, unique claim, terminal record, and manifest consistently
record one registered exact audit over \(1\le n\le12\), zero candidate
numerical runs, no candidate rerun, and empty computed-tail lists.

## Strengths

### S1. The negative-trace gap is genuinely repaired

The proof does not hide the sign conversion inside the imported theorem.  It
gives three exhaustive parity branches, makes the half-period failure mode
explicit, and handles characteristic two in the delicate half-index branch.

**Evidence Anchor**: `equation: manuscript.tex:247-330 — Table 1 and Theorem 3.3, including the 2n/n/k routing and p != 2 subargument`

### S2. Additive order and exact dynamical period remain separated

The kernel lemma uses determinant divisibility only to obtain a nonzero
kernel, then uses primitivity against every earlier determinant to exclude
all smaller returns.  The cycle count is derived only after exact period has
been established.

**Evidence Anchor**: `equation: manuscript.tex:182-205 — primitive-kernel lemma and (p^r-1)/n orbit partition`

### S3. The standard-cat boundary is complete and handles the nonprimitive case

The twelve-term ledger, modulo-two/three profiles, and the modulo-five
Jordan calculation jointly prove the iff statement.  The manuscript does
not infer carrier absence from primitive-divisor absence at period ten.

**Evidence Anchor**: `table: manuscript Table 2 and Theorem 4.2 — n=1,...,12 ledger, p=5 profile {2:4,10:20}, and exclusions at 1,6,12`

### S4. The obstruction is stated at the correct level

The clock realizes all additive orders and is locally unbounded on its dense
torsion domain.  The paper explicitly distinguishes a raw orbit label, a
normalized average, an unnormalized point-potential sum, and native
monodromy, and it does not promote any of them into a transfer, zeta,
quantum, or prime/zero claim.

**Evidence Anchor**: `equation: manuscript.tex:486-562 — Theorem 5.1 and the orbit-label/average/sum/monodromy comparison`

### S5. The theorem/computation firewall and release artifacts are unusually clear

The finite registered audit is used only for the frozen boundary and exact
profiles.  The infinite tail is explicitly theorem-derived.  Source, result,
figure, citation, and PDF bindings close without changing the one-shot raw
result.

**Evidence Anchor**: `dataset: manuscript.tex:579-635 plus result_manifest.json — n=1,...,12 only, empty tail, one run, manifest PASS`

## Critical findings

**None.**  No single defect invalidates a core claim or makes acceptance
impossible.

## Major findings

**None.**  No core theorem requires re-analysis, new evidence, or structural
rewriting.

## Minor findings

### M1. Use the spectral radius or absolute unstable multiplier for negative trace

**Problem**: The clock theorem is stated for every hyperbolic
\(A\in\mathrm{SL}_2(\mathbb Z)\), including \(\operatorname{tr}A<-2\),
but the proof later calls \(\alpha\) “the expanding eigenvalue” and writes
the unstable log-multiplier as \(n\log\alpha\).  In the negative-trace case
the eigenvalue of modulus greater than one is negative, so that real
logarithm is not the intended quantity.

**Evidence Anchor**: `text: manuscript.tex:550-552 — "Its unstable log-multiplier is n log alpha, where alpha is the expanding eigenvalue of A"`

**Why it matters**: The point-independence conclusion is correct, but the
displayed real logarithm is not uniformly defined on the theorem's full
trace-sign scope.

**Suggestion**: Define \(\rho(A)>1\) as the spectral radius and write the
logarithm of the modulus of the unstable multiplier as
\(n\log\rho(A)\).  Use the same notation anywhere the general, rather than
standard positive-trace, clock theorem is summarized.

**Severity**: Minor  
**Confidence**: 5/5 — core expertise in hyperbolic linear dynamics

### M2. Add the direct ordinary-period-set literature bridge

**Problem**: The introduction explicitly distinguishes the new
prime-additive-order constraint from unconstrained existence of period-
\(n\) points, but it does not cite the direct toral-automorphism period-set
literature already identified in the project's novelty audit.  The current
12-source bibliography gives strong prime-lattice and rational-lattice
context, yet this exact contrast is left implicit.

**Evidence Anchor**: `absence: Introduction and References — expected direct support for the ordinary period-set contrast; checked manuscript.tex:77-128, references.bib, and NOVELTY_AUDIT.md items 4 and 6`

**Why it matters**: This does not weaken the theorem, but a specialist reader
should be shown precisely what changes when additive prime order is imposed.

**Suggestion**: Add one bounded sentence and one or two already-verified
references, preferably Kannan--Subramania Pillai--Ali Akbar--Sankararao
(2011), *The Set of Periods of Periodic Points of a Toral Automorphism*, and/or
Seibt (2003), *A Period Formula for Torus Automorphisms*.  State that these
address ordinary period sets or rational-lattice period formulae, not the
cross-prime carrier theorem.  Re-run the citation-key closure after any
bibliography change.

**Severity**: Minor  
**Confidence**: 4/5 — direct sources are verified in the local novelty audit; no new online search was performed

### M3. Reconcile the citation ledger's remaining unchecked release item

**Problem**: The citation ledger's final checklist still leaves URL
re-resolution and bibliography compilation unchecked, while the subsequent
independent plan/figure/citation review and author pre-review audit report a
clean 12-item compiled bibliography.  The live manuscript indeed has 12
unique cited keys, the BibTeX file has exactly the same 12 entries, and the
BibTeX log has no warning, but the ledger status itself is stale.

**Evidence Anchor**: `text: CITATION_VERIFICATION.md final checklist — "Re-resolve all URLs and compile the bibliography when manuscript work is authorized"`

**Why it matters**: This is not a scientific gap; it is a release-state
ambiguity in an artifact the manuscript package treats as citation
authority.

**Suggestion**: After M2 is resolved, either mark the item complete with the
new compilation/re-resolution evidence or state explicitly which part was
not repeated and retain the verified cutoff.  Bind the revised ledger and
bibliography hashes in the post-revision integrity record.

**Severity**: Minor  
**Confidence**: 5/5 — direct artifact comparison

## Claim-by-claim verdict

| Claim surface | Verdict | Review note |
|---|---|---|
| General hyperbolic \(\mathrm{SL}_2(\mathbb Z)\), every \(n>12\) | PASS | Positive trace is a Flatters corollary; negative trace is independently and exhaustively converted by parity. |
| Primitive divisor to exact prime-order carrier | PASS | Every nonzero kernel vector has exact period; no splitting or semisimplicity assumption is used. |
| Standard cat iff \(n\notin\{1,6,12\}\) | PASS | Positive cases, support-prime exclusions, and period-ten Jordan repair close the classification. |
| \(\mathrm{Per}=\mathrm{Tor}\), all orders, local unboundedness | PASS | Group and coprime-perturbation arguments are correct. |
| Orbit sum versus raw label versus monodromy | PASS WITH M1 | Dependence claims are correct; replace the signed-eigenvalue logarithm by spectral-radius notation. |
| Novelty and related-work positioning | PASS WITH M2 | Safe verbs and nonclaims are appropriate; add the direct ordinary-period-set bridge. |
| One-shot exact evidence and hashes | PASS | Source/raw/manifest/report hashes reproduce; 21/21 and 27/27 reports parse cleanly; no external target or tail execution appears. |

## Build, typography, figures, and visual QA

I compiled a copied paper tree twice in an isolated temporary directory.
Both clean builds were byte-identical to each other and to the bound
pre-review PDF at SHA-256
`9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8`.
The document has 12 pages, 33/33 embedded and subset fonts, no raster image
objects, no unresolved citation/reference, and no LaTeX, BibTeX, overfull, or
underfull warning.

All 12 rendered pages were inspected.  The three figures, all compact data
tables, theorem statements, long claim map, hashes, and bibliography are
legible, uncropped, and free of overlap or corrupt glyphs.  Figures 1--3
preserve the intended semantic boundaries: theorem versus finite audit,
primitive divisor versus Jordan repair, and capacity versus specificity.

The ARS PDF-read preflight returned `UNAVAILABLE` solely because `pypdf` is
not installed; this was retained as an advisory rather than misreported as a
PASS.  `pdfinfo`, `pdftotext`, font/image inspection, two isolated builds,
and original-resolution page rendering independently succeeded.

## Dimension scores

These uncalibrated scores are ordinal quality judgments, not venue
acceptance probabilities.  The recommendation is controlled by the concrete
unresolved items above.

| Dimension | Score | Descriptor | Basis |
|---|---:|---|---|
| Originality | 72 | Adequate | Useful exact synthesis and negative-trace repair, deliberately low novelty. |
| Methodological rigor | 96 | Exceptional | Complete proofs, explicit edge cases, frozen one-shot exact audit. |
| Evidence sufficiency | 94 | Exceptional | Claim/evidence map, closed raw artifacts, independent result and figure gates. |
| Argument coherence | 94 | Exceptional | Clean arithmetic bridge, sharp boundary, then specificity obstruction. |
| Writing quality | 93 | Exceptional | Precise, restrained, visually polished; one notation correction remains. |
| Literature integration | 82 | Strong | Main collisions are cited; M2 would close the direct ordinary-period contrast. |
| Significance and impact | 78 | Strong | Valuable obstruction and exact technical note, not a broad new theory. |
| **Weighted average** | **90** | **Minor Revision pending bounded fixes** | No Critical/Major issue. |

## Required revision checklist

1. Replace the general signed-eigenvalue expression \(n\log\alpha\) by
   \(n\log\rho(A)\), explicitly as the logarithm of the unstable
   multiplier's modulus.
2. Add a short ordinary-period-set literature contrast using only locally
   verified sources; update and re-close citations if entries change.
3. Reconcile the citation ledger's last unchecked release item and refresh
   all manuscript/package hashes affected by the bounded revision.
4. Update pre-review lifecycle wording and filenames only at the proper
   finalization gate; do not create `paper_final.pdf` merely on the strength
   of this Round-1 report.

## Devil's-advocate conclusion

The strongest plausible counter-argument is that the manuscript packages a
largely classical primitive-divisor corollary and finite-lattice calculation
as a new paper.  The paper already answers this appropriately: it assigns
low novelty, attributes Flatters and classical cat-map arithmetic, avoids a
priority claim, and makes the audited negative conclusion part of the
contribution.  That counter-argument limits significance; it does not expose
a mathematical defect.  I found no unresolved Devil's-Advocate Critical
issue.

## Final verdict

**MINOR REVISION — scientific core and evidence chain pass.**  The three
required fixes are local and should be followed by a fresh hash-bound
Round-2 verification.  No candidate rerun, new experiment, tail scan,
prime/zero access, transfer/Fredholm construction, or scope expansion is
warranted.
