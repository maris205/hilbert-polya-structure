# Independent Manuscript Review — Round 2

Review date: 2026-08-15 UTC  
Candidate: `cat_centralizer_cyclic_torsor_v1`  
Manuscript: *A Centralizer-Quotient Audit for Cat-Map Torsion Shells*  
Reviewer role: fresh independent Round-2 manuscript reviewer for mathematics,
claim/evidence discipline, citations, scope, provenance, reproducibility, and
publication readiness  
Verdict: **PASS**  
Disposition: **MAY_FINALIZE**  
Finding inventory: **CRITICAL=0 / MAJOR=0 / MINOR=0**  
Confidence: **5/5** for mathematics, no-change closure, and local artifact
integrity; **4/5** for literature completeness because this review was
intentionally offline  
Overall score: **90/100 (9.0/10)**

## Executive decision

The exact unchanged manuscript passes fresh independent Round-2 review.  The
Round-1 review accepted the manuscript with zero Critical, Major, or Minor
finding; the no-change response correctly preserved the accepted bytes; and
the Round-1 integrity record accurately binds that closure.  I independently
re-audited the full argument rather than treating Round 1 as scientific
authority.  I found no mathematical error, unsupported inference, evidence
leakage, citation defect, scope overreach, anonymity failure, build regression,
or visual defect.

The main theorem is correct over every residue ring, including the composite,
binary, and ramified-five cases.  The full local centralizer acts transitively
on the cyclic-vector locus because that locus is its exact torsor; since the
cat matrix lies in the acting group, the induced coarse quotient dynamics is
the identity on one point.  Restricting to determinant one retains exactly the
norm-image classes but still leaves identity dynamics.  Prime-shell and
reversing strata are correctly separated from the cyclic torsor, and CRT
shows that the one-class full cyclic quotient is not prime-specific.  The
manuscript therefore supports its narrow negative decision: the external
substitution $z=q^{-s}$ supplies a modulus label, not an intrinsic return
time of either coarse quotient.

Two fresh isolated builds reproduced the frozen 15-page revision PDF byte for
byte, with identical terminal logs, zero substantive warning, embedded fonts,
vector figures, and a clean page-by-page visual audit.  There is no residual
scientific or editorial blocker.  Final integrity may bind and finalize the
exact source and PDF reviewed here.  This review does not itself perform
finalization, create `paper_final.pdf`, mutate pipeline state, or authorize a
silent substitution of changed bytes.

## Exact Round-2 bindings

Every principal identity supplied for this round was independently recomputed:

| Object | SHA-256 | Round-2 result |
|---|---|---|
| Round-1 independent review | `bb1bdfb379062d2fe11245568ca3f6a97845456004119d3954c17dd917828c24` | PASS; exact verdict `ACCEPT`, findings 0/0/0 |
| Round-1 no-change response | `b3c4d6ecea0d5bc165bcb50fbb240ffede2d44804cd32dd9b66d487b93d6d561` | PASS |
| Round-1 no-change integrity record | `af4404f0606fdd2c8efc2c7d19eb1f89ed2b8298eaa26fc861faceb068c14364` | PASS |
| unchanged `paper/manuscript.tex` | `65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6` | PASS |
| `paper/paper_round1_revision.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` | PASS; 15 pages |
| live `paper/manuscript.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` | PASS; byte-identical |
| immutable `paper/paper_pre_review.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` | PASS; byte-identical |
| `paper/PAPER_CONFIGURATION.md` | `26ef0b765d9be6b9443ea19bb258de005d2fe1f8b6c1a63fcf7ef5a667915847` | PASS |
| pre-Round-2 `paper/PIPELINE_STATE.json` | `4929915d6fb610aceed1db76d31334a4a72542ebe1fb00da43ae84674866a8ee` | PASS; `READY_FOR_INDEPENDENT_ROUND2` |

The manuscript-support files are also unchanged: `math_commands.tex` is
`1484c2da170d49053741bb6d843fbf561a99439f537f5e760dbc2c843658dd6f`,
`references.bib` is
`1ccce7ade3079ca995f00058f4811bdd02a9062d8038b27be2f967f480fe8699`,
and `build.sh` is
`29bd4f55a6dd867f73a3afdad5f49d74ee0fdc0dff023473527e83ea22b0bb01`.
The claim, experiment, figure, plagiarism, and pre-review integrity artifacts
retain their recorded hashes.  `paper_final.pdf` was absent throughout this
review.

