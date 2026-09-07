# Second algebraic/arithmetic replacement breadth scout

**Audit date:** 2026-09-02 UTC.  
**Stage:** Stage-1 literal-system breadth and exact falsification.  
**External status:** `HOLD_EXTERNAL`.  
**Paper status:** no number, no draft, no freeze, and no novelty or priority
claim.

## Outcome

This lane tested **thirteen genuinely different literal finite systems** after
the permanent exits of `QTS` and `QNC`.  The deterministic verifier enumerated
**96 parameter boxes**, **84,137 states**, and executed **506,625 assertions**.
The frozen profile digest is

```text
011b264f4eb463bc2d6ff27ad425478d98514e73d2afa86fe445db58d37806ee
```

The paper-level survivor pool is **empty**.  This is the intended outcome of a
strict breadth gate, not an invitation to promote the least weak candidate.
Every system fails at least one of the required axes:

1. a uniform temporal theorem with a sharp all-parameter silhouette; and
2. an independent fibre, inverse, endpoint, or structural theorem not already
   owned by a standard action, algorithm, quotient, or permanent kill engine.

Four systems have exact and useful inverse data (`QCD`, `ESP`, `AHP`, `NWT`),
but their temporal profiles encode irregular character or rational-map
arithmetic.  Three systems have striking periods (`HUR`, `MRK`, `KRC`), but are
literal permutations with fibre one and directly owned actions.  `CLU` has the
strongest visual bifurcation, yet its regular locus is the standard rank-two
cluster recurrence and a fixed-invariant second-order linear recurrence.  The
remaining systems are shallow, algorithmic, or instances of permanently
excluded matrix/factor-multiplicity engines.

Exact replay is counterexample pressure, not proof or owner clearance.  The
owner audit is in `OWNER_SEARCH_LOG.md`; the executable and transcript are
`verify_algebraic_replacement2.py` and `CANONICAL.txt`.

## Intake table

| handle | literal carrier and update | two-axis profile | verdict |
|---|---|---|---|
| `QCD` | `F_p`, `x -> x+chi(x)`, `chi(0)=0` | exact cycles and fibres; tails are quadratic-character runs | `KILL_WEAK_TEMPORAL` |
| `ESP` | `F_p^2`, `(x,y)->(xy,x+y)` | complete Vieta fibres; temporal graph jumps with `p` | `KILL_WEAK_TEMPORAL` |
| `AHP` | `F_p^2`, `(x,y)->(x+y,xy inv0(x+y))` | complete singular/quadratic fibres; periods and tails jump | `KILL_WEAK_TEMPORAL` |
| `CCS` | `F_p`, residues fixed and nonresidues squared | complete graph and fibres, but depth exactly one | `KILL_THEOREM_THIN` |
| `HUR` | `S_n^2`, `(a,b)->(b,b^{-1}ab)` | rich braid-action periods; fibre identically one | `KILL_DIRECT_ACTION_OWNER` |
| `MRK` | Markoff surface over `F_p`, `(x,y,z)->(y,z,3yz-x)` | rich Vieta-rotor periods; fibre identically one | `KILL_DIRECT_ACTION_OWNER` |
| `CLU` | `F_p^2`, `(x,y)->(y,(1+y^2)inv0(x))` | sharp `p mod 4` singularity; cluster/matrix engine | `KILL_OWNED_ENGINE` |
| `SFE` | monic `f in F_p[t]`, `deg f<=n`, `f->gcd(f,f')` | sharp multiplicity clock; squarefree-factorization operator | `KILL_ALGORITHM_ENGINE` |
| `GCM` | `M_2(F_p)`, `A->AA^T A` | small-box one-step graphs; matrix-polynomial classification | `KILL_PERMANENT_MATRIX_ENGINE` |
| `BHD` | typed binary cubics -> Hessian quadratics -> discriminants -> sink | exact depth three; classical covariants and imposed grading | `KILL_THEOREM_THIN` |
| `PRE` | bounded polynomial pairs, `(f,g)->(g,rem(f,g))` | exact Euclidean clock and terminal fibres | `KILL_DIRECT_ALGORITHM` |
| `KRC` | `NC(n)`, `pi->pi^{-1}c` | explicit orbit structure; fibre identically one | `KILL_DIRECT_ACTION_OWNER` |
| `NWT` | `F_p`, totalized Newton map of `x^3-x` | cubic inverse equation; irregular rational-map graph | `KILL_WEAK_TEMPORAL` |

