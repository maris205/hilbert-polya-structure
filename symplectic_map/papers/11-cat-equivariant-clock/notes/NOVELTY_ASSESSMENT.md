# Novelty Assessment

## Verdict

**GO_SCOPED_BOUNDARY_NOTE_LOW_NOVELTY**.

Safe title:

**An Equivariant-Zeta Audit of Cat-Map Centralizer Quotients**.

Required positioning:

> On the regular centralizer torsor, the fixed-point Burnside zeta retains
> the source order but restores source multiplicity under cardinality, the
> integral orbit-counting zeta has only quotient period one, and the stronger
> $G$-permutation/enhanced classes retain the translating element only inside
> a modulus-dependent labelled coefficient category.  Orbifold and free
> stack quotients collapse to one fixed point.

Overall novelty score: **2/10**.  The two competing Burnside-ring zetas, the
$G$-permutation invariant, the enhanced Burnside carrier, the orbifold maps,
and the quotient shortening/gluing mechanisms are prior art.  The defensible
delta is the exact specialization of those definitions to the Paper-10
centralizer torsor and the resulting Route-A retention--compression ledger.
No constituent construction is claimed as new.

The note is scientifically useful because Paper 10 explicitly left this
boundary open, and because “equivariant zeta retains information” is too
coarse a statement: three inequivalent constructions retain three different
levels of information.  The note must remain a boundary audit, not a new
equivariant-zeta theory.

Search cutoff: **2026-08-15 UTC**.  The bounded search covered the named
primary sources, citing and publication records, quotient-orbit and
finite-field quotient literature, and 2024--2026 equivariant Ruelle/Fried
work.  No absence claim or historical-priority inference is permitted.

## Definition-sensitive novelty map

| Construction | What it retains on $X_q\simeq G_q$, $\phi_q=L_{a_q}$ | What it loses or costs | Novelty |
|---|---|---|---:|
| 2008 point-order/fixed-point rational Burnside zeta, revisited in 2015 | exact source order $r_q$ in the support; regular orbit coefficient $\mathbf u_q$ | does not retain the exact generator $a_q$; cardinality gives multiplicity $m_q$; rational Burnside exponent | 0/10 |
| 2015 orbit-order integral Burnside zeta | free orbit type $[G_q/1]$ and its marks | only quotient period $1$; no source order | 0/10 |
| 2013 $G$-permutation zeta | twisted stabilizer $\langle(1,a_q^{-1})\rangle$ and hence exact $a_q$ for a fixed effective labelled regular action | lives in a $q$-dependent Grothendieck ring; modulo the action kernel in non-effective actions | 0/10 |
| 2018 enhanced Burnside class | irreducible class $\widehat X_{1,1,a_q,1}$; exact $a_q$ for abelian labelled $G_q$ | no isotropy character beyond the trivial one on a free torsor; still a varying coefficient ring | 0/10 |
| 2015 orbifold reductions | point version keeps $r_q$ with exponent $1/r_q$; orbit version gives one factor | neither gives a unit-exponent source-period factor | 0/10 |
| enhanced orbifold/inertia zeta | identity sector of the free quotient | all nonidentity sectors empty; result $(1-t)^{-1}$ | 0/10 |
| quotient stack/action groupoid | Morita class of a point; induced map up to $2$-isomorphism | no $r_q$, $a_q$, $n_q$, or $q$ | elementary |
| combined retention--compression A0 certificate | exact comparison of all rows on one arithmetic torsor family | scoped to named definitions; not universal | 2/10 |

The more general finite-abelian-$C$-set formula

$$
X=\coprod_Kn_K(C/K),
\qquad
d_K=[\langle a\rangle:\langle a\rangle\cap K]
$$

is likewise an elementary specialization of these prior definitions.  Its
source product, quotient product, Burnside exact-period classes,
$(\mathbb Z\times C)$ stabilizers, and $BK$ inertia sectors are not claimed
as new structure.  The frozen $C_6/C_2\sqcup C_6/C_3$ example is a diagnostic
counterexample, not a novelty claim.

## Dominant primary-source collisions

### 1. Gusein-Zade--Luengo--Melle-Hernández (2015)

S. M. Gusein-Zade, I. Luengo, and A. Melle-Hernández,
“On an equivariant version of the zeta function of a transformation,”
*Arnold Mathematical Journal* **1**(2), 127--140 (2015), DOI
`10.1007/s40598-015-0012-8`, arXiv `1203.3344`.

This is the strongest direct collision.  It explicitly distinguishes the
equivariant Lefschetz number that counts fixed points from the alternative
one that counts fixed $G$-orbits.  Its example
$X=(G/H)\times\mathbb Z_k$ with a return twist gives different first
nonzero orders in $X$ and $X/G$.  It defines the integral orbit-order
Burnside zeta and both orbifold reductions.  It also states that when the
monodromy belongs to the symmetry group, the induced quotient action is
trivial and the orbit-order equivariant zeta reduces to period one.

