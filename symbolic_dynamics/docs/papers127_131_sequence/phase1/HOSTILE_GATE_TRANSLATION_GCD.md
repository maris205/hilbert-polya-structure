# Hostile owner/value gate: translation--GCD erosion (`P01` scout handle)

**Gate date:** 2026-08-31 UTC  
**Role:** independent nonauthor hostile gate  
**Object status:** old reserve / conditional re-entry; not a new intake system  
**Paper status:** no paper number, no freeze, no manuscript authorized  
**External status:** **HOLD** for posting, submission, priority, and novelty

## Verdict

**REWRITE.**  The candidate may re-enter the later global five-system value
comparison after the owner and terminology repairs below.  This is not a
paper-level `GO` and is not permission to freeze a number.

The mathematical contract survived a genuinely separate extension-field
audit.  No counterexample was found in all monic polynomials through degree
six over `F4`, through degree four over `F8`, or through degree four over
`F9`.  The audit used explicit irreducible quotient-field bases and did not
import either prime-field engine.  It made **180,403 exact assertions** over
**17,523 states**, and a fresh run is byte-identical to the canonical
transcript.

Three defects prevent an immediate `GO`.

1. **Direct owner omitted (major).**  Garefalakis 2011 and, especially,
   Reis 2016/2018 already characterize translation-fixed irreducibles and
   state exactly the displayed formula for `b_(pm)`.  That formula and its
   Artin--Schreier/trace derivation are entirely zero credit, not part of the
   residual all-depth theorem.
2. **Internal mechanism collision understated (major).**  P110 already
   studies `x -> x join sigma(x)` on a cyclically acted lattice, proves the
   consecutive-orbit-fold iterate, invariant endpoint, finite clock, basins,
   and depth.  Translation--GCD is its order-dual meet operation in the
   divisibility lattice.  The literal polynomial census differs, but the
   semilattice dynamics does not.  Every generic orbit-fold statement must
   be zero credit and the P110 firewall must be explicit.
3. **“Kernel” is structurally misleading (major if asserted
   algebraically).**  The terminal projection `Q` is not a monoid
   homomorphism.  In characteristic `p`, put

   ```text
   a=x,     b=(x^p-x)/x.
   ```

   Then `Q(a)=Q(b)=1`, while `Q(ab)=x^p-x`.  Thus `Q^(-1)(1)` is the unit
   fibre (or terminal-free residual class), not the kernel of a monoid
   morphism.  The coefficient and fibre formulas remain correct, but the
   terminology and proof must not invoke multiplicativity of `Q`.

After these subtractions, two connected residual outputs remain: the exact
all-depth Euler product coupling translation-orbit exponent vectors to
cyclic run avoidance, and the target-by-target graded terminal-fibre census.
That conjunction is sufficient for **conditional re-entry to the global
value gate**, but it is borderline for an independent short paper because
the fixed-irreducible input and transfer method are owned/standard and the
terminal split is elementary.  The global comparison must decide whether
this residual is stronger than the other four systems; assertion volume is
irrelevant to that decision.

## 1. Scope and provenance audit

The handle `P01` is local to scouting.  It is not a paper number.  The exact
map already appears as rank 3, `RESERVE / HOLD`, in
`docs/papers112_116_sequence/scouting/ALGEBRAIC_SCOUT.md`, backed there by a
382,545-assertion prime-field verifier.  The current breadth scout correctly
says that this is an old reserve satisfying its previously stated “closed
full-depth census” re-entry condition.

The following are old and receive **zero contribution credit**:

1. the literal update `T(f)=gcd(f(x),f(x+1))`;
2. `T^t(f)=gcd_(0<=j<=t) f(x+j)`;
3. stabilization by time `p-1` and the sharp missing-factor witness;
4. the fixed/terminal ring `F_q[x^p-x]` and bounded fixed counts;
5. all depth tables already printed by the old prime-field scout; and
6. the fact that translation permutes irreducibles in orbits of length one
   or `p`.

The breadth scout proposed the following as new residual:

- the cyclic residual-exponent statistic and all-depth OGF `H_(q,p,t)`;
- the unique graded split `f=Q(f)g`, with `Q(g)=1`;
- the OGF and coefficients for the unit fibre `Q^(-1)(1)`; and
- every exact-degree and degree-capped fibre over an invariant target.

