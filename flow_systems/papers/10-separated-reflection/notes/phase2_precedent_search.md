# Paper 10 Phase-2 bounded precedent search

Search date: **2026-08-14 (Asia/Shanghai)**  
Search stop: **2026-08-14T21:42:36+08:00**  
Artifact class: **novelty/source-verification ledger only**  
Final classification: **SUPPORTED_WITHIN_SEARCH**

## 1. Exact novelty unit and exclusions

The searched unit was not the generic statement that maps from a nonempty
indiscrete space to a `T0` space are constant.  It was the conjunction, on the
actual inherited finite-kernel Deninger `E_f` prime-packet owners, of:

1. `K0`, Hausdorff, and completely-regular-Hausdorff units with their typed
   universal properties;
2. collapse of `C(X)`, `C_b(X)`, and continuous fields into the fixed carrier
   `B(ell^2(N))` with norm, SOT, and WOT;
3. the topology-generated trivial Borel algebra, constant maps to countably
   separated measurable targets, and classification of positive finite
   measures without a Radon import;
4. continuous unit-circle characters for the explicitly transported group law
   on the actual `Q_p`;
5. the two directed continuity tests for the noncanonical standard-circle set
   bijection; and
6. the tagged copied-prime coproduct, its discrete prime reflection, and its
   `ell^1_+` component-mass ledger with the global-source boundary retained.

Two bodies of material are excluded from the Paper-10 novelty unit:

- **generic topology/measure facts:** indiscrete-space `T0` collapse, trivial
  topology-generated Borel sigma-algebras, and measures on `{emptyset,X}` are
  standard background, not a novelty claim;
- **Paper-9-owned consequences:** Paper 9 already establishes the actual
  packet/orbit/`Q_p` indiscreteness and records the immediate trivial-Borel and
  constant-`T0`-map consequences.  Paper 10 may cite but may not reclaim them.

Accordingly, a source that contains only a generic lemma or only a Paper-9
consequence is a baseline, not an exact precedent for the package above.

## 2. Search method and reproducible query ledger

The search followed an exact-conjunction-first, then decomposition strategy.
Search-engine windows were manually screened by title/snippet and, for serious
candidates, by official abstract/metadata.  Search-engine total-hit counts were
not exposed and are therefore recorded as `NOT_EXPOSED`; no count has been
inferred from result-page length.

### 2.1 Web/arXiv/DOI discovery queries

The following literal query strings were run through the web search endpoint;
official arXiv record pages and DOI landing metadata were preferred over
aggregator copies for verification:

```text
"rational Witt vectors" Deninger "Kolmogorov quotient"
"rational Witt vectors" Deninger "Hausdorff reflection"
Deninger "prime packet" topology
Deninger "finite-kernel" "Borel" Witt

site:arxiv.org Deninger "Dynamical systems for arithmetic schemes" rational Witt
site:arxiv.org/abs Deninger rational Witt vector dynamical systems arithmetic schemes
site:doi.org Deninger "rational Witt" dynamical systems
site:zbmath.org Deninger "rational Witt vectors"

"Dynamical systems for arithmetic schemes" "Kolmogorov quotient"
"Dynamical systems for arithmetic schemes" "Hausdorff reflection"
"Dynamical systems for arithmetic schemes" "Borel sigma-algebra" measure
"Dynamical systems for arithmetic schemes" "continuous functions" packet

site:arxiv.org/abs "Primes, knots and periodic orbits" Deninger
Deninger "E_f" rational Witt vectors
"E_f" "Dynamical systems for arithmetic schemes"
"finite kernel" Deninger rational Witt characters
"finite-kernel" Deninger arithmetic schemes

Deninger W_rat packet indiscrete topology
Deninger W_rat "non-Hausdorff" packet
"W_rat(X)(C)" "Borel"
"rational Witt" "trivial topology" Deninger

"Dynamical systems for arithmetic schemes" "continuous character"
"Dynamical systems for arithmetic schemes" "operator field" Borel
Deninger rational Witt packet coproduct primes
Deninger periodic orbit packet measurable measure character

Morishita Deninger space Connes Consani closed orbit arXiv 2025
site:arxiv.org Morishita Deninger rational Witt dynamical systems 2025
Morishita "Deninger spaces" rational Witt
"Deninger closed orbit" "Connes-Consani" Morishita
```

