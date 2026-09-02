# Independent candidate hostile gate — P162--P166

**Gate date:** 2026-09-02 UTC  
**Scope:** four proposed candidates only; no manuscript allocation  
**External state:** `HOLD_EXTERNAL`  
**Calibration:** `NOT_CALIBRATED`

## Outcome first

The four candidates do not yield a green paper pool.  The exact formulae
survive the independent arithmetic checks, but three candidates fail the
portfolio/owner/value gate.  Only `BQC` remains, and only at **low amber**.

| candidate | mathematical audit | decisive hostile result | theorem mass after subtraction | verdict |
|---|---|---|---|---|
| `RFW`, reciprocal Fibonacci window | exact formulas survived; no counterexample in the checked prime grid or the `p=2` control | reciprocal coordinates conjugate the entire nonsingular core to the ordinary Fibonacci matrix; the singular splice reuses the occupied P108/P115/P150 package | cycle/clock data are finite-linear background; only a deleted projective-orbit boundary remains | **KILL** |
| `CNG`, cyclic neighbour--GCD | sliding-window, depth, image, and fibre claims survived, including `m=1` and cap zero | it is exactly the already-killed `R11 cyclic adjacent-gcd smoothing`; its binary shadow is exactly the already-killed `X05: w -> w AND shift(w)` | none after the literal internal collision | **KILL** |
| `AA01/USP`, unit-pivot Schur stripping | formulas survived over both `Z/4Z` and `F_2[epsilon]/(epsilon^2)` | the dynamics is pivot-without-permutation Gaussian elimination; both advertised axes are one reverse-LDU product count | one lemma with geometric and fibre corollaries, not two independent axes | **KILL** |
| `BQC`, consecutive-block graph quotient | all checked boundary, image, clock, mass, and source-edge-weight identities survived | quotient graphs are directly owned; the inverse atlas is the generic subset-direct-image bin product | correct and compact, but owner-exposed and probably below a full note without a genuinely separate third axis | **AMBER (LOW)** |

There are therefore **zero GREEN, one AMBER, and three KILL** decisions.  This
is an insufficient pool for a five-paper batch.  No killed candidate is a
silent reserve.

## Audit basis

I read the four scout implementations/transcripts, the arithmetic and graph
owner logs, the P1--P161 occupancy summaries, and the nearest theorem and kill
ledgers.  In particular, the gate used the following internal controls rather
than comparing titles alone:

- P108: exact Fibonacci iterates, clock, image, and every-fibre geometry;
- P115: generic finite-linear component, tree, image, fibre, and zeta engine;
- P150: a zero-totalized finite-field rational map with a singular affine
  boundary, complete cycles, tails, image, and codomain-wide fibres;
- the P117--P121 killed candidate `R11`, literally cyclic adjacent-GCD
  smoothing;
- the P132--P136 killed candidate `X05`, literally `w -> w AND shift(w)`;
- P97/P143/P148 and the current graph scout as controls for direct images,
  quotient structure, and fixed-block contraction;
- the permanent exclusions against renamed classical algorithms, elementary
  erosion, generic finite-linear functional graphs, and transferred proof
  engines.

The independent verifier is
[`hostile_gate/verify_gate.py`](hostile_gate/verify_gate.py).  It imports no
scout code and uses exact integer/ring arithmetic.  A fresh run made
**747,537 assertions** and returned `STATUS PASS`.  It adds controls that are
not present in exactly that form in the scouts:

1. `RFW`: `p=2,3,5,7,11,13`, direct functional-graph depths, every-time fibres,
   projective bad lines, and pointwise reciprocal conjugacy wherever defined;
2. `CNG`: `m=1`, exponent cap zero, the literal prime-power GCD shadow, and the
   exact binary-AND conjugacy;
3. `USP`: two nonisomorphic local rings of order four, all source matrices
   through size three, all survival/failure shells, their mass identity, and
   matching-stratum target fibres;
