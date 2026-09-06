# Algebraic/arithmetic Stage-1 scout for the P147--P151 intake

Status: **HOLD_EXTERNAL**.  This is an internal falsification and owner-risk
ledger, not a paper, not a novelty claim, and not a paper-number assignment.
The root-control family based on codimension-one exterior powers of fixed-rank
finite abelian `p`-group types was treated as occupied and was not entered.

## Outcome first

Ten genuinely different literal finite/absorbing systems were defined and
tested.  They are different update rules, not ten parameter choices of one
rule.  Exact enumeration generated **929,002 assertions**.  Two systems retain
a coherent all-parameter theorem spine subject to owner subtraction, one is an
owner-compressed reserve, and seven are killed.

| rank | handle | literal system | early signal | owner/internal risk | verdict |
|---:|---|---|---|---|---|
| 1 | QAR | `x -> x(x+p)` on `p Z / p^e Z` | exact branched valuation clock, temporal polynomial, and discriminant fibre atlas | medium-high quadratic/`p`-adic owner risk; not the occupied exterior-power control | `SELECT_INTERNAL_OWNER_PENDING` |
| 2 | TMD | `x -> x Tr(x)` on `F_{p^n}` | closed iterates, exact tail/period law, and all-target fibres | medium-high trace-polynomial owner risk | `SELECT_INTERNAL_OWNER_PENDING` |
| 3 | MFR | `(x,y) -> (y,xy)` on `F_p^2` | depth-two boundary plus Smith-normal fixed-iterate census | long dynamics is a standard Fibonacci toral automorphism; P108 recurrence proximity | `RESERVE_OWNER_COMPRESSED` |
| 4 | QCW | `x -> x+chi(x)` on `F_p`, with `0 -> 0` | exact fixed/2-cycle boundary census | maximum tail is controlled by irregular Legendre-symbol runs | `KILL_THEOREM_THIN` |
| 5 | ASH | `x -> x^p-x` on `F_{p^n}` | exact trace-zero image and constant-field fibres | generic finite linear/Artin--Schreier dynamics; P109/P115 neighbourhood | `KILL_OWNER_LINEAR` |
| 6 | TFS | `f -> f+f^p` on `xF_p[x]/(x^N)` | exact permutation order and fixed-space dimension | direct unipotent-linear reduction and P115 truncated-polynomial collision | `KILL_INTERNAL_OWNER` |
| 7 | SPP | `sigma -> sigma^{c(sigma)}` on `S_n` | cycle-count Lyapunov function | all-`n` clock/fibre census degenerates into partition casework | `KILL_HARD_EXCLUSION` |
| 8 | CMD | `n -> lambda(n)` | strict descent and short exact profiles | literal iterated Carmichael function has direct owners; P133 arithmetic-descent proximity | `KILL_DIRECT_OWNER` |
| 9 | LBG | `n -> gcd(n, binom(2n,n))` | short divisor descent | central-binomial divisibility is owner-heavy and endpoints are irregular | `KILL_NO_SPINE` |
| 10 | GND | quadratic-field norm `(a,b) -> (a^2-db^2,0)` | complete norm fibres and closed iterates | exactly norm collapse followed by the owned scalar square map | `KILL_DIRECT_OWNER` |

The order above is a Stage-1 research order, not a publication ranking.  In
particular, the two `SELECT_INTERNAL` labels mean only “mathematically worth an
owner check.”

## Exact computational contract

The standard-library verifier is
[`verify_algebraic_scout.py`](verify_algebraic_scout.py).  Its byte-for-byte
expected output is [`CANONICAL.txt`](CANONICAL.txt).  It constructs every
declared finite carrier, verifies closure, computes functional-graph orbit and
fibre data, and compares those data with the displayed formulae.  Enumeration
is used only as counterexample pressure; none of the formulae below is claimed
proved by enumeration.

| handle | boxes/states tested | assertions |
|---|---:|---:|
| QAR | 19 / 11,447 | 71,154 |
| TMD | 12 / 5,380 | 72,628 |
| ASH | 19 / 9,220 | 36,937 |
| TFS | 20 / 3,918 | 11,894 |
| SPP | 7 / 46,232 | 231,160 |
| CMD | 1 / 20,000 | 80,002 |
| QCW | 167 / 76,125 | 305,001 |
| MFR | 14 / 8,257 | 33,420 |
| LBG | 1 / 2,500 | 12,501 |
| GND | 13 / 8,253 | 74,303 |
| cross-system meta-invariants | — | 2 |
| **total** | **10 literal systems** | **929,002** |

The two meta-invariants assert that exactly ten rows were emitted and that all
ten handles are distinct.

