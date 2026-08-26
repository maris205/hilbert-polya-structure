# Paper 17 Phase-1 independent mathematical, devil, and domain review

Review date: **2026-08-16 (Asia/Shanghai)**  
Review role: **independent ARS domain mathematician and devil reviewer**  
Review mode: **read-only exact-byte re-derivation**  
Verdict: **PASS — C0 / M0 / m0**  
Phase-1 gate decision: **EXACT PHASE-1 PROOF GATE MAY BE FROZEN**  
Publication ceiling: **TECHNICAL_NOTE_CANDIDATE; no standalone pass**

Symbolic proof implementation, controls, Route A/B, manuscript drafting,
release, Git, and public synchronization remain **false / unauthorized**.
This report is the only file written by this review.

## 1. Independence boundary and frozen tuple

I read the complete bound tuple and independently re-derived the registered
mathematics from the definitions.  The final source report and the combined
methodology/devil report were treated as claims to test, not as proof
authority.  The exact bytes checked before judgment were:

| Bound artifact | SHA-256 | Receipt |
|---|---|---|
| Papers 14--18 batch design lock | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | exact match |
| Paper-17 base protocol | `5ca581cff6f2fe088744a522646466ef2f5ce124ad3cdf50367cc5ed33347cea` | exact match |
| Paper-17 candidate lock | `2db53e92961cdfa7e43e4e06b7cdd81a2d87d97d15957d793b720bd86c71a604` | exact match |
| Phase-1 amendment v1 | `3ada0e70a0d3f53bd68e1a44e63c24870215987176d538c513400dc99ef95f3d` | exact match |
| Phase-1 amendment v2 | `2ce675880b171ee598f8a796edf55f9c695e2e6d0973620371d3ba460c7d1957` | exact match |
| Final source/domain report | `9991dc5e27ea8577d4236d38feeb63bfc110e3a3b242b3c17be8607da01f9e64` | exact match |
| Combined methodology/devil report | `811e51fc96baedf81a3e4185fa49519ff6c15bad37d866d8186054a24c25653e` | exact match |

The owner-subtraction bytes named by the batch lock were also checked:

| Owner artifact | SHA-256 | Receipt |
|---|---|---|
| Paper-9 manuscript | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | exact match |
| Paper-9 proof audit | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | exact match |
| Paper-10 manuscript | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` | exact match |
| Paper-10 proof audit | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | exact match |
| Paper-11 manuscript | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | exact match |
| Paper-11 proof audit | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | exact match |

The effective precedence order is

```text
batch lock / base protocol / candidate lock
  < amendment v1 on its conflicting claims
  < amendment v2 on the localic domain
  < this independent Phase-1 verdict
