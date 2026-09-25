# Full finite-symmetry quotients: owned clocks, shortening and packet multiplicity

**Paper:**424-finite-symmetry-quotient. **Candidate:**`ANG-AUDIT-20260923-FSQ01`.
Date2026-09-23; exact conditional derivation; internal review record linked below.
**Outcome:** `FINITE-SYMMETRY QUOTIENT LAW ESTABLISHED; NO AUTOMATIC ARITHMETIC ADMISSION — CONDITIONAL FILTER / FORK`.

## Abstract

For a full smooth density owner with a commuting finite measure-preserving
symmetry group, its geometric clock descends to the actual finite-orbit
quotient with pushforward measure. A quotient cycle need not have the same
source period or physical primitive as a lift. We give exact stabilizer,
shortening and multiplicity formulas, including nonfree points and zero-clock
cycles, and classify all aperiodic quotient preimages. Three whole external
controls separate merging copies, shortening a cycle, and nonfree isotropy.
This does not provide an endogenous prime source, authorize arbitrary
equal-time merging, or apply a reversing symmetry as a commuting one.

## 1. Frozen owner and scope

The [card](candidate-card.md) fixes one second-countable smooth manifold M,
strictly positive smooth density mu, C1 diffeomorphism F, and finite group K
of C1 mu-preserving diffeomorphisms commuting with F. Countably many
components, ineffective action, nonfree strata and all null points remain.
Y=M/K, pi:M->Y, nu=pi_*mu, barF([x])=[Fx] are the FULL quotient owner.
No chosen periodic representative, density change or matrix/scale reduction.
J_F is the pointwise density Jacobian, kappa=log J_F; its actual inverse
q(y)=1/J_F(F^-1 y) gives kappa(x)=-log q(Fx). Signed clocks are allowed.
The descended version, not an arbitrary a.e. RN choice, defines barkappa.

| Ledger field | This object |
| --- | --- |
| Carrier/action | M,F,K and full Y,barF, each with own specified measure |
| Arithmetic lineage | Conditional prime-symbolic realization -> actual symmetry reduction |
| Clock/extension | Geometric IMAGE clock; full source times R, all heights |
| Packets | Actual integer-lag source orbits, entire isotropy clock group |
| Classical symplectic map/positive roof/suspension | NOT APPLICABLE |
| Trace/operator | NOT SUPPLIED; T3 NOT AUDITED |
| Formal Route / B | UNASSIGNED / NOT INVOKED |

Strong arithmetic naturalness is not a consequence of this conditional arrow.
The benchmark is nonempty positive ledger, EVERY primitive log ordinary prime,
and at most one packet per prime; all-prime coverage is additional.

## 2. All-point clock descent and own IMAGE

**Proposition1.** The stated full quotient has an owned all-point IMAGE
version barJ([x])=J_F(x), and barkappa=log barJ is well defined.

Proof. A positive smooth density is sigma-finite on this second-countable
manifold. For each a in K, the continuous geometric J_a equals1 a.e. by
measure preservation, hence everywhere: any open discrepancy has positive
measure. Chain rule and Fa=aF imply J_F(ax)=J_F(x) at every point.
The finite-orbit quotient is standard Borel (a Borel ordering selects the
least of a finite orbit); invariant functions descend as Borel functions.
This finite-group fact does not supply a selector for the F orbit quotient.
Finite K-saturations of a countable finite-measure cover give a sigma-finite
cover for nu. barF is a Borel bijection with inverse[x]->[F^-1x].
For EVERY Borel E subset Y, not just a generic stratum,

```
pi^-1(barF E) = F(pi^-1 E),
nu(barF E) = integral_(pi^-1 E) J_F dmu = integral_E barJ dnu.
```

The inverse law follows with barq([y])=1/J_F(F^-1y). No division by
|K|, stabilizer size or selected orbit length occurs in these identities.
They also hold on null nonfree strata with the prescribed descended version.
The same chain rule supplies all iterated IMAGE versions and clocks. QED.

## 3. Whole actual groupoids and phase ledger

