# Source and ownership audit: Boole admission contract

Audit date: 2026-09-05. Repository HEAD observed before writes:
1ad0bf5b2c3c79733a434b72d62201de9b70868a.
This is a bounded candidate-admission audit, not a systematic literature
review, novelty certificate, journal-readiness claim or completed paper.
All research text in this directory is current-model internal author material;
no external model, human referee or private-corpus upload was used.

## Actual local input and collision checks

The root and Hénon AGENTS files, repository batch skill and its full workflow,
the full proof-writer skill, current state, and
[the active scout, section A](../../SCOUT_C399_C403.md) were read.
The closest old mathematical package was read through its proof:
[C380 Blaschke proof](../../henon_finite_blaschke_ruelle_spectrum_route_a/proof/ANALYTIC_PROOF.md).
The collision search also inspected candidate-registry entries for C381
(LSV), C257 (quadratic Newton--Cayley) and the earlier Boole reserve entry.

Representative actual repository queries, run from the repository root:

    rg -n -i '\bBoole\b|dilogarithm.{0,40}determinant|determinant.{0,40}dilogarithm' henon_dynamics flow_systems symbolic_dynamics --glob '*.md' --glob '*.tex' --glob '!**/qa_final/**'
    rg -n -i '\bBoole\b|McMillan|\bQRT\b' papers docs flow_systems henon_dynamics --glob '*.md' --glob '*.tex' --glob '!**/qa_final/**'

The first query found the scout/current-state references and the previous
IDEA reserve, not an older completed Boole stability-collision theorem.
This is a query-specific observation, not proof of absence throughout every
unindexed file. The second query belongs to the preceding read-only scouting
pass and also established that a bare McMillan atlas was owner-heavy.

### Exact C380 overlap

C380's source is $w(w-\alpha)/(1-\alpha w)$ for $0\le\alpha<1$.
The present subcritical Cayley form is $w(w+q)/(1+qw)$, $q=2a-1$.
Thus the direct overlap is $q=-\alpha$, $0<a\le1/2$; the wider classical
Blaschke theorem covers the remaining positive $q$.

C380 already owns the full-circle spectrum/product and fixed-point
residue strategy. Our candidate cannot count any of those by themselves
as an independent paper increment. Its different owner is the actual
finite-real periodic set, excluding the infinity fixed primitive, carried
across the change of real/complex fixed-point location and parabolic
multiplicity. The proof explicitly does not equate deletion of a null
orbit with modification of an ordinary $L^p$ transfer operator.

## Primary sources actually accessed

The access descriptions below are bounded to visible browser text. They
do not attest that a human has read the sources. No bibliographic API or
cross-model citation service was invoked.

