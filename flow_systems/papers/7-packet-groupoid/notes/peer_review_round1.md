# Paper 7 independent peer review — Round 1

Review date: **2026-08-14 (Asia/Shanghai)**  
Review mode: **independent, read-only, exact-byte review**  
Manuscript: *Prime Packets without a Packet Trace: Decomposable Proxies, a
Zero-Mode Ledger, and the Same-Object Boundary*  
Recommendation: **ACCEPT**

## 1. Decision and finding register

| Severity | Open findings |
|---|---:|
| Critical | **0** |
| Major | **0** |
| Minor | **0** |

The locked manuscript is mathematically coherent, source-disciplined,
reproducible within its stated control scope, and ready for release. I found
no correction that is mandatory for acceptance.

This decision is deliberately narrower than an endorsement of the proxy as a
Riemann spectral model. The manuscript proves exact proxy theorems and an
equally important negative ownership result. It does **not** claim that the
published packet flow owns the selected measure, operator algebra, trace,
zero-mode family, determinant, or Route-B operator. That boundary is preserved
consistently from the abstract through the Route table and declarations.

### Mandatory repair list

**None.**

## 2. Review method

I applied the ARS-Codex academic-review and integrity principles as a
decision-impact review:

1. every load-bearing conclusion was tied to an exact text locator and a
   locked evidence artifact;
2. mathematical validity, source ownership, operator terminology,
   reproducibility, and presentation were reviewed as separate gates;
3. the strongest counterargument was tested rather than averaged away;
4. severities were assigned only when a defect would affect correctness,
   interpretation, reproducibility, or the release decision; and
5. prior review verdicts were treated as evidence, not inherited as this
   review's conclusion.

The manuscript and all supporting records were read-only. This report is the
only workspace file created by this review.

## 3. Exact submission and evidence lock

### 3.1 Release bytes

| Artifact | SHA-256 | Observed state |
|---|---|---|
| paper/manuscript.tex | ad14cc033eee56db804dd29e5e44a47fbeb56fac286cda775268d782813830fd | exact match |
| paper/references.bib | 25c8f9c95505c5a752ae2c1bfd7c18cc4811c33fac15a77fdb83bfbf2a0c5bf7 | exact match |
| paper/fig_owner_map.tex | 684bb3e83de9f12c92651580797d72c0b528051549b80f8239dc083dfcde03f3 | exact match |
| paper/fig_ef_collapse.tex | fca764ba3ee291961c7b9c013544ea5751cc03f6ce8d4168fbd4ddfff9e86959 | exact match |
| paper/paper.pdf | 77aeaf1c381528998ecd8da591e9630a57326c1ebbf9bc2ac56f956048e22365 | exact match; 22 A4 pages |

All manuscript line locators below refer to the locked manuscript bytes
ad14cc03… .

### 3.2 Normative and independent evidence

| Evidence record | SHA-256 |
|---|---|
| notes/research_protocol.md | 2f8dc9a802cfcf8b578db24419909de710563ece62cf026e9848fac437ba1581 |
| notes/candidate_lock.md | 73314bb031f663e8532a922821e66b20f31bd6f20b06a801a25147d6e55a17a0 |
| notes/proof_audit.md | febcd43e5d23daf893816b815c81f19ee4da5bac42a554d553262784660f00b5 |
| notes/phase3_protocol_amendment.md | b8c55c5a2ebd4f22f6990671d03b2e1d997ce180e7638ed933b20471374eb03c |
| notes/phase3_postfix_review.md | 8527d940ccac52279ac857a9db7739e8a4d4849035d6a6a371aeaac7beacb475 |
| notes/phase3_lock_ef_review.md | 913f901d2afe648c10bddfbfd41f9a3d7356c2b5f99c87d459547810d596581b |
| notes/source_audit.md | a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53 |
| notes/operator_source_audit.md | 69a76991c94cab24652c8d7d9f71c47a8eba70fcd7d1d4148689d47ff56e8b04 |
| notes/composition_blueprint.md | ec916a47cc77b7d6e731614d2f258f7c61ecb3317b405ad5fc0b094324a6cc7b |
| notes/route_audit.md | 79261a2e6e70350a22d1fc81336c24c7c86fc1baafaa5ed8acbbebea404a6091 |
| results/packet_trace_manifest.json | fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26 |

