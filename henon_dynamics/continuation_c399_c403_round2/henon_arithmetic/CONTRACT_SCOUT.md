# Hénon arithmetic scout: one retained all-clock contract

Date: 2026-09-05. Repository baseline inspected:
`1667dfc0c24e10a8a3627e80f93e301538d18012`.
This is an unnumbered candidate/proof handoff, not a completed paper or release.
Only this new directory is owned by the scout. No Git operation, old snapshot,
numbered paper, TeX source, registry, or shared state was changed.

## Decision

**Retain one contract for independent proof and admission review:** exact
Frobenius–Hénon intersection counts at every nonresonant pair of clocks,
including their small-Frobenius boundary defect, sharp trace-agreement
threshold, and the distinction between transcendental fixed-time slices and
rational genuine diagonal dynamics.

The increment is not eventual large-Frobenius agreement, étaleness, or the
general possibility of nonuniform trace thresholds. Those have explicit
classical owners below. The proposed increment is the complete,
coefficient-uniform boundary calculation for genuine nonlinear Hénon maps.
No literature-priority guarantee or target-arithmetic promotion is made.

Only two candidate entrances were examined. The other was non-Archimedean
Hénon horseshoe periodic counts, rejected because the available conjugacy
already gives the contemplated all-period count. No third candidate was
opened once the first obtained a complete proof route.

## Contract and assumptions

Let $q=p^e$, $k=\overline{\mathbb F}_q$, and

$$
H(x,y)=(y,f(y)-a x),\qquad
f\in\mathbb F_q[y],\quad \deg f=d\ge2,\quad a\in\mathbb F_q^*.
$$

The domain is $\mathbb A^2(k)$, not a fixed finite field. The map is an
invertible polynomial recurrence, with inverse
$H^{-1}(x,y)=((f(x)-y)/a,x)$. No coefficient other than the leading one and
$a$ is restricted. Define the actual $q^r$-power morphism
$\Phi_r(x,y)=(x^{q^r},y^{q^r})$, and retain two distinct positive-integer
clocks $n$ (Hénon iterate) and $r$ (Frobenius power):

$$
M_H(n,r)=\#\{P\in\mathbb A^2(k):H^n(P)=\Phi_r(P)\}.
$$

This is neither $\#\operatorname{Fix}(H^n)(\mathbb F_{q^r})$ nor the
Frobenius count of one fixed-period zero-dimensional scheme. Its arithmetic
is intrinsic to the coefficients and Frobenius; there is no prime table,
fitted roof, external target spectrum, or substituted Euler product.

**Main theorem.** Put $D=d^n$, $Q=q^r$. For every such map and every pair
$n,r\ge1$ satisfying $D\ne Q$, the intersection is finite and reduced and

$$
\boxed{M_H(n,r)=\max\{Q^2,DQ\}.}
$$

In particular, if $d$ is not a power of $p$, this is an **all-period,
all-Frobenius-power, all-coefficient theorem**: equality $d^n=q^r$ is then
impossible. This family includes all quadratic Hénon maps in every odd
characteristic and all cubic Hénon maps in characteristic two. The primary
contract uses that nonresonant degree family; the pointwise theorem also
applies away from resonance when $d$ is a power of $p$.

The decisive success criterion is a proof of the formula for $D>Q$, not just
the elementary large-$Q$ count. A counterexample to either boundary local
length kills or corrects the contract. A primary-source theorem already
giving this full coefficient-uniform Hénon law would trigger a source-owner
reassessment; the formula is not retained solely because searches returned
no exact title match.

## Proof status and dependency map

**PROVABLE AS STATED**, meaning the argument below closes the stated
nonresonant claim. This is an author-side mathematical status, not independent
review or paper admission.

The proof depends on:

1. An induction on the coordinate degrees of a generalized Hénon iterate.
2. Classical Chow intersection in $\mathbb P^2\times\mathbb P^2$, with
   graph multidegrees computed directly.