One correction is mandatory: the fixed irreducible count `b_d`, although
needed as an input to `H_(q,p,t)`, is not residual.  It is a direct theorem
of the owner literature identified in section 5 below.

## 2. Independent reconstruction of the rule

Let `q=p^a`, let `sigma(f)(x)=f(x+1)` on monic polynomials in
`F_q[x]`, and define

```text
T(f)=gcd(f,sigma(f)),       Q(f)=T^(p-1)(f).
```

Translation by one has order `p`, not order `q`.  Therefore the acting
group is the prime-subfield subgroup `F_p <= (F_q,+)` in every extension
field.  This distinction is essential: invariance under `x -> x+1` gives
`F_q[x^p-x]`, whereas invariance under every translation in `F_q` would give
`F_q[x^q-x]`.

### 2.1 Orbit-exponent dynamics

Factor a monic polynomial over `F_q` and fix a nontrivial translation orbit
of irreducibles

```text
P_0, P_1=sigma(P_0), ..., P_(p-1)=sigma^(p-1)(P_0).
```

If the exponent vector of `f` on this orbit is
`e=(e_0,...,e_(p-1))`, then one application of `T` takes cyclic adjacent
minima (up to the harmless choice of orientation).  At time `t`, each
coordinate is the minimum on a cyclic window of length `t+1`.  At time
`p-1`, every coordinate is

```text
m=min_j e_j.
```

Subtracting `m` leaves a residual vector `c` with `min(c)=0`.  Its local
stabilization depth is the longest cyclic run of positive entries: the
time-`t` window has reached zero everywhere exactly when every length
`t+1` cyclic window contains a zero.  Fixed irreducibles are unchanged and
have no transient coordinate.

This reconstruction is correct, including repeated factors.  It does not
depend on squarefreeness.

### 2.2 Fixed irreducibles: correct but directly owned

Let

```text
N_d(q)=(1/d) sum_(e|d) mu(e) q^(d/e)
```

be the usual number of monic irreducibles of degree `d`, and let `b_d` be
the number fixed by `x -> x+1`.  The proposed formula is

```text
b_d=0                                      if p does not divide d,

b_(pm)=(p-1)/(pm) sum_(e|s) mu(s/e) q^(p^v e),
         where m=p^v s and gcd(s,p)=1.
```

This is correct.  It is also exactly Reis's Theorem 2(c), written there as

```text
(p-1)/(pm) sum_(d|m, gcd(d,p)=1) mu(d) q^(m/d).
```

The two displays agree after writing `m=p^v s` and substituting `d=s/e`.
Consequently

```text
a_d=(N_d(q)-b_d)/p
```

correctly counts the nonfixed translation orbits, but neither `b_d` nor
this immediate orbit quotient may be presented as a new theorem.

### 2.3 All-depth enumerator

For `0<=t<=p-1`, let `R_(p,t)(y)` count nonnegative cyclic vectors
`c=(c_0,...,c_(p-1))` with minimum zero and with no positive cyclic run
longer than `t`, weighted by `y^(sum c_i)`.  Equivalently, with
`u=y/(1-y)`, the proposed `(t+1)`-state run automaton has transitions

```text
i -> 0       with weight 1,       0<=i<=t,
i -> i+1     with weight u,       0<=i<t.
```

The trace of its `p`-th matrix power counts cyclic words with the correct
marked positive entries.  The trace convention is sound: every admissible
cyclic support containing a zero has a unique consistent run-length state
sequence.  The excluded all-positive support is exactly the condition
`min(c)=0`.

Multiplying over irreducible translation orbits gives

```text
H_(q,p,t)(z)
  = 1/(1-q z^p) product_(d>=1) R_(p,t)(z^d)^(a_d).
```

The factor `1/(1-qz^p)` accounts collectively for arbitrary invariant
factors.  The formula is correct as a formal power series: for any desired
coefficient only finitely many degrees contribute.  The boundary checks
are also correct:

```text
R_(p,0)=1,          H_(q,p,0)=1/(1-qz^p),

R_(p,p-1)(y)=(1-y^p)/(1-y)^p,
H_(q,p,p-1)(z)=1/(1-qz).
```

