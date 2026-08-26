# Paper 12 research protocol

Protocol date: **2026-08-15 (Asia/Shanghai)**  
Status: **V4 DESIGN/SOURCE RE-LOCK PASS — TARGETED PROOF AND CONTROLS AUTHORIZED**  
Working title: **Marked Time Cohomology and Orbitwise Standardization of
Indiscrete Arithmetic Action Groupoids**

## 1. Trigger, nonredundancy gate, and research question

Papers 9--11 establish an exact sequence of losses on a rational-Witt actual
fixed orbit: the inherited topology is indiscrete; separated unit observables
collapse; globally continuous arrow functions factor through real time; and
the author-defined global-QC convolution algebra and its transported
completions forget the action, stabilizer, prime, and period.

The action groupoid itself still contains an isotropy relation, and the source
flow supplies the normalized real-time homomorphism `c(x,t)=t`.  Paper 12 asks
whether this marked categorical datum retains anything that the separated
observable and convolution records erase.

The primary falsifiable question is:

> Does time projection induce a pullback isomorphism from the unnormalized
> continuous group cochain complex of `R` onto the author-defined continuous
> nerve cochain complex of the actual inherited-indiscrete action groupoid;
> does restriction of the source-normalized class `[c]` recover exactly
> `(log p) Z`; and does this period obey exact covariance under marked
> isomorphisms while failing, by explicit unequal-period counterisomorphisms,
> to descend as a scale invariant after positive rescaling or forgetting the
> mark?

For the fixed-prime packet, the strengthened question also asks whether the
same action and mark canonically determine an orbitwise Hausdorff coproduct
standardization and whether the continuous identity functor from that finer
groupoid to the actual indiscrete groupoid realizes

```text
H_cnv^1(G_actual;R)=R
  -> H_cnv^1(G_std;R)=R^Q
```

as the constant diagonal, intrinsically equal to the invariant subspace for
all strict time-preserving equivariant automorphisms.  Here `Q` is only the
bare orbit set and `R^Q` is the algebraic product of all functions `Q->R`.

This is a theorem package, not a pre-certified result.  Its continuous-complex
half may prove action-blind; its marked isotropy half may retain action data.
Both halves and their morphism boundary are required for a standalone paper.
If the package reduces to the already-known Paper-11 time-factorization lemma
plus a restatement of Deninger's stabilizer, the standalone gate fails and the
material must remain a note or merge.

Standalone eligibility additionally requires:

1. a substantive all-degree nerve/cochain-chain-map theorem, not only `H^1`;
2. strict/scaled/unmarked functoriality with explicit counterisomorphisms;
3. a source-verified fixed-prime `PACKET_COROLLARY`; an honest `ORBIT_ONLY`
   outcome forces `NOTE_OR_MERGE` rather than standalone release;
4. a standard period-quotient construction with exact one-sided topology and
   no transport overclaim;
5. a bounded exact-package novelty search; and
6. controls proving the generic construction accepts arbitrary clocks and
   therefore supplies no arithmetic specificity by itself;
7. a section-free orbitwise standardization equivalence for the entire
   common-stabilizer packet, including the canonical automorphism exact
   sequence; and
8. an exact standardized-versus-actual `H^1` comparison whose pullback image
   is the strict-automorphism invariant diagonal.

The decision is executable rather than stylistic:

```text
STANDALONE_PASS
  requires (i) the all-degree natural chain reduction, (ii) the fully typed
  strict/scaled/unmarked covariance and non-descent theorem, and (iii) the
  normalized period-quotient functor, the full-and-faithful orbitwise
  standardization equivalence, and the invariant-diagonal `H^1` theorem,
  all absent as stated from Papers 9--11,
  plus a source-verified `PACKET_COROLLARY` and a bounded nearest-precedent
  audit.

NOTE_OR_MERGE
  is mandatory if the source audit reduces the package to Paper-11 arrow
  factorization plus a routine degreewise bar-complex corollary and
  Deninger's already-owned stabilizer, or if the topology/category package
  remains only a routine assembly without the proved cohomological diagonal
  and invariant-subspace theorem.
```

The Phase-2 comparison matrix must separate generic background, direct
continuous-groupoid-cohomology precedent, Papers 9--11 internal prior use,
and the rational-Witt application. A zero exact-string hit never by itself
establishes standalone novelty.

Novelty wording is capped at `SUPPORTED_WITHIN_SEARCH`.

## 2. Generic groupoid and nerve

Let `X` be a nonempty indiscrete space with an arbitrary right action of the
additive group `R`.  Define, as in Paper 11,

```text
G=G(X,alpha)=X rtimes R,
r(x,t)=x,
s(x,t)=x dot t,
(x,t)(x dot t,u)=(x,t+u),
(x,t)^(-1)=(x dot t,-t).
```

The arrow topology is the product of the indiscrete topology on `X` and the
usual topology on `R`.  No transitivity, freeness, orbit count, period, or
arithmetic label is assumed in the generic theorem.

For `n>=1`, give the composable nerve `G^(n)` the subspace topology from
`G^n`.  Freeze the coordinate map

```text
Psi_n:X x R^n -> G^(n),
Psi_n(x;t_1,...,t_n)
 = ((x,t_1),
    (x dot t_1,t_2),
    ...,
    (x dot (t_1+...+t_(n-1)),t_n)).
```

Put `G^(0)=X`.  `P12-1` must prove, for every `n>=1`, that `Psi_n` is a
homeomorphism and that every open subset of `G^(n)` is `X x U` in these
coordinates.  A finite-degree computation is not an all-degree proof.

