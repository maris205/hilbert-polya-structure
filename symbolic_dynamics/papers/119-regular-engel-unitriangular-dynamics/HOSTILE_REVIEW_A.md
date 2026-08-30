# Hostile Review A — P119

Status: independent nonauthor review. External dissemination, novelty,
priority, and submission remain **HOLD**. I reviewed the complete paper-local
package, `main.tex`, the six-page `main.pdf`, the bibliography, the canonical
verifier and transcript, and every supporting claim/control document. I did
not edit the manuscript or consult another review.

## Provisional verdict

**MAJOR REVISION AND A FRESH OWNER GATE.** I found no counterexample to the
stated algebraic or dynamical formulas. The commutator orientation, the two
one-step derivations, all iterated fibres and layers, the filtration
indegrees, the zeta calculation, and the nonregular `U_4` control all survive
independent reconstruction, including characteristic two and the small
endpoints. The package is nevertheless not circulation-ready: it omits a
2013 paper whose Lemma 1 proves the same fixed-regular restricted
surjectivity and whose Theorem 1 uses the same fixed second entry for the
iterated Engel image. That result owns the backbone from which the temporal
census is derived.

Severity count: **C: 1 (owner/claim boundary, not a mathematical
counterexample); M: 0; m: 2.**

## Independent reconstruction

Let `N=sum E_(i,i+1)`, `J=I+N`, and use the manuscript's convention

`E(X)=[X,J]=X^(-1) J^(-1) X J`.

For `gamma_k=I+n_k`, products of offset at least `r` and offset at least `s`
have offset at least `r+s`. Hence
`E(gamma_k) subset gamma_(k+1)` in every characteristic.

Put `phi(X)=J^(-1)XJ`. If `E(X_1)=E(X_2)=Y`, then

`phi(X_2 X_1^(-1))=X_2 Y (X_1 Y)^(-1)=X_2 X_1^(-1)`.

Conversely a `phi`-fixed `h` satisfies `E(hX)=E(X)`. Thus a nonempty fibre
is the **left** coset `C_(gamma_k)(J) X`; the orientation printed in the paper
is correct. Commuting with `J` is equivalent to commuting with the regular
shift `N`. The boundary equations and diagonal recurrence give the full
matrix centralizer `F_q[N]`, so

`C_(gamma_k)(J)={I+a_k N^k+...+a_(n-1)N^(n-1)}`

and its order is `q^(n-k)`. Once surjectivity is known, this gives the stated
uniform one-step fibre.

The coordinate route also reconstructs without division. Writing
`X=I+A`, `Y=I+B`, the equation `E(X)=Y` is exactly

`AN-NA=B+NB+AB+NAB`.

On source superdiagonal `r`, the left side is the difference map

`Delta_r(x_1,...,x_(n-r))=(x_1-x_2,...,x_(n-r-1)-x_(n-r))`.

It is onto with a one-dimensional constant kernel over every finite field,
including characteristic two. Since `B` starts at offset `k+1`, the `AB`
and `NAB` contributions at stage `r` use only source offsets strictly below
`r`. There are therefore `n-k` successive free constants and exactly
`q^(n-k)` solutions. No inverse of a field element or characteristic
restriction is hidden in this proof.

Composing the uniform restricted maps gives

`E^t(gamma_k)=gamma_(k+t)` and
`#(E^t|_(gamma_k))^(-1)(Y)=q^S_(k,t)`

for `Y in gamma_(k+t)`, where
`S_(k,t)=sum_(j=k)^(k+t-1)(n-j)`. Taking the root fibre and consecutive
differences yields

`L_(k,t)=(q^(n-k-t+1)-1) q^S_(k,t-1)`

for `1<=t<=n-k`. At `k=1,t=n-1` this is
`(q-1)q^(binom(n,2)-1)`. Subtracting the nested source fibres gives the two
filtration-indegree formulas. Since every state reaches `I`, the functional
graph has one component and only the loop at `I`; hence every positive
iterate fixes exactly one point and the zeta function is `(1-z)^(-1)`.

Finally, for `J'=I+E_12+E_34` in `U_4`, direct multiplication gives

`A(E_12+E_34)=(E_12+E_34)A`

if and only if `a_23=0` and `a_24=a_13`. Four coordinates are free, so the
centralizer has order `q^4`; fixed-coset fibres have order `q^4`; and the
image has order `q^6/q^4=q^2<q^3=|gamma_2|`. These equations remain correct
in characteristic two.

## Critical issue

### C1 (direct owner and contribution boundary): Bier 2013 already owns the fixed-`J` surjectivity backbone