## 1. QAR — quadratic absorber on a local maximal ideal

### Literal definition and early profile

Fix an odd prime `p` and `e >= 2`.  Let

`X_{p,e} = p Z / p^e Z`, and `F(x) = x(x+p) mod p^e`.

This is a self-map of the maximal ideal.  The computation found one recurrent
point, namely the absorber `0`, in every tested box.  Representative temporal
profiles `D(z)=sum_x z^{tau(x)}` were:

- `p=3,e=6`: `1 + 5z + 12z^2 + 36z^3 + 108z^4 + 81z^5`, image size `31`, maximum fibre `27`;
- `p=5,e=6`: `1 + 9z + 40z^2 + 200z^3 + 1000z^4 + 1875z^5`, image size `261`, maximum fibre `125`;
- `p=7,e=5`: `1 + 13z + 84z^2 + 588z^3 + 1715z^4`, image size `151`, maximum fibre `98`.

The anomaly that makes the system useful is the `v_p(x)=1` branch.  It is not
just “valuation increases”: the cancellation depth of `x/p+1` controls the
first jump, while all higher-valuation states subsequently climb by exactly
one valuation unit.

### Candidate all-parameter theorem spine

Put `tau(x)=min{t>=0:F^t(x)=0}` and cap `v_p(0)` at the modulus exponent.

- `tau(0)=0`.
- If `a=v_p(x)>=2`, then `tau(x)=e-a`.
- If `x=pu` with `u` a unit, put `r=v_p(u+1)` capped at `e-1`; then
  `tau(x)=max(1,e-1-r)`.
- For `e=2`, `D(z)=1+(p-1)z`.  For `e>=3`,

  `D(z)=1+(2p-1)z + sum_{d=2}^{e-2} 2(p-1)p^{d-1}z^d + (p-2)p^{e-2}z^{e-1}`.

  Thus the sharp maximum is `e-1`, attained by `(p-2)p^{e-2}` states.
- A target outside `p^2 Z/p^e Z` has no preimage.  Write an allowed target as
  `y=p^2w`, put `n=e-2`, and let `rho_{p^n}(Delta)` be the number of square
  roots of `Delta` modulo `p^n`.  Then

  `|F^{-1}(y)| = p rho_{p^n}(1+4w)`.

  If `Delta=0`, `rho=p^{floor(n/2)}`.  If
  `v_p(Delta)=2c<n` and the unit part is a quadratic residue modulo `p`, then
  `rho=2p^c`; otherwise `rho=0`.
- Consequently the image size is

  `1 + (1/2) sum_{c=0}^{floor((n-1)/2)} (p-1)p^{n-2c-1}`.

### Proof engine, collision, and owner risk

The proof engine is elementary but map-specific: split at `v_p(x)=1`, prove
the valuation clock, then complete the square
`(2u+1)^2 = 1+4w` and use exact square-root counts over odd prime powers.
The nearest internal mechanisms are P142's valuation/gcd dynamics, P100's
digit-erasure valuation phase, and P107's ideal-power lane.  QAR differs in
being an element polynomial with a cancellation branch and discriminant fibre
geometry, but that distinction still needs portfolio review.

Owner risk is **medium-high**.  Translating by `p/2` converts the quadratic to
a standard monic quadratic `z^2+c` on the translated ideal, so broad quadratic
`p`-adic dynamics is close.  Bounded exact-phrase searches on 2026-09-01 did
not locate the literal finite maximal-ideal theorem package; that miss is not
novelty evidence.  Verdict: `SELECT_INTERNAL_OWNER_PENDING`.

## 2. TMD — trace multiplier on a finite field

### Literal definition and early profile

For an odd prime `p` and `n>=2`, define

`T(x)=x Tr_{F_{p^n}/F_p}(x)` on `F_{p^n}`.

The verifier uses trace-normal coordinates: trace is the sum of coordinates
and the multiplier is a base-field scalar, which is linearly isomorphic to the
literal field map.  Representative profiles were:

- `(p,n)=(5,4)`: tails `{0:126,1:249,2:250}`, recurrent `126`, image `251`;
- `(7,4)`: tails `{0:1030,1:1371}`, recurrent/image `1030`, maximum period `2`;
- `(11,3)`: tails `{0:606,1:725}`, recurrent/image `606`, maximum period `4`.

The useful signal is that an apparently nonlinear extension-field map closes
on one scalar trace recurrence without losing complete pointwise information.

### Candidate all-parameter theorem spine

Let `a=Tr(x)`.  Then

`T^t(x)=x a^{2^t-1}` and `Tr(T^t(x))=a^{2^t}`.