## Independence and Round-1 no-change provenance

I previously performed the independent result-integrity audit for the frozen
registered result package, but I had not reviewed this manuscript, its
Round-1 report, or its response before this task.  I did not author or revise
the manuscript, proof package, figures, bibliography, Round-1 review,
Round-1 response, or lifecycle records.  This Round-2 review is therefore a
fresh manuscript assessment, while transparently reusing the separately
identified result-integrity authority rather than pretending to be a second
result reviewer.

Round 1 requires no finding-by-finding repair: its exact inventory is zero
Critical, zero Major, and zero Minor finding.  Its three editorial
observations are explicitly below the finding threshold, and its two
questions concern future release metadata rather than the accepted scientific
bytes.  The author-side response correctly chose no change instead of altering
a byte-specific accepted package.  Direct comparison now confirms:

- the source remains at the exact Round-1 digest;
- the live, pre-review, and Round-1-revision PDFs are identical;
- the response and integrity record consistently state no change and no
  finalization;
- the pipeline remains at its declared pre-Round-2 state; and
- no `paper_final.pdf` has been created.

There is consequently no unaddressed Round-1 item, no undocumented adjustment,
and no no-change provenance discrepancy.  Under the re-review protocol, the
Round-1 finding set is vacuously closed and the independent regression below
supports the present `PASS` disposition.

## Fresh mathematical audit

### Universal centralizer and cyclic torsor

For

\[
 A=\begin{pmatrix}2&1\\1&1\end{pmatrix},
 \qquad P=[e_1,Ae_1]=\begin{pmatrix}1&2\\0&1\end{pmatrix},
\]

the determinant of $P$ is one over every $R_q=\mathbb Z/q\mathbb Z$.
Thus $(e_1,Ae_1)$ is a universal cyclic basis, including over nonreduced
composite rings.  A matrix commuting with $A$ is determined by its action on
that basis and is exactly $aI+bA$.  Invertibility is equivalent to
$aI+bA\in R_q[A]^\times$, so the full centralizer is the unit group
$C_q=R_q[A]^\times$.

For $U\in C_q$,
$[Ue_1,AUe_1]=U[e_1,Ae_1]$.  Conversely, a cyclic vector $v$ determines
the unique commuter $U$ satisfying $Ue_1=v$, and its cyclicity makes $U$
invertible.  Hence $U\mapsto Ue_1$ is a free transitive action of $C_q$ on
$CV_q$.  Cyclic vectors are unimodular and therefore have exact additive
order $q$, so $CV_q\subseteq E_q$.  No field-only division or unstated
semisimplicity enters the proof.

### Source orbits and the two coarse quotient clocks

Under the torsor identification, the source action of $A$ is multiplication
by $A\in C_q$.  Every cyclic source orbit therefore has exact length
$\operatorname{ord}_q(A)$, and the orbit set is
$C_q/\langle A\rangle$.  This correctly preserves the source orbit ledger
before any centralizer quotient is taken.

The full $C_q$-quotient of $CV_q$ is one class.  More importantly,
$A\in C_q^1\subseteq C_q$, so the map induced by $A$ on both the full and
determinant-one quotient is the identity.  Their native primitive period is
one.  The formal full-quotient factor is therefore $(1-z)^{-1}$, while the
replacement $z=q^{-s}$ or the assignment of length $\log q$ is external
specialization.  The paper never identifies that external label with a
source return time.

### Determinant-one quotient and the local norm image

The quadratic algebra relation $A^2-3A+I=0$ gives

\[
 \det(aI+bA)=a^2+3ab+b^2=N_q(a+bT).
\]

Thus $C_q^1=\ker N_q$.  The covariance
$\Delta(Dv)=\det(D)\Delta(v)$ and the torsor equality show that two cyclic
vectors are in the same $C_q^1$-orbit exactly when their determinant/norm
labels agree.  Hence $CV_q/C_q^1\cong\operatorname{im}N_q$, with identity
dynamics on every class.

The local norm computation is complete.  At split and inert odd primes away
from five, and at the unramified binary prime, the norm on units is
surjective through all prime-power lifts.  At five, writing
$\pi=2T-3$ gives $\pi^2=5$; the unit norm image is exactly the subgroup
whose residue is a square, and scalar square roots supply the converse.
Chinese remaindering therefore yields

