# Manuscript Integrity Audit — Paper 5

Audit date: 2026-08-13  
Candidate: `FF-FROB-SUSP-P1-F2-KOOPMAN-P1`  
Audited release: `paper/paper.pdf`  
Verdict: **PASS** within the frozen A4 and limited B1--B3 scope

## 1. Release identity

| Artifact | SHA-256 |
|---|---|
| `paper/paper.pdf` | `802ad1a1169be166d5a82da2e0247a92e6c848113303c7d70818bbdfd90acef5` |
| `paper/manuscript.tex` | `3616a52872510f9b8ddb355b8f35b437ba0956dc592342757f5c64f5214c8f4a` |
| `paper/references.bib` | `e020001bf9a2273bd58ff5454dc24d61d58627ed1940950dde685c63303bbc46` |
| `results/koopman_spectral_manifest.json` | `af9746cd5a5684ecbd7c92fdbbbf661ad6ad6acd00577c8ce5aa938421bf0344` |

The release PDF has 14 letter-size pages. It was built with
XeLaTeX, BibTeX, XeLaTeX, and XeLaTeX. The final log has:

- zero compilation errors;
- zero undefined citations;
- zero undefined cross-references;
- zero overfull boxes;
- five underfull-box notices, all confined to narrow table cells and without
  clipped or missing content.

Every page was rasterized and visually inspected. Both native TikZ figures,
all four tables, equations, Chinese glyphs, bibliography, and declarations
rendered legibly. Figure 2 was revised after visual inspection to prevent
relationship labels from crossing ledger text.

## 2. Claim-boundary audit

The final manuscript was checked against `composition_blueprint.md` and
`proof_audit.md`. The central claims match the frozen proof certificate:

| Claim | Manuscript status | Integrity result |
|---|---|---|
| all families of finite, strictly positive component weights are unitarily equivalent | theorem and proof | `VERIFIED` |
| `A_w` has the complete periodic Sobolev direct-sum domain | definition before self-adjointness | `VERIFIED` |
| `A_w` is the Stone self-adjoint generator | Fourier/direct-sum proof | `VERIFIED` |
| point spectrum is `(2*pi/log(2))*Q` | equality including converse | `VERIFIED` |
| every point eigenvalue has countably infinite multiplicity | degree-`kb`, mode-`ka` proof; zero included | `VERIFIED` |
| spectrum and essential spectrum are `R`; discrete spectrum is empty | closure plus singular Weyl sequences | `VERIFIED` |
| complete pure-point eigenbasis coexists with irrational continuous-spectrum points | explicit terminology remark | `VERIFIED` |
| every interval of positive width has infinite projection rank | exact interval quantifier | `VERIFIED` |
| compact resolvent and trace-class heat fail after kernel deletion | nonzero rational-eigenspace control | `VERIFIED` |
| orbit, cohomology, and Koopman actions are different ledgers | proposition plus native TikZ ledger | `VERIFIED` |
| no physical quantization is supplied | scoped frozen-data statement | `VERIFIED` |

The probability-weight statement was checked explicitly: the manuscript now
requires `sum_x w_x L_x = 1`, rather than an insufficient unweighted
summability condition.

## 3. Route and scope audit

The only serialized verdicts are:

```text
A4_UNITARY_OR_SCATTERING_CANDIDATE — PROVED
B1_COMPLETE_OPERATOR_DEFINITION — PROVED
B2_SELF_ADJOINT — PROVED
B3_FAIL — PROVED
ROUTE_B_REJECTED at Gate C
hilbert_polya_claim_allowed: false
```

B4 and B5 occur only as scope annotations: **outside the limited audit / not
invoked / no verdict serialized**. No `B4_FAIL`, `B5_FAIL`, pass enum, or
invented evaluation status occurs in the manuscript. The manifest records
`b4_b5_invoked: false` and limits its Route-B scope to B1--B3.

## 4. Citation and source integrity

The manuscript cites ten bibliography entries, and all ten entries are used.
The final BibTeX log reports zero warnings. DOI-bearing references include
their DOI fields. Load-bearing locators are stable theorem, section, or
equation identifiers, consistent with the source matrix's explicit decision
not to claim uncertified PDF-reader page anchors.

External theorem use remains within the source matrix:

- Deligne: closed-point/Frobenius dictionary and cohomological determinant;
- Niederreiter--Xing: irreducible-polynomial count;
- ter Elst--Lemańczyk: Koopman group context;
- Teschl: direct sums, Stone framework, and spectral terminology;
- Bornemann: ordinary trace-class Fredholm determinant boundary;
- Kostant: historical quantization context only.

No source is cited for a stronger conclusion than its recorded role. The
candidate-specific spectral, multiplicity, compactness, and heat results are
proved in the manuscript.

## 5. Computational reproducibility

Final command:

```bash
./experiments/reproduce.sh
```

Result: **8/8 tests pass** in 0.005 seconds.

The generated artifact hashes are:

| Artifact | SHA-256 |
|---|---|
| `closed_point_degree_controls.csv` | `eb6694a34c0e911cdd718659412aacef0929db75104381e2b404276b06f7e059` |
| `frequency_multiplicity_witnesses.csv` | `3e917c08590557b7481e6bc4e00c3a641605374be8e7a1e09c6131b1c5837029` |
| `weight_unitary_controls.csv` | `0b4c91d6e9a1903571ada2889f668cb61ee0a0904ad92570f493019b6b197b10` |

Finite controls are presented as regression checks, not as evidence for the
infinite theorems.

## 6. Exclusion and disclosure audit

- `target_zero_data_used: false`;
- `fitted_parameters: []`;
- no Riemann-zero list, zero statistic, prime table, scale fit, shift fit,
  potential fit, boundary fit, randomness, or network access;
- no eigenvalue scatterplot or fitted spectrum;
- no ordinary determinant is claimed beyond its valid trace-class boundary;
- relative or renormalized determinants are correctly described as possible
  new candidates requiring additional choices.

Mandatory manuscript disclosures are present: Data and Code Availability,
Ethics, CRediT Author Contributions, Funding, Conflict of Interest,
AI-Assistance Disclosure, and an explicit Limitations subsection.

## 7. Writing-quality audit

The final prose contains none of the ARS high-frequency warning terms and no
throat-clearing openers. No em dash is used in prose. Technical terminology is
kept consistent: `pure-point spectral measures`, `continuous-spectrum
accumulation points`, `interval of positive width`, and `physical quantization
is not supplied` are not replaced by stronger or ambiguous formulations.

## 8. Residual limitations

The local source corpus's ARS PDF preflight remained unavailable because
`pypdf` was absent during source acquisition. `pdfinfo` and `pdftotext`
succeeded, and stable section/theorem/equation locators were verified, but no
reader-page anchors are upgraded in this release. This does not affect the
candidate-specific proofs, which are reproduced in full.

The manuscript has not undergone a separate external journal peer-review
panel in this audit. `PASS` means integrity-clean and review-ready within the
frozen project protocol, not accepted by an external venue.