If `a=0`, the zero vector is fixed and every other vector has tail one.  If
`a!=0` and `ord(a)=2^j d` with `d` odd, the point has tail `j` and period
`ord_d(2)` (with the `d=1` period defined as one).

Write `p-1=2^s m`, `m` odd.  The full depth polynomial is

`1 + (p^{n-1}-1)z + p^{n-1}(m + sum_{j=1}^s 2^{j-1}m z^j)`.

Hence the recurrent count is `1+p^{n-1}m`, and the fixed count is
`1+p^{n-1}`.  The complete one-step fibre law is:

- the zero target has `p^{n-1}` preimages;
- a nonzero target `y` with nonzero square trace has two preimages;
- every other target has none.

### Proof engine, collision, and owner risk

The proof engine is trace linearity plus the cyclic structure of `F_p^*` and
its `2`-primary/odd decomposition.  The closest internal collision is the
scalar power-map skeleton behind P103 and the general finite-field/power-map
exclusion.  TMD retains more map-specific content than a bare power map because
the full extension-field fibres and trace-zero boundary are part of the same
theorem.

Owner risk is **medium-high**: the broad `x h(Tr(x))` construction is explicit
in finite-field permutation-polynomial literature.  A bounded search did not
locate the literal functional graph of `h(t)=t`; again, that miss is not novelty
evidence.  Verdict: `SELECT_INTERNAL_OWNER_PENDING`.

## 3. ASH — Artin--Schreier difference

### Literal definition and profile

On `F_{p^n}`, let `A(x)=x^p-x`.  In a scaled normal basis this is cyclic shift
minus identity.  Exact tests covered `p=2,n<=10`, `p=3,n<=7`, and `p=5,n<=5`.
For every box the kernel was the constant-coordinate line of size `p`, the
image was the trace-zero hyperplane of size `p^{n-1}`, and every target in that
hyperplane had exactly `p` preimages.  Dynamics varied sharply with `(p,n)`:
`(2,10)` had maximum tail `2` and period `30`, while `(5,5)` was completely
absorbing with maximum tail `5`.

### Spine, proof engine, and kill

A possible spine would classify tails and cycles from the primary/rational
canonical form of the circulant `S-I`, along with the uniform fibre theorem.
The proof engine is exactly finite linear algebra and the Artin--Schreier exact
sequence.  That is also fatal: it lies in the generic linear-operator lane and
near P109's nilpotent-image and P115's Frobenius/Cartier mechanisms.  Owner risk
is **direct/high** by structural reduction, even without a literal functional-
graph title.  Verdict: `KILL_OWNER_LINEAR`.

## 4. TFS — truncated Frobenius shear

### Literal definition and profile

Let `I=xF_p[x]/(x^N)` and `U(f)=f+f^p`.  If `P(f)=f^p`, then `U=I+P` with
nilpotent `P`.  All tested states were recurrent.  Put
`h=min{k:p^k>=N}`.  The verified exact formulae were

- `ord(U)=p^{min{r:p^r>=h}}`;
- `|Fix(U)|=p^{N-1-floor((N-1)/p)}`.

For example, `(p,N)=(2,11)` had order `4` and period census
`{1:32,2:224,4:768}`; `(3,7)` had order `3`, with `81` fixed states and `648`
states of period `3`.

### Spine, proof engine, and kill

The proof is the characteristic-`p` identity
`(I+P)^{p^r}=I+P^{p^r}` plus monomial support.  This produces a clean theorem,
but it is a unipotent linear operator on the same truncated-polynomial terrain
as occupied P115.  There is no independent residual after that reduction.
Verdict: `KILL_INTERNAL_OWNER`.

## 5. SPP — state-dependent power on a symmetric group

### Literal definition and profile

For `sigma in S_n`, let `c(sigma)` be its number of disjoint cycles and define
`P(sigma)=sigma^{c(sigma)}`.  Raising a cycle of length `ell` to the `c`th power
splits it into `gcd(ell,c)` cycles, so cycle count never decreases.  A state is
recurrent exactly when `gcd(c(sigma),ell)=1` for every cycle length `ell`.

Exact enumeration through `S_8` confirmed the criterion.  The recurrent counts
for `n=2,...,8` were `2,3,21,40,465,2030,23233`; maximum tails were at most two
in that window, while maximum periods reached four.

### Spine, proof engine, and kill

The cycle-splitting formula is a good Lyapunov lemma.  A full all-`n` theorem,
however, would still require parameter-dependent partition arithmetic for
clock, image, and fibres.  This is precisely the state-dependent group-power
hard-exclusion pattern, with high generic owner risk and no map-specific atlas.
Verdict: `KILL_HARD_EXCLUSION`.

