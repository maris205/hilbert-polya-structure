# HCS-C54 source-control and bounded-novelty audit

Status: **primary metadata checked; exact locators recorded where relied upon;
novelty statement search-bounded**.

Audit date: 2026-08-14.

## 1. Formal mathematical inputs

The release theorem does not depend on unpackaged scout files or temporary
planning notes.  Such notes were historical reconnaissance only: they are not
theorem inputs, release sources, or reproducibility evidence.  The formal
evidence chain is instead the proof package in this project, the exact
primary-source locators below, and the project-local producer/checker artifacts
once their release hashes are promoted.

HCS-C53 supplies the explicit semilinear reversal, rational equation model,
and certified rational compatible packet data in the smooth rows \(2,3,4\).
It is not cited for a semisimplicity theorem.  HCS-C54's scoped code/results
lane is now a release candidate with a persistent replayable manifest.  The
44-entry full-project inventory includes that manifest; only the implementation
commit remains a later provenance stage.

### 1.1 Committed upstream provenance lock

The project-local checker reads the HCS-C53 dependency from a committed git
object rather than trusting mutable working-tree bytes.  Its verified status is
`VERIFIED_GIT_OBJECT_CERTIFICATE_AND_COMMITTED_ROUTE_TUPLE`, with:

- HCS-C53 provenance commit
  `9d509d3b3826b7bfbdb38ed9fe4dac9297f5dbdf`;
- committed HCS-C53 Route SHA-256
  `ae508e6e41523559f014f6fbcd0c4c199229f221fe6ac915a75cd27b02e73719`;
- implementation commit
  `0a7f0fdb8290eab4aa92ed5ade432401c40c22cf`;
- certificate SHA-256
  `f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79`;
- payload SHA-256
  `8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41`;
- independent-check SHA-256
  `0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67`;
- code/results-manifest SHA-256
  `b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480`.

These are committed upstream dependency locks and are distinct from the
current HCS-C54 release-candidate tuple.

### 1.2 Current HCS-C54 scoped release candidate

Immutable replay passes 36 of 36 semantic gates and 93 of 93 unit tests.
The persistent 11-entry code/results manifest and release-candidate hashes are:

    payload               f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1
    certificate           780cc9f249e836d3fa5b51a00fd2cdb9af0eac595d929cd1be4d728df1921846
    independent check     160b3a9d11354b41404642a3dd22d6e43f2ce576126acb21eb0133e552fc0c0a
    schema                 4cee6c2252d5743ca3c5fee40ec98fbc945223312d2196fb63a43730281deedf
    code/results manifest 62f67e6d4929496974020febab3bc0e2cff45ed153b0cef51937031863d866ba

This is the SHA-256 of the persistent file
`results/CODE_RESULTS_HASHES.sha256`.  That file lists exactly seven release
code files and four release result files and excludes both manifest files.
The 44-entry full-project inventory includes the scoped manifest.  It does not
claim the pending implementation commit.

## 2. Primary-source locators

### 2.1 Fermat projective monomial symmetry and one-dimensional sectors

**Lars Brünjes**, “On the Zeta Function of Forms of Fermat Equations,”
arXiv:math/0301186 (2003).

Verified from the arXiv metadata and PDF:

- Proposition 3.8 identifies the projective monomial automorphism group of a
  Fermat form as \((S_n\wr\mu_m)/\mu_m\).
- Lemma/Definition 4.3 identifies the diagonal character set.
- Theorem 4.6 states that the primitive pieces indexed by nonzero character
  tuples are one-dimensional and records geometric-Frobenius Jacobi
  eigenvalues.
- Example 4.7 treats the cubic in six variables and its extreme sectors.

Use in HCS-C54: Fermat background and the optional stronger diagonal-sector
refinement.  Brünjes does **not** classify the simultaneous stabilizer of the
new cubic--quadric pair and does not prove Theorem A or C.

Verification record:

- arXiv metadata: title, author, and identifier confirmed through the official
  arXiv API;
- downloaded arXiv PDF SHA-256:
  `f97ba9df391222e649c2c1641b5bd11a94590ab15f4b846adedd323d71748c13`.

### 2.2 Purity and separation of weights

**Pierre Deligne**, “La conjecture de Weil II,” *Publications
Mathématiques de l'IHÉS* **52** (1980), 137--252,
DOI `10.1007/BF02684780`.