## 3. Author-defined continuous unnormalized nerve cochains

Let `A` be a named `T0` topological abelian group with continuous addition
and inversion. Freeze the constant coefficient bundle and identity arrow
action

```text
underline(A)_X=X x A -> X,
gamma . (s(gamma),a)=(r(gamma),a).
```

Continuity of this action is a `P12-2` obligation. After the displayed
trivialization, define the **Paper-12 author-defined continuous unnormalized
nerve complex**

```text
C_cnv^0(G;underline(A))=C(X,A),
C_cnv^n(G;underline(A))=C(G^(n),A), n>=1,
```

with pointwise addition. Equivalently these are continuous sections of the
appropriate pullback of `underline(A)_X` after trivialization. All globally
continuous cochains are retained, including values on degenerate simplices;
no normalized-subcomplex condition is imposed. There is no support, decay,
boundedness, integrability, differentiability, Borel-only, or compactness
restriction.

The comparison complex for the one-object group `R` uses exactly the same
unnormalized convention. Until Phase 2 proves equality with a named published
theory at matching hypotheses, the manuscript must use `C_cnv` and
`H_cnv`, not the unqualified phrase “the continuous topological-groupoid
cohomology.” A source using normalized cochains may be cited only after a
separate normalization-comparison theorem.

For `h in C_cnv^0`, freeze

```text
(d^0 h)(gamma)=h(s gamma)-h(r gamma).
```

For `n>=1`, freeze the inhomogeneous trivial-coefficient differential

```text
delta_0(gamma_1,...,gamma_(n+1))=(gamma_2,...,gamma_(n+1)),
delta_i(...)=
  (gamma_1,...,gamma_i gamma_(i+1),...,gamma_(n+1)), 1<=i<=n,
delta_(n+1)(gamma_1,...,gamma_(n+1))=(gamma_1,...,gamma_n),
d^n=sum_(i=0)^(n+1) (-1)^i delta_i^*.
```

Equivalently,

```text
(d^n f)(gamma_1,...,gamma_(n+1))
 = f(gamma_2,...,gamma_(n+1))
   + sum_(i=1)^n (-1)^i
       f(gamma_1,...,gamma_i gamma_(i+1),...,gamma_(n+1))
   + (-1)^(n+1) f(gamma_1,...,gamma_n).
```

`P12-2` must directly prove `d^(n+1)d^n=0`; a source label cannot replace that
proof. Freeze the algebraic objects

```text
Z_cnv^n(G;underline(A))=ker d^n,
B_cnv^0(G;underline(A))={0},
B_cnv^n(G;underline(A))=im d^(n-1), n>=1,
H_cnv^n(G;underline(A))=Z_cnv^n/B_cnv^n.
```

These are abstract abelian groups and, for `A=R`, real vector spaces. No
topology on the cochain groups or quotient topology on `H_cnv^n` is claimed.

Let `C_cnv^n(R;A)` denote the same author-defined inhomogeneous unnormalized
continuous cochain complex for the one-object topological group `R`. Let
`pi_n:G^(n)->R^n` be time projection in `Psi_n` coordinates and define its
contravariant pullback

```text
T_0=pi_0^*:A -> C(X,A),       T_0(a)(x)=a,
T_n=pi_n^*:C_cnv^n(R;A)->C_cnv^n(G;underline(A)),
T_n(f)(Psi_n(x;t_1,...,t_n))=f(t_1,...,t_n), n>=1.
```

For any chosen `x_0 in X`, define an evaluation candidate

```text
E_(x_0),0(h)=h(x_0),
E_(x_0),n(F)(t_1,...,t_n)=F(Psi_n(x_0;t_1,...,t_n)).
```

`P12-3` asks whether `T_bullet` is an isomorphism of cochain complexes in
every degree. The proof must establish `T d=d T`, bijectivity, and that
`E_(x_0)` is independent of the chosen unit only **after** the `T0`
factorization theorem, hence is the inverse of `T`. It may use Paper 11 only
after binding its exact arrow theorem and may not infer all degrees from the
arrow case without proving the nerve topology.

Removing the `T0` condition on `A` is a mandatory negative control.

## 4. Real degree one and the marked time class

Specialize to `A=R` with trivial coefficients.  Freeze

```text
c(x,t)=t.
```

This is the source-normalized time cocycle only on the Deninger application;
on the generic groupoid it is the coordinate cocycle.  It is globally
continuous but unbounded and has all-arrow support, hence is not in Paper
11's `C_qc^glob`.

`P12-4` must prove or refute:

```text
Z_cnv^1(G;R)=R c,
B_cnv^1(G;R)={0},
H_cnv^1(G;R)=R[c].
```

The proposed proof obligations are exact: continuous factorization gives
`b(x,t)=f(t)`; the cocycle law gives the Cauchy equation; continuity gives
`f(t)=lambda t`; continuous degree-zero cochains are constant because `A` is
`T0`, so their coboundaries vanish.  Each implication and its coefficient
domain must be audited independently.

The abstract one-dimensional vector space `H_cnv^1(G;R)` does **not** select a
preferred nonzero class.  Only the Deninger source time normalization marks
`[c]`.

## 5. Isotropy restriction and period subgroup

For a unit `x`, let

```text
H_x=Stab_R(x),
G_x^x={(x,t):t in H_x}.
```

For a real 1-cocycle `b`, first define the restriction homomorphism

```text
res_x:Z_cnv^1(G;R)->Hom_cont(G_x^x,R),
res_x(b)=b|_(G_x^x).
```

`P12-5` must prove:

1. restriction to isotropy is a group homomorphism;
2. every 1-coboundary vanishes on isotropy;
3. only after (2), the assignment

   ```text
   Per_x([b])=image(res_x(b)) subset R
   ```

   is representative-independent on `H_cnv^1(G;R)`;
4. for `b=lambda c`, `Per_x([b])=lambda H_x`;
5. in a transitive `R`-action, `H_x` is independent of `x` because `R` is
   abelian; and
6. only under the additional hypothesis `H_x=LZ`, `L>0`, `H^1` is
   scale-blind in the precise lattice sense: as `lambda` ranges over nonzero
   reals, the collection of scaled rank-one lattices is independent of the
   original positive generator.

Freeze four nonconflated owners:

```text
G(X,alpha)                     generic arbitrary indiscrete R-action;
G_(p,a)^orb=X_(p,a) rtimes R  one actual fixed orbit, every p and a;
G_p^pkt=Gamma_p rtimes R      one actual fixed-prime packet, every p;
G^global                      excluded full Deninger suspension owner.
```

`G_(p,a)^orb` and `G_p^pkt` are Paper-11/Paper-12 range-first
transformation-groupoid definitions built from Deninger's right flow; they
are not attributed as groupoid constructions to Deninger. Paper 9 owns their
actual inherited indiscrete unit topologies. Deninger physical pp. 38--39,
Section 6 and Theorem 6.1 are the frozen Phase-2 input for the packet action,
common multiplicative stabilizer `p^Z`, and logarithmic conversion to
additive time. Paper 9 proof/source hashes provide the exact `Gamma_p` owner
and topology separately.

For the rational-Witt fixed orbit, Phase 2 must reverify the same-object
source theorem

```text
H_x=L_p Z,  L_p=log p,
```

for every `p,a`.  Only then may `P12-6` state

```text
Per_x([c])=(log p) Z.
```

This is marked-period recovery, not a new derivation of Deninger's stabilizer
and not a canonical normalization supplied by abstract cohomology.

The packet corollary

```text
Per_x([c])=(log p) Z for every x in Gamma_p
```

is a separately typed `PACKET_COROLLARY` on `G_p^pkt`. Phase 2 must verify
that the additive action is the restriction of the same Deninger flow, that
`c(x,t)=t` is the same normalized time coordinate, and that **every** packet
unit has stabilizer `(log p)Z`. Failure of any one check yields `ORBIT_ONLY`
and omission of the packet claim; an orbitwise statement may not be promoted,
and the standalone decision is then `NOTE_OR_MERGE`.
No theorem here concerns `G^global`, a cross-prime union, or the full
suspension.

## 6. Strict, scaled, and unmarked categories

The categorical result is restricted to normalized transitive coordinate-
marked action groupoids. An object is

```text
(G=X rtimes R,c),
X nonempty and indiscrete,
x dot t a continuous transitive right action,
c(x,t)=t,
H=Stab_R(x)=LZ for some L>0.
```

Transitivity and commutativity make `H` independent of `x`. The object set is
shared by the following categories.

1. `C_str`: a morphism `F:(G,c)->(G',c')` is a topological groupoid
   isomorphism with homeomorphic unit map `F_0`, continuous arrow map and
   inverse, satisfying `c' o F=c`. Identity and composition are the ordinary
   groupoid identity and composition.
2. `C_scale`: a morphism is a pair `(F,alpha)`, `alpha>0`, with the same
   topological groupoid conditions and `c' o F=alpha c`. Composition is
   `(F',alpha') o (F,alpha)=(F' o F,alpha' alpha)`; the inverse is
   `(F^(-1),alpha^(-1))`. `C_str` is the `alpha=1` subcategory.
3. `C_un`: a morphism is a topological groupoid isomorphism after forgetting
   `c`; no equation involving time is required.

Every arrow is compared at the transported unit `F_0(x)`. `P12-7` must prove
the exact covariance law

```text
Per_(F_0(x))([c'])=alpha Per_x([c])
```

for `(F,alpha)` in `C_scale`; strict preservation is the special case
`alpha=1`. Exact subgroup equality does **not** characterize strictness.
The claim about weaker categories is only existential non-descent: the period
generator is not an invariant of `C_scale` or `C_un` because those categories
contain explicit isomorphisms between unequal-period lattice objects. It is
not claimed that every weaker morphism changes the subgroup.

For `L,M>0`, freeze

```text
X_L=R/LZ as a set with the indiscrete topology,
[r]_L dot t=[r+t]_L,
G_L=X_L rtimes R,
alpha=M/L,
F_alpha([r]_L,t)=([alpha r]_M,alpha t).
```

The proof must verify well-definedness, topology, range, source,
multiplication, inverse, the formula for `F_alpha^(-1)`, and
`c_M o F_alpha=alpha c_L`. This supplies non-descent for `L!=M`.

The orientation-reversing same-period control

```text
F_-([r]_L,t)=([-r]_L,-t)
```

must also be verified. It is unmarked, satisfies `c_L o F_-=-c_L`, and
preserves the subgroup `LZ`; it refutes any converse from exact subgroup
equality to strictness. Trivial (`H=R`), free (`H={0}`), and rationally
scale-invariant dense-period controls likewise prevent universal-loss
wording.

## 7. Normalized standard period-quotient functor and one-sided topology

Define `Hom_(R,0)^std` to have objects the pointed standard Hausdorff right
homogeneous spaces `(R/H,[0])`, with `H=LZ`, `L>0`, and morphisms the
basepoint-preserving continuous strictly `R`-equivariant homeomorphisms. Such
a morphism exists exactly when the subgroups agree and then has formula
`[t]_H|->[t]_(H')`. On `C_str` define