## 6. CMD — Carmichael descent

### Literal definition and profile

On `{1,...,B}`, set `C(1)=1` and `C(n)=lambda(n)` for `n>1`.  The map strictly
decreases away from `1`.  At `B=100,1000,10000,20000`, the observed sharp
maximum depths were respectively `6,8,10,10`.

### Spine, proof engine, and kill

The natural theorem spine would be exact or asymptotic absorption height and
depth distribution, using prime-power formulae for `lambda`, least common
multiples, and Pratt-like factor descent.  This is not available as a fresh
system: the iterated Carmichael function and the number of iterations needed
to reach `1` are literal subjects of existing papers.  It also approaches the
P133 arithmetic-descent lane.  Verdict: `KILL_DIRECT_OWNER`.

## 7. QCW — quadratic-character walk

### Literal definition and profile

For an odd prime `p`, set `Q(0)=0` and
`Q(x)=x+chi_p(x) mod p` for `x!=0`.  Every nonzero step is nearest-neighbour.
If a residue is followed by a nonresidue, the adjacent pair is a 2-cycle; all
other points walk along a constant-sign run toward such a boundary (or, for
the appropriate endpoint, toward zero).

Writing `epsilon=chi_p(-1)`, the exact number of residue-to-nonresidue
boundaries is `(p-epsilon)/4`, so the recurrent count is
`1+(p-epsilon)/2`.  All cycles have length one or two and all fibres have size
at most two.  Across all odd primes through `997`, maximum tails grew
irregularly: `3` at `p=31`, `6` at `127`, `9` at `499`, and `10` at `997`.

### Spine, proof engine, and kill

The recurrent census follows from one quadratic-character correlation sum.
The full temporal polynomial is a run-length census, but a sharp all-prime
maximum is the longest-run problem for Legendre symbols.  Thus the early
profile cleanly identifies its own obstruction: the most interesting clock is
not available from the local dynamical rule.  Nearest portfolio collision is
the broad symbolic/run-statistics lane rather than a single occupied map.
Verdict: `KILL_THEOREM_THIN`.

## 8. MFR — multiplicative Fibonacci boundary map

### Literal definition and profile

On `F_p^2`, define `M(x,y)=(y,xy)`.  The origin is fixed; `(a,0)` with `a!=0`
has tail one; `(0,b)` with `b!=0` has tail two; and the nonzero torus is
permuted.  Consequently

- `D(z)=((p-1)^2+1)+ (p-1)z+(p-1)z^2`;
- the image size is `p(p-1)+1`;
- the origin has `p` preimages, every target with nonzero first coordinate has
  one, and the remaining targets have none.

With `x=g^a,y=g^b` on the torus, the exponent vector evolves under the
Fibonacci matrix `A=[[0,1],[1,1]]` modulo `m=p-1`.  If the Smith invariants of
`A^t-I` are `s_1,s_2`, then the full map has

`|Fix(M^t)|=1+gcd(m,s_1)gcd(m,s_2)`.

Tests through `p=43` verified all fibre, depth, and `t<=12` fixed-iterate
formulae.  At `p=11` the recurrent count was `101` and maximum period `60`.

### Spine, proof engine, and reserve decision

The proof engine is boundary stratification, discrete logarithms on the torus,
and Smith normal form.  It is exceptionally complete, but most of its long
dynamics is literally a finite toral Fibonacci/cat map, a mature mechanism;
the portfolio also already contains the P108 capped-Fibonacci recurrence.
Only the absorbing boundary extension remains map-specific.  Verdict:
`RESERVE_OWNER_COMPRESSED`, not a current selection.

## 9. LBG — central-binomial gcd descent

### Literal definition and profile

On `{1,...,B}`, let
`G(n)=gcd(n, binom(2n,n))`.  Since `G(n)` divides `n`, every nonfixed orbit
descends.  Exact profiles had maximum depth `3` at `B=50`, `4` at `B=500`, and
`5` at `B=2500`; the corresponding fixed counts were `8,56,262`.  The endpoint
set and fibres showed no stable finite-parameter pattern.

### Spine, proof engine, and kill

Any serious theorem would need Kummer/carry valuations and fine information on
the prime factors of `n`; central-binomial divisibility itself has strong
direct literature.  Unlike QAR, the irregular arithmetic does not compress to
a map-specific finite statistic.  Nearest internal collision is again the
arithmetic descent/valuation portfolio.  Verdict: `KILL_NO_SPINE`.

## 10. GND — quadratic finite-field norm descent

### Literal definition and profile