## Representative exact data

The complete 96-box transcript is frozen in `CANONICAL.txt`.  These rows show
the signals used at the gate.

| handle and box | states | image | max fibre | recurrent | max tail | selected cycle census |
|---|---:|---:|---:|---:|---:|---|
| `QCD`, `p=41` | 41 | 30 | 2 | 21 | 4 | one fixed point, ten 2-cycles |
| `ESP`, `p=13` | 169 | 91 | 2 | 17 | 18 | 13 fixed points, one 4-cycle |
| `AHP`, `p=19` | 361 | 181 | 19 | 91 | 5 | 19 fixed, nine 2-, eighteen 3-cycles |
| `CCS`, `p=43` | 43 | 22 | 2 | 22 | 1 | 22 fixed points |
| `HUR`, `n=5` | 14,400 | 14,400 | 1 | 14,400 | 0 | periods `1,2,3,4,5,6,8,10,12` |
| `MRK`, `p=23` | 461 | 461 | 1 | 461 | 0 | periods through 120 |
| `CLU`, `p=13` | 169 | 145 | 13 | 45 | 11 | periods `1,2,3,4,6` |
| `CLU`, `p=19` | 361 | 361 | 1 | 361 | 0 | periods through 20 |
| `SFE`, `p=7,n=4` | 2,801 | 64 | 2,402 | 1 | 4 | one fixed point |
| `GCM`, `p=7` | 2,401 | 545 | 27 | 545 | 1 | periods `1,2,4` |
| `BHD`, `p=11` | 15,984 | 1,283 | 132 | 1 | 3 | one fixed sink |
| `PRE`, `p=5,n=2` | 15,625 | 2,605 | 126 | 125 | 3 | 125 fixed terminals |
| `KRC`, `n=8` | 1,430 | 1,430 | 1 | 1,430 | 0 | `2:1,4:1,8:8,16:85` cycles |
| `NWT`, `p=43` | 43 | 29 | 3 | 9 | 8 | three fixed points, two 3-cycles |

## 1. `QCD`: quadratic-character drift

For an odd prime `p`, let `chi` be the Legendre symbol with `chi(0)=0` and
define

```text
F_p(x)=x+chi(x) mod p.                                      (1)
```

### Exact structural axis

Zero is fixed.  Every other recurrent component is an adjacent transition

```text
a (quadratic residue) <-> a+1 (quadratic nonresidue).
```

The number of 2-cycles is

```text
C_2(p)=(p-chi(-1))/4.                                      (2)
```

Every fibre has size at most two.  If `D_2(p)` denotes the number of targets
with two preimages, then direct character summation gives

```text
D_2(p)=(p-1+chi(2)-chi(-2))/4 +(1+chi(-1))/2,               (3)
|image(F_p)|=p-D_2(p).                                      (4)
```

The verifier checks (2)--(4) for thirteen primes through 43.

### Fatal temporal obstruction

Away from zero, an orbit moves monotonically by `+1` along a run of quadratic
residues and by `-1` along a run of nonresidues until it reaches a residue to
nonresidue boundary.  Thus the tail-depth histogram is a run-length statistic
of the cyclic quadratic-character word.  The maximum tail already changes as

```text
p:        3  5  7  11 13 17 19 23 29 31 37 41 43
max tail: 0  1  1   2  3  2  3  3  3  3  3  4  4.
```

Longest and prescribed runs of quadratic residues and nonresidues are a
classical, still arithmetically deep subject.  Repackaging their complete word
statistics as a functional-graph temporal polynomial would not be a new
closed all-prime theorem engine.  `QCD` therefore has one exact axis, not two.

## 2. `ESP`: elementary-symmetric plane map

Define

```text
E_p(x,y)=(xy,x+y).                                          (5)
```

For a target `(u,v)`, the source coordinates are the ordered roots of

```text
T^2-vT+u=0.                                                 (6)
```

Consequently

```text
|image(E_p)|=p(p+1)/2,
#{targets with fibre 1}=p,
#{targets with fibre 2}=p(p-1)/2.                           (7)
```