Thus `[z^n](H_t-H_(t-1))` is the exact number of degree-`n` states with
depth exactly `t`.  The owner-subtracted residual is the coupling of the
owned `a_d` sequence to this local depth statistic and Euler product; the
fixed irreducible formula and finite-state transfer technique themselves
are zero credit.

### 2.4 Terminal split and fibres

On every nonfixed irreducible orbit, `Q(f)` takes the common minimum
exponent.  On every fixed irreducible it takes the full exponent.  Therefore

```text
f=Q(f) g,       Q(g)=1
```

and this pair is unique.  This is a graded set-theoretic factorization.  It
does **not** make `Q` multiplicative on arbitrary factors.  The property
actually used for target fibres is the narrower and true identity

```text
Q(hg)=h Q(g)        when h is invariant.
```

Let `U_(q,p,n)` denote the number of monic degree-`n` polynomials in the
unit fibre `Q^(-1)(1)`.  Since all monics have OGF `1/(1-qz)` and invariant
monics have OGF `1/(1-qz^p)`, the unique graded split gives

```text
U_(q,p)(z)=(1-qz^p)/(1-qz),

U_(q,p,n)=q^n                           for 0<=n<p,
             q^n-q^(n-p+1)              for n>=p.
```

If `h` is invariant of degree `m`, multiplication by `h` is a bijection
from the degree-`N-m` unit fibre to the degree-`N` fibre over `h`.  Hence

```text
# {f: deg f=N, Q(f)=h} = U_(q,p,N-m),
```

with zero understood for `N<m`; summing gives every degree-capped fibre.
The argument is correct.  It must be described as a graded product
bijection, not as a first-isomorphism theorem or a monoid-kernel quotient.

## 3. Boundary and counterexample stress

The following edges were reconstructed separately and are all sound.

| boundary | hostile check | result |
|---|---|---|
| degree zero | `1` is fixed, `Q(1)=1`, and `U_0=1` | pass |
| `p=2` | only depths zero and one occur; no odd-prime inference is used | pass |
| extension fields | clock is `p-1`, not `q-1`; invariant variable is `x^p-x` | pass |
| fixed targets | exact fibres vanish below target degree and depend only on residual degree | pass |
| repeated factors | exponent minima handle arbitrary multiplicity | pass |
| sharp clock | `(x^p-x)/x` has one missing coordinate and depth `p-1` | pass |
| terminal CDF | `H_(p-1)=1/(1-qz)` recovers every monic polynomial | pass |
| false multiplicativity | `Q(x)=Q((x^p-x)/x)=1` but `Q(x^p-x)=x^p-x` | counterexample fixed in code |
| characteristic zero | translation has no finite `p`-clock | correctly outside scope |

No theorem counterexample was found.  The only mathematical-language defect
is use of “kernel” in a way that may suggest a homomorphism.  A symbol such
as `K_n` may be retained for coefficients if explicitly defined, but prose
should say **unit fibre**, **terminal-free residuals**, or simply
`Q^(-1)(1)`.

## 4. Independent extension-field verifier

### 4.1 Independence of implementation

`verify_translation_gcd_extensions.py` was written separately for this
gate.  It imports neither
`docs/papers112_116_sequence/scouting/code/algebraic_translation_gcd.py`
nor `docs/papers127_131_sequence/scouting/algebraic/verify_algebraic_scout.py`.
It uses a different arithmetic route:

- base-`p` coefficient words modulo an explicitly declared irreducible
  polynomial for each extension field;
- exhaustive field associativity, distributivity, inverse, basis-relation,
  and Frobenius checks;
- Horner substitution for literal `f(x+1)`;
- a fresh Euclidean polynomial GCD over the quotient-field tables;
- naive trial-division irreducibility, independent of factorization used by
  the dynamics;
- literal translation-orbit partitioning of every enumerated irreducible;
- direct enumeration of residual exponent vectors, not reuse of the scout's
  support/binomial or transfer routine; and
- exhaustive comparison of every enumerated degree/depth and every target
  fibre within the stated boxes.

The declared bases are irreducible by the degree-two/three no-root test:

```text
F4 = F2[u]/(u^2+u+1),
F8 = F2[u]/(u^3+u+1),
F9 = F3[u]/(u^2+1).
```

