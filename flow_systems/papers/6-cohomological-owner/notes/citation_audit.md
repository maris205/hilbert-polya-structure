# Paper 6 Citation and Source-Integrity Audit

Audit date: **2026-08-13**  
Audit mode: independent, read-only citation/source review  
Manuscript: `paper/manuscript.tex`  
Decision: **ACCEPT**

## 1. Decision

The current manuscript passes the citation and source-integrity gate.  There
are **no mandatory revisions** and no source-faithfulness defect remains.

The audit checked the final candidate locked by these SHA-256 values:

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `d36783ebbfabd67fdda7f04d1aae3556e72b137e51985b7cd6448a35f0cb8219` |
| `paper/references.bib` | `9cae6271cefad92c78de9a4cb9533fb12503760e11f05b3f06d240cef1c67e05` |
| `paper/paper.pdf` | `f8eccdd7d486a10885d6f5502ad929f08d5ce27b14cb2457f1de8999b9f14573` |
| `notes/source_audit.md` | `1d97fe0c8435f3f916e67076bd2a1e91f2fdc8db6aacc0bd4493b5bb3e8f45b8` |

## 2. Citation-accounting summary

| Check | Result |
|---|---:|
| BibTeX entries | 6 |
| Cited BibTeX entries | 6 |
| Uncited bibliography entries | 0 |
| In-text citation keys absent from bibliography | 0 |
| Distinct citation commands | 10 |
| BibTeX warnings | 0 |
| Undefined citations or references | 0 |
| Metadata/DOI discrepancies affecting identity | 0 |
| Unsupported or overstated source-backed claims | 0 |

All bibliography records are cited at least once.  Every manuscript citation
key resolves, and the final `.bbl` contains the same six records.  The one
remaining LaTeX diagnostic is a non-citation-related underfull box.

## 3. Reference existence and metadata

| Key | Identity check | Audit result |
|---|---|---|
| `Deligne1974` | Numdam record; *Publications Mathématiques de l'IHÉS* 43 (1974), 273--307; DOI `10.1007/BF02684373` | **verified** |
| `Koopman1931` | original four-page PNAS scan, 17(5), 315--318; DOI `10.1073/pnas.17.5.315` | **verified**; the final record correctly follows the printed plural title, “Transformations” |
| `Stone1932` | *Annals of Mathematics* 33(3), 643--648; DOI `10.2307/1968538` | **verified** |
| `TerElstLemanczyk2017` | Cambridge journal record, 37(5), 1635--1656; DOI `10.1017/etds.2015.111` | **verified** |
| `Teschl2009` | AMS GSM 99, 2009, ISBN `978-0-8218-4660-5`, DOI `10.1090/gsm/099` | **verified as the first edition** |
| `StacksTrace2026` | Stacks Project, Chapter 64, Tag `03SJ`, local copy compiled 14 July 2026 | **verified** as a living supporting source |

The PNAS publisher endpoint returned HTTP 403 during review.  This is an
access restriction, not an identity failure: the local four-page scan was
matched by printed title, author, volume, issue, pagination and DOI metadata.
The source audit discloses this rather than presenting the mirror as a
publisher copy.

## 4. Load-bearing claim-to-source audit

### 4.1 Deligne: orbit, trace, and determinant owner

**SUPPORTED.**  Deligne §1.1 defines the closed-point product and the native
variable \(t=q^{-s}\); §1.4 identifies closed points with finite Frobenius
orbits and records the divisor-sum point count; equations (1.5.1)--(1.5.4)
give the alternating compact-support trace and graded determinant.  These
locators support the manuscript's three uses of `Deligne1974`.

The previously risky convention boundary is now closed in the final text.
The manuscript fixes \(\ell\ne2\), defines

\[
 H^i_{\rm et}=H^i_{\rm et}(X_{\overline{\mathbb F}_2},\mathbb Q_\ell),
 \qquad \Phi=F^*,
\]

and states that \(F^*\) is exactly the pullback appearing in Deligne's
equations (1.5.1)--(1.5.4).  It separately keeps the point permutation as the
square map and notes that inversion reverses finite cycles without changing
their degrees.  Thus the trace eigenvalues \((1,2)\) and
\(Z(\mathbb P^1,t)=((1-t)(1-2t))^{-1}\) are not obtained by silently mixing
arithmetic- and geometric-Frobenius conventions.

The source is not overextended: the manuscript does not attribute a complex
Hilbert structure, self-adjoint Hamiltonian, logarithm branch, unitary
equivalence or Riemann-ξ determinant to Deligne.

### 4.2 Teschl and Stone: complete operator and spectrum

**SUPPORTED.**  The local PDF title page identifies the book as Gerald
Teschl, *Mathematical Methods in Quantum Mechanics*, GSM **99**, AMS,
**2009**, ISBN `978-0-8218-4660-5`, version 12 February 2009.  It is not the
2014 second edition (GSM 157).  The final BibTeX record and source audit now
use the correct first-edition metadata.

