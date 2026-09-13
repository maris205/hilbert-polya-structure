# Publication-Stage Scope

## Authority and present lifecycle

This document governs the transition from the frozen mathematical source
package and independently passed paper plan to a possible anonymous,
proof-first article. It is a governance artifact, not a manuscript,
bibliography, build, manuscript review, revision, finalization, release, or
submission authorization.

The current state is exactly:

**PUBLICATION_STAGE_LOCKED / PENDING_INDEPENDENT_PUBLICATION_REVIEW / NO_DRAFT / NO_BUILD / NO_RELEASE**

The exact public title is:

**Support Size and Finite-Rank Torus Escape for Generalized Hénon Maps**

The one-sentence contribution is:

> We prove that, for generalized Hénon maps with a nonzero constant term,
> increasing the actual nonconstant support from one monomial to at least two
> lowers the sharp coefficient-uniform finite-rank torus-survival threshold
> from four transitions to two, with explicit cardinality bounds and matching
> shorter-window rank-one families.

The governance freeze date is 2026-08-17 UTC. The present authority consists
of this scope together with `experiments/publication_lock.json`. Earlier
source-design, source-lock, and paper-plan statuses are bound provenance; none
of them independently authorizes a downstream artifact.

## Frozen-input gate

Before either governance artifact was written, the publication-stage author
read and rehashed all fifteen existing project files. Every path, byte count,
LF-line count, and SHA-256 identity matched the stable pre-governance
snapshot.

| Frozen input | Bytes | LF lines | SHA-256 |
|---|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 5,824 | 129 | `f50a42f9dde61f00801c4696447c6b161a496cdfb7047b468041917225ba65f6` |
| `experiments/EXPERIMENT_TRACKER.md` | 1,971 | 48 | `4578dd2cfbedb25cd2a327ba6d865535bf3d007951f9b749032f9bd6d633b83d` |
| `experiments/source_lock.json` | 31,945 | 1 | `86205b1f4dc12ab71302e9b283021c8085afc16f0cf6b479d9a91738c03041fd` |
| `notes/CITATION_VERIFICATION.md` | 10,733 | 205 | `6ec31651060c148d3110856d8709206f60c36ea990b6c433fa9ab0e0944bab24` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 7,659 | 59 | `bc5541dcebce9b2cb8cb7e180a91097d55f0d6b0fdc74fb5b4be7f432e462311` |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | 9,989 | 211 | `d7493502cf05fb489f5dfe88ce48c6b93c549316bc62f95e617aedb255c399d3` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 13,903 | 360 | `046e2ec16b46e8de903eac950c1df922725c5b16e359f5ed6c45bd28e737dd61` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 14,929 | 298 | `f1c55a810008ef920cd421c4578a98c1d91f8feb800d478e285d2807602cd72c` |
| `notes/NOVELTY_ASSESSMENT.md` | 7,309 | 117 | `83c9ab497211c7b5cd5d11b7061a292aba4fb258976a01ec8b9216b11226b96b` |
| `notes/PROOF_PACKAGE.md` | 16,808 | 704 | `b44c1f164c97fb5d383cbef941fdef88be4e702066e40efcfb18543be0c4bdf8` |
| `notes/RESEARCH_QUESTION.md` | 8,319 | 318 | `43b7f965dc04db33c1f00e45880466730d7ee2a25d84f117e91cace71b26a928` |
| `paper/PAPER_PLAN.md` | 34,681 | 880 | `875d26506ba552c79fe62fe11ac1a70e73e1a00245e8bb1aacc1b5c58753d336` |
| `refine-logs/FINAL_PROPOSAL.md` | 5,387 | 155 | `220bb54312f80f17b6b99a37afffa902fd04a6b696c0c3e1f60f4ed8d374b540` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4,253 | 98 | `329c7a6687612ff806508640f7add09201ac9ddedd41c10fabd9582a4beab8b2` |
| `refine-logs/REVIEW_SUMMARY.md` | 5,479 | 95 | `20256b3f6915781c07dadb6beec26fa69529c5c7d0660b0171c14d460656c55a` |

The source-lock review ends with the exact verdict `SOURCE_LOCK_PASS`. The
paper-plan review ends with the exact verdict `PAPER_PLAN_PASS`. Those
verdicts establish provenance and eligibility only.

## Current authorization state

At governance freeze, every downstream authorization is false.

| Authorization | Current value |
|---|---|
| anonymous manuscript drafting | false |
| bibliography authoring | false |
| source-level manuscript review | false |
| build or compilation | false |
| code, CAS, or scientific execution | false |
| experiment, data, or result generation | false |
| figure or external asset generation | false |
| manuscript Round-1 or Round-2 review | false |
| source revision | false |
| finalization or `paper/main.pdf` | false |
| identity disclosure | false |
| submission or upload | false |
| public release or external messaging | false |

The independent publication-stage review defined below is the sole permitted
next project write. Freezing this governance pair is not permission to draft,
build, review a manuscript, revise source, or communicate externally.

## Exact mathematical setup and constants

The article must use the generalized Hénon normal form

\[
1\le e_1<\cdots<e_s=d,
\qquad
P(X)=c+\sum_{j=1}^s b_jX^{e_j},
\]

\[
H(x,y)=(P(x)+ay,x),
\qquad
a,c,b_1,\ldots,b_s\in K^*,
\]

where \(K\) has characteristic zero and \(\Gamma\le K^*\) has finite rank
\(r\). Finite generation is not assumed. The integer \(s\) is the actual
collected positive-degree support after equal exponents are combined and zero
coefficients are deleted. The inverse is

