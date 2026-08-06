# Source and duplication audit

Date: 2026-08-06

## Local inheritance

Paper 5 contributes the exact area-preserving Hénon family, reversibility,
periodic-orbit viewpoint, and the motivation to seek a natural spectral
object.  Its fitted critical values, quartic surrogate, zero fit, and averaged
Markov constructions are hypotheses or modeling choices, not foundations.
The present \(a=6\) map is a member of that exact family, but it is a distinct
rigorously certified hyperbolic regime rather than Paper 5's fitted
near-critical \(a\approx1.02\) regime.  No numerical conclusion is transferred
between those parameters without proof.

The following repository programs already occupy nearby ground:

- `cyclic_ulam_map`: finite-resolution Ulam spectra;
- `dyna_zeta_map`: generic finite cycle/zeta experiments;
- `henon_weighted_zeta`: the certified local survivor, multiplier-weighted
  cycle determinants, and finite-volume comparisons;
- `henon_mobius_correlations`: typical and exceptional arithmetic
  correlations.

Accordingly, the new paper cannot consist only of another Ulam matrix, an
unweighted SFT zeta, a finite-section instability determinant, a raw Möbius
correlation, or a pressure root.

## External boundary

The area-preserving Hénon map already has mature work on anti-integrable
symbolic continuation, homoclinic bifurcations, and symmetry constraints.  A
new symbolic catalogue alone is therefore not a credible novelty claim.

Natural unitary quantization of a classical Hénon map on \(L^2(\mathbb R)\)
also already exists.  A direct quantization or a numerical unitary spectrum is
not novel without a new localized trace, determinant, resonance, or obstruction
theorem.

Complex Hénon/Julia dynamics already appear in rigorous and semiclassical
tunneling studies.  A complexification is a candidate only if it yields a
specified holomorphic operator theorem not present in that literature.

Arithmetic Hénon dynamics is an active field: adelic heights, periodic
parameter values, and rational/integral periodic points have been studied.
Finite-field and adelic candidates remain legitimate exploration targets, but
their exact theorem delta must be audited before novelty is claimed.

## Novelty policy

No candidate in this planning package is declared novel.  Promotion requires a
claim-by-claim primary-source table answering:

1. Is the mathematical object already defined?
2. Is the claimed orbit/determinant identity already known in greater
   generality?
3. Does the Hénon specialization add a theorem or only an example?
4. Is the proposed arithmetic or operator structure intrinsic under recoding,
   conjugacy and gauge?
5. What precise negative theorem remains publishable if the bridge fails?

## External sources for the first audit

- D. G. Sterling, H. R. Dullin, and J. D. Meiss, “Homoclinic Bifurcations for
  the Hénon Map,” including anti-integrable symbols and the area-preserving
  case: https://arxiv.org/abs/chao-dyn/9904019
- J. E. Fornæss and B. Weickert, “A quantized Hénon map,” unitary quantization
  on \(L^2(\mathbb R)\):
  https://www.aimsciences.org/article/doi/10.3934/dcds.2000.6.723
- A. Shudo, Y. Ishii, and K. S. Ikeda, complex Hénon/Julia-set tunneling:
  https://arxiv.org/abs/nlin/0205048
- L.-C. Hsia and S. Kawaguchi, adelic heights and periodic parameters in Hénon
  families: https://arxiv.org/abs/1810.03841
- H. Kim, H. Krieger, M.-I. Postolache, and V. Szeto, rational and integral
  periodic points for Hénon maps: https://arxiv.org/abs/2412.01668
- R. Calleja et al., high-order periodic-orbit computation for symplectic maps:
  https://arxiv.org/abs/2003.02788
- J. E. Fornæss, H. Peters, and L. Vivas, “Hénon maps: a list of open
  problems”: https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html
- R. Bowen and C. Series, Markov maps associated with Fuchsian groups:
  https://numdam.org/articles/10.1007/BF02684772/
- L. Guillopé, K. K. Lin, and M. Zworski, Schottky/Selberg zeta as a Fredholm
  determinant: https://arxiv.org/abs/math/0211041