3. The Jacobian criterion for the affine intersection.
4. An elementary complete-local-ring length calculation at one infinity
   point and a transverse intersection at the other.

No trace formula, point enumeration, asymptotic estimate, Newton heuristic,
or characteristic-zero Hénon theorem is an input to the exact count.

## Complete proof route

### 1. Projective geometry of every iterate

Write $g=H^n=(g_1,g_2)$. Inductively,
$\deg g_1=d^{n-1}<D=\deg g_2$, and the leading homogeneous part of $g_2$
is $L_n y^D$, with $L_n\ne0$. The induction uses
$g_1^{\rm new}=g_2$ and $g_2^{\rm new}=f(g_2)-a g_1$; the latter summands
have unequal degrees, so no leading cancellation occurs in any
characteristic. Applying the same argument to the inverse shows that
$g^{-1}$ has degree $D$, with leading first coordinate a nonzero multiple of
$x^D$ and lower-degree second coordinate.

In homogeneous coordinates $[x:y:z]$, the rational projective extension of
$g$ has unique indeterminacy point
$I_+=[1:0:0]$, contracts the rest of $L_\infty=\{z=0\}$ to
$I_-=[0:1:0]$, and is regular and fixed at $I_-$. The inverse has the roles
of $I_+$ and $I_-$ exchanged. These statements follow by homogenizing both
coordinates to degree $D$ and using the leading terms just obtained.

Let $\Gamma_g$ be the closure of the affine graph in
$X=\mathbb P^2\times\mathbb P^2$. It is the same closed surface as the
transpose of the graph closure of $g^{-1}$. At every point above a domain
where $g$ is regular it is its ordinary graph; the analogous statement
holds over the second factor where $g^{-1}$ is regular.

### 2. The total projective intersection

Let $h_1,h_2$ be the two hyperplane classes. The Chow ring is
$\mathbb Z[h_1,h_2]/(h_1^3,h_2^3)$, normalized by
$\deg(h_1^2h_2^2)=1$. The graph coefficients are obtained by intersecting
with two generic hyperplanes on one factor, or one on each factor:

$$
[\Gamma_g]=h_1^2+D h_1h_2+h_2^2,
\qquad
[\Gamma_{\Phi_r}]=Q^2h_1^2+Qh_1h_2+h_2^2.
$$

For $g$, the end coefficients are one because both projections are
birational; the middle coefficient is $D$ because the inverse image of a
generic line has degree $D$. For $\Phi_r$, the three coefficients are its
topological degree $Q^2$, line degree $Q$, and one. Consequently, once
properness of this intersection has been checked locally below, its total
intersection number is

$$
\deg([\Gamma_g]\,[\Gamma_{\Phi_r}])=1+DQ+Q^2.
$$

This graph calculation is necessary: blindly applying affine Bézout to
the largest degrees would not account for the infinity contribution.

### 3. Affine points and the only possible boundary points

The affine equations are $g_1-x^Q=g_2-y^Q=0$. Their Jacobian is $Dg$,
because the derivatives of $x^Q,y^Q$ vanish. Its determinant is $a^n\ne0$.
Thus this finite-type intersection is zero-dimensional and smooth over
$k$, hence finite and reduced; each affine local intersection number is
one. This does not yet compute how many affine points there are.

On $\Gamma_{\Phi_r}$, an infinity point has the form
$(P,\Phi_r(P))$ with $P\in L_\infty$. If $P\ne I_+$, the graph of $g$
forces the second coordinate to be $I_-$, and the coordinatewise power map
has only $P=I_-$ above $I_-$. If $P=I_+$, then $\Phi_r(P)=I_+$.
Therefore the only possible boundary intersections are

$$
(I_-,I_-),\qquad (I_+,I_+).
$$

Both belong to $\Gamma_g$: at the first use $g(I_-)=I_-$, and at the
second use $g^{-1}(I_+)=I_+$.

### 4. The attracting infinity point has length $Q\min(D,Q)$

Use the source/target chart $y\ne0$ centered at $I_-$, with
$u=x/y$, $v=z/y$. There are polynomials $A(u,v),C(u,v)$ such that locally

