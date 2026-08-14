# Paper 8 independent peer review — round 1

**Manuscript:** *Isotropy Averaging Erases Returns: Character Traces and a
Fixed-Map Normality Obstruction on Deninger Prime Orbits*  
**Author:** Liang Wang  
**Review date:** 2026-08-14 (Asia/Shanghai)  
**Review mode:** ARS full manuscript review, mathematical-integrity audit,
devil's-advocate check, reproducibility check, and release-integrity check  
**Editorial decision:** **ACCEPT**  
**Open findings:** **0 Critical / 0 Major / 0 Minor**

This decision applies only to the exact final lock below. Any change to the
manuscript, bibliography, native figures, or release PDF reopens the relevant
part of the review.

## 1. Exact final lock

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `paper/manuscript.tex` | 54,921 | `c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa` |
| `paper/references.bib` | 5,606 | `a0d3300c8f7cc093db47e8339adcc079f3d2a993d68d862a37e8d1d79cf0f35e` |
| `paper/figures/owner_map.tex` | — | `b1978bcd5f37cb470096f36b3f05c7a5bc4abf30001b417d8eda5094bd54a34d` |
| `paper/figures/character_filter.tex` | — | `6405ba10b414dfebc5d25811d26b71f3cccccd07f554ce56ee83af55061e72a7` |
| `paper/paper.pdf` | 191,048 | `fad0f602edf4d2300b91bd7b356e363da3ab776c645288a14f39ae171aea262a` |

The canonical release PDF is `paper/paper.pdf`. The obsolete
`paper/manuscript.pdf` and build auxiliaries were removed before the final
decision.

### Byte-drift record

The review did not silently transfer a verdict across drafts.

| Review point | TeX | BibTeX | PDF |
|---|---|---|---|
| Initial review snapshot | `f9bc90bf…93e7d` | `9d68fb0c…e46f` | `55ff9599…ee7` (`manuscript.pdf`) |
| Repaired intermediate snapshot | `d6bf228b…538f` | `33e97b86…fc7` | `bb0db761…099` (`manuscript.pdf`) |
| Final adjudicated release | `c58392dc…9fa` | `a0d3300c…f35e` | `fad0f602…62a` (`paper.pdf`) |

The final transition incorporated the compatible-character trivialization,
the exact crossed-product sign bridge, figure-label separation, and the final
manifestation/locator corrections. The final hashes remained unchanged during
the clean-build, text-layer, visual, route, and control audits.

## 2. Material reviewed

The review covered the complete final manuscript and bibliography, the
19-page release PDF, both native TikZ figures, both release READMEs, and the
following proof and integrity owners:

- `notes/proof_audit.md` and `notes/composition_blueprint.md`;
- `notes/phase3_topology_ownership_proofs.md` and
  `notes/phase3_operator_proofs.md`;
- `notes/phase3_peer_review.md` and `notes/phase3_controls_review.md`;
- `notes/route_audit.md`, all five final Stage-8 Route-A YAML records, and
  `notes/stage8_summary_zh.md`;
- `results/isotropy_trace_manifest.json`, all nine CSV controls, the test
  suite, and the reproduction entry point;
- the topology, groupoid, trace/harmonic, and novelty source manifests,
  checksums, preflight sidecars, and load-bearing retained source pages.

The paper is theoretical/conceptual work at the intersection of transformation
groupoids, crossed products, semifinite traces, harmonic analysis, and
arithmetic dynamics. The appropriate standard is proof correctness and owner
discipline, not empirical effect estimation.

## 3. Editorial synthesis

The manuscript's strongest result is both mathematically meaningful and
correctly scoped: on one already selected actual prime orbit, character
evaluation retains the return comb but cannot extend normally along the fixed
Zak-regular map, while the native regular FNS trace averages over the isotropy
dual and retains only time zero. The full finite rank-one corner converts this
contrast into a rigorous normality obstruction.

The manuscript also handles the principal danger responsibly. It does not use
the local theorem to repair the missing packet topology or packet same-map
transport. The packet question remains `NOT_TESTABLE`; the fixed one-orbit
analogue is `REFUTED`; and the positive-time scalar ledger is a separate
`PASS`. These are three typed conclusions, not three pieces of one promoted
operator.

The contribution is therefore suitable for release in its present exact
form. Its novelty claim is appropriately bounded by the documented search and
does not claim priority over the classical ingredients.

## 4. Mathematical and same-object audit

### 4.1 Owner chain

