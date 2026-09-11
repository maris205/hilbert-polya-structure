# Owner-first search log: algebraic replacement2

**Search date:** 2026-09-02 UTC.  
**Scope:** thirteen literal systems in `SCOUT.md`.  
**External status:** `HOLD_EXTERNAL`.  
**Interpretation:** an indexed miss is a bounded non-hit, never a novelty or
priority statement.

## Method and boundary

The search was run before any candidate could be called a survivor.  It used
exact formulas, coordinate aliases, the named action/algorithm, and the proof
engine exposed by the exact data.  Technical conclusions below rely on author
manuscripts, journal/publisher records, or other primary sources.  Search
snippets, repositories, blogs, MathOverflow, Wikipedia, and aggregators were
used only as locators and receive no evidentiary weight.

The search was English-heavy and bounded to indexed web search, arXiv, and
publisher pages available on the audit date.  It did not exhaust books,
theses, non-English literature, unindexed proceedings, or every birational or
representation-theoretic alias.  A “literal non-hit” below means only that the
listed queries did not return the exact finite self-map.  Since the pool has no
survivor, no absence claim is required.

## Queries actually run

### Character, symmetric, and mean maps

```text
"x + chi(x)" finite field dynamics quadratic character
"x+chi(x)" finite field map quadratic character
elementary symmetric map (xy,x+y) finite field dynamics functional graph
arithmetic harmonic mean map finite field dynamics
"(xy, x+y)" dynamical system finite field
"(x+y,xy/(x+y))" finite field
"arithmetic-harmonic mean" finite fields iteration
Vieta map elementary symmetric functions quotient S2 finite fields
site:arxiv.org consecutive quadratic residues runs modulo prime longest run
quadratic residues consecutive runs modulo p primary paper
site:doi.org runs of consecutive quadratic residues modulo prime
quadratic character patterns finite fields consecutive residues paper
```

### Group actions, cubic surfaces, cluster maps, and partitions

```text
site:arxiv.org Hurwitz action braid group tuples finite groups orbits
site:arxiv.org Markoff triples finite fields Vieta involutions Bourgain Gamburd Sarnak
site:arxiv.org rank two cluster map y (1+y^2)/x dynamics QRT
site:arxiv.org Kreweras complementation orbit counting
site:arxiv.org "x_{n+2}x_n" "x_{n+1}^2+1"
site:arxiv.org "x_{n+2} x_n = x_{n+1}^2 + 1" cluster
site:arxiv.org Fomin Zelevinsky rank 2 cluster algebras recurrence
site:arxiv.org QRT map finite fields singularity confinement functional graph
Reiner Stanton White cyclic sieving Kreweras complement noncrossing partitions original paper
site:arxiv.org cyclic sieving noncrossing partitions Kreweras complement
Kreweras complement order 2n orbit sizes noncrossing partitions paper
site:doi.org Kreweras complementation noncrossing partitions cyclic sieving
```

### Algorithms, covariants, Newton maps, and matrix maps

```text
site:arxiv.org finite field Newton map functional graph Newton method dynamics
site:arxiv.org polynomial Euclidean algorithm finite fields average case
site:arxiv.org squarefree factorization gcd f f' finite fields algorithm
site:arxiv.org Hessian map binary cubic forms iteration invariants
"Newton map" "finite field" dynamics polynomial
"Newton's method" over finite fields dynamics
site:arxiv.org Newton map finite fields arithmetic dynamics
site:arxiv.org finite field functional graph rational maps Newton
"A A^T A" finite field matrix map iteration
"AA^T A" matrix dynamics
Gram map finite field matrices A transpose A dynamics
polynomial matrix map functional graph finite fields
site:arxiv.org binary cubic Hessian discriminant invariant theory
site:arxiv.org iteration Hessian map cubic forms dynamics
binary cubic form Hessian (3ac-b^2) discriminant primary source
site:arxiv.org Hessian map elliptic curves moduli dynamics
site:arxiv.org "gcd(f,f')" squarefree factorization finite field
site:arxiv.org square-free factorization finite fields derivative gcd polynomial
site:doi.org squarefree factorization finite fields gcd derivative algorithm
square-free factorization finite fields original paper Yun algorithm
```