For either own bijection T:X->X, write
G_T={(z,k,T^kz):z in X,k in Z}, source T^kz, range z.
Total invertibility proves this equals the actual meeting-triple definition.
For k>=0, c(z,k,T^kz)=S_k(z), with S_k the k-step sum of own kappa;
for negative k use S_k(z)=-S_(-k)(T^kz). Concatenation proves the cocycle.
Thus (Tz,-1,z) has -kappa(z); all (w,h)->(z,h+c) and heights are kept.

The COMPLETE kernels are

```
ker lag = {(z,0,z)};
ker c = {(z,k,T^kz):S_k(z)=0};
ker lag intersect ker c = units.
```

Clock kernel can contain nonunit arrows, even though the lag kernel does not.
Source orbits are exactly {T^n z:n in Z}. A source of least period q has
isotropy qZ and signed sum C=S_q(z), ENTIRE physical H=CZ. Its extension
isotropy is0 if C!=0, otherwise qZ; its primitive is |C| only when C!=0,
with repetitions r|C|. Aperiodic sources have isotropy0,H=0,extension
isotropy0, regardless of possible zero-clock arrows between different points.

There are no strictly preperiodic points: T^a z on a cycle implies z lies
on that cycle by applying T^-a. Full incoming to a core is therefore exactly
its cycle, with all integer arrows retained; all other full orbits remain.
For a reference b and z=T^n b, a phase coordinate is

```
h+S_n(b) modulo H_b.
```

Changing n by a source period changes it by a multiple of C; changing b
only shifts the coordinate. For H=0 the real phase remains free. This is
an orbitwise description, not a global measurable/manifold quotient claim.

## 4. Exact finite-symmetry cycle law

**Theorem2.** A point x is periodic upstairs iff [x] is periodic downstairs.
Let downstairs least period be ell, set S=Stab_K(x), and choose ANY g with
F^ell x=gx. Then g normalizes S. Let r be the order of gS in N_K(S)/S.
The upstairs least period is q=r ell. Every upstairs cycle over that one
downstairs cycle has that same q and signed sum C=r barC, where
barC=sum_(j=0)^(ell-1) kappa(F^j x). There are EXACTLY

```
|K| / (r |S|)
```

distinct upstairs cycles above it. Upstairs H=CZ; downstairs H=barC Z.
No nonzero clock is created from zero. If C!=0 the downstairs positive
primitive is |C|/r, with its own source period ell, not a manually rescaled
upstairs roof. All choices of g yield the same integer r and clock law.

Proof. Periodicity upstairs implies it below. Conversely F^ell x=gx and
commutation imply F^(j ell)x=g^j x; finite order of g yields periodic x.
Stab(F^ell x)=S by commutation, but Stab(gx)=g S g^-1, so g normalizes S.
The first j>0 with g^j x=x is exactly the order of gS. Any upstairs period
is a downstairs period, hence a multiple of ell; this proves q=r ell.
The g's taking x to F^ellx form one coset gS, so r is independent of choice.

Let L={a in K:ax lies on the F-cycle of x}. It is a subgroup. Sending a
to the unique shift t mod q with ax=F^t x gives a homomorphism into Z/q
with kernel S. Its image is precisely the multiples of ell: membership
forces barF^t[x]=[x], and powers of g realize them. Thus |L|=r|S|.
The cycles over the quotient cycle are K-translates indexed by K/L, proving
the exact count even when K is ineffective or S nontrivial.
K-invariance gives kappa(F^(ell+j)x)=kappa(gF^j x)=kappa(F^j x).
The r blocks therefore have the same sum barC, giving C=r barC.
Section3 supplies entire isotropy/phase/repetition groups, not only a witness.
Every lift and its actual arrows remain. QED.

**Aperiodic complement.** For a nonperiodic quotient orbit through[x], its
FULL preimage is union_(a in K) O_F(ax). It consists of |K|/|S| distinct
aperiodic upstairs orbits, each mapping bijectively onto the quotient orbit.
Indeed ax=F^n x implies F^(ord(a)n)x=x, so n=0 and a in S; no nonzero
relative phase shift can occur. All these orbits have isotropy/H=0; their
clocks and real phase coordinates are still the ones in Section3. Thus
the periodic count is not incorrectly applied to the nonperiodic remainder.

## 5. Three complete external controls