For odd `p`, choose a nonsquare `d` and represent `F_{p^2}` as
`F_p[u]/(u^2-d)`.  Define

`N(a,b)=(a^2-db^2,0)`.

The image is the embedded base-field axis.  Zero has one preimage; every
nonzero base-field target has `p+1` preimages; targets off the axis have none.
Moreover, for `t>=1`,

`N^t(a,b)=((a^2-db^2)^{2^{t-1}},0)`.

At `p=43` this gave maximum tail `2`, recurrent count `22`, maximum period `6`,
and depth census `{0:22,1:903,2:924}`.

### Spine, proof engine, and kill

The proof is the standard fibre structure of the finite-field norm followed by
the scalar square-map graph.  That exact reduction is fatal: norm and square
already explain every nontrivial feature, and generic power maps are excluded
by the portfolio.  Verdict: `KILL_DIRECT_OWNER`.

## Owner subtraction and primary-source ledger

Only primary author copies, arXiv records, publisher DOI pages, or official
journal records are used below.  Searches were bounded and completed on
2026-09-01; failure to retrieve an exact phrase is not evidence of novelty.

| affected handle | primary source | what it owns / why it matters | effect |
|---|---|---|---|
| QAR; GND control | Fan and Liao, [*Dynamics of the square mapping on the ring of p-adic integers*](https://arxiv.org/abs/1408.4574), [DOI 10.1090/proc12777](https://doi.org/10.1090/proc12777) | detailed square-map dynamics over `Z_p`; establishes that scalar-square reductions are not fresh and raises the bar for nearby monic quadratics | kills the scaled-square control and GND residual; raises QAR owner risk |
| QAR | Fan and Liao, [*On minimal decomposition of p-adic polynomial dynamical systems*](https://doi.org/10.1016/j.aim.2011.06.032) | general polynomial `p`-adic decomposition framework | QAR requires literal finite-quotient owner subtraction before promotion |
| TMD | Akbary, Ghioca, and Wang, [*On constructing permutations of finite fields*](https://doi.org/10.1016/j.ffa.2010.10.002), [author PDF](https://people.math.carleton.ca/~wang/papers/PPAGW.pdf) | explicit trace-reduction framework containing maps of the form `h(Tr(x)) phi(x)+g(Tr(x))`, including the `x h(Tr(x))` neighbourhood | does not directly supply the TMD functional graph found here, but makes owner risk medium-high |
| MFR | Chen, Wong, Liao, and Xiang, [*Period distribution of generalized discrete Arnold cat map*](https://doi.org/10.1016/j.tcs.2014.08.002) | finite two-dimensional toral matrix periods via recurrence/finite-field methods | compresses MFR's torus part to known machinery |
| MFR | Nance, [*Periods of the discretized Arnold Cat Map and its extension to n dimensions*](https://arxiv.org/abs/1111.2984) | explicit Fibonacci divisibility behind discrete cat-map periods | reinforces reserve-only status |
| CMD | Martin and Pomerance, [*The iterated Carmichael lambda-function and the number of cycles of the power generator*](https://arxiv.org/abs/math/0406335) | explicitly studies iterates of `lambda` and iterations toward `1` | direct owner hit; permanent kill |
| CMD | Harland, [*The number of iterates of the Carmichael lambda function required to reach 1*](https://arxiv.org/abs/1203.4791) | literal absorption-height quantity | direct owner hit; permanent kill |
| LBG | Ford and Konyagin, [*Divisibility of the central binomial coefficient*](https://arxiv.org/abs/1909.03903) | densities for `n^ell | binom(2n,n)` and coprimality with the central binomial coefficient | makes endpoint/fibre arithmetic owner-heavy; no dynamical residual emerged |

No exact primary-source owner was retrieved for the literal QAR or TMD
functional-graph packages, and no exact source for the absorbing-boundary MFR
map was retrieved.  Those are search outcomes, not clearance decisions.

## Controls and final recommendation

One tempting local-ring control was explicitly rejected: on
`pZ/p^eZ`, the map `x -> x^2/p` is carried by `x=pz` exactly to the ordinary
square map `z -> z^2 mod p^{e-1}`.  It is therefore a parameterized wrapper of
an owned system, not an eleventh candidate.

The algebraic lane should pass **QAR** and **TMD** to root-level owner review,
with QAR marginally first because its valuation branch and discriminant fibre
atlas are more distant from the generic finite-field power-map exclusion.
**MFR** may be kept only as a reserve if a boundary-extension theorem is wanted;
its torus core should receive zero novelty credit.  The other seven systems
should not consume another paper-stage round unless their literal update is
materially changed.