| Owner | What is proved | What is withheld |
|---|---|---|
| inherited packet `Gamma_p` | source packet, common clock/isotropy, quasi-compactness, second countability, free compact residual action, open intrinsic quotient | packet Hausdorff/LCH, packet completion, transverse Radon selection, packet trace, same-map transport |
| chosen actual orbit `O` | inherited circle `R/(LZ)`, LCH groupoid, Haar convention, amenability | canonical selection inside the packet or packet multiplicity |
| local algebra `A_L` | actual unstabilized `C(T) tensor K(H_0)` model and full/reduced equality | packet field/product chart or canonical trace-preserving trivialization |
| character trace `tau_theta` | l.s.c., densely defined, semifinite, nonfaithful, unbounded C*-trace and phase-weighted return comb | normality in the fixed regular von Neumann owner |
| regular owner `M_L^reg` | faithful Zak representation, `L-infinity(T,m) bar-tensor B(H_0)`, FNS trace `L f(0)` | nonzero-return sensitivity |
| scalar `Theta_+` | coefficient-one positive-time Radon measure | packet/global operator, determinant, or spectral realization |

No proof credit is transferred between these rows.

### 4.2 Theorem-by-theorem findings

1. **Actual-orbit topology — PASS.** The source-flow orbit map
   `q:R/(LZ)->O` is a continuous bijection. If `h` is the restricted continuous
   Deninger--Morishita map, then `h q` is the standard circle bijection and its
   inverse is continuous; hence `q^{-1}=(h q)^{-1}h` is continuous. The proof
   therefore does not rely on an invalid compact-to-non-Hausdorff shortcut.
   Flow anti-equivariance changes orientation, not absolute period or isotropy.

2. **Packet topology boundary — PASS.** The manuscript distinguishes
   open-cover compactness from Hausdorff compactness, uses the intrinsic
   quotient `Q_p=Gamma_p/K_p`, and does not identify `Q_p` with an abstract
   parametrizing base. Packet Hausdorff/LCH and local triviality remain open.

3. **Groupoid convention and completion — PASS.** The arrow, source/range,
   product, inverse, convolution, and involution are internally consistent in
   the frozen source-fibre/right-Haar convention. Appendix A supplies the exact
   bridge
   `alpha_t g(y)=g(y-t)` and `F_a(t)(y)=a(y-t,t)` before the standard crossed-
   product theorems are used. Amenability, full/reduced equality, and the
   unstabilized Williams/MRW compact-operator model are applied only to the
   chosen transitive orbit.

4. **Induced-character sign — PASS.** The four coupled choices are consistent:
   `chi_theta(rL)=exp(+ir theta)`,
   `eta(u+rL)=exp(-ir theta)eta(u)`,
   `k_(n,theta)=(2pi n-theta)/L`, and
   `fhat(xi)=integral f(t)exp(-it xi)dt`. Translation by `t` acts as
   `eta(u)->eta(u-t)`, yielding eigenvalue `fhat(k_(n,theta))` and return phase
   `exp(+ir theta)`. No isolated sign was changed.

5. **Trace class and shifted Poisson formula — PASS.** For
   `f in C_c^infinity(R)`, uniform rapid decay makes every character fibre
   trace class before the trace is taken. Scaled Poisson summation gives
   `T_theta(f)=L sum_r f(rL)exp(+ir theta)` with absolute convergence.

6. **Character-trace type and domains — PASS.** The final text fixes a
   compatible induced-character trivialization satisfying
   `Phi(a)(theta)=pi_theta(a)`. Evaluation followed by the compact-operator
   trace is correctly treated as an extended-positive C*-trace. Dense
   definition, semifiniteness, lower semicontinuity, nonfaithfulness, and
   unboundedness are separately justified; it is never called normal on the
   regular owner.

7. **Zak bicommutant and FNS trace — PASS.** The Zak transform has the correct
   quasiperiodicity and Parseval normalization, and the represented continuous
   compact fields have bicommutant
   `L-infinity(T,dtheta/(2pi)) bar-tensor B(H_0)`. The FNS weight is first
   defined on the positive cone. The square-integrable left ideal and complex
   trace ideal are then stated before complex kernels are traced. Uniform
   trace-norm integrability licenses Fubini and gives exactly `L f(0)`.

8. **Fixed-map no-normal-extension theorem — PASS.** The projection
   `q=1 tensor e` is in `A_L`, full, and finite for every character trace. A
   hypothetical normal extended-positive weight has finite compression to
   `qM_L^reg q=L-infinity(T,m)`. Continuous decreasing peaks equal one at the
   selected character but decrease to zero Haar-a.e., contradicting normal
   order continuity. The same projection and embedding are used throughout.

9. **Singular extensions — PASS WITH THE STATED CEILING.** The measure-algebra
   ultrafilter construction gives distinct singular extensions of the finite
   corner state. The manuscript explicitly does not claim a singular
   extended-positive tracial extension of the full unbounded `tau_theta`.

