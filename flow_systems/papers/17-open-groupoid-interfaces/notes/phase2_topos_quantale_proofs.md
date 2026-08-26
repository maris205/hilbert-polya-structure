# Paper 17 Phase-2 topos--quantale symbolic proof ledger

Status: **COMPLETE — AUTHORIZED SYMBOLIC PROOF ONLY**  
Version: `P17-P2-PROOF-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Proof verdict: **PASS — C0/M0/m0**  
Publication ceiling: **TECHNICAL_NOTE_CANDIDATE**  
Standalone disposition: **FALSE; independent proof and nonredundancy review required**  
Controls, Route A/B, manuscript, release, Git, and public synchronization:
**not authorized / false**

## 1. Exact authorization and evidence binding

The Phase-1 gate authorizes exactly this symbolic ledger.  Immediately before
proof work, the gate and all artifacts in its authority tuple were rehashed:

| Artifact | SHA-256 | Receipt |
|---|---|---|
| `notes/phase1_final_gate.md` | `025ee0404484bfa906094adc940528fc6c2c564c39783e1f1658ed9666f645df` | exact match |
| historical batch design lock | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | exact match |
| batch amendment v1 | `afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802` | exact match |
| `notes/research_protocol.md` | `5ca581cff6f2fe088744a522646466ef2f5ce124ad3cdf50367cc5ed33347cea` | exact match |
| `notes/candidate_lock.md` | `2db53e92961cdfa7e43e4e06b7cdd81a2d87d97d15957d793b720bd86c71a604` | exact match |
| `notes/phase1_amendment_v1.md` | `3ada0e70a0d3f53bd68e1a44e63c24870215987176d538c513400dc99ef95f3d` | exact match |
| `notes/phase1_amendment_v2.md` | `2ce675880b171ee598f8a796edf55f9c695e2e6d0973620371d3ba460c7d1957` | exact match |
| `notes/phase1_framework_source_precheck.md` | `9991dc5e27ea8577d4236d38feeb63bfc110e3a3b242b3c17be8607da01f9e64` | exact match |
| `notes/phase1_methodology_devils_review.md` | `811e51fc96baedf81a3e4185fa49519ff6c15bad37d866d8186054a24c25653e` | exact match |
| `notes/phase1_independent_math_review.md` | `bdf89476d49ab8a5b3bb7deff9f8738079bd185fd38a00bc1c9ba175677ad6d4` | exact match |

The owner-subtraction receipts named by the gate were also checked:

| Upstream owner | SHA-256 | Use in this ledger |
|---|---|---|
| Paper-9 manuscript | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | actual packet/orbit indiscreteness and literal fixed-prime stabilizer only |
| Paper-9 proof audit | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | verification of the preceding actual-owner input only |
| Paper-10 manuscript | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` | separated, Borel, and measurable comparison boundary only |
| Paper-10 proof audit | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | verification of that boundary only |
| Paper-11 manuscript | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | range-first formulas, arrow opens, and composable-pair chart; no new credit |
| Paper-11 proof audit | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | verification of those inherited lemmas only |