[Agnieszka Bier, *On solvability of Engel equations in the group of
triangular matrices over a field*, Linear Algebra and its Applications 438
(2013), 2320–2330](https://doi.org/10.1016/j.laa.2012.10.009) is not in the
bibliography or any owner ledger in the package. The
[author-repository text](https://delibra.bg.polsl.pl/Content/31969/REPO_35897_-_On-Solvability-of-En_0000.pdf)
makes the collision exact:

- Bier uses the same convention `[A,B]=A^(-1)B^(-1)AB`.
- Her Lemma 1 fixes the same
  `B=I+sum_(i=1)^(n-1) E_(i,i+1)=J`.
- Her `UT_n^m` is the subgroup with the first `m` superdiagonals zero,
  namely the present `gamma_(m+1)`. Lemma 1 proves that every
  `C in UT_n^m` is `[A,B]` for some `A in UT_n^(m-1)`. With `k=m`, this is
  exactly `E(gamma_k)=gamma_(k+1)`.
- Her proof of Theorem 1 iterates that same fixed `B` and obtains every
  element of `UT_n^m` as an `m`-Engel value. Thus the full-source iterated
  image statement is direct prior art, and repeated use of Lemma 1 supplies
  every restricted image equality used here.
- Bier works over an arbitrary field of arbitrary characteristic, so the
  present finite-field setting is a specialization, not an escape from the
  owner.

Bier does **not** state the finite-field solution count, left-coset fibre,
depth distribution, filtration-type predecessor census, zeta formula, or
the displayed nonregular `U_4` calculation. Those are the possible residual,
but they are all short consequences or refinements once the owned
surjectivity and classical regular centralizer are installed. The current
introductory residual list, `CLAIMS_EVIDENCE.md`, `NARRATIVE_REPORT.md`,
`PAPER_PLAN.md`, and `README.md` therefore over-credit the paper by treating
the image equality as part of the new conjunction and by omitting the
closest literal owner.

Required repair:

1. Add Bier 2013 to the bibliography and cite Lemma 1 and Theorem 1 at the
   first statement of the one-step and iterated image equalities.
2. State explicitly that `E(gamma_k)=gamma_(k+1)` and the corresponding
   fixed-`J` Engel-image existence are owned results, reproduced only for
   self-containment; give them zero contribution credit in every supporting
   document.
3. Recast Theorem 3.1 as an **exact-fibre refinement of Bier's
   surjectivity**, separating the owned image equality from the finite-field
   cardinality and coset assertions.
4. Recast Proposition 4.1 as a complementary self-contained proof that also
   counts all solutions. Do not present the existence/surjectivity portion
   as a new second derivation without citing Bier's earlier block-inductive
   route.
5. Narrow the residual everywhere to this fixed pair's uniform finite-field
   fibres, exact temporal/layer and typed-indegree census, and explicit
   `U_4` guard. Submit that narrower delta to a fresh specialist owner gate;
   the bounded non-hit for the complete census is not a novelty conclusion.

The strongest hostile objection after this subtraction is contribution
density: every temporal formula is obtained by multiplying or subtracting
uniform fibres, while the image theorem driving those fibres is already in
the literature. The manuscript may remain a useful exact note, but the
present package cannot decide whether that residual clears a publication
threshold.

## Major issues

No mathematical major issue found. In particular, I found no failed
characteristic, endpoint, orientation, or counting case in the theorem
statements as written.

## Minor issues

### m1 (claim ceiling): “complete rooted functional graph” is broader than the stated classification

The conclusion says that the fibre products yield “the complete rooted
functional graph.” The paper explicitly proves depths, layer sizes, global
indegrees, and filtration-stratified predecessor counts. It does not state a
labeled adjacency classification, nor does it formulate the short recursive
argument that the type-dependent child multiplicities determine the typed
tree up to isomorphism.

Required repair: replace this phrase by “the complete
filtration-typed fibre and depth census,” or add a precise typed-tree
isomorphism statement and the recursive proof. Do not let a census sound
like a stronger graph-classification theorem.

### m2 (claim ceiling): the `U_4` example disproves universality, not all nonregular cases

The proposition correctly proves failure for one nonregular element and the
text later says it blocks extension to *arbitrary* unipotent second entries.
The abstract and section title use the shorter phrase “regularity is
essential,” which can be read as saying every nonregular second entry fails;
no such classification is proved.

Required repair: use the precise formulation already present later in the
paper: “the theorem does not extend to arbitrary nonregular (or arbitrary
noncentral unipotent) second entries.” Retain the literal `U_4` proposition
and do not infer necessity for each conjugacy type.

## Boundary, characteristic, and orientation audit

- `n=1`: the separate singleton statement and zeta function are correct.
- `n=2`: the group is abelian, `E` is constant, and the layers are `1,q-1`.
- `k=1`: all full-phase fibre and indegree formulas specialize correctly.
- `k=n-1`: `gamma_(n-1)` maps to `{I}` with one fibre of size `q`.
- `t=0`: the empty exponent sum gives identity iterates and singleton
  fibres.
- `t=n-k`: the exponent equals `log_q |gamma_k|`; the fibre over `I` is the
  whole source. Later times remain constant.
- Characteristic two: subtraction in `Delta_r` becomes addition, but its
  kernel is still the constant vectors; the triangular proof uses no
  division. The `U_4` centralizer equations also retain rank two.
- Multiplication order: `E(X)=Y` is equivalent to `XJ=JXY`, and equal fibres
  are left cosets `C_(gamma_k)(J)X`, not right cosets.

## Exact controls

- Fresh canonical verifier: **PASS**, **1,491,877 assertions**.
- Fresh stdout versus `code/verification_output.txt`: **byte-identical**.
- Covered fields: `F_2,F_3,F_4,F_5,F_8,F_9`.
- Exhaustive lanes: 55,808 regular states, 39 restricted surjections, 112
  iterated-fibre profiles, and 20,514 nonregular-counterexample states.
- Exact artifact: all 43 data rows were rebuilt and byte-checked by the
  verifier.
- Six-page visual inspection: no clipped display, missing glyph, unreadable
  table, or evident layout defect.

These controls are strong falsification evidence for the formulas. They do
not repair the missing owner or certify novelty.

## Mandatory resolution before circulation

1. Cite and exactly subtract Bier 2013, including Lemma 1 and Theorem 1.
2. Reframe the one-step theorem as an exact finite-field fibre refinement of
   the owned fixed-`J` surjectivity.
3. Revalue the paper on the narrow residual after that subtraction; retain
   external status **HOLD** until the owner gate is repeated.
4. Tighten “complete graph” and “regularity is essential” to the precise
   census and counterexample statements actually proved.