Paper 11 is a finite regular-torsor specialization of these definitions.  It
may derive the exact formulas, but may not call the point/orbit distinction,
the Burnside series, the additive/exponentwise orbifold reduction, or the
clock collapse new.

The rational point-order predecessor is already explicit in S. M.
Gusein-Zade, I. Luengo, and A. Melle-Hernández, “An equivariant version of
the monodromy zeta function,” *Geometry, Topology, and Mathematical Physics*,
AMS Translations Series 2 **224**, 139--146 (2008), arXiv `0803.3708`.  It
uses the Burnside ring tensored with $\mathbb Q$, equivariant Lefschetz
numbers, and the Burnside $\lambda$/power structure.  This blocks any claim
that the rational point-order construction first appeared in 2015 or in
Paper 11.

### 2. Gusein-Zade (2013): the stronger $G$-permutation invariant

S. M. Gusein-Zade, “On an equivariant analogue of the monodromy zeta
function,” *Functional Analysis and Its Applications* **47**(1), 14--20
(2013), arXiv `1207.2282`.

This paper defines the equivariant zeta as a virtual finite or locally finite
$G$-permutation, equivalently a $(\mathbb Z\times G)$-set, determined by all
twisted equivariant Lefschetz numbers $L^G(g\phi^m)$.  Irreducible classes are
parametrized by triples $(H,m,\alpha)$ with
$\alpha\in C_G(H)/H$.

For the regular centralizer torsor the class is not merely the point-order
series.  It is the actual $G_q$-permutation with stabilizer
$\langle(1,a_q^{-1})\rangle$, triple $(1,1,a_q^{-1})$.  It therefore records
$a_q$ exactly only because the regular action is effective and $G_q$ is held
fixed as a labelled group.  This construction must be kept distinct from the
2015 fixed-point and orbit-counting Burnside power series.

### 3. Ebeling--Gusein-Zade (2018): enhanced Burnside carrier

Wolfgang Ebeling and Sabir M. Gusein-Zade, “Enhanced equivariant Saito
duality,” *Journal of Algebra and Its Applications* **17**(10), 1850181
(2018), DOI `10.1142/S0219498818501815`, arXiv `1506.05604`.

The enhanced Burnside ring is generated by finite $G$-sets equipped with a
$G$-equivariant bijection and isotropy characters.  Its irreducible classes
carry $(H,k,\bar h,\bar\alpha)$.  It also defines an enhanced orbifold zeta by
fixed sectors and centralizer quotients.

For a free regular torsor, $H=1$, $k=1$, and the character is forced to be
trivial.  The enhanced class remembers $a_q$, but its orbifold zeta has only
the identity sector and is the one-fixed-point factor.  Both the positive
retention and negative orbifold collapse are direct specializations.

### 4. Zegowitz (2017): shortening and gluing

Stefanie Zegowitz, “Closed orbits in quotient systems,” *Ergodic Theory and
Dynamical Systems* **37**(7), 2337--2352 (2017), DOI
`10.1017/etds.2016.3`, arXiv `1502.02693`.

Zegowitz separates surviving, gluing, and shortening phenomena for a finite
group action commuting with a map.  Her exact formulas use
$|\mathcal O_T(x)\cap\mathcal O_G(x)|$ for shortening and the ratio
$|\mathcal O_G(x)|/|\mathcal O_T(x)\cap\mathcal O_G(x)|$ for gluing.
Paper 11's values $r_q$ and $m_q$ are a direct regular-action corollary, not a
new quotient-orbit theorem.

### 5. Walton (2018): finite-field quotient/twist boundary

Laura Walton, “Counting periodic points on quotient varieties over
$\mathbb F_q$,” *Journal of Number Theory* **189**, 202--223 (2018), DOI
`10.1016/j.jnt.2018.03.023`, arXiv `1705.09034`.

Walton relates periodic points on $V/G$ to periodic points on $V$, twists,
and subgroup quotients for quasiprojective varieties over finite fields.  Her
basic lift says a quotient-periodic point has a periodic lift after multiplying
the quotient period by the order of a correcting group element.  This
supports the general period-shortening boundary.

It is not a direct theorem about the finite sets $X_q$ over composite residue
rings.  Paper 11 neither constructs varieties/twists nor extends Walton's
theorem.

### 6. Miles (2017): acting-group zeta boundary

Richard Miles, “A dynamical zeta function for group actions,” *Monatshefte
für Mathematik* **182**(3), 683--708 (2017), DOI
`10.1007/s00605-016-0909-x`, arXiv `1506.08555`.

Miles defines a zeta using fixed sets of finite-index subgroups of a finitely
generated acting group and derives a stabilizer-sensitive product formula.
The paper explicitly tacitly assumes that the acting group is infinite.
Therefore it is not the finite-centralizer zeta used here.  Replacing $G_q$
by an infinite presentation such as $\mathbb Z\times G_q$ would add a chosen
acting group and its subgroup-growth data; it would not be an intrinsic
repair of the finite quotient.