The selected source convention is Forssell's category of equivariant sheaves
for an open topological groupoid: an object is a local homeomorphism over the
unit space equipped with a continuous groupoid action.  Forssell states that
these form a Grothendieck topos in Section 2.1, physical pp. 2--3 of
[arXiv:1111.2952v2](https://arxiv.org/pdf/1111.2952).  Moerdijk's
[classifying-topos paper](https://doi.org/10.1090/S0002-9947-1988-0973173-9)
is the foundational source.  For the quantale branch, multiplication,
involution, right-sided/base elements, the nonunital open-groupoid case, and
localic reconstruction are taken in Protin--Resende's exact convention:
definitions on printed pp. 203--205, Theorems 2.41 and 2.45 on printed
pp. 214--215, and the composable-pair/local-compactness warning on printed
pp. 245--246 of [*Quantales of open groupoids*](https://doi.org/10.4171/JNCG/90).
No etale-only inverse-quantal-frame or quantale-sheaf equivalence is used.

## 2. Conventions and exact theorem domain

Let `H` be a topological group with identity `e`, written multiplicatively
until the real and integer examples.  Let `X` be a nonempty globally
indiscrete space with a continuous right action `(x,h) -> x.h`.  Use the
range-first transformation groupoid

```text
G=G(X,H),
G^(0)=X,                         G^(1)=X x H,
r(x,h)=x,                        s(x,h)=x.h,
(x,h)(x.h,k)=(x,hk),             (x,h)^(-1)=(x.h,h^(-1)).       (2.1)
```

An equivariant etale object is acted on from the left by groupoid arrows:
an arrow `g:y->x` sends the fibre over `y` to the fibre over `x`.  Under
(2.1), the residual sheet convention is therefore a **left** continuous
action of `H` on a discrete set:

```text
h.(k.a)=(hk).a.                                               (2.2)
```

Write `B_cont(H)` for the category/topos of such discrete continuous left
`H`-sets and equivariant maps.  This choice removes the otherwise hidden
opposite-group ambiguity.

The direct topos and bare involutive-open-set-quantale calculations below
hold for arbitrary topological `H`.  The combined multiplicative open
quantal-frame and localic-reconstruction conclusion is asserted only for
**locally compact** `H`, after the canonical comparison

```text
q_H: O(H) tensor O(H) -> O(H x H)                              (2.3)
```

has been installed.  Neither Hausdorffness nor second countability is added.

## 3. The open topological groupoid and its real-time type

### Proposition 3.1 — topology and groupoid structure

Every arrow open is uniquely of the form `X x U`, with `U` open in `H`.
The composable-pair map

```text
Theta:X x H x H -> G^(2),
Theta(x,h,k)=((x,h),(x.h,k))                                  (3.1)
```

is a homeomorphism.  Under this chart, multiplication is
`(x,h,k)->(x,hk)`.

**Proof.**  The only nonempty basic opens in `X x H` have whole first
factor, so unions are exactly `X x U`; nonemptiness of `X` gives uniqueness.
The map (3.1) is a bijection by the definition of composability.  It is
continuous as a map into `(X x H)^2` because the action and coordinate maps
are continuous.  Its inverse consists of the first object coordinate and
the two group-coordinate projections, hence is continuous.  Equivalently,
the subspace basis on `G^(2)` pulls back to the basis `X x U x V`.

The range and source maps are continuous because their target is
indiscrete.  In chart (3.1), multiplication is continuous by continuity of
group multiplication.  Inversion pulls `X x U` back to `X x U^(-1)`, and
the unit map pulls `X x U` back to `X` or the empty set according as `e` is
or is not in `U`.  Thus all structure maps are continuous.  QED.

### Proposition 3.2 — openness

`G(X,H)` is an open topological groupoid.

**Proof.**  Range sends a nonempty arrow open `X x U` to `X`.  For source,
choose `h in U`.  Right translation `x->x.h` is a bijection, so

```text
s(X x U) contains {x.h:x in X}=X.
```

The empty open maps to the empty set.  Hence both source and range are open.
Group multiplication is also open: in chart (3.1), an open is a union of
sets `X x U x V`, whose images are `X x UV`; `UV` is open in a topological
group.  QED.

### Proposition 3.3 — actual real time is non-etale

For `H=R` with addition and its usual topology, `G(X,R)` is not etale.  Its
unit image `X x {0}` is not arrow-open.

**Proof.**  Every neighbourhood of an arrow contains `X x U` for a
nonempty open interval `U`.  Choose distinct `u,v in U` and any `x in X`.
Then

```text
s(x,u)=x.u=(x.(u-v)).v=s(x.(u-v),v),
```

while the two arrows are distinct because `u!=v`.  Thus source is not
locally injective anywhere and cannot be a local homeomorphism.  Finally,
`{0}` is not open in `R`, so the unit image is not open.  No corresponding
non-etale claim is made for discrete time: if `H` is discrete, each
`X x {h}` is an etale source chart.  QED.

## 4. Whole-`X` sheets and the classifying-topos equivalence

### Lemma 4.1 — exact classification of etale spaces over `X_ind`

For every set `S`, give `X x S` the product topology with `S` discrete and
let `p_S(x,a)=x`.  Its opens are exactly `X x A`, `A subset S`, and `p_S`
is a local homeomorphism.  Conversely, every local homeomorphism `p:E->X`
is canonically isomorphic over `X` to one of these objects, with

```text
S=Gamma(X,E),                                                  (4.1)
```

the set of global sections.

**Proof.**  The assertion for `p_S` is immediate: each sheet `X x {a}` is
open and maps homeomorphically to `X`.  Conversely, every `e in E` has an
open neighbourhood `W` that maps homeomorphically to a nonempty open of
`X`; that open must be all of `X`.  Hence `W` is the image of a global
section.  If two global sections agree at one point, their equalizer is a
nonempty open of `X` (use a common etale chart), hence is all of `X`.
Therefore their images are either equal or disjoint and partition `E`.
The evaluation map

```text
X x Gamma(X,E) -> E,     (x,a) -> a(x)                       (4.2)
```

is consequently a bijective local homeomorphism, hence a homeomorphism over
`X`.  QED.

### Theorem 4.2 — explicit equivalence `B(G(X,H)) ~= B_cont(H)`

For every topological group `H`, nonempty indiscrete `X`, and continuous
right action on `X`, there are explicit quasi-inverse functors

```text
F:B(G(X,H)) -> B_cont(H),
E:B_cont(H) -> B(G(X,H)).                                    (4.3)
```

They give an equivalence of the selected Grothendieck topoi/categories.
The equivalence depends only on `H`, not on the cardinality of `X`, its
right action, orbit decomposition, or stabilizers.

**Proof.**  Put an equivariant etale object into the canonical sheet form
`X x S` of Lemma 4.1.  The groupoid action is then described by a sheet
label

```text
lambda:X x H x S -> S_discrete,
alpha((x,h),(x.h,a))=(x,lambda(x,h,a)).                       (4.4)
```

For fixed `a`, continuity makes each fibre of
`lambda_a:X x H->S` open.  Every such fibre has the form `X x U`, so
`lambda_a` is independent of `x`.  Define

```text
h.a=lambda(x,h,a).                                           (4.5)
```

This is well defined and continuous as a map `H x S_discrete->S_discrete`:
the domain decomposes into the open summands `H x {a}`, and on each summand
continuity follows from (4.4).  The unit axiom gives `e.a=a`.  Applying first
`(x.h,k)` and then `(x,h)` and comparing with their composite `(x,hk)` gives

```text
h.(k.a)=(hk).a,
```

so (4.5) is the left action fixed in (2.2).  An equivariant map of etale
spaces is a map over `X`; Lemma 4.1 makes it `id_X x f` for a unique set map
`f`, and groupoid equivariance is exactly `f(h.a)=h.f(a)`.  This defines `F`.

Conversely, for a discrete continuous left `H`-set `S`, define `E(S)` to be
`p_S:X x S->X` with action

```text
(x,h).(x.h,a)=(x,h.a).                                      (4.6)
```

The pullback action domain is `X x H x S`; continuity of (4.6) follows from
continuity of the `H`-action on the discrete set, and (2.2) proves the
groupoid action axiom.  Send an equivariant set map `f` to `id_X x f`.
This defines `E`.  Equations (4.4)--(4.6) show `F E=id` exactly, while the
canonical evaluation isomorphism (4.2) gives `E F~=id`.  These natural
isomorphisms prove (4.3).  QED.

### Corollary 4.3 — connected real time

```text
B(G(X,R)) ~= Set.                                           (4.7)
```

**Proof.**  For a continuous action of connected `R` on a discrete set
`S`, every orbit map `R->S` has connected image and is therefore constant.
The identity fixes its starting point, so the action is trivial.  Thus
`B_cont(R)` is exactly the category of sets and functions.  Apply Theorem
4.2.  QED.

### Corollary 4.4 — the disconnected-time falsifier

For `H=Z` with the discrete topology,

```text
B(G(X,Z)) ~= BZ,
```

and this topos is not `Set`.

**Proof.**  Every abstract `Z`-action on a discrete set is continuous.  In
particular, the regular translation action of `Z` on itself is nontrivial.
It is a transitive, hence connected, object of `BZ` and is not terminal;
in `Set`, every nonempty connected object is a singleton and hence terminal.
Thus `BZ` is not equivalent to `Set`.  This falsifies any attempt to remove
connectedness from (4.7).  QED.

## 5. Bare arrow-open quantale and its base

### Theorem 5.1 — direct quantale computation

For arbitrary topological `H`, the frame isomorphism

```text
Phi:O(H) -> O(G^(1)),      Phi(U)=X x U                      (5.1)
```

intertwines arbitrary joins, finite meets, groupoid-open multiplication,
and involution as follows:

```text
Phi(union_i U_i)=join_i Phi(U_i),
Phi(U intersection V)=Phi(U) meet Phi(V),
Phi(U) Phi(V)=Phi(UV),
Phi(U)^*=Phi(U^(-1)).                                        (5.2)
```

Thus the registered bare involutive open-set quantale is

```text
O(G(X,H)) ~= O(H).                                           (5.3)
```

It is independent of `X` and of the action on `X`.

**Proof.**  The frame statements follow from the unique form of arrow
opens.  In the composable-pair chart, the product of `X x U` and `X x V`
is the image of `X x U x V`, hence is `X x UV`; both inclusions are literal
arrow compositions.  Inversion sends `(x,h)` to `(x.h,h^(-1))`; for each
fixed `h`, `x->x.h` is a bijection, so its image is `X x U^(-1)`.  Open-set
product distributes over arbitrary unions, completing the quantale check.
QED.

### Proposition 5.2 — right-sided elements and the base frame

Use `top` for the lattice top, so it is not confused with a multiplicative
unit.  The right-sided elements `a` satisfying `a top <= a` are exactly

```text
empty and X x H.
```

Consequently the algebraically registered right-sided/base frame is the
two-element frame `2`.

**Proof.**  Under (5.1), right-sidedness is `UH subset U`.  It holds for
`U=empty`.  If `U` is nonempty and `u in U`, then `uH=H`, so `UH=H` and the
condition forces `U=H`.  Conversely `HH=H`.  QED.

### Proposition 5.3 — real-time nonunitality

The quantale `O(G(X,R))~=O(R)` is nonunital.

**Proof.**  Suppose an open `E subset R` were a multiplicative unit.  It is
nonempty because `empty+R=empty`.  For every bounded open interval `U`,
`E+U=U`.  If `e in E`, then `e+U subset U`; comparing the endpoints of a
bounded interval forces `e=0`.  Thus `E subset {0}`, but no nonempty subset
of `{0}` is open in `R`.  Contradiction.  This agrees with Proposition 3.3:
the unit image is not arrow-open.  QED.

The theorem is deliberately a bare/open-quantal calculation.  It creates no
C*-algebra, measure, state, trace, strict time marker, or etale quantale-sheaf
equivalence.

## 6. The `q_H` gate and open-localic reconstruction

### Proposition 6.1 — exact composable-pair comparison

For nonempty indiscrete `X`,

```text
O(G^(0)) ~= 2,
O(G^(1)) ~= O(H),
O(G^(2)) ~= O(H x H),
O(G^(1)) tensor_{O(G^(0))} O(G^(1)) ~= O(H) tensor O(H).      (6.1)
```

Under these identifications, the comparison from the frame of the localic
pullback to the point-set composable-pair frame is precisely (2.3), induced
by open rectangles.

**Proof.**  The first two identities are the indiscrete/product calculation;
the third follows from the homeomorphism (3.1).  Tensoring over the terminal
base frame `2` is ordinary frame tensor product.  The universal bimorphism
sends `(U,V)` to the rectangle `U x V`, which is exactly `q_H`.  QED.

### Theorem 6.2 — locally compact joint theorem

If `H` is locally compact in the registered Protin--Resende convention,
then `q_H` is an isomorphism, the associated locales form the one-object
open localic group with arrow locale `Loc(H)`, and the multiplicative open
quantal frame `O(H)` reconstructs that localic groupoid.

**Proof.**  First, local compactness is not lost on the arrow presentation.
If `C` is a compact neighbourhood of `h in H`, then `X x C` is a compact
neighbourhood of every `(x,h)`: an open cover of `X x C` is exactly a cover
of `C` after the frame identification (5.1), so it has a finite subcover.
Thus `X_ind x H` is locally compact whenever `H` is, with no Hausdorff or
second-countability input.

Protin--Resende, printed pp. 245--246, identify local compactness of the
arrow space as a sufficient hypothesis for the canonical composable-pair
frame comparison to be an isomorphism.  Applied to (6.1), this gives exactly
`q_H`, not an unnamed replacement comparison.  Multiplication on `H x H`
therefore descends from the correct localic pullback.  The source and range
locales both map to the terminal unit locale, and inversion is induced by
group inversion.  Theorem 2.41 gives the corresponding multiplicative open
quantal frame; Theorem 2.45 reconstructs the open localic groupoid from it.
QED.

### Corollary 6.3 — exact location of information loss

For actual time `H=R`, the owner chain is

```text
topological presentation: X_ind rtimes R with its point-set action;
Top -> Loc:                terminal unit locale and arrow locale Loc(R);
open quantal frame:        O(R), reconstructing that localic groupoid.    (6.2)
```

The additional points of a nontrivial indiscrete `X`, their set-theoretic
orbit decomposition, and their stabilizers disappear when the nonsober
topological presentation is sent to locales: `O(X)=2`.  They are **not**
lost through failure of the Protin--Resende reconstruction theorem, which
fully reconstructs the localic groupoid it receives.  No assertion is made
outside the locally compact domain merely from the bare isomorphism (5.3).

## 7. Standard periodic circle

Fix `L>0`, put

```text
S_L=R/(LZ) with its standard circle topology,
G_L=S_L rtimes R
```

and retain the same range-first convention: `([r],t)` is an arrow from
`[r+t]` to `[r]`.

### Theorem 7.1 — standard classifying topos

There are explicit quasi-inverse equivalences

```text
B(G_L) ~= B(LZ) ~= BZ.                                      (7.1)
```

**Proof.**  At `o=[0]`, the isotropy arrows are `(o,nL)`, so the fibre of
an equivariant etale space over `o` is a discrete left `LZ`-set.  This gives
the restriction functor.

Conversely, for a discrete left `LZ`-set `A`, form the associated etale
bundle

```text
E_A=(R x A)/(LZ) -> R/(LZ),                                 (7.2)
```

where `(r+nL,a)` is identified with `(r,(-nL).a)`.  This inverse in the
associated-bundle relation is forced by the range-first convention and the
left action fixed in (2.2).  Local sections of the
covering `R->S_L` show that (7.2) is etale.  The arrow `([r],t)`, whose
source is `[r+t]`, sends the class represented over `[r+t]` to the class
with the same sheet coordinate represented over `[r]`; the displayed
equivalence relation makes this independent of representatives.  This is a
continuous groupoid action.  Orbit transport shows that restricting (7.2)
back to `o` recovers `A`, while every equivariant etale bundle is recovered
from its fibre over `o`.  The same constructions on arrows are inverse.
Explicitly, `[0,a]=[nL,(nL).a]`; the isotropy arrow `(o,nL)` sends the latter
representative to `[0,(nL).a]`, so restriction recovers the stipulated left
`LZ`-action rather than its unrecorded opposite.
Finally, division by the positive generator identifies the discrete group
`LZ` abstractly with `Z`, proving (7.1).  QED.

The topos in (7.1) is not `Set` by the regular-`Z` argument of Corollary 4.4.
Thus the standard owner retains abstract integer isotropy.

### Proposition 7.2 — standard quantale and base

The standard arrow frame is `O(S_L x R)`.  Its right-sided elements are
exactly

```text
A x R,       A in O(S_L),                                   (7.3)
```

so the algebraically recoverable base frame is `O(S_L)`, not `2`.
The arrow space is locally compact, hence the exact composable-pair
comparison holds and Protin--Resende reconstruction returns the standard
localic action groupoid.

**Proof.**  If an arrow open is right-sided, composing any one of its arrows
with all arrows having the required range fills the whole time fibre at the
same range point.  It is therefore `A x R`.  Its range projection `A` is
open because projection from `S_L x R` is open.  Conversely every `A x R`
is right-sided, proving (7.3).  The circle is compact Hausdorff and `R` is
locally compact, so their product is locally compact; Theorem 6.2's cited
comparison applies.  QED.

## 8. Topology-isolated actual/standard comparison

Use the same underlying periodic right-`R` action set `R/(LZ)` twice:

```text
actual orbit:   (R/(LZ))_ind rtimes R,
standard owner: (R/(LZ))_std rtimes R.                       (8.1)
```

Theorems 4.2, 5.1, 7.1, and 7.2 give

| Interface | Actual inherited orbit | Standard circle owner |
|---|---|---|
| classifying topos | `Set` | `BZ` |
| arrow quantale | `O(R)` | `O(S_L x R)` |
| base/right-sided frame | `2` | `O(S_L)` |
| abstract isotropy retained by the plain output | no | `Z` |

The base frame is algebraically defined inside the open quantal frame, so
the two quantales cannot be isomorphic in the registered sense.  This
comparison varies topology while holding the underlying periodic action set
and literal time action fixed.  It does not compare a nontransitive full
packet to a single standard orbit and then attribute the difference solely
to topology.

The actual calculations are action-blind: on one declared nonempty
indiscrete carrier, the trivial action, a periodic action when registered,
and a nontransitive action all yield the same `Set` topos for real time and
the same `O(R)` quantale with base `2`.  This is a theorem consequence, not
execution of a deterministic control suite.

## 9. Unmarked dilation and the strict-marker obstruction

### Proposition 9.1 — unmarked positive periods are isomorphic

For `L,L'>0` and `c=L'/L`, define

```text
F_0([r]_L)=[cr]_(L'),
F_1([r]_L,t)=([cr]_(L'),ct).                                 (9.1)
```

Then `F=(F_0,F_1)` is an isomorphism of unmarked topological groupoids.
Consequently neither the plain classifying topos nor the plain open quantal
frame distinguishes the numerical value of `L`.

**Proof.**  Multiplication by `c` sends `LZ` onto `L'Z`, so `F_0` is a
well-defined circle homeomorphism.  It respects source because

```text
F_0([r+t]_L)=[cr+ct]_(L'),
```

which is the source of `F_1([r],t)`, and it plainly respects range,
composition, inversion, and units.  Replacing `c` by `c^(-1)` gives the
inverse.  Isomorphic groupoids have equivalent classifying topoi and
isomorphic open-set quantales.  QED.

### Proposition 9.2 — strict real-time marking recovers the period

Adjoin the strict time marker

```text
tau_L:G_L^(1)->R,      tau_L([r],t)=t.                        (9.2)
```

If an isomorphism of such marked records is required to preserve `tau`
literally, then a record of period `L` is isomorphic to one of period `L'`
only if `L=L'`.

**Proof.**  A strict marked isomorphism preserves arrow times and therefore
intertwines the two actions of the same, fixed real line.  It sends the
stabilizer-time set of any point to the stabilizer-time set of its image.
Those sets are respectively `LZ` and `L'Z`, hence `LZ=L'Z`.  Their positive
primitive generators are equal, so `L=L'`.  In particular the dilation
(9.1) is strict only when `ct=t` for all `t`, i.e. `c=1`.  QED.

The marker (9.2) is separately registered structure.  Proposition 9.2 does
not promote numerical `L` to an invariant of either plain output in
Proposition 9.1.

## 10. Fixed-prime application and owner firewall

Let `p` be a rational prime.  Paper 9 supplies the actual fixed-prime packet
`Gamma_p` and each actual inherited orbit as nontrivial indiscrete spaces;
it also supplies the literal stabilizer `(log p)Z` for an orbit.  Applying
the generic theorems, and only then substituting this owner, gives

```text
B(G(Gamma_p,R)) ~= Set,
O(G(Gamma_p,R)) ~= O(R),
right-sided/base frame ~= 2,
the open groupoid is non-etale and its quantale is nonunital. (10.1)
```

The same conclusions hold for any one actual inherited orbit.  They do not
recover packet cardinality, orbit labels, orbit decomposition, `p`, the set
stabilizer `(log p)Z`, or the numerical clock `log p`.  For a topology-
isolated comparison, take that orbit's underlying set/action with its actual
indiscrete topology and with the separately imposed standard circle topology;
Section 8 then gives `Set/2` versus `BZ/O(S_log(p))`.

The provenance and novelty subtraction is exact:

| Owner | Inherited fact | What Paper 17 proves beyond it |
|---|---|---|
| Paper 9 | actual packet/orbit indiscreteness and literal stabilizer | substitution into the already proved generic topos/quantale theorem only |
| Paper 10 | separated-reflection, continuous-observable, Borel, measurable, and positive-finite-measure collapses | no relabeling of those results as a topos theorem; (10.1) concerns equivariant etale objects and open quantales |
| Paper 11 | range-first groupoid formulas, arrow-open classification, composable-pair chart, and one action-blind convolution record | the explicit equivariant-sheaf equivalence, base/localic calculation, standard asymmetry, and marked/unmarked boundary |
| Moerdijk/Forssell | the open-groupoid classifying-topos framework | exact computation on the locked owners |
| Protin--Resende | open quantal frames and localic reconstruction | exact computation and correct localization of the `Top -> Loc` loss |

Neither (10.1) nor any comparison in this ledger constructs a standard
topology on the actual owner, a C*-algebra, Borel enhancement, Haar system,
measure, representation, state, trace, determinant, or Route-B object.

## 11. Claim closure, proof-surface audit, and publication disposition

| Claim | Symbolic disposition | Essential proof location |
|---|---|---|
| open actual groupoid and composable-pair topology | `PROVED` | Propositions 3.1--3.2 |
| actual real-time non-etaleness | `PROVED` | Proposition 3.3 |
| whole-`X` etale sheets and `B(G(X,H))~=B_cont(H)` | `PROVED` | Lemma 4.1 and Theorem 4.2 |
| connected `R` / disconnected `Z` split | `PROVED` | Corollaries 4.3--4.4 |
| bare quantale, involution, joins, base, nonunit | `PROVED` | Theorem 5.1 and Propositions 5.2--5.3 |
| `q_H` and locally compact localic theorem | `PROVED WITH EXACT PRIMARY-SOURCE INPUT` | Proposition 6.1 and Theorem 6.2 |
| point loss occurs at `Top -> Loc` | `PROVED/TYPED` | Corollary 6.3 |
| standard `BZ`, quantale, and base `O(S_L)` | `PROVED` | Theorem 7.1 and Proposition 7.2 |
| actual/standard asymmetry | `PROVED` | Section 8 |
| unmarked dilation / strict-marker obstruction | `PROVED` | Propositions 9.1--9.2 |
| fixed-prime application and P9--P11 firewall | `PROVED/TYPED` | Section 10 |

No proof step requires Hausdorffness or second countability of the generic
actual owner.  Local compactness is used only at the registered `q_H` and
localic-reconstruction gate.  The topos and bare quantale branches remain
separate direct computations; no etale-only bridge is used.  The standard
topology and strict marker are never imported into the actual owner.

After owner/source subtraction, the generic calculations remain too short
for a full standalone-paper claim.  The surviving contribution is the
joint actual/standard comparison across both interfaces, together with the
precise localic-loss and strict/unmarked boundaries.  Therefore this ledger
retains the batch ceiling and does not promote it:

```text
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
SYMBOLIC_PROOF=PASS
TOPOS_BRANCH=PASS
QUANTALE_BRANCH=PASS
Q_H_LOCALLY_COMPACT_GATE=PASS
ACTUAL_STANDARD_COMPARISON=PASS
UNMARKED_STRICT_BOUNDARY=PASS
FIXED_PRIME_OWNER_FIREWALL=PASS
TECHNICAL_NOTE_CANDIDATE=true
STANDALONE_PASS=false
INDEPENDENT_PROOF_REVIEW_REQUIRED=true
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```