\[
H^{-1}(X,Y)=\left(Y,\frac{X-P(Y)}a\right).
\]

For \(m\ge0\), the convention is exactly

\[
T_m(H,\Gamma)=
\{Q\in\Gamma^2:H^j(Q)\in\Gamma^2\text{ for }0\le j\le m\}.
\]

Thus \(T_m\) records \(m\) transitions and \(m+1\) states.

For \(q\ge2\) and \(R\ge0\), set

\[
\mathcal A(q,R)=(8q)^{4q^4(q+R+1)}.
\]

For \(2\le q\le s+1\), set

\[
\mathcal S_q(d,r)
=d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr),
\qquad
\mathcal S_*=\max_{2\le q\le s+1}\mathcal S_q(d,r).
\]

For nonempty \(J\subseteq[s]\), use \(e_{\max J}\) and \(e_{\min J}\)
for the largest and smallest selected exponents. The component budget is
defined, and must be defined, by the two explicit subset sums

\[
\boxed{
\begin{aligned}
\mathcal M(\mathbf e)
={}&2(2^s-1)\\
&+\sum_{\substack{J\subseteq[s]\\|J|\ge2}}
(e_{\max J}-e_{\min J})
+\sum_{\varnothing\ne J\subseteq[s]}e_{\max J}.
\end{aligned}}
\]

The identities

\[
\mathcal M(\mathbf e)
=2^{s+1}-2+\sum_{k=1}^s(2^k-2^{s-k})e_k
\]

and

\[
\mathcal M(\mathbf e)
\le2(2^s-1)+d(2^{s+1}-s-2)
\]

are checksums only. Neither replaces the subset-sum definition.

## Exact theorem package and contribution hierarchy

The article presents one support-size phase transition, with PC1 dominant,
PC2 as its matching sharpness result, and PC3 as a fully reproduced but
subordinate support-one comparison.

### PC1: dominant support-at-least-two theorem

If \(s\ge2\), then

\[
\boxed{
\#T_2(H,\Gamma)
\le d\mathcal A(s+2,3r)+\mathcal M(\mathbf e)\mathcal S_*.
}
\]

The statement is coefficient-uniform under the displayed nonvanishing
hypotheses. It neither assumes that a coefficient belongs to \(\Gamma\) nor
assumes finite generation.

### PC2: exact one-transition obstruction

For every prescribed support \(1\le e_1<\cdots<e_s\) with \(s\ge2\), take

\[
K=\mathbb Q,
\qquad a=b_1=\cdots=b_s=1,
\qquad c=-s,
\qquad \Gamma=\langle2\rangle.
\]

Then \(P(1)=0\), and

\[
(1,2^n)\longmapsto(2^n,1)
\qquad(n\ge0).
\]

Hence \(T_1\) is infinite in rank one for every prescribed actual support,
so the PC1 threshold is exactly two transitions. A rank-zero roots-of-unity
variant may be mentioned only as a secondary observation; it cannot replace
this rational rank-one headline.

### PC3: fully reproduced support-one comparison

For \(P(X)=c+bX^d\), with \(d\ge2\) and \(a,b,c\ne0\),

\[
\boxed{
\#T_4(H,\Gamma)
\le4d\mathcal A(3,3r)+81d^2.
}
\]

For every \(d\ge2\), choose \(c^{d-1}=-1\), \(b=1\), \(a=-1\),
\(K=\mathbb Q(c)\), and \(\Gamma=\langle2,c,-1\rangle\). This group has
rank one because \(c\) and \(-1\) are torsion. For \(t=2^n\) and
\(Q_t=(t,t^d)\), the scalar recurrence segment in the order
\(x_{-1},x_0,x_1,x_2,x_3\) is

\[
t^d, t, c, -t, (-t)^d.
\]

Thus \(T_3\) is infinite, and the support-one threshold is exactly four
transitions.

The exact conceptual synthesis is

\[
\begin{array}{c|c|c}
\text{actual nonconstant support}
&\text{uniformly finite window}
&\text{sharp shorter failure}\\ \hline
s=1&T_4&T_3\text{ can be infinite},\\
s\ge2&T_2&T_1\text{ can be infinite}.
\end{array}
\]

## Sole proof input and mandatory field bridge

Amoroso--Viada, Theorem 6.2, is the sole external theorem used in a proof.
It bounds nondegenerate solutions of a \(q\)-term linear equation in a
rank-\(R\) subgroup by \(\mathcal A(q,R)\), but its published statement is
over an algebraically closed characteristic-zero field.

For an arbitrary characteristic-zero field \(K\), the article must choose an
algebraic closure \(\overline K\), include \(K^*\) and \(\Gamma\) into
\(\overline K^*\), and then apply the theorem there. The inclusion preserves
the abstract rank of \(\Gamma\); all tuple groups used are homomorphic images
of \(\Gamma^2\) or \(\Gamma^3\), so their ranks are at most \(2r\) or
\(3r\). Every solution over \(K\) injects into the solution set over
\(\overline K\). This bounds the original set without a descent claim or an
equality claim between the two solution sets. Fixed coefficients remain
coefficients of the linear equation and are never adjoined to the variable
group.

## Proof-visibility lock

No essential proof may be replaced by a sketch, declared routine, or hidden
in an appendix. Appendices A--C are redundant audits: deleting all three must
leave every theorem and counterexample fully proved.

### Sparse-image lemma

For a degree-at-most-\(d\) polynomial

\[
F(X)=\sum_{\ell=1}^q f_\ell X^{m_\ell}
\]

with exactly \(q\ge2\) nonzero terms, distinct exponents, and
\(\lambda\in K^*\), the article must prove