$$
g(u,v)=\left(\frac{A(u,v)}{C(u,v)},
                   \frac{v^D}{C(u,v)}\right),
\qquad C(0,0)=L_n\ne0,\qquad A(u,0)=0.
$$

In fact $C(u,0)=L_n$ by the pure leading term, but only its invertibility
is needed. Frobenius is $(u,v)\mapsto(u^Q,v^Q)$ in this chart. Since
$\Gamma_g$ is a smooth graph here, the local intersection is the quotient
of $k[[u,v]]$ by

$$
B=A-u^Q C,\qquad v^D-v^Q C.
$$

If $D>Q$, the second equation is $v^Q$ times the unit
$v^{D-Q}-C$. If $D<Q$, it is $v^D$ times the unit
$1-v^{Q-D}C$. Thus, with $m=\min(D,Q)$, the ideal is $(B,v^m)$.

Here $B(u,0)=-u^Q C(u,0)$ has exact order $Q$ in $u$. Put
$R=k[[u,v]]/(B)$. Multiplication by $v$ is injective on $R$: if
$v h=B k_0$, reduction modulo $v$ in the domain $k[[u]]$ shows that
$k_0$ is divisible by $v$, after which cancellation in $k[[u,v]]$ shows
$h\in(B)$. It follows that each successive quotient
$v^iR/v^{i+1}R$ is isomorphic to $R/vR$, whose $k$-length is $Q$.
The $m$-step filtration therefore gives

$$
\operatorname{length}_k R/v^mR=mQ=Q\min(D,Q).
$$

This calculation neither assumes separable coordinate polynomials nor uses
a characteristic-zero analytic preparation theorem.

### 5. The other infinity point has length one

Near $(I_+,I_+)$, parameterize $\Gamma_g$ by the second coordinate $Y$
as $(g^{-1}(Y),Y)$, since $g^{-1}$ is regular at $I_+$. The graph
intersection equation is

$$
Y=\Phi_r(g^{-1}(Y)).
$$

The right side has zero differential in characteristic $p$. In local
coordinates centered at $I_+$, the two defining equations consequently
have identity linear part. They generate the maximal ideal of the completed
local ring, so this intersection is transverse and has length one.

### 6. Subtract the boundary

All affine and boundary intersections are isolated, so the projective
intersection is proper. Both graph surfaces are smooth at the intersection
points just examined; the computed local complete-intersection lengths
are their intersection multiplicities. Subtracting the two boundary terms
from the total yields

$$
M_H(n,r)=1+DQ+Q^2-1-Q\min(D,Q)
        =\max(DQ,Q^2).
$$

This proves the main theorem for every quantified coefficient and every
nonresonant pair of clocks. $\square$

## Consequences that belong to this same contract

Assume throughout this section that $d$ is not a power of $p$.

### A. Exact sharp threshold, not a new general trace principle

For fixed $n$, define

$$
R_n=\left\lfloor\log_q(d^n)\right\rfloor.
$$

Then $M_H(n,r)=q^{2r}$ exactly when $r\ge R_n+1$, and is strictly
larger for $1\le r\le R_n$. On compactly supported étale cohomology of
$\mathbb A^2$, only $H_c^4\simeq\mathbb Q_\ell(-2)$ is nonzero;
the polynomial automorphism acts as one and $\Phi_r$ as $q^{2r}$.
Thus the first and eventual trace-agreement threshold for $H^{-n}$ is
exactly $R_n+1$. It grows with slope $\log_q d$ in Hénon time.
The general existence and nonuniformity of such thresholds are classical;
the asserted Hénon-specific contribution is this exact threshold and the
full defect below it.

### B. Fixed-time Frobenius slices are often transcendental

Define the *slice generating function*, not the zeta of a fixed variety, by

$$
\mathcal Z_{H,n}(t)=\exp\left(\sum_{r\ge1}M_H(n,r)\frac{t^r}{r}\right).
$$