```

No conclusion below relies on a proof, control, Route, or manuscript file
for Paper 17.

## 2. Exact framework receipts

The independent domain check confirmed the following primary-source
boundaries.

1. Forssell, Section 2.1, defines equivariant sheaves for open topological
   groupoids as local homeomorphisms with continuous groupoid action and
   records that they form a Grothendieck topos.  The definition does not
   impose Hausdorffness on the present owner:
   [arXiv:1111.2952v2, physical pp. 2--3](https://arxiv.org/pdf/1111.2952).
2. Protin--Resende Theorem 2.41 sends an open localic groupoid to a
   multiplicative open quantal frame, and Theorem 2.45 reconstructs the
   corresponding localic groupoid up to isomorphism:
   [DOI 10.4171/JNCG/90, printed pp. 214--215](https://ems.press/content/serial-article-files/30505).
3. The same source, printed pp. 245--246, explicitly warns that the
   canonical composable-pair frame quotient need not be an isomorphism and
   gives local compactness of the arrow space as a sufficient condition.
   Definition 5.26 adds neither Hausdorffness nor second countability to its
   locally compact open-groupoid convention.

These receipts license the amended domain.  They do not license an
etale-only quantale-sheaf equivalence, a topological reconstruction of a
nonsober presentation, or localic reconstruction for arbitrary `H` without
the `q_H` comparison.

## 3. Direct re-derivation for arbitrary topological `H`

Let `X` be nonempty with the globally indiscrete topology, let `H` be a
topological group, and let `X` carry any continuous right `H`-action.  Use
the range-first groupoid

```text
G(X,H)^(0) = X,
G(X,H)^(1) = X x H,
r(x,h) = x,
s(x,h) = x.h,
(x,h)(x.h,k) = (x,hk).
```

Every arrow open is uniquely `X x U` for an open `U` in `H`.
For nonempty `U`, both `r(X x U)` and `s(X x U)` equal `X`: range is
immediate, and each right translation of `X` is a bijection.  Empty opens
map to the empty set.  Thus `G(X,H)` is an open topological groupoid for
every registered `H`, independently of the carrier cardinality, action,
orbit decomposition, or stabilizers.

For actual time `H=R`, the source map is not locally injective.  If `u` and
`v` are distinct points of an open interval and `x` is arbitrary, then

```text
s(x,u) = s(x.(u-v),v).
```

The arrows are distinct because their time coordinates differ.  Hence the
actual-real groupoid is open and non-etale, and its unit image
`X x {0}` is not arrow-open.  This non-etale conclusion is not promoted to
discrete `H`; for discrete time, the sets `X x {h}` are open local charts.

## 4. Independent topos calculation

### 4.1 Sheaves and etale spaces over `X_ind`

A sheaf on nonempty `X_ind` is determined by its value on the sole
nonempty open `X`.  If that value is a set `S`, the associated etale space
is

```text
p_S : X x S -> X,
```

whose opens are exactly `X x A`, `A subseteq S`.  Conversely every etale
space over `X_ind` decomposes into such whole-`X` sheets.  This gives the
usual equivalence `Sh(X_ind) ~= Set`, but the groupoid action must still be
classified rather than discarded.

### 4.2 Equivariant structure

After identifying the action pullback with `X x H x S`, an equivariant
structure has a sheet-label function

```text
lambda : X x H x S -> S_discrete.
```

For fixed `a in S`, continuity of `lambda(-,-,a)` forces every inverse
image to be `X x U`; hence the label is independent of the `X` coordinate
and varies continuously with `h`.  The unit and composition axioms are
exactly the axioms for a continuous action of `H` on the discrete set `S`,
with handedness fixed by the range-first convention.  The same argument on
maps of etale spaces says that morphisms are precisely equivariant set
maps.  Explicit quasi-inverses therefore give

```text
B(G(X,H)) ~= B_cont(H)
```

for arbitrary topological `H`.  The original action on `X` does not enter
the output.

For connected `H=R`, every orbit map `R -> S_discrete` has connected image
and is constant; the unit law makes the action trivial.  Thus

```text
B(G(X,R)) ~= Set.
```

For the mandatory negative control `H=Z_discrete`, the regular translation
action of `Z` on itself is continuous and nontrivial, so the output is
`BZ`, not `Set`.  Connectedness is therefore used exactly once, at the
real-time corollary, and is not hidden in the generic theorem.

## 5. Independent bare-quantale calculation

The frame map

```text
Phi : O(H) -> O(X x H),
Phi(U) = X x U
```

is an isomorphism.  Direct composition and inversion give

```text
Phi(U) Phi(V) = Phi(UV),
Phi(U)^*       = Phi(U^(-1)).
```

The product `UV` is open in every topological group.  These formulas define
the registered bare involutive open-set quantale for arbitrary `H` and are
independent of the action on `X`.  Its right-sided elements satisfy
`UH subseteq U`; any nonempty such `U` obeys `UH=H`, so the right-sided
frame is exactly

```text
R(O(G(X,H))) ~= 2.
```

For `H=R`, if an open `E` were a multiplicative unit, then
`E+U=U` for every open interval `U`.  Each `e in E` would therefore satisfy
`e+U subseteq U` for every such `U`, forcing `e=0`.  Hence
`E subseteq {0}`, which cannot be a nonempty open unit.  This agrees with
the open/non-etale classification.

This direct calculation does **not** by itself identify topological
composable pairs with the localic pullback for arbitrary `H`.  In
particular, it does not turn the arbitrary-`H` bare quantale into the
combined localic-reconstruction theorem.

## 6. Locally compact domain and `q_H`

Because `O(X_ind) ~= 2`, the point-set and localic composable-pair frames
reduce respectively to

```text
O(G^(2)) ~= O(H x H),
O(G^(1)) tensor_{O(G^(0))} O(G^(1)) ~= O(H) tensor O(H).
```

The exact comparison is therefore

```text
q_H : O(H) tensor O(H) -> O(H x H).
```

Amendment v2 correctly requires local compactness of `H` and retains
`q_H` as an explicit proof-or-citation obligation.  The Protin--Resende
source gives local compactness of the arrow space as sufficient.  Here the
same condition is also visible directly: opens of `X_ind x H` depend only
on `H`, and a compact neighborhood in `H` lifts to a quasi-compact
neighborhood with the same open-cover ledger in `X_ind x H`.

Once `q_H` is an isomorphism, topological multiplication on `H x H`
supplies multiplication on the correct localic pullback.  The open-quantal-
frame theorem and Theorem 2.45 then reconstruct the associated one-object
open localic group with arrow locale `Loc(H)`.  For the actual owner,

```text
Topological presentation: X_ind rtimes R
Top -> Loc:              terminal unit locale with arrow locale R
Open quantal frame:      O(R), reconstructing that localic groupoid
```

Thus the extra point-set carrier, its orbit decomposition, and its set
stabilizers disappear at the spatial-to-localic passage.  They are not
lost by a failure of Protin--Resende reconstruction.  The amended wording
is mathematically exact.

The three required examples remain inside the domain: usual `R` is locally
compact and connected, discrete `Z` is locally compact and disconnected,
and the standard-circle groupoid uses the same locally compact real time.

## 7. Standard-circle owner and scale variance

Let

```text
S_L = R/(LZ),
G_L = S_L rtimes R
```

with the standard circle topology and `L>0`.

Restriction of an equivariant etale space to `[0]` produces a discrete
`LZ`-set.  Conversely, an `LZ`-set `A` produces the associated etale bundle

```text
(R x A)/(LZ) -> R/(LZ).
```

These constructions are quasi-inverse, giving

```text
B(G_L) ~= B(LZ) ~= BZ.
```

This topos is not `Set`: the regular transitive `Z`-set is connected and
nonterminal, whereas every nonempty connected object of `Set` is terminal.
Thus the standard output retains abstract integer isotropy, unlike the
actual-real output.

On the quantale side the arrow frame is `O(S_L x R)`, and its algebraically
defined right-sided/base frame is `O(S_L)`, not `2`.  Local compactness
places this groupoid in the multiplicative open-quantal-frame/localic
domain, so the plain quantale reconstructs the standard localic action
groupoid rather than the actual one-object localic group.

For `c=L'/L`, the maps