The final M5 closure is present at phase3_lock_ef_review.md lines 717–810:
the previously reported downstream propagation issue is explicitly closed,
with Critical/Major/required-Minor counts all zero. I independently checked
the corrected blueprint rather than relying on that prior disposition.

### 3.3 Object-specific Route records

All four YAML files parsed successfully and retained the following hashes:

| Candidate | YAML SHA-256 |
|---|---|
| DEN-WITT-Z-FIN | 2b946f8a5b2ff0c4621687742f53001b22468810cfbca52e06f220c42c8bd92c |
| DEN-WITT-PACKET-DECOMP-K0-M1 | 44250231fac3f8f1f6dbb181482b0e9b02e06e2e2634924d382200ee1f98db81 |
| DEN-WITT-PACKET-DECOMP-RETURN-DIST-M | b787d2cc1341584eb701a2741c4ccaff4a07283e5b8aa42b463636196e5b0fe1 |
| DEN-WITT-PACKET-DECOMP-MASS-FAM | cf6d40f03a6158daecdcb292967f9cb814b3906e335b4c5b17e60d41a9ab15ca |

## 4. Claim-by-claim mathematical review

### 4.1 FNS foundation

**Locator:** manuscript lines 285–370, especially Proposition
“Concrete faithful normal semifinite trace” at lines 311–361.  
**Verdict:** **PASS.**

The direct-integral component traces are tracial and faithful. Normality is
handled for arbitrary increasing nets, not just sequences. Semifiniteness is
proved using the increasing congruence cutdowns
A_p^(1/2) E_(p,N) A_p^(1/2), followed by a finite-prime/finite-mode directed
net. The bound by ||A_p||(2N+1) is sufficient, and the global weighted sum
uses only 0 < m_p < infinity. The bounded L1 block criterion follows
componentwise from functional calculus. Trace existence is correctly proved
before any Dirichlet-series special case.

### 4.2 P7-1 — component Poisson trace

**Locator:** manuscript lines 375–423.  
**Verdict:** **PASS.**

For U_L(t)g(u)=g(u-t), the normalized Fourier mode has eigenvalue
exp(-2 pi i n t/L), hence T_L(f) has eigenvalue f-hat(2 pi n/L). The
Schwartz decay gives absolute trace-class summability on the circle factor.
The periodization convention produces the factor L in

    sum_n f-hat(2 pi n/L) = L sum_r f(rL).

The probability transverse base contributes total mass one and no hidden
multiplicity factor.

### 4.3 P7-2 — exact global L1 boundary

**Locator:** manuscript lines 431–478.  
**Verdict:** **PASS.**

The global block is bounded by ||f||_1 independently of p. For nonzero f,
the whole-line Riemann sums for |f-hat| give
||C_(p,f)||_(1,tau_p) asymptotic to c_f log p with c_f > 0. Eventual
two-sided comparison therefore yields the exact equivalence

    C_f in L1_(tau_m)  iff  sum_p m_p log p < infinity.

The unit-mass obstruction is consequently stronger than divergence of a
delicate cancellation: its positive trace-norm summands do not tend to zero.

### 4.4 P7-3 — positive-time return measure

**Locator:** manuscript lines 480–520.  
**Verdict:** **PASS.**

On a compact interval [a,b] contained in positive time, a contributing pair
(p,r) obeys p <= exp(b) and r <= b/log 2, so only finitely many atoms occur.
This proves local finiteness for arbitrary positive finite masses. The text
correctly permits tau_m(C_f)=Theta_m(f) only inside the global L1 domain and
keeps Theta_m as a separately owned Radon measure outside it. The zero-time
term and the absence of regularization are explicit.

### 4.5 P7-4 — affiliated versus bounded domains

