# Paper 22 Phase-2 source, site, and obstruction screen

Date: **2026-08-24**

Status: **REVISE TO AN EXACT SITE AND EXTENSION-OBSTRUCTION PRECHECK**

This report binds the source-authored problem and its nearest precedents.  It
does not solve the fppf lift, authorize a manuscript, or construct a bridge to
any packet, flow, operator, or Route object.

**Phase-3 correction (2026-08-24):** the later explicit descent proof shows
that the sectionwise Dedekind equality printed as Deninger's Corollary 4.6 is
false already for `A=k[x]` on the finite-flat site.  Proposition 4.3 gives
local/sheaf surjectivity, not surjectivity on `A`-sections.  Do not use item 4
below as a positive comparator; see
[the all-index nonlift theorem](phase3_all_index_nonlift_theorem.md), Section
5.1.  The fppf inputs from Propositions 4.3 and 4.5 and Example 4.4 remain
valid.

## 1. Search protocol

Search date: **2026-08-24**.

Search surfaces included arXiv API/full text, OpenAlex, Crossref, EMS Press,
Cambridge Core, AMS, Springer Nature, the Stacks Project, and targeted web
discovery used only to locate primary or official records.  Exact arXiv query
families included:

```text
"sheafified Verschiebung"
Verschiebung AND fppf
"Rational Witt vectors and associated sheaves"
"reduced monoid algebra" AND Verschiebung
Verschiebung AND sheafification
Verschiebung AND "monoid algebra"
Verschiebung AND "K-theory of endomorphisms"
Verschiebung AND "Witt vectors"
```

The first six exact-owner searches returned only Deninger's source or zero
hits.  The broader Witt-vector result set was screened title-by-title and
abstract-by-abstract.  Inclusion required full-text inspection of a primary
paper or official mathematical reference that either defines the exact owner
or supplies a clearly delimited kernel, quotient, extension, or F/V
precedent.  p-typical, derived, KEnd, TR, and arithmetic-jet owners were
excluded from the load-bearing conclusion.

Bounded-search result:

```text
NO_DIRECT_EXACT_POST_SOURCE_SOLUTION_FOUND
```

This is not a global novelty theorem.

## 2. Exact source binding

The exact owner is Christopher Deninger, *Rational Witt vectors and
associated sheaves*, arXiv `2508.05329v1` (2025), DOI
`10.48550/arXiv.2508.05329`.

The source allows a Stacks-style small version of `AffSch` or
`NoethAffSch`.  The first Paper-22 branch is now frozen as a fixed small
skeleton of the absolute category

```text
C = NoethAffSch_fppf
```

over `Spec Z`, equipped with the usual fppf pretopology.  No extra relative
base scheme is introduced.  Here “fp topology” in the source means the
**finite-flat** topology, not a finite-presentation topology; it remains a
separate comparator.

For a commutative unital ring `A`, the source uses

```text
underline Z A = Z[A,multiplication] / Z(0),
W_rat(A)       = rational big Witt vectors inside 1+T A[[T]].
```

After sheafification on `C`, Teichmueller elements `[a]=1-aT` induce

```text
omega: underline Z(O)^sharp ->> W_rat(O)^sharp.
```

The operation `V_N` is an **additive** big-Witt endomorphism, represented by

```text
V_N(f)(T)=f(T^N).
```

Therefore the desired lift is initially an additive sheaf endomorphism, not
a ring endomorphism.

Source locators in the v1 PDF are equation (4), p. 3; equation (20), p. 14;
Proposition 4.3, p. 21; Example 4.4, p. 22; Corollary 4.6, p. 23;
Corollary 4.7, p. 24; and the open question, p. 25.

Primary links:

- <https://arxiv.org/abs/2508.05329>
- <https://arxiv.org/html/2508.05329v1>
- <https://stacks.math.columbia.edu/tag/021L>

## 3. Controls supplied by the source

1. Proposition 4.3 makes `omega^sharp` a sheaf epimorphism for a topology
   whose covers include the relevant syntomic finite locally free covers;
   this applies to fppf.
2. Example 4.4, on `F_2[epsilon]/(epsilon^2)`, shows noninjectivity on every
   subcanonical topology.  The fppf problem cannot be solved by pretending
   `omega` has an inverse.
3. Corollary 4.7 gives an isomorphism and hence an additive lift on certain
   non-subcanonical sites finer than the finite pretopology.  This is a
   positive comparator, not an fppf answer.
4. **SUPERSEDED BY PHASE 3:** Corollary 4.6 prints a finite-flat-site
   identification for Dedekind-ring sections, but the all-index descent
   witness counterexamples its sectionwise surjectivity.  Only its
   Proposition-4.5-based injectivity component survives.

## 4. Source matrix and maximum-prior subtraction