```text
[r]_L       |-> [cr]_(L'),
([r]_L,t)   |-> ([cr]_(L'),ct)
```

form a topological-groupoid isomorphism.  Consequently neither the plain
classifying topos nor the plain open quantal frame distinguishes positive
values of `L`.  A separately registered strict time marker requires the
arrow-time coordinate to remain `t`; it then forbids the displayed
dilation unless `c=1`.  The correct conclusion is therefore:

```text
plain standard output: abstract Z isotropy and circle-localic base survive;
plain unmarked output: numerical L does not survive;
strict time-marked record: numerical L may be compared because dilation is forbidden.
```

No standard topology or strict marker is imported into the actual owner.

## 8. Devil's-advocate attacks

| Attack | Independent resolution | Gate consequence |
|---|---|---|
| A hidden nonconstant etale sheet may survive on `X_ind`. | Rejected: every etale open is a union of whole-`X` sheets. | The proof must exhibit the sheet equivalence explicitly. |
| The equivariant topos may retain the action on `X`. | Rejected: continuity forces the sheet label to be independent of `x`. | Only the continuous discrete `H`-action survives. |
| `Set` may hold for all time groups. | Refuted by the regular discrete `Z`-set. | Keep the `Z` negative control and use connectedness only for `R`. |
| The bare arrow quantale may retain orbit or stabilizer data. | Rejected by the exact `O(H)` multiplication/involution calculation. | Action-blindness is restricted to this registered interface. |
| Bare `O(H)` alone may justify localic reconstruction for arbitrary `H`. | Refuted: `q_H` is a separate comparison and is not automatic. | Keep the locally compact domain and explicit `q_H` gate. |
| The quantale theorem itself forgets the nonsober points. | Refuted: Theorem 2.45 reconstructs the localic groupoid it receives. | Attribute loss to `Top -> Loc`. |
| Actual and standard periodic orbits may have the same outputs. | Refuted: `Set/2` versus `BZ/O(S_L)`. | The topology-isolated actual-orbit/standard-orbit comparison is mandatory. |
| The plain standard outputs may recover `L`. | Refuted by simultaneous object/time dilation. | Numerical scale requires the extra strict marker. |
| Paper 17 may claim a new standalone theorem after relabeling Paper 11. | Sustained against standalone status. | Retain only `TECHNICAL_NOTE_CANDIDATE`; joint proof and later novelty gate remain mandatory. |

No attack exposes an unfixed contradiction, false universal quantifier, or
owner splice in the amended Phase-1 tuple.

