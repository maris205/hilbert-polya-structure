# Hostile owner/value gate: X01 divisor tent and C1 transpose self-commutator

**Review posture:** independent, fail-closed owner/value audit.  Mathematical
correctness, mechanical verification, internal collision, and short-paper value
are separate gates: passing one does not repair failure of another.

**Scope read:** the two proof dossiers, their scouting records, verifier source
and canonical output, and the P1--P121 sequence ledgers relevant to the two
mechanisms.  I reran both exact programs and made an additional literal depth
enumeration for C1.  The external status of both candidates remains
`HOLD_EXTERNAL`.

## Executive decision

| candidate | theorem audit | mechanical-translation risk | P1--P121 collision | short-paper value | decision |
|---|---|---|---|---|---|
| X01, complementary-divisor tent | formulas (1)--(17) survive the present audit | **fatal/high**: after valuations, essentially the complete package is the doubling power map on `Z/(2a)` modulo sign, followed by direct products | **exact historical candidate collision** with the P102-round `balanced-divisor tent`; no numbered-manuscript identity located | too little residual after owner/mechanism subtraction | **KILL** |
| C1, `A -> AA^T-A^TA` | universal collapse and fibre formulas pass, but both advertised depth censuses are **false** | **high**: one-line involution collapse plus an elementary three-variable parametrization | **exact literal collision** with B2B-08 in the P117--P121 scout, already killed as theorem-thin | insufficient even after repairing the false theorem | **KILL** |

Neither item may receive a paper number from the current dossier.  The labels
above are value/collision decisions, not assertions that every displayed
calculation is wrong.

## 1. X01: complementary-divisor tent

### 1.1 Formula-by-formula audit

Let `N=product p_i^(a_i)` and write `d=product p_i^(e_i)`.

1. **Literal valuation rule, (1)--(3): correct.**  Primewise subtraction of
   the minimum valuation from the maximum gives
   `v_p(Phi_N(d))=|2e-a|`, so the divisor map is the direct product of the
   stated local maps.

2. **Sign-quotient model, (4)--(5): correct.**  With `y=a-e`, folding
   doubling on `Z/(2a)` modulo `y~-y` gives `2 min(y,a-y)`, exactly the
   complementary coordinate of `|2e-a|`.

3. **Pointwise preperiod and period, (6)--(8): correct.**  If the additive
   order of `y` is `M=2^alpha m` with `m` odd, doubling strips exactly
   `alpha` powers of two.  The sign quotient cannot shorten that tail: an
   earlier return would require an even divisor of one of the odd integers
   `2^k-1` or `2^k+1`.  On the remaining odd cyclic group, the least quotient
   period is the least `k` with `2^k=+/-1 (mod m)`.  Maximum and lcm are the
   correct direct-product tail and period operations.

4. **Recurrence and layers, (9)--(12): correct.**  The condition
   `2^(v_2(a)+1) | a-e` is exactly `alpha=0`; its local count is
   `(odd(a)+1)/2`.  Counting multiples of
   `2^max(v_2(2a)-t,0)` in `[0,a]` gives (11), and differencing gives the
   exact layers.

5. **Iterated fibres, (13): correct.**  The two congruences
   `2^t y=+z,-z (mod 2a)` give the generic count, while `z=0` and `z=a` are
   precisely the self-sign exceptions.  The four cases also pass endpoint
   tests (`a=1`, saturated `t`, and targets `j=0,a`).

6. **Fixed iterates, cycles, and zeta, (14)--(17): correct.**  The `+` and
   `-` solution subgroups intersect only at zero; the other self-inverse
   residue `a` solves neither congruence.  Burnside therefore gives (14).
   Products, Möbius inversion, and the finite Euler product then follow.

The canonical pilot rerun reproduced the stored output byte for byte and
reported `348392` assertions.  This is credible bounded falsification support,
not an ownership or value certificate.

### 1.2 Mechanical-translation gate

The dossier itself supplies an exact conjugacy/quotient reduction, not merely
an analogy.  Once (2) and (5) are written down:

- tails and periods are the standard `2`-primary/unit decomposition of a
  power map on a finite cyclic group;
- fibres are linear congruence counts followed by the sign quotient;
- fixed points are Burnside counts for `2^n y=+/-y`;
- the global theorem is a Cartesian product; and
- exact cycles and zeta are mechanical Möbius/Euler bookkeeping.

The valuation derivation and the cyclic-quotient derivation are useful checks,
but they are not two independent substantive proof engines: the former merely
identifies the arithmetic map with the latter coordinate system.  The residual
is therefore an exact worked arithmetic realization of a known mechanism, not
a new dynamical engine.