The exact count gives

$$
\mathcal Z_{H,n}(t)=\frac{\exp(P_n(t))}{1-q^2t},\qquad
P_n(t)=\sum_{r=1}^{R_n}(d^nq^r-q^{2r})\frac{t^r}{r}.
$$

If $d^n<q$, the polynomial is zero and the slice is rational. If $d^n>q$,
$P_n$ is nonconstant, so the slice is transcendental over $\mathbb C(t)$.
Indeed $\exp(P_n)$ has an essential singularity at infinity (or exponential
growth along a ray with positive leading real part), whereas an algebraic
function has only finite-order Puiseux growth there. Multiplying by the
nonzero rational factor does not change transcendence.

This does not contradict Dwork rationality: the equations defining the
count change with $r$, and this is not $\#X(\mathbb F_{q^r})$ for a single
finite-type variety $X$.

### C. No all-$r$ finite-dimensional invertible-Frobenius trace for a defect slice

If $d^n>q$, there cannot exist a finite collection of finite-dimensional
characteristic-zero spaces and matrices $F_i,A_i$, with each $F_i$
invertible, such that

$$
M_H(n,r)=\sum_i\epsilon_i\operatorname{Tr}(F_i^r A_i)
\quad\text{for every }r\ge1,\qquad \epsilon_i\in\{1,-1\}.
$$

No commutation assumption on $F_i,A_i$ is needed. By Cayley–Hamilton, the
difference between the right side and $q^{2r}$ satisfies a linear
recurrence whose constant coefficient is nonzero. If this sequence is
zero for every sufficiently large $r$, the recurrence can be solved
backwards to show that it is zero for every $r\ge1$. The positive defect
at $r=1$ is a contradiction. The exclusion is finite-dimensional and
all-clock; it says nothing about infinite-dimensional realizations or
boundary-corrected correspondences.

### D. Genuine diagonal dynamics has a rational zeta

For any fixed positive integers $k_0,s_0$, the polynomial map
$S=H^{-k_0}\circ\Phi_{s_0}$ is a genuine single dynamical system on
$\mathbb A^2(k)$. Since $H$ and Frobenius commute,

$$
\#\operatorname{Fix}(S^m)=M_H(k_0m,s_0m)
 =\Lambda^m,\qquad
\Lambda=\max(q^{2s_0},q^{s_0}d^{k_0}),
$$

for every $m\ge1$. Its Artin–Mazur zeta is consequently
$\zeta_S(t)=(1-\Lambda t)^{-1}$. This is not a target Euler factor, and
it must not be confused with the fixed-$n$ slice above or with the
cohomological determinant $(1-q^{2s_0}t)^{-1}$. In the regime
$d^{k_0}>q^{s_0}$ those two single-map determinants differ. This is a
precise boundary-at-infinity effect, not a failure of the properly stated
eventual trace theorem.

## Resonance is a real excluded case

The proof uses $D\ne Q$ exactly when replacing
$v^D-v^Q C$ by a pure power times a unit. At $D=Q$ this becomes
$v^Q(1-C)$ and the unit need not exist.

An actual nonlinear control is

$$
p=q=d=3,\quad f(y)=y^3+y^2,\quad a=1,\quad n=r=1.
$$

The equations give $y=x^3$ and
$x^9+x^6-x=x^9$, leaving $x^6-x=0$. Its derivative is $-1$ in
characteristic three, so there are **six** distinct geometric solutions,
not the naive value nine. This is not merely an additive/group example.
Full resonant classification is outside the retained contract, not an
unproved clause hidden in “all parameters.”

## Primary sources and ownership boundary

This is a bounded primary-source scan on 2026-09-05, not a systematic
literature review or a proof of global novelty. Browsing was used in the
normal citation-discovery route; no resolver API or external model was
called, and no human-read attestation is asserted. Source excerpts were
read through web HTML/abstract views, not acquired as local source PDFs.