### 4.2 Exact results

| field and phase | literal states / terminal images | fixed irreducibles `b_d` in range | selected top-degree CDF | selected unit-fibre coefficients |
|---|---:|---|---|---|
| `F4`, degree `<=6` | `5,461 / 85` | `b_2=2, b_4=4, b_6=10` | degree 6: `64,4096` for `t=0,1` | `1,4,12,48,192,768,3072` |
| `F8`, degree `<=4` | `4,681 / 73` | `b_2=4, b_4=16` | degree 4: `64,4096` for `t=0,1` | `1,8,56,448,3584` |
| `F9`, degree `<=4` | `7,381 / 10` | `b_3=6` | degree 4: `0,5904,6561` for `t=0,1,2` | `1,9,81,720,6480` |

The script checks more than the selected printed cells.  For every state it
checks literal/window equality, the terminal clock, invariance, divisibility,
quotient reconstruction, and membership of the residual in `Q^(-1)(1)`.
For every target and every input degree it checks the exact fibre formula,
then the bounded sum.  For every irreducible degree in range it checks the
classical total, the Reis fixed count, and the number and lengths of literal
translation orbits.  Finally it checks every degree cell in every available
depth CDF against an independently generated Euler product.

The `F9` lane is particularly informative: it simultaneously tests a genuine
extension field, odd characteristic, a nontrivial intermediate depth, and
the trace-owned fixed count `b_3=6`.

### 4.3 Reproduction and pinned evidence

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers127_131_sequence/phase1/verify_translation_gcd_extensions.py

PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers127_131_sequence/phase1/verify_translation_gcd_extensions.py \
  | cmp -s - \
  docs/papers127_131_sequence/phase1/TRANSLATION_GCD_EXTENSIONS_CANONICAL.txt
```

Fresh result: `cmp` status `0`.

```text
f2035f158049e880ce8c9471d85cf9bfe170a8faf076c147498232357b692b92
  verify_translation_gcd_extensions.py

826a73769c453b5227a4f7af0ab9fd2ced417c0ea15b6492b2910cc3e984677f
  TRANSLATION_GCD_EXTENSIONS_CANONICAL.txt
