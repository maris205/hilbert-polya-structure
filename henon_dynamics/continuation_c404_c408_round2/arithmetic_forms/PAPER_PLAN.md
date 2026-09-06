# C405 paper plan

Title: Singular Gram limits at the critical line of Dirichlet convolution.

One sentence: critical normalized divisibility Grams have a nonzero GCD
entrywise limit but collapse in strong resolvent sense when the coefficient
square sum diverges, whereas the summable alternative has a nonzero maximal
convolution limit.

Type: complete mathematics short article, not an ML venue submission.
Plain article, anonymous author block, no invented affiliation or arbitrary
page quota. All proofs, quantifiers and maximal-domain arguments belong in
the actual PDF. The whole result is one paper, not one paper per limit case.

## Claim–evidence map

| Claim | Evidence | Position |
|---|---|---|
| Prime-product kernel has a precise closability boundary | proof §§1–2, independent arithmetic review | Supporting explicit witness; classical positivity credited |
| Critical divergent Grams have purely singular entrywise limit and zero strong-resolvent limit | proof §§2–4, reviewer reconstruction | Main theorem, divergent branch |
| Summable critical coefficients converge to nonzero C*C/F_infinity | proof §5, maximal-domain variational proof | Main theorem, summable branch |
| Nonmultiplicative slow variation is covered | proof (6)–(7) and hypotheses | Full family, not an example table |
| Finite exact identities agree and invalid-tail controls fail | exact_checks.py, BOUNDED_RECEIPTS.md | Finite sentinels only, never the limiting proof |

## Proposed sections

0. Abstract: immediately state the nonzero-entrywise/zero-resolvent contrast,
   both summability branches, and the fixed ell² setting. No priority claims.
1. Introduction and positioning: distinguish finite GCD norm studies,
   Hilberdink Gram formulas, subcritical LCM/Schatten limits and classical
   form relaxation. State the full dichotomy before the auxiliary lemmas.
2. Arithmetic product forms: finite Poisson positivity, prime shifts, exact
   tail identities, pure singularity and converse closability. The general
   form decomposition belongs to Simon; do not relabel it as a new theory.
3. Variational consequence: complete diagonal recovery and resolvent proof
   for positive entrywise approximants; norm divergence. This is a useful
   consequence of the arithmetic witness, not a separately claimed discovery.
4. Critical regular variation: actual finite Gram identity and all UCT,
   summation and floor bounds. Highlight why A_N(1,1)=1 is compatible with
   the stated resolvent convergence.
5. Square-summable alternative: maximal rowwise convolution, dense closed
   domain, finite-row weak lower bound, recovery at the true minimizer and
   strong convexity. Do not assume coordinate truncations are a graph core.
6. Examples, checks and limitations: log-power threshold beta=1/2, the
   exact finite sentinel and invalid-tail control, no numerical proof of
   infinite claims, no exclusion of all other Hilbert-space renormalizations.
7. Conclusion and reproducibility: one fixed-space obstruction/dichotomy,
   not target Euler factors or an RH/HP theorem. AI and internal-review
   disclosure; no human-peer-review or submission-readiness promise.

A compact branch comparison table can clarify the two mathematical limits
and classical subcritical context. No plots are needed; do not draw numerical
resolvent convergence from infeasibly slow prime-tail scales.

## Citations and review

Use the actual scopes in SOURCE_AUDIT.md, now including Simon 1978 original
§§2–3 following the non-author recommendation. Hilberdink's arbitrary Gram
identity, ABS finite Poisson positivity, Hilberdink–Pushnitski compact LCM
results and standard regular variation are owned inputs. Cite only sources
that support a statement in the draft. BGT book metadata may be used without
inventing an unread theorem/page locator. New metadata must come from trusted
author/publisher records, DOI data or verified existing project BibTeX.

Independent proof/source review is
`../henon_resonance/CROSS_REVIEW_ARITHMETIC_FORMS.md`: mathematical blockers 0,
theorem corrections 0. The accepted source amendment changes attribution,
not mathematics. The manuscript still needs an actual non-author text,
claim/citation and reverse-outline check, then final deterministic builds.