| Source | Access and status | Ownership relevant to this contract |
|---|---|---|
| K. V. Shuddhodan, *Constraints on the cohomological correspondence associated to a self map*, Compositio Mathematica 155 (2019), 1047–1056, DOI [10.1112/S0010437X19007188](https://doi.org/10.1112/S0010437X19007188) | Publisher metadata and [author v2 HTML](https://arxiv.org/html/1803.06461), §2, Example 3.6 and Remark 3.7 inspected. Published research article. | Lemma 2.6 gives twisted étaleness; Proposition 2.10 gives eventual trace agreement; Definition 2.12/Lemma 2.14 concern a cohomological zeta. Example 3.6 treats a torus and Remark 3.7 discusses nonuniform thresholds. Those mechanisms and motivations are not new here. The inspected text does not supply the Hénon boundary calculation above. |
| Y. Varshavsky, *Lefschetz–Verdier trace formula and a generalization of a theorem of Fujiwara*, Geometric and Functional Analysis 17 (2007), 271–319 | [Author manuscript](https://arxiv.org/html/math/0505564), especially introduction and contracting-correspondence explanation; [arXiv metadata](https://arxiv.org/abs/math/0505564). | Explicitly owns the general sufficiently-high-Frobenius trace theorem and contracting-boundary method, credits Pink/Fujiwara. Our elementary exact boundary multiplicity is a special-family calculation, not a replacement or new proof of the general theorem. |
| K. Fujiwara, *Rigid geometry, Lefschetz–Verdier trace formula and Deligne’s conjecture*, Inventiones Mathematicae 127 (1997), 489–533 | Original DOI retrieval [10.1007/s002220050129](https://doi.org/10.1007/s002220050129) failed during this scan. Attribution and precise result are confirmed in the two accessed primary papers above. No claim of full-text inspection. | Original classical owner of eventual nonproper trace agreement. The present proof does not invoke his theorem to compute the count. |
| K. Allen, D. DeMark, C. Petsche, *Non-Archimedean Hénon maps, attractors, and horseshoes* | [Author abstract/metadata](https://arxiv.org/abs/1610.04271), submitted 2016, accessed; source proof not audited. | The abstract states a two-sided two-symbol full-shift conjugacy in a parameter region. The prospective local-field horseshoe fixed counts then follow immediately and were not retained as a second paper. |
| The Stacks Project, intersection-theory framework | [Gysin maps for local complete intersections](https://stacks.math.columbia.edu/tag/0FEZ), accessed as primary reference-project documentation. | Classical intersection products, not a Hénon-specific result. The graph multidegrees and every local length used here are computed in the proof. |

For mathematical evidence, published theorem/proof sources are the relevant
standard; the biomedical seven-level design ladder is inapplicable. No
venue-quartile or calibrated score is invented. Publisher/source identity is
confirmed where stated; comprehensive predatory-venue, author-conflict, and
retraction audits were not performed and are not claimed. The corpus is
intentionally concentrated in foundational theoretical work; no artificial
recent-source quota was used to broaden this bounded task.

Search strings included `Hénon Frobenius twisted fixed points finite fields`,
`polynomial automorphism Frobenius graph intersection`, `Hénon finite fields
dynamical zeta`, `Fujiwara trace formula Frobenius correspondence large
powers`, and exact-title searches for Shuddhodan and Varshavsky. Accented and
unaccented Hénon forms and exclusions of Perron–Frobenius/Koopman noise were
tried. Many Hénon/Frobenius hits were unrelated transfer-operator pages and
were excluded. The non-Archimedean entrance used `Hénon maps non archimedean
horseshoe periodic points zeta`.

The local `papers/` filename scan found no directly relevant source PDF;
`literature/` is absent. No Zotero or Obsidian tools were available. The
research-lit arXiv source step used browser metadata rather than launching
a programmatic resolver, following the ARS ordinary-discovery override.

## Repository collisions actually checked

- [C12A fixed-period Frobenius obstruction](../../henon_frobenius_scheme_obstruction/README.md):
  its object is $\#\operatorname{Fix}(H^n)(\mathbb F_{q^r})$, a finite
  permutation representation for fixed $n$. The present equalizer
  $H^n=\Phi_r$ is a different two-clock object with growing degree as $r$
  varies. The definition must remain explicit to avoid relabelling C12A.
- [C32 source bibliography](../../phase2_hcs_c32_artin_schreier_quantum_trace/SOURCE_CORPUS_AND_ANNOTATED_BIBLIOGRAPHY.md):
  Varshavsky already occurs as background. That quantum Artin–Schreier trace
  lane is not the present geometric equalizer count.
- [First scout](../../SCOUT_C399_C403.md) and
  [prior arithmetic closeout](../../research_c399_c403/arithmetic_scout/CONTINUATION_CLOSEOUT.md):
  generic group endomorphisms, matrix polynomial counts and Hessian/Lattès
  dynamics remain rejected; no attempt was made to revive them.
- [Earlier source audit](../../next_paper_henon_candidate_search/SOURCE_AUDIT.md):
  Allen–DeMark–Petsche is already recorded; horseshoe counting is not fresh.
- Targeted `rg` searches of Hénon Markdown/TeX for twisted Frobenius graphs,
  Fujiwara/Pink, Shuddhodan, small/large Frobenius and nonuniform traces
  found the above background but no existing package claiming this exact
  max-law. Wider Shuddhodan/exact-title searches in `flow_systems` and
  `symbolic_dynamics` also returned no matching owner. This search-bounded
  absence is not a uniqueness or novelty certificate.

## Bounded executable evidence

`bounded_check.py` computes quotient dimensions from Gröbner standard
monomials over prime fields. It does not enumerate a chosen extension field
and does not infer the all-period theorem from a finite census. The polynomial
equations and Jacobian are constructed directly, independently of the
projective boundary proof.

The saved source specifies a complete 36-parameter
quadratic family over $\mathbb F_3$ at $(n,r)=(2,1)$, eleven additional
cases covering both sides of the threshold, higher iterates, characteristic
two and nonprime base fields with prime-subfield coefficients, and the
nonlinear resonant negative control above. Execution completed with exit
status zero: all **47 nonresonant exact checks passed**, and the negative
control returned six rather than nine. The environment and complete rows
are recorded in `bounded_results.json`; that file is authoritative for
the observed tests. These tests do not establish the quantified theorem.

Earlier disposable exploratory commands also computed several exact
dimensions and were not saved as proof evidence. One degree-256 Gröbner
calculation was manually interrupted after the useful lower-degree output;
it is not a completed check. The saved bounded script avoids that case.

Reproduction from the repository root:

```bash
python henon_dynamics/continuation_c399_c403_round2/henon_arithmetic/bounded_check.py
```

## Handoff, limitations, and scientific scope

This scout recommends **one** independent review of the actual projective
proof, particularly the graph-class pairing and the two local graph charts,
plus an admission judgment about whether the exact small-twist law is a
substantial enough Hénon increment over the identified general sources.
No formal Route-A evaluation is claimed or evaluator artifact modified.
The pinned evaluator remains v0.2.0; `NO_BAD_EULER_OR_ROOT_NUMBER` is intact.

The theorem supplies intrinsic source arithmetic and an exact source-side
obstruction. It establishes no target Euler factors, automorphy, functional
equation, root numbers, Riemann-zero correspondence, or Hilbert–Pólya
operator. Degree-only universality may itself limit discriminatory power.
Resonant equal-degree coefficients, ordinary Hénon periodic-point zeta,
full exact-period Galois groups, and higher-dimensional regular automorphisms
are explicitly outside this contract.

The repository batch skill determined the substantive-contract and collision
gates. Research-lit and ARS supplied bounded primary-source provenance
discipline; proof-writer required an explicit theorem, proof dependencies,
and the resonant failure control. Their broad-review quotas and older
external-model examples did not enlarge the assigned bounded scan. All
research and proof text here is AI-assisted current-team work; it is not
human or external peer review.