- R. de la Llave, J. M. Marco, and R. Moriyón, periodic data and Livšic
  cohomology: https://annals.math.princeton.edu/1986/123-3/p03
- J. A. G. Roberts and F. Vivaldi on finite reversible maps:
  https://arxiv.org/abs/0905.4135
- J. Allen, D. DeMark, and C. Petsche, non-Archimedean Hénon horseshoes:
  https://arxiv.org/abs/1610.04271
- H. Balibrea-Iniesta et al., non-autonomous Hénon horseshoe geometry:
  https://arxiv.org/abs/1705.10216
- J. Buzzi, analytic limitations for random zeta functions:
  https://doi.org/10.1017/S0143385702000524

These sources delimit obvious collisions; they do not constitute a complete
novelty review.

## Exact anti-integrable/SFT collision at (H_6)

Sterling--Dullin--Meiss is a direct source collision, not merely background.
For their Hénon convention

\[
(x',y')=(y-k+x^2,-bx),
\]

the linear change

\[
x=-6q,qquad y=6p
\]

conjugates the Paper-5 map \(H_6(q,p)=(1-6q^2-p,q)\) to their
area-preserving parameters \(b=1,k=6\).  With

\[
\epsilon=k^{-1/2}=1/\sqrt6,qquad z=\epsilon x=-\sqrt6q,
\]

their equation (3) and signed-root operator (7) are

\[
\epsilon(z_{i+1}+bz_{i-1})+1-z_i^2=0,
\qquad
T_i(z)=s_i\sqrt{1+\epsilon(z_{i+1}+bz_{i-1})},
\]

which are exactly the real C02B recurrence after this sign/scale change.

Their §5 defines

\[
\Sigma_F=\{s:\text{the two chronological neighbors are not both }-\}.
\]

Because \(s_i=\operatorname{sgn}z_i=-\operatorname{sgn}q_i\), this is exactly
the C02B/C02C rule that the two \(q\)-neighbor signs are not both positive.
Theorem 3 (preprint printed pp. 12--13) proves existence and uniqueness for
every sequence in this SFT by the same contraction mechanism.  Its equation
(12) has the limiting bound

\[
\lim_{b\to1^-}\epsilon_{\max}(b)=\frac1{\sqrt3}
>\frac1{\sqrt6},
\]

so it covers this exact real \(H_6\) parameter.  Consequently, the real
signed-root survivor, its SFT, and real sequence-space existence/uniqueness
are prior art and cannot contribute to novelty.  The C02B/C02C survivor is
only the specified complex disks, full complex endpoint domains, joint
holomorphy, explicit localization/projective constants and any later
trace-compatible aggregate error theorem.