The cited locators were checked directly:

- Theorem 2.23, printed pp. 79--80: countable orthogonal sums of
  self-adjoint operators, maximal graph domain, resolvent direct sum, and
  spectrum equal to the closure of the union of component spectra;
- Theorems 5.1--5.2, printed pp. 123--125: the self-adjoint-generator and
  strongly/weakly continuous unitary-group correspondence;
- §6.4, printed pp. 145--147: the self-adjoint essential-spectrum
  characterization and singular Weyl-sequence criterion.

The manuscript uses the first two locators explicitly at the operator proof.
Its essential-spectrum argument is also source-faithful: it constructs the
singular Weyl sequence directly, while the source audit records the §6.4
framework.  Compact-resolvent and heat-trace failure are then proved
internally from infinite-dimensional eigenspaces rather than falsely
attributed to Stone or Teschl.

### 4.3 Koopman-group sources

**SUPPORTED.**  Koopman's printed pp. 315--317 construct the invariant-measure
\(L^2\) space and unitary composition group.  The manuscript does not import
the historical paper's analytic Hamiltonian hypotheses into the disjoint
circle model; translation invariance and strong continuity are proved for
the frozen model.  Ter Elst--Lemańczyk gives the modern \(C_0\)-Koopman-group
context and the need to specify the measure/action hypotheses.  The exact
circle Fourier spectrum remains an internal calculation.

There is a metadata nuance with no remaining defect: some DOI/Crossref
records normalize Koopman's title to singular “Transformation,” but the
original printed headline is plural “Transformations.”  The final BibTeX and
source audit correctly follow the primary manifestation.

### 4.4 Stacks Project supporting role

**SUPPORTED WITH CORRECT BOUNDARY.**  Tag `03SJ` is the trace-formula section;
the locally locked Chapter 64 copy includes the dimension-one formula and
explicitly distinguishes arithmetic from geometric Frobenius.  The
manuscript uses Stacks only as a modern convention check and states that
Deligne remains the load-bearing source.  This avoids replacing a primary
theorem with a living exposition.

### 4.5 Claims proved by this paper or its deterministic artifacts

The all-degree positivity lemma, periodic-circle Fourier diagonalization,
infinite multiplicity, full/essential spectrum, heat obstruction,
non-equivalence, direct-sum obstruction, and \(t=2^{-s}\) pole-lattice lift
are proved in the manuscript and checked against the proof/reproduction
artifacts.  They do not require an external citation for their truth.  The
finite tables are described as regression checks rather than evidence for
the infinite theorems, so there is no data-to-claim inflation.

## 5. Local-source integrity

| Local source | SHA-256 | Page count / identity |
|---|---|---|
| `deligne-weil-i.pdf` | `8392b345d4854e6dc55fb42cfc0b616d941935983723627237239a87348f42e5` | 36 pages; title/author embedded |
| `koopman-1931.pdf` | `1e8042406f9e450c288573536a423c727bd1237083324545f188966b6ebee767` | 4 printed PNAS pages |
| `stacks-trace.pdf` | `99d5358fe636cb18afa5a81f93c7906995db2a02a15efd742ba90e07cb74c828` | 45 pages; version line present |
| `ter-elst-lemanczyk-koopman-groups.pdf` | `9dcf83e9318360ed5211ef4844f224973d15213f907e2e891512c4ddfebb1a56` | 23 pages; title/authors and arXiv version present |
| `teschl-mathematical-methods-qm.pdf` | `8dc8de0b58aa0a3fedfe594a345f9b5875322e5526ea581cb640a98d55b82818` | 317 pages; GSM 99/2009 title page present |

ARS PDF read-integrity preflight returned `UNAVAILABLE` for all five local
PDFs because `pypdf` is not installed in the environment.  Following the
protocol, this was not promoted to `PASS`, nor treated as evidence against a
page anchor.  Content was instead located independently with Poppler
(`pdfinfo` plus page-scoped `pdftotext`) and matched by equation, theorem,
title-page and section text.  This is a nonblocking read-integrity advisory.

## 6. Mandatory revisions and advisories

### Mandatory revisions

**None.**

### Nonblocking advisories

1. Keep the explicit \(\ell\), \(\Phi=F^*\), and point-map convention paragraph
   unchanged in any later copy edit; shortening it would reopen the primary
   convention risk.
2. If the local PDF toolchain later gains `pypdf`, regenerate and retain
   preflight sidecars before reusing physical-page anchors.  The present
   content-based check is sufficient for this release but is not a machine
   `PASS` under the ARS page-anchor protocol.
3. If the Stacks Project record is refreshed, update the compiled-version and
   access-date note together; it is a living reference.

## 7. Final integrity statement

The bibliography is real and complete, every reference is used, the
load-bearing cited claims match the retrieved source text, and the manuscript
does not splice Deligne's determinant credit into the Koopman operator.  The
2009 Teschl edition and theorem numbering are correct.  The current lock is
therefore **ACCEPTED** for citation and source integrity.
