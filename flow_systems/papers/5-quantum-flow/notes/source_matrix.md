# Source Matrix — Koopman/Stone Audit

Audit date: 2026-08-13  
Candidate: `FF-FROB-SUSP-P1-F2-KOOPMAN-P1`  
Corpus policy: original papers, official journal/publisher records, and an
author-hosted research text; no tertiary theorem source

## 1. Source-lock result

The corpus is sufficient for every external input used in the Phase 1 theorem
audit:

1. the finite-field closed-point count in every degree;
2. the standard Koopman pullback convention;
3. Stone generation and countable orthogonal sums of self-adjoint operators;
4. the distinction between discrete and essential spectrum;
5. the trace-class boundary of the ordinary Fredholm determinant;
6. the finite-dimensional etale-cohomological Frobenius determinant.

The candidate-specific spectrum, multiplicity, noncompactness, and heat-trace
obstructions are proved directly in `research_protocol.md` and
`candidate_lock.md`. They are not copied from an example with a different
operator.

## 2. Search and inclusion protocol

- **Last searched:** 2026-08-13.
- **Search surfaces:** DOI records, official journal/publisher pages, arXiv,
  and author-maintained publication pages.
- **Core queries:** combinations of “one-parameter Koopman group generator,”
  “Stone one-parameter unitary group,” “orthogonal sum self-adjoint spectrum,”
  “number irreducible polynomials finite field degree,” “Weil I Frobenius
  determinant,” and “Fredholm determinant trace class.”
- **Inclusion rule:** a source had to state a definition or theorem used at an
  exact interface in the audit; original papers and authoritative
  author/publisher texts were preferred.
- **Exclusion rule:** tertiary summaries, search snippets without a checked
  record, physics analogy without a domain theorem, and any source whose role
  would require importing a different operator.
- **Stopping rule:** stop once each external interface had one primary or
  authoritative checked source and the candidate-specific conclusions could be
  derived directly.

No target-zero or rational-prime dataset was searched or used.

## 3. Acquired local corpus

