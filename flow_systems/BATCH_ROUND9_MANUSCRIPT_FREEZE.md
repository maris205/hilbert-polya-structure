# Batch Round 9 manuscript freeze — Papers 24–28

Date: 2026-08-28
Pipeline position: ARS Stage 2 (`WRITE`)
Route position: Route A only; Route B entry remains unauthorized

## 1. Round objective

Round 9 converts the proved and numerically certified Stage-1 results of
Papers 24–28 into five relatively complete, independently readable research
manuscripts.  A manuscript is not complete merely because it contains a main
theorem.  Every Round-9 paper must contain a motivated research question,
definitions, prior-work positioning, theorem statements, proofs, a transparent
computational or certificate method where applicable, a discussion of the
Route-A consequences, limitations, a conclusion, references, and the required
publication declarations.

This round is a manuscript-completion round.  It does not reopen frozen
candidate definitions, fit parameters to target primes or Riemann zeros, or
promote any candidate to Route B.

## 2. Common paper configuration

| Field | Frozen value |
|---|---|
| Paper type | theoretical/computational mathematics article |
| Discipline | dynamical systems, arithmetic geometry, spectral theory |
| Target venue | general field journal; no venue-specific compliance claimed |
| Body language | English |
| Abstracts | independent English and Traditional-Chinese abstracts |
| Citation system | `plainnat` numerical citations, preserving the project decision |
| Primary output | `manuscript.tex`, `references.bib`, compiled `paper.pdf` |
| Target size | 4,000–6,500 English body words per paper, excluding references |
| Author | Liang Wang |
| Affiliation | School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Luoyu Road 1037, 430070, Hubei, P.R. China |
| Contact | `wangliang.f@gmail.com` |
| Funding | no funding |
| Conflict of interest | none |
| Citation policy | source existence and claim support must be checked; no fabricated references |
| Retraction policy | mark-only unless a current undisputed retraction is found |
| Data policy | repository artifacts and deterministic scripts are the paper data |

The previously confirmed single-author CRediT statement is used: Liang Wang is
responsible for conceptualization, methodology, software, validation, formal
analysis, investigation, data curation, writing (original draft and review),
visualization, and project administration.

## 3. Mandatory manuscript anatomy

Each paper must contain all of the following:

1. title and full author block;
2. English abstract of 150–300 words and 5–7 keywords;
3. independently composed Traditional-Chinese abstract of 300–500 Chinese
   characters and 5–7 keywords;
4. introduction with a precise research question and contribution list;
5. mathematical setting and definitions;
6. related-work section using only checked sources;
7. main results with explicit evidence labels;
8. complete proofs of the theorem-level claims credited to the paper;
9. computational/certificate method and exact reproducibility path, when used;
10. adversarial-control or proves-too-much analysis;
11. Route-A interpretation that keeps A0–A4 separate;
12. limitations and open obligations;
13. conclusion;
14. Data and Code Availability, Ethics Declaration, Author Contributions,
    Conflict of Interest, Funding, and AI-Assisted Research Disclosure;
15. a `plainnat` bibliography with zero citation orphans.

The PDF must compile from LaTeX.  HTML-to-PDF conversion is not allowed.

## 4. Paper-specific locks

### Paper 24

Working title: **Congruence Trace Universality and the Limits of First-Jet
Separation in Bianchi Holonomy**.

Central result: for a commutative ring `R`, a non-zero-divisor `m`, and
`gamma = I + mA` in `SL_2(R)`, prove

```text
(tr(gamma)^2 - 4)/m^2 = m^2 det(A)^2 - 4 det(A),
```

together with the conjugacy, inversion, and power laws for the first jet.  The
11,481-row level-3 Bianchi ledger and the four frozen control families quantify
the separation gain and the remaining collisions.

Claim boundary: the theorem establishes universality and a necessary
congruence invariant.  It does not establish prime-ideal ownership.  Four
executed frozen families cover only two of the three canonical Route-A A0
control types, so the mandatory canonical-control gate remains `2/3`.

### Paper 25

Working title: **Why a Unit-Roof Symbolic Determinant Does Not Transfer to the
Physical Three-Disk Flow**.

Central result: derive the exact period means

```text
T_2/2 = d - 2a,       T_3/3 = d - sqrt(3)a,
```

prove the physical roof is not cohomologous to a constant, and prove that no
owner- and repetition-preserving scalar substitution `z = exp(-cs)` transfers
the unit-roof symbolic determinant to the physical clock.  The 2,241-row
replay is supporting evidence, not the proof.

Claim boundary: the theorem rejects only scalar constant-roof transfer.  It
does not compute or reject the genuine nonconstant-roof transfer operator or
the Gutzwiller–Voros determinant.

### Paper 26

Working title: **Exact Newform-Period Taxonomy for a Level-11 Time Change of
the Modular Geodesic Flow**.

Central result: present the exact real involution and normalized period
coordinate, then prove the complete 138-instance/55-group taxonomy: two full
complex kernels, two real-projection-only cases, 134 true nonkernels, and no
unresolved cases.  State and prove the group-level failures of the frozen
moment laws.

Claim boundary: the finite exact taxonomy refutes the tested naive Hecke-like
recurrences.  It is not a theorem about all modular geodesics, a global
transfer determinant, or a rational-prime owner map.

### Paper 27

Working title: **Renormalization Obstructions in Congruence and Homology
Towers of Geodesic Flows**.

Central result: for the genus-two pure homology cover `H_N`, prove degree
`N^4`, deck order `N` for a primitive owner, `N^3` primitive lift components,
and physical lift period `N ell(g)`.  Derive the four determinant-factor
quadrants and show why only the fully renormalized fixed finite panel reproduces
the base factor.

Claim boundary: the positive identity is a finite-panel identity.  It does not
extend to the full primitive spectrum or prove residuality, and it cannot be
used as a Route-A A2 certificate.

### Paper 28

Working title: **An Exact Systole and Finite Enumeration Certificate for a
Nonarithmetic Genus-Two Octagon**.

Central result: for the frozen Nazarenko exponential-octagon surface, prove

```text
sys = 2 acosh(1/(2 exp(-1/5) - 1)),
```

with primitive equality witness `g_0 g_3`, exact Gaussian-integer polynomial
`PSU(1,1)` normal forms, and the compact tile-chain theorem that makes the
18,533-state enumeration complete through the target-blind cutoff
`Lambda = 21/10`.

Claim boundary: 144 equality group elements are not asserted to be 144 owner
classes.  The paper certifies the control geometry and cutoff only; it does not
run a Bolza/control census, magnetic comparison, A2 experiment, or Route-B
audit.

## 5. Evidence and data firewall

- No target prime table or Riemann-zero table may enter a candidate definition,
  parameter choice, cutoff, theorem proof, or manuscript figure.
- Numerical displays must be derived from frozen exact artifacts.
- `PROVED`, `NUMERICALLY_CERTIFIED`, `NUMERICAL_OBSERVATION`, `OPEN`, and
  `REFUTED` must not be conflated.
- A Route-A failure or no-go theorem is a valid paper result, but it cannot be
  written as a positive Hilbert–Pólya realization.
- Route-B evaluation files must not be created in this round.

## 6. Stage boundary

Completion of all five manuscript packages closes ARS Stage 2 only.  Entry to
Stage 2.5 (`INTEGRITY`) requires an explicit user confirmation after the five
drafts, compilation receipts, and Stage-2 dashboard are presented.
