# Bounded source audit: rational Mann and the torsion-coset kernel

Date: 2026-09-08 UTC. Scope: the exact external formulation and classical
ownership of the auxiliary [torsion kernel](PROOF_PACKAGE.md), under
[its frozen contract](FROZEN_CONTRACT.md). This is AI-assisted internal
source work, not human peer review, a comprehensive literature review,
or a global novelty certificate.

## Result and access boundary

The rational minimal-vanishing-sum bound needed by the algorithm is the
classical Mann bound. The original publisher record and extract were
accessed, but the original full theorem/proof pages were **not obtained**.
That distinction is retained rather than describing a publisher metadata
lookup as a full original-paper read.

The exact rational-coefficient form was corroborated in primary research
articles on equations in roots of unity. An accessible author-hosted paper
also states the polygon form explicitly. These are research papers, not
blog summaries, but their citations share Mann as a classical dependency;
they are not independent replications of his theorem.

To remove any mathematical reliance on unavailable original proof pages,
Lemma 1 of the proof package gives the complete elementary argument for
the precise rational, indexed-subsum version used here. Source access
remains partial; the mathematical input is proved rather than left as an
unverified black box.

## Primary-source evidence matrix

| Source | What was actually accessed | Exact role and limitation |
|---|---|---|
| Henry B. Mann, *On linear relations between roots of unity*, Mathematika 12(2) (1965), 107–117, [DOI/publisher record](https://doi.org/10.1112/S0025579300005210), [Cambridge extract](https://www.cambridge.org/core/journals/mathematika/article/abs/on-linear-relations-between-roots-of-unity/346C7FE8D77A7D987662F7310265271D) | Publisher metadata and the original introductory extract; Wiley's PDF route redirected to its abstract record. | Verified original identity and rational-integer setup. Original full theorem/proof pages were not read; do not cite this access as full-text verification. |
| Jan-Hendrik Evertse, *The number of solutions of linear equations in roots of unity*, Acta Arithmetica 89 (1999), 45–51; [author PDF](https://pub.math.leidenuniv.nl/~evertsejh/98-roots.pdf), [journal PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8915.pdf) | Research-PDF retrieval metadata and indexed source text, including the introduction; subsequent direct fetches were inconsistent or timed out. | The introduction gives the nonzero rational-coefficient, nondegenerate normalized equation and the distinct-prime bound through the number of terms plus the right-hand side. This matches the required indexed version after normalization. This was not a full-paper review. |
| Benedict H. Gross, Eriko Hironaka, Curtis T. McMullen, *Cyclotomic factors of Coxeter polynomials*, [author version dated 9 September 2008](https://people.math.harvard.edu/~ctm/papers/home/text/papers/en/en.pdf) | Author-hosted PDF text, especially Section 2, printed pages 4–5, and Theorem 2.2. | Explicitly states the Mann prime-product bound for primitive polar rational polygons. That formulation has its own positivity and primitive-divisor definitions; it is corroboration, not a license to skip the indexed rational hypotheses in our Lemma 1. |
| Iskander Aliev and Chris Smyth, *Solving algebraic equations in roots of unity*, [arXiv:0704.1747v3](https://arxiv.org/abs/0704.1747), [PDF](https://arxiv.org/pdf/0704.1747) | arXiv metadata and PDF introduction plus Section 2.3, including lattice/coset and Smith-normal-form arguments. | Establishes the bounded ownership warning: explicit torsion-coset algorithms and this lattice machinery predate our work. The introduction points to its Section 6 algorithm and earlier Sarnak–Adams and Ruppert algorithms. We do not use its arbitrary-complex-coefficient formulation as an effective black box. |

An additional indexed excerpt from Umberto Zannier's *On the linear
independence of roots of unity over finite extensions of Q* gave the same
rational indexed-subsum bound. The retrieved legacy PDF had no usable
text layer in that call, so this is not promoted to another full-text
verification receipt. The proof does not depend on that excerpt.

## Exact scope of the Mann input

The algorithm uses the following statement, with $b\ge2$:

$$q_i\in\mathbb Q^*,\quad\theta_i\in\mu_\infty,\quad
\sum_{i=1}^bq_i\theta_i=0,$$

with no nonempty proper **indexed** vanishing subsum, implies

$$\left(\theta_i/\theta_j\right)^{P(b)}=1,
\qquad P(b)=\prod_{p\le b}p.$$

The following restrictions are essential:

- Rational coefficients are used only after the original cyclotomic
  coefficients have been expanded into rational weights times fixed roots.
- The conclusion concerns ratios, not the absolute order of every root.
- The term count is that of the expanded rational-weighted list. It is
  not automatically the sparse monomial count of the original polynomial.
- Minimality is applied to actual vanishing blocks of an actual torsion
  zero. The finite enumeration may include other exactly vanishing patterns
  because its separate soundness proof remains valid for them.
- Repeated roots and signed weights are retained in the indexed version;
  Lemma 1 proves this version without an unproved conversion to primitive
  positive divisors.
- Characteristic zero is used in the cyclotomic field-degree argument.

## What is proved here and what remains classical

The package supplies an explicit proof of the needed input, a complete
finite pattern algorithm, soundness and torsion coverage, connected
decomposition, exact finite-union tests, and a rectangular-Smith-normal-form
torsion-lifting proof. These details support the coordinator's exact
existential-torsion interface; they are not a claim to have invented
torsion-coset algorithms.

The existence of older algorithms is directly relevant prior art for this
auxiliary kernel. We make no claim that the particular Hénon use is new;
the coordinator and the separate source owner retain the main AF5-C
increment/ownership question. The Loxton bound, the dynamical Noetherian
argument, and the final finite periodic atlas are outside this audit.

## Retrieval method and exact search ledger

`research-lit` and the ARS bounded `fact-check`/source-verification route
were used after reading their instructions. No Zotero or Obsidian tools
were available. A filename-only scan of the local `papers/` collection
found no relevant Mann/cyclotomic/torsion/Loxton PDF; `literature/` was
absent. No unrelated local manuscript was opened. No local arXiv fetch
script was found in the inspected skill locations, so the arXiv-specific
query below used the permitted browser fallback. No programmatic
bibliographic API or external model was called.

The twelve search strings actually submitted were:

1. `Henry B Mann 1965 On linear relations between roots of unity Mathematika theorem rational coefficients pdf`
2. `site:arxiv.org Mann theorem rational coefficients roots unity torsion cosets algorithm`
3. `"Mann" "roots of unity" "Theorem 1" "107" pdf`
4. `"On linear relations between roots of unity" filetype:pdf`
5. `"Mann theorem" "rational" "squarefree" roots of unity`
6. `"Mann" "1965" "roots" "minimum" "primes" theorem`
7. `"Mann" "On linear relations" "1964" pdf`
8. `"Mann" "roots of unity" DTIC`
9. `"Cyclotomic factors of Coxeter" McMullen pdf`
10. `"AD0610448"`
11. `"DTIC" "ON LINEAR RELATIONS"`
12. `"Mann" "roots of unity" "rational" theorem squarefree product primes`

Direct URL opens, publisher-link clicks, and source-page requests were
additional retrieval operations, not additional search strings. Search
results from nonprimary aggregators were not used as mathematical authority.
The original-report/DTIC route did not supply an accessible original text.

One read-only request for Wiley's publicly linked first-page preview used
`curl -fsSL --max-time 30` piped to `base64 -w 0`; it failed with a TLS
connection error and yielded no inspected image. The pipeline's final
status belonged to `base64`, not a successful image fetch. No file was
downloaded or retained by that command. Browser screenshot requests did
not expose an image for inspection in this interface; no visual-reading
claim is made from those requests.

## Verification limits and evidence classification

- Mathematical research articles and original theorem text are the relevant
  evidence class; an empirical RCT/meta-analysis hierarchy is inapplicable
  to this proof task. No invented numerical evidence score is assigned.
- Publisher or author-host identity was checked at the accessed URLs.
  Exhaustive indexing, predatory-journal databases, retraction databases,
  and author conflict-of-interest checks were not performed. Their absence
  is not labelled a clean bibliographic-integrity certificate.
- Several sources restate the same classical theorem. Agreement verifies
  the requested formulation within the accessed record, not independence
  of the underlying proof or universal citation correctness.
- Mann's full original proof access remains unavailable. Lemma 1's explicit
  argument is the mathematical remedy, not a claim that source access
  succeeded retroactively.
- There was no mathematical execution, symbolic import, finite census,
  GPU work, old rerun, Git operation, manuscript/PDF production, or external
  model review. New writes are confined to `torsion_kernel/`.
- These bounded findings neither admit a fourth contract nor imply target
  arithmetic progress. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.