```text
S(G,c)=R/H=R/Per_x([c]),
S(F)([t]_H)=[t]_(H').
```

`P12-8` must first prove `H'=H`, hence well-definedness and continuity, and
then prove `S(id)=id` and `S(F' o F)=S(F') o S(F)`. Thus `S` is a functor
only on the normalized strict category. For an arbitrary class
`[b]=lambda[c]`, the value-space quotient `R/Per_x([b])` is a separate
record; it is not asserted to parametrize the action orbit.

For a chosen unit `x`, define

```text
theta_x:S(G,c)->X,  theta_x([t])=x dot t.
```

The proof must show it is a well-defined right-equivariant bijection and the
naturality square

```text
F_0 o theta_x = theta_(F_0(x)) o S(F).
```

For `x'=x dot u`, with `tau_u([t])=[u+t]`, it must prove
`theta_(x')=theta_x o tau_u`. Hence only the unbased homogeneous space is
canonical; a based chart is not. For nontrivial indiscrete `X`, `theta_x` is
continuous from the usual Hausdorff quotient and its inverse is not.

For `(F,alpha)` in `C_scale`, the separate dilation

```text
D_alpha:R/H -> R/(alpha H),  [t]_H |-> [alpha t]_(alpha H)
```

is continuous and satisfies a semilinear time-rescaling law. It is **not** a
morphism in `Hom_(R,0)^std` unless `alpha=1`; it must not be silently inserted in
the strict functor.

### 7.1 Transitive one-orbit standardization (the `Q={*}` subcase)

The pointed functor above is a correct but deliberately lossy shadow. Define
`Hom_R^std` to have standard Hausdorff transitive right `R`-homogeneous spaces
with stabilizer `LZ`, `L>0`, as objects and continuous strictly
`R`-equivariant homeomorphisms as morphisms, with no chosen basepoint.

For a strict marked object `(G=X rtimes R,c)` and any unit `x`, put

```text
q_x:R->X, q_x(t)=x dot t,
Std(G,c)=the same set X with the quotient topology transported by q_x.
```

`P12-8` must prove this topology is independent of `x`, is the usual standard
Hausdorff `R/H` topology, and has a continuous identity map to the actual
indiscrete topology but no continuous inverse when nontrivial. For a strict
marked isomorphism `F`, define `Std(F)=F_0`. The proof must show

```text
Std:C_str -> Hom_R^std
```

is full and faithful and is an equivalence with the inverse construction that
indiscretizes a standard homogeneous-space unit set and forms its marked
range-first action groupoid. Equivalently, every standard equivariant
homeomorphism lifts uniquely to `F(x,t)=(F_0(x),t)` and every strict marked
isomorphism descends.

For `H=LZ`, the proof must also classify, as abstract groups,

```text
Aut_Cstr(G,c) ~= Aut_R(Std(G,c)) ~= R/H
```

by unit translations. The pointed functor `S` must be presented as the shadow
obtained after choosing a basepoint; it is not faithful because it forgets
those translations. This standardization is not the singleton Hausdorff/CRH
reflection of the actual topology and never retypes the standard topology as
the inherited one.

No Haar measure, function algebra, trace, Poisson formula, crossed product,
completion, or operator credit is included in this target. Those would form
a fresh candidate, not an automatic consequence.

This subsection applies only to a transitive orbit groupoid.  The fixed-prime
packet is not transitive and may not instantiate `C_str` or this one-orbit
functor as a whole.

### 7.2 Common-stabilizer orbitwise standardization and the `H^1` diagonal

Define `C_common=disjoint-union_(L>0) C_common(LZ)` exactly as in
`phase3_standalone_amendment_v4.md`: its unit
space is globally indiscrete, the action need not be transitive, and every
unit has the same lattice stabilizer `H=LZ`, `L>0`.  Put `Q=X/R` as a bare
set.  The section-free topology

```text
U open in Std_coprod(X)
iff U intersect O has the quotient R/H topology for every orbit O
```

must make the same underlying set the topological coproduct of standard
`R/H` torsors.  The proof must establish basepoint independence on each
orbit, Hausdorffness, joint action continuity, open orbits, and uniqueness
among Hausdorff action-compatible topologies with open orbits.  The
compactness of `R/H` is a required step; no noncocompact generalization is
pre-certified.

For fixed `H`, let `Tor_R^coprod(H)` have precisely those nonempty coproducts as
objects and strictly equivariant homeomorphisms as arrows; take their
disjoint union over `H=LZ`. The functor `Std_coprod` must be full
and faithful and inverse to the construction `Indisc` that replaces the
whole unit topology by one global indiscrete topology. Under the ambient ZFC
convention, the canonical
abstract-group statement is only

```text
1 -> (R/H)^Q -> Aut_R(Std_coprod(X)) -> Sym(Q) -> 1.
```

Surjectivity and, after choosing one origin in every orbit, the noncanonical
wreath-product splitting use choice. No topology on the automorphism group is
claimed.

Here `Q=X/R` is nonempty. With `G_std=Std_coprod(X) rtimes R` and
`G_actual=X_indisc rtimes R`, the
identity on units and arrows gives a continuous marked functor

```text
J:G_std -> G_actual.
```

For the frozen real unnormalized continuous complex, `P12-8` must prove

```text
H_cnv^1(G_std;R) ~= R^Q,
rho([b])(q)=b(x,L)/L for any x in q,
rho(J^*(lambda[c]))=(q |-> lambda),
image(J^*)=(R^Q)^(Aut_R(G_std))=the constant diagonal.
```

