# HCS-C33 source corpus and annotated bibliography

**Audit date:** 2026-08-12 UTC

## Corpus labels

- **Core:** directly supports or defeats a proposed C33 claim.
- **Boundary:** fixes terminology or prevents a stronger inference.
- **Context:** maps the active nearby literature.
- **Excluded:** assessed and found not to address the coupled object.

The evidence level follows the field-neutral ARS hierarchy.  Most primary
mathematical papers are Level VI because they are individual theoretical or
computational studies; a foundational monograph is Level VII.  The letter
grade records directness, source integrity, and applicability to C33, not an
empirical-study ranking.

## A. Exact Hénon orbit algebra

### 1. Endler and Gallas 2002 — Core, Level VI, grade A

Endler, A., & Gallas, J. A. C. (2002). Arithmetical signatures of the
dynamics of the Hénon map. *Physical Review E, 65*, 036231.
https://doi.org/10.1103/PhysRevE.65.036231

This paper gives a parameter-dependent polynomial for period-four Hénon
orbits and studies the resulting arithmetic monodromy/discontinuities.  It
establishes that low-period elimination, parameter discriminants, and
ordinary orbit-cover monodromy are prior art.  It does not introduce a
periodic action-value map, Maxwell divisor, or Hill-decorated collision.

### 2. Endler and Gallas 2004 — Core, Level VI, grade A

Endler, A., & Gallas, J. A. C. (2004). Existence and characterization of
stable ghost orbits in the Hénon map. *Physica A, 344*, 491–497.
https://doi.org/10.1016/j.physa.2004.06.019

The paper derives exact period-six coordinate, orbital-sum, and stability
polynomials and uses discriminants to locate bifurcations.  It is direct
precedent for coupling exact orbit algebra to stability, but its marker is an
orbital-coordinate sum rather than the cyclic action, and it does not form a
Kummer cover on an equal-action locus.

### 3. Endler and Gallas 2006, orbital sums — Decisive core collision,
Level VI, grade A

Endler, A., & Gallas, J. A. C. (2006). Reductions and simplifications of
orbital sums in a Hamiltonian repeller. *Physics Letters A, 352*, 124–128.
https://doi.org/10.1016/j.physleta.2006.01.031
Author PDF: https://inaesp.org/PublicJG/endler_gallas_orbital_sums_PLA2006.pdf

This is the decisive prior-work boundary.  It gives the exact period-five
Hamiltonian Hénon sextics, the six period-five cycles at \(A=6\), their
number-field organization, discriminants, and full symmetric Galois group.
The C33 marker normalization/function field is therefore not new.  The paper
studies sums of orbital coordinates \(\sigma=\sum q_i\), not the generating
action \(\Phi_{5,A}\), and it does not compute the degree-nine equal-action
divisor or a Hill square class on it.

### 4. Endler and Gallas 2006, conjugacy classes — Core, Level VI, grade A

Endler, A., & Gallas, J. A. C. (2006). Conjugacy classes and chiral doublets
in the Hénon Hamiltonian repeller. *Physics Letters A, 356*, 1–7.
https://doi.org/10.1016/j.physleta.2006.04.042
Author PDF: https://www.inaesp.org/PublicJG/conjugacy_classes_PLA_356_1_2006.pdf

This paper separates diagonal, non-diagonal, and chiral orbit classes and
gives exact low-period factorization formulas.  It establishes that
reversibility classes and branch pairing are prior art.  It does not use an
equal-action node or descend a stability square class through branch
exchange.

### 5. Gallas 2007 — Context/core boundary, Level VI, grade A-

Gallas, J. A. C. (2007). Counting orbits in conjugacy classes of the Hénon
Hamiltonian repeller. *Physics Letters A, 360*, 512–514.
https://doi.org/10.1016/j.physleta.2006.08.065
Author PDF: https://inaesp.org/PublicJG/counting_PLA360_512_2007.pdf

The paper gives arbitrary-period counting formulas for reversible Hénon orbit
classes.  It prevents C33 from claiming the first exact class count or first
use of reversibility.  Its counts do not determine action-critical-value
geometry or Hill-Kummer monodromy.

### 6. Brison and Gallas 2018 — Decisive equivalence boundary, Level VI,
grade A

Brison, O. J., & Gallas, J. A. C. (2018). Polynomial interpolation as
detector of orbital equation equivalence. *International Journal of Modern
Physics C, 29*(8), 1850096.
https://doi.org/10.1142/S0129183118500961