| Source | Exact role | Boundary |
|---|---|---|
| C. Deninger, arXiv `2508.05329v1` | exact objects, epimorphism, controls, and explicit fp/fppf open question | a v1 preprint; no fppf kernel or lift criterion is computed |
| C. Deninger, A. Mellit, *ZR and rings of Witt vectors W_S(R)*, RSMUP 142 (2019), 93--102, DOI `10.4171/RSMUP/32` | Theorem 1.1 gives an explicit kernel for a nearby monoid-algebra-to-Witt map | different quotient and no fppf sheafification |
| E. Dotto, A. Krause, T. Nikolaus, I. Patchkoria, *Witt vectors with coefficients...*, Compos. Math. 158 (2022), 366--408, DOI `10.1112/S0010437X22007254` | Propositions 1.23 and 1.39--1.41 show F/V descent through kernel preservation for another Witt owner | not Deninger's sheaf epimorphism |
| A. Blumberg, D. Gepner, G. Tabuada, *K-theory of endomorphisms via noncommutative motives*, TAMS 368 (2016), 1435--1465, DOI `10.1090/tran/6507` | Definition 5.6 and Theorem 5.7 classify `V_n` operations within KEnd | different stable-infinity-category owner |
| S. Agarwal et al., *Frobenius and Verschiebung for K-theory of endomorphisms*, arXiv `2507.05956v1` | twisted-KEnd operations, composition laws, and trace compatibility | predates Deninger's question and has no fppf reduced-monoid sheaf |
| J. Campbell et al., *K-Theory of Endomorphisms, the TR-Trace, and Zeta Functions*, La Matematica 4 (2025), 214--292, DOI `10.1007/s44007-025-00154-0` | rational power-series/KEnd/big-Witt/TR comparison | no `omega^sharp` or fppf descent |
| Stacks Project Tags `03CN`, `010I`, `06XP` | abelian sheaves, extensions, and derived `Ext` | generic formalism; no arithmetic kernel computation |

Additional primary links:

- <https://doi.org/10.4171/RSMUP/32>
- <https://doi.org/10.1112/S0010437X22007254>
- <https://doi.org/10.1090/tran/6507>
- <https://arxiv.org/abs/2507.05956>
- <https://doi.org/10.1007/s44007-025-00154-0>
- <https://stacks.math.columbia.edu/tag/03CN>
- <https://stacks.math.columbia.edu/tag/010I>
- <https://stacks.math.columbia.edu/tag/06XP>

The KEnd/TR and p-typical precedents are not evidence that the exact lift
exists.  They are retained only to prevent owner substitution.

## 5. Correct first obstruction

In `Ab(C)`, put

```text
Z = underline Z(O)^sharp,
W = W_rat(O)^sharp,
K = ker(omega),
e : 0 -> K -> Z -> W -> 0.
```

Thus `e` defines a class in `Ext^1(W,K)`.  If an additive lift
`tilde V_N:Z->Z` satisfies

```text
omega o tilde V_N = V_N o omega,
```

then it preserves `K` and induces an endomorphism `u:K->K`.  For a fixed
`u`, the exact extension-theoretic criterion is

```text
u_* e = V_N^* e              in Ext^1(W,K).
```

When this equality holds, the lifts inducing `u` form a
`Hom(W,K)`-torsor.  This is a general precheck lemma derived from extension
functoriality; it is not Deninger's missing arithmetic theorem.

The previous methodology's immediate jump to a “Cech obstruction” was too
strong.  A Cech representative is available only after selecting an actual
cover/resolution and proving that it computes the relevant sheaf `Ext` class.

## 6. Binding next gate

The first nontrivial test is frozen at `N=2`; `V_1=id` is a control only.
Before proof promotion, the project must:

1. compute the actual fppf sheaf `K` sufficiently to determine endomorphisms
   `u` relevant to `V_2`;
2. identify the extension class `e` and compute `V_2^*e`;
3. decide whether some `u` satisfies `u_*e=V_2^*e`;
4. in the positive case, construct the lift and prove naturality/additivity;
   in the negative case, retain an explicit obstruction object or section;
5. only then audit Frobenius/Verschiebung identities and any larger family of
   indices.

If the work ends with the abstract `Ext` equality but no calculation for
`N=2`, it fails the frozen theorem threshold.

## 7. Phase-2 verdict

```text
EXACT_SOURCE_OWNER=PASS
EXACT_FPPF_EPIMORPHISM=PASS
DIRECT_POST_SOURCE_SOLUTION=NOT_FOUND_IN_BOUNDED_SEARCH
ORIGINAL_CECH_FIRST_METHOD=REVISE
EXTENSION_OBSTRUCTION_PRECHECK=PASS
ACTUAL_KERNEL_AND_EXTENSION_COMPUTATION=NOT_STARTED
PROOF_LOCK=NOT_READY
MANUSCRIPT=NOT_AUTHORIZED
ROUTE_ADVANCEMENT=NONE
```

Historical-state note: the last four lines record the end of Phase 2.  They
are superseded by the Phase-3 theorem linked above; in particular the actual
descent obstruction is now computed and the proof lock has passed.

The project remains live because the open problem is genuine and correctly
typed.  It does not yet pass into a proof phase because the nonformal
arithmetic calculation has not begun.