| Source | Actual access and locator | What it already owns / limitation |
|---|---|---|
| Ken Umeno and Ken-ichi Okubo, “Exact Lyapunov exponents of the generalized Boole transformations,” PTEP 2016, 021A01 | [arXiv v3 HTML](https://arxiv.org/html/1510.08569v3), including Theorems 1--3, section 3 and Table 1; [arXiv metadata](https://arxiv.org/abs/1510.08569) verifies DOI 10.1093/ptep/ptv195 | The three statistical regimes and explicit Lyapunov formulas are established prior work. We use this for ownership, not as a proof of the candidate's new determinant assertions. Our phase claims are independently proved at the narrower invariant-measure/survival level. |
| Shin-itiro Goto and Ken Umeno, “Maps on statistical manifolds exactly reduced from the Perron-Frobenius equations for solvable chaotic maps” | [arXiv v3 HTML](https://arxiv.org/html/1707.03607v3), Proposition 3.1 and Lemmas 3.1--3.3; [metadata](https://arxiv.org/abs/1707.03607) | Exact Cauchy location/scale closure and its complex-coordinate relation are not new mechanisms. This source is cited as an author preprint version; no unverified journal status is assigned here. |
| Nelly Elisenia Mendoza Mendoza and Luis Bladismir Ruiz Leal, “Dinámica de la transformación generalizada de Boole,” Revista Bases de la Ciencia 7, special issue (2022), 300--310 | [publisher metadata](https://revistas.utm.edu.ec/index.php/Basedelaciencia/article/view/4408) and [publisher PDF](https://revistas.utm.edu.ec/index.php/Basedelaciencia/article/download/4408/7355/27220), Lemma 3.1 and Theorem 4.5 | The supercritical real repelling fixed points, exterior escape and invariant binary Cantor dynamics are prior results, even for the additional affine-shift parameter excluded here. The PDF has an unrelated English translated heading; its Spanish title, authors, DOI and mathematical content agree with the metadata. This editorial anomaly is disclosed, not used to erase ownership. |
| Claudio Bonanno, Paolo Giulietti and Marco Lenci, “Global-local mixing for the Boole map” (2018 author version) | [arXiv v2 HTML](https://arxiv.org/html/1802.00397v2), introduction and invariant-measure/global-local definitions; [metadata](https://arxiv.org/abs/1802.00397) | Infinite-Lebesgue Boole dynamics and global-local mixing are classical literature for this candidate. We make no new mixing claim and do not use a finite periodic-point calculation to prove one. |
| Oscar F. Bandtlow, Wolfram Just and Julia Slipantschuk, “Spectral structure of transfer operators for expanding circle maps,” Ann. IHP Analyse non linéaire 34 (2017), 31--43 | [primary journal PDF via Numdam](https://www.numdam.org/item/AIHPC_2017__34_1_31_0.pdf), Theorem 5.4 and Remarks 5.5--5.7; [arXiv metadata](https://arxiv.org/abs/1311.3122) | The full-circle Hardy-space transfer spectrum and Fredholm mechanism are prior work. Remark 5.6 itself explains older adjoint-operator ancestry. The finite-real deleted-orbit product is not silently identified with that old operator. |

All source-specific summaries above are limited paraphrases. The proof
package derives its formulas directly; it does not copy a source proof or
rename the source authors' principal results.

## Directed stability/resonance searches actually run

The browser was queried with the following strings across this admission
pass and the immediately preceding read-only scout:

    "Boole" "dynamical determinant"
    "Boole transformation" "fixed point" "index"
    "generalized Boole" "resonance" determinant
    "parabolic" "dilogarithm" "dynamical determinant"
    "Boole" "Fredholm"
    "Boole" "stability" "zeta"
    "generalized Boole" "dilogarithm"
    "Boole transformation" "determinant"
    "generalized Boole" "zeta function"
    "Boole" "dilogarithm"

The returned candidate-relevant hits led to the sources above and to
generalized/super-generalized Boole intermittency literature. Many other
hits concerned Boole quadrature, Boole polynomials or unrelated
fixed-point theory; those do not address this rational map and were not
counted as relevant evidence. No directly matching theorem for the entire
finite-real deletion/resonance/two-sided critical-limit contract was found
in these returned sources.

This negative result has substantial limits. Search engines do not index
all formulas or older books; alternate rational-map normal forms can hide
a prior result; we did not perform a full citation-graph search or inspect
every thesis. The candidate is therefore SEARCH-BOUNDED NO DIRECT MATCH,
not “new,” “first,” or “certified original.”

## Classical inputs versus independently derived candidate increment

### Classical and not admission credit by themselves

- Cauchy and infinite-Lebesgue invariant measures, the three statistical
  regimes, and Lyapunov formulas.
- Binary Cantor coding and escape outside the real fixed interval.
- Blaschke conjugacy, complete circle transfer spectra, holomorphic index
  methods, and primitive stability products as a general formalism.
- A finite list of periodic roots, rational parameters or determinant values.

### The integrated contract actually derived in PROOF_PACKAGE.md

- Every finite real iterate and its positive simple multipliers, with
  separate accounting for the two nonreal fixed points, infinity's simple
  multiplier away from criticality, and its critical multiplicity/index.
- The all-iterate finite-real stability sum and the resulting meromorphic
  quotient, rather than the old full-circle determinant.
- Every zero/pole coincidence through the exact logarithmic commensurability
  condition; the entire iff classification $a=(1-2a)^{2m}$.
- The non-meromorphic critical fractional order and two-sided locally
  uniform limit after removing precisely the two newborn fixed primitives
  on the supercritical side.
- The exact survival identity from the inverse-Jacobian sum, included to
  keep the physical survivor separate from the abstract diagonal product.

These are independent derivations in this author draft. “Independent” here
describes the derivation and the distinct repository contract, not a claim
that the statements are absent from all mathematical literature.

## Admission objections and next proof obligations

The strongest objection is that most of the machinery and the entire
classical phase picture already have owners. The candidate is worth
considering only as one complete physical-periodic-set collision theorem;
it must be rejected if reduced to those classical pieces or a parameter
table. A newly found prior theorem covering the integrated contract should
trigger significance reassessment, not evasive renaming.

The author's proof has no presently identified missing lemma. Independent
review should especially attempt to break:

1. the exact physical-domain exclusion and simple fixed-point count at
   $a=1$, rather than promoting the degree count alone;
2. the residue coordinate correction $I_\infty-1$ and the quintic term
   responsible for the critical index;
3. necessity of the first-pole cancellation and completeness of the
   rational-log ratio divisor description;
4. the signs in the supercritical primitive-factor division;
5. the all-$n$ uniform bounds used for local uniform convergence;
6. the distinction between source product realizability and a natural
   physical transfer operator.

No formal Route-A evaluation has been run here. There is no new intrinsic
prime mechanism, arithmetic control PASS, target determinant/zero match,
Euler factor, root number, automorphy or Hilbert--Pólya correspondence.
The conservative exploratory ceiling is unchanged:
$A0\_FAIL$, $A1\_WEAK$, $A2\_FAIL$, $A3\_FAIL$,
$A4\_FORMAL\_HINT$. All target/Route-B flags and permission remain false.

## Coordinator amendment after independent review (2026-09-05)

The independent review is now saved at
[BOOLE_INDEPENDENT_REVIEW.md](../reviews/BOOLE_INDEPENDENT_REVIEW.md).
It found the explicit weighted contract provable as stated, but required a
sharper classical-ownership boundary before admission. Its input hashes refer
to this file before the present append; the original proof/code are unchanged.

Mendoza–Ruiz §3 already defines the same real deleted-prepole domain. Its
Theorems 4.2 and 4.4 identify the critical and `1/2<a<1` dynamics with binary
shift dynamics after removing eventually constant sequences. Consequently the
unweighted count `2^n-2` in those regimes is an immediate prior corollary.
The domain and those unweighted counts are **not** independent admission credit.
The manuscript's introduction now states this explicitly and keeps the weighted
deletion, entire-resonance iff, and compensated critical limit as one question.
The reviewer's direct primary-PDF locators are recorded in the linked review.

For the manuscript bibliography, the coordinator additionally checked primary
arXiv/journal metadata and retrieved DOI BibTeX on this date. Umeno–Okubo and
Mendoza–Ruiz metadata agree with the primary records. CrossRef's negotiated
record for the Blaschke DOI returned a different author ordering from the
Numdam primary journal record; `paper/references.bib` deliberately follows the
primary order **Bandtlow, Just, Slipantschuk**, with this discrepancy disclosed.
The published title, journal, volume 34, issue 1, pages 31–43, year 2017 and
DOI agree. Three cited entries, not the entire broader discovery list, form
the draft bibliography. This source amendment does not certify global novelty.