The authors publish polynomial bridges between equivalent orbital equations,
including the period-five Hénon cluster used by the repository.  This closes
the loophole that a relabelled sextic or birationally equivalent plane model
could be advertised as a new orbit cover.  C33 must be about the singular
action embedding and Hill decoration, not the normalization.

## B. Discrete action and the closest Hénon equal-action precedent

### 7. Kook and Meiss 1989 — Core, Level VI, grade A

Kook, H.-T., & Meiss, J. D. (1989). Periodic orbits for reversible,
symplectic mappings. *Physica D, 35*, 65–86.
https://doi.org/10.1016/0167-2789(89)90096-1

This is foundational prior work for reversible symplectic maps, generating
functions, and periodic-orbit action principles.  The use of a discrete
action to encode periodic Hénon trajectories is not itself new.

### 8. Shudo 2005 — Closest conceptual collision, Level VI, grade B+

Shudo, A. (2005). Stokes geometry for the quantized Hénon map in the
horseshoe regime. *RIMS Kôkyûroku, 1431*, 107–115.
https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1431-12.pdf

The paper writes a discrete Hénon action functional, derives the map by its
variational equations, and defines virtual turning points using two distinct
saddles with a common endpoint and equal action.  This is the closest
conceptual prior collision: C33 cannot claim the first equal-action Hénon
saddles.  The setting is a fixed-endpoint quantum propagator and Stokes
geometry, not a closed period-five orbit family over the parameter line; no
degree-nine parameter divisor, Hill branch product, number-field norm, or
Kummer cover appears.

### 9. Shudo and Ikeda 2008 — Core boundary, Level VI, grade A-

Shudo, A., & Ikeda, K. S. (2008). Stokes geometry for the quantum Hénon map.
*Nonlinearity, 21*, 1831–1880.
https://doi.org/10.1088/0951-7715/21/8/007