\[
\#\{(t,u)\in\Gamma^2:\lambda u=F(t)\}
\le d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr).
\]

The normalized tuple is a homomorphic image of \(\Gamma^2\), hence has rank
at most \(2r\). Amoroso--Viada counts nondegenerate tuples, and a ratio of
two coordinates leaves a power fiber of size at most \(d\). Degenerate
solutions are unioned over all nonempty proper zero subsets of sizes
\(2,\ldots,q-1\), exactly \(2^q-q-2\) candidates; each selected subsum is a
nonzero polynomial of degree at most \(d\), hence has at most \(d\) roots.
The proof must audit arbitrary torsion, including infinite torsion: the
external bound is rank-based, and all remaining fibers are ordinary
polynomial root fibers.

### PC1 local rank and four exhaustive incidence types

Write

\[
Q=(v,u),\qquad H(Q)=(z,v),\qquad H^2(Q)=(w,z),
\]

and normalize the first recurrence with the fixed convention

\[
Z=z/c,
\qquad U=-au/c,
\qquad M_j=-b_jv^{e_j}/c,
\]

so that \(Z+U+\sum_jM_j=1\). The variable tuple is an image of
\(\Gamma^3\), of rank at most \(3r\); the nondegenerate contribution is at
most \(d\mathcal A(s+2,3r)\).

For \(B_J(X)=\sum_{j\in J}b_jX^{e_j}\), every chosen nonempty proper zero
subsum is covered by exactly one of the following membership types, without
claiming that different labels are disjoint.

| Type | Membership of the chosen zero subsum | Exact equations | Allowed labels and budget |
|---|---|---|---|
| GZ | \(Z\) in, \(U\) out | \(z=B_J(v)\), \(-au=c+B_{J^c}(v)\) | \(\varnothing\ne J\subseteq[s]\); one sparse-image budget per label |
| GU | \(Z\) out, \(U\) in | \(au=-B_J(v)\), \(z=c+B_{J^c}(v)\) | \(\varnothing\ne J\subseteq[s]\); one sparse-image budget per label |
| R0 | neither \(Z\) nor \(U\) in | \(B_J(v)=0\) | \(|J|\ge2\); at most \(e_{\max J}-e_{\min J}\) roots |
| R1 | both \(Z\) and \(U\) in; \(J\) is the nonempty complementary monomial set | \(c+B_J(v)=0\) | \(\varnothing\ne J\subseteq[s]\); at most \(e_{\max J}\) roots |

The graph proof must handle \(J=[s]\) and \(|J|=1\) explicitly. In each
endpoint, one side still has at least two terms because \(s\ge2\). It must
state that outputs may lie in a fixed coefficient coset while variables
remain in \(\Gamma\); no coefficient-membership hypothesis is introduced.

For either root type, fixing \(v=\rho\) leaves

\[
w=(c+a\rho)+\sum_{j=1}^s b_jz^{e_j}.
\]

If \(c+a\rho\ne0\), this has \(s+1\) terms. If the constant cancels, it
still has exactly \(s\ge2\) nonzero terms. The sparse-image lemma closes the
vertical fiber, and the first recurrence uniquely recovers \(u\). If several
proper subsums vanish, any available label may be selected and the union over
all labels intentionally overcounts. These arguments must yield the two
defining subset sums for \(\mathcal M(\mathbf e)\), followed by both checksum
proofs.

### PC2 and essential-boundary calculations

The PC2 substitution must appear as a direct proof. The article must also
verify the two exact failures:

\[
c=0,\qquad P(X)=X^d+X,\qquad a=-1:\qquad
(t,t^d)\longmapsto(t,t)\longmapsto(t^d,t),
\]

and

\[
a=0,\qquad P(X)=-1+X+X^2:\qquad
(1,t)\longmapsto(1,1)\longmapsto(1,1).
\]

They show that \(c\ne0\) and \(a\ne0\) are essential, rather than optional
normalizations.

### Complete support-one proof

For the scalar recurrence

\[
x_{i+1}=bx_i^d+ax_{i-1}+c,
\]

the article must derive the three local labels

\[
\begin{array}{lll}
A_i:&x_{i-1}=-c/a,&x_{i+1}=bx_i^d,\\
B_i:&bx_i^d=-c,&x_{i+1}=ax_{i-1},\\
C_i:&bx_i^d=-ax_{i-1},&x_{i+1}=c.
\end{array}
\]

It must display and derive the complete nine-word adjacent transition ledger
for \(AA,AB,AC,BA,BB,BC,CA,CB,CC\). Only \(BA\) and \(CB\) may remain free
after two labels. Every third label closes \(BA\). For \(CB\), only \(CBA\)
may remain free, and only under

\[
a=-1,
\qquad bc^{d-1}=-1.
\]

Every fourth label closes that branch with a nonzero equation of degree at
most \(d^2\). The word union is exactly \(3^4d^2=81d^2\), with simultaneous
labels safely overcounted. Together with the four possible nondegenerate
local indices, this proves the PC3 bound. The rank-one sharpness chain must
then be checked in its exact scalar order.

## Article structure, page, and style lock

The future manuscript is a standard, self-contained, anonymous pure-
mathematics `article`, not a venue template or an ML-conference paper. It has
exactly eight numbered main sections in this order:

1. **Introduction and main results**;
2. **Arithmetic-dynamical context**;
3. **Setup and quantitative unit equations**;
4. **Sparse polynomial images in finite-rank tori**;
5. **Two-transition finiteness for support \(s\ge2\)**;
6. **Sharpness and essential hypotheses**;
7. **The complete support-one comparison**;
8. **Phase transition, limitations, and conclusion**.