**Locator:** manuscript lines 525–584, especially lines 544–578.  
**Verdict:** **PASS; versioned correction is correctly propagated.**

The two conditions are separated exactly:

    affiliated L1:       sum_p m_p p^(-Re s) < infinity;
    bounded tau-ideal:   Re s >= 0 and the same weighted sum converges.

The operator norm is sup_p p^(-Re s), while the extended trace norm is the
weighted Dirichlet sum. The example m_p=p^(-3), Re s=-1 correctly witnesses
the difference. For unit masses both conditions reduce to Re s>1. The
historical conflation is disclosed and tied to the versioned amendment rather
than silently erased.

### 4.6 Relative-norm holomorphy

**Locator:** manuscript lines 586–640.  
**Verdict:** **PASS.**

On compact subsets of H_m, logarithmic derivative factors are dominated by a
strictly more convergent weighted prime series. The independent operator-norm
tail sup_(p>P)(log p)^k p^(-a) tends to zero. These two controls establish
locally uniform convergence of finite-prime entire truncations in
||.||+||.||_(1,tau_m), for all derivative orders. The logarithm and its
derivative then have geometric majorants because ||K_s|| is uniformly below
one. The proof does not rely on trace norm alone.

### 4.7 P7-5 — scalar and determinant taxonomy

**Locator:** manuscript lines 642–769.  
**Verdict:** **PASS.**

The manuscript defines a branch-fixed principal trace-log scalar on H_m,
not an unqualified global determinant. Absolute, locally uniform convergence
licenses the trace and double-series interchange. For unit masses the
identity D_tau(s)=product_p(1-p^(-s)) and Z=D_tau^(-1)=zeta(s) is asserted only
for Re s>1.

The taxonomy is also correct:

- ordinary Fredholm theory is unavailable in the intended representation;
- de la Harpe–Skandalis is naturally quotient-valued before the selected
  local scalar lift;
- the positive semifinite Fuglede–Kadison quantity is |D_tau| and loses
  phase;
- I-K_s is invertible on H_m, so the Breuer–Fredholm index is zero; and
- the finite-trace analytic determinant is not imported verbatim into the
  globally infinite trace.

### 4.8 The actual B_p and ordinary Hilbert multiplicity

**Locator:** manuscript lines 702–727.  
**Verdict:** **PASS.**

The coordinatewise sign subgroup contains an infinite product of C_2 factors,
whereas the procyclic subgroup p^(Z-hat) has at most one nonidentity
involution. Its intersection with the sign subgroup has size at most two, so
the quotient B_p is infinite. Arbitrarily many disjoint nonempty open sets
then give arbitrarily large orthogonal families in Haar L2(B_p). Thus
P_(0,p) has infinite ordinary Hilbert rank even though tau_p(P_(0,p))=1.
The ordinary-Fredholm exclusion is proved for the frozen base itself, not
only for a generic control space.

### 4.9 P7-6 — scope of mass classification

**Locator:** manuscript lines 774–799.  
**Verdict:** **PASS, correctly scoped.**

Positive finite sequences classify only the frozen central-scalar trace
family, with m_p recoverable from tau_m(P_(0,p)). The manuscript explicitly
notes that nonconstant positive central densities produce further FNS traces.
The copied-component calculation is additive and is not misused to select
unit mass.

### 4.10 P7-7 — target-conditioned uniqueness

**Locator:** manuscript lines 801–820.  
**Verdict:** **PASS.**

Equality with the unit-coefficient prime-power logarithmic derivative forces
m_p=1 by uniqueness of absolutely convergent Dirichlet series, already at the
primitive coefficient n=p. The text immediately identifies the circularity:
target-conditioned coefficient uniqueness is a consistency result, not
source provenance.

### 4.11 P7-8 — base blindness and arbitrary-clock compiler

**Locator:** manuscript lines 822–889.  
**Verdict:** **PASS.**

