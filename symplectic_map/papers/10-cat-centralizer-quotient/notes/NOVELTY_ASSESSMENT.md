# Novelty Assessment

## Verdict

**GO_SCOPED_NEGATIVE_NOTE_LOW_NOVELTY**.

Safe title:

**A Centralizer-Quotient Audit for Cat-Map Torsion Shells**.

Required positioning:

> A cyclic-vector stratum of every modulus is a torsor under the full
> finite-module centralizer, but quotienting by that group also quotients out
> the cat map itself; the resulting one-point dynamics has no modulus clock,
> and the symplectic centralizer leaves norm-class multiplicity.

Overall novelty score: **3/10**.  The centralizer, cyclic-matrix, finite-ring,
prime-lattice, Hecke-symmetry, and equivariant-zeta ingredients have strong
prior collisions.  The defensible delta is their use in one tightly scoped
Route-A decision: the exact multiplicity-one set quotient is proved, then
separated from a genuine quotient-dynamical Euler factor, from symplectic
symmetry, and from prime specificity.

This is sufficiently distinct from Paper 9 to justify a short negative note:
Paper 9 left the centralizer route genuinely open; Paper 10 closes the coarse
full-centralizer version and records the richer equivariant/stacky version as
outside scope.  It is not sufficiently novel to support a new centralizer or
zeta theory claim.

Search cutoff: **2026-08-15 UTC**.  The bounded search covered primary
literature on rational-lattice cat-map symmetries, cyclic matrices and
commutants, quantum Hecke centralizers, finite-ring cycle structure,
equivariant/orbifold zeta functions, group-action zeta functions, and
2024--2026 cat-map work.  Absence from this search is not evidence of
historical priority.

## Core-claim assessment

| Component | Novelty | Closest collision | Safe delta |
|---|---:|---|---|
| A nonscalar $2\times2$ cat matrix has commutant $R[A]$ when a cyclic vector exists | 0.5/10 | Baake--Neumärker--Roberts (2013) explicitly uses cyclic vectors to identify commuting rings over rational lattices; over $\mathbb F_p$ it states $S(A)=\mathbb F_p[A]^\times$ | Give the two-line all-$q$ proof for this fixed matrix; claim no theorem novelty |
| $\mathrm{CV}_q$ is a torsor under $R_q[A]^\times$ | 2/10 | Elementary cyclic-module/unit-orbit consequence; BNR's finite-ring symmetry example is very close | Make the exact torsor map and determinant criterion explicit for the audit |
| Prime full-shell centralizer strata are $1/3/2$ in inert/split/ramified cases, while the reversor can merge the split eigenlines | 1/10 | BNR §4/Table 1 gives the finite-field normal forms, symmetry groups, and reversing groups | Record only the induced three-layer orbit-stratum corollary and discard fractions |
| The symplectic centralizer leaves norm classes | 2/10 | Kurlberg--Rudnick use norm-one modular centralizers as the Hecke symmetry group; BNR also separates determinant-one subgroups | Contrast the full finite-module centralizer with $\mathrm{SL}_2=\mathrm{Sp}_2$ and bind exact class counts |
| Quotienting by a group that contains $A$ makes induced $A$ dynamics trivial | 1/10 | General quotient-action fact; Gusein-Zade--Luengo--Melle-Hernández distinguish orders in $X$ from orders in $X/G$ and develop finer equivariant/orbifold zetas | Apply the fact to prevent a one-class set quotient from being advertised as a new clock |
| The same one-class quotient holds for composite $q$ | 2/10 | BNR treats rational lattices and prime powers; Tan--Li treats exact cycle lifting over $\mathbb Z_{p^k}$ | Use four frozen composites as a proves-too-much control, not as new finite-ring theory |
| Combined A0 failure certificate | 3/10 | No exact HP-Dynamics decision package was located; all ingredients are nevertheless classical or elementary | Close Paper 9's explicit escape with an honest full-GL/symplectic/coarse-quotient boundary |

## Dominant primary-source collisions

### 1. Baake--Neumärker--Roberts (2013): direct symmetry collision