These are followed by Appendices A--C, in order, and then the final
References. The appendices are:

- Appendix A: **Rank and power-fiber audit**;
- Appendix B: **PC1 subset and component ledger**;
- Appendix C: **Support-one continuation ledger**.

The exact public order is therefore: abstract; Sections 1--8; Appendices
A--C; References. A forced page break must precede the final References so
that the mathematical-content boundary is auditable. References may not
precede or interrupt the appendices.

The mathematical-content count begins on the first PDF page, includes the
abstract, all eight sections, and all three appendices, and ends at the end of
Appendix C. It must be 24--26 nonempty pages inclusive. References are
excluded. The target allocation is 25.0 pages: 22.0 from the abstract through
Section 8 and 3.0 across Appendices A--C. No total-page cap may force proof
omission.

The abstract must contain 180--220 words. It states PC1 first, gives its exact
bound, identifies vanishing proper subsums as the obstacle, summarizes the
graph/root-fiber mechanism, and closes with PC2 and the support-one contrast.
It contains no citation, provenance, publication history, priority language,
or excluded generalization.

The prose follows a result-first, proof-first mathematical style. Definitions
precede use; every hypothesis travels with its theorem; claims and evidence
are separated; no generic filler, fake quotation, unsupported superlative,
sentence-fragment outline prose, or computational-evidence rhetoric is
allowed. PC1 receives the first theorem display and largest proof allocation.
PC3 is visibly subordinate.

## Figure, asset, and proof-table lock

The article has exactly zero figures, figure environments, image files,
included graphics, raster or vector assets, external assets, diagrams,
experiments, datasets, scans, empirical results, or empirical tables. No
figure-generation phase is authorized or needed.

Exactly four main-text proof tables are required, and no other table
environment is permitted:

| Table | Location | Locked mathematical content |
|---|---|---|
| 1 | Section 5.3 | GZ/GU/R0/R1 membership, equations, \(J\)-convention, and budget |
| 2 | Section 7.4 | all nine adjacent A/B/C words |
| 3 | Section 7.5 | BAA/BAB/BAC equations and bounds |
| 4 | Section 7.6 | CBB/CBC/CBA and CBAA/CBAB/CBAC continuations |

These four tables carry proof algebra. The surrounding text must derive every
row; a table never replaces a proof. There is no literature scorecard,
decorative comparison table, or evidentiary visual.

## Citation and bibliography lock

The bibliography contains exactly seven verified primary entries, all of
which must be cited in the article. No uncited entry, wildcard `\nocite`,
duplicate key, missing entry, secondary summary, or bibliography entry for the
non-public support-one predecessor is permitted.

1. Francesco Amoroso and Evelina Viada, *Small points on subvarieties of a
   torus*, Duke Mathematical Journal 150(3), 407--442 (2009). Theorem 6.2 is
   the sole external proof input.
2. Jan-Hendrik Evertse, Hans Peter Schlickewei, and Wolfgang M. Schmidt,
   *Linear equations in variables which lie in a multiplicative group*,
   Annals of Mathematics 155(3), 807--836 (2002). Historical predecessor
   only.
3. Holly Krieger, Aaron Levin, Zachary Scherr, Thomas J. Tucker, Yu Yasufuku,
   and Michael E. Zieve, *Uniform Boundedness of S-Units in Arithmetic
   Dynamics*, Pacific Journal of Mathematics 274(1), 97--106 (2015).
4. Jason P. Bell and Dragos Ghioca, *Intersections of orbits of self-maps with
   subgroups in semiabelian varieties*, Bulletin of the London Mathematical
   Society 56, 783--795 (2024).
5. Zhuchao Ji, Junyi Xie, and Geng-Rui Zhang, *Cyclotomic integral points for
   affine dynamics*, arXiv:2511.13443, v2 dated 2026-01-20.
6. Jorge Mello and Yu Yasufuku, *On higher dimensional integrality and
   multiplicative dependence in semigroup algebraic dynamics*,
   arXiv:2604.03745, v1 dated 2026-04-04.
7. Hyeonggeun Kim, Holly Krieger, Mara-Ioana Postolache, and Vivian Szeto,
   *Hénon maps with many rational periodic points*, arXiv:2412.01668, v2
   dated 2025-07-08.

The theorem-number roles are exact:

- Amoroso--Viada Theorem 6.2 supplies the displayed nondegenerate unit-
  equation bound, after the algebraic-closure bridge.
- Evertse--Schlickewei--Schmidt Theorem 1.1 is historical only and is not the
  source of \(\mathcal A(q,R)\).
- Krieger et al. Theorem 1.7 is the monic \(S\)-integral one-variable image
  bound. Theorem 1.8 is the local non-Archimedean one-exceptional-coefficient
  valuation statement. Corollary 1.9 is the associated number-field one-orbit
  consequence. None is a two-dimensional, all-initial-state, arbitrary-field
  finite-rank theorem.
- Bell--Ghioca Theorem 1.1 fixes one orbit and a finitely generated subgroup.
  Part (i) gives arithmetic progressions plus a zero-Banach-density residual;
  part (ii), for a regular map, makes only the residual finite. The entire
  hitting-time set need not be finite, and a Hénon restriction to
  \(\mathbb G_m^2\) is generally rational.
- Ji--Xie--Zhang v2 Theorem 1.8 and Corollary 1.9 give cyclotomic periodic-
  point non-density in their stated Hénon/positive-entropy settings, not
  finiteness, a finite-rank group bound, or a window theorem.
