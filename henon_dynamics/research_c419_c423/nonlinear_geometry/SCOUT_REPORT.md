# C419--C423 nonlinear-return scout

2026-09-07. Status: **THREE_SCREENED / ZERO_RECOMMENDED_FOR_ADMISSION**.
This is AI-assisted internal research, not a manuscript, independent peer
review, formal Route-A evaluation or worldwide-priority assertion.

The pre-computation objects, full quantifiers, domains, clocks, observables,
arithmetic carriers, deductions and stop boundaries are in
[FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md). No seed was replaced; all three
were made precise. The arithmetic lane's Somos-4 elliptic QRT contract was
explicitly kept out of scope. The old positive two-twist reserve was neither
edited nor rerun nor re-reviewed by this author.

## 1. Outcome

| Contract | Actual mathematical outcome | Recommended disposition |
|---|---|---|
| NG1: T_a(x,y,z)=(y,z,yz+a-x), all a in Z, all Z^3 | Correct invariant, a fixed-point family and unbounded four-step channels for every a; no complete all-a integral recurrent-core classification beyond the earlier unclosed proposal | REJECT_RESURFACED_GLOBAL_CORE_GAP |
| NG2: coefficient-free rank-two Phi_{b,c}, all positive b,c, native rational nonzero domain | Complete periodic **set** classification reduces to classical finite-type identities, one classical affine conic and brief elementary exclusions; a rational 3-cycle refutes the misleading generic-periodicity shortcut | RETAIN_SMALL_COMPANION / REJECT_INSUFFICIENT_RESIDUAL_SUBSTANCE |
| NG3: one Coxeter return on W_k, all k in Z | Correct globally defined rational involutions; compact real locus and complete elementary abs(k)<=4 boundary; no all-k rational denominator/height exhaustion | REJECT_NO_SINGLE_WORD_ARITHMETIC_CLOSURE |

These are research dispositions, not proofs that the unsolved questions are
impossible. The coordinator retains authority over admission. No computation
of a larger height, coefficient, word or period box is recommended.

## 2. NG1: the old global core has not been replaced

The invariant identity K_a o T_a=K_a is exact. The inverse is
T_a^{-1}(x,y,z)=(xy+a-z,x,y). For every t in Z, set a=2t-t^2. Then
(t,t,t) is fixed and lies on level K_a=2t^3-3t^2. Consequently a
parameter-independent coordinate core cannot be transplanted from a=0.
These diagonal fixed points are singular on their respective levels;
excluding them would change the frozen ordinary-point contract.

There is a stronger fixed-parameter obstruction to a finite coordinate box:
for every a,t in Z, the cyclic scalar word

    (-1,t,-1,a+1-t)

satisfies x_{i+3}+x_i=x_{i+1}x_{i+2}+a. Thus (-1,t,-1) is fixed by
T_a^4 for every t, with possibly smaller least period at special values.
Its level is t^2-(a+1)t+2+2a. This is a direct symbolic substitution,
not an enlarged census. A valid full answer needs finitely described
unbounded channels plus any residual core, not a finite fixed-a box across
all levels.

This is a falsifier of a naive uniform-small-box strategy, not of a
parameter-dependent complete classification. The missing work is still a
new all-a escape/core argument covering every ordinary integral periodic
point and every period. No such argument emerged in this bounded pass.

The closest local collision is the generalized-character proposal already
left unclosed in [the previous scout, NG3](../../research_c414_c418/nonlinear_geometry/SCOUT_REPORT.md).
Restricting its coefficient family to A=B=C does not itself close that gap.
The a=0 case belongs to [C413](../../continuation_c409_c413_round2/nonlinear_geometry/PROOF_PACKAGE.md).