Michael Baake, Natascha Neumärker, and John A. G. Roberts,
“Orbit structure and (reversing) symmetries of toral endomorphisms on rational
lattices,” *Discrete and Continuous Dynamical Systems A* **33**(2), 527--553
(2013), DOI
[`10.3934/dcds.2013.33.527`](https://doi.org/10.3934/dcds.2013.33.527),
arXiv:[`1205.1003`](https://arxiv.org/abs/1205.1003).

This is the strongest collision.  Section 4 and its finite-field table give
the scalar, Jordan, split, and irreducible conjugacy types and their symmetry
groups.  It states that a cyclic matrix has commutant $\mathbb F_p[M]$ and
symmetry group $\mathbb F_p[M]^\times$; in dimension two every nonscalar
matrix over $\mathbb F_p$ is cyclic.  Its finite-ring Example 2 explicitly
uses a cyclic vector to identify a commuting ring over $\mathbb Z/8\mathbb Z$
and then separates the determinant-one subgroup.  Its Arnold-cat appendix
also gives prime-power periods and cycle polynomials.

Paper 10 may derive its fixed-matrix torsor and quotient corollaries, but may
not call the centralizer rings, symmetry groups, finite-field types, or
prime-power setting new.  BNR also distinguishes local rational-lattice
symmetries from global toral symmetries.  The full $C_q$ used here is therefore
honestly described as a $q$-dependent local pseudo-symmetry group; the note
does not claim that all of it is the reduction of one fixed global
centralizer.

### 2. Kurlberg--Rudnick (2000): norm-one/Hecke collision

Pär Kurlberg and Zeév Rudnick, “Hecke theory and equidistribution for the
quantization of linear maps of the torus,” *Duke Mathematical Journal*
**103**(1), 47--77 (2000), DOI
[`10.1215/S0012-7094-00-10314-6`](https://doi.org/10.1215/S0012-7094-00-10314-6),
arXiv:[`chao-dyn/9901031`](https://arxiv.org/abs/chao-dyn/9901031).

They construct a commutative group of quantum symmetries from norm-one
elements of a quadratic order modulo the quantization modulus.  These
elements lie in $\mathrm{SL}_2$ and commute with the cat map.  Their local
analysis includes split, inert, and ramified norm behavior.  This directly
prevents Paper 10 from presenting a norm-one centralizer or its arithmetic
case split as new; it also makes the full-$\mathrm{GL}_2$ versus symplectic
distinction mandatory.

The present project does not quantize, construct Hecke operators, or claim
anything about eigenfunction equidistribution.

### 3. Gusein-Zade--Luengo--Melle-Hernández (2015): quotient-zeta collision

S. M. Gusein-Zade, I. Luengo, and A. Melle-Hernández, “On an equivariant
version of the zeta function of a transformation,” *Arnold Mathematical
Journal* **1**(2), 127--140 (2015), DOI
[`10.1007/s40598-015-0012-8`](https://doi.org/10.1007/s40598-015-0012-8),
arXiv:[`1203.3344`](https://arxiv.org/abs/1203.3344).

They distinguish periodic order in $X$ from periodic order in the coarse
quotient $X/G$, define equivariant Lefschetz/zeta data with Burnside-ring
coefficients, and discuss two orbifold versions.  In particular, their
framework makes clear that the coarse quotient can lose dynamical order while
finer equivariant data retains orbit and stabilizer information.

Therefore Paper 10's observation that $A\in C_q$ acts trivially on
$\mathrm{CV}_q/C_q$ is not a new zeta theorem.  The safe contribution is only
to apply this general fact as an A0 gate.  Burnside, orbifold, stacky, and
twisted-sector refinements remain outside scope and must not be declared
impossible.

### 4. Prime-lattice and finite-lattice orbit products

Gregory Gaspari, “The Arnold cat map on prime lattices,” *Physica D* **73**,
352--372 (1994), DOI
[`10.1016/0167-2789(94)90105-8`](https://doi.org/10.1016/0167-2789(94)90105-8),
already gives the prime-lattice common-period and orbit-decomposition setting.

Michael Baake, John A. G. Roberts, and Alfred Weiss, “Periodic orbits of
linear endomorphisms on the 2-torus and its lattices,” *Nonlinearity* **21**,
2427--2446 (2008), DOI
[`10.1088/0951-7715/21/10/012`](https://doi.org/10.1088/0951-7715/21/10/012),
arXiv:[`0808.3489`](https://arxiv.org/abs/0808.3489), develops finite and
rational-lattice orbit statistics and Euler products.

Paper 10 claims neither a new prime-lattice classification nor a new
finite-lattice Euler product.

### 5. Group-action zeta boundary

Richard Miles, “A dynamical zeta function for group actions,”
arXiv:[`1506.08555`](https://arxiv.org/abs/1506.08555) (2015), introduces a
zeta function for group actions with a product formula connected to the zeta
of the acting group.  It is broader than a single coarse quotient and is not
implemented here.  It reinforces the need to say exactly which group-action
or quotient zeta convention is being used.

### 6. Current finite-ring and finite-permutation frontier

Kai Tan and Chengqing Li, “The Graph Structure of a Class of Permutation Maps
over Ring $\mathbb Z_{p^k}$,” arXiv:[`2506.20118`](https://arxiv.org/abs/2506.20118)
(2025 preprint), develops exact cycle-length distributions and lifting over
prime-power rings with the cat map as an example.  This blocks broad claims
of new composite/prime-power cat-map cycle analysis.

Aryaman Chandra, “Arithmetic Landscape Functions of a Discrete Cat Map,”
arXiv:[`2607.24857`](https://arxiv.org/abs/2607.24857) (2026 preprint), gives
finite-torus Green-function and cycle-product identities for the discrete cat
map.  It blocks generic claims of a new finite-permutation determinant or
cycle-product packaging.  Paper 10 uses neither its Green function nor a
spectral landscape.

The 2023--2026 smooth-centralizer literature was screened but concerns
rigidity of diffeomorphism centralizers near toral automorphisms, not the
fixed finite-module torsor and coarse quotient.  It is background rather than
a direct support for the theorem.

## Claim extraction and search routes

The search tested these claims separately:

1. commutants of cyclic matrices over $\mathbb Z/q\mathbb Z$;
2. transitivity of cat-map finite centralizers on cyclic vectors;
3. split/inert/ramified centralizer orbits on $p$-torsion;
4. norm-one or symplectic cat-map centralizers;
5. zeta functions after quotienting a map by a commuting finite group;
6. groupoid, Burnside, orbifold, and twisted-sector refinements;
7. composite and prime-power cat-map cycle structure; and
8. 2024--2026 finite-torus cat-map determinant work.

Representative formulations included “cat map rational lattice centralizer,”
“cyclic vector commutant over $\mathbb Z/n\mathbb Z$,” “norm one Hecke cat
map,” “equivariant zeta quotient transformation,” “group action dynamical
zeta,” and current arXiv variants.  No source located packaged the same
Route-A failure certificate, but that absence does not increase the novelty
of the underlying mathematics.

## Safe positioning and forbidden claims

Use the following boundaries:

- Say **full finite-module centralizer torsor**, not a new canonical
  symplectic quotient.
- Say **coarse quotient has one class and identity induced dynamics**, not
  that it creates a primitive orbit with period $\log q$.
- Say **the substitution $z=q^{-s}$ is external**, not that a quotient zeta
  theorem produces a Riemann local factor.
- Say **the symplectic centralizer leaves norm classes**, not that Hecke
  symmetries fail or are irrelevant.
- Say **three separate layers: symplectic centralizer, full local centralizer,
  and reversing group**, not one undifferentiated “symmetry quotient.”
- Say **$q$-dependent local pseudo-symmetries**, not a fixed global torus
  centralizer action.
- Say **cyclic stratum**, not full shell, at split and ramified primes.
- Say **same mechanism for composites**, not that all arithmetic quotient
  constructions are impossible.
- Say **scoped low-novelty audit**, never “first,” “discover,” “new
  centralizer classification,” “new equivariant zeta,” “new Hecke theory,”
  “construct the Riemann dynamics,” or “historical priority.”

## Decision rationale

`GO` is preferable to `MERGE` because the centralizer route was an explicit,
substantive outside-scope escape in Paper 9 and its closure requires two new
distinctions: full $\mathrm{GL}_2$ versus symplectic centralizers, and
multiplicity-one set quotient versus trivial quotient dynamics.  `KILL` is
unnecessary because these distinctions yield a complete negative theorem and
a clean handoff to a genuinely different equivariant/stacky question.

The note must remain short and transparent.  Any attempt to expand it into a
new centralizer, Hecke, equivariant-zeta, or quantization theory would collide
with prior art and exceed the frozen claim.

## Independent-review boundary

This author assessment is not an independent novelty or proof review.  A
fresh reviewer must check all final design hashes, primary-source uses, the
local norm image at $2$ and $5$, and the coarse/equivariant quotient boundary
before any code or registered execution is authorized.