4. `BQC`: `n=1`, `c>n`, unequal last blocks, `t=0`, post-stabilization times,
   exact images, pointwise semigroup law, global mass, and every coefficient
   of each checked source-edge-weight fibre polynomial.

The four author verifiers were also replayed fresh and byte-compared with
their frozen transcripts:

| source verifier | frozen assertions | replay |
|---|---:|---|
| `root/verify_rfw.py` | 2,425,108 | byte-match / PASS |
| `root/verify_cng.py` | 36,435 | byte-match / PASS |
| `arithmetic_algebra/verify_scout.py` | 18,528 across 12 systems | byte-match / PASS |
| `graph_set/verify_scout.py` | 1,217,850 across 16 systems; 98,320 attributed to `BQC` | byte-match / PASS |

These runs are falsification evidence only.  They do not establish the
untested all-parameter statements or ownership.

## 1. `RFW` — reciprocal Fibonacci window

### Cold derivation

For a prime `p`, totalize inversion by `inv0(0)=0` and let

```text
H(x,y) = (y, xy inv0(x+y)).
```

On the nonsingular torus `xy(x+y) != 0`, put

```text
Psi(x,y) = (x^(-1),y^(-1)),       M(u,v)=(v,u+v).
```

Then the claimed nonlinear core collapses immediately:

```text
Psi H Psi^(-1) = M.
```

Let `z=z(p)` be the least positive index for which `F_z=0 mod p`.  The
singular directions are the single projective orbit

```text
[M^j(1,0)],  0 <= j < z.
```

This gives the depth histogram without any functional-graph search:

```text
N_0 = p^2-z(p-1),
N_1 = p-1,
N_2 = 2(p-1),
N_d = p-1                 for 3 <= d <= z-1.
```

In particular the sharp maximum depth is `z-1`.  The sink fibre is

```text
|(H^t)^(-1)(0,0)| = 1                         t=0,
                     p                         t=1,
                     1+min(t+1,z)(p-1)         t>=2.
```

The one-step inverse law is also forced directly by solving
`a=y`, `b=xy/(x+y)`:

```text
p   at (a,b)=(0,0);
0   at a=0,b!=0;
2   at a!=0,b=0;
0   at a=b!=0;
1   at ab!=0,a!=b.
```

On the recurrent set, the fixed-point count at time `k` is

```text
p^nullity(M^k-I) - z(p-1) 1_{M^k=I},
```

and Möbius inversion gives the cycle census.  Thus every displayed temporal
quantity is either ordinary Fibonacci-matrix arithmetic or accounting for
one removed projective orbit.

### Boundary and counterexample attacks

- `t=0` gives identity fibres of size one.
- The `p=2` control still satisfies the depth and fibre formulas, but its
  nonsingular torus chart is empty.  This is a degenerate extension, not a
  counterexample and not additional paper value.
- Coordinate-axis orientation matters: `(x,0)` has depth one, while `(0,y)`
  with `y!=0` has depth two.  The independent implementation checked both.
- For all checked targets through saturation, fibre mass is exactly `p^2`.
- No counterexample was found.  The hostile failure is contribution-level,
  not correctness-level.

### Owner and internal collision

