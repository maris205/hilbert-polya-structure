# Primary-source and ownership audit

2026-09-06. Author-side bounded audit, not an independent admission decision,
human reading attestation, peer review, or exhaustive novelty certificate.
The proof is in `PROOF_PACKAGE.md`; the exact contract is in `CONTRACT.md`.

## 1. Central source and exact version

Jakub Byszewski, Gunther Cornelissen, Marc Houben (BCH), *Dynamics of
endomorphisms of algebraic groups*,
[arXiv:2209.00085v2](https://arxiv.org/abs/2209.00085v2), submitted
19 April 2024; [original PDF](https://arxiv.org/pdf/2209.00085v2), 176 PDF pages.
The current unversioned arXiv landing page was checked on the audit date and
listed v2 as its latest version. No journal DOI or final EMS book identifier
has been invented.

The following original passages were actually inspected. Locators are the
source's section/theorem numbers; PDF indices are not printed page numbers.

| Original locator | Role and restriction in this candidate |
|---|---|
| Definitions 7.1.1–7.1.2 | FAD data; positive periodic `r`; nonnegative **real** `s,t`; exponent periods coprime to their own prime. Genuine fixed-point realizability is required for the dynamical corollary. |
| Definition 10.3.9; Lemmas 10.3.2 and 10.3.10 | Hyperbolicity here means a unique dominant root. This is not an inference from terminology in another paper. |
| Definition 12.4.1; text before Theorem 12.4.3 | The hyperbolic archimedean phase is identically one; its detector coordinate is trivial. |
| Equation (12.4); Theorem 12.4.3(ii) | Classical continuous detector-image representation for `N pi_f(N)/Lambda^N`. This entire orbit-asymptotic reduction is deducted. |
| Theorems 12.5.1–12.5.2; Remark 12.5.3 | Existing cardinality dichotomy; one-prime, zero-wild-term topology; nonhyperbolic interval inclusion. |
| Lemma 12.5.4 and proof; proof of Theorem 12.5.2(ii) | One-variable nonconstancy/injectivity machinery was read to check overlap. The candidate does not extrapolate its injectivity conclusion. |
| Proof of Theorem 12.5.1, printed pp. 132–133 | BCH already chooses a negative integer in the other coordinates to make slice coefficients nonzero. The negative-integer choice itself is classical here; the candidate combines it with the new positive Fourier lemma on every cylinder. |
| Problem 14.1.1 | The explicit remaining hyperbolic regimes are multiple primes and/or nonzero wild terms. These are the source-local open regimes addressed here. |
| Example 7.1.3; Examples 7.2.6–7.2.9; Definition 9.1.2 and Proposition 9.1.4 | Classical realizations and product closure used in `REALIZED_EXAMPLES.md`. |

The candidate's added work is the adaptive finite cover and positive
radial-kernel Fourier argument. Merely having continuum many limits, a
continuous detector image, or a classical fixed-count formula is not counted
as an added theorem. The scope statement is: **the proof resolves the
hyperbolic regimes expressly left open by the cited 2024 public version**.
It does not classify general nonhyperbolic detector images or solve every
part of the general topology question.

## 2. Closest earlier sources actually compared

### Byszewski–Cornelissen, 2018

*Dynamics on abelian varieties in positive characteristic*, with an appendix
by Robert Royals and Thomas Ward, *Algebra & Number Theory* 12(9),
2185–2235 (2018), [publisher PDF](https://msp.org/ant/2018/12-9/ant-v12-n9-p06-p.pdf),
[article DOI](https://doi.org/10.2140/ant.2018.12.2185).

Read scope: introduction's Theorem F, Proposition 9.4, Theorem 9.5 and its
proof, especially the one-coordinate detector and local injectivity
argument. This is a close mathematical predecessor, not a new discovery of
Cantor behavior. Its hypotheses and fixed-count data belong to the
one-characteristic, no-wild-factor setting. The candidate must be judged on
the all-finite-prime/wild extension and the covering estimate.

### Everest–Miles–Stevens–Ward, 2007

Graham Everest, Richard Miles, Shaun Stevens, Thomas Ward,
*Orbit-counting in non-hyperbolic dynamical systems*, *J. Reine Angew. Math.*
608 (2007), 155–182,
[author preprint](https://arxiv.org/pdf/math/0511569),
[institutional record](https://durham-repository.worktribe.com/output/1502557),
[DOI](https://doi.org/10.1515/crelle.2007.056).

Read scope: introductory Theorems 1.1 and 1.3, Section 2 including Lemma 2.4
and Corollary 2.5, and the detector convergence construction in the proof of
Theorem 1.1. The paper already owns the `S`-integer orbit-counting/detector
framework and a one-prime quantitative injectivity example. Its use of
“non-hyperbolic” is not substituted for BCH's unique-dominant-root definition.
No zero-upper-box-dimensional theorem for the present full FAD class was
identified in these inspected passages. Full-text term searches are only
supporting navigation, not proof of absence.

## 3. Recent near-owner and the book-version gap

Gunther Cornelissen and Sun Woo Park, *Orbit decomposition statistics for
discrete dynamical systems: the Cesàro mean and a large deviation principle*,
[arXiv:2605.24504v2](https://arxiv.org/abs/2605.24504v2), submitted
19 June 2026; [original PDF](https://arxiv.org/pdf/2605.24504v2), 23 pages
(the PDF itself carries a 23 June 2026 date).

Read scope: abstract and introductory Theorems A–D; Section 4's proof of
Theorem C, including its FAD decomposition; bibliography entries 4–8.
The observed FAD result concerns the Cesàro mean of normalized fixed counts,
feeding a large-deviation theorem for general orbit decompositions. That
observable is different from the topology of the limit set of normalized
prime-orbit counting. No claimed theorem in those passages supplies the
adaptive cover or perfectness argument of the candidate. Full-PDF searches
for Cantor/accumulation were also made; lack of a term hit is not the basis
of the mathematical distinction.

**Important residual uncertainty:** bibliography entry 6 describes BCH as
forthcoming in *Tracts in Mathematics*, EMS Press, 2026. A corresponding
final book text or publisher version was not obtained in this audit. The
[author publication list](https://webspace.science.uu.nl/~corne102/publications.html)
still links the older preprint title and 2022 description; the
[author arXiv index](https://arxiv.org/a/cornelissen_g_1.html) lists the
176-page v2 and the 2026 Cornelissen–Park paper. These are useful version
leads, not evidence that an unpublished revision cannot contain the result.
The [EMS book portal](https://ems.press/books) and targeted publisher-domain
searches did not yield an accessible matching new book text.

Consequently the permitted novelty wording is “no direct prior solution
was found in this bounded primary-source check,” not “the problem is
guaranteed still open worldwide on 2026-09-06.” A later source or a final
book update, if produced, must be compared before any stronger publication
priority statement. Author contact or external manuscript upload was not
performed or implicitly authorized.

## 4. Bounded search record

Searches were made through the available browser on 2026-09-06. Primary
arXiv/publisher/author/institutional pages were used for substantive claims.
Search snippets and secondary aggregators were used only as leads. Exact
query families included:

- `"finite-adelically distorted" Cantor`, dimension, box;
- `FAD orbit Hausdorff dimension`, `dynamical detector group Cantor dimension`;
- `orbit counting accumulation Cantor arithmetic`, `orbit-counting Cantor dimension`;
- `"Dynamics of endomorphisms of algebraic groups" 2025`, 2026, EMS;
- the older title ending `and related systems`, with EMS;
- `site:ems.press Cornelissen Houben`, `site:ems.press Byszewski`, and title queries;
- `Cornelissen Park accumulation`, plus the current author arXiv/publication lists.

The positive results and their actual read scopes are recorded above.
Searches returning unrelated books, group-theory papers, or catalog snippets
do not count as reviewed literature. No numerical census was required or
run: finite simulations would not establish the covering/perfectness
statements or settle ownership.

## 5. Internal collision check

The local scouting registry and relevant C374–C378, C389–C393,
C394–C398 idea reports were checked, as were C404–C406's frozen contracts
during initial selection. The p-adic interpolation and arboreal alternatives
were set aside for existing overlap; no registered theorem on the full
hyperbolic FAD orbit-limit image was located in that check.

The existing `s_integer_solenoid_chronology_zeta/IDEA_REPORT.md` was also
read: it studies noncommuting chronological cocycles, same-Parikh fibre
zeta analytic types, and continuation comparisons. Shared classical
solenoid fixed-count input is not a new owner, but its proved observable
and theorem are different from the present quantitative limit-set topology.
This is a scoped collision conclusion, not a claim to have reread every
file in the repository.

## 6. Independent review still required

Review should recheck every quantifier in Theorem 1, local rescaling in
Lemma 7, Fourier-type dominance and countable dominated convergence,
positivity of the negative-integer slice, the coprime-period CRT argument,
and the exact BCH detector reduction. Source/version uncertainty is
reported separately from mathematical correctness. No C-number, formal
Route-A score, final admission, or peer-review status is assigned here.