All six maps below are bijections with inverse IMAGE version1/2: geometric
upstairs and geometrically descended downstairs, including the specified
null/nonfree points, without presuming a differential quotient Jacobian.
Upstairs Lebesgue/counting and
downstairs2Lebesgue produce forward IMAGE2, so own kappa=log2 everywhere.
This is proved directly by dilation change of variables on each component;
the finite permutations preserve counting measure. For the half-line,
nu(E)=Leb(pi^-1E)=2Leb(E), with0 null but explicitly retained.

For each map its whole G is (z,k,T^kz), c=k log2. Thus ALL clock, lag
and joint kernels are units; source-cycle loops need not be clock-kernel
loops. Nonzero orbits are the complete two-sided dilation sequences below,
with source/extension isotropy0,H0 and free phase h+n log2 at T^n b.
There are no other incoming points to any listed cycle.

| Control | Whole upstairs iterates T^n | Complete periodic ledger upstairs | Full quotient |
| --- | --- | --- | --- |
|A duplicate copies|(2^n x,j)|Two separate fixed cores(0,0),(0,1), each H=log2 Z, sourceZ, extension0|R,2y; one0 fixed core, H=log2 Z|
|B phase cycling|(2^n x,j+n mod2)|One two-state core(0,0)<->(0,1), H=2log2 Z, source2Z, extension0|R,2y; one0 fixed core, H=log2 Z|
|C nonfree reflection|2^n x|Only0 fixed, H=log2 Z, sourceZ, extension0|[0,infinity),2y; only0 fixed,H=log2 Z|

Downstairs source isotropy at0 is Z and extension isotropy0 for all three;
primitive/repeats are log2,rlog2. A upstairs primitives are two separate
log2 packets, B upstairs is log4 with repeats rlog4, C upstairs log2.
For the fixed cores phase is h modlog2. B upstairs phase, reference(0,0),
is h+j log2 mod2log2; these two source phases form ONE packet.

For A every downstairs nonzero orbit lifts to two label-separated orbits.
For B every nonzero quotient orbit likewise lifts to two orbits, not one:
choosing x at a given dilation position fixes the two alternative label
parities. For C a positive nonzero quotient orbit lifts to its positive and
negative orbits. These formulas cover EVERY nonzero point, both signs and
all n in Z. On the periodic cores A has S=1,r=1 and2 upper cycles;
B has S=1,r=2 and1 upper cycle; C has S=K,r=1 and1 upper cycle.
This explicitly tests why |K| alone cannot give the shortening factor.

## 6. Decision, adverse boundaries and evidence

The exact symmetry and quotient IMAGE law can genuinely merge duplicate
source packets or shorten a physical primitive. It does not do so merely
because two lengths agree. The three quotients satisfy only the necessary
nonempty/prime-only/unique test at prime2, NOT all-prime coverage, and are
EXTERNAL controls without endogenous divisibility. A reversing action such
as RFR=F^-1 is outside the commuting hypothesis unless separately proved
to commute. Arbitrary reweighting, group deletion or representative selection
would create a new object. No universal quotient no-go or rescue follows.

T0/clock construction established conditionally; arithmetic T1 NOT PASSED;
T2 exact conditional transport law; T3 NOT AUDITED. Classical NOT APPLICABLE,
formal UNASSIGNED, B NOT INVOKED. Portfolio CONDITIONAL FILTER / FORK:
apply only to a separately supplied full lineage-qualified owner and exact K.
No new carrier admitted, no claim about RH/zeros/quantization or trace.

Proof method: exact chain-rule/change-of-variables, finite-group algebra,
and full dilation-orbit enumeration. No precision/cutoff/numerical experiments.
AI assisted the design, exact derivation, drafting and internal review.
Root wrote this derivation before reading reviewer raw. Design/collision
exposures remain in the card; internal same-model review NOT_CALIBRATED,
not independently attested human or external peer verification.
Control label/dilation choices illustrate ownership,
not arithmetic evidence; arbitrary-design PROVES_TOO_MUCH risk remains.
See [claims](claim-ledger.md), [navigation](README.md),
[scope](evidence/scope-review.md), [independent derivation](evidence/independent-derivation.md),
[final review](evidence/independent-review.md) and
[batch](../420-divisor-reciprocal-displacement/batch-summary.md).