Roberts' classical generator-based escape results must be deducted before
claiming a new trace-map mechanism. Cantat--Loray's entropy and bounded
whole-group-orbit results do not classify one T_a orbit. Jang's tropical
skeleton model is not the integral recurrent core, and Abboud's common
periodic-set rigidity has different parameter hypotheses and quantifiers.
Iwasaki--Uehara's isolated-index formula is weighted and projective; it does
not enumerate our integral points. Their actual source scopes and accessed
versions are recorded in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).

Replacement boundary: return only with a genuinely new uniform core lemma,
not a coefficient table, a=0 clock change, old reserve word or a Lefschetz
number renamed as an integral point count.

Cheapest next theoretical gate, **not executed as a new project here**:
classify the arithmetic first return to the small-coordinate section,
including all of its unbounded affine channels. The elementary entrance
bound alone is cheap: if M>0 is a maximal absolute scalar coordinate in a
cycle, its recurrence gives |x_{i+1}|<=2+|a|/M. If M<sqrt(|a|), the
entrance bound is immediate; otherwise use this inequality. The all-zero
cycle is separate and also satisfies it. Hence every cycle meets
|x|<=2+sqrt(|a|). What remains missing is the complete return classification
on that section; replacing it by a sampled transition graph would not
close the question.

## 3. NG2: a complete but small companion classification

Write the two-sided alternating sequence as

    u_j u_{j+1}=1+v_j^b,
    v_{j-1} v_j=1+u_j^c.

The initial pair is (u_0,v_0), and one Phi_{b,c} iterate advances j by one.
All u_j and v_j are nonzero rational numbers on the frozen domain U_{b,c}.

The following classification is recorded to preserve a useful screening
result. It is not put forward as a substantial new paper or a priority claim.

* If bc<=3, every point of U_{b,c} is periodic. The map identities have
  orders 5,3,4 when bc=1,2,3 respectively. This states an order of the map,
  not the least period of every specialized point.
* If (b,c)=(1,4), the entire rational periodic set is

      {(u,uv-1): u,v in Q, u^2+uv+v^2=1, uv(u+v) != 0}.

  Every such point has least Phi-period 3.
* The (4,1) set is the image of this set under
  L_1(x,y)=(y,(1+y)/x); this is a conjugacy on the native domains.
* In every other case bc>=4 the rational periodic set is empty.

### 3.1 Hyperbolic exponents: a short valuation obstruction

Suppose bc>4 and the sequence is periodic. Fix a prime p. If some even
phase u_j has negative valuation, let -r<0 be the minimum even valuation.
The second exchange relation at that phase has valuation -cr, since
v_p(1+u_j^c)=c v_p(u_j). Thus some odd phase has negative valuation.
Let -s<0 be its minimum. Since each neighboring valuation is at least its
parity minimum, the two exchange relations give

    cr <= 2s,     bs <= 2r.

Multiplication contradicts bc>4. Starting with a negative odd phase gives
the same conclusion. Therefore every coordinate of a rational periodic
sequence is integral. This is a maximum-valuation argument, not a claim
deduced from nonperiodicity of the cluster variables.

If b,c>=2, let M be the largest absolute integral coordinate in the cycle.
For M>=2, the relation centered at a coordinate of magnitude M is
impossible: exponent 2 gives 1+M^2>M^2, while every exponent e>=3 gives
|1+(+/- M)^e|>=M^e-1>M^2. The neighboring product has magnitude at most
M^2. For M=1, the right-hand side is 0 or 2, never a product of two
nonzero coordinates from {+1,-1}. Hence no such cycle exists.

If b=1 and c>=5, let U=max |u_j| and V=max |v_j|. Integrality gives
positive integers U,V. The first exchange relation gives V<=U^2+1, and
the second gives U^c-1<=V^2. For U>=2,

    U^c-1 >= U^5-1 > (U^2+1)^2,

because U^4(U-1)-2U^2-2>0. Thus U=1. The first relation then forces
every v_j=-2 (zero is forbidden), and consecutive u_j have opposite signs.
But v_{j-1}v_j=4 cannot equal 1+(+/-1)^c, which is either 0 or 2.
The c=1,b>=5 case follows by shifting the alternating phase. This covers
all bc>4 without a parameter census.