Brison--Nogueira's primary paper on
[matrices and linear recurrences in finite fields](https://doi.org/10.1080/00150517.2006.12428322)
and Vinson's primary paper on
[period versus rank of apparition](https://doi.org/10.1080/00150517.1963.12431578)
own the `M`, order, period, and `z(p)` inputs.  Elspas and the finite-linear
sources already subtracted for P115 own generic state-diagram machinery.  A
bounded exact-map search did not locate this literal totalization, but the
decision does not rely on that non-hit.

Internally, the main conjunction is already occupied in pieces:

| interface | occupied engine |
|---|---|
| Fibonacci iterate and sharp Fibonacci clock | P108 |
| finite-linear recurrent core, fixed/cycle/Möbius census | P115 |
| zero-totalized finite-field rational map, singular tree, every-target fibres | P150 |

Unlike P150, `RFW` has an arithmetic height `z(p)-1`; however that height is
exactly the classical rank of apparition of the linearized matrix.  Once this
is subtracted, the residual is merely the boundary splice of one projective
orbit.  This is the same failure mode for which the P157--P161 gate killed
the totalized Cremona control after its standard core and totalization
silhouette were removed.

### Verdict and frozen claim ceiling

**KILL — internal proof-package collision.**  The literal map may be retained
as a negative scouting example, but it must not receive a paper number.

If the result is ever cited internally, the maximum honest claim is:

> The totalized map is the reciprocal-chart pullback of the Fibonacci matrix
> away from a single projective singular orbit, from which its boundary depths
> and fibres follow.

Do not claim a new Fibonacci recurrence, rank-of-apparition law, finite-linear
functional graph, zeta method, or general zero-totalization mechanism.  A
revival would require a genuinely independent invariant not reducible to
`(M,z(p))` and a fresh portfolio decision; the current formulas are frozen
negative evidence, not a reserve.

## 2. `CNG` — cyclic neighbour--GCD

### Cold derivation

For a cyclic tuple of divisors of `N`, write the `p`-adic exponents as
`a_i(p)`.  The literal update

```text
d_i' = gcd(d_i,d_(i+1))
```

is componentwise

```text
a_i'(p)=min(a_i(p),a_(i+1)(p)).
```

Associativity and idempotence of `min` give, for every `t`,

```text
T^t(a)_i = min_{0<=j<=t} a_(i+j).
```

For one prime, the depth is the longest cyclic run strictly above the global
minimum, capped at `m-1`; for several primes, the depth is the maximum of
these primewise depths.  The one-step image criterion is also elementary:
a target is in the image exactly when it has no strict cyclic local minimum.
The canonical predecessor is

```text
a_i=max(b_(i-1),b_i).
```

Target fibres and the depth CDF can be written as traces of the appropriate
finite transfer matrices.  CRT multiplies target fibres and takes the maximum
of primewise clocks.  These claims are correct in the checked range, including
`m=1`, where every state is fixed.

### Decisive literal collision

This candidate is not merely similar to a previous paper.  It is the same
system already recorded and killed in
`docs/papers117_121_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md`:

```text
R11 | cyclic adjacent-gcd smoothing | exact sliding-window gcd
    | kill: semilattice erosion/P100
```

The binary exponent layer is additionally the exact system `X05` in the
P132--P136 cross-family scout:

```text
w -> w AND shift(w) | fixed-only recurrence, height n-1
                    | kill: elementary erosion
```

The independent verifier checks this bitwise equality state by state.  The
external cellular-morphology literature also treats erosion as a cellular
automaton; for example the primary IEEE paper
[Cellular Mathematical Morphology](https://doi.org/10.1109/MICAI.2007.30)
explicitly reformulates erosion in CA terms.  That external adjacency is not
needed for the kill because the internal literal collision is already fatal.

### Verdict and frozen claim ceiling

**KILL — exact internal re-entry.**  The transfer-matrix depth CDF and
target-resolved traces do not reopen an explicitly killed literal system;
they are standard regular-language enumeration layered on the same erosion.

The frozen ceiling is a ledger statement only: cyclic neighbour-GCD is
primewise one-sided semilattice erosion with a sliding-window iterate.  No
paper, novelty, priority, or reserve claim is authorized.

## 3. `AA01/USP` — unit-pivot Schur stripping

### Cold derivation

Let `R` be a finite commutative local ring, `Q=|R|`, and `U=|R^x|`.  For

```text
A = [ a  b ]
    [ c  D ]
```

with `a` a unit, the update is `S(A)=D-ca^(-1)b`; otherwise it enters the
failure sink.  Given a target `B`, a reverse step chooses independently

```text
a in R^x,  b in R^(1 x k),  c in R^(k x 1),
```

and then forces `D=B+ca^(-1)b`.  Therefore the entire proposed package is the
single reverse-LDU product

```text
# survive t pivots in M_n(R) = U^t Q^(n^2-t),              0<=t<=n,
# first fail at t+1          = U^t Q^(n^2-t)(1-U/Q),       0<=t<n,
# sources of B in M_k(R)     = U^t Q^(2kt+t(t-1))
  from M_(k+t)(R).
```

The successful terminal mass `U^n Q^(n^2-n)` plus the `n` failure shells is
`Q^(n^2)`.  The `t=0` target fibre is one.  The statements must remain
source-stratum specific: if all matrix sizes and the fixed failure sink are
pooled, a global sink fibre is not one of the displayed formulas.

### Boundary and ring attacks

The independent implementation checked the formulas not only for residue
rings used by the scout but also for both nonisomorphic local rings of order
four:

```text
Z/4Z,                  Q=4,U=2;
F_2[epsilon]/(epsilon^2), Q=4,U=2.
```

All matrices through size three, every admissible survival time, every
failure shell, full mass, and every matching target fibre passed.  Thus no
counterexample was found to the advertised dependence on `(Q,U)`.

### Owner and theorem-mass attack

Parker's primary paper
[Schur complements obey Lambek's categorial grammar](https://doi.org/10.1016/S0024-3795(97)10033-7)
directly treats recursive Schur complements as Gaussian elimination and LU
decomposition.  Finite-ring matrix enumeration is also adjacent; the scout
correctly identifies Choosuwan--Jitman--Udomkavanich's
[finite principal-ideal-ring determinant work](https://arxiv.org/abs/1605.06826).
The bounded search found no paper stating the exact failure-sink packaging,
but that does not create value.

The progress threshold requires a genuinely separate second axis.  Here:

- the truncated-geometric survival law is the probability that successive
  LDU diagonal coordinates are units;
- the every-target fibre is the same LDU coordinate product with the final
  Schur block fixed;
- recovery of `(Q,U)` merely divides two instances of that same product.

No second proof object survives.  Calling the pivot loop a finite dynamical
system does not change the fact that this is standard Gaussian elimination
without row exchanges, expressly barred by the problem anchor's
renamed-classical-algorithm clause.

### Verdict and frozen claim ceiling

**KILL — correct but theorem-thin after direct mechanism subtraction.**  Do
not allocate a manuscript.

The maximum frozen statement is a reusable lemma:

> Reverse unit-pivot LDU coordinates over a finite commutative local ring give
> the displayed stratumwise survival, failure-shell, and prescribed-Schur-
> target counts.

It must be labelled an elementary Gaussian/LDU enumeration.  A revival would
need a genuinely independent arithmetic or structural theorem not determined
only by `(Q,U)` and not another reformulation of the same factorization.

## 4. `BQC` — consecutive-block graph quotient

### Cold derivation

Fix `n>=1`, `c>=2`, and

```text
q_c(i)=floor((i-1)/c)+1.
```

Map every edge through `q_c`, OR duplicate cross-block edges, and discard
loops, while retaining the ambient labels `[n]`.  Nested consecutive blocks
give

```text
Q_c^t = Q_(c^t),
m_t=ceil(n/c^t),
tau(G)=max_{uv in E(G)} min{t:q_(c^t)(u)=q_(c^t)(v)},
max_G tau(G)=ceil(log_c n).
```

The edge `{1,n}` is sharp.  At time `t`, let the block sizes be `s_r(t)`.
The exact image is every graph supported on `[m_t]`, and a supported target
`H` has source-edge polynomial

```text
(1+z)^[sum_r binom(s_r(t),2)]
  product_{{r,s} in E(H)} ((1+z)^[s_r(t)s_s(t)]-1).
```

The independent checks confirm all boundary cases in the scout:

- `n=1` has height zero and one state;
- `t=0` gives `z^|E(H)|` and a singleton identity fibre;
- `c>n` collapses every edge in one step;
- unequal final blocks use their actual sizes;
- unsupported targets have empty fibres;
- after stabilization, the empty-target polynomial is
  `(1+z)^binom(n,2)`;
- every coefficient sum agrees with the unweighted fibre, and all target
  fibres sum to `2^binom(n,2)`.

No mathematical counterexample was found.

### Strongest hostile reduction

Define a finite edge map

```text
f_t : binom([n],2) -> binom([m_t],2) union {bottom}
```

by sending an edge to its quotient edge or to `bottom` when its endpoints
coalesce.  Then `Q_c^t(G)` is simply the direct image of the subset `E(G)`,
with `bottom` discarded.  The entire fibre polynomial is the generic theorem
for a powerset direct image:

- elements of `f_t^(-1)(bottom)` are free;
- for every requested target element, choose a nonempty subset of its bin;
- for every omitted target element, choose the empty subset.

Thus the fibre atlas is exact, but its proof is not graph-specific.  It is one
application of independent subset bins.  The only other input is the
elementary `c`-adic endpoint coalescence schedule.

### Owner and internal comparison

Bubboloni's primary work on
[graph homomorphisms and quotient components](https://doi.org/10.4171/RSMUP/138-2)
and Hickingbotham--Jungeblut--Merker--Wood's
[squaregraph paper](https://doi.org/10.1002/jgt.23008) own the loopless
existential quotient convention: distinct cells are adjacent exactly when an
original edge crosses them.  Parthasarathy's primary
[enumeration of graphs with a given partition](https://doi.org/10.4153/CJM-1968-005-0)
is nearby but does not, on the inspected evidence, state this exact labelled
iterated fibre polynomial.  No direct owner of the full conjunction was found
in the bounded pass; this remains a non-hit, not novelty evidence.

The closest internal systems do not give a literal collision:

- P148 contracts selected levels of plane rooted trees and has recursive
  ordered-tree inverse geometry, not independent edge bins;
- P143 is a row-inclusion/preorder residual, not a fixed quotient of graph
  vertices;
- P97 is a nonlinear sumset map, although generic direct-image language and
  powerset-bin counting must receive zero credit.

This is enough to avoid a KILL, but not enough for GREEN.  Once graph quotient
and generic subset pushforward are subtracted, the residual proof is very
short, and both theorem axes are controlled by the same fixed endpoint map.

### Verdict and frozen claim ceiling

**AMBER (LOW) — mathematically closed, owner/value unresolved.**  It is the
only candidate that may proceed to a deeper specialist/value gate, but it
should not yet receive a paper number.

The maximum claim ceiling that may be frozen is exactly:

1. the labelled, loopless, consecutive-block OR quotient on the fixed ambient
   carrier;
2. `Q_c^t=Q_(c^t)`, the pointwise edge-coalescence clock, and sharp height;
3. the complete time-`t` image with actual short-block sizes;
4. the supported/unsupported every-target source-edge polynomial and its
   exact-weight coefficients.

Forbidden claims include novelty of quotient graphs, graph contraction,
blow-ups, direct images of subsets, independent-bin enumeration, or a generic
finite-map fibre theorem.  Promotion to GREEN requires both:

- a specialist owner check targeted at iterated fixed-partition quotients and
  prescribed quotient-graph enumeration; and
- a genuinely separate theorem axis whose proof is not just the same edge map
  or the generic powerset-direct-image product.

Without that additional axis, the honest terminal decision is
`KILL_OWNER_THIN`, even if the current formulas remain correct.

## Final gate instruction

```text
RFW       KILL_INTERNAL_P108_P115_P150
CNG       KILL_EXACT_PRIOR_R11_AND_X05
AA01/USP  KILL_CLASSICAL_LDU_THEOREM_THIN
BQC       AMBER_LOW_OWNER_AND_MASS_GATE
POOL      0 GREEN / 1 AMBER / 3 KILL
EXTERNAL  HOLD_EXTERNAL
```

No paper drafting, numbering, novelty language, public posting, specialist
contact, or external release is authorized by this gate.