Relevant primary literature confirms that the surrounding mechanisms are
already mature.  Scheicher--Sirvent--Surer study tent-map dynamics and transfer
of periodicity through beta-expansions in
[JLMS 93 (2016), 319--340](https://doi.org/10.1112/jlms/jdv071).
Qureshi--Reis give structural functional graphs for power maps on finite
groups, including the abelian case, in
[arXiv:2107.00584](https://arxiv.org/abs/2107.00584).  Neither source was found
to state this literal gcd/lcm divisor map, but that bounded non-hit does not
create enough residual value after the exact reduction.

### 1.3 Internal collision

This is not a fresh lane in the project.  The P102--P106 candidate ledger
already records `balanced-divisor tent`, with the same diagnostic fixed-count
formula `gcd(2^k +/- 1,m)`, and marks it `RESERVE OWNER-HEAVY` because the
normalized action is the classical tent map
(`docs/papers102_106_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md`, line
30).  The stage report likewise lists balanced divisor tents among the
rejected/reserved candidates.  X01 enriches that old candidate with layers and
fibres, but does not change its exact conjugacy or owner/value bottleneck.

This is an exact **historical sequence-candidate collision**, although no
numbered P1--P121 manuscript was found to have frozen the literal map.  P100's
valuation digit eroder and P107's ideal dynamics are only adjacent collisions;
they are not needed for the kill decision.

### 1.4 Allowed claim ceiling and reconsideration conditions

**Permitted archival ceiling only:** “For the literal map (1), valuations give
an arithmetic realization of sign-quotient doubling, from which the displayed
pointwise, layer, fibre, fixed-count, and zeta formulas follow.”

It may **not** claim a new tent-map mechanism, a new finite power-map method, a
new orbit-classification method, new zeta machinery, or a fresh project lane.
Static divisor arithmetic, unitary-divisor facts, multiplicative orders,
Burnside, products, Möbius inversion, and zeta conversion receive zero credit.

Reconsideration requires all of the following; adding examples or repackaging
the current formulas does not suffice:

1. identify explicitly that X01 resurrects the P102-round balanced-divisor
   tent and explain what genuinely new theorem now clears that old kill gate;
2. add a nonmechanical arithmetic theorem not inherited from cyclic doubling,
   sign quotient, or Cartesian products;
3. obtain a second substantive proof route, rather than a second coordinate
   derivation of the same quotient;
4. complete a specialist direct-owner audit for the literal divisor operator;
   and
5. show short-paper value after all generic tent/power-map and static divisor
   facts are removed.

Until then the decision is **`KILL / ARCHIVE THE CORRECT DOSSIER`**.

## 2. C1: transpose self-commutator

### 2.1 Correct statements

For an involutive associative algebra,
`Delta(x)=xx^*-x^*x` is self-adjoint, and every self-adjoint input maps to
zero.  Hence `Delta^2=0`, zero is the only periodic point, and every orbit has
depth at most two.  This universal identity is correct in every characteristic.

For `M_2(F_q)`, the coordinate formulas are also correct.

- In odd characteristic, with `u=b-c`, `v=b+c`, `w=a-d`, one has
  `Delta(A)=((uv,-uw),(-uw,-uv))`.  The image has size `q^2`, the zero fibre
  has size `q^3+q^2-q`, and every nonzero image point has `q(q-1)` preimages.
- In characteristic two, `u=v=b+c`, `w=a+d`, and
  `Delta(A)=((u^2,uw),(uw,u^2))`.  The image has size `q^2-q+1`, the zero
  fibre has size `q^3`, and every nonzero image point has `q^2` preimages.

These fibre formulas agree with the literal rerun over
`F_2,F_3,F_4,F_5,F_7,F_8,F_9`.

### 2.2 Fatal theorem error: image is not the depth-one layer

Equations (3) and (7) in the dossier are false.  They silently identify
`im Delta` with the depth-one set.  But `Delta^2=0` says only
`im Delta subseteq ker Delta`, and here the inclusion is strict.  The depth
partition is

```text
L0 = 1,
L1 = |ker Delta|-1 = |Delta^{-1}(0)|-1,
L2 = q^4-|ker Delta|.
```

Therefore the corrected formulas are

```text
odd characteristic:
  (L0,L1,L2) = (1, q^3+q^2-q-1, q^4-q^3-q^2+q),

characteristic two:
  (L0,L1,L2) = (1, q^3-1, q^4-q^3).
```

Literal enumeration exposes the discrepancy immediately:

| field | dossier claim | actual/corrected |
|---|---:|---:|
| `F_2` | `(1,2,13)` | `(1,7,8)` |
| `F_3` | `(1,8,72)` | `(1,32,48)` |
| `F_5` | `(1,24,600)` | `(1,144,480)` |
| `F_7` | `(1,48,2352)` | `(1,384,2016)` |

The stored verifier reproduces byte for byte and reports `68497` assertions,
but it does **not** verify the claimed depth census.  In
`alg_transpose_self_commutator_verify.py`, lines 126/131 merely assign the
closed-form tuple, and line 139 checks only that its three entries sum to
`q^4`.  It never computes a state's least depth.  Thus the canonical `PASS`
is compatible with a false central theorem and cannot support dossier lines
62--65, 92--99, or the statement at lines 103--107 that (2)--(7) were checked.

After correction, a full graph description must distinguish four vertex
roles:

1. zero, whose indegree is the zero-fibre size;
2. nonzero image points, which lie in the kernel and have the stated positive
   nonzero fibre size;
3. kernel points outside the image, which have depth one and indegree zero;
4. points outside the kernel, which have depth two and indegree zero.

The current “entire directed functional graph” sentence omits this necessary
`im Delta` versus `ker Delta` separation.

### 2.3 Mechanical value and internal collision

Even corrected, the temporal result is the one-line involution observation
`image subset fixed locus -> next image zero`.  The `2 x 2` refinement is a
single elementary parametrization by `(u,v,w)` with one free coordinate.
These are reliable calculations, but not two substantive proof routes and not
enough residual for a short paper.

More decisively, the **identical literal map** already appears as B2B-08 in
the P117--P121 algebraic Phase-2B scout:

```text
K(A)=AA^T-A^TA on M_d(F_q); K(A) is symmetric, hence K^2=0;
KILL: theorem-thin.
```

The accompanying discussion says there is no nontrivial temporal
stratification and that the mechanism is too close to one-line matrix-image
collapses already firewalled by P103/P109
(`docs/papers117_121_sequence/scouting/ALGEBRAIC_PHASE2B_SCOUT.md`, lines
39 and 317--326).  C1 is therefore an exact historical sequence-candidate
collision and reverses a prior explicit kill without acknowledging or clearing
it.

P45's analytic rank-one operator self-commutator/Schatten wall is only
terminologically and thematically adjacent, not the same finite-field map.
There is no need to overstate that collision because B2B-08 is exact.

A bounded exact-owner search found no primary paper stating these precise
`M_2(F_q)` fibres.  The nearest primary source located is Guralnick's work on
finite-field analogues of singular-value decomposition and the relationship
between `AA^T` and `A^TA`,
[arXiv:1805.06999](https://arxiv.org/abs/1805.06999), published in Linear
Algebra and its Applications.  It is adjacent background, not evidence that it
owns the displayed difference-map census.  Conversely, the non-hit is not a
novelty certificate and cannot overcome the internal kill or theorem error.

### 2.4 Allowed claim ceiling and required repairs

**Permitted ceiling after correction, as a lemma inside a materially broader
project:** “The transpose self-commutator on `M_2(F_q)` has square-zero
dynamics, the displayed characteristic-sensitive image and fibre sizes, and
the corrected kernel-based depth partition.”  The universal identity is
zero-credit.  No claim may extend the `M_2` fibre classification to general
`M_n`, and “complete functional graph” is forbidden until the four vertex
roles above are stated and literally verified.

Minimum correctness repairs, even for archival use:

1. replace (3) and (7), every numerical layer example, and every downstream
   reference by the corrected depth formulas;
2. repair the verifier so it computes the least depth of every enumerated
   state and separately checks `im Delta`, `ker Delta`, and their difference;
3. state the four vertex roles and their indegrees explicitly;
4. rerun prime and extension-field controls and require canonical-output
   equality only after the corrected assertions are active; and
5. retract the present claim that the verifier checks (2)--(7).

Those repairs restore correctness but **do not** clear the paper-value gate.
Reconsideration as a paper candidate additionally requires a genuinely
nonmechanical theorem beyond the killed B2B-08 mechanism--for example a
substantial higher-rank fibre/stratum theorem with a verified owner residual--
plus explicit explanation of why the prior P117--P121 kill is now obsolete.

The present decision is **`KILL / CORRECT BEFORE ANY REUSE`**.

## Final gate

- **X01:** `KILL`; mathematically coherent, but exact prior-lane collision and
  fatal mechanical-value subtraction.  Archive only under the narrow worked-
  realization ceiling.
- **C1:** `KILL`; false advertised depth theorem, verifier blind spot, and an
  exact prior literal candidate already killed as theorem-thin.  Corrected
  formulas may survive only as a lemma in a substantially broader result.
- **External release:** `HOLD_EXTERNAL` for both.