Here `R^Q` is the algebraic Cartesian product, with no topology.  General
standardized cocycles are only cohomologous to the orbitwise time cocycles;
`B_cnv^1(G_std;R)` is generally nonzero.  No higher-degree standardized
cohomology is part of this target.

For the fixed-prime packet, `Q` is only the underlying orbit set of Paper-9
`Q_p`.  The constructed discrete component index, the actual indiscrete
`Q_p`, the actual packet, and the standardized coproduct packet are four
different typed records.

## 8. Controls and falsifiers

The control package is fixed before proof work and contains no post-hoc
random choice.

| ID | Exact owner/action | Expected witness |
|---|---|---|
| `TRIV-2` | `X={0,1}` with the indiscrete topology and `x dot t=x` | every stabilizer is `R`; `Per(c)=R`; no least positive period |
| `FREE-R` | `X=R` as a set with the indiscrete topology and `x dot t=x+t` | every stabilizer is `{0}` |
| `PER-L` | `X_L=R/LZ`, `[r] dot t=[r+t]`, for `L in {log 2, log 4, sqrt(2), 37/29}` | stabilizer and marked period are exactly `LZ`; generic theorem signature identical for all labels |
| `DENSE-Q` | `X=R/Q` as a set with the indiscrete topology and translation action | stabilizer and marked period are `Q`, hence not a lattice |
| `NONTRANS-1-2` | disjoint set `(R/Z) disjoint-union (R/2Z)` carrying one indiscrete topology; translation preserves each component | two orbits with stabilizers `Z` and `2Z`, while the global cochain reduction remains time-only |
| `NON-T0-A2` | `X={x_0,x_1}` indiscrete with trivial action; coefficient `A=Z/2Z` with indiscrete topology | degree-zero `h(x_0)=0`, `h(x_1)=1` is continuous and not constant, so `T0` removal breaks factorization |
| `SCALE-LM` | `F_alpha:G_L->G_M` for every ordered unequal pair in the fixed `PER-L` set | positive covariance, explicit inverse, and no strict unequal-period map |
| `REVERSE-L` | `F_-:G_L->G_L` for the same fixed `L` set | period subgroup preserved although the mark changes sign |
| `LABEL-SWAP` | labels `prime-2`, `composite-4`, `nonarith-sqrt2`, `neutral-37/29` permuted over the same typed controls | no theorem or Route coordinate changes with the label |
| `STD-COPROD-H1` | `m` disjoint common-order `n`-cycles, `n in {3,5,7}`, `m in {1,2,3}` | orbitwise topology/equivalence, automorphism count, actual dimension `1`, standardized dimension `m`, diagonal rank/invariant dimension `1`, and a nonzero standardized coboundary |

The executable contract is:

```text
generator:       code/generate_controls.py
tests:           code/test_controls.py
entry point:     experiments/reproduce.sh
checked results: results/*.csv
manifest:        results/manifest.json
optional seed:   120012 (reserved; no stochastic sample is required)
```

The v4 output is exactly
`results/orbitwise_standardization_h1_controls.csv`, with the 26-column
schema and deterministic row order frozen in
`phase3_standalone_amendment_v4.md`: `9` model rows, `90` basepoint rows,
`3151` automorphism rows, and `2` negative rows, for `3252` body rows.  The
complete package has `11` CSV files, `3486` body rows, and at least `96`
meaningful tests.

The generator and tests use only the Python standard library. Exact symbolic,
integer, rational, set-membership, and string checks use zero tolerance;
floating checks for the four displayed real constants use absolute tolerance
`1e-12` with the printed precision frozen in the manifest. The manifest must
bind active locks, Phase-2 final gate, implementations, expected artifact
names, row counts, and artifact hashes. `reproduce.sh` must run unit tests,
generate twice in independent temporary directories, compare both generations
and checked-in results byte-for-byte, run a strict `--verify-only` mode, reject
extra/missing/tampered/lock-drift bytes, and leave no `__pycache__`, `.pyc`, or
`.pyo` artifact. At least 96 tests and explicit wrong-direction/wrong-scale
negatives are required. Controls remain finite witnesses and falsifiers, not
proofs of the universal theorems.

These controls are expected to show `PROVES_TOO_MUCH` for arithmetic
specificity.  That does not refute the exact rational-Witt application, but
it caps Route credit at the registered source relation.

The theorem package is immediately refuted or narrowed by any of:

- a nerve coordinate map `Psi_n` that is not a homeomorphism;
- a continuous `T0`-valued cochain not factoring through time;
- failure of `T_bullet` to commute with `d`;
- a nonlinear continuous real additive `f`;
- a nonzero continuous real coboundary on the actual globally indiscrete
  groupoid (standardized coboundaries are generally nonzero);
- a rational-Witt isotropy time outside `(log p)Z` or a missing integer
  multiple;
- a strict marked isomorphism between unequal period subgroups;
- failure of the explicit scaled control isomorphism;
- a packet point with a different stabilizer;
- a claim that `c` has global-QC support; or
- a basepoint-dependent transported standard topology, a strict morphism not
  recovered by the standardization, or a missing/distorted unit translation;
- treating `B_cnv^1(G_std;R)` as zero or all standardized cocycles as
  orbitwise time-only representatives;
- reversing `J:G_std->G_actual` or its contravariant pullback;
- replacing the full product `R^Q` by a direct sum or by continuous functions
  on the actual indiscrete `Q_p`;
