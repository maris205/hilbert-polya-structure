# Paper 15 Phase-1 mathematical rigidity precheck

Date: **2026-08-16 (Asia/Shanghai)**  
Mode: **ARS Phase-1 mathematical/domain precheck**  
Disposition: **HOLD — mathematical package feasible, current standalone centre fails the nonroutine gate**  
Findings: **C1 / M1 / m1**  
Proof, controls, Route, manuscript, release, Git, and public synchronization:
**not authorized by this report**

## 1. Exact reviewed bytes and scope

This report reviews only the following current tuple:

```text
Papers 14--18 batch design lock
  2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
Paper 15 research protocol
  53e023e427616e5bd98852181495c6598940e2eb238f100482f3abc7011ca59c
Paper 12 final manuscript
  c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163
Paper 12 integrated proof audit
  c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab
Paper 13 final manuscript
  c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701
Paper 13 proof audit
  e2f8fb8df4f3418fb3ff0fb60c87f9c7a4ae26cc7470c8c14aec3f86f6df1a63
Papers 9--13 final batch audit
  6aa915a9e85153957b269448ba23b56716c4f64d18e6b3c85f904d73b0001aea
```

The superseded Paper-15 protocol with digest `6ed8...0cce2` is not reviewed.
The current repair replaces the false one-orbit-per-prime simplification by

```text
Q_Per = disjoint_union_{p in P} Q_p,
L(q)=log(p) for q in Q_p,
Q_p nonempty.
```

That repair **closes the multiplicity/type issue for the rigidity theorem**.
A global orbit bijection with one scale sends each `Q_p` into a unique length
fibre; target surjectivity and nonemptiness of every target fibre then show
that the image is the whole fibre and that the induced prime-class map is a
bijection.  No equality or enumeration of the cardinalities `|Q_p|` is
needed.  This conclusion is set/action-level only: it transfers no actual
topology to the constructed standardization.

## 2. Exact mixed-lattice theorem package

Let `X` be a nonempty right `R`-set.  Assume that every stabilizer is a
positive cocompact lattice.  Since `R` is abelian, the stabilizer is constant
on an orbit.  For `q in Q_X=X/R`, write

```text
H_X(q)=L_X(q) Z,  L_X(q)>0.
```

The positive generator `L_X(q)` is intrinsic to the literal subgroup of the
one fixed time line.  It is not merely the abstract isomorphism type `Z`.

### 2.1 Section-free standardization

For an orbit `O_q` and `x in O_q`, let

```text
e_x:R -> O_q,  e_x(t)=x.t.
```

Give `O_q` the quotient topology for `e_x` and give `X` the coproduct of
these orbit topologies.  If `x'=x.u`, then `e_x'=e_x o T_u`; translation
`T_u` is a homeomorphism of `R`.  Hence the orbit topology is independent of
the selected point.  Equivalently, the definition can require the pullback
condition for every `x`, so no section of `X -> Q_X` is part of the
construction.

Each orbit is canonically a topological `R`-torsor of type
`R/(L_X(q)Z)`.  It is compact Hausdorff.  The coproduct standardization is
Hausdorff, its orbits are open and closed, and its right action is jointly
continuous componentwise.

It is the unique topology on this same `R`-set satisfying all three
conditions:

1. Hausdorff;
2. every orbit open; and
3. the right `R`-action jointly continuous.

Indeed, under any such topology, `e_x` induces a continuous bijection from
the compact space `R/H_X(q)` to the Hausdorff orbit.  It is a homeomorphism;
openness of all orbits then forces the coproduct topology.

The result extends Paper 12 from one common `H` to varying `H_X(q)`, but the
proof is componentwise the same proof.  It is an explicit retopologization,
not actual inherited topology and not a separated reflection.

### 2.2 Strict and globally scaled categories

For two such objects `X,Y`, a globally `c`-scaled unit isomorphism is a pair
`(f,c)`, with `c>0`, such that

```text
f(x.t)=f(x).(c t).
```

On marked action groupoids its forced normal form is

```text
F(x,t)=(f(x),c t),     c_Y o F = c c_X.
```

It is strict exactly when `c=1`.  Standardization and global
indiscretization give inverse equivalences both for strict maps and for
these globally scaled maps, provided the standardized target category uses
the displayed semilinear equivariance equation.  This equivalence says
nothing about unmarked algebraic groupoid isomorphisms.