The official Numdam scan verifies the bibliographic data.  Section 1.2,
especially (1.2.2), defines pointwise purity and mixedness, and
(1.2.5)(i) records stability of the pure-weight category.  Use in HCS-C54:
purity background for the already constructed compatible systems.  The paper
does not use Weil II to construct a packet in a new row.  The only conclusion
needed in Theorem C is that pure constituents of different weights cannot be
isomorphic.  Official Numdam PDF SHA-256:
b06eea61bf9cb2b596c162f5befcf85d1be69828910a6107c8aa3a99c4afcc71.

### 2.3 Chebotarev density

**Jean-Pierre Serre**, “Quelques applications du théorème de densité de
Chebotarev,” *Publications Mathématiques de l'IHÉS* **54** (1981),
123--201, DOI `10.1007/BF02698692`.

Verified from the official Numdam scan:

- §2.1 defines Frobenius conjugacy classes;
- Theorem 1 gives density \(|C|/|G|\) for a conjugacy-stable subset
  \(C\) of a finite Galois group.

Use in HCS-C54: Frobenius density after restriction to \(G_K\), combined
with fixed-\(\ell\) semisimplification and the characteristic-zero character
lemma.  This does not attribute a semisimplicity theorem to HCS-C53.  Official Numdam PDF
SHA-256:
`bfcda9821742b02801e4f1264750aebeb656141fbd53fb61b8662333e1491830`.

### 2.4 Brauer--Nesbitt character rigidity

**Richard Brauer and Cecil Nesbitt**, “On the Modular Characters of
Groups,” *Annals of Mathematics* (2) **42** (1941), no. 2, 556--590,
DOI `10.2307/1968918`.

Crossref verifies the authors, title, journal, year, volume, issue, pages, and
DOI.  HCS-C54 uses only the standard characteristic-zero semisimple
trace-rigidity consequence: two finite-dimensional semisimple
representations with the same trace character have the same semisimple
class.  We did not verify a theorem-number locator for that exact modern
formulation in the 1941 paper.  The proof package states the required
character lemma internally, so the citation is historical background rather
than an asserted exact locator.

### 2.5 General Cayley--Jacobian identification

**Jan Nagel**, “The Abel--Jacobi Map for Complete Intersections,”
*Indagationes Mathematicae* **8** (1997), no. 1, 95--113,
DOI `10.1016/S0019-3577(97)83353-8`.

Crossref verifies the title, author, journal, year, volume, issue, pages, and
DOI.  Proposition 2.16 gives

\[
H_{\mathrm{var}}^{n-p,p}(X)\cong R_{p,d(X)},
\qquad
d(X)=\sum_i d_i-n-r-2.
\]

For the present \((2,3)\) threefold, \(n=3\), \(r=1\), and
\(\sum_i d_i=5\), so \(d(X)=-1\).  Taking \(p=1\) gives the precise
locator

\[
H^{2,1}(X_3)=H_{\mathrm{var}}^{2,1}(X_3)\cong R_{1,-1}.
\]

Use in HCS-C54: the general complete-intersection Cayley/Jacobian
identification.  The exact monomial quotient, residue-corrected source-group
action, and character arithmetic remain internal proofs.

### 2.6 Quadric--cubic fivefold instance

**David Favero, Atanas Iliev, and Ludmil Katzarkov**, “On the Griffiths
Groups of Fano Manifolds of Calabi--Yau Hodge Type,” *Pure and Applied
Mathematics Quarterly* **10** (2014), no. 1, 1--55,
DOI `10.4310/PAMQ.2014.v10.n1.a1`; arXiv:1212.2608.

Verified from the arXiv PDF and Crossref metadata:

- §5.4 defines the Cayley hypersurface, its bigrading, Jacobian ideal, and
  bigraded ring for a smooth \((2,3)\) intersection;
- equation (8) records the corresponding primitive Hodge components and the
  fivefold Hodge numbers.

Use in HCS-C54: a \(\mathbf P^7\) fivefold instance and Hodge-type context.
Section 5.4 does not literally cover the present threefold, so it is not used
as the locator for \(H^{2,1}(X_3)\cong R_{1,-1}\).  The exact \(n=3\)
quotient, group action, determinant ratio, and character are new
source-specific computations.

Verification record:

- official arXiv metadata confirms title and all three authors;
- arXiv PDF SHA-256:
  `02fd23c00c0130c1a4d75451da6a26df516f24d1b2bc89c5cc8477f544388271`.