## 9. Paper 9--11 subtraction and nonredundancy ceiling

The exact subtraction is stable:

| Prior owner | Already owned | Paper-17 admissible delta |
|---|---|---|
| Paper 9 | actual packet/orbit/quotient indiscreteness and set stabilizer/clock | application input only; no credit for reproving indiscreteness |
| Paper 10 | separated-reflection, continuous-observable, Borel, measurable, and positive-finite-measure collapse; standard-circle direction | no renaming of separated or measurable collapse as a topos theorem |
| Paper 11 | generic action-groupoid formulas, arrow-open classification, composable-pair chart, and one action-blind convolution record | may be cited as point-set lemmas; not new topology or convolution credit |
| Moerdijk/Forssell | open-groupoid equivariant-sheaf framework | exact computation on the locked actual and standard owners |
| Protin--Resende | open quantal frames and localic reconstruction | exact owner computation, base comparison, and correct localization of `Top -> Loc` loss |

After this subtraction, the generic calculations are too short for a
standalone-paper claim.  The defensible remaining package is the joint
actual/standard/marked comparison across both interfaces.  Therefore:

```text
STANDALONE_PASS:          HOLD / unsupported
TECHNICAL_NOTE_CANDIDATE: PASS at Phase 1 only
NOTE_OR_MERGE:            required if either branch, the standard control,
                          or the marked/unmarked comparison is omitted
```

This assessment does not allocate the batch's sole Technical Note slot
irreversibly and makes no priority claim.

## 10. Findings and coverage receipt

### Critical findings

None.

### Major findings

None.

### Minor findings

None.

The zero-finding judgment follows from the following explicit coverage
receipt rather than from deference to the preceding reviews:

| Dimension checked | Basis for no residual finding |
|---|---|
| owner/type validity | actual, standard, marked, bare-quantale, and localic owners remain separate |
| arbitrary-`H` theorem | direct topos and bare-quantale calculations are valid without local compactness |
| localic domain | `q_H` is separately named and the combined theorem is locally compact |
| connectedness | `R` and discrete-`Z` branches are explicitly separated |
| non-etaleness/unitality | asserted for actual real time, not leaked into discrete time |
| standard comparison | `BZ/O(S_L)` replaces the false symmetric collapse |
| information-loss wording | point loss is assigned to `Top -> Loc`, while localic reconstruction remains full |
| scale variance | unmarked dilation and strict-marker obstruction are distinct statements |
| P9--P11 subtraction | only the joint new interface calculation remains; standalone status is denied |

The handedness convention, construction of quasi-inverse functors,
arrow-local-compactness check, and topology-isolated actual-orbit control
remain mandatory proof-surface obligations.  They are already entailed by
the amended protocol and do not require another Phase-1 amendment.

## 11. Exact Phase-1 proof gate

The exact Phase-1 proof gate may now be frozen on the seven-artifact tuple
listed in section 1, with this review appended as the final independent
mathematical/devil/domain receipt.  The authorized next operation is only a
symbolic proof in the order already fixed by the amended protocol:

1. open groupoid and actual-real non-etale type;
2. etale-sheet classification and explicit topos equivalence;
3. connected `R` and disconnected `Z` split;
4. bare quantale, right-sided frame, and real-time nonunitality;
5. locally compact `q_H` check before localic reconstruction;
6. actual-orbit versus standard-orbit comparison;
7. unmarked dilation versus strict-marker obstruction; and
8. fixed-prime application only after the generic theorems.

The proof must fail closed if it needs Hausdorffness, second countability,
an etale-only quantale-sheaf equivalence, a proxy topology, an unregistered
strict marker, or a claim that the quantale reconstructs the nonsober
point-set presentation.

```text
Critical: 0
Major:    0
Minor:    0

MATHEMATICS:                         PASS
DEVIL / COUNTEREXAMPLES:             PASS
ARBITRARY-H TOPOS + BARE QUANTALE:   PASS
LOCALLY COMPACT H / q_H DOMAIN:      PASS
ACTUAL R / NEGATIVE Z CONTROL:       PASS
STANDARD CIRCLE / NUMERICAL L:       PASS
TOP -> LOC WORDING:                  PASS
P9--P11 SUBTRACTION:                 PASS
FINAL EXACT-BYTE VERDICT:            PASS C0/M0/m0
NEXT GATE:                           FREEZE EXACT PHASE-1 PROOF GATE;
                                     symbolic proof only after owner authorization
```

This review authorizes no control execution, Route record, manuscript,
release, Route B, Git operation, or public synchronization.