- claiming a canonical wreath splitting without an orbit section, or using
  scaled/unmarked automorphisms in the invariant-subspace theorem;
- accepting mixed stabilizers in `C_common`, or importing the constructed
  discrete component-index topology into the actual `Q_p`; or
- any full-suspension/all-prime promotion without a separately proved owner.

## 9. Targets and phase gates

Active targets are exactly:

```text
P12-1  all-degree nerve topology;
P12-2  cochain convention, d^2=0, and domain audit;
P12-3  full continuous cochain-complex time-projection isomorphism;
P12-4  real Z^1, B^1, and H^1 classification;
P12-5  isotropy restriction and generic period formula;
P12-6  rational-Witt fixed-orbit specialization and packet gate;
P12-7  strict/scaled/unmarked rigidity split and counterisomorphisms;
P12-8  pointed period quotient, common-stabilizer orbitwise standardization
       equivalence, automorphism exact sequence, standardized H^1=R^Q,
       and actual-to-standard diagonal/invariant characterization;
P12-9  deterministic adversarial controls and reproduction;
P12-10 typed negative-boundary Route-A evaluation with Route B false.
```

Phase 1 passes only after methodology, devil's-advocate, and source/domain
reviewers close every owner, coefficient, differential, morphism, packet,
novelty, and Route ambiguity on exact bytes.

Phase 2 must:

- audit primary/authoritative definitions of continuous topological-groupoid
  cohomology, constant coefficient bundles, unnormalized nerve cochains,
  coboundaries, isotropy restriction, and cocycle-preserving morphisms;
- bind exact Deninger/Paper-9/Paper-11 locators and same-object strengths;
- determine whether the period-quotient functor has a direct precedent;
- perform a bounded exact-package novelty search; and
- preserve local source PDFs only with preflight/hash manifests and exclude
  them from public synchronization.

The preregistered comparator set is Deninger arXiv `1807.06400v4`;
Mackenzie, *Rigid cohomology of topological groupoids* (1978), DOI
`10.1017/S1446788700011794`; Blanco--Uribe--Waldorf, *Pontrjagin duality on
multiplicative gerbes* (2023), DOI `10.4171/JNCG/528`, Sections 2.3--2.4;
Farsi--Huang--Kumjian--Packer (2022), DOI `10.1017/etds.2021.69`, Definition
3.7; and Fuchssteiner--Wockel arXiv `1110.2977` plus any exact published
manifestation. These are convention/domain comparators only. Their locally
compact, locally trivial, etale, paracompact, normalized, or derived-theory
hypotheses may not be imported to the actual owner.

The v4 incremental comparator set additionally includes the Stacks Project
Tag `0B1W` for topological coproducts; an authoritative closed-subgroup
homogeneous-space quotient theorem; Gepner--Meier, *Compositio Mathematica*
**159** (2023), Proposition 2.15, DOI
`10.1112/S0010437X23007509`, for action groupoids over `B G`; Guillou--May,
*Algebraic & Geometric Topology* **17** (2017), Proposition 5.19, DOI
`10.2140/agt.2017.17.3259`; and Alp--Wensley, *Applied Categorical
Structures* **18** (2010), Section 3.1, DOI
`10.1007/s10485-008-9183-y`. Their compactly generated weak Hausdorff,
finite-`G`-set, or finite-component hypotheses are mandatory ceilings. They
do not by themselves prove the exact indiscrete-packet standardization or
the `H^1` diagonal/invariant theorem.

The bounded search must record cutoff date, `last_searched_at`, endpoints,
query strings, backward/forward chaining, include/exclude reasons, and nearest
precedents across: continuous nerve cochains; topological-group cohomology;
topological-groupoid modules; continuous 1-cocycles; cocycle-preserving or
graded isomorphisms; isotropy restriction; homogeneous quotient recovery;
and Deninger/Papers 9--11. A direct precedent must match the same owner/domain,
the full unnormalized nerve complex, marked isotropy image, and the
strict/scaled/unmarked boundary. The only allowed negative-search wording is
`SUPPORTED_WITHIN_SEARCH`.

The search cutoff is **2026-08-15**. Required endpoints are arXiv, Crossref,
OpenAlex, Semantic Scholar, zbMATH or MathSciNet where accessible, Google
Scholar where reproducible, journal/publisher pages, and author publication
lists. At minimum record exact variants of:

```text
"continuous cohomology" groupoid (nerve OR composable tuples)
"continuous cochains" "action groupoid" indiscrete
"trivial coefficient bundle" groupoid cohomology
groupoid cocycle isotropy (restriction OR period group)
"cocycle-preserving" "groupoid isomorphism"
graded groupoid cocycle scaling
"R/LZ" "action groupoid" cohomology
Deninger (cocycle OR cohomology OR isotropy OR "marked period")
"rational Witt" ("groupoid cohomology" OR cocycle)
"topological coproduct" torsor "action groupoid" cohomology
"disjoint union" homogeneous spaces automorphism wreath product
"indiscrete" packet standardization cohomology
"orbitwise" H^1 groupoid invariant subspace
"action groupoid" "fully faithful" "over BG"
```

Unavailable, rate-limited, or non-exportable endpoints must be recorded as
such, not treated as zero results.

Phase 3 must provide direct proofs, deterministic controls, an independent
peer review, nonconflated Route records, and a composition blueprint before
manuscript drafting.

The v4 standalone-strength branch additionally requires a targeted audit of
topological coproducts of homogeneous torsors, equivariant/action-groupoid
lifting, orbit-permutation automorphisms, transitive groupoid `H^1`, and any
exact precedent for the actual-to-standard diagonal/invariant theorem. The
v2 mathematical proofs remain valid, but Route and manuscript work stay
blocked until the v4 amendment is exact-byte re-locked, source-audited,
proved, controlled, and independently reviewed.