```

Expected terminus:

```text
TOTAL_ASSERTIONS=180403
scope_sentinel=finite extension-field enumeration is falsification evidence, never proof
credit_sentinel=old window/clock/fixed/depth results remain zero credit
release_sentinel=bounded owner non-hit is not novelty or priority; external HOLD
```

## 5. Direct-owner audit

Searches were run on 2026-08-31 UTC.  Technical ownership below is based
only on primary papers or author/official preprints.  Search-engine absence
is not evidence of novelty.

### 5.1 Direct hits and zero-credit subtraction

| primary source | directly owned interface | mandatory subtraction |
|---|---|---|
| T. Garefalakis, [*On the action of `GL_2(F_q)` on irreducible polynomials over `F_q`*](https://doi.org/10.1016/j.jpaa.2010.10.015), JPAA 215 (2011), 1835--1843 | action of `GL_2(F_q)` on irreducibles; fixed points and enumeration for `x -> x+b`, including translations of order `p` | translation action on irreducibles and its fixed-count formula are zero credit |
| L. Reis, [*The action of `GL_2(F_q)` on irreducible polynomials over `F_q`*](https://arxiv.org/abs/1608.03915), especially Theorems 1 and 2 | for an `F_p`-subspace `S`, characterizes all `S`-translation-invariant polynomials as `f(P_S(x))`; for one-dimensional `S`, states exactly `(p-1)/(pm) sum_(d|m,(d,p)=1) mu(d)q^(m/d)` | `F_q[x^p-x]` for `S=F_p`, the Artin--Schreier trace criterion, and the exact `b_(pm)` formula are zero credit |
| R. Gow and G. McGuire, [*Invariant Rational Functions, Linear Fractional Transformations and Irreducible Polynomials over Finite Fields*](https://doi.org/10.1016/j.ffa.2021.101991), FFA 2022 | subgroup actions in `PGL_2`, invariant rational functions, orbit polynomials, and factorization patterns | generic orbit-polynomial and invariant-function language is zero credit |
| M. Schulz, [*Rational Transformations and Invariant Polynomials*](https://arxiv.org/abs/2306.13502), 2023 | quotient maps for finite `PGL_2` subgroups and factorization of invariant rational transformations | generic quotient-map/factor-orbit theory is zero credit; do not call the present `Q` a new invariant-theory quotient map |
| J. Gerhard, M. Giesbrecht, A. Storjohann, E. V. Zima, [*Shiftless Decomposition and Polynomial-time Rational Summation*](https://doi.org/10.1145/860854.860887), ISSAC 2003 | shifted polynomial gcds, dispersion, shift classes, and gcd-based shiftless factorization in characteristic zero | shifted-gcd and shift-class algorithmic vocabulary is zero credit; this source does not own the finite-characteristic temporal census |
| F. Reimers, [*Separating invariants of finite groups*](https://doi.org/10.1016/j.jalgebra.2018.03.022), J. Algebra 2018 | modular finite-group invariant-ring background, including the additive cyclic action | invariant-ring background is zero credit |

Reis is the decisive missed owner.  Its formula is not merely adjacent: it is
algebraically identical to the scout's `b_(pm)` display.  Gow--McGuire alone
is not an adequate citation/subtraction for that formula.

### 5.2 Bounded non-hit

The following focused queries did not locate a primary source stating the
same iterated self-map together with the all-depth Euler product and every
terminal target fibre:

```text
"gcd(f(x), f(x+1))" polynomial finite field
polynomial "orbit gcd" finite group action gcd translates
"gcd" "group orbit" polynomial invariant divisor
finite group action polynomial gcd all translates invariant core
translation gcd polynomial dynamics finite field depth generating function
```

This is recorded only as **NO DIRECT HIT LOCATED IN THE BOUNDED QUERY**.
It is not novelty clearance.  In particular, the residual could still be
judged too mechanical after the owner and internal subtractions even if no
same-map paper exists.

## 6. Internal collision/value attack

### 6.1 P110 is the primary collision

P110 defines on the partition lattice

```text
J(x)=x join sigma(x)
```

under a cyclic automorphism and proves

```text
J^t(x)=join_(0<=j<=t) sigma^j(x).
```

Translation--GCD is precisely

```text
T(x)=x meet sigma(x),
T^t(x)=meet_(0<=j<=t) sigma^j(x)
```

in the free divisibility lattice of monic polynomials.  Hence the generic
semilattice fold, the invariant terminal projection, absence of nontrivial
recurrence, and finite group-order clock are already occupied up to order
duality.  They cannot support the value case for `P01`.

The surviving literal separation is real: P110's endpoint is a subgroup
coset partition with Möbius--Bell basins and primitive-chord depth, whereas
`P01` has irreducible-orbit exponent minima, a run-avoidance Euler product,
and uniform graded fibres over invariant polynomials.  This is why the
collision forces subtraction and comparison rather than an automatic kill.

### 6.2 Other portfolio interfaces

- **P115:** same broad carrier category (bounded polynomials over finite
  fields) and another exact image/fibre package, but its Cartier
  coefficient-decimation update and semilinear index chains are not
  conjugate to divisibility meet.  This raises portfolio crowding/value
  pressure, not a literal collision.
- **P105:** cycle-minimum pruning spends generic “cyclic minima plus finite
  depth” rhetoric.  The polynomial exponent-vector transfer is different,
  so only broad temporal language is subtracted.
- **P124:** exact basins and finite-state transfer already appear in the
  portfolio, but on a cross-colon ideal map.  Transfer machinery itself is
  zero credit; the candidate must foreground its specific all-degree
  polynomial enumeration.
- **old P112--P116 algebra scout:** the map, prime-field clock, fixed ring,
  and depth tables are internally archived and cannot be recycled as this
  round's progress.

No direct collision with P119, P123, P125, or P126 was found at the literal
map or primary proof-engine level.

### 6.3 “So what?” test after subtraction

What remains is narrower than the current scout presentation suggests.

1. **Substantive residual A:** one formula gives every exact degree and
   every depth for the literal map over all `q=p^a`, by coupling an owned
   irreducible-orbit census to a cyclic residual-exponent statistic.
2. **Residual B:** the terminal projection has a unique graded
   invariant/residual split, yielding an exact unit-fibre OGF and every
   target fibre, exact-degree and degree-capped.

Residual A is the value anchor.  Residual B is clean but nearly mechanical
once exponent minima are written down.  The candidate therefore passes only
as a conditional old-reserve re-entry.  If the global comparison cannot make
Residual A the clear center, or if a direct source owns the same depth Euler
product, the proper decision is `KILL`, not a paper led by the old clock or
fixed ring.

## 7. Required rewrite before re-entry

The following repairs are mandatory before any proof dossier or manuscript.

1. Add Garefalakis and Reis to the direct-owner table.  State explicitly
   that Reis Theorem 2(c) is the displayed `b_(pm)` formula.
2. Move the invariant-ring characterization, fixed irreducible
   characterization/count, trace criterion, and `a_d` orbit quotient into
   zero-credit background.
3. Replace “terminal kernel” in prose by “unit fibre”, “terminal-free
   residual class”, or `Q^(-1)(1)`.  If the symbol `K_n` is retained, say it
   is a counting notation only.  Include the nonmultiplicativity
   counterexample or an equally explicit warning.
4. Prove the fibre split using orbit exponents or the restricted identity
   `Q(hg)=hQ(g)` for invariant `h`; never assert that `Q` is a monoid
   morphism.
5. Add a point-by-point P110 order-dual firewall.  The semilattice iterate,
   clock, endpoint/recurrent statements, and generic cyclic closure receive
   zero credit.
6. Make the all-depth Euler product the sole lead theorem.  Terminal fibres
   may be the second theorem/corollary package; old window, fixed, and sharp
   clock results may appear only as setup or boundary checks.
7. Carry `q=p^a` from the first definition and distinguish the order-`p`
   subgroup generated by `1` from the full additive group of `F_q`.
8. Preserve the extension-field verifier and canonical output as independent
   gate evidence; do not merge it into or replace it with the prime-field
   discovery engine.
9. Submit the rewritten residual to the global five-system value comparison.
   No number or paper directory may be assigned solely on this gate.

## 8. Claim ceiling

If the rewrite closes every item above and the global comparison selects the
candidate, the maximum defensible internal claim package is:

1. for the already-defined finite-field translation--GCD map, an exact
   all-degree OGF for depth at most `t`, `0<=t<=p-1`, expressed through the
   cyclic residual-vector polynomial and the **owned** fixed-irreducible
   counts;
2. exact depth layers by consecutive differences of those OGFs;
3. the unique graded terminal-core/residual split;
4. the unit-fibre OGF and coefficients; and
5. every exact-degree and degree-capped fibre over each invariant terminal
   target, valid for all finite fields `F_(p^a)`.

The following claims are above the ceiling or forbidden:

- novelty or priority for the literal map;
- novelty for the sliding-window identity, `p-1` clock, sharp witness,
  invariant ring, fixed counts, translation irreducible classification, or
  `b_d` formula;
- calling `Q^(-1)(1)` an algebraic kernel or implying that `Q` is
  multiplicative;
- presenting a generic finite-group semilattice orbit fold as a new engine;
- claiming extension-field enumeration proves the all-parameter theorem;
- claiming a bounded owner non-hit establishes novelty; or
- external release without a later specialist owner audit and explicit
  authorization.

## 9. Gate disposition

| axis | disposition |
|---|---|
| literal correctness | **PASS** |
| extension-field translation | **PASS** (`F4/F8/F9`) |
| fixed irreducible formula | **PASS mathematically / DIRECTLY OWNED** |
| all-depth Euler product | **PASS mechanically / residual owner risk remains** |
| terminal split and fibres | **PASS after kernel terminology repair** |
| P1--P126 firewall | **REWRITE: P110 order-dual collision must be explicit** |
| short-paper value | **CONDITIONAL / borderline; global comparison required** |
| novelty/priority | **NOT ESTABLISHED** |
| external release | **HOLD** |

**Final gate:** `REWRITE -> CONDITIONAL RE-ENTRY TO GLOBAL VALUE GATE`.
Failure to zero-credit Garefalakis/Reis, repair the false kernel implication,
or distinguish the residual from P110 changes the decision to `KILL`.
Successful repair does not itself freeze a paper; it only restores eligibility
for the five-system comparison.
