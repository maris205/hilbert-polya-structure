# Consolidated hostile-review closure — P151

**Status:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**  
**Scope:** anonymous internal review closure; no external-release authority

## Review ledger

| round | verdict | Critical | Major | Minor |
|---|---|---:|---:|---:|
| Hostile Review A | REVISE | 0 | 1 | 3 |
| Hostile Review B | ACCEPT | 0 | 0 | 0 |

Review A found no mathematical counterexample but required direct-owner
subtraction, source/version repair, evidence-language correction, and an
explicit formal/analytic bridge.  Independent Review B rederived the repaired
theorem and closed every finding.

## Review-A findings and closure

| item | repair | Review-B result |
|---|---|---|
| M1, Major: Sericola's generic joint time/place law and moments and Chen's general-tree PGF algorithm were omitted | Both primary owners now appear in the bibliography, source ledger, ownership table, prose subtraction, and limitations.  Generic laws, rationality, algorithms, and moment availability receive zero credit. | CLOSED |
| m1, Minor: de la Iglesia--Juarez was cited only as a preprint | The journal version of record is now used: *J. Math. Anal. Appl.* 517(2), 126624 (2023), DOI `10.1016/j.jmaa.2022.126624`; arXiv remains only an access route. | CLOSED |
| m2, Minor: one-attempt derivative checks were overstated as independent | The manuscript and ledgers now say exact/additional.  The shared continuant-derivative engine is disclosed; only the literal-state versus rational-series comparison is described as separately assembled. | CLOSED |
| m3, Minor: the formal renewal series was not explicitly connected to evaluation at one | The proof now states `Q(0)=0`, `Q(1)=1-H/r<1`, and `D(1)=H product ell_j>0`, separately licensing the formal inverse, almost-sure renewal, and endpoint/moment evaluation. | CLOSED |

## Accepted residual after owner subtraction

No contribution credit is assigned to generic finite-chain joint
time/place laws or moment matrices, generic tree hitting-time PGF algorithms,
general gambler's ruin or continuants, endpoint probabilities, the mean
formula, equal-arm star laws, spider spectral/factorization frameworks, or
general network tomography.

The accepted residual is limited to:

1. the explicit unequal-spider continuant product for the labelled leaf-
   marked first-passage law;
2. the compact unequal-spider scalar variance specialization and its stopped-
   renewal derivation;
3. sharp fixed-total integer mean extremizers with complete equality classes;
   and
4. the exact endpoint-ray/common-dilation boundary, with the mean recovering
   scale for model-generated exact data.

The source audit is a bounded primary-source non-hit, not a novelty, priority,
authorship, freedom-to-operate, or release certificate.

## Review-B evidence

- A cold verifier replay matched `verification_output.txt` byte for byte and
  passed **1,446,432** exact integer/`Fraction` assertions.
- A separate exact absorbing-linear-system implementation reproduced endpoint
  probabilities, means, and variances on adversarial unequal profiles without
  importing the manuscript's quotient-derivative code.
- Two isolated clean
  `pdflatex -> bibtex -> pdflatex -> pdflatex` builds were mutually
  byte-identical and byte-identical to the packaged current PDF.
- The current `main.pdf`/`main_round1.pdf` is 6 A4 pages, 356,664 bytes, with
  SHA-256
  `24fddbfb896510cf2712a8ade2a3ac37d04712676f635e39f1170c4cc334e8d9`.
- Every one of the six current pages was inspected at original detail; no
  clipping, overlap, blank page, corrupt glyph, unresolved marker, anonymity
  leak, or other visible defect was found.

## Decision and freeze boundary

P151 is internally accepted at Round 2 with **0 surviving Critical, Major, or
Minor findings**.  Root archived `main_round2.pdf` as a read-only,
byte-identical copy of the accepted current PDF and regenerated the final
paper-local manifest.  That historical-copy and manifest step does not reopen
the theorem review.  External status remains **`HOLD_EXTERNAL`**.