This is precisely the degree-two symmetric quotient/Vieta calculation.  It is
complete but structurally standard.  The forward graph has no uniform small
silhouette: max tails at `p=3,5,7,11,13,17,19,23` are respectively
`4,4,8,13,18,14,26,29`, while its nontrivial cycle periods change among
`4,6,8,10`.  No second all-prime axis survived.

## 3. `AHP`: totalized arithmetic--harmonic pair

On `F_p^2`, put

```text
H_p(x,y)=(s,xy inv0(s)),  s=x+y.                            (8)
```

The product is invariant.  The singular target `(0,0)` has exactly `p`
preimages.  If the target first coordinate `u` is nonzero, its sources are the
ordered pairs determined by

```text
T^2-uT+uv=0.                                                (9)
```

Hence every nonsingular fibre has size `0,1,2`, and

```text
|image(H_p)|=(p^2+1)/2,  max fibre=p uniquely at (0,0).     (10)
```

The exact graph does not stabilize: recurrent sizes for
`p=7,11,13,17,19,23` are `25,21,61,113,91,89`, and max tails are
`1,3,3,2,5,5`.  On invariant-product leaves the induced coordinate update is
a degree-two rational map, so (10) does not supply a closed temporal theorem.

## 4. `CCS`: character-controlled squaring

Define

```text
S_p(x)=x       if chi(x)>=0,
S_p(x)=x^2     if chi(x)=-1.                                (11)
```

There are `(p+1)/2` fixed points, every other point has depth one, and the
image is exactly the set of squares together with zero.  The fibre refinement
depends only on whether the two square roots of a residue are themselves
residues.  This is a complete but one-step graph, so it is rejected by the
theorem-size gate without needing an owner claim.

## 5. `HUR`: two-strand Hurwitz move

For permutations `a,b in S_n`, define

```text
B(a,b)=(b,b^{-1}ab).                                       (12)
```

It preserves `ab` and has explicit inverse

```text
B^{-1}(c,d)=(cdc^{-1},c).                                  (13)
```

The `n=5` carrier already has periods through 12, but all 14,400 states are
recurrent and every fibre is one.  This is literally a Hurwitz braid action;
the action and its finite orbits are directly studied in the primary
literature.  There is no independent inverse/fibre axis to subtract from that
owner.

## 6. `MRK`: Markoff Vieta rotor

On

```text
M_p={(x,y,z):x^2+y^2+z^2=3xyz},
R(x,y,z)=(y,z,3yz-x),                                      (14)
```

the inverse is `(a,b,c)->(3ab-c,a,b)`.  Thus this is a permutation, with
periods already reaching 138 at `p=17` and 120 at `p=23`.  Bourgain--Gamburd--
Sarnak directly study the group of morphisms generated by these Vieta
involutions on congruence solutions of the same Markoff surface.  The exact
rotor is attractive data, but the fibre theorem is identically one and the
temporal question belongs to the owned action.

## 7. `CLU`: totalized rank-two cluster map

Define

```text
C_p(x,y)=(y,(1+y^2)inv0(x)).                               (15)
```

The exact bifurcation is conspicuous.  For every tested `p=3 mod 4`, the map
is a permutation of all `p^2` points.  For tested `p=1 mod 4`, it has a unique
fibre of size `p` and long exceptional tails (`3,11,15,27` for
`p=5,13,17,29`).  Nevertheless, away from singular coordinates the recurrence
is

```text
x_{m+2}x_m=1+x_{m+1}^2,                                   (16)
K=(x_m^2+x_{m+1}^2+1)/(x_m x_{m+1}),
x_{m+2}=Kx_{m+1}-x_m.                                     (17)
```

Equation (16) is the affine rank-two cluster recurrence.  Once `K` is fixed,
(17) is a two-dimensional linear matrix iteration, a permanent intake kill.
The zero-totalized singular boundary is too small to support a second paper
after both owned engines are subtracted.

## 8. `SFE`: squarefree erosion

For `p>n`, on all monic polynomials of degree at most `n`, define

```text
D(f)=monic gcd(f,f').                                      (18)
```

If `f=prod_i P_i^{m_i}`, then

```text
D(f)=prod_i P_i^{m_i-1},                                   (19)
```