### 2.3 Complete isomorphism classification

A globally `c`-scaled isomorphism `X -> Y` exists if and only if there is a
bijection

```text
sigma:Q_X -> Q_Y
```

such that

```text
L_Y(sigma(q)) = c L_X(q)                 (all q in Q_X).       (1)
```

Necessity follows by transporting the stabilizer in the semilinear
equivariance equation.  For sufficiency in ZFC, choose origins `x_q` and
`y_r` and define

```text
f(x_q.t)=y_{sigma(q)}.(a(q)+c t),
a(q) in R/(L_Y(sigma(q))Z).
```

Equation (1) makes this well-defined.  Componentwise it is the quotient
dilation `R/H_X(q) -> R/H_Y(sigma(q))`, hence a homeomorphism; its inverse
has scale `c^{-1}`.  The topology and invariant (1) are section-free, while
this existence witness and every displayed split choose origins.

With chosen origins, write a map as `(sigma,c,a)`.  If `(tau,d,b)` follows
it, the exact laws are

```text
(tau,d,b) o (sigma,c,a)
  = (tau o sigma, d c, q |-> b(sigma(q)) + d a(q)),

(sigma,c,a)^{-1}
  = (sigma^{-1}, c^{-1},
     r |-> -c^{-1} a(sigma^{-1}(r))).
```

Every sum is taken in the correctly scaled target quotient.  These formulas
are proof guards against an incorrect inverse-index or scale action.

Equivalently, with

```text
m_X(lambda)=card{q in Q_X : L_X(q)=lambda},
```

strict isomorphism means `m_X(lambda)=m_Y(lambda)` for all `lambda`, while a
`c`-scaled isomorphism means

```text
m_X(lambda)=m_Y(c lambda)                (all lambda>0),
```

where cardinal comparison and the sufficiency direction use choice.

### 2.4 Correct automorphism extensions

For one mixed object define

```text
K_L = product_{q in Q} R/(L(q)Z),

Sym_L(Q) = {sigma in Sym(Q): L(sigma(q))=L(q) for all q},

W_L = {(sigma,c) in Sym(Q) x R_{>0}:
       L(sigma(q))=c L(q) for all q}.
```

The multiplication in `W_L` is

```text
(tau,d)(sigma,c)=(tau o sigma,d c).
```

The canonical statements are

```text
1 -> K_L -> Aut_str(Std X) -> Sym_L(Q) -> 1,

1 -> K_L -> Aut_sc(Std X)  -> W_L      -> 1.                 (2)
```

The kernel consists of independent component rotations and is the full
Cartesian product, not a direct sum.  The maps and kernel identification
are section-free.  Surjectivity is a ZFC existence statement.  Choosing one
origin in every orbit gives noncanonical splittings of (2).  Thus the
globally scaled quotient is not merely an unnamed “permutation group”; it is
the group of compatible `(permutation,scale)` pairs `W_L`.

## 3. Prime-clock rigidity: two direct proofs

Let `P` be the set of positive rational primes.  Suppose `c>0` and a
bijection `sigma:P->P` satisfy

```text
log(sigma(p))=c log(p)                    (all p in P).        (3)
```

### Proof A — minimum of the length support

Put `S={log p:p in P}`.  Bijection and (3) give `cS=S`.  The set `S` has
the positive minimum `log 2`.  Therefore

```text
log 2 = min(S) = min(cS) = c log 2,
```

so `c=1`.  Equation (3) and injectivity of `log` then give
`sigma(p)=p` for every prime.

This proof uses neither the prime number theorem nor unique factorization,
prime density, prime infinitude, or a counting estimate.  More generally:

> If a nonempty subset `S` of `R_{>0}` has a minimum and `cS=S` for
> `c>0`, then `c=1`.

Consequently the proposed arithmetic centre is an instance of a one-line
ordered-set lemma; primality enters only in identifying the supplied support
and its minimum.

### Proof B — order-preserving prime permutation

If `p<q`, then positivity of `c` and (3) imply
`sigma(p)<sigma(q)`.  Hence `sigma` is a strictly increasing bijection of
the ordered primes.  Any increasing bijection of a sequence of order type
`N` fixes its first element and then every successor by induction.  Thus
`sigma=id`, and (3) at `p=2` gives `c=1`.

This is longer than Proof A and has the same routine ceiling.

### Optional PNT proof and source need

