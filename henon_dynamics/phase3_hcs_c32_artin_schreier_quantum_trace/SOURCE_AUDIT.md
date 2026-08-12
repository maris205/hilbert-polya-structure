# HCS-C32 Phase 3 primary-source audit

Date: 2026-08-12 UTC

Verdict: `PRIMARY_THEOREM_CHAIN_VERIFIED_WITH_LOCAL_SCOPE`

This audit records the exact source burden needed to turn the finite-field
collision into a theorem.  It does not claim novelty for the general Morse,
Gauss-sum, Fourier-transform, or Hill statements.

## 1. Deligne and Katz: henselian quadratic normal form

P. Deligne and N. Katz, eds., *Groupes de monodromie en géométrie
algébrique, SGA 7 II*, Lecture Notes in Mathematics 340, Springer, 1973,
Exposé XV. DOI: <https://doi.org/10.1007/BFb0060511>.

Verified author-hosted volume:
<https://publications.ias.edu/sites/default/files/Number12.pdf>

Verified PDF SHA-256:
`fa679debfc8ada3232d7e752a1837fc6ce474488e20a44d7641cf296876e1297`

Locators:

- Exposé XV, Theorem 1.2.6 and Corollary 1.3.2: ordinary quadratic
  singularities and henselian normal form in families;
- Exposé XV, §2.2.5 D/E: the quadratic vanishing-cycle character;
- Exposé XV, §§3.2.2--3.2.3: the corresponding quadratic local model.

Allowed use: a nondegenerate critical point in residue characteristic not two
is locally equivalent, in the henselian setting, to its quadratic model.

Forbidden promotion: this does not identify the global cohomology or the
contribution at infinity.

## 2. Fu: quadratic vanishing cycles and Thom--Sebastiani

L. Fu, *A Thom--Sebastiani theorem in characteristic p*, Mathematical
Research Letters 21 (2014), 101--119.
DOI: <https://doi.org/10.4310/MRL.2014.v21.n1.a8>.
Published PDF:
<https://intlpress.com/site/pub/files/_fulltext/journals/mrl/2014/0021/0001/MRL-2014-0021-0001-a008.pdf>.
Preprint: <https://arxiv.org/abs/1105.5210>.

Verified published-PDF SHA-256:
`566da1f0c1998db71563e92075a273db8059febb393983ba42e91fa12568aaba`

Locators in the verified published PDF:

- Example 2.3;
- Corollary 2.4 (published pages 104--105).

These passages compute the rank-one quadratic vanishing-cycle representation
and its parity-dependent Kummer/Tate description.  The arXiv v2 file labels
the same passages Example 1.3 and Corollary 1.4; the release citation uses the
formal journal numbering.

Allowed use: the Morse local object is rank one in its vanishing degree and is
controlled by quadratic Kummer/Gauss data.

Forbidden promotion: rank one does not give a canonical positive form,
self-adjoint operator, or Hilbert--Pólya structure.

## 3. Laumon: local Fourier transform and Gauss representation

G. Laumon, *Transformation de Fourier, constantes d'équations
fonctionnelles et conjecture de Weil*, Publications Mathématiques de l'IHÉS
65 (1987), 131--210. DOI: <https://doi.org/10.1007/BF02698937>.

Official scan: <https://www.numdam.org/item/PMIHES_1987__65__131_0.pdf>

Verified PDF SHA-256:
`c666e214ae586651b9f171f6a39d755e58f96379970ffa98bafb2d9be591fc8e`

Locators:

- Definition 2.4.2.3;
- Theorem 2.4.3;
- Proposition 2.5.3.1 (journal pages 162--166).

Allowed use: local Fourier transform converts the quadratic Kummer character
to the associated Gauss representation, subject to the paper's shifts and
local-direction conventions.

Shift firewall: the standard Fourier--Deligne functor includes ([1]), so its
trace function differs by a minus sign from the unshifted raw Fourier
integral used in the elementary exponential-sum calculation.

## 4. Deligne: extension characters and Hasse--Davenport

P. Deligne, *Cohomologie étale, SGA 4 1/2*, Lecture Notes in Mathematics
569, Springer, 1977. Official record:
<https://publications.ias.edu/node/378>.

Verified official PDF SHA-256:
`fb2939521f4c0ea0cdd55a90bec2e618e32fb433c78b194e705c6d989f4e42a6`

Locator: Theorem 1.15, Hasse--Davenport.

The present collision does not depend on choosing a Hasse--Davenport sign:
the explicit matrix (C\in\operatorname{GL}_5(\mathbb F_{61})) base-changes
to every extension and directly identifies the two quadratic sums.  The
source is retained to control extension-character conventions.

## 5. Bolotin and Treschev: discrete Hill formula

S. V. Bolotin and D. V. Treschev, *Hill's formula*, Russian Mathematical
Surveys 65 (2010), 191--257.
DOI: <https://doi.org/10.1070/RM2010v065n02ABEH004671>.

Locator: Theorem 2.1.

Allowed use: the general relation between the Hessian of a discrete
Lagrangian action and the determinant of the return-map linearization.

The Phase-3 code also reconstructs both sides independently and verifies the
specialized sign orbit by orbit, so the (p=61) collision does not rest on a
numerical or bibliographic sign guess.

## 6. Prior-work and novelty audit

The following components are prior art or formal consequences:

- the henselian Morse lemma;
- quadratic Gauss sums and their dependence on discriminant square class;
- rank-one quadratic vanishing cycles;
- local Fourier transform of Kummer characters;
- the discrete Hill formula;
- the generic Deligne rank/purity theorem for the smooth leading cubic;
- chronological kernel composition by compactly supported pushforward.

The Phase-3 delta is narrower:

1. an exact Hénon-specific pair of primitive five-cycles over
   (mathbb F_{61});
2. equal critical value and explicitly congruent Hessian forms;
3. unequal Hill determinant values;
4. the resulting source-certified obstruction to recovering the full Hill
   value from the unframed Morse-local representation.

No audited source was found that states this Hénon-specific collision.  This
is a search-bounded novelty statement, not a claim of exhaustive absence.

## 7. Claim boundary

The source chain supports

`GOOD_PRIME_MORSE_LOCAL_HILL_INFORMATION_GATE=STOP`.

It does not support:

- `GLOBAL_ARTIN_SCHREIER_COHOMOLOGY=TRIVIAL`;
- `ALL_HENON_DEFORMATIONS=OBSTRUCTED`;
- `DEGENERATE_VANISHING_CYCLES_FORGET_HIGHER_JETS`;
- `CONTRIBUTION_AT_INFINITY=ZERO`;
- `HILBERT_POLYA_OPERATOR_EXISTS`.

## 8. AI-use disclosure

AI assistance was used for source discovery, formula cross-checking, exact
experiment design, code generation, and synthesis.  Primary statements were
checked against the cited PDFs; the exact witness is independently replayed
by a checker that does not import the producer.