10. **Scalar ledgers — PASS.** `R_p`, finite-prime sums, and
    `Theta_+` are kept as different typed domains. For compact
    `K subset (0,infinity)`, bounds on both `p` and `r` give local finiteness.
    Coefficient one is owned by rational closed-point counting, not by an
    orbit count within `Gamma_p`. The all-prime zero-time mass is correctly
    excluded and identified as divergent.

11. **Controls — PASS AS CONTROLS ONLY.** The finite computations test signs,
    scale changes, cancellation, shrinking peaks, representative classes,
    arbitrary/copied/composite clocks, transverse choices, and domain
    separation. The text repeatedly states that these do not prove the
    infinite theorems or packet transport.

## 5. Devil's-advocate adjudication

The strongest apparent rejection argument is that a one-orbit calculation
cannot decide a statement about the full Deninger packet. That objection is
correct as a scope warning but does not defeat the paper: the title, both
abstracts, theorem table, owner diagram, packet section, Route audit, and
conclusion all retain the packet result as `NOT_TESTABLE` and the obstruction
as a fixed chosen-orbit theorem.

A second objection is that point evaluation is not a well-defined functional
on Haar `L-infinity`. The proof does not make that mistake. It assumes a normal
extension on the fixed von Neumann algebra, compresses it to a finite normal
functional, and compares only its restriction to the embedded continuous
corner. The decreasing-peak contradiction is therefore valid.

A third objection is that the local Poisson mechanism also compiles arbitrary
and composite clocks. The manuscript accepts this proves-too-much control and
accordingly gives the local traces only weak arithmetic relation. Stronger
arithmetic provenance is assigned solely to source-derived closed points and
their `log p` clocks; no determinant or spectral promotion follows.

No devil's-advocate challenge survives as a Critical or Major finding.

## 6. Route and promotion audit

The manuscript table, `notes/route_audit.md`, and the five exact Stage-8 YAMLs
agree coordinate by coordinate:

| Record | Exact Route-A tuple |
|---|---|
| `DEN-EF-PACKET-ACTION-GRPD-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` |
| `DEN-EF-ORBIT-ACTION-GRPD` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` |
| `DEN-EF-ORBIT-GRPD-REG-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` |
| `DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` |
| `DEN-EF-GRPD-TIME-RETURN-POS` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` |

All five records have overall verdict `ROUTE_A_EXPLORATORY`; all five Boolean
`route_b_invocation_allowed` fields are `false`. There is no Paper-8 Route-B
record. Searches of the manuscript found no positive promotion to a
determinant, A3/A4 structure, completed divisor, analytic continuation,
functional equation, Gamma factor, zero-counting theorem, global all-prime
operator, natural quantization, Route B, or Hilbert--Pólya claim.

## 7. Abstracts, tables, and declarations

- The English abstract contains the exact local character formula, regular
  value, fixed-map `REFUTED`, packet `NOT_TESTABLE`, scalar `PASS`, and explicit
  nonclaim boundary.
- The independent Simplified-Chinese abstract states the same hierarchy and
  does not silently strengthen any English claim.
- Tables 1--6 preserve the theorem types, domains, owners, five Route tuples,
  and forbidden promotions. All were legible in the final PDF.
- The owner/stop diagram visibly separates the packet, chosen orbit, local
  algebra, character fibre, regular owner, and scalar branch; unavailable
  arrows are dashed and labeled.
- Declarations cover data/code, ethics/consent, CRediT-style author
  contributions, competing interests, funding, generative-AI use, source and
  citation integrity, and acknowledgments.
- The AI disclosure is specific: it reports the assisted tasks, disclaims AI
  authorship and cross-model review, states that no unpublished manuscript was
  uploaded to a secondary model, and retains human responsibility.

## 8. Citation and source-integrity audit

The final source has 30 citation commands, 14 unique cited keys, and exactly 14
BibTeX records: no missing key, uncited entry, or duplicate key was found. The
final independent build has no unresolved citation or reference.

The final corrections bind the relevant claims to exact manifestations:

- Deninger's journal article is separated from the arXiv-v4 physical-page
  locators, and the chapter record gives pp. 177--196;
- Bourne--Rennie is volume 21, issue 3, article 16;
- Combes--Zettl is volume 265, issue 1, pp. 67--81;
- Elliott--Robert--Santiago binds Theorem 3.11 to arXiv-v2 physical p. 12;
- Williams's technical locators are explicitly to author draft v3.1;
- Morishita's technical claims are explicitly to arXiv v5.

The topology and trace checksum ledgers verify against the retained bytes. The
topology, trace/harmonic, and novelty preflight sidecars report `PASS`. The five
groupoid-source ARS sidecars report `UNAVAILABLE` because `pypdf` was absent in
that audit environment; the manuscript and source audit disclose this rather
than relabeling it as `PASS`. Independent `pdfinfo` and `pdftotext` checks found
all five readable with the recorded page counts, and the image-only MRW pages
were covered by the documented rendered-page fallback.