The top-result windows produced no record whose title/abstract asserted the
exact conjunction.  “Prime packet,” “finite kernel,” “operator field,” and
`E_f` also generated high-noise results from networking, harmonic analysis,
physics, and unrelated arithmetic uses; these were rejected before full-text
acquisition.

### 2.2 Bibliographic endpoint cross-check

Six fixed strings were also sent on the same date to:

- Crossref REST: `https://api.crossref.org/works`, parameters
  `query.bibliographic=<query>&rows=1&select=title`;
- OpenAlex REST: `https://api.openalex.org/works`, parameters
  `search=<query>&per-page=1`.

Endpoint-reported counts are discovery counts, not exact-conjunction counts.
Crossref/OpenAlex lexical expansion is visibly broad; the returned top title
is included below to make the noise auditable.

| ID | Literal query | Crossref count / top title | OpenAlex count / top title |
|---|---|---|---|
| Q1 | `Deninger rational Witt Kolmogorov Hausdorff reflection` | 269071 / *Witt vector rings and the relative de Rham Witt complex* | 0 / none |
| Q2 | `Deninger rational Witt trivial Borel finite measure` | 671289 / *Witt vector rings and the relative de Rham Witt complex* | 7 / *Scaling group flow and Lefschetz trace formula for laminated spaces with p-adic transversal* |
| Q3 | `Deninger rational Witt continuous observable operator field` | 1780200 / *Witt vector rings and the relative de Rham Witt complex* | 1 / *Noncommutative Geometry, the Spectral Standpoint* |
| Q4 | `Deninger prime packet continuous character` | 541787 / *State-of-the-art in terahertz continuous-wave photomixer systems* | 16 / *On higher regulators of Siegel threefolds II: the connection to the special value* |
| Q5 | `Deninger prime packet coproduct` | 82033 / *Sports on Television* | 1 / *Dynamical systems for arithmetic schemes* |
| Q6 | `Deninger E_f finite kernel packet` | 470337 / *Finite expressions for higher derivatives of the Dirichlet L-function and the Deninger R-function* | 0 / none |

These counts were not treated as included records.  The top-title audit shows
why a numeric broad-search count cannot substitute for object- and
claim-matched screening.

## 3. Candidate ledger and source verification

Serious records were deduplicated by title/identifier.  `0` records survived
as an exact Paper-10 precedent; one primary construction source was retained
as baseline context and three adjacent records were excluded.