Exponentiating (3) gives `sigma(p)=p^c`.  Bijection yields, for `y>0`,

```text
pi(y)=pi(y^(1/c)).
```

The prime number theorem would imply

```text
pi(y^(1/c))/pi(y) ~ c y^(1/c-1),
```

which tends to `0` for `c>1` and to infinity for `0<c<1`, contradicting the
exact ratio `1`.  This proof is correct but strictly weaker and needlessly
source-heavy.  The final proof should use Proof A.  No PNT source is needed
unless the manuscript elects to retain the optional asymptotic proof.

## 4. Prime-fibre application and owner guard

On the repaired current protocol, every orbit in `Q_p` has length `log p`.
Let a globally `c`-scaled automorphism induce an orbit bijection `rho`.
For `q in Q_p`, equation (1) places `rho(q)` in the unique fibre whose
length is `c log p`; call it `Q_{sigma(p)}`.  All of `Q_p` lands in that
fibre.  Conversely, any target orbit in `Q_{sigma(p)}` has a preimage in
some `Q_r`; injectivity of multiplication by `c` forces `r=p`.  Hence
`rho(Q_p)=Q_{sigma(p)}`.  Nonempty fibres and global surjectivity make
`sigma` a prime permutation.

Proof A gives `c=1` and fixes every prime-length fibre.  It does **not** make
the orbit automorphism the identity: arbitrary permutations within each
`Q_p` and independent circle rotations remain.  In particular the prime
case has

```text
W_L = product_{p in P} Sym(Q_p)
```

at scale `1`, together with the rotation kernel

```text
product_{p in P} product_{q in Q_p} R/((log p)Z).
```

The input is Deninger's already marked periodic-orbit family.  “Recovery”
here means rigidity of its supplied literal stabilizer lengths under one
global time rescaling.  It is not selection of primes from a generic clock
family, recovery from the actual topology, or an unmarked/analytic
invariant.

## 5. Required proof guards and countercontrols

1. **Nonempty owner.**  For the empty object every scale condition is
   vacuous.  Nonemptiness is load-bearing.
2. **One literal time line.**  The subgroups must be literal subgroups of the
   same marked `R`; abstractly every `LZ` is isomorphic to `Z`, so the number
   `L` disappears after forgetting the time mark.
3. **One global positive scale.**  If the scale may depend on the prime,
   every prime permutation is possible: use
   `c_p=log(sigma(p))/log(p)` and orbitwise quotient dilations.  This is the
   mandatory sharp negative control.
4. **Bijectivity.**  For a generic geometric clock
   `Q=N_0`, `L_n=a^n` with `a>1`, multiplication by `a` and the shift
   `n |-> n+1` give an injective scaled map that is not onto.  The
   isomorphism conclusion cannot be applied to embeddings.
5. **A minimum is the actual rigidity mechanism.**  For
   `Q=Z`, `L_n=a^n`, the shift `n |-> n+1` is a nontrivial globally
   `a`-scaled automorphism.  Mixed-lattice families are not rigid in
   general.  The difference is the absence of a minimum, not primality.
6. **Positive versus signed scale.**  If signed scales are admitted,
   orientation reversal has factor `-1`; length labels see only its absolute
   value.  Prime-length rigidity would give `|c|=1`, not strictness.
7. **Isomorphisms only.**  For a noninvertible strictly equivariant map one
   generally gets stabilizer inclusion, not equality.  Equation (1) is an
   iff only in the isomorphism category.
8. **Topology hypotheses.**  Dropping Hausdorffness leaves the indiscrete
   orbit topology as a competing topology.  Dropping open orbits permits,
   for example, a product of a nondiscrete index space with a standard
   circle.  The uniqueness theorem must retain all three hypotheses.
9. **Cocompact positive lattices.**  Compact-to-Hausdorff is the uniqueness
   step.  No theorem here extends to `H=0`, dense stabilizers, or arbitrary
   subgroups of `R`.
10. **Choice boundary.**  Standardization and the label invariant require no
    orbit origins.  Lifting an arbitrary compatible permutation and writing
    a wreath/semidirect split do require a system of origins in ZFC.
11. **Owner boundary.**  The standardized topology is constructed from the
    action.  The protocol may use the bare actual periodic-orbit set and
    its source-owned stabilizers, but may not call the constructed topology
    the inherited global periodic-locus topology.
