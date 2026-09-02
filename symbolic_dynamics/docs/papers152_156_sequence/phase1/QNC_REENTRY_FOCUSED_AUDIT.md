# QNC reserve re-entry focused freeze-gate audit

**Audit date:** 2026-09-02 UTC.  
**Gate verdict:** `KILL_DIRECT`.  
**Mathematical status:** the stated all-odd-prime, all-precision contract passed
independent exact replay.  
**External status:** `HOLD_EXTERNAL`.  
**Intake effect:** no paper number, no paper draft, and no novelty, priority, or
publication claim.

## 1. Scope and decision rule

The re-entry candidate is the finite self-map

```text
X_{p,e}=p Z / p^e Z,
Q_{p,e}(x)=x(x+p) mod p^e,                  p odd prime, e>=2.
```

It was retained below the freeze line in the P147--P151 algebraic replacement
scout.  This audit rechecked the literal formula, all useful affine aliases,
the primary-source citation chain, the temporal theorem, the complete inverse
atlas, and a fresh exact implementation.

The decision rule is deliberately stricter than literal-string ownership.  A
candidate is killed if a prior general theorem specializes with no structural
freedom to one of its two claimed theorem axes and the remaining axis is only
an elementary instance calculation.  An exact-map title or an identical
notation is not required for a direct theorem-engine collision.

That is what happens here.  The mathematical formulas are correct, but
desJardins--Zieve already give the exact critical-residue-class fibre
distribution containing QNC.  Wright supplies the standard discriminant and
square-root labels.  The only substantial formula not printed by those sources
is the elementary valuation-layer temporal polynomial.  QNC therefore no
longer has two independent paper-sized axes.

## 2. Coordinate normalization and alias coverage

Three bijective presentations were checked before the owner search.

### 2.1 Scaled maximal-ideal coordinate

Write `x=pu`.  Division by `p` identifies `X_{p,e}` with
`Z/p^(e-1)Z`, and the induced map is

```text
T(u)=p u(u+1) mod p^(e-1).                  (1)
```

This is the correct form for searches involving a maximal ideal, a contracting
ball, or a residue-ring local coordinate.

### 2.2 Translation to a monic centered quadratic

Because `2` is a unit, put `y=x+p/2` in `Z/p^eZ`.  Then

```text
y |-> y^2+c,        c=p/2-p^2/4=p(2-p)/4,  (2)
```

on the translated ball `p/2+pZ/p^eZ`.  Its fixed point `p/2` has multiplier
`p`.  Thus QNC is also the finite-level dynamics of a monic quadratic on an
attracting residue ball.

### 2.3 Unit-centered coordinate

On `Z/p^(e-1)Z`, let `z=1+2u=1+2x/p`.  Equation (1) becomes

```text
g(z)=1+(p/2)(z^2-1).                        (3)
```

The independent verifier checks (1)--(3) at every state in every test box.
None of the three coordinate changes repairs the owner collision below.

## 3. Owner-first search log and bounded non-hits

The search used arXiv author manuscripts, primary publisher records, and full
text.  Search-result snippets were used only to locate sources, never as the
basis of the verdict.

Representative queries actually run included:

```text
"x(x+p)" p-adic dynamics
"x^2+px" "functional graph"
"x^2 + p x" "functional graph" modulo
"p x+x^2" p-adic dynamics attracting fixed point
"p u(u+1)" p-adic dynamics OR modulo
"1+(p/2)(z^2-1)" dynamics
"p(2-p)/4" quadratic dynamics
quadratic polynomial p-adic attracting fixed point multiplier p maximal ideal
quadratic dynamics on residue rings maximal ideal attracting ball
functional graph quadratic polynomial modulo p^n
functional graphs Z/p^nZ polynomial
polynomial functional graph modulo prime powers cycle lifting
```