- Mello--Yasufuku Theorems 1.1--1.2 and Corollary 1.3 depend on
  \(\mathrm{Hyp}_\epsilon\) for \(\epsilon\ge(1+c)/2\). Theorem 4.2 plus
  Vojta applies only for sufficiently small \(\epsilon\) with additional
  divisor hypotheses. The range/hypothesis mismatch remains unresolved and
  unused.
- Kim--Krieger--Postolache--Szeto Theorem A treats odd \(d>2\), degree at
  most \(d\), and at least \((d-4)^2\) rational periodic points. Theorem B
  treats \(d\equiv1\pmod6\) and a selected integer cycle of length
  \((8d+10)/3\). Neither classifies or bounds all rational or integral
  periodic points.

The bounded primary-source search is frozen through 2026-08-17. Its statement
is only that no direct collision was located for the exact PC1--PC3 package.
It is not a global priority or unpublished-work absence claim.

## Mandatory anti-claims

The article must make the following twenty-one boundaries explicit, without
silently strengthening a neighboring source or the theorem package.

1. No positive-characteristic analogue is claimed.
2. PC1 does not allow \(c=0\), \(a=0\), or a zero displayed \(b_j\).
3. Repeated exponents and zero coefficients must be collected or deleted
   before support size is counted.
4. The support-size statement is not claimed to be affine-conjugacy invariant.
5. The displayed unit-equation, sparse-image, component, and cardinality
   constants are not claimed optimal.
6. No effective enumeration algorithm for \(T_2\) or \(T_4\) is claimed.
7. No height estimate is claimed.
8. No classification of periodic points, rational periodic points, or
   integral cycles is claimed.
9. No classification of every coefficient stratum with an infinite shorter
   window is claimed.
10. No theorem for arbitrary rational maps, arbitrary polynomial
    automorphisms, arbitrary Hénon compositions, or arbitrary normal forms is
    claimed.
11. Finite rank is not replaced by an assertion about arbitrary subgroups.
12. Finite rank is not silently replaced by finite generation.
13. No coefficient is assumed to lie in \(\Gamma\).
14. No closure of \(\Gamma\) under addition is assumed or claimed.
15. The bounded literature search is not an absolute priority, “first,” or
    absence-of-unpublished-work statement.
16. Bell--Ghioca's finite residual is not finiteness of the whole hitting-time
    set, and the Hénon torus restriction is not declared regular.
17. Ji--Xie--Zhang non-density is not turned into finiteness or a cardinality
    bound.
18. The two incompatible Mello--Yasufuku epsilon regimes are not merged into
    an unconditional theorem.
19. The restricted Kim et al. constructions are not turned into universal
    rational or integral periodic-point bounds.
20. No code, CAS, computation, scan, experiment, data, or numerical check is
    theorem evidence.
21. PC3 receives no separate renewed novelty claim and is not a black-box
    citation to the earlier manuscript.

## Mandatory public-safe absorption and no-parallel paragraph

The following paragraph must appear verbatim exactly once in the future
article, in Section 8.3 only. It is excluded from the abstract, theorem
statements, proofs, literature positioning, novelty discussion, tables,
appendices, and References.

> An earlier manuscript by the same authors treated only the one-monomial
> case. The present paper reproduces that theorem and proof in full as part of
> the support-size phase transition, thereby absorbing the earlier manuscript;
> the two manuscripts will not be submitted in parallel, and the present paper
> is the sole intended external version of the overlapping material.

The future article is the sole intended external vehicle for all overlapping
support-one material. The earlier artifact is non-public provenance, is not a
bibliographic entry, supplies no black-box proof step, and may not move toward
external submission in parallel.

## Public-text anonymity and hygiene lock

Both public source files and extracted PDF text must contain no manuscript-
author name, affiliation, email address, or self-identifying link, and no
manuscript/front-matter date or identity-bearing timestamp. They must also
contain no acknowledgment, grant, repository identity, submission identifier,
internal candidate identifier, internal project number, local filesystem
path, hash, governance status, review verdict, agent name, operational
instruction, or priority claim. The article uses an anonymous presentation
with no identity-bearing manuscript-author or PDF metadata and no
acknowledgment section.

Neutral bibliographic author names, publication years, and the locked preprint
version dates are required in citations and References. They are expressly
exempt from the manuscript-author identity and front-matter date ban, but they
may not be used to reveal manuscript authorship.

Generic identity-free producer and creator tool names are permitted in PDF
metadata only when they disclose no user, host, path, or timestamp. Metadata
creation and modification dates, trailer identifiers, identity-bearing author
or subject fields, identity-bearing keywords, and submission identifiers are
forbidden. Neutral bibliographic dates visible in citations and References are
not metadata dates and are not forbidden.

## Independent publication-stage review gate

The sole next project write is exactly:

`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`

The reviewer must be fresh and independent. The reviewer must have authored
or modified none of the fifteen frozen inputs, neither governance artifact,
and no future manuscript source. The governance author cannot review or sign
its own work.

Before the explicit governance-author stop, the reviewer may not open, list,
stat, hash, or inventory either governance path. After that stop, the reviewer
may read exactly the seventeen governance-stage paths. It must rehash all
fifteen inputs and both governance artifacts, validate strict canonical JSON
round-trip behavior with duplicate-key and nonfinite-number rejection, verify
the scope binding, exact inventory, future absences, theorem, proof,
citation, anti-claim, absorption, page, table, anonymity, role, build, review-
chain, cleanup, and lifecycle contracts.

Any mismatch, ambiguity, independence failure, or blocker has disposition
**WRITE NOTHING**. Only if every conjunctive check passes may the reviewer
create its sole review file. Its last nonempty line must be exactly:

**PUBLICATION_STAGE_PASS**

No approximate wording substitutes for that verdict. A missing review or any
other final line leaves all downstream authorization false. A passing review
activates only the anonymous two-file manuscript-author stage; it activates
neither source-level review nor a build.

## Exact stage path universes

Let \(F\) be exactly the fifteen paths in the frozen-input table. Define the
successive exact project path universes:

\[
\begin{aligned}
U_G={}&F\cup\{\texttt{notes/PUBLICATION_STAGE_SCOPE.md},
\texttt{experiments/publication_lock.json}\},\\
U_P={}&U_G\cup\{\texttt{notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md}\},\\
U_D={}&U_P\cup\{\texttt{paper/main.tex},
\texttt{paper/references.bib}\},\\
U_L={}&U_D\cup\{\texttt{notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md}\},\\
U_{R0}={}&U_L\cup\{\texttt{paper/main_round0.pdf},
\texttt{paper/BUILD_RECEIPT_R0.json}\},\\
U_{V1}={}&U_{R0}\cup\{\texttt{notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md}\},\\
U_{S1}={}&U_{V1}\cup\{\texttt{paper/SOURCE_REVISION_RECEIPT_R1.json}\},\\
U_{R1}={}&U_{S1}\cup\{\texttt{paper/main_round1.pdf},
\texttt{paper/BUILD_RECEIPT_R1.json}\},\\
U_{V2}={}&U_{R1}\cup\{\texttt{notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md}\}.
\end{aligned}
\]

Their exact regular-file counts are, respectively,

\[
17, 18, 20, 21, 23, 24, 25, 27, 28.
\]

At every stage the only project directories are `experiments`, `notes`,
`paper`, and `refine-logs`, and the symlink count is zero. A stage may begin
only when its predecessor's exact path universe and stable identities hold and
every later path is absent.

## Exact temporal role contracts

| Role | Activation | Exact read universe | Exact project write universe |
|---|---|---|---|
| publication-stage author | present governance task | \(F\) before writing; each governance artifact only after its own creation for binding and validation | scope, then publication lock only |
| independent publication reviewer | explicit stable governance-author stop | \(U_G\) | publication-stage review only |
| anonymous manuscript author | exact final-line `PUBLICATION_STAGE_PASS` | \(U_P\) | `paper/main.tex`; `paper/references.bib` |
| advisory source-math auditor | stable anonymous-author stop | \(U_D\) | none |
| bounded pre-source repair author | separate explicit repair instruction after a zero-write audit | \(U_D\) | existing `paper/main.tex`; existing `paper/references.bib` only |
| fresh formal source reviewer | stable source stop after any authorized repair and fresh re-audit | \(U_D\) | source-level review only, and only on PASS |
| Round-0 builder | exact source PASS, stable \(U_L\), and separate explicit build GO | \(U_L\) | Round-0 PDF and receipt only |
| fresh Round-1 manuscript reviewer | stable Round-0 builder stop | \(U_{R0}\) | Round-1 review only |
| bounded revision author | stable Round-1 review | \(U_{V1}\) | the two existing sources and revision receipt only |
| Round-1 builder | stable bounded-revision stop | \(U_{S1}\) | Round-1 PDF and receipt only |
| fresh Round-2 reviewer | stable Round-1 builder stop | \(U_{R1}\) | Round-2 review only |

Each read universe is a complete allowlist. No role may read a later artifact,
expand its own read or write universe, review an object it authored, edit
source while building, or self-sign a gate.

## Anonymous manuscript-author contract

Only an exact `PUBLICATION_STAGE_PASS` may activate an anonymous manuscript
author. That author may write exactly:

- `paper/main.tex`;
- `paper/references.bib`.

All eight sections, Appendices A--C, definitions, theorems, proofs, four proof
tables, limitations, and the unique Section 8.3 paragraph must be in the
single `main.tex`. No `sections/`, macro file, style file, class file, figure,
asset, supplementary source, code, data, result, or build artifact is
authorized. The bibliography file contains exactly the seven locked primary
entries and no others.

The author may not compile, access the network, install software, run code,
CAS, symbolic engines, scientific calculations, scans, or parameter searches,
or generate data or assets. It may not read any future source review, build,
manuscript review, revision, finalization, or release artifact. The sources
must include deterministic pdfTeX-compatible controls suppressing dates,
identity-bearing metadata, and the trailer identifier, without exposing
governance in public text.

The author must perform static source checks only, report stable SHA-256 and
byte counts for both source files, verify exact \(U_D\), and stop. That stop
does not authorize a build.

## Zero-write source audit, bounded repair, and formal source PASS

After the anonymous-author stop, a source-math auditor may read exactly
\(U_D\) and perform a zero-project-write advisory audit of proof completeness,
theorem constants, citations, abstract word count, structure, source hygiene,
LaTeX compatibility, bibliography-key equality, and all static contracts.
The audit has no lifecycle effect and creates no project path.

If that audit finds a bounded compatibility or proof-presentation defect, a
source repair is permitted only after a separate explicit instruction. The
repair author may edit only the two existing public sources, may not enlarge
the theorem or bibliography, and must map every edit to the bounded defect.
After any repair, the author stops with new stable identities and a fresh
source audit is required. No repair is authorized merely by this scope.

There is exactly one formal source-level review path:

`notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md`

A fresh reviewer, who authored neither public source, reads exactly \(U_D\).
It independently checks the complete PC1--PC3 proof, every citation role, all
seven bibliography entries and citation keys, all static LaTeX and anonymity
requirements, the 180--220-word abstract, eight sections, three appendices,
four proof tables, exact absorption occurrence, and every anti-claim. A
blocker has disposition **WRITE NOTHING**. Any resulting repair requires a
separate explicit instruction and then a fresh reviewer; the blocked reviewer
does not leave a project report.