The load-bearing claims checked against the retained pages include Deninger
equation (35) and Theorem 6.1, Deninger survey Theorem 4.2, Morishita equation
(1.1.5), Remark 2.1.13 and Lemmas 3.4--3.5, Williams equation (4.63) and
Theorems 4.30/5.12, the amenability/full-reduced theorem, the dual-Haar and
normality inputs, and the locked Fourier/Poisson convention. The manuscript
does not credit any of these sources with the new fixed-map corner theorem.

A separate citation/integrity audit on the same exact lock also returned
`ACCEPT` with no open citation issue.

## 9. Reproducibility audit

I independently ran the 18-test suite with bytecode generation disabled and
then ran the result verifier without regenerating workspace artifacts. Result:

```text
Ran 18 tests ... OK
PASS: artifact, active-tuple, and implementation hashes verified
```

All nine CSV hashes match `results/isotropy_trace_manifest.json`; the nine
files contain 129 data rows. The active-lock and implementation hashes also
match. The exact manifest SHA-256 is

```text
20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07
```

The full reproduction record additionally documents two fresh generations as
byte-identical. The implementation is standard-library only and declares no
randomness, network input, external dataset, fitted parameter, target-zero
data, or timestamp.

## 10. Clean build and PDF audit

The final sources and native figures were copied to an isolated temporary
directory. The four README commands were then run in order:

```text
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex paper
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
```

The final pass was clean except for the two harmless and disclosed underfull
boxes (badness 10000 at source lines 93--95 and badness 1038 at lines
148--149). There were no overfull boxes, unresolved citations/references,
undefined controls, missing glyphs, or BibTeX warnings.

The independently rebuilt PDF has an exactly identical `pdftotext -layout`
layer to the locked release PDF (text-layer SHA-256
`333a501f499b42d141269bee7048f350a5f8442b65dd27921af7fa4ad7433e91`).
The release PDF itself remains governed by its exact lock hash above.

Final PDF checks:

- 19 pages, A4, PDF 1.5, unencrypted;
- title, author, subject, and keywords metadata are correct;
- every reported font is embedded, subset, and Unicode-mapped;
- all 19 pages were rendered and individually inspected;
- no clipping, blank/corrupt page, missing glyph, broken equation, malformed
  reference, or unreadable table was found;
- both figures are legible, and the final Figure 1 arrow labels are separated
  from boxes and connector lines;
- Tables 1--6, the bilingual front matter, appendices, declarations, and all
  14 references are visually intact.

## 11. Closed round-one findings

The following early Minor findings were repaired before the exact final lock.
They are recorded here to preserve review history; none remains open.

| ID | Initial finding | Final closure evidence | Status |
|---|---|---|---|
| M1 | “Fix any trivialization” was broader than the formula licensed, because an arbitrary base reparametrization could relabel `theta`. | Final source fixes a **compatible induced-character trivialization** and states `Phi(a)(theta)=pi_theta(a)`. | CLOSED |
| M2 | Appendix A initially compressed the groupoid-to-crossed-product bridge and did not display the exact sign/reparametrization needed by the main representation. | Final Appendix A states `alpha_tg(y)=g(y-t)` and `F_a(t)(y)=a(y-t,t)`, then checks convolution and involution. | CLOSED |
| M3 | Early Figure 1 arrow labels were visually too close to arrows/boxes. | Final `owner_map.tex` separates “choose one actual orbit / not canonical” and “fixed regular map”; the release page is legible. | CLOSED |

No Critical or Major finding arose in round 1.

## 12. Release/copyright gate

Local retention of exact source PDFs is valuable for verification but does not
establish redistribution rights. The project now has three mutually
consistent safeguards:

1. both release READMEs require public synchronization to omit
   `notes/sources/*.pdf` unless an exact-manifestation licence is documented;
2. `notes/sources/README.md` explains the retention boundary; and
3. `notes/sources/.gitignore` contains the default `*.pdf` exclusion while
   preserving manifests, hashes, URLs/locators, checksum ledgers, and preflight
   sidecars.

**Operational release condition:** immediately before any public push, verify
that zero `papers/8-isotropy-trace/notes/sources/*.pdf` paths are staged or
tracked. If any such PDF is present without an exact redistribution licence,
that is a **release blocker**, not a manuscript-mathematics defect. A
`.gitignore` rule does not remove a file that was already tracked, so the
staged-path check remains mandatory.

## 13. Final decision

**ACCEPT** the exact final manuscript and release PDF identified in Section 1.
The mathematical result is correct at its declared owner, the packet/local/
scalar hierarchy is preserved, the signs and domains close, Route coordinates
are not spliced, citations and declarations pass, the controls reproduce, and
the 19-page PDF is release-quality.

The only remaining action is the operational public-sync check in Section 12;
it does not require a manuscript revision.