Replacing B_p by a singleton or any probability space preserves every
constant-fibre semifinite formula while changing ordinary Hilbert
multiplicity. The arbitrary-clock generalization separates local finiteness
of the positive-time return ledger from convergence and strict-norm
requirements for the trace-log branch. The domain is allowed to be empty.
The “proves too much” control is interpreted as a ceiling on geometric and
arithmetic inference, not as positive provenance.

### 4.12 Morishita printed gap and the restricted E_f theorem

**Locator:** manuscript lines 891–1008.  
**Verdict:** **PASS.**

I checked the load-bearing statements against the frozen local primary
manifestations:

- Morishita equation (2.1.5) uses the full character set and Remark 2.1.13
  explicitly omits Deninger's refinement.
- Morishita equation (2.2.7) uses the multiplicative monoid of positive
  integers. Every displayed image character therefore has finite kernel,
  while the full Hom set includes the trivial infinite-kernel character.
  The printed full-space surjectivity cannot hold as stated.
- The printed proof of Theorem 3.6(2) checks the p-coordinate but does not
  establish the required nonzero away-from-p coordinates on that full space.
- Deninger equation (35) gives exactly the finite-kernel E_f representation
  used in the repair. Lemmas 3.4–3.5 of Morishita support continuity,
  equivariance, suspension descent, and time reversal after restriction.
- On a closed p-fibre, normalization by n^(-1) in Q^× and by an element of
  Z-hat^× sends a source point into C_p; the flow covers the full target
  circle.
- Deninger equations (62)–(68) bound the image to at most one finite zero
  coordinate, whereas the Connes–Consani target contains a class with two.
  The zero set is invariant under the target quotient, proving strict global
  non-surjectivity.

The theorem is therefore a valid new restricted derivation: continuous,
flow-anti-equivariant, packetwise onto C_p, transversely collapsing, and
strictly not globally onto. It is not presented as Morishita's unmodified
full-space theorem.

### 4.13 No transport and P7-9

**Locator:** manuscript lines 987–1070, including T0–T7 at lines 1018–1043
and Theorem P7-9 at lines 1054–1069.  
**Verdict:** **PASS as a bounded negative ownership certificate.**

The Morishita map targets the separate Connes–Consani adelic object, not the
Paper-7 proxy. It collapses transverse labels and transports none of the
proxy's measure, representation, algebra, FNS trace, L1 domain, return
functional, zero mode, analytic family, or determinant. The four ownership
sources, operator corpus, and bounded update search support the stated
negative result. Crucially, the manuscript calls this an audited absence
statement through 14 August 2026, not a universal nonexistence theorem.

## 5. Same-object Route audit

**Locator:** manuscript lines 1072–1123; authoritative comparison:
notes/route_audit.md lines 46–51 and 171–202.  
**Verdict:** **PASS.**

The manuscript's four object-specific rows exactly match the four YAML
records:

| Object | (A0,A1,A2,A3,A4) | Overall; Route B |
|---|---|---|
| Published source | (A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL) | ROUTE_A_EXPLORATORY; false |
| Mass-family proxy | (A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL) | ROUTE_A_EXPLORATORY; false |
| Return record | (A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL) | ROUTE_A_EXPLORATORY; false |
| Zero-mode record | (A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL) | ROUTE_A_EXPLORATORY; false |

No coordinate splice is performed. In particular, source A0/A1, return-record
A1, and zero-mode A2 are not combined into a synthetic candidate. No Paper-7
Route-B YAML exists, and every candidate records Route-B invocation as false.

## 6. Reproduction, build, and visual audit

### 6.1 Deterministic controls

Running ./experiments/reproduce.sh from the Paper-7 root completed
successfully:

    21/21 tests: PASS
    artifact count: 9 CSV files
    data rows: 407
    prime count through 5000: 669
    implementation-hash verification: PASS
    tampered/missing/extra manifest tests: PASS
    two fresh regenerations: byte-for-byte identical
    manifest SHA-256:
    fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26