Only if every source-level check passes may the reviewer create its sole file,
whose last nonempty line is exactly:

**MANUSCRIPT_SOURCE_PASS**

That PASS binds the exact source SHA-256 and byte counts. It still does not
authorize compilation. Round 0 requires, in addition, a separate explicit
build GO and stable exact \(U_L\).

## Round-0 isolated deterministic build protocol

Round 0 begins only after stable source bytes, exact
`MANUSCRIPT_SOURCE_PASS`, exact \(U_L\), every later path absent, and a
separate explicit build GO. It performs exactly two clean builds in two
distinct, new, empty, builder-owned, non-symlink directories created from the
literal template:

`/tmp/p16-paper16-r0-XXXXXXXX`

Each resolved directory must match
`^/tmp/p16-paper16-r0-[A-Za-z0-9]{8}$`, have `/tmp` as its resolved parent,
and contain no entry before the exact two source-byte copies are placed there.
Reuse or a path outside the pattern is a blocker.

The builder resolves one absolute `pdflatex` and one absolute `bibtex`
executable before both runs, records each executable's SHA-256 and complete
version text, and uses the same identities in both. Every build command uses
exactly this environment:

    TZ=UTC
    LC_ALL=C
    LANG=C
    SOURCE_DATE_EPOCH=1786924800
    FORCE_SOURCE_DATE=1

In each clean root, run exactly and in order:

    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex

All eight exit codes must be zero. The builder may not edit source, access the
network, install a package, rasterize any page, run scientific code or CAS,
use shell escape, or read an undeclared project path. In each temporary root,
the only allowed entries are regular non-symlink files named `main.tex`,
`references.bib`, `main.aux`, `main.bbl`, `main.blg`, `main.log`, optional
`main.out`, optional `main.toc`, and `main.pdf`.

The two PDFs must be identical in bytes, SHA-256, and byte count. The two
`main.bbl` files must also be byte-identical. A mismatch fails the round and
cannot be repaired by selecting one output.

## Non-raster source and PDF validation contract

Before persistence, both clean builds must pass all of the following checks
using non-raster tools:

- zero TeX, LaTeX, and BibTeX errors;
- zero undefined references and zero undefined citations;
- zero unresolved TODO, FIXME, XXX, VERIFY, placeholder, drafting, or repair
  marker;
- every warning enumerated, with a warning failing unless it is explicitly
  cosmetic, source-independent, incapable of affecting mathematics, layout,
  citations, fonts, anonymity, or reproducibility, and later accepted by the
  independent manuscript reviewer;
- zero missing glyphs, missing characters, missing fonts, and overfull boxes;
- all PDF fonts embedded, subset, and equipped with a Unicode map;
- exact title, anonymous presentation, 180--220-word abstract, Sections 1--8,
  Appendices A--C, and final References in the locked order;
- 24--26 nonempty mathematical-content pages from the first page through the
  end of Appendix C, including the appendices and excluding References;
- exactly four proof tables in their locked locations and zero other tables;
- zero figure environment, `\includegraphics`, image file, external asset,
  image XObject, attachment, embedded file, AcroForm, XFA object, JavaScript,
  launch action, rich-media object, or file-attachment annotation;
- anonymous metadata with no author identity, date, submission identifier,
  local path, or trailer ID;
- public source and extracted PDF text free of internal paths, hashes,
  project numbers, governance labels, verdicts, acknowledgments, grants,
  identity, unsupported priority language, and operational instructions;
- exact set equality among citation keys used in `main.tex`, entry keys in
  `references.bib`, and `\bibitem` keys in `main.bbl`, with exactly seven
  keys, no duplicate, wildcard `\nocite`, uncited entry, or missing entry;
- exact theorem assumptions, constants, field bridge, four PC1 cases,
  support-one ledger, examples, counterexamples, citation roles, anti-claims,
  and exactly one verbatim absorption paragraph in Section 8.3; and
- zero empirical claim or computational evidence.

Every non-raster validation executable whose output enters a receipt must be
recorded by absolute path, executable SHA-256, and complete version text.
Every PDF page must contain non-whitespace public mathematical text; blank
pages are forbidden.

## Round-0 persistence, receipt, and cleanup

Only after both clean builds and all validation checks pass may the builder
persist exactly:

- `paper/main_round0.pdf`;
- `paper/BUILD_RECEIPT_R0.json`.

No `paper/main.pdf`, auxiliary, log, transcript, cache, temporary directory,
or other project artifact may remain. The persisted PDF is an exact byte copy
of both clean-run PDFs.

`BUILD_RECEIPT_R0.json` must be strict compact canonical JSON: UTF-8; object
keys recursively sorted by Unicode code point; no insignificant whitespace,
duplicate key, nonfinite number, or carriage return; and exactly one terminal
LF. Its own SHA-256 and byte count are excluded. It binds:

- the governance pair, publication-stage review, both sources, and formal
  source-level review;
- prebuild and postbuild source SHA-256 and byte counts;
- both validated temporary-root paths, pattern, ownership, distinctness,
  initial emptiness, and non-symlink status;
- absolute build and validation executable paths, hashes, and full versions;
- the exact environment and command sequence, all eight exit codes, and each
  command transcript's hash and byte count;