12. **No analytic promotion.**  Nothing above supplies cohomology beyond
    Paper 12, a `C*`-dynamical system, an Arveson spectrum, trace,
    determinant, or Paper-16 result.

## 6. Source needs

- Deninger, *Dynamical systems for arithmetic schemes*, arXiv
  `1807.06400v4`, Section 6 and Theorem 6.1, is the exact primary source for
  the global periodic-locus decomposition into packets, every-point
  stabilizer, logarithmic time, and orbit length.  The retained Paper-12
  source manifestation and preflight already bind physical pp. 38--39.
- Paper 12 is the direct mathematical predecessor for strict/scaled
  covariance, common-lattice standardization, and the common-lattice
  automorphism extension.  A standalone public manuscript must either cite
  an immutable public Paper-12 identity or restate every load-bearing lemma
  self-containedly.
- Stacks Project Tag `0B1W` suffices for generic coproduct topology.
  The already audited homogeneous-space, over-`B R`, and finite wreath
  references remain nearest background, not proofs of the exact mixed
  package.
- **PNT is not load-bearing and should not be frozen merely for P15-5.**
  The protocol's unconditional sentence requiring a PNT source before the
  final proof gate should be made conditional on actually retaining the
  optional PNT proof.
- A bounded incremental exact-package search is still required before any
  novelty wording.  Search failure may license only
  `NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH`; it cannot overcome
  the routine nature of Proof A.

## 7. Nonredundancy and standalone ceiling

Paper 12 already proves:

- common-`H` section-free standardization and uniqueness;
- the full-and-faithful strict equivalence with global indiscretization;
- strict stabilizer preservation and positive scaled covariance;
- explicit single-orbit dilations between unequal periods; and
- the common-`H` rotation/permutation automorphism extension.

Paper 15's exact mathematical delta is therefore limited to varying the
label `L(q)`, replacing the full symmetric group by its label-compatible
subgroup, recording `W_L`, proving the sufficiency half of the global-scale
classification, and applying the minimum lemma to the full prime-length
support.  P15-1--P15-4 are componentwise Paper-12/standard orbit-type
bookkeeping.  P15-5 is true, but it is even more general and more routine
than the protocol anticipates.

Paper 13 studies gauge-trivial twists, selected component completions, and a
generic constant-diagonal corona record; its fixed-prime outputs explicitly
recover no prime.  Paper 15 does not duplicate those analytic mechanisms and
does not contradict their nonretention result: it deliberately keeps the
marked stabilizer length and the entire mixed support, while Paper 13's
tag-forgotten outputs discard that information.  No Paper-13 `C*` or corona
claim may be imported to increase Paper-15 weight.

The package is mathematically clean enough for a short technical note or a
foundational section of Paper 16.  It does **not**, on the current centre,
clear the batch lock's standalone requirement.  Calling Proof A a
substantive arithmetic rigidity theorem would overstate both its hypotheses
and its content.  Adding PNT would obscure rather than strengthen it.

## 8. Findings and decision

### Critical — C1

The declared standalone-bearing centre collapses to the general lemma
`min(S)>0 and cS=S => c=1`.  This invalidates the protocol's required
independent finding that the PNT/prime-clock conjunction is nonroutine.  The
theorem is true; the standalone rationale is not.

### Major — M1

Before any proof freeze, the scaled automorphism quotient must be typed as
`W_L` in (2), distinct from the strict label-preserving permutation group.
Unmarked algebraic isomorphisms must remain outside both classification
theorems unless a separate exact category is defined.  Otherwise a claimed
“complete classification” would silently mix variances.

### Minor — m1

The Phase-1 protocol unconditionally requests a PNT source at the final
proof gate even though its own elementary-proof branch is sufficient.  Make
that source requirement conditional or remove it from the load-bearing
gate.

### Decision

```text
MATHEMATICAL_FEASIBILITY = GO
CURRENT_STANDALONE_GATE  = NO_GO
OVERALL_PHASE_1_DECISION = HOLD
RECOMMENDED_DISPOSITION  = NOTE_OR_MERGE
```

Proceed only after an explicit author/orchestrator choice does one of the
following:

1. designate Paper 15 as the batch's sole possible Technical Note and freeze
   the exact theorem package above;
2. merge this package into Paper 16 as its categorical foundation; or
3. supply a genuinely nonroutine new centre and subject it to fresh
   nonredundancy, source, and mathematical review.

No proof, controls, Route, manuscript, or release work is authorized by this
HOLD report.