### 3.2 The affine boundary and its domain

For (2,2), a maximum absolute coordinate M on any finite real orbit would
give 1+M^2<=M^2. So there are no native real periodic points.

For (1,4), use the rational coordinate change
(x,y)=(u,uv-1), with u=x and v=(1+y)/x. It conjugates the map to

    G(u,v)=(v,(u+v^3)/(uv-1)).

The classical invariant and linearization are

    J=(u^2+v^2)/(uv-1),     G(u,v)=(v,Jv-u).

Nobe already owns the singular quartic, its conic transformation and its
linearization; Nobe--Matsukidaira explicitly give the mixed-exponent
recurrence. The formulas above are their mechanism in our native rational
coordinates, checked directly, not a new resolution theorem.
[Nobe, Theorem 1 and Corollary 1](https://arxiv.org/pdf/1808.08125),
[Nobe--Matsukidaira, Section 2.3](https://arxiv.org/pdf/1904.02853).

For a nonzero periodic rational vector, the matrix
[[0,1],[-1,J]] has a root-of-unity eigenvalue. Its determinant is 1, so
J=lambda+lambda^{-1}; as a rational algebraic integer in [-2,2], J belongs
to {-2,-1,0,1,2}. The conic equation
u^2+v^2-Juv=-J excludes J=0,1,2 over the reals (except the forbidden zero
vector at J=0). At J=-2 it becomes (u+v)^2=2 and has no rational points.
Only J=-1 remains. The map is then (u,v)->(v,-u-v), of order 3 with no
nonzero fixed vector. The nonzero phases are exactly u,v,-u-v. Also
uv<=1/3 on this real conic, so uv-1 and its cyclic counterparts never
vanish. Thus uv(u+v)!=0 is exactly the remaining native-domain condition.

For example, the actual two-mutation orbit is

    (3/7,-34/49) -> (5/7,-89/49) -> (-8/7,-73/49) -> (3/7,-34/49).

Every intermediate scalar phase is nonzero. This directly prevents reading
an infinite order of the generic map as absence of specialized periodic
points. The apparent claim in the Nobe--Matsukidaira abstract is clarified
by their explicit definition of **map** period in Section 2.2; this is not
a contradiction with the source's actual theorem.

For the remaining cases, coefficient-free finite-type periodicity is
classical. [Fomin--Zelevinsky, Theorem 6.1 and finite-type formulas](https://arxiv.org/pdf/math/0104151).
Specialization is legitimate throughout U: only defined, nonzero recurrence
phases are used. No zero-crossing continuation or scheme saturation is
silently added. Since Phi_{b,c}=L_c o L_b and
L_b o Phi_{b,c}=Phi_{c,b} o L_b, the swapped cases have the same native
periodic-set classification.

### 3.3 Why this is not a paper recommendation

After subtracting finite-type periodicity and the known affine conic, the
residue is the brief valuation/size exclusion in Section 3.1 and an
elementary rational trace test. The uniform b,c quantifier is useful, but
does not by itself make this residual work a substantial new geometric or
arithmetic mechanism. No source was found that states this exact signed
rational classification verbatim; that bounded non-finding is neither a
priority claim nor a substitute for the substance requirement.

C408 counts local lengths on an unsaturated alternating-zero cyclic
relation scheme. Every such zero is outside U; no part of its local length
formula is being used as an ordinary periodic-point count here.

Replacement boundary: a future proposal needs a materially new arithmetic
mechanism. Merely recasting this lemma as a paper, adjoining known root-of-
unity fields or changing one exponent is not recommended.

## 4. NG3: compact real dynamics does not close rational heights

The exact W_k family and the projection involutions are already owned by
Fuchs--Litman--Silverman--Tran. Their finite group-orbit constructions and
uniform-boundedness question concern the full generated group, not this
one Coxeter composition. [Primary paper](https://arxiv.org/pdf/2201.12588).

Our formulas have 1+y^2 z^2>0 on Q^3, so every affine rational phase is
defined, and each involution preserves W_k. There is no need to remove
points at a real pole or add a compactification boundary. Singular points
remain ordinary states, not collections of points on exceptional divisors.

The identity

    x^2+y^2+z^2+(xyz+k/2)^2 = k^2/4

holds on W_k. Hence the **entire real locus** is compact and every real
orbit is archimedean bounded. This supplies no rational denominator bound.
It exposes exactly why the earlier discrete integral escape/core template
does not settle the frozen rational K3 problem.

AM--GM gives x^2+y^2+z^2+x^2y^2z^2>=4|xyz|. A nonzero real solution
has xyz!=0, hence |k|>=4. Thus |k|<4 has only the origin. At k=+/-4,
equality forces |x|=|y|=|z|=1 and kxyz=-4, giving the origin and four
sign points. Each is fixed by all three involutions. The exact boundary
check confirms five ordinary fixed points in each k=+/-4 fiber. The
singular sign support is already in the primary paper's Proposition 9.5
(the accessed arXiv numbering), so this elementary slice is not a new slot.

The unresolved increment is a complete single-word rational-height or
denominator theorem for every |k|>4, followed by exhaustive cycle closure.
Canonical-height or finite-group finiteness statements cannot silently
supply an effective all-parameter list. Hutz's different Wehler family
already provides arithmetic periodic-point search infrastructure, but its
existence is not the missing uniform theorem for W_k.

Replacement boundary: a new single-word arithmetic control theorem is
needed. No finite-prime group-orbit table, first-period sample, group-wide
uniformity conjecture or small compact boundary counts as that theorem.

Cheapest next theoretical gate, **not executed here**: determine whether
the exact local valuation dynamics of the three involutions can bound
rational denominators for one periodic Coxeter orbit, uniformly in k.
On nonzero coordinates the alternative root formula is
sigma_x=(y^2+z^2)/(x(1+y^2z^2)). At an odd prime p congruent to 3 mod 4,
neither sum of two unit squares cancels, so

    v_p(x')=2 min(v_p(y),v_p(z))
             -2 min(0,v_p(y)+v_p(z))-v_p(x).

The p congruent to 1 mod 4 cancellation and p=2 cases cannot be discarded.
A periodic valuation model without a lift controlling residue cancellation
and global height would remain a scaffold, not the required classification.

## 5. Computation receipt and target boundary

[exact_checks.py](exact_checks.py) performs only identity checks and explicit
native witnesses. First version exited 0 in 0.421 seconds. One additional
square-completion identity was then added; the changed script exited 0 in
0.403 seconds. No old accepted check was rerun. All final assertions passed:

* NG1 invariant and symbolic unbounded-parameter fixed-point family.
* NG2 finite-type identities at orders 5,3,4, affine invariant/linearization,
  and all phases of the displayed exact rational 3-cycle.
* NG3 invariant, involution, square completion and the ten sign/origin
  boundary points across k=-4 and k=4.

Two subsecond exploratory symbolic calls also factored the Phi_{1,3}^2
fixed equations: the elimination polynomial was y^2(y-3)(y+1)^3. They
were not needed for the periodic-set statement, and no least-period
classification of all finite-type points is inferred from them.

The symbolic checks do not prove NG1/NG3 global exhaustiveness. The proof
of the small NG2 classification is the argument above, not a numerical
period list. No GPU, paid/external model, full paper, evaluation, global
index or Git mutation was used by this lane.

Intrinsic source arithmetic here remains source arithmetic. No target
Euler factors, root numbers, functional equation, automorphy, zero/divisor
correspondence or Hilbert--Pólya operator has been established.
NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.