## 10. Route-A/B boundaries

The generic complex reduction is an action-blind control and cannot receive
arithmetic credit.  The actual marked period owner may inherit an arithmetic
source relation only from Deninger's same object.  A period subgroup is not
yet an amplitude, trace, global prime enumeration, dynamical zeta, determinant,
Weil form, analytic continuation, or quantum lift.

To make the later negative evaluation reproducible rather than missing-input
`NOT_TESTABLE`, freeze eight nonconflated Route owners with every mandatory
field.

```text
candidate_id: GEN-INDISC-R-ACTION-CNV
candidate_definition: author-defined unnormalized continuous nerve complex
                      on a generic nonempty indiscrete R-action;
family: GENERIC-INDISCRETE-ACTION-CONTROL;
phase_space: G(X,alpha)^(bullet);
dynamics: arbitrary continuous right R-action on X;
parameters: X, alpha, named T0 coefficient A, cochain degree n;
parameter_provenance: author-defined universal theorem variables;
arithmetic_origin: NONE;
clock: coordinate time only, no arithmetic normalization;
normalization: additive real time.

candidate_id: DEN-EF-ACTUAL-ORBIT-CNV-P-A
candidate_definition: the same complex on G_(p,a)^orb;
family: DEN-EF-ACTUAL-ORBIT-TIME-COHOMOLOGY;
phase_space: full nerve of G_(p,a)^orb=X_(p,a) rtimes R;
dynamics: restricted Deninger right +t flow;
parameters: rational prime p, normalized Paper-9 orbit label a, degree n;
parameter_provenance: Deninger action/clock + Paper-9 topology + Paper-11
                      groupoid + Paper-12 complex;
arithmetic_origin: exact fixed-prime rational-Witt source owner;
clock: c(x,t)=t;
normalization: Deninger additive logarithmic-time scale.

candidate_id: DEN-EF-ACTUAL-PACKET-CNV-P
candidate_definition: the same complex on G_p^pkt, conditional on P12-6;
family: DEN-EF-ACTUAL-PACKET-TIME-COHOMOLOGY;
phase_space: full nerve of G_p^pkt=Gamma_p rtimes R;
dynamics: restricted fixed-prime Deninger right +t flow;
parameters: rational prime p, degree n;
parameter_provenance: Deninger common packet stabilizer + Paper-9 packet
                      topology + Paper-12 groupoid/complex;
arithmetic_origin: exact fixed-prime packet source owner;
clock: c(x,t)=t;
normalization: Deninger additive logarithmic-time scale.

candidate_id: DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A
candidate_definition: isotropy image of [c] on G_(p,a)^orb;
family: DEN-EF-ACTUAL-MARKED-PERIOD;
phase_space: marked pair (G_(p,a)^orb,c);
dynamics: restricted Deninger right +t flow;
parameters: rational prime p and normalized orbit label a;
parameter_provenance: source-normalized clock and stabilizer, no fitted scale;
arithmetic_origin: (log p)Z source relation;
clock: c(x,t)=t;
normalization: fixed source logarithmic time.

candidate_id: DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P
candidate_definition: common isotropy image of [c] on G_p^pkt, conditional
                      on the every-unit packet gate;
family: DEN-EF-ACTUAL-PACKET-MARKED-PERIOD;
phase_space: marked pair (G_p^pkt,c);
dynamics: restricted fixed-prime Deninger right +t flow;
parameters: rational prime p;
parameter_provenance: source common stabilizer, no orbitwise promotion;
arithmetic_origin: (log p)Z source relation at every packet unit;
clock: c(x,t)=t;
normalization: fixed source logarithmic time.

candidate_id: DEN-EF-STANDARD-PERIOD-QUOTIENT-P
candidate_definition: one-orbit standard isomorphism-class proxy and pointed
                      shadow (R/(log p)Z,[0]); it does not serialize the
                      same-set packet standardization;
family: STANDARD-MARKED-PERIOD-PROXY;
phase_space: usual Hausdorff R/(log p)Z;
dynamics: standard right translation;
parameters: rational prime p;
parameter_provenance: derived from the source-marked period only;
arithmetic_origin: copied source period relation, no actual-topology credit;
clock: standard additive translation coordinate;
normalization: inherited from the marked source clock.

candidate_id: DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P
candidate_definition: orbitwise standard coproduct packet groupoid and the
                      comparison J_p:G_p^std->G_p^actual, including the
                      H^1 diagonal/invariant statement;
family: DEN-EF-STANDARDIZED-PACKET-H1-COMPARISON;
phase_space: comparison pair (G_p^std,G_p^actual,J_p);
dynamics: the same right +t action, with standard open orbit components in
          the domain and the actual indiscrete packet in the codomain;
parameters: rational prime p, bare orbit set Q_p, H=(log p)Z;
parameter_provenance: Deninger common stabilizer + Paper-9 actual packet and
                      orbit set + Paper-12 constructed coproduct topology;
arithmetic_origin: copied common source period only, no Q_p topology/count;
clock: c(x,t)=t on both comparison owners;
normalization: fixed source logarithmic time, no fitted scale.

candidate_id: UNMARKED-PERIOD-SCALING-CONTROL
candidate_definition: G_L/G_M dilation and orientation-reversal controls;
family: GENERIC-ARBITRARY-PERIOD-CONTROL;
phase_space: G_L for L in {log 2, log 4, sqrt(2), 37/29};
dynamics: standard right translation on indiscrete R/LZ sets;
parameters: frozen L,M and alpha=M/L;
parameter_provenance: preregistered author controls independent of primes;
arithmetic_origin: NONE;
clock: explicitly unmarked for the owner verdict; c is used only to test loss;
normalization: NONE beyond each frozen control coordinate.
```