with zero exponents removed.  Therefore one is the unique recurrent point and
the depth is `max_i m_i`, sharply `n` at `f=t^n`.  This clean theorem is
exactly repeated-factor erosion by the classical derivative--GCD squarefree
factorization step.  Both the algorithm owner and the occupied
valuation/multiplicity proof engine kill it.

## 9. `GCM`: Gram cube

On `2 by 2` matrices over `F_p`, define

```text
G(A)=AA^T A.                                                (20)
```

The small graphs are shallow but field-sensitive: at `p=3` it is a
permutation with periods one and two; at `p=5,7` all tails have length at most
one but image and fibre distributions differ sharply.  Any full proof must
classify matrices under the bilinear form and reduce the iteration to scalar
or block matrix powers.  This is precisely the generic matrix-polynomial/
power engine excluded at intake, while the observed temporal axis is only one
step.

## 10. `BHD`: binary-Hessian graded descent

The carrier is the disjoint union of typed binary cubics, binary quadratics,
scalars, and a sink.  For

```text
f=aX^3+bX^2Y+cXY^2+dY^3,
```

the update is

```text
(a,b,c,d) -> (3ac-b^2, 9ad-bc, 3bd-c^2)
(A,B,C)   -> B^2-4AC
s         -> sink.                                         (21)
```

The temporal polynomial is imposed by the type grading:

```text
1 + p z + p^3 z^2 + p^4 z^3.                              (22)
```

Hessian and discriminant are classical covariants, and modern work already
iterates Hessians and studies finite-field Hessian graphs on elliptic moduli.
Equation (22) is therefore an artificial three-level wrapper, not an
independent dynamical theorem.

## 11. `PRE`: polynomial-remainder Euclidean dynamics

On polynomial pairs of degree at most `n`, define

```text
(f,g)->(g,rem(f,g)),     (f,0)->(f,0).                      (23)
```

Every recurrent point is a terminal `(f,0)`.  The degree of the second
coordinate strictly decreases after each nonterminal update, giving max tail
at most `n+1`; exact boxes attain the bound.  The fibres are division-algorithm
fibres.  This is literally the polynomial Euclidean algorithm, already a
primary literature object and internally too close to P131 Euclidean queues.

## 12. `KRC`: Kreweras complement

Represent `pi in NC(n)` as its permutation and put

```text
K(pi)=pi^{-1}c,   c=(1 2 ... n).                            (24)
```

The carrier has Catalan size and `K` is a permutation of order dividing `2n`.
For `n=8` the exact cycle census is

```text
one 2-cycle, one 4-cycle, eight 8-cycles, eighty-five 16-cycles.
```

Kreweras orbits and their cyclic-sieving formulas are directly owned.  The
map also lies in an occupied noncrossing-partition ecosystem and has fibre one,
so it cannot furnish the required independent second axis.

## 13. `NWT`: zero-totalized cubic Newton map

For `p>3`, let

```text
N_p(x)=x-(x^3-x)inv0(3x^2-1).                              (25)
```

The three roots `0,1,-1` are fixed, and the two critical-denominator points
are additional fixed points exactly when `chi(3)=1`.  Thus

```text
#fixed=3+2[chi(3)=1].                                      (26)
```

For a nonsingular source, `N_p(x)=y` is equivalent to

```text
2x^3-3yx^2+y=0,                                            (27)
```

so every fibre has size at most four after the possible totalized critical
source is added.  The verifier checks (26)--(27).  But the graph is irregular:
at `p=43` it has max tail eight and two 3-cycles; at `p=41` max tail seven and
periods two and four; other primes show periods six.  Newton maps are already
a mature rational-dynamics family, and this convention leaves no closed
all-prime temporal axis.

## Freeze-gate conclusion

No candidate is authorized for a focused freeze gate.  In particular:

- do not promote `QCD` by calling a quadratic-character run statistic a new
  temporal formula;
- do not split the singular boundary of `CLU` away from its rank-two cluster
  and matrix recurrence merely to manufacture a second axis;
- do not treat the rich periods of `HUR`, `MRK`, or `KRC` as enough when their
  fibres are identically one and their actions are directly owned;
- do not reuse `SFE`, `GCM`, `BHD`, or `PRE` under altered grading or notation.

The replacement2 algebraic lane therefore returns **no paper-level survivor**.
All decisions remain `HOLD_EXTERNAL`.