The literal dynamical formulas did not produce an exact-map paper in this
bounded search.  One literal `x^2+px` hit was Dwivedi--Mittal--Saxena,
[*Counting basic-irreducible factors mod p^k in deterministic poly-time and
p-adic applications*](https://arxiv.org/abs/1902.07785).  Its example concerns
factorization and root counting, not iteration; it is a false dynamical hit.

The decisive source appeared through the conceptual and citation-chain search,
not the literal formula.  Fan--Liao explicitly identify desJardins--Zieve as
the source of their odd-prime finite-level induction.  Reading the latter's
tail section exposed an exact specialization to the QNC carrier.

The non-hit statement above is bounded.  The search was English-heavy and did
not exhaust every book, thesis, non-indexed journal, non-English source, or
every affine conjugate.  It establishes neither novelty nor absence of an even
closer owner.  Since a decisive owner was found anyway, no stronger non-hit
claim is needed.

## 4. Citation chain and full-text findings

### 4.1 desJardins--Zieve: decisive direct specialization

David L. desJardins and Michael E. Zieve,
[*On the Structure of Polynomial Mappings Modulo an Odd Prime Power*
(`Polynomial Mappings mod p^n`)](https://arxiv.org/abs/math/0103046),
arXiv:math/0103046.

Full-text points checked: Sections 3, 5, and especially Section 6.4, “Tails.”
For an integer polynomial `f`, an odd prime `p`, and a cycle
`(x_1,...,x_k)` modulo `p`, Section 6.4 treats the union of residue classes
above that cycle at level `p^n`.

Two statements specialize directly to QNC.

1. If the derivative vanishes modulo `p` on the cycle, the lifted residue
   classes contain a single cycle and every other point is on a tail.  For
   `f(x)=x^2+px`, the class `0 mod p` is a fixed class and
   `f'(0)=p=0 mod p`; its level-`e` lift is exactly `X_{p,e}`.
2. If in addition the second derivative is nonzero modulo `p`, the paper gives
   the positive-fibre sizes and their multiplicities exactly: for
   `1<=j<n/2`, there are

   ```text
   (p-1)p^(n-2j-1)/2 targets with fibre size 2p^j,                 (4)
   ```

   together with one target whose fibre has size `p^floor(n/2)`.
   Here `f''(0)=2` is a unit, so the hypothesis holds for every odd `p`.

This is not merely a general framework that could be adapted in many ways.
Set `n=e` and put `j=r+1`.  QNC's noncritical discriminant layers become

```text
fibre size       2p^(r+1)=2p^j,
target count      (p-1)p^(e-2r-3)/2
                =(p-1)p^(e-2j-1)/2,                              (5)
```

which is exactly (4).  QNC's discriminant-zero fibre is

```text
p * p^floor((e-2)/2) = p^floor(e/2),                              (6)
```

the unique remaining fibre in the cited result.

Consequently the cited distribution already gives, by direct specialization:

- the entire positive-fibre histogram;
- the image size, obtained by summing the target multiplicities;
- the unique maximum `p^(e/2)` when `e` is even;
- the maximum `2p^((e-1)/2)` with `(p-1)/2` maximizers when `e` is odd.

These are precisely the claimed image and parity-switch results.  The source
does not attach QNC's explicit discriminant label to each target and does not
print its exact depth polynomial, but it owns the whole distributional inverse
axis.

### 4.2 Fan--Liao: same local-dynamics engine, qualitative attraction

- Aihua Fan and Lingmin Liao,
  [*On minimal decomposition of p-adic polynomial dynamical systems*](https://arxiv.org/abs/1010.5583),
  arXiv:1010.5583; *Advances in Mathematics* 228 (2011),
  DOI [`10.1016/j.aim.2011.06.032`](https://doi.org/10.1016/j.aim.2011.06.032).
- Shilei Fan and Lingmin Liao,
  [*Dynamics of convergent power series on the integral ring of a finite
  extension of Q_p*](https://arxiv.org/abs/1401.1062), arXiv:1401.1062.

The first paper's Section 2 says that its odd-prime core follows
desJardins--Zieve.  It classifies a derivative-zero lifted cycle as “growing
tails” and proves that its clopen lift consists of an attracting periodic orbit
and its basin.  Its detailed classification of arbitrary quadratic
polynomials is only for `p=2`, so it does not separately print the odd-prime
QNC graph.  The second paper extends the minimal-decomposition mechanism to
integral rings of finite extensions and again traces the finite-level
prediction method to desJardins--Zieve.  It gives a general qualitative owner
boundary, not a rescue from the direct fibre result.

Shilei Fan and Lingmin Liao,
[*Dynamics of the square mapping on the ring of p-adic integers*](https://arxiv.org/abs/1408.4574),
arXiv:1408.4574, studies `x -> x^2` on every `Z/p^nZ` and `Z_p` and gives its
complete minimal decomposition.  QNC's centered form is `y^2+p(2-p)/4`, not
the square map, so this source is a nearest family member rather than the
decisive exact specialization.

### 4.3 Wright: direct discriminant and root-count input

Steve Wright,
[*On the Quadratic Formula Modulo N*](https://arxiv.org/abs/1507.07513),
arXiv:1507.07513; *Journal of Algebra, Number Theory and Applications* 7
(2007), 33--68.

The full text treats the discriminant reduction for arbitrary quadratic
congruences, gives prime-power corollaries, and records Gauss's exact number of
square roots modulo a prime power.  Since QNC reduces to a monic quadratic and
`2` is invertible, the exact quadratic formula applies without an obstruction.
Thus the target labels in Section 6 below are a clean specialization of
standard direct input.  They cannot be used as an independent owner axis.

### 4.4 Anashin and later prime-power graph frameworks

Vladimir Anashin,
[*Ergodic Transformations of the Space of p-adic Integers*](https://arxiv.org/abs/math/0602083),
arXiv:math/0602083, characterizes compatible measure-preserving and ergodic
maps by their residue-level permutations and treats ergodicity on small
spheres.  QNC is a highly non-bijective contraction, so this is a general
background framework, not an exact graph owner.

Tomoki Nara,
[*Lifting of cycles in functional graphs*](https://arxiv.org/abs/2509.16234),
arXiv:2509.16234, develops cycle lifting for polynomial functional graphs on
`Z/p^nZ`.  The paper explicitly focuses on cycles, and full-text searches for
“preimage” and “tree” produced no theorem competing with the QNC inverse
atlas.  QNC has only the fixed cycle zero, so this source adds no surviving
axis.

Bernard Mans, Min Sha, Igor E. Shparlinski, and Daniel Sutantyo,
[*On Functional Graphs of Quadratic Polynomials*](https://arxiv.org/abs/1706.04734),
arXiv:1706.04734, and Sergei Konyagin et al.,
[*Functional Graphs of Polynomials over Finite Fields*](https://arxiv.org/abs/1307.2718),
arXiv:1307.2718, work over finite fields, especially prime fields.  They do not
cover the nilpotent residue-ring carrier.  Somer--Križek's power-digraph work
concerns `x -> x^2` or `x -> x^k` modulo composite integers, again not the
shifted QNC polynomial.  These are nearest graph literature, not the decisive
owner; desJardins--Zieve is.

## 5. Independent temporal derivation

Let `tau(x)` be the first time at which the orbit reaches zero.  Zero is fixed.
For nonzero `x`, there are two disjoint regimes.

### 5.1 Inner layers

If `v_p(x)=a>=2`, then `x+p` has valuation one and hence

```text
v_p(Q(x))=min(e,a+1).                                           (7)
```

Thus `tau(x)=e-a` on this layer.

### 5.2 Outer layer and the single cancellation

If `x=pu` with `u` a unit, then

```text
Q(x)=p^2 u(u+1),
v_p(Q(x))=min(e,2+v_p(u+1)).                                   (8)
```

After this first step, any nonzero image lies in an inner layer and (7)
applies.  Therefore

```text
tau(pu)=e-1-min(v_p(u+1),e-2).                                 (9)
```

All nonzero points reach zero, so zero is the unique recurrent point.  The
element `x=p` has `u+1=2` a unit and attains the sharp depth `e-1`.

For `e=2`, every nonzero point has depth one:

```text
D_{p,2}(z)=1+(p-1)z.                                           (10)
```

Assume `e>=3`.  The coefficient at depth one has two contributions:

- `v_p(x)=e-1`, giving `p-1` points;
- outer units with `u=-1 mod p^(e-2)`, giving `p` points.

Hence it is `2p-1`.  For `2<=t<=e-2`, the inner layer
`v_p(x)=e-t` and the outer cancellation layer
`v_p(u+1)=e-1-t` each contain `(p-1)p^(t-1)` points.  Finally, depth
`e-1` consists of the outer units for which both `u` and `u+1` are units;
there are `(p-2)p^(e-2)` of them.  Consequently

```text
D_{p,e}(z)
 =1+(2p-1)z
  +2(p-1) sum_{t=2}^{e-2} p^(t-1) z^t
  +(p-2)p^(e-2) z^(e-1).                                      (11)
```

The coefficients sum to `p^(e-1)`, the carrier size.  Equations (7)--(11)
were derived independently of the owner specialization and checked literally.

## 6. Independent every-target fibre derivation

Write a source as `x=pu`, where `u` is taken modulo `p^(e-1)`.  Every image is
divisible by `p^2`.  For a target `y=p^2w`, put `k=e-2`.  The inverse equation
is

```text
u(u+1)=w mod p^k
iff (2u+1)^2=Delta:=1+4w mod p^k.                              (12)
```

Each solution modulo `p^k` has exactly `p` lifts to a source coordinate modulo
`p^(k+1)`.  Let `R_k(Delta)` denote the number of square roots of `Delta`
modulo `p^k`.  Then every target satisfies

```text
|Q^(-1)(y)| = 0                         if p^2 does not divide y,
              p R_k(1+4w)               if y=p^2w.              (13)
```

For `k>=1`, the standard odd-prime root count is

```text
R_k(Delta)=p^floor(k/2)       if Delta=0 mod p^k;
            0                 if v_p(Delta)<k is odd;
            2p^r              if v_p(Delta)=2r<k and the unit
                              part is a square mod p;
            0                 otherwise.                        (14)
```

Set `R_0(0)=1`.  Since `w -> 1+4w` is a bijection, the image cardinality is
the number of squares modulo `p^k`:

```text
|im Q|=1+(p-1)/2 sum_{r=0}^{floor((k-1)/2)} p^(k-2r-1).         (15)
```

When `k` is even, the unique discriminant-zero target has the largest fibre,
of size `p^(k/2+1)`.  When `k` is odd, the nonzero discriminants of valuation
`k-1` with square unit part give the largest fibre
`2p^((k-1)/2+1)`; there are `(p-1)/2` such targets.  This proves the parity
switch and target labels.

Equations (12)--(15) are correct.  However, (14) is standard Wright/Gauss
input, while the unlabeled distribution, image, and parity switch are already
the direct specialization (4)--(6).  Relabelling the old distribution by its
discriminants does not restore an independent theorem axis.

## 7. Independent exact replay and frozen transcript

The new verifier is
[`verify_qnc_reentry.py`](../scouting/algebraic/verify_qnc_reentry.py).  It
does not import the P147--P151 implementation.  It checks:

- literal carrier invariance and all three coordinate presentations;
- the two valuation regimes and the first zero time of every state;
- the complete coefficient vector (10)--(11), the unique fixed point, and a
  sharp witness;
- (13)--(14) for every target, including empty fibres;
- the image census, the complete positive-fibre histogram, total fibre mass,
  and the labelled even/odd maximizers.

The box set contains

```text
p=3,  e=2..10;
p=5,  e=2..7;
p=7,  e=2..6;
p=11, e=2..5;
p=13, e=2..5;
p=17, e=2..4;
p=19, e=2..4.
```

Result:

```text
34 boxes
128,162 states
1,025,731 exact assertions
PROFILE_SHA256=b0c98b5c19d535f8a21a85f5fd18a309461fb88779733eea8f7396145943b22b
STATUS PASS
```

The frozen transcript is
[`QNC_REENTRY_CANONICAL.txt`](../scouting/algebraic/QNC_REENTRY_CANONICAL.txt).
A process-separated cold replay compared with `diff -u` produced no diff.

Enumeration is evidence against implementation or formula mistakes; it is not
a literature or novelty claim.

## 8. Claim subtraction and final verdict

The following inputs receive zero credit:

- valuation arithmetic on `Z/p^eZ` and the attracting-ball vocabulary;
- affine normalization of a monic quadratic;
- completing the square and odd-prime square-root counts;
- desJardins--Zieve's exact critical-class fibre distribution;
- the image and parity-sensitive maximum obtained from that distribution;
- Fan--Liao's generic growing-tail/attracting-basin classification.

After subtraction, the genuine map-specific residual is the two-regime clock,
its exact layer polynomial, and the explicit attachment of standard
discriminant labels to the already-owned fibre histogram.  That residual is
mathematically clean but no longer supports two independent theorem axes.

**Final gate: `KILL_DIRECT`.**  QNC is permanently removed from the P152--P156
replacement pool.  The kill is caused by a direct theorem specialization, not
by a failed formula.  Do not narrow it to a temporal-only note, revive it under
one of (1)--(3), assign it a paper number, or state novelty.  All records remain
`HOLD_EXTERNAL`.