Primary source: D. G. Sterling, H. R. Dullin and J. D. Meiss,
[*Homoclinic Bifurcations for the Hénon Map*](https://arxiv.org/abs/chao-dyn/9904019),
especially equations (1), (3), (7), §5 and Theorem 3.

## Post-pilot theorem boundary

The C02B pilot proves an explicit signed-root sequence-polydisc contraction,
but “complex domain exists” is not itself a novelty claim.  Complex Hénon
horseshoes and their symbolic/pinning structures are already treated in, among
other sources:

- J. H. Hubbard and R. W. Oberste-Vorth, *Hénon mappings in the complex
  domain I: The global topology of dynamical space*:
  https://www.numdam.org/articles/10.1007/BF02698886/
- J. H. Hubbard and R. W. Oberste-Vorth, *Hénon mappings in the complex
  domain II: Projective and inductive limits of polynomials*:
  https://arxiv.org/abs/math/9401224
- R. W. Oberste-Vorth, *Complex horseshoes and the dynamics of mappings of two
  complex variables*, Cornell PhD thesis (1987; uploaded to arXiv in 2005):
  https://arxiv.org/abs/math/0507073

Hubbard--Oberste-Vorth II's Definition 3.2 and Proposition 3.7 give general
crossed mappings and their composition and are a direct collision for that
qualitative mechanism.  The small-Jacobian restriction belongs to its global
Hénon application (Theorem 1.4 and §4), which does not directly certify the
present determinant-one \(H_6\) disks.  Oberste-Vorth supplies the broader
complex-horseshoe boundary; exact applicability to the certified domains is
not asserted.

More directly, analytic pinning coordinates and their iterates already exist:

- H. H. Rugh, *The correlation spectrum for hyperbolic analytic maps*,
  Nonlinearity 5 (1992), 1237--1263:
  https://doi.org/10.1088/0951-7715/5/6/003
- V. Baladi, E. R. Pujals, and M. Sambarino, *Dynamical zeta functions for
  analytic surface diffeomorphisms with dominated splitting*:
  https://arxiv.org/abs/math/0307045

In particular, the latter's Proposition 2.6 and Corollary 2.8 give iterated
analytic pinning maps, two-variable composition/fixed-point relations, and
symbolic-cycle closure for the almost-hyperbolic analytic symbolic maps and
admissible non-all-neutral words defined there.  This covers the qualitative
mechanism needed for the uniformly hyperbolic \(H_6\) branches, but is not a
statement about arbitrary analytic surface systems.  Finite-window existence,
holomorphy, gluing, or cyclic closure alone is therefore not a credible
theorem delta.

Their formulas (3.10)--(3.11) and the residue computation produce the
absolute denominator \(|\det(Df^n-I)|^{-1}\), with orientation signs in the
kernel playing an essential role.  They therefore establish the general
absolute flat-trace/Fredholm mechanism, not the present signed holomorphic
convention \(\det(I-DH_6^n)^{-1}\).  A signed operator/cocycle convention must
be frozen and proved separately in C02D.

Likewise, a statement that an analytic Axiom-A system has a generalized
Fredholm determinant is available in broader settings; see H. H. Rugh,
*Generalized Fredholm determinants and Selberg zeta functions for Axiom A
dynamical systems*:
https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/generalized-fredholm-determinants-and-selberg-zeta-functions-for-axiom-a-dynamical-systems/5CCDE98C3D58F37B45E78AD07B29C339

Accordingly, the next-paper novelty gate is not “complexify the Hénon map,”
“construct pinning coordinates,” or “write a Fredholm determinant.”  WP0 must
first determine whether a constructive quantitative theorem delta remains:

1. explicit finite-window endpoint domains for the Paper-5/R059 recurrence;
2. holomorphic dependence and exponential boundary localization with
   source-locked constants;
3. an exact crossed-map matching-Jacobian identity tied to chronological
   monodromy and the signed local flat trace;
4. complex-\(q\) projective-fibre recertification and a quantitative error or
   distortion theorem not supplied verbatim by general theory;
5. only later, an explicit graph-directed operator and trace-compatible
   approximation theorem under a separately frozen function-space convention.

The completed comparison shows that the qualitative statements are direct
collisions, while explicit constants and identities survive as effective
C02C infrastructure.  They are insufficient by themselves to freeze the
paper.

### Scoped WP0 comparison matrix after Sterling and C02C

This table is the completed scoped WP0 routing audit.  It fixes the current
claim boundary for C02C; it is not a substitute for a journal-level exhaustive
review.

| Proposed claim | Closest known scope | Final ruling | Surviving \(H_6\) delta |
|---|---|---|---|
| Real signed-root SFT and sequence-space uniqueness at \(H_6\) | Sterling--Dullin--Meiss Theorem 3 covers the conjugate \(b=1,k=6\) system and the same forbidden-neighbor SFT. | **known; no novelty** | none for the real survivor/existence mechanism |
| Explicit complex signed-root sequence polydiscs with margins and contraction \(2/\sqrt{17}\) | Sterling--Dullin--Meiss supplies the real contraction/SFT; general complex horseshoe/pinning theories supply holomorphic context but do not state these project disks and constants. | retain as proved effective specialization; novelty unconfirmed | specified complex domains, exact constants, reproducible certificate |
| Unique holomorphic finite-window endpoint solution | Rugh pinning half-inverses and Baladi--Pujals--Sambarino iterated pinning maps cover this mechanism in general analytic hyperbolic settings. | not a standalone novelty claim | explicit full-disk Neumann bounds only |
| Two-variable pinning composition and symbolic-cycle closure | Baladi--Pujals--Sambarino Proposition 2.6 and Corollary 2.8 are a direct collision risk. | presumed known until a sharper delta is proved | exact \(H_6\) matching-Jacobian/monodromy formula and certified error |
| Complex projective derivative child disks | C02 proves disks only over the real survivor; general theory does not automatically validate those same disks for complex \(q\). | **proved in C02C** | exact minimal complex-\(q\) child disks, separation and fibre derivative constant; no joint unscaled base--fibre contraction |
| Nuclear analytic operator and periodic-orbit trace | Rugh 1992 and BPS provide closely related constructions; BPS's orientation-signed kernel yields an absolute determinant denominator. | no claim; exact signed space/kernel/weight unset | only a new signed specialization plus non-routine aggregate approximation theorem |
| Entire/generalized Fredholm determinant for an Axiom-A surface system | Rugh 1996 proves this in broader settings. | not novel by specialization alone | a different intrinsic weight with a proved new identity, if one exists |
| Crossed-map composition in Hubbard--Oberste-Vorth II | Definition 3.2 and Proposition 3.7 are general and directly collide with qualitative crossed composition; its global Hénon application uses a small-Jacobian regime that does not certify the determinant-one disks. | composition known; global \(H_6\) domain not subsumed | only explicit determinant-one domains/constants |

### Primary-source location audit

The following locations were checked against the exact claims needed by the
finite-window construction.

| Source | Checked mechanism | Location and ruling |
|---|---|---|
| Sterling--Dullin--Meiss, *Homoclinic Bifurcations for the Hénon Map* | real signed-root operator, SFT and uniqueness at the exact area-preserving parameter | Equations (1), (3), (7), printed pp. 2, 4--5; §5 and Theorem 3, printed pp. 11--13.  The conjugacy \((x,y)=(-6q,6p)\) sends \(H_6\) to \(b=1,k=6\), and the sign reversal identifies the two forbidden-neighbor rules.  Since \(1/\sqrt6<\lim_{b\to1^-}\epsilon_{\max}=1/\sqrt3\), the real SFT/existence theorem is a direct collision. |
| Baladi--Pujals--Sambarino, *Dynamical zeta functions for analytic surface diffeomorphisms with dominated splitting* | pinning coordinates, chronological iteration, periodic closure, kernel and determinant | Definition 2.4 and (2.6), preprint printed p. 6 (published p. 180); Proposition 2.6 and (2.7)--(2.10), pp. 8--9 (published pp. 182--183); Remark 2.7, p. 9; Corollary 2.8, p. 10 (published p. 184); kernel (2.13), p. 11 (published p. 185); Remark 3.6, p. 21 (published p. 195); Lemma 3.8 and (3.10)--(3.11), p. 23 (published p. 197); residue calculation, p. 25 (published p. 199).  These supply qualitative two-variable pinning, chronological gluing, periodic closure and the **absolute-denominator** flat-trace/Fredholm mechanism.  The residue numerator contains the corresponding endpoint derivative, but the signed convention remains open. |
| Rugh, *The correlation spectrum for hyperbolic analytic maps* (1992) | original analytic hyperbolic pinning and spectral construction | DOI and bibliographic record verified.  The publisher full text was not openly available in this environment, so exact theorem locations were cross-checked through the explicit attribution and formulas in Baladi--Pujals--Sambarino.  No claim of a direct full-text page audit is made. |
| Rugh, *Generalized Fredholm determinants and Selberg zeta functions for Axiom A dynamical systems* (1996) | generalized weighted Fredholm determinant | Theorem 1 in the author/CERN copy gives the entire generalized weighted determinant for real-analytic Axiom-A surface diffeomorphisms.  A qualitative determinant for the present horseshoe is therefore not new by specialization. |
| Hubbard--Oberste-Vorth II | crossed mappings and composition in complex Hénon dynamics | Definition 3.2 and Proposition 3.7 give general crossed mappings and composition and directly collide with that mechanism.  The small-Jacobian condition belongs to the later global Hénon application, which does not directly include the determinant-one disks. |
| Oberste-Vorth, *Complex horseshoes...* (Cornell PhD thesis) | general complex horseshoe framework | Confirms that complex horseshoe existence and symbolic coding are mature prior art; it does not state the C02C constants. |
| Yi-Chiuan Chen, *Holomorphic Shadowing for Hénon Maps Revisited: an Implicit Function Theorem Perspective* ([arXiv:2203.02970](https://arxiv.org/abs/2203.02970)) | holomorphic continuation/shadowing context | Reviews the signed-root/shadowing operator lineage, including Sterling--Meiss, and reinforces that holomorphic orbit continuation is not by itself a theorem delta.  Its Hubbard--Oberste-Vorth shadowing objective and parameter setting differ from the explicit determinant-one endpoint certificate. |

Primary links used for the audit are the
[Sterling--Dullin--Meiss arXiv record](https://arxiv.org/abs/chao-dyn/9904019),
the
[official IMJ preprint](https://www.imj-prg.fr/preprints/350.pdf) and
[arXiv record](https://arxiv.org/abs/math/0307045) for
Baladi--Pujals--Sambarino, the
[1992 DOI](https://doi.org/10.1088/0951-7715/5/6/003), the
[official CERN copy of Rugh 1996](https://cds.cern.ch/record/260160/files/P00021854.pdf),
the [Hubbard--Oberste-Vorth II preprint](https://arxiv.org/abs/math/9401224),
and [Oberste-Vorth's complex-horseshoe thesis](https://arxiv.org/abs/math/0507073).

### Scoped WP0 routing ruling after Sterling and C02C

The scoped WP0 audit leaves a nonempty project-specific effective package,
but **does not confirm a publishable novelty delta**.  C02C proves, for the
exact Paper-5 family at \(a=6\):

1. full frozen endpoint disks and uniform constants
   \(a_0=1/\sqrt{17}\), \(\kappa=2/\sqrt{17}\), and
   \(\beta=1/(\sqrt{17}-2)\);
2. explicit exponential endpoint localization and exact two-coordinate
   gluing, including the doubled chronological incidences at periods one and
   two;
3. an explicit signed matching/Hill/monodromy bookkeeping identity and
   finite-dimensional trace-residue factor; BPS already contains the general
   matching/monodromy residue mechanism in the absolute-denominator
   convention, and the Hill identity is not counted as standalone novelty;
4. exact complex-\(q\) projective child disks, pole clearance, separation and
   distortion constants;
5. a reproducible producer/checker certificate with complete case IDs and
   adversarial chronology controls.

Those results are useful effective infrastructure, but the real signed-root
SFT/existence, qualitative complex pinning, gluing, periodic closure and
absolute-denominator Fredholm mechanism are prior art.  The ruling is
therefore
`RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD;
NOVELTY_DELTA_UNCONFIRMED`.  A full paper is frozen only if a
trace-compatible cylinder/operator approximation theorem converts the
explicit constants into a genuinely new aggregate estimate.  A direct Rugh
1992 full-text check, a dedicated Hill-identity source audit and a
journal-level novelty review remain mandatory before any manuscript freeze.
Otherwise C02C remains a rigorous project-specific bridge and the
breadth-first RH search resumes.

## Post-pilot negative-source boundary

The C03 matched-control result is consistent with Roberts--Vivaldi's theory of
finite reversible maps.  Its local identity is therefore recorded as a
false-positive mechanism, not an arithmetic discovery.  The C05 gauge and
one-symbol Maslov collapses are exact internal obstructions and require no
external statistical novelty claim.