Every one of these eight records also freezes:

```text
determinant_convention: NONE_BY_DESIGN_NO_DETERMINANT_OBJECT;
orbit_cutoff: NOT_APPLICABLE_EXACT_THEOREM;
precision: SYMBOLIC_EXACT plus the frozen 1e-12 float-control boundary;
training_data: NONE;
forbidden_data: zeta zeros, zero/divisor fitting, target-zero optimization,
                traces, Paper-8 coefficients, Paper-11 completions;
code_commit: unavailable-no-git-content-sha256-lock-required;
artifact_paths:
  papers/12-marked-time-cohomology/notes/proof_audit.md
  papers/12-marked-time-cohomology/results/manifest.json
  papers/12-marked-time-cohomology/notes/phase3_peer_review.md
  papers/12-marked-time-cohomology/notes/route_audit.md
  evaluations/route_a/<candidate_id>/2026-08-15-stage12.yaml
```

Before `P12-10` executes, every displayed path must exist and its final
SHA-256 must be serialized in the YAML and route audit. The `code_commit`
value is a resolved no-Git provenance state, not a pending placeholder; exact
implementation and artifact SHA-256 locks are mandatory substitutes.

`NONE_BY_DESIGN_NO_DETERMINANT_OBJECT` is a present, falsifiable convention,
not an omitted field. It entails an A2 failure unless a fresh owner and
versioned protocol introduce a determinant. The formal evaluator still owns
the final A0/A1 decisions and may classify a layer `NOT_TESTABLE` where the
typed owner intentionally has no such object.

All Phase-1 candidate owners therefore have the design ceiling:

```text
A2_FAIL, A3_FAIL, A4_FAIL;
Route B invocation false;
no Route-B YAML.
```

`A1_PASS_ANALYTIC` is forbidden at design time. The formal evaluator must
decide whether exact marked repetitions earn `A1_WEAK` or remain `A1_FAIL`
after checking primitive/repeated status, orientation, multiplicity,
enumeration, stability, completeness, arithmetic derivation, and the frozen
arbitrary-period controls. A period subgroup alone does not pass A1. No
A-coordinate may be imported from
Paper 8's character trace, Paper 11's group-R completion, or the positive-time
scalar ledger.

## 10.1 Release and citation boundary

The final Paper-12 manuscript PDF and declared textual/code supplement may be
released only after manuscript, citation, declaration, peer, and release
gates pass. No `notes/sources/*.pdf` is a public supplement or may be embedded
in the manuscript PDF. Bibliography entries use canonical DOI, journal,
publisher, arXiv, or author endpoints, never local paths or audit hashes;
hashes remain reproducibility locators only. If Papers 9 or 11 lack an
immutable public manifestation at release time, Paper 12 must provide an
honest citable companion-preprint record or restate the required dependency
self-containedly. The public-sync dry run must list every released file and
mechanically show zero retained source PDFs in the staged/index payload.

## 11. Standalone and Paper-13 handoff

The preregistered delta matrix is:

| Paper-12 target | Inherited premise | New conclusion/proof obligation |
|---|---|---|
| P12-1--3 | Paper 11 proves the arrow (`n=1`) product topology and T0 time factorization | every finite nerve degree, exact face maps, direct `d^2=0`, natural pullback/inverse chain isomorphism |
| P12-4 | Paper 11 supplies degree-one factorization | algebraic `Z^1/B^1/H^1` classification with continuous Cauchy proof and no cochain topology |
| P12-5--6 | Deninger/Paper 9 own stabilizers and actual topology | representative-independent isotropy restriction of cohomology classes on the exact orbit/packet groupoids |
| P12-7 | no prior paper defines these morphism categories | strict/scaled covariance, explicit unequal-period non-descent, orientation-reversal nonconverse |
| P12-8 | Paper 10 distinguishes actual indiscrete and standard Hausdorff quotient directions; v2 actual `H^1` is one-dimensional | section-free orbitwise coproduct standardization, common-stabilizer category equivalence, canonical automorphism exact sequence, standardized `H^1=R^Q`, and actual pullback image equal to strict-symmetry invariants |
| P12-9 | earlier papers supply no cohomology controls | deterministic exact compiler, non-T0 falsifier, finite common-cycle diagonal/wreath controls, and two-generation reproduction |

Paper 12 becomes a standalone manuscript only if the full complex theorem,
marked-period recovery, morphism-category rigidity split, `PACKET_COROLLARY`,
canonical orbitwise standardization equivalence and automorphism exact
sequence, standardized-versus-actual `H^1` diagonal/invariant theorem,
updated controls, bounded novelty search, and independent reviews all close
without overclaim. Topology plus a wreath formula is insufficient. Otherwise
preserve it as a technical note or merge it with Paper 11 under the exact
`NOTE_OR_MERGE` rule in Section 1.

A possible Paper-13 question is deliberately not part of this lock:

> classify continuous circle-valued 2-cocycles on the same actual nerve and
> test whether any scalar twist of the author global-QC convolution can retain
> the action or period.

Paper 13 may start only under a fresh Phase-1 owner/domain/source lock.  It
may not assume that every multiplier is a coboundary, that a twisted
completion exists, or that the marked period quotient transports the actual
topology.
