# Independent Postrun Theorem-Quantifier and Scope Audit

**Candidate:** `cat_equivariant_retention_tradeoff_v1`  
**Audit date:** 2026-08-15 UTC  
**Audit mode:** fresh read-only semantic audit; no experiment or candidate run;
no network access; no mutation of source, code, result, report, manifest,
manuscript, plan, or figure assets  
**Verdict:** `PASS_WITH_SCOPE_CORRECTION`

## Executive disposition

The sentence

> none of the four audited scalar reductions has both source support
> $r_q$ and unit exponent

is false under the natural per-row quantification used in the frozen proof,
research question, source lock, claims matrix, and prose description of
K011.  At the locked row

$$
q=2,\qquad n_2=3,\qquad r_2=3,\qquad m_2=1,
$$

the point-cardinality reduction is exactly

$$
(1-t^{r_2})^{-m_2}=(1-t^3)^{-1}.
$$

It therefore has both source support and unit exponent.  This is not a
rounding issue, convention issue, or ambiguity in the raw payload: both
scientific engines, the frozen expected ledger, the official table, and the
independent result table all record the exact pair $(3,1)$.

The raw arithmetic records remain correct.  The implemented K011 Boolean is
also true, but it checks a weaker family-level proposition: no one reduction
type supplies both properties uniformly over the complete locked family.  It
does not check that every reduction in every row fails to combine them.

The terminal A0 disposition remains valid under this corrected scope.  The
$q=2$ point-cardinality factor is a one-cycle source factor, but its support
is $r_2=3$, not an intrinsic modulus label; the locked collision
$r_2=r_4=3$ proves that this period does not identify $q$, and the full
construction still supplies neither a prime selector nor a common cross-$q$
clock.  Accordingly, the immutable classification may remain