This peer-reviewed development gives a systematic quantum-Hénon Stokes
geometry with virtual turning points and new Stokes curves.  It raises the
novelty threshold for any action-collision interpretation, while remaining
distinct from the algebraic periodic-parameter Maxwell/Hill construction.
The same program is developed in Shudo's chapter
[*A role of virtual turning points and new Stokes curves in Stokes geometry
of the quantum Hénon map*](https://doi.org/10.1007/978-4-431-73240-2_21)
and in Shudo--Ikeda's 2016
[*Toward pruning theory of the Stokes geometry for the quantum Hénon
map*](https://doi.org/10.1088/0951-7715/29/2/375).

## C. Maxwell strata and critical-value monodromy

### 10. Looijenga 1974 — Foundational core, Level VI, grade A

Looijenga, E. (1974). The complement of the bifurcation variety of a simple
singularity. *Inventiones Mathematicae, 23*(2), 105–116.
https://doi.org/10.1007/BF01405164

This is foundational for discriminant complements and monodromy of critical
values in singularity theory.  It makes clear that critical-value
configuration maps and their braid monodromy are classical structures, not
Hénon discoveries.

### 11. Zvonkine and Lando 1999 — Core, Level VI, grade A

Zvonkine, D., & Lando, S. K. (1999). On multiplicities of the
Lyashko–Looijenga mapping on discriminant strata. *Functional Analysis and
Its Applications, 33*, 178–188.
https://doi.org/10.1007/BF02465202
MathNet record: https://www.mathnet.ru/eng/faa363

The Lyashko–Looijenga map sends a function/polynomial to its unordered
critical values, and this paper studies its multiplicities on discriminant
strata.  Thus a discriminant factor created by equal critical values is a
classical critical-value-map phenomenon.  The C33 increment cannot be the
bare existence of a Maxwell factor.

### 12. Yu 1999 — Core boundary, Level VI, grade A-

Yu, J. (1999). Galois group of Looijenga–Lyashko mapping. *Mathematische
Zeitschrift, 232*, 321–330.
https://doi.org/10.1007/s002090050517

This supplies direct prior art for symmetric/Galois monodromy of a
critical-value map.  Consequently the abstract occurrence of a symmetric
group on collision parameters is not novel.  What may still be new is the
exact Hénon polynomial \(P_9\), its source-locked modular proof, and its
coupling to Hill data.

### 13. Żołądek 2006 — Terminology boundary, Level VII, grade A

Żołądek, H. (2006). *The Monodromy Group*. Birkhäuser.
https://doi.org/10.1007/3-7643-7536-1

Section 4.4 distinguishes the caustic, where a critical point becomes
degenerate, from Maxwell strata, where several Morse critical points share a
critical value.  This exactly supports C33's distinction between the old
parabolic/orbit-cover discriminant and the new \(P_9\) equal-action factor.
The distinction is classical and must not be claimed as new.

### 14. van Manen 2007 — Boundary, Level VI, grade B+

van Manen, M. (2007). Maxwell strata and caustics. In *Singularities in
Geometry and Topology*, pp. 787–824. World Scientific.
https://doi.org/10.1142/9789812706812_0028

This chapter develops Maxwell and caustic strata for families of functions.
It supports the generic node language and the expectation that equal-value
strata can occur without Hessian degeneracy.  It does not contain the Hénon
period-five specialization or the arithmetic stability decoration.

**Supplementary Picard--Lefschetz boundary (not a separate numbered ledger
decision).** Vassiliev, V. A. (1995). Stratified Picard--Lefschetz theory.
*Selecta Mathematica, 1*, 597--621.
https://doi.org/10.1007/BF01589499
Author version: https://arxiv.org/abs/alg-geom/9505015

Vassiliev supplies the appropriate stratified vanishing-cycle framework.
It also marks a strict claim boundary: an ordinary equal-critical-value node
in the action image does not, by itself, prove a Picard--Lefschetz action for
the Hénon family.  Such a claim would require an additional local-family and
vanishing-cycle theorem, which Phase 2 does not authorize.

## D. Hill and Kummer boundaries

### 15. Bolotin and Treschev 2010 — Decisive core theorem, Level VI, grade A

Bolotin, S. V., & Treschev, D. V. (2010). Hill's formula. *Russian
Mathematical Surveys, 65*(2), 191–257.
https://doi.org/10.1070/RM2010v065n02ABEH004671
Author version: https://arxiv.org/abs/1006.1532

The paper proves multidimensional Hill formulas for discrete Lagrangian
systems, relating the Hessian of a periodic action to the monodromy
determinant.  The C33 Hill polynomial is an exact Hénon specialization, not a
new general identity.  The potentially new datum is its square class after
restriction to the equal-action branch pair.

### 16. Artal Bartolo, Cogolludo-Agustín, and Ortigas-Galindo 2014 — Kummer
boundary, Level VI, grade A

Artal Bartolo, E., Cogolludo-Agustín, J. I., & Ortigas-Galindo, J. (2014).
Kummer covers and braid monodromy. *Journal of the Institute of Mathematics
of Jussieu, 13*(3), 633–670.
https://doi.org/10.1017/S1474748013000297
Author version: https://arxiv.org/abs/1205.5427

The paper constructs braid monodromy for curves obtained through Kummer
covers.  It proves that “Kummer plus braid monodromy” is itself established
technology.  It does not attach a Kummer equation to a pair of equal-action
periodic Hénon branches using their Hill determinant.

## E. Current Hénon context

### 17. Gonchenko, Gonchenko, and Safonov 2021 — Context, Level VI, grade A-

Gonchenko, M., Gonchenko, S., & Safonov, K. (2021). Reversible perturbations
of conservative Hénon-like maps. *Discrete and Continuous Dynamical Systems,
41*, 4841–4876.
https://doi.org/10.3934/dcds.2020343

This recent conservative-Hénon source confirms continued activity around
reversibility and bifurcations.  It contains no exact action-value
discriminant or arithmetic Hill cover.

### 18. Julia Xénelkis de Hénon collective 2024 — Current field map, Level VII, grade A-

de Hénon, J. X. [collective pseudonym] (2024). Hénon maps: A list of open problems. *Arnold
Mathematical Journal, 10*, 585–620.
https://doi.org/10.1007/s40598-024-00252-x
Author version: https://arxiv.org/abs/2312.03907

The paper is signed under the collective pseudonym “Julia Xénelkis de
Hénon”; the arXiv record identifies the underlying contributor group.  This
multi-contributor field survey maps real, complex, algebraic, and arithmetic
Hénon questions.  The searched text did not reveal the C33
action-image-node/Hill-Kummer construction.  This is current-context evidence, not
proof of priority.

### 19. MacKay and Shardlow 1994 — Parabolic boundary, Level VI, grade A-

MacKay, R. S., & Shardlow, T. (1994). The multiplicity of bifurcations for
area-preserving maps. *Bulletin of the London Mathematical Society, 26*,
382–394. https://doi.org/10.1112/blms/26.4.382
Author PDF: https://people.bath.ac.uk/tjs42/assets/pubs/R1.pdf

The paper studies degeneracy of periodic points through
\(f_\mu^q(x)=x\) and \(\det(Df_\mu^q-I)=0\), including the period-five
area-preserving Hénon setting.  It is direct prior art for the
parabolic/caustic side of the discriminant.  It does not study equality of
actions between two distinct nonparabolic period-five branches.

### 20. Godwin 1984 — Maxwell-elimination boundary, Level VI, grade B+

Godwin, A. N. (1984). The precise determination of Maxwell sets for cuspoid
catastrophes. *International Journal of Mathematical Education in Science
and Technology, 15*, 167–182.
https://doi.org/10.1080/0020739840150205

Godwin uses an iterated/discriminant-of-a-discriminant calculation to locate
equal-critical-value Maxwell sets.  Therefore C33's resultant/discriminant
strategy is not methodologically new.  Godwin additionally uses real-root
tests to isolate the minima convention; C33 does not claim that its two
Morse critical points are minima.  The exact Hénon polynomial and the Hill
square class remain outside this source.

### 21. Qu and Xia 2024 — Current action context, Level VI, grade A-

Qu, H., & Xia, Z. (2024). Action and periodic orbits of area-preserving
diffeomorphisms. *Journal of Differential Equations, 391*, 246–264.
https://doi.org/10.1016/j.jde.2024.01.026

This current paper confirms that action-based periodic-orbit questions for
area-preserving diffeomorphisms remain active.  It supplies no exact Hénon
critical-value cover, Maxwell polynomial, or arithmetic Hill decoration.

## F. Assessed exclusions and near misses

### 22. Kim, Krieger, Postolache, and Szeto 2024 — Excluded

*Hénon maps with many rational periodic points*, arXiv:2412.01668.
https://arxiv.org/abs/2412.01668

This is highly relevant to arithmetic Hénon periodic points but does not use
a generating action, equal critical values, Hill determinants, or Kummer
decoration.

### 23. Zhang 2024 — Excluded

*Arithmetic properties of families of plane polynomial automorphisms*,
arXiv:2407.15952. https://arxiv.org/abs/2407.15952

The paper studies height and periodic-parameter questions in Hénon-type
families.  Its parameter geometry is a useful semantic control, but it does
not intersect the C33 invariant.

### 24. Huxford and Salter 2025 — Excluded after detailed assessment

Huxford, P., & Salter, N. (2025). Noninjectivity of the monodromy of certain
equicritical strata. *Geometriae Dedicata, 219*, 88.
https://doi.org/10.1007/s10711-025-01027-0

This recent paper distinguishes intrinsic from embedded monodromy and tracks
roots and critical points of polynomial strata.  Its equicritical strata fix
critical-point multiplicities; they are not Maxwell strata of equal critical
values.  It is a nearby modern monodromy source, not a C33 duplicate.

### 25. Artal Bartolo 2026 — Excluded/current survey

*Topology of complex plane curves: braid monodromy, local and global
problems*, arXiv:2604.26596. https://arxiv.org/abs/2604.26596

This current survey confirms active plane-curve braid-monodromy work but has
no Hénon action or stability-determinant specialization.

### 26. Hénon--Heiles periodic-orbit literature — Excluded family

The Hénon--Heiles Hamiltonian flow is a different dynamical system.  Papers
on its periodic-orbit bifurcations, while discoverable under the same name,
do not support claims about the area-preserving Hénon map.

## Corpus-level overlap ruling

The corpus establishes direct prior art for every separate ingredient:

\[
\begin{aligned}
&\text{period-five orbit cover} &&\text{Endler--Gallas/Brison--Gallas},\\
&\text{Hénon discrete action and equal-action saddles} &&\text{Kook--Meiss/Shudo},\\
&\text{Maxwell critical-value strata} &&\text{Looijenga/Żołądek/van Manen},\\
&\text{critical-value Galois monodromy} &&\text{Zvonkine--Lando/Yu},\\
&\text{Hill action-Hessian identity} &&\text{Bolotin--Treschev},\\
&\text{Kummer plus braid monodromy} &&\text{Artal et al.}
\end{aligned}
\]

No audited source combines these into the exact period-five Hénon object

\[
P_9(A)=0,
\qquad
u^2=h_1h_2,
\]

with \(h_i=\det(I-DH_A^5)\) on the two equal-action branches.  The resulting
priority statement remains search-bounded.