## 2024--2026 frontier screen

The closest current items located were:

- Mohammad Reza Rahmati, “Mirror Symmetry, Zeta Functions and Mackey
  Functors,” *Contemporary Mathematics* **5**(2), 1820--1842 (2024), DOI
  `10.37256/cm.5220244455`;
- David Ayala, Aaron Mazel-Gee, and Nick Rozenblyum, “Symmetries of the
  cyclic nerve,” *Advances in Mathematics* **466**, 110170 (2025), DOI
  `10.1016/j.aim.2025.110170`, arXiv `2405.03897`;

- Peter Hochs and Hemanth Saratchandran, “A Ruelle dynamical zeta function
  for equivariant flows,” arXiv `2303.00312`;
- Peter Hochs and Hemanth Saratchandran, “An equivariant Guillemin trace
  formula,” arXiv `2502.08367` (2025); and
- Peter Hochs and Christopher Pirie, “The Equivariant Fried Conjecture for
  Suspension Flow of an Equivariant Isometry,” arXiv `2507.06792` (2025);
  and
- Sabir M. Gusein-Zade, “Monodromy Zeta Functions in Singularity Theory,”
  in *Handbook of Geometry and Topology of Singularities VIII*, 289--316
  (Springer, 2026), DOI `10.1007/978-3-031-99571-2_7`.

Rahmati concerns orbifold cohomological zeta/L-series and Mackey functors;
Ayala--Mazel-Gee--Rozenblyum concern cyclic nerves and Hochschild homology;
the Hochs papers concern proper/cocompact smooth actions, flows, trace
formulas, and analytic torsion; and the 2026 chapter is a survey of mature
monodromy-zeta notions.  None supplies a closer finite
regular-torsor/Burnside collision or an intrinsic prime selector for the
Paper-10 modulus family.  They are frontier context only; Paper 11 invokes
none of their analytic, cohomological, or higher-categorical hypotheses.

The search also screened 2024--2026 work using “orbifold zeta” in arithmetic
geometry, singularity mirror symmetry, representation theory, and Selberg or
Ruelle settings.  Those meanings are not interchangeable with the finite-set
transformation zetas frozen here.

## Exact safe delta

The only defensible contribution is the following combined audit.

1. Specialize the three inequivalent equivariant carriers to the exact
   Paper-10 torsor.
2. Derive the finite-abelian-$C$-set hierarchy by orbit type and freeze the
   effective $C_6/C_2\sqcup C_6/C_3$ no-period-six counterexample.
3. Prove the four scalar reduction formulas.
4. Show that the stronger permutation/enhanced carriers retain $a_q$ only in
   a labelled $q$-dependent category.
5. Show that a quotient stack may retain $BK$ inertia sectors while all
   induced dynamics is static; the free torsor specializes to a point.
6. Bind the result to prime and composite controls, including period
   collisions $r_2=r_4$ and $r_6=r_9$.
7. Record the Route-A outcome without excluding unexamined transfer,
   representation-valued, weighted, or analytic constructions.

## Safe positioning and forbidden claims

Use:

- **point-order rational Burnside zeta** for the $L^G$ construction;
- **orbit-order integral Burnside zeta** for the $\widetilde L^G$
  construction;
- **$G$-permutation zeta** for the $(\mathbb Z\times G)$-set construction;
- **enhanced Burnside class** only for the character-equipped carrier;
- **orbifold reduction** only after naming which equivariant Lefschetz
  sequence is reduced;
- **free action-groupoid/quotient-stack collapse** only under Morita and
  $2$-isomorphism invariance; and
- **retention--compression tradeoff in this torsor family**, not a universal
  no-go theorem.

Never use “the equivariant zeta” without a qualifier.  Never claim “first,”
“new Burnside zeta,” “new orbifold zeta,” “new stacky zeta,” “all equivariant
refinements fail,” “the stronger invariant forgets $A$,” “the ambient group
is an intrinsic modulus clock,” “constructs the Riemann Euler product,” or
historical priority.

## Decision rationale

`GO` rather than `MERGE` is justified because this is the fifth and terminal
paper in the batch and resolves a deliberately preserved boundary with a
definition-sensitive result: one refinement retains period, one retains
orbit type, and a third retains the twist, but none yields the requested
one-factor intrinsic prime/modulus clock under the audited standard
reductions.

`GO` does not imply high novelty.  The note should be short, explicit about
prior art, and framed as an audit/synthesis.  Any attempt to introduce a new
general equivariant, stacky, analytic, or representation-valued zeta would
require a different source lock and is forbidden here.

## Independent-review boundary

This author assessment is not an independent proof or novelty review.  A
fresh reviewer must bind the final seven-file source-lock package, check the
three definitions separately, verify the signs/twists $a_q$ versus
$a_q^{-1}$, confirm the four scalar exponents, and reject any statement that
the free quotient-stack result covers non-Morita-invariant presentation data.