- per-run PDF, `main.bbl`, final-log, and combined-transcript hashes and bytes;
- PDF and BBL identity booleans;
- every error, warning, reference, citation, glyph, font, overfull-box, page,
  nonempty-page, metadata, security, public-text, citation-set, table, figure,
  proof-content, and external-access check;
- the persisted PDF hash and byte count;
- exact prewrite and postwrite stage universes; and
- explicit temporary cleanup operations and verified root absences.

After all receipt facts needed from a temporary root are captured, the builder
validates the resolved root and exact regular-file allowlist, unlinks each
allowed file individually by an explicit resolved path, and removes the now
empty root with `rmdir`. Recursive deletion, unresolved variables, globs, and
symlink traversal are forbidden. Both roots must be verified absent before
the builder stops. A validation failure authorizes no persistence; a cleanup
failure after persistence is reported as a blocker without adding another
project artifact.

## Round-1 review and the sole bounded revision

After a stable exact \(U_{R0}\) builder stop, a fresh independent reviewer may
write only:

`notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md`

A precondition mismatch has disposition **WRITE NOTHING**. Otherwise, the
review rehashes the complete allowed chain, validates the R0 receipt and PDF
against the sources, and independently audits every theorem, proof
transition, constant, table row, example, citation role, bibliography key,
page boundary, nonempty page, limitation, anti-claim, anonymity property,
absorption occurrence, PDF structural property, warning disposition, and
visual layout without rasterization.

The final disposition is exactly one of `MANUSCRIPT_R1_PASS` or
`MANUSCRIPT_R1_REPAIR_REQUIRED`. Every finding has a stable identifier,
severity, exact location, required bounded repair, and theorem-scope impact.
Neither disposition authorizes finalization or release.

Exactly one bounded revision-author window follows the stable R1 review. The
author may edit only `paper/main.tex` and `paper/references.bib` and must add
the strict canonical `paper/SOURCE_REVISION_RECEIPT_R1.json`. Every change
must map to an R1 finding and preserve theorem scope, proof dependencies,
citation boundaries, page contract, anonymity, and absorption. If R1 requires
no repair, both source files remain byte-identical and the receipt records a
no-op with zero changes. No second revision window exists. A theorem,
bibliography, governance, or evidence expansion is a blocker.

The revision receipt excludes its own hash and bytes and binds the R1 review,
pre/post source hashes and bytes, an exact source-diff digest and bounded
change ledger, or explicit no-op identities. It also binds exact prewrite and
postwrite path universes.

## Round-1 deterministic rebuild and fresh Round-2 review

After an exact \(U_{S1}\) revision stop, the Round-1 builder repeats the same
two-clean-build protocol and every validation against the revised source. Its
two clean roots use the literal template

`/tmp/p16-paper16-r1-XXXXXXXX`

and match `^/tmp/p16-paper16-r1-[A-Za-z0-9]{8}$`. It persists only:

- `paper/main_round1.pdf`;
- `paper/BUILD_RECEIPT_R1.json`.

The R1 receipt has the same canonical and content contract as R0. It also
binds the R0 PDF and receipt, R1 review, revision receipt, and exact authorized
pre/post source identities. It preserves all R0 artifacts and never writes
`paper/main.pdf`. The R0 and R1 PDFs may differ only if the revision receipt
authorizes the exact source diff; after a no-op revision, they must be
byte-identical.

After a stable exact \(U_{R1}\) stop, a fresh Round-2 reviewer, distinct from
all authors, builders, and prior reviewers, may write only

`notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md`.

A precondition mismatch has disposition **WRITE NOTHING**. The reviewer
rehashes the full allowed chain, replays every R1 finding and repair, verifies
no theorem drift or new defect, and repeats every theorem, proof, citation,
page, PDF, anonymity, warning, public-text, inventory, and cleanup audit. The
sole positive final-line verdict is exactly:

**MANUSCRIPT_R2_PASS**

A repair-required result creates no second revision authority.

Even an exact Round-2 PASS does not authorize finalization, `paper/main.pdf`,
camera-ready changes, identity disclosure, public release, submission,
upload, venue communication, external messaging, or use of the absorbed
predecessor as a parallel vehicle. Each requires a separate future lock and
fresh independent review.

## Inventory and publication-author stop

Immediately before these governance writes, the project contained exactly 15
regular files, four subdirectories excluding the root, zero symbolic links,
and no other entry type. After this scope and the canonical lock are written,
the required inventory is exactly \(U_G\): 17 regular files, the same four
subdirectories (`experiments`, `notes`, `paper`, `refine-logs`), zero symbolic
links, and no other entry type.

At the governance stop, all of the following are absent:

- `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`;
- `notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md`;
- `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md`;
- `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md`;
- `paper/main.tex` and `paper/references.bib`;
- both round PDFs and both build receipts;
- `paper/SOURCE_REVISION_RECEIPT_R1.json` and `paper/main.pdf`;
- every section source, macro file, style file, class file, figure, asset,
  code, data, result, build intermediate, release, submission, upload,
  identity, or external-messaging artifact; and
- every forbidden directory named `build`, `code`, `data`, `figures`,
  `manuscript`, `output`, `release`, `results`, `source`, or `submission`.

The publication lock binds this scope by safe relative path, SHA-256, byte
count, and LF-line count. It binds itself only by relative path and authority
role; its own SHA-256 and byte count are excluded. The lock is strict compact
canonical JSON with recursively Unicode-sorted keys, duplicate-key and
nonfinite-number rejection, and exactly one terminal LF.

After writing and validating exactly the two governance artifacts, the author
must rehash all fifteen frozen inputs, verify exact \(U_G\), verify every
future absence, report both governance identities, and stop. No downstream
file may be written in the same authoring turn.