The nine manifest artifact hashes, row counts, and byte counts matched. The
maximum Poisson-convention residual was 4.440892098500626e-16; the maximum
finite D/Z product residual was 2.6645352591003757e-15. Quantity labels and
signs agree with the manuscript: tau-Log D is negative on the positive-real
control domain, log Z=-tau-Log D is positive, and D/Z are reciprocal.

These controls use no network, randomness, external dataset, target-zero
data, or fitted masses, clocks, shifts, phases, or cutoffs. They remain
finite convention and regression witnesses, not proofs of the infinite
theorems or of source transport.

### 6.2 Independent clean build

I copied only the release paper inputs into an independent temporary
directory and ran the documented sequence:

    xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
    bibtex paper
    xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
    xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
    xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex

Results:

- 22 A4 pages and 223,230 bytes;
- 15 bibliography entries and no BibTeX warning;
- zero undefined citations or references;
- zero overfull boxes;
- zero LaTeX/package warnings and zero missing-glyph diagnostics;
- 35 nonfatal underfull boxes, matching the release audit; and
- all PDF fonts embedded.

The temporary build PDF had SHA-256
cde784b9b86aa2f43f86dd4ad3622b0d93be4d96754353fc638b463e60241778,
so the PDF container was not byte-identical to the locked release PDF.
However, pdftotext -layout outputs from the release and clean build were
byte-identical, both with SHA-256
2dcdd03ff979ebfcbc7a9fc10d4480690ee2c9f5eb78b98e24f4ba9fcf20d429.
The README promises a clean, cross-reference-stable build, not a
bit-reproducible PDF container; this is therefore not a finding.

### 6.3 Visual sampling

Pages 1, 4, 16, 17, and 22 were rasterized and inspected at original detail.
The bilingual abstract, owner-map figure, E_f-collapse figure, T0–T7 table,
four-object Route table, and bibliography were legible and unclipped. I found
no overlapping text, missing glyph, broken figure, margin overflow, or
unreadable table entry.

## 7. Citation and source integrity

The locked auxiliary citation set contains 15 unique keys, exactly matching
the 15 bibliography entries: no dangling citation and no uncited bibliography
record. The source directory contains 15 PDFs and 15 same-stem preflight
sidecars. Every sidecar records PASS, equal declared/enumerated/reader page
counts, and an empty warnings list.

The primary locators supporting the most consequential ownership claims were
checked directly in the local PDFs:

- Deninger v4: equation (35), Theorems 5.2 and 6.1, and equations (62)–(68);
- Deninger's survey: Theorem 4.2;
- Morishita v5: equation (2.1.5), Remark 2.1.13, equation (2.2.7),
  Lemmas 3.4–3.5, and Theorem 3.6 with its printed proof;
- Connes–Consani: equation (2) and the target quotient's zero-set invariant;
- the cited primary operator sources for direct-integral/FNS traces,
  generalized Lp spaces, relative determinants, Fuglede–Kadison modulus,
  Breuer–Fredholm index, ordinary Fredholm determinants, and the Fourier
  convention.

The bibliography does not substitute a review article for a load-bearing
primary theorem. I found no fabricated reference, locator mismatch, or
citation that supports a stronger claim than its source.

## 8. Integrity and disclosure review

**Verdict:** **PASS.**

- The P7-4 deviation is recorded non-retroactively and propagated into the
  final theorem, domain, taxonomy, blueprint, and status ledger.
- No empirical target, zero list, fitting objective, tuned hyperparameter, or
  post hoc validation region is used.
- Numerical controls are explicitly denied proof or Route authority.
- The source/proxy/return/zero-mode/adelic objects remain typed separately,
  preventing result splicing and provenance inflation.
- Negative-search language is date-bounded and does not become a universal
  impossibility claim.
- Data/code availability, ethics, authorship responsibility, competing
  interests, funding, and AI-use statements are present at manuscript lines
  1263–1312.
- The AI disclosure accurately assigns responsibility to the human author and
  does not claim an unperformed cross-model review.

## 9. Strongest counterargument and adjudication