| Key | Bibliographic identity and authoritative URL | Local artifact | SHA-256 | Verified locator | Role |
|---|---|---|---|---|---|
| `TES09` | Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, 1st ed., AMS GSM 99 (2009), [author-authorized online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf) | `sources/teschl_mathematical_methods_qm.pdf` | `8dc8de0b58aa0a3fedfe594a345f9b5875322e5526ea581cb640a98d55b82818` | §1.4; §2.5, Theorem 2.23; §5.1, Theorems 5.1--5.2; §§6.3--6.4 | Hilbert direct sums, self-adjoint direct sums, Stone theorem, trace class, essential/discrete spectrum |
| `TEL17` | A. F. M. ter Elst and M. Lemańczyk, “On one-parameter Koopman groups,” *Ergodic Theory and Dynamical Systems* 37(5) (2017), 1635--1656, [DOI 10.1017/etds.2015.111](https://doi.org/10.1017/etds.2015.111), [author copy](https://www-users.mat.umk.pl/~mlem/files/ElstLe.pdf) | `sources/ter_elst_lemanczyk_koopman_groups.pdf` | `9dcf83e9318360ed5211ef4844f224973d15213f907e2e891512c4ddfebb1a56` | Introduction; Theorem 1.1; sigma-finite extension noted as Theorem 2.8 | authoritative Koopman group definition and generator context |
| `NX09` | Harald Niederreiter and Chaoping Xing, “Finite Fields and Function Fields,” Chapter 1 of *Algebraic Geometry in Coding Theory and Cryptography*, Princeton UP (2009), 1--29, [DOI 10.1515/9781400831302-002](https://doi.org/10.1515/9781400831302-002) | `sources/niederreiter_xing_ch1_finite_fields.pdf` | `fcdc6f3df9bc3068d707ee414187529c2b0b1d9c21865ce0a7426a0c8de0b0d6` | §1.3, Theorem 1.3.6 | exact number of monic irreducibles of degree \(d\) |
| `DEL74` | Pierre Deligne, “La conjecture de Weil I,” *Publ. Math. IHES* 43 (1974), 273--307, [DOI 10.1007/BF02684373 and official NUMDAM record](https://www.numdam.org/item/PMIHES_1974__43__273_0/) | `sources/deligne_weil_I_1974.pdf` | `8392b345d4854e6dc55fb42cfc0b616d941935983723627237239a87348f42e5` | §1.4; equation (1.5.4) | closed points as Frobenius orbits and the cohomological determinant ledger |
| `BOR10` | Folkmar Bornemann, “On the Numerical Evaluation of Fredholm Determinants,” *Mathematics of Computation* 79 (2010), 871--915, [DOI 10.1090/S0025-5718-09-02280-7](https://doi.org/10.1090/S0025-5718-09-02280-7), [arXiv:0804.2543](https://arxiv.org/abs/0804.2543) | `sources/bornemann_fredholm_determinants_2008.pdf` | `0652a97dcc57ec8727dbef4f60d14cb22c7b428b8551e3ecf67464803bde798a` | §§2--3, especially “Definition and Properties of Fredholm and Operator Determinants” | ordinary operator determinant for trace-class operators; product, Plemelj, and exterior-power formulations |

All corresponding plain-text extractions are stored beside the PDFs with a
`.txt` suffix.

### Edition correction

The acquired Teschl hash is the **first edition, GSM 99 (2009)**, as its title
page and ISBN `978-0-8218-4660-5` show. The author page also lists a second
edition (GSM 157, 2014), but this audit cites theorem locators in the acquired
first-edition file. The two editions must not be conflated.

## 4. PDF read audit

The ARS PDF preflight script was run on every acquired PDF. Every JSON report
returned `UNAVAILABLE` solely because `pypdf` is not installed:

| Artifact | `pdfinfo` page count | Preflight JSON |
|---|---:|---|
| Bornemann | 43 | `sources/bornemann_fredholm_determinants_2008.pdf.preflight.json` |
| Deligne | 36 | `sources/deligne_weil_I_1974.pdf.preflight.json` |
| Niederreiter--Xing | 29 | `sources/niederreiter_xing_ch1_finite_fields.pdf.preflight.json` |
| ter Elst--Lemańczyk | 23 | `sources/ter_elst_lemanczyk_koopman_groups.pdf.preflight.json` |
| Teschl | 317 | `sources/teschl_mathematical_methods_qm.pdf.preflight.json` |

`pdfinfo` and `pdftotext` both succeeded. Therefore section, theorem, and
equation labels were verified in extracted text, but PDF reader-page anchors
were **not** preflight-certified and are deliberately omitted. A future
composition phase may install a compatible parser or visually certify pages;
it must not silently upgrade the current locator status.

## 5. Historical metadata, not load-bearing theorem sources

| Key | Record | Use and boundary |
|---|---|---|
| `KOO31` | Bernard O. Koopman, “Hamiltonian Systems and Transformations in Hilbert Space,” *PNAS* 17(5) (1931), 315--318, [DOI 10.1073/pnas.17.5.315](https://doi.org/10.1073/pnas.17.5.315) | historical provenance for representing dynamics on Hilbert space; no candidate-specific theorem is attributed to it |
| `STO32` | Marshall H. Stone, “On one-parameter unitary groups in Hilbert space,” *Annals of Mathematics* 33(3) (1932), 643--648, [DOI 10.2307/1968538](https://doi.org/10.2307/1968538) | original Stone-theorem provenance; the checked working statement is `TES09`, Theorems 5.1--5.2 |
| `KOS70` | Bertram Kostant, “Quantization and Unitary Representations,” in *Lectures in Modern Analysis and Applications III*, LNM 170 (1970), [DOI 10.1007/BFb0079068](https://doi.org/10.1007/BFb0079068) | historical geometric-quantization context for why a Koopman representation alone does not freeze prequantum/polarization data; no impossibility claim is inferred |

No local full-text hash is claimed for these three records. Their metadata were
verified through DOI/journal or publisher records; all load-bearing operator
statements are independently present in the acquired Teschl text.

## 6. Claim-to-source matrix

| Claim ID | Exact input or conclusion | Source support | Candidate-specific proof location | Status |
|---|---|---|---|---|
| `S1` | Koopman pullback is \(U_Tf=f\circ T\), unitary for invertible measure-preserving \(T\) | `TEL17`, Introduction | `research_protocol.md` §6 checks invariance and the chosen inverse-flow sign | `PROVED` |
| `S2` | A continuous one-parameter Koopman family is a \(C_0\)-group; Stone supplies its generator | `TEL17`, Introduction/Theorem 1.1; `TES09` §5.1 | direct finite-support approximation proves strong continuity | `PROVED` |
| `S3` | Countable Hilbert direct sums and self-adjoint operator sums are legitimate | `TES09` §1.4 and §2.5, Theorem 2.23 | domain and periodic boundary conditions stated explicitly | `PROVED` |
| `S4` | Spectrum of \(\bigoplus_xA_x\) is the closure of the union of component spectra | `TES09`, Theorem 2.23 | union is \((2\pi/\log2)\mathbb Q\), whose closure is \(\mathbb R\) | `PROVED` |
| `S5` | Discrete spectrum consists of isolated finite-multiplicity eigenvalues; essential spectrum is the remainder / has the Weyl-sequence test used here | `TES09` §§6.2--6.4 | rational and irrational singular Weyl sequences constructed explicitly | `PROVED` |
| `S6` | Number of monic irreducibles is \(I_q(d)=d^{-1}\sum_{e\mid d}\mu(e)q^{d/e}\) | `NX09`, Theorem 1.3.6 | direct inequality proves \(I_2(d)>0\) for all \(d\ge2\); infinity gives the extra degree-one point | `PROVED` |
| `S7` | Closed points are finite Frobenius orbits and degree is orbit cardinality | `DEL74` §1.4; also inherited Paper 4 audit | identifies each \(d\) with a suspension circumference \(d\log2\) | `PROVED` |
| `S8` | Degree-\(d\) circle generator has frequencies \(2\pi n/(d\log2)\) | standard periodic Fourier calculation; `TES09` supplies operator framework | explicit normalized basis and derivative calculation in §7 | `PROVED` |
| `S9` | \(\sigma_{\rm p}(A_w)=(2\pi/\log2)\mathbb Q\) and each point eigenvalue has infinite multiplicity | no external example invoked | degree-\(kb\), mode-\(ka\) construction | `PROVED` |
| `S10` | \(\sigma(A_w)=\sigma_{\rm ess}(A_w)=\mathbb R\) while the eigenvectors form a complete pure-point basis | `TES09`, direct-sum theorem and spectral-type definitions | exact eigenspaces plus irrational singular Weyl sequences | `PROVED` |
| `S11` | No compact resolvent and no finite-rank projection for any interval of positive width | compactness definitions in `TES09`; proof is direct | resolvent acts by one nonzero scalar on an infinite orthonormal eigenspace; every positive-width interval contains a rational eigenvalue | `PROVED` |
| `S12` | \(e^{-tA_w^2}\), \(e^{-t|A_w|}\), and \((1+A_w^2)^{-s/2}\) are not trace class | `TES09` §6.3 for trace-class framework | each is nondecaying on an infinite-dimensional eigenspace; zero deletion control uses a nonzero rational eigenspace | `PROVED` |
| `S13` | Ordinary \(\det(I+zK)\) has the canonical operator-determinant theory for trace-class \(K\) | `BOR10` §3 | required trace-class inputs fail for the frozen generator/group | `PROVED` boundary |
| `S14` | Hasse--Weil zeta has an alternating finite-dimensional etale-cohomological Frobenius determinant | `DEL74` equation (1.5.4) | ledger table compares its space/action with \(A_w\) | `PROVED` different-operator result |
| `S15` | Shared arithmetic origin is not an operator conjugacy or determinant identity | Paper 3 same-object certificate T0--T7 | no bridge morphism or same-operator trace identity exists in frozen data | `PROVED` logical boundary / absent bridge `NOT_TESTABLE` |
| `S16` | Positive component weights do not change the unitary equivalence class | no external theorem needed | \(W_wf=(\sqrt{w_x}f_x)_x\) intertwines group and generator | `PROVED` |

## 7. Source-specific audit notes

### `TEL17`: scope of the Koopman citation

The paper defines a Koopman one-parameter group by composition with measurable
maps and studies the generator characterization. Its introduction works first
with a standard Borel probability space and points to the sigma-finite
generalization in Theorem 2.8. The present candidate does not depend on the
converse characterization: its maps and invariant measure are explicit, so
unitarity and strong continuity are proved directly. This avoids importing
unneeded probability or ergodicity hypotheses.

The source often calls the \(C_0\)-group generator skew-adjoint under the
semigroup convention \(U_t=e^{tG}\). This audit instead freezes the
self-adjoint Stone convention \(U_t=e^{-itA_w}\), so \(G=-iA_w\). The
conversion is recorded; the two conventions are not contradictory.

### `TES09`: exact direct-sum use

Theorem 2.23 states both self-adjointness of the orthogonal sum and closure of
the union of component spectra. It does not itself calculate the periodic
circle spectrum or multiplicities. Those are direct Fourier calculations in
the frozen object. Similarly, the Weyl-sequence construction at irrational
accumulation points is candidate-specific.

### `NX09` and `DEL74`: why every denominator occurs

`DEL74` supplies the closed-point/Frobenius-orbit dictionary. `NX09` supplies
the exact irreducible-polynomial count. On \(\mathbb A^1_{\mathbb F_2}\), each
degree-\(d\) monic irreducible gives a closed point; the point at infinity adds
one degree-one point. The positivity inequality is written in full because the
spectral proof needs existence for all degrees, not only an asymptotic.

### `BOR10`: determinant claim boundary

The citation supports the standard trace-class Fredholm determinant, including
equivalent product, finite-rank-limit, Plemelj, and exterior-power
descriptions. It is used only to state that the ordinary operator determinant
is unavailable for the frozen non-trace-class inputs. The audit does not use
the stronger and generally false claim that *all conceivable* regularized or
relative determinants are impossible. Such a construction would introduce
new choices and a new candidate.

### `DEL74`: cohomology is not Koopman space

Equation (1.5.4) acts on compactly supported etale cohomology and takes an
alternating product over cohomological degree. Nothing in `DEL74` identifies
that finite-dimensional Frobenius action with the circle derivative
\(-i\,d/du\). The equality of the Paper 4 orbit product with Hasse--Weil zeta
must therefore remain in the orbit/cohomology ledger, not be relabeled a
Koopman spectral determinant.

## 8. Evidence limitations

1. No page-level anchors are claimed because the ARS parser preflight was
   unavailable. Stable theorem, section, and equation labels are used.
2. `TES09` is an author-hosted, AMS-authorized first-edition text, not the
   second edition listed elsewhere.
3. `TEL17` supplies general terminology; the exact sigma-finite candidate is
   verified directly rather than by a black-box invocation.
4. The local `BOR10` artifact reflects the arXiv manuscript stream and its
   extracted title page carries a later manuscript timestamp. The stable
   scholarly identity is arXiv:0804.2543 and the 2010 AMS publication; only
   timeless §§2--3 operator facts are used.
5. No source in the corpus provides a physical quantization of this
   suspension. That absence is reported as `NOT_TESTABLE`, not as an
   impossibility theorem.
6. No source is used to infer a Riemann-zero correspondence.

## 9. Reproducibility commands

Run from the workspace root:

```bash
sha256sum papers/5-quantum-flow/notes/sources/*.pdf
pdfinfo papers/5-quantum-flow/notes/sources/teschl_mathematical_methods_qm.pdf
rg -n "Theorem 2.23|Theorem 5.2" \
  papers/5-quantum-flow/notes/sources/teschl_mathematical_methods_qm.txt
rg -n "Theorem 1.3.6" \
  papers/5-quantum-flow/notes/sources/niederreiter_xing_ch1_finite_fields.txt
rg -n "1.5.4" \
  papers/5-quantum-flow/notes/sources/deligne_weil_I_1974.txt
rg -n "Definition and Properties of Fredholm" \
  papers/5-quantum-flow/notes/sources/bornemann_fredholm_determinants_2008.txt
```

These commands verify artifact identity and locator presence. They do not
replace the mathematical derivations recorded in the protocol.