`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /`
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`

only if the publication layer defines the tradeoff as family-nonuniform and
states the $q=2$ exception prominently.  Silent reuse of the stronger
per-row claim would make the publication fail this audit.

## 1. Exact quantifiers

Let

$$
\mathcal Q=(2,3,5,7,11,4,6,9,10)
$$

and let the four reduction types be

$$
J=\{\kappa\mathrm{pt},\Phi\mathrm{pt},
      \kappa\mathrm{orb},\Phi\mathrm{orb}\}.
$$

Write $(S_j(q),E_j(q))$ for the support and positive exponent of the sole
factor of reduction type $j$ at modulus $q$, and define

$$
P_j(q)\iff \bigl(S_j(q)=r_q\bigr)\land\bigl(E_j(q)=1\bigr).
$$

The frozen formulas, which are correct, give

$$
\begin{array}{c|c}
j & (S_j(q),E_j(q))\\ \hline
\kappa\mathrm{pt} & (r_q,m_q)\\
\Phi\mathrm{pt} & (r_q,1/r_q)\\
\kappa\mathrm{orb} & (1,n_q)\\
\Phi\mathrm{orb} & (1,1).
\end{array}
$$

The overstrong claim is

$$
\forall q\in\mathcal Q\;\forall j\in J:\ \neg P_j(q).
\tag{false per-row claim}
$$

It is false because $P_{\kappa\mathrm{pt}}(2)$ is true.

The exact locked-row statement is

$$
P_{\kappa\mathrm{pt}}(2)\text{ is true, and every other }P_j(q)
\text{ is false.}
\tag{exact locked statement}
$$

Equivalently:

- for $q=2$, exactly one of the four reductions has both properties;
- for every $q\in\mathcal Q\setminus\{2\}$, none of the four does; and
- over all 36 locked row/type pairs, $(2,\kappa\mathrm{pt})$ is the unique
  positive pair.

The correct family-uniform statement is

$$
\neg\exists j\in J\;\forall q\in\mathcal Q:\ P_j(q),
\tag{correct family-uniform claim}
$$

or, equivalently,

$$
\forall j\in J\;\exists q\in\mathcal Q:\ \neg P_j(q).
$$

In words: **no single scalar-reduction type has source support and unit
exponent uniformly across the locked nine-row family.**

At theorem level, the safe statement is conditional rather than universal:
the point-cardinality reduction has both properties exactly when $m_q=1$;
the point-orbifold exponent is $1/r_q$; and both orbit-order reductions have
support one.  For the present matrix, $r_q>1$ for every $q\ge2$ because
$A\not\equiv I\pmod q$ (its off-diagonal entry is $1$).  Thus any exception
to the four-way failure can only come from $m_q=1$ in the
point-cardinality row; the locked family contains precisely the observed
$q=2$ exception.  No stronger all-$q$ assertion about when $m_q=1$ is
needed or authorized here.

## 2. Audit of all nine rows and all four factors

Each entry is `(support, exponent)`.  A star marks simultaneous source
support and unit exponent.

| $q$ | $(n_q,r_q,m_q)$ | $\kappa$(point) | $\Phi$(point) | $\kappa$(orbit) | $\Phi$(orbit) |
|---:|---:|---:|---:|---:|---:|
| 2 | $(3,3,1)$ | **$(3,1)^\star$** | $(3,1/3)$ | $(1,3)$ | $(1,1)$ |
| 3 | $(8,4,2)$ | $(4,2)$ | $(4,1/4)$ | $(1,8)$ | $(1,1)$ |
| 5 | $(20,10,2)$ | $(10,2)$ | $(10,1/10)$ | $(1,20)$ | $(1,1)$ |
| 7 | $(48,8,6)$ | $(8,6)$ | $(8,1/8)$ | $(1,48)$ | $(1,1)$ |
| 11 | $(100,5,20)$ | $(5,20)$ | $(5,1/5)$ | $(1,100)$ | $(1,1)$ |
| 4 | $(12,3,4)$ | $(3,4)$ | $(3,1/3)$ | $(1,12)$ | $(1,1)$ |
| 6 | $(24,12,2)$ | $(12,2)$ | $(12,1/12)$ | $(1,24)$ | $(1,1)$ |
| 9 | $(72,12,6)$ | $(12,6)$ | $(12,1/12)$ | $(1,72)$ | $(1,1)$ |
| 10 | $(60,30,2)$ | $(30,2)$ | $(30,1/30)$ | $(1,60)$ | $(1,1)$ |

The table independently exposes both relevant facts:

1. the per-row `none` claim has one exact counterexample; and
2. no column/reduction type is starred in every row.

## 3. What K011 actually certifies

The K011 predicate is duplicated in `candidate.py` and `manifest.py`.  Its
logical structure is:

1. `not all(...)` point-cardinality exponents are one;
2. all point-orbifold exponents are nonunit; and
3. in every row, both orbit reductions have support different from $r_q$.

Together with the already checked point supports, this establishes the
family-uniform claim above.  In particular, the first clause is

$$
\neg\forall q\in\mathcal Q:\ E_{\kappa\mathrm{pt}}(q)=1,
$$

not

$$
\forall q\in\mathcal Q:\ E_{\kappa\mathrm{pt}}(q)\ne1.
$$

Consequently:

- raw `controls.K011 = true` is correct for the implemented predicate;
- the code and manifest recomputation agree;
- the prose label in `INDEPENDENT_RESULT_INTEGRITY.md` saying that no
  audited scalar reduction has both properties is an invalid strengthening;
  and
- neither manifest closure nor the postrun analyzer converts that stronger
  gloss into a proved statement.  Those mechanisms correctly preserve and
  validate the immutable payload; they do not repair a theorem quantifier.

No code or result mutation is necessary to report the correct raw fact.
K011 must simply be described as a **family-uniform nonattainment** control,
not as a **per-row nonattainment** control.

## 4. Raw classification and A0 validity

### 4.1 Retention--compression classification

`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED` remains defensible
with an explicit scope definition:

> Across the locked family, no one of the four scalar-reduction types
> uniformly combines source support with unit exponent.  At the individual
> row $q=2$, the point-cardinality reduction is the unique locked exception,
> because the source already consists of one cycle ($m_2=1$).

The token must not be glossed as disjointness of retention and compression
at every modulus.

### 4.2 A0 disposition

`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC` remains valid.  The frozen research
question requires not merely a unit factor, but an **intrinsic
modulus/prime clock**.  The $q=2$ exception satisfies only the local
one-factor condition:

- its support is $r_2=3$, not $q=2$;
- $r_2=r_4=3$, so the support is not modulus-injective;
- use of the shell label $q$ or the substitution $t=q^{-s}$ remains
  external;
- the coefficient and stronger-carrier categories vary with $q$ and no
  common comparison map is supplied; and
- composite moduli satisfy the same construction, so no prime selector is
  obtained.

Thus C23--C25 and the exact externality record suffice for A0.  The false
per-row version of C21 is not required for the modulus-global conclusion.
The A0 rationale must, however, be written as failure of a common intrinsic
modulus/prime clock, not as absence of every local one-cycle source factor.

### 4.3 Route B

`ROUTE_B_NOT_OPENED` is unaffected.  The $q=2$ identity is an elementary
member of the already frozen scalar ledger and supplies no transfer,
Fredholm, Hecke, quantization, Ruelle/Fried, prime-zero, or analytic
authority.

## 5. Publication-layer correction requirements

It is honest to leave the immutable source, execution tree, raw results,
reports, and manifest unchanged **only if** the manuscript treats them as
preserved provenance and explicitly records this postrun scope correction.
A silent reinterpretation is not sufficient.

### 5.1 Mandatory disclosure

The manuscript must contain a visible theorem-scope or provenance statement
substantially equivalent to:

> Frozen design prose described the four-way comparison with an overstrong
> per-row quantifier.  The exact registered ledger contains one exception:
> for $q=2$, $m_2=1$ and the point-cardinality reduction is
> $(1-t^3)^{-1}$.  The registered K011 predicate checks instead that no
> reduction type has source support and unit exponent uniformly across the
> locked family.  We use only this family-uniform statement.  The raw
> formulas and results are unchanged, and the A0 conclusion concerns the
> absence of a common intrinsic modulus/prime clock.

This disclosure should appear before the first substantive use of the
tradeoff, with a concise reminder in the exact-results section or appendix.

### 5.2 Abstract and introduction

If the scalar tradeoff is mentioned, use wording such as:

> No one of the four scalar-reduction types combines source support and unit
> exponent uniformly over the locked nine-row family; the sole individual
> exception is the point-cardinality factor at $q=2$, where $m_2=1$.

The existing broader conclusion may then follow:

> This exception still does not produce a common intrinsic modulus clock or
> a prime selector.

### 5.3 Theorem, proposition, and proof wording

After displaying the four exact formulas, the manuscript must state:

> The point-cardinality factor has source support and unit exponent exactly
> when $m_q=1$.  In the locked ledger this occurs at $q=2$ and nowhere else.
> The point-orbifold factor retains source support with exponent $1/r_q$,
> while the two orbit factors have support one.  Hence no one reduction type
> supplies both properties uniformly across the locked family.

The proof must derive this directly from the formulas.  It must not repeat
the frozen proof sentence that all four outputs fail simultaneously for an
arbitrary row.

### 5.4 Claims and result-language wording

Any publication claims matrix should replace the frozen C21 gloss with:

> **C21-corrected:** No one of the four scalar-reduction types has source
> support and unit exponent for every modulus in the locked family.  The
> unique locked row/type exception is
> $(q,j)=(2,\kappa\mathrm{pt})$.

When K011 is reported, label it:

> `K011 — family-uniform source-support/unit-exponent nonattainment`.

The manuscript may cite the immutable result-review file as provenance, but
must flag its stronger K011 prose description as superseded by this semantic
audit.  It may not quote that line as theorem evidence.

### 5.5 Table, figure, and caption requirements

- The main four-reduction table must show the $q=2$ point-cardinality entry
  $(3,1)$ and visibly mark it as the sole locked exception.
- Figure 1's point-cardinality branch must read
  `support r_q; exponent m_q; unit when m_q=1`, not an unconditional
  retention/compression exclusion.
- Figure 2 panel C must display the exact $q=2$ cell and may summarize the
  column-level result as `no family-uniform starred column`.
- Figure 2's caption must state both that $q=2$ is the sole individual
  exception and that the conclusion is family-uniform.  Suitable wording is:

  > Exact support/exponent ledger.  The point-cardinality reduction at
  > $q=2$ is $(3,1)$, the sole locked row/type pair combining source support
  > and unit exponent.  No reduction type does so uniformly across all nine
  > rows; the retained support still fails to identify the modulus because
  > $r_2=r_4=3$.

- Figure 3 need not carry the scalar exception, but neither its labels nor
  its caption may infer that effectivity or static inertia proves the false
  per-row scalar claim.
- Any graphical use of `tradeoff certified` must include a legend or caption
  defining `tradeoff` as family-nonuniform, not pointwise mutual exclusion.

### 5.6 A0 conclusion wording

Use:

> Although the $q=2$ source already has one cycle and therefore yields the
> unit point-cardinality factor $(1-t^3)^{-1}$, the support $3$ is not an
> intrinsic modulus clock: it also occurs at $q=4$.  Across the locked
> family no scalar reduction supplies a uniform source-support/unit-exponent
> construction, stronger coefficients remain in varying labelled
> categories, and composites obey the same hierarchy.  The audited
> constructions therefore produce neither a common intrinsic modulus clock
> nor a prime selector.

## 6. Forbidden stronger claims

The publication must not state or imply any of the following:

1. “None of the four audited scalar reductions has both source support and
   unit exponent,” without an explicit family-uniform qualifier and the
   $q=2$ exception.
2. “For every locked $q$” or “for every $q\ge2$, none of the four reductions
   has both properties.”
3. “Obtaining $(1-t^{r_q})^{-1}$ always requires a $q$-dependent
   normalization.”  It requires no normalization when $m_q=1$, including
   the locked $q=2$ row.
4. “Every source-supporting cardinality reduction restores multiplicity
   greater than one.”  At $q=2$ the restored multiplicity is one.
5. “K011 proves per-row nonattainment,” or any equivalent interchange of
   `not all` with `all not`.
6. “The immutable proof package is provable as stated” with respect to the
   four-way nonattainment sentence.  Its formulas are correct; that
   inference is not.
7. “A0 fails because no local one-factor source-supported output exists.”
   The defensible A0 reason is the absence of a **common intrinsic
   modulus/prime clock**.
8. Any universal claim about all possible equivariant, orbifold, stacky,
   representation-valued, weighted, or analytic refinements.

## 7. Hash-bound evidence

The audit conclusions above bind the following observed SHA-256 digests.
All paths are relative to `papers/11-cat-equivariant-clock/`.

| Role | Path or tree | SHA-256 |
|---|---|---|
| frozen source lock | `experiments/source_lock.json` | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` |
| frozen proof | `notes/PROOF_PACKAGE.md` | `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948` |
| frozen research question | `notes/RESEARCH_QUESTION.md` | `f695dd359e4f965fcf13e7c4550daf9ae90ce6565fbdb61a8c3a39fb2cee174a` |
| frozen claims matrix | `notes/CLAIMS_EVIDENCE_MATRIX.md` | `0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490` |
| frozen experiment plan | `experiments/EXPERIMENT_PLAN.md` | `2e69d035a315061cf0cbc9608fae66cbc2545480b84dabaa6e20b3a40f3409e5` |
| K011 execution implementation | `code/equivariant_clock/candidate.py` | `cd8ca382a4178add3702aa76f13df76dfa57751a0525320c2a9b1b4d02c3751b` |
| K011 manifest recomputation | `code/equivariant_clock/manifest.py` | `039617f436d657ce145188826340742d66c768b121091aab57a1d98e01e4a909` |
| immutable execution tree | manifest-bound framed tree | `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb` |
| raw exact result | `results/EXPERIMENT_RESULTS.json` | `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe` |
| registered claim | `results/registered_run.claim.json` | `c58c9bc93d0e6af2440c163323d7dcc3c098a0c470f0f11bfb31fa98fb82c79f` |
| registered terminal | `results/registered_run.json` | `e6ec2c40094a933a3b6f18a46afb36df538e84fb8afee9b63ba6ab166acbe983` |
| independent result report | `results/INDEPENDENT_RESULT_INTEGRITY.md` | `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20` |
| official exact-result report | `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `06f547fdfbbfb3bd51a57041758a49f18acceca9dda8e19967c2364500d64918` |
| official validation report | `experiments/OFFICIAL_VALIDATION_REPORT.md` | `754a36c0e2e6b5c5002ecb8b3473d0af0e077b4f5b88da2bc6851bdafad23221` |
| postrun analyzer review | `results/POSTRUN_ANALYZER_REVIEW.md` | `ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8` |
| strict result manifest | `results/result_manifest.json` | `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c` |
| paused paper plan | `PAPER_PLAN.md` | `f43a7f18194cf35f606ba6df20e0ceb8bb28c7693214cc9d512b4d0c3d1ca118` |
| paused manuscript | `paper/manuscript.tex` | `2b8c4305a46f0a923414834d896e48f95260b1b666e3fd327e2e849796a2f8e0` |

The manifest itself reports `pass: true`, the exact terminal
classification, and the same raw-result, source-lock, execution-tree, and
result-review bindings.  This audit does not dispute closure or provenance;
it corrects the scope of one semantic inference drawn from the preserved
payload.

## Final verdict

`PASS_WITH_SCOPE_CORRECTION`

The pass is conditional on implementing every publication-layer requirement
in Section 5 and avoiding every claim in Section 6.  If the manuscript,
tables, figures, captions, claims matrix, or final integrity record repeats
the unqualified per-row `none` claim, the disposition becomes `FAIL`.