## Primary-source findings and decision effects

### `QCD`: exact map not found; temporal engine is an owned residue-run problem

The exact strings `x+chi(x)` and `x+χ(x)` did not return a paper treating the
literal functional graph.  That is only a bounded literal non-hit.

The exposed temporal engine has a substantial primary literature:

- Anna Oganesyan,
  [*Quadratic residue patterns, algebraic curves and a K3 surface*](https://arxiv.org/abs/2403.16326),
  studies prescribed consecutive residue/nonresidue patterns and their exact
  or asymptotic counts via algebraic curves.
- Patrick Hummel,
  [*On consecutive quadratic non-residues: a conjecture of Issai
  Schur*](https://arxiv.org/abs/math/0305298), proves a theorem about the
  greatest run of consecutive nonresidues modulo a prime.
- [*Exact Frequencies of Consecutive Quadratic Residue and Nonresidue Patterns
  Modulo a Prime*](https://arxiv.org/abs/2607.11068) gives exact length-two and
  length-three character-pattern frequencies.  This is precisely the level of
  character summation behind `QCD`'s 2-cycle and double-fibre formulas, though
  it does not discuss `QCD` as a map.

**Effect:** no direct-map kill is asserted.  The candidate is killed because
its missing all-prime temporal theorem is exactly the longest-run/pattern
problem, while its short-pattern structural formulas are standard direct
inputs.  It is owner-compressed to one axis.

### `ESP`: bounded exact-map non-hit; inverse theorem is the symmetric quotient

Queries for `(xy,x+y)`, “elementary symmetric map,” “Vieta map,” and finite
field dynamics did not locate a primary source iterating this exact ordered
plane map.  The hits concerned general symmetric polynomials and unrelated
finite-field varieties.

The complete inverse result needs no external theorem beyond the elementary
identity that `(x,y)` are the ordered roots of `T^2-vT+u`.  It is the quotient
of `A^2` by the transposition action, with discriminant stratification.

**Effect:** the bounded miss gives no novelty credit.  The standard inverse
axis plus the irregular exact temporal data is insufficient, so the kill is
`KILL_WEAK_TEMPORAL`, not `KILL_DIRECT_OWNER`.

### `AHP`: bounded exact totalization non-hit; nearest mean literature differs

Searches for the exact update `(x+y,xy/(x+y))` over finite fields did not find
a primary exact-map graph paper.  Arithmetic--harmonic mean literature usually
uses the normalized update

```text
((x+y)/2, 2xy/(x+y)),
```

not the literal totalized update audited here.  Finite-field mean searches
also found Bátorová--Gajović,
[*Arithmetic-geometric mean sequences over finite fields*](https://arxiv.org/abs/2501.00577),
which is a different mean pair and does not own `AHP`.

**Effect:** no direct owner is claimed.  The inverse quadratic and singular
fibre are elementary; exact temporal profiles vary sharply with `p`.
`KILL_WEAK_TEMPORAL` follows independently of the bounded owner result.

### `CCS`: early theorem-size kill

No owner conclusion is needed.  The literal definition itself proves that all
nonfixed states enter the fixed set in one step.  Searches would not repair a
missing temporal axis.

**Effect:** `KILL_THEOREM_THIN` before any novelty inference.

### `HUR`: direct named-action owner

Tetsuya Ito,
[*Finite orbits of Hurwitz actions on braid systems*](https://arxiv.org/abs/0912.0405),
defines the natural braid-group Hurwitz action on products and studies finite
orbits, including the length-two setting.  Jean Michel,
[*Hurwitz action on tuples of Euclidean reflections*](https://arxiv.org/abs/math/0410313),
is another primary action/orbit source.

The audited map `(a,b)->(b,b^{-1}ab)` is the standard two-strand Hurwitz
generator, not merely an analogy.

**Effect:** direct action ownership plus fibre one gives
`KILL_DIRECT_ACTION_OWNER`.

### `MRK`: direct Markoff/Vieta-action owner

Jean Bourgain, Alex Gamburd, and Peter Sarnak,
[*Markoff Triples and Strong Approximation*](https://arxiv.org/abs/1505.06411),
study the group of morphisms generated by Vieta involutions on congruence
solutions of the Markoff equation and related affine cubic surfaces.

The audited carrier is that congruence surface, and the rotor is a coordinate
rotation composed with its Vieta involution.

**Effect:** direct family/action ownership.  Since the map is bijective, the
inverse/fibre axis contributes only the explicit inverse and fibre one.
`KILL_DIRECT_ACTION_OWNER`.

### `CLU`: rank-two cluster recurrence and permanent matrix-power engine

Primary cluster sources checked were:

- Sergey Fomin and Andrei Zelevinsky,
  [*Cluster algebras I: Foundations*](https://arxiv.org/abs/math/0104151);
- Paul Sherman and Andrei Zelevinsky,
  [*Positivity and canonical bases in rank 2 cluster algebras of finite and
  affine types*](https://arxiv.org/abs/math/0307082);
- Sergey Fomin and Andrei Zelevinsky,
  [*Cluster algebras II: Finite type classification*](https://arxiv.org/abs/math/0208229).

The regular-locus recurrence `x_{m+2}x_m=1+x_{m+1}^2` is the affine rank-two
exchange recurrence.  Independently, its invariant `K` turns it into
`x_{m+2}=Kx_{m+1}-x_m`, so the temporal proof is a two-by-two matrix power.

**Effect:** even if the exact `inv0` boundary has no literal owner in this
bounded search, both dominant engines are already owned or permanently
excluded.  `KILL_OWNED_ENGINE`.

### `SFE`: direct squarefree-factorization operator

David Y. Y. Yun,
[*On square-free decomposition algorithms*](https://doi.org/10.1145/800205.806320),
is the classical primary algorithm source.  Martin von zur Gathen,
[*On square-free factorization of multivariate polynomials over a finite
field*](https://doi.org/10.1016/S0304-3975(97)00059-5), gives a finite-field
squarefree-decomposition algorithm based on derivative and GCD mechanisms.

The single `gcd(f,f')` update is the standard repeated-factor extraction step;
iteration merely subtracts one from every irreducible-factor multiplicity.

**Effect:** the entire theorem engine is algorithmic factor-multiplicity
erosion, also colliding with the portfolio's valuation/erasure firewall.
`KILL_ALGORITHM_ENGINE`.

### `GCM`: bounded exact-map non-hit; permanent matrix engine suffices

Exact queries for `AA^T A`, “Gram cube,” and finite-field matrix dynamics did
not locate a primary source for this literal functional graph.  General
finite-field functional-graph sources such as Konyagin et al.,
[*Functional Graphs of Polynomials over Finite Fields*](https://arxiv.org/abs/1307.2718),
and Oliveira--Brochero,
[*Dynamics of polynomial maps over finite fields*](https://arxiv.org/abs/2201.00954),
do not directly cover this multivariate matrix map and are not cited as direct
owners.

**Effect:** no direct owner claim.  The observed graph is depth zero or one,
and a general proof requires matrix congruence/block classification followed
by scalar or block powers.  The permanent matrix-power kill decides the gate.

### `BHD`: classical covariants plus directly studied Hessian dynamics

Primary and authoritative sources include:

- G. B. Mathews,
  [*Relations Between Arithmetical Binary Cubic Forms and Their
  Hessians*](https://doi.org/10.1112/plms/s2-9.1.200), on binary cubics and
  their Hessians;
- Patrick Popescu-Pampu,
  [*Iterating the Hessian: a dynamical system on the moduli space of elliptic
  curves and dessins d'enfants*](https://arxiv.org/abs/0809.4340);
- Marzio Mula, Federico Pintore, and Daniele Taufer,
  [*The Hessian of elliptic curves as a Lattes map*](https://arxiv.org/abs/2407.17042),
  which explicitly studies finite-field Hessian functional graphs.

The latter two use plane cubics/elliptic moduli rather than the typed binary
descent here, so they are family owners rather than literal-map owners.

**Effect:** the algebraic arrows are classical covariants and the depth-three
clock is imposed by carrier grading.  `KILL_THEOREM_THIN`.

### `PRE`: direct Euclidean-algorithm owner and internal collision

Nardo Gimenez, Guillermo Matera, Mariana Perez, and Melina Privitelli,
[*Average-case complexity of the Euclidean algorithm with a fixed polynomial
over a finite field*](https://arxiv.org/abs/2001.03222), studies the Euclidean
algorithm on polynomial pairs over `F_q`, including degree and GCD behavior.

The audited update is literally one Euclidean division step.  It also collides
with P131's occupied Euclidean-queue interface.

**Effect:** `KILL_DIRECT_ALGORITHM`.

### `KRC`: direct orbit-count/cyclic-sieving ownership

Primary sources checked were:

- Christine Heitsch,
  [*Counting orbits under Kreweras complementation*](https://arxiv.org/abs/2303.12240),
  which explicitly counts orbits according to length;
- Victor Reiner, Dennis Stanton, and Dennis White,
  [*The cyclic sieving phenomenon*](https://doi.org/10.1016/j.jcta.2004.04.009),
  whose examples include noncrossing partitions;
- David Bessis and Victor Reiner,
  [*Cyclic sieving of noncrossing partitions for complex reflection
  groups*](https://arxiv.org/abs/math/0701792), which identifies the
  Kreweras action and its square in the reflection-group setting.

**Effect:** the exact temporal axis is directly owned.  The map is a
permutation, so fibre one supplies no second theorem.  The carrier also lies
inside an already dense noncrossing-partition portfolio region.
`KILL_DIRECT_ACTION_OWNER`.

### `NWT`: mature Newton-map family; exact totalization not located

Primary sources checked include:

- Xander Faber and Adam Towsley,
  [*Newton's Method Over Global Height Fields*](https://arxiv.org/abs/1212.6409),
  which treats Newton iteration as rational arithmetic dynamics, including
  positive characteristic phenomena;
- Xiaoguang Wang, Yongcheng Yin, and Jinsong Zeng,
  [*Dynamics of Newton maps*](https://arxiv.org/abs/1805.11478), on the
  dynamics of Newton maps for arbitrary polynomials;
- Russell Lodge, Yauhen Mikulich, and Dierk Schleicher,
  [*A classification of postcritically finite Newton
  maps*](https://arxiv.org/abs/1510.02771).

Searches did not locate the exact affine finite-field convention that sends a
zero derivative denominator to the same point via `inv0(0)=0`; the usual
projective rational map instead has a pole there.  This is a bounded literal
non-hit, not owner clearance.

**Effect:** the exact inverse is just a cubic equation, while exact temporal
data varies irregularly with `p`.  The candidate fails the temporal gate even
before a more exhaustive Newton-map citation audit.  `KILL_WEAK_TEMPORAL`.

## Final owner verdict

No paper-level survivor remains.  Direct owners decide `HUR`, `MRK`, `PRE`,
and `KRC`; standard owned/permanent engines decide `CLU`, `SFE`, and `GCM`;
theorem thinness decides `CCS` and `BHD`; and missing all-parameter temporal
axes decide `QCD`, `ESP`, `AHP`, and `NWT`.

No statement in this log asserts novelty, nonexistence of a closer source, or
authorization to draft a paper.  Everything remains `HOLD_EXTERNAL`.