\[
 |\operatorname{im}N_q|=
 \begin{cases}
   \varphi(q),&5\nmid q,\\
   \varphi(q)/2,&5\mid q.
 \end{cases}
\]

This is the exact symplectic multiplicity boundary claimed in the paper; it
does not restore a nontrivial quotient clock.

### Prime-shell, reversal, and composite boundaries

For prime $p$, the noncyclic part of the complete shell is the nonzero zero
locus of $\Delta_p(x,y)=x^2-xy-y^2$, whose discriminant is five.  It is
empty at the inert controls $p=2,3,7$, consists of two eigenlines at the
split control $p=11$, and is one ramified eigenline at $p=5$.  The full
centralizer therefore has respectively 1, 3, and 2 full-shell strata in the
inert/binary, split, and ramified cases.

The displayed reversor $J$ satisfies $JAJ^{-1}=A^{-1}$.  It exchanges the
two split eigenlines and preserves the ramified line, giving the frozen prime
reversing counts $(1,1,2,1,2)$ for $q=2,3,5,7,11$.  The paper explicitly
limits this claim to the group generated by the centralizer and a reversor
for $A^{\pm1}$; it does not claim a classification of all power normalizers.

For general composite $q$, cyclicity is a local unit condition and the
counts multiply under CRT.  The exact-order shell has Jordan-totient size,
the cyclic locus has the stated prime-local lift product, and its quotient by
the full centralizer remains one class for every $q$.  The predeclared
composites (4,6,9,10) therefore demonstrate the mechanism's
non-specificity without being used to prove the all-$q$ theorem.

### Claim-firewall receipt

| Claim family | Independent Round-2 check | Status |
|---|---|---|
| C1: commutant | universal cyclic basis; every commuter is $aI+bA$ | PASS |
| C2: torsor and exact additive order | $U\mapsto Ue_1$ is bijective and equivariant; $CV_q\subseteq E_q$ | PASS |
| C3: cyclic source orbits | uniform length $\operatorname{ord}_q(A)$; cosets $C_q/\langle A\rangle$ | PASS |
| C4-C5: full quotient and clock | one class, identity transition, $(1-z)^{-1}$; $q^{-s}$ is external | PASS |
| C6: symplectic quotient | determinant covariance and norm-one fibers | PASS |
| C7: norm-image size | all units away from five; exact index two at five; CRT formula | PASS |
| C8: prime shell and reversal | 1/3/2 full strata and frozen reversing counts 1/1/2/1/2 | PASS |
| C9: composite formulas | exact local lift counts and one full cyclic quotient class for every $q$ | PASS |
| C10: registered control | all nine finite rows agree with the bound exact result | PASS |
| X1-X2: exclusions | enriched quotient/zeta and Hecke/transfer/Fredholm/quantum routes remain untested | PASS |

No claimed theorem depends on the nine development-seen controls.  No
outside-scope construction is presented as ruled out, and no local
$q$-dependent centralizer is promoted to a single global symmetry.

## Exact evidence and lifecycle audit

The immutable upstream chain rehashes consistently:

| Evidence authority | SHA-256 / disposition |
|---|---|
| source lock | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` |
| independent source review | `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5` / `SOURCE_PASS` |
| proof package | `2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c` |
| claim/evidence matrix | `03424a71fc8716618545a6c7c8b0fd05f5ad744cff034255ab0337012da0303d` |
| reviewed execution tree | `87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436` |
| deployment review history | `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0` / final `DEPLOYMENT_PASS` |
| registered claim | `48d767edd9e3dc8f67ba1563ec03d50ef53983447263d0ce8857cfd7ff3326da` |
| raw registered result | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` |
| terminal run record | `6cebc4224d3f275edc2ee6a847f1f7ba71d2f7793959281bcfe853fdb708ffe3` |
| post-run JUnit | `c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195` |
| independent result integrity | `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58` / `RESULT_PASS` |
| strict result manifest | `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658` / `PASS` |
| official experiment report | `1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e` |
| official validation report | `f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a` |

The strict live `results/` inventory contains exactly its nine allowed
regular files and no extra path.  All listed hashes match.  The preserved
history records the initial pre-deployment failure of a shallow semantic
validator, its bounded repair and independent re-review, exactly one
registered exact audit, zero candidate numerical runs, and zero candidate
reruns.  The original failure is not hidden or overwritten.

The nine rows are ordered $q=2,3,5,7,11,4,6,9,10$.  A compact independent
receipt is:

| $q$ | $\lvert E_q\rvert$ | $\lvert CV_q\rvert=\lvert C_q\rvert$ | $\lvert C_q^1\rvert$ | $\operatorname{ord}_q(A)$ | cyclic $A$-orbits | $CV/C^1$ | $E/C$ | $E/C^1$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 3 | 8 | 8 | 4 | 4 | 2 | 2 | 1 | 2 |
| 5 | 24 | 20 | 10 | 10 | 2 | 2 | 2 | 4 |
| 7 | 48 | 48 | 8 | 8 | 6 | 6 | 1 | 6 |
| 11 | 120 | 100 | 10 | 5 | 20 | 10 | 3 | 12 |
| 4 | 12 | 12 | 6 | 3 | 4 | 2 | 1 | 2 |
| 6 | 24 | 24 | 12 | 12 | 2 | 2 | 1 | 2 |
| 9 | 72 | 72 | 12 | 12 | 6 | 6 | 1 | 6 |
| 10 | 72 | 60 | 30 | 30 | 2 | 2 | 2 | 4 |

The full cyclic quotient count is one in all nine rows.  Both quotient maps
have native period one.  The matrix and quadratic-algebra engines agree
object by object; determinant equals norm; norm-one orbits equal determinant
fibers; full/symplectic/reversing strata agree with the frozen classification;
and composite rows prove no prime selector.  The manuscript reports these
finite rows as exact falsification controls, never as proof of the all-$q$
claims or as numerical evidence about $s$, $q^{-s}$, or logarithms.

I did not import or execute the candidate, rerun the registered audit or its
tests, enumerate a new modulus, evaluate a numerical $s$, $q^{-s}$, or
$\log q$, access prime or Riemann-zero data, or use the network in this
Round-2 manuscript review.

## Literature, citation, originality, and scope audit

The literature position is suitable for a deliberately low-novelty
structural audit.  Baake--Neumärker--Roberts is acknowledged as the closest
centralizer/reversal collision; Kurlberg--Rudnick and
Kurlberg--Rosenzweig--Rudnick delimit the norm-one Hecke and invariant-form
background; and Gusein-Zade--Luengo--Melle-Hernández is cited at the coarse
quotient identity-clock boundary.  The general-ring, group-action-zeta,
prime-lattice, prime-power, finite-torus, and twisted-sector sources are used
claim-locally to constrain rather than inflate novelty.  The manuscript does
not claim a new general centralizer classification, a new Hecke theory, an
exhaustive no-go theorem, first discovery, or historical priority.

Mechanical closure gives exactly 14 unique cited keys against 14 bibliography
entries, with missing keys 0 and unused entries 0.  All 56 labels are unique,
and all 40 `ref`/`eqref` uses resolve.  BibTeX reports zero warning.  The
frozen citation-verification ledger remains at
`b4596ed56aee5eb47314221bba681098e45011a3fdc9dafc201315e597a1bfc6`.
This review made no network call, so its literature conclusion is a local
audit of the frozen sources and their bounded uses, not a new exhaustive
search of 2024-2026 literature.  That limitation does not undermine any
stated claim because the manuscript makes no exhaustive-absence or priority
assertion.

The bound plagiarism/originality artifact remains at
`c7e0e2b02f2db393f5893c56ea5f8638067902dc48430728bd3763566781d75f`.
The manuscript's prose, captions, theorem statements, and tables present the
route-specific audit as such; shared standard formulas for the cat matrix and
quadratic algebra are mathematical identities rather than evidence of copied
prose.  This is a local provenance check, not an external plagiarism
certificate.

The claim scope is disciplined throughout.  Burnside, equivariant,
orbifold, stacky, groupoid, and twisted-sector refinements remain live but
untested; Hecke, transfer, Fredholm, and quantum routes are not opened; and
the negative conclusion closes only the coarse $q$-dependent local
centralizer construction actually analyzed.  The manuscript does not infer
global analytic continuation, a functional equation, spectral realization,
prime-zero correspondence, or RH progress.

## Independent build, PDF, and visual QA

I copied only the frozen manuscript source, math commands, bibliography, and
three included vector-PDF figures into each of two fresh temporary build
trees.  In both trees I executed the declared deterministic
LaTeX--BibTeX--LaTeX sequence with the frozen environment.  The result is:

| Check | Build A | Build B | Round-2 result |
|---|---|---|---|
| PDF SHA-256 | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` | same | byte-identical to frozen revision |
| LaTeX-log SHA-256 | `f25ef2cac5202002df9dc4de99cf5c9f2ff8d9976ca5f2938f54e6c532746767` | same | byte-identical |
| BibTeX-log SHA-256 | `30b5b34d3dd350f820edce18b81e27d9d41a2c8642deaff7bc9c094907c856cb` | same | byte-identical |
| bibliography SHA-256 | `5fac9743cfba7fd9ff09b8c6623634b77bd9438ef47ecf68830c32b0a43fc498` | same | byte-identical |
| auxiliary SHA-256 | `6e02071ad6afd968a9f5727301c7912b87b31128b207654d03e1c0df7fcac899` | same | byte-identical |
| outline SHA-256 | `8c67c9850c8be74214cb843131bb82ea236df1c77999333bb5f32918b2b33ee5` | same | byte-identical |
| size/pages | 516261 bytes / 15 | same | exact |
| build stderr | 0 bytes | 0 bytes | clean |

The terminal logs contain no LaTeX or package error, substantive warning,
undefined citation/reference, overfull box, or underfull box.  The only broad
word-pattern hit is the name of the loaded `infwarerr` package; BibTeX's
terminal counter is `warning$ -- 0`.

PDF inspection found all 29 font records embedded, subset, and Unicode-mapped,
with no Type-3 font.  `pdfimages` reports zero raster image object, so the
three included figures remain vector.  Ghostscript rendered all 15 pages
successfully.  I visually inspected every page and separately inspected the
three figure pages at original rendered resolution.  Theorems, equations,
both dense result tables, references, long provenance digests, and all figure
annotations are legible.  No clipping, collision, missing glyph, broken
figure, unresolved marker, or evidence mismatch appears.

The PDF metadata identify only `Anonymous Authors`.  Source and extracted PDF
contain no affiliation, email, ORCID, grant identifier, identifying
repository URL, local filesystem path, `TODO`, `VERIFY`, or unresolved `??`
marker.  The PDF has no form, JavaScript, encryption, or hidden custom
metadata stream.  The declarations appropriately defer authorship, conflict,
funding, and venue-specific fields until release.

## Findings, non-findings, and score

- **Critical findings:** none.
- **Major findings:** none.
- **Minor findings:** none.
- **Residual blockers:** none.

The Round-1 below-Minor wording observations remain genuinely nonblocking.
“Every reversor differs from $J$ by a commuter” is unambiguous in its
defined context; the ASCII spelling “etale” is typographic only; and replacing
“Pre-review manuscript” plus completing authorship/CRediT, conflicts, funding,
and venue metadata is a release/deployment action rather than a scientific
revision.  Exact provenance digests should be handled according to the chosen
venue's double-blind policy, but no identity leak is established in the bound
artifact.

| Dimension | Score | Round-2 assessment |
|---|---:|---|
| Originality (20%) | 64 | Deliberately incremental; the strongest collisions are explicit. |
| Methodological rigor (25%) | 98 | All-modulus proof, exact scope firewall, and adverse validator history are unusually strong. |
| Evidence sufficiency (25%) | 97 | Proof authority, one-shot controls, independent reconstruction, and strict manifests agree. |
| Argument coherence (15%) | 96 | Torsor, quotient, clock erasure, norm boundary, and route decision form a direct chain. |
| Writing quality (15%) | 94 | Precise, anonymous, visually clean, and publication-ready in its stated role. |
| **Weighted total** | **90.05** | **PASS; terminal scientific readiness for the exact frozen bytes.** |

The score is limited by the inherently narrow and largely classical
contribution, not by a residual defect.  The best positioning remains a
specialized negative technical note or companion audit.  Within that role,
the rigor, evidence transparency, and scope control are excellent.

## Final verdict and non-finalization boundary

**PASS — MAY_FINALIZE.**  The exact unchanged source at
`65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6`
and exact 15-page Round-1-revision PDF at
`f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378`
have passed fresh independent Round-2 manuscript review.  No further
scientific, mathematical, evidentiary, bibliographic, figure, or presentation
change is required.

Final integrity may now bind the exact reviewed PDF and proceed to the
project's finalization stage.  This report does not finalize the paper,
create `paper_final.pdf`, update any manifest or pipeline record, release the
repository, or submit externally.  Any change to the manuscript source, PDF,
bibliography, figures, claim manifest, or bound evidence after this review
creates a new snapshot and requires the applicable integrity and review
checks before finalization.
