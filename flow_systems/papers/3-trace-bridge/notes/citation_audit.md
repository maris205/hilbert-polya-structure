# Paper 3 Citation and Claim-Alignment Audit

Audit date: **2026-08-13**  
Artifact audited: `paper/paper.pdf` and `paper/manuscript.tex`  
Bibliography style: numeric `plainnat`  
Decision: **MINOR REVISION** before release freeze

## 1. Executive result

The bibliography is real, internally complete, and well aligned with the
paper's deliberately schematic use of the cofinite Selberg formula.  BibTeX
reports 10 entries and zero warnings; every entry is cited and every citation
key is defined.  No retracted, fabricated, duplicate or obvious wrong-source
entry was found.

Two small changes are mandatory before final release:

1. The English abstract must add the singular-support qualification to the
   “all nonzero singular germs” sentence.  The theorem is correct only after
   the set `P` is assumed to contain every possible nonzero singular location.
   The full text states this exactly; the abstract currently suppresses the
   hypothesis and is therefore stronger than the proved claim.
2. The Selberg DOI currently resolves to a 404 target even though the article
   and DOI metadata are bibliographically established.  Keep the DOI, but add
   a stable archive/metadata URL (the CERN bibliographic record is already
   source-locked) and describe the live DOI endpoint as unavailable on the
   audit date rather than as a successful full-text manifestation.

The absence of a locally acquired Selberg/Hejhal full convention is disclosed
in the manuscript and does not invalidate the paper's theorem, because the
manuscript prints only a typed schematic cofinite identity and proves the
clock-support obstruction independently.  It does mean that no unprinted
constant, sign, exact Fourier convention or equation locator may be credited
to those sources in the final claim ledger.

## 2. Mechanical citation checks

| Metric | Result |
|---|---:|
| bibliography entries | 10 |
| entries cited in text | 10 |
| undefined in-text citation keys | 0 |
| uncited bibliography entries | 0 |
| BibTeX warnings | 0 |
| unresolved cross-references | 0 |
| duplicate bibliographic identities | 0 |
| references with DOI | 9 |
| arXiv/URL-only reference | 1 (`Kordyukov2001`) |
| references from 2021--2026 | 2 |
| foundational pre-2000 references | 7 |
| author self-citations | 0 |

The old-source concentration is appropriate: the paper audits original trace
theorems rather than surveying an empirical frontier.  The 2024/2026 ALKL
source supplies the current foliated-flow endpoint.

## 3. Reference-by-reference verification

| Key | Bibliographic identity | Live/official check | Claim use | Verdict |
|---|---|---|---|---|
| `Deninger2026` | C. Deninger, *Dynamical Systems for Arithmetic Schemes*, *Indagationes Mathematicae* 37(1), 25--136 | DOI `10.1016/j.indag.2024.05.007` resolved; local arXiv v4 SHA is recorded | packet exhaustion, prime-indexed period law, missing frozen trace/operator data | **PASS**; v4 manifestation disclosure retained |
| `DuistermaatGuillemin1975` | J.J. Duistermaat and V.W. Guillemin, *Invent. Math.* 29, 39--79 | DOI `10.1007/BF01405172` resolved; local scan audited | local wave-trace singular structure under elliptic/clean hypotheses | **PASS** |
| `Selberg1956` | A. Selberg, *J. Indian Math. Soc.* 20, 47--87 | article metadata verified; DOI `10.18311/JIMS/1956/16985` currently lands on 404 | original trace-formula provenance and framework only | **PASS WITH URL FIX**; no formula-level locator claimed |
| `Hejhal1983` | D.A. Hejhal, LNM 1001, Springer, 810 pp. | DOI `10.1007/BFb0061302` resolved; official contents confirm Versions A--C | detailed cofinite authority, used only schematically | **PASS WITH DISCLOSED ACCESS LIMIT** |
| `Kordyukov2001` | Yu.A. Kordyukov, *St. Petersburg Math. J.* 12(3), 407--422 | local arXiv original checked; bibliographic correction inherited from Paper 2 audit | relative/foliated trace hypotheses | **PASS** |
| `AlvarezKordyukovLeichtnam2026` | J.A. Álvarez López, Yu.A. Kordyukov, E. Leichtnam, LNM 2387 | book DOI `10.1007/978-3-032-15413-2` resolved; local arXiv v2 checked | exact cohomological/`b`-trace foliated-flow framework | **PASS** |
| `DyatlovZworski2016` | S. Dyatlov and M. Zworski, *Ann. Sci. ENS* 49(3), 543--577 | DOI `10.24033/asens.2290` resolved; local PDF checked | flat trace, Anosov orbit coefficient and resonance distinction | **PASS** |
| `Gutzwiller1971` | M.C. Gutzwiller, *J. Math. Phys.* 12(3), 343--358 | DOI metadata verified; publisher endpoint returned access denial rather than missing identity | historical quasiclassical provenance only | **PASS** |
| `CombescureRalstonRobert1999` | M. Combescure, J. Ralston, D. Robert, *Commun. Math. Phys.* 202, 463--480 | DOI `10.1007/s002200050591` resolved; original arXiv text checked | rigorous localized \(\hbar\to0\) theorem with remainder | **PASS** |
| `Fried1986` | D. Fried, *Ann. Sci. ENS* 19(4), 491--517 | DOI `10.24033/asens.1515` resolved; local Numdam PDF checked | exact Ruelle/Selberg zeta relationship in the stated hyperbolic scope | **PASS** |