| ID | Verified record | Source status | Decision | Reason |
|---|---|---|---|---|
| C1 | C. Deninger, *Dynamical systems for arithmetic schemes*, [arXiv:1807.06400](https://arxiv.org/abs/1807.06400), journal DOI [10.1016/j.indag.2024.05.007](https://doi.org/10.1016/j.indag.2024.05.007) | Primary construction; official arXiv and DOI metadata agree; journal version | `BASELINE_INCLUDE` | Exact source family and packet context, but not a precedent for the registered separated-reflection/observable/measure/operator/coproduct conjunction. |
| C2 | C. Deninger, *Primes, knots and periodic orbits*, [arXiv:2301.11643](https://arxiv.org/abs/2301.11643) | Author survey; official arXiv metadata | `EXCLUDE_OWNER_MISMATCH` | Discusses the global `W_rat(X)(C)`/dynamical picture and continuous functions in a different global topology; it does not own the actual restricted finite-kernel indiscrete packet package. It is also already in the Paper-9 source ledger. |
| C3 | M. Morishita, *On a relation between Deninger's foliated dynamical systems and Connes-Consani's adelic spaces*, [arXiv:2508.15971](https://arxiv.org/abs/2508.15971) | Primary recent preprint; official arXiv metadata; post-2024 preprint signal disclosed | `EXCLUDE_TARGET_AND_PRIOR_USE` | Directly adjacent adelic/closed-orbit comparison, but its comparison target and topology are not the Paper-10 actual inherited packet reflections. Paper 9 already records this source and its full-character/finite-kernel boundary. |
| C4 | C. Deninger, *Rational Witt vectors and associated sheaves*, [arXiv:2508.05329](https://arxiv.org/abs/2508.05329) | Primary recent preprint; official arXiv metadata; post-2024 preprint signal disclosed | `EXCLUDE_OBJECT_CLAIM_MISMATCH` | Concerns rational-Witt sheaf construction, not the packet-internal collapse, operator targets, or copied-prime coproduct. |
| C5 | Generic indiscrete-space, Kolmogorov quotient, Borel, and finite-measure references | Standard background, including Paper-10 Phase-1 domain sources | `EXCLUDE_GENERIC` | Supports reusable lemmas only; does not mention the Deninger `E_f` packet owner or the exact conjunction. |
| C6 | Networking “prime packets,” torus orbit packets, unrelated finite-kernel/Borel papers, and generic character/operator-field records | Search false positives | `EXCLUDE_LEXICAL_FALSE_POSITIVE` | Failed at title/object screen; no Deninger rational-Witt packet owner. |

No source was accepted merely from a search snippet.  C1--C4 identifiers and
titles were checked at official arXiv records; C1's publication identity was
cross-checked at the DOI.  The newer C3/C4 preprints are disclosed rather than
silently promoted to peer-reviewed precedent.

### Paper-9 non-redundancy gate

The local Paper-9 record already owns or explicitly records:

- actual `Gamma_p`, inherited orbit, and `Q_p` nontrivial indiscreteness;
- the immediate constant-map-to-`T0` and trivial-Borel consequences;
- the standard-circle proxy versus actual-owner correction;
- Deninger `2301.11643` and Morishita `2508.15971` as sources.

Therefore the search supplies no novelty credit for those statements.  The
only Paper-10 novelty unit tested here is the integrated typed package in
Section 1, including its universal-property scope, positive-finite-measure
typing, fixed operator targets, transported character law, directed proxy
test, and tagged-coproduct/global boundary.

## 4. Acquisition and integrity ledger

- Newly retained full texts: **0**.
- Newly created `prec-*` sidecars/manifests: **0**.
- Reason: no record survived title/abstract/object-target screening as a
  direct exact-precedent candidate.  Consequently PDF preflight, file hash,
  and license-retention gates were not triggered.
- No semantic “phrase absent from full text” claim is made for C2--C4; their
  exclusion is limited to the scope/object/target mismatch visible in verified
  metadata and abstracts, plus Paper 9's existing source ledger for C2/C3.
- Existing Phase-1 source files and every active lock were left untouched.

## 5. Bounded conclusion and stopping rule

**SUPPORTED_WITHIN_SEARCH.** As of 2026-08-14, the named web, arXiv/DOI,
Crossref, and OpenAlex searches located no publication precedent for the exact
Paper-10 conjunction on the actual finite-kernel Deninger packet owners.
Generic indiscrete-space consequences and Paper-9 results are explicitly
outside this conclusion and receive no Paper-10 novelty credit.

This is a bounded search finding, not a proof that no precedent exists.
Terminology such as `E_f`, “packet,” “reflection,” and “observable collapse” is
not consistently indexed; Crossref/OpenAlex broad counts are noisy; no
subscription-only specialist database supplied an exact-phrase count; and
later publications may change the result.  The stop rule was met when (i) all
six registered conjunction blocks had exact and decomposed queries, (ii) both
bibliographic endpoints returned only noise or known context, and (iii) every
serious adjacent candidate had a reproducible inclusion/exclusion decision.