The strongest objection is that the exact scalar is a universal ledger
compiler rather than a geometry-sensitive invariant: probability-base
replacement, arbitrary clocks, composite-augmented clocks, positive mass
perturbations, and copied components preserve substantial parts of the
formalism. Therefore the equality with the Euler product cannot by itself
certify Deninger's packet geometry, unit-mass provenance, a Ruelle
determinant, a completed divisor, or a Hilbert–Pólya operator.

That objection is **valid but not a defect in this manuscript**, because it is
the manuscript's own adversarial conclusion. P7-8 proves the blindness,
P7-9 denies transport, the Route table prevents cross-object aggregation, A3
and A4 fail, and Route B remains closed. The paper's defensible contribution
is precisely the combination of an exact local analytic proxy theorem with a
negative same-object ownership certificate.

## 10. Final recommendation

**ACCEPT.**

The release has no open Critical, Major, or Minor finding. P7-1–P7-9, the FNS
foundation, the P7-4 domain split, relative-norm holomorphy, the actual-B_p
multiplicity argument, determinant taxonomy, restricted E_f bridge, strict
non-surjectivity, no-transport conclusion, four-object no-splice Route table,
deterministic controls, bibliography, presentation, and declarations all
survive independent review on the exact locked bytes.

## 11. Bibliographic-only metadata re-lock addendum — 2026-08-14

### 11.1 Scope, independence, and exact-byte lock

This addendum is a fresh read-only review of the bibliographic-only revision;
it does not inherit acceptance merely from the earlier review.  The prior
accepted report is anchored at SHA-256
`a2a6e6a865cd0daccb1a25dffcbc3b6a3a9638c0be6eded8bfd2fd0ba9bf565c`.
No manuscript, bibliography, PDF, manifest, README, code, experiment, or
result file was changed by the reviewer.  The final candidate reviewed here is
locked as follows:

| Artifact | Final SHA-256 |
|---|---|
| `paper/manuscript.tex` | `5fd2f30d072b5c629a67c2be95b8fcc95a917e694f7e6be13a45f347f0e0c384` |
| `paper/references.bib` | `68d96e5857dafd0594acd5d465637487c9281e06a178faed3e2998c231d3b48f` |
| `paper/paper.pdf` | `4f0f9fbebf705e6b73c34fb66b01d4dda9d6ac37b7409f587bbefd8fecdcbd8d` |
| `notes/sources/paper7_source_manifest.md` | `d99a0e9c9ddcfb4ab5ca3f7a57284dd1a405567664ce3dcc1d7abd1602fd4d0e` |
| `paper/README.md` | `523e3d5bccf36054783e793eb2c6b35ea1dcc0b00d6e9d468cb0fee3ae6a15d0` |

All five hashes were recomputed from the workspace bytes and match the release
lock exactly.

### 11.2 Mathematical-content drift audit

An exact unified diff against the initially accepted TeX lock
`ad14cc033eee56db804dd29e5e44a47fbeb56fac286cda775268d782813830fd`
contains only two nonmathematical hunks:

1. manuscript lines 765–767 add the primary pinpoint “Definition and
   Lemma 1, p. 521” to the already accepted Fuglede–Kadison positivity claim;
2. manuscript lines 1266–1276 name the canonical 15-source manifest and make
   the integrity declaration accurately distinguish positive load-bearing
   locators from bounded whole-text negative searches.

There is no change to a definition, hypothesis, formula, theorem, proof,
operator, domain, normalization, numerical claim, P7-1–P7-9 verdict, Route
tuple, or Route-B status.  The bibliography diff changes metadata only; all 15
BibTeX keys and every in-text citation target are stable.  Thus the accepted
mathematical content has not drifted.

### 11.3 Metadata and locator verification

The revised records were checked independently against DOI registries,
publisher/journal records, the versioned arXiv manifestations, and the local
source artifacts.  The resulting record-level audit is:

| Record | Re-lock result |
|---|---|
| `Deninger2023` | arXiv v1 remains the theorem-locator manifestation; the 2024 *Colloquium De Giorgi 2021 and 2022* cross-record is correctly separated. |
| `ConnesConsani2025` | final *Regulators V*, Contemporary Mathematics 842 (2026), pp. 105–132, DOI `10.1090/conm/842/16852` verified; the note correctly preserves arXiv v1 for equation locators and disclaims byte/text identity. |
| `BagarelloTrapaniTriolo2006` | volume 55, issue 1, pp. 21–28, DOI `10.1007/BF02874664` verified. |
| `Hiai1988` | volume 17, issue 1, pp. 117–137, DOI `10.14492/hokmj/1381517791` verified. |
| `FackKosaki1986` | volume 123, issue 2, pp. 269–300, DOI `10.2140/pjm.1986.123.269` verified. |
| `Bornemann2010` | volume 79, **number 270**, pp. 871–915, DOI `10.1090/S0025-5718-09-02280-7` verified against the AMS issue record; the earlier mechanical “issue 2” suggestion is superseded and does not appear in the final bytes. |
| `GuidoIsolaLapidus2009` | volume 361, issue 6, pp. 3041–3070, DOI `10.1090/S0002-9947-08-04702-8` verified. |
| `BenameurEtAl2006` | final World Scientific chapter, pp. 297–352, DOI `10.1142/9789812773609_0012` verified; section/page locators remain explicitly bound to arXiv v1 of 20 December 2005. |
| `Laugesen2009` | the cited artifact is correctly recorded as arXiv v2, revised 17 May 2017; definition/theorem locators remain bound to that manifestation. |
| `FugledeKadison1952` | the new pinpoint at manuscript lines 765–767 matches Definition and Lemma 1 on journal p. 521 of the local primary PDF. |

The final auxiliary citation set has 15 unique keys and equals the 15-entry
bibliography key set exactly: no dangling citation, missing bibliography item,
or uncited record.  BibTeX emits 15 `\bibitem`s and no warning.

### 11.4 Canonical-source, build, control, and Route receipts

The canonical manifest hash above enumerates 15 PDFs and 15 same-stem
preflight sidecars.  Independent recomputation found 15/15 PDF hashes and
15/15 sidecar hashes equal to the manifest; every sidecar embeds the matching
PDF hash, reports `PASS`, gives equal declared/enumerated/reader page counts,
and has an empty warnings array.

A clean copy of the final TeX, BibTeX, figures, and README was built with
XeLaTeX, BibTeX, and three final XeLaTeX passes.  It completed at 22 A4 pages.
The final log has zero undefined citations or references, zero overfull boxes,
zero missing-glyph diagnostics, zero LaTeX/package warnings, and the same 35
nonfatal underfull-box diagnostics declared in the README.  `pdffonts` reports
all fonts embedded.  `pdftotext -layout` on the locked release and independent
rebuild is byte-identical, with SHA-256
`0fa1f50432c4d219aa84289f4c63f7938b890bf1b3a6c533eb8c9e562d719b34`.
Pages 1, 4, 11, 12, 16, 17, 21, and 22 were rasterized and inspected; the
bilingual front matter, figures, determinant table and new pinpoint, T0–T7 and
four-object Route tables, declarations, and revised bibliography are legible
and unclipped, with no overlap, margin overflow, or missing glyph.

The authoritative control manifest remains
`fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26`.
In an isolated copy, `experiments/reproduce.sh` again passed 21/21 tests; two
fresh regenerations were byte-identical.  The object-specific Route audit
remains
`79261a2e6e70350a22d1fc81336c24c7c86fc1baafaa5ed8acbbebea404a6091`:
the published source, mass-family proxy, return record, and zero-mode record
remain four separate objects, tuple coordinates are not spliced, and Route B
is false for every row.

### 11.5 Final re-lock decision

**FINAL ACCEPT — Critical 0 / Major 0 / Minor 0.**

The bibliographic-only revision resolves the metadata and manifestation
issues without changing the accepted mathematics, claim strength, object
typing, Route adjudication, deterministic controls, or disclosures.  There is
no mandatory repair remaining on the exact locked bytes listed in §11.1.