## 4. High-impact claim-to-source alignment

### 4.1 Deninger packets

The manuscript attributes only the packet exhaustion and period law to
Deninger.  The missing trace/operator conclusions are an audit of what the
frozen source does not define, supported in detail by Paper 2.  It does not
claim that Deninger proves the ordinary product divergence.  Alignment passes.

### 4.2 Duistermaat--Guillemin

The paper says that the source gives local singular information for a fixed
positive self-adjoint elliptic operator under clean hypotheses.  It explicitly
withholds a full global orbit-sum inference.  This matches the source and the
paper's local-germ theorem.  Alignment passes.

### 4.3 Complete cofinite Selberg framework

The manuscript uses the data type

```text
discrete + continuous/scattering
  = identity + elliptic + parabolic/cusp + hyperbolic
```

and separately displays only the algebraically verified hyperbolic repeated
coefficient.  It does not print a full unverified normalization.  That is the
right response to the source-acquisition gap.  The words “exact complete
tested identity” refer to the established framework, not to a locally
reproduced convention.  Preserve the limitation sentence and do not add
formula numbers from metadata.  Alignment passes at framework level.

### 4.4 Foliated Lefschetz, flat trace and resonances

The manuscript names each analytic ledger and its hypotheses, and explicitly
denies that cohomological or generally non-self-adjoint resonance ledgers are
automatically quantum spectra.  It also refuses to identify a Deninger packet
with a preserved leaf.  Alignment passes.

### 4.5 Gutzwiller

The historical 1971 source is used for provenance, while the theorem-level
\(O(\hbar^\infty)\) statement is assigned to Combescure--Ralston--Robert.
The manuscript keeps the family/fixed-operator distinction explicit.
Alignment passes.

## 5. Claim-strength issue requiring correction

Current abstract wording:

> “Even all nonzero singular germs leave an exactly characterized ambiguity
> that is smooth off zero …”

Safe replacement:

> “Under an explicit prior containing every possible nonzero singular
> location, all nonzero singular germs leave an exactly characterized
> ambiguity that is smooth off zero …”

The Chinese abstract should receive the equivalent qualification.  Without
it, one may add an unlisted delta singularity, exactly as the manuscript later
explains.  This is a scope correction, not a change to the theorem.

## 6. Bibliographic correction log

| Priority | Location | Action |
|---|---|---|
| mandatory | English and Chinese abstracts | add the singular-support-prior qualification |
| mandatory | `Selberg1956` BibTeX | add stable CERN/IAS metadata URL while retaining the registered DOI |
| mandatory | `notes/source_matrix.md` | record that the DOI endpoint returned 404 on 2026-08-13; distinguish metadata verification from full-text acquisition |
| advisory | bibliography layout | the last page is sparse but correctly rendered; no padding source should be added merely for page balance |
| advisory | paper title metadata | current PDF title is the short title only; this is acceptable, though the full subtitle may be added if desired |

## 7. Release gate

Citation/integrity verdict after the three mandatory edits:

```text
ACCEPT
```

Until then:

```text
MINOR REVISION
```

No source replacement, new literature search, or change to the main
mathematical result is required.