### 2.7 Jacobi-sum context

**André Weil**, “Jacobi Sums as ‘Grössencharaktere’,” *Transactions of the
American Mathematical Society* **73** (1952), no. 3, 487--495,
DOI `10.1090/S0002-9947-1952-0051263-0`.

Crossref/AMS metadata verifies the citation.  This is context for interpreting
Fermat Jacobi sectors; HCS-C54 does not use it to prove automorphy or a
functional equation.

## 3. Claim-to-source boundary

| HCS-C54 statement | External source role | New work required here |
|---|---|---|
| Fermat projective monomial background | Brünjes, Proposition 3.8 | intersection with the weighted cycle quadric; recurrence and exhaustive \(6n\) count |
| one-dimensional Fermat sectors | Brünjes, Lemma/Definition 4.3 and Theorem 4.6 | common-source two-rail obstruction and coefficient-orbit check |
| different pure weights | Deligne, Weil II | packet-specific rank divisibilities and \(n\mid24\) reduction |
| density of Frobenius classes | Serre, §2.1, Theorem 1 | restriction from split rational primes and the exact two-rail K0 identity |
| semisimple trace rigidity | Brauer--Nesbitt | split-invisible kernel caveat and actual/virtual distinction |
| general Cayley identification | Nagel, Proposition 2.16 | specialization to \(R_{1,-1}\), exact 27-by-7 quotient, residue-corrected matrices, and full \(G_3\)-character |
| \((2,3)\) fivefold instance | Favero--Iliev--Katzarkov, §5.4 | context only; no transfer of the fivefold formula to the threefold |

No citation is used as authority for the new simultaneous cubic--quadric
stabilizer or the \(n\mid4\) classification.

## 4. Search-bounded novelty audit

This is a targeted screen, not a systematic-review or database-exhaustive
novelty certificate.

### Databases and date

- arXiv official API, searched 2026-08-14;
- Crossref official API, searched 2026-08-14;
- known-primary-source backward search from Brünjes and
  Favero--Iliev--Katzarkov.

### Exact arXiv queries

The following four conjunctions returned zero records:

1. `"projective monomial stabilizer" AND "cubic quadric"`;
2. `"dihedral" AND "cubic quadric" AND "Fermat"`;
3. `"compatible system" AND "denominator" AND "split prime"`;
4. `"Dih(C_9)" AND "Cayley"`.

A broader `Fermat AND monomial AND automorphism` query returned a Dwork-family
paper but no statement about the weighted cubic--quadric pair.  Broader
Crossref searches for the projective-monomial pair, universal dihedral pair,
split-denominator compatible system, and the \(D_9\) Cayley character returned
only unrelated geometric-modeling, combinatorial split-system, or general
dihedral results.

### Nearest primary work

- Brünjes is nearest on full projective monomial Fermat symmetry and
  one-dimensional Fermat sectors.
- Nagel supplies the general Cayley/Jacobian identification, while
  Favero--Iliev--Katzarkov is the nearest explicit \((2,3)\) fivefold
  instance.
- Serre and Brauer--Nesbitt supply the general density/character mechanism.

No searched source states the simultaneous pair stabilizer
\(\operatorname{Dih}(C_{3n})\), the packet-admissible ordinary-realization
classification \(n\mid4\), or the exact common-source \(n=3\) two-rail
character obstruction.  The correct novelty label is therefore
**search-supported and bounded**, never “first” or “no prior work exists.”

## 5. Citation integrity decisions

- Published metadata are preferred where a DOI exists.
- Brünjes is cited as an arXiv preprint because that is the verified primary
  version used for exact proposition/theorem locators.
- The Favero--Iliev--Katzarkov journal and arXiv versions are not duplicated
  under separate citation keys.
- No secondary survey is used to support a theorem-level claim.
- No recent-paper claim, automorphy claim, or analytic continuation claim is
  imported.

## 6. Negative-claim firewall

The sources above do not prove and HCS-C54 does not claim:

- the full PGL automorphism group of the source intersection;
- smoothness or a motive for \(n\ge5\);
- a global or inert fractional root;
- a common untwisted rational group scheme for the standard Fermat model and
  the HCS-C53 complete-intersection model;
- injectivity of restriction on virtual rational representation classes;
- automorphy, a functional equation, or RH.
