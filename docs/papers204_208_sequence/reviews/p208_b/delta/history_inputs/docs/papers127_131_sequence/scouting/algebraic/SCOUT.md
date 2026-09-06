# Algebraic/linear breadth scout for the P127--P131 sequence

Status: **SCOUT ONLY / NO PAPER NUMBER / NO FREEZE / EXTERNAL HOLD**  
Owner-search date: **2026-08-31 UTC**  
Mechanical status: **PASS, 27 literal systems, 740,365 exact assertions**

The identifiers below are local scout handles, not paper numbers.  This lane
enumerated 27 finite or locally finite maps in six families.  It advances no
newly discovered literal system.  One old reserve, `P01` below, earns a
**CONDITIONAL RE-ENTRY** because this pass adds an all-depth Euler product and
complete terminal quotient/kernel/fibre formulas.  The literal map, its
sliding-window identity, sharp clock, fixed set, and old depth tables were
already present in the P112--P116 scouting archive and receive zero credit.
The remaining 26 systems are killed here.

No bounded search miss in this report is evidence of novelty or priority.
No public posting, submission, priority language, or external release is
authorized.

## 1. Intake firewall and counting convention

The intake comparison covered the on-disk P1--P126 paper directories, the
historical collision maps, and the relevant prior scout ledgers.  In
particular:

- P99 occupies unipotent shear on fixed-index integer sublattices;
- P103 occupies double adjugation on full matrix spaces;
- P107 occupies annihilator--power ideal dynamics;
- P109 occupies nilpotent image dynamics on finite subspace lattices;
- P115 occupies bounded Cartier coefficient sections and their complete
  finite functional graphs;
- P119 occupies fixed-regular Engel commutator dynamics;
- P124 occupies cross-colon dynamics on rectangular monomial ideals; and
- P125 occupies a quadratic-state shear on a quadratic space over
  `F_2`.

The earlier hard ledger at
`docs/papers122_126_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md`
explicitly kills gcd/lcm comparators and ideal-pair meet/join as lattice
sorting or closure.  The P117--P121 firewall likewise gives zero credit to
ordinary closure, sorting, finite-linear functional graphs, and cosmetic
valuation or coefficient variants.  Those exclusions are applied below even
when a small exact census looks attractive.

An assertion is one deterministic Boolean equality or membership check made
by `verify_algebraic_scout.py`.  The script uses only standard-library exact
integer, finite-field, polynomial, relation, permutation, and bitset
arithmetic.  The assertion total is the sum of the per-system counters printed
in `CANONICAL.txt`; no setup operation or printed metric is counted as an
assertion.

| family | systems | assertions |
|---|---:|---:|
| finite modules/subspace lattices | 5 | 441,745 |
| finite rings | 4 | 1,857 |
| finite semigroups/relations | 5 | 199,250 |
| matrix actions | 5 | 3,081 |
| polynomial transforms | 5 | 93,802 |
| monomial-ideal transforms | 3 | 630 |
| **total** | **27** | **740,365** |

## 2. Literal catalogue and hostile disposition

### 2.1 Finite modules and subspace lattices

| handle | literal state space and update | exact range and assertions | observed signal | disposition |
|---|---|---:|---|---|
| `M01` | On `L(F_2^d)^r`, one left-to-right sweep applies `(U_i,U_{i+1}) -> (U_i intersect U_{i+1},U_i+U_{i+1})` for `i=1,...,r-1`. | `d=2,3`, `r=3..5`, 73,507 tuples; **431,009** | Universal depth at most `r-1`, sharp in every tested box; image is the weak flags.  Terminal fibre ranges include `1..8,742`. | **KILL COLLISION.**  The universal clock is a lattice-comparator fact.  Fibre constancy inside one dimension stratum is only `GL`-equivariance.  The internal meet/join-comparator hard exclusion applies. |
| `M02` | `(A,B,C) -> (A intersect (B+C), B intersect (C+A), C intersect (A+B))`. | all `16^3` triples in `L(F_2^3)`; **10,108** | Coordinatewise descent, maximum depth one; histogram `0:1090, 1:3006`. | **KILL.**  Shallow subspace closure with no second output and direct P109 adjacency. |
| `M03` | `U -> U^perp + <e_1>` on `L(F_2^3)` for the standard dot product. | all 16 subspaces; **32** | tails at most one and periods at most two. | **KILL.**  Ortholattice/affine closure is mature and the census is tiny. |
| `M04` | `v -> Jv` for the nilpotent Jordan shift on `F_2^d`, with zero as sink (equivalently, projective points plus the sink because the base field is `F_2`). | every vector for `2<=d<=8`, 508 states; **508** | absorption time is the highest occupied Jordan coordinate; maximum 8. | **KILL.**  Generic kernel-filtration clock and a direct P109 package collision. |
| `M05` | On ideals `(p^a)` of `Z/p^e`, apply the colon `(p^a):p=(p^max(a-1,0))`. | all `0<=a<=e`, `2<=e<=12`; 88 states; **88** | exact one-coordinate valuation erosion, maximum depth 12. | **KILL.**  Mechanical saturation/valuation lane; P99/P115 firewall. |

`M01` also supplied the smallest useful negative control.  In
`L(F_2^2)=M_3`, feed the three distinct lines `(L_1,L_2,L_3)`.  Two sweeps
give `(0,L_3,V)`, while reversing the first and third line gives
`(0,L_1,V)`.  Gerlach's symmetric lattice sort gives `(0,V,V)`.  Thus the
literal action is order-sensitive on a nondistributive lattice, but this
separation does not by itself overcome the prior comparator kill.

### 2.2 Finite rings

| handle | literal state space and update | exact range and assertions | observed signal | disposition |
|---|---|---:|---|---|
| `R01` | Artin--Schreier map `x -> x^2+x` in `F_(2^m)` using fixed irreducible polynomial bases. | every element for `2<=m<=5`, 60 states; **1,480** | profiles `m2:t2p1`, `m3:t1p3`, `m4:t4p1`, `m5:t1p15`. | **KILL.**  A linearized-polynomial/Frobenius map in disguise. |
| `R02` | Squaring `(a+b eps)^2=a^2+2ab eps` in `F_p[eps]/(eps^2)`. | `p=3,5,7`, 83 states; **166** | maximum tails `1,2,1` and periods `2,4,6`. | **KILL.**  Standard finite-ring power dynamics; no independent fibre signal. |
| `R03` | `d -> gcd(n,d^2-d)` on the divisor set of `n`. | `n=30,36,60,84,120`, 57 states; **114** | all orbits fix within two steps. | **KILL.**  CRT prime-support arithmetic is coordinatewise and shallow. |
| `R04` | `x -> x^(-1)` for units of `Z/n`, and `x -> 0` for nonunits. | `n=8,12,15,16,21,25`, 97 states; **97** | 28 fixed states; tail at most one, period at most two. | **KILL.**  Immediate involution plus a sink. |

### 2.3 Finite semigroups and relations

| handle | literal state space and update | exact range and assertions | observed signal | disposition |
|---|---|---:|---|---|
| `S01` | `f -> f o g o f` in the full transformation semigroup `T_n`, with `g` the standard `n`-cycle. | all maps for `n=3,4`, 283 states; **849** | rank never rises; maximum tail/period are both two. | **KILL.**  Broad sandwich-semigroup ownership and no clean second theorem. |
| `S02` | `R -> R union R^2` in the Boolean relation semigroup. | all `2^16` relations on four labelled points; **196,608** | 3,994 fixed relations; transitive closure is reached in at most two rounds. | **KILL.**  Literal repeated-squaring transitive closure. |
| `S03` | `R -> R intersect R^2`. | all 512 relations on three points plus strict total orders through `n=9`; **1,557** | strict order obeys `R_t=R^(2^t)`, with logarithmic deletion clock. | **KILL.**  Relation powers are the direct semigroup mechanism. |
| `S04` | On the `2 x 2` rectangular band `(i,j)(k,l)=(i,l)`, update `(a,b,c)->(ab,bc,ca)`. | all 64 triples; **128** | 16 fixed states and 48 states of period three, with no tails. | **KILL.**  Pure coordinate transport. |
| `S05` | `(x,y)->(xy,yx)` on `S_3 x S_3`. | all 36 pairs; **108** | tails through three, periods one/two; the two coordinates remain conjugate. | **KILL.**  Nielsen/Hurwitz-style group-action owner risk and no closed large-family census. |

### 2.4 Matrix actions

| handle | literal state space and update | exact range and assertions | observed signal | disposition |
|---|---|---:|---|---|
| `X01` | `A -> A^T+A^2` over `F_2`. | all matrices of sizes 2 and 3, 528 states; **1,056** | size three has tail 7 and period 6. | **KILL.**  No monotone proof spine and too close to P125's quadratic-state lane. |
| `X02` | `A -> [A,J]^2` in `M_2(F_3)`, `J=[[0,1],[0,0]]`. | all 81 matrices; **162** | every orbit fixes within two steps. | **KILL.**  Commulator-polynomial collapse overlaps P119/P125 controls. |
| `X03` | `A -> A^T J A` in `M_2(F_2)`, `J=[[0,1],[1,0]]`. | all 16 matrices; **48** | identically `det(A)J`, hence one-step collapse. | **KILL.**  Too small; direct quadratic-congruence identity. |
| `X04` | `A -> adj(A)+I` in `M_2(F_3)`. | all 81 matrices; **162** | no fixed point; periods three/six. | **KILL.**  Direct near-variant of P103 double-adjugate dynamics. |
| `X05` | In the disjoint union of square matrix sizes, choose the lexicographically first nonzero pivot, take its Schur complement, and delete the pivot row/column; zero matrices fix. | all 512 initial `3 x 3` matrices over `F_2`; **1,653** | termination time equals rank; rank histogram `1,49,294,168`. | **KILL.**  Gaussian elimination translated into a shrinking map. |

### 2.5 Polynomial transforms

All polynomials are represented densely and normalized to be monic whenever
the result is nonzero.

| handle | literal state space and update | exact range and assertions | observed signal | disposition |
|---|---|---:|---|---|
| `P01` | `T(f)=gcd(f(x),f(x+1))` on monic `F_p[x]`, including `1`. | `(p,D)=(2,7),(3,6),(5,5)`, 5,254 states; **44,472** | sharp depths `1,2,4`; 34 terminal images; all-depth top-degree CDFs include `p=5: 5,2575,3025,3105,3125`; terminal kernel fibres `129,973,3901`. | **CONDITIONAL RE-ENTRY, not a new literal system.**  New residual: all-depth Euler product plus exact terminal quotient/kernel/fibres. |
| `P02` | `f -> gcd(f(x), monic(f(2x)))` over `F_5`. | degree at most 5, 3,906 states; **16,258** | same sliding-minimum law for a multiplicative orbit of length four; depth three. | **KILL SIBLING.**  It is a generic cyclic-automorphism control, not an independent paper direction. |
| `P03` | `f -> gcd(f,f')`; if `f'=0`, this fixes `f`. | `(p,D)=(2,8),(3,6),(5,5)`, 5,510 states; **11,023** | multiplicity descent, tails `1,2,4`. | **KILL.**  Squarefree/inseparable factor extraction is classical; the prior differential-core scout is closer still. |
| `P04` | `f -> monic(f(x+1)-f(x))`, with zero fixed. | same three boxes, 5,513 states; **11,029** | nilpotent with characteristic-dependent plateaux; maximum depths `2,3,5`. | **KILL.**  Finite-difference calculus owns the mechanism; old A3 hard kill. |
| `P05` | `f -> gcd(f, monic(x^deg(f)f(1/x)))`. | same three boxes, 5,510 states; **11,020** | idempotent after at most one nontrivial step. | **KILL.**  Self-reciprocal factor extraction is mature and dynamically shallow. |

### 2.6 Monomial-ideal transforms

The phase is the 70 upward-closed exponent sets in the box `[0,3]^2`, i.e.
monomial ideals truncated by `(x^4,y^4)`.

| handle | literal update | range and assertions | observed signal | disposition |
|---|---|---:|---|---|
| `I01` | Add every Borel move `(a,b)->(a+1,b-1)` with `b>0`, then take upward closure. | all 70 ideals; **210** | 28 fixed ideals, maximum depth three. | **KILL.**  Standard strongly-stable/Borel closure and P124 crowding. |
| `I02` | Reflect the exponent box through `(a,b)->(3-a,3-b)` and complement. | all 70 ideals; **210** | six fixed ideals and 64 points in two-cycles. | **KILL.**  Boxed Alexander duality is a direct involution. |
| `I03` | Truncated Minkowski square of the exponent upset, followed by upward closure. | all 70 ideals; **210** | two fixed ideals, maximum depth three. | **KILL.**  Direct ideal powers and P107 collision. |

## 3. Sole conditional re-entry: translation--GCD erosion

### 3.1 Provenance and zero-credit ledger

This literal system is not a new discovery.  It appears as rank 3,
`RESERVE / HOLD`, in
`docs/papers112_116_sequence/scouting/ALGEBRAIC_SCOUT.md`, with a separate
382,545-assertion verifier at
`docs/papers112_116_sequence/scouting/code/algebraic_translation_gcd.py`.
The following are therefore **zero credit in this round**:

1. `T^t(f)=gcd(f(x),f(x+1),...,f(x+t))`;
2. stabilization by time `p-1` and its sharp witness;
3. the terminal invariant ring `F_q[x^p-x]`;
4. bounded fixed counts; and
5. the previously enumerated depth profiles.

The re-entry is supported only by the new closed all-depth census and the
terminal quotient/kernel/fibre package below.  It enters the later global
value comparison as an old reserve that has met its stated repair condition,
not as another intake discovery.

### 3.2 Theorem-level contract

Let `q=p^a`, let `sigma f(x)=f(x+1)` on monic `F_q[x]`, and put

```text
T(f)=gcd(f,sigma f),       Q(f)=T^(p-1)(f).
```

The contract has four clauses.

**Temporal quotient.**  For every `t>=0`,

```text
T^t(f)=gcd_(0<=j<=t) sigma^j f.
```

Thus `Q` is an idempotent retraction to the monic part of
`F_q[x^p-x]`.  The bound `p-1` is sharp already for
`f=(x^p-x)/x=x^(p-1)-1`.

**Orbit-exponent conjugacy.**  Translation acts on monic irreducibles in
orbits of length one or `p`.  On a nonfixed orbit, write the exponent vector
of `f` as `(e_0,...,e_(p-1))`.  At time `t`, every coordinate is the minimum
over a cyclic window of length `t+1`.  After subtracting
`m=min_j e_j`, the local depth is the longest cyclic run of positive
coordinates.  Fixed irreducibles contribute no transient.

**All-depth census.**  Let

```text
N_d(q) = (1/d) sum_(e|d) mu(e) q^(d/e)
```

be the number of monic irreducibles of degree `d`.  Let `b_d` be the number
fixed by translation.  It is zero unless `d=pm`; if `m=p^v s` with
`gcd(s,p)=1`, the Artin--Schreier trace calculation gives

```text
b_(pm) = (p-1)/(p m) sum_(e|s) mu(s/e) q^(p^v e).
```

Hence the number of nonfixed irreducible `p`-orbits of degree `d` is
`a_d=(N_d(q)-b_d)/p`.

For `0<=t<=p-1`, define

```text
R_(p,t)(y)
  = sum y^(c_0+...+c_(p-1)),
```

where the sum is over nonnegative cyclic vectors with minimum zero and no
positive cyclic run longer than `t`.  This is explicit: if `u=y/(1-y)` and
`M_t(u)` has entries

```text
(M_t)_(i,0)=1                    for 0<=i<=t,
(M_t)_(i,i+1)=u                  for 0<=i<t,
all other entries zero,
```

then `R_(p,t)(y)=trace(M_t(u)^p)`.  The exact-degree OGF for states of depth
at most `t` is

```text
H_(q,p,t)(z)
  = 1/(1-q z^p) product_(d>=1) R_(p,t)(z^d)^(a_d).
```

Consequently, `H_t-H_(t-1)` is the exact depth-`t` OGF.  At the terminal
time,

```text
R_(p,p-1)(y)=(1-y^p)/(1-y)^p,
H_(q,p,p-1)(z)=1/(1-qz),
```

which supplies an internal boundary check rather than an additional claim.

**Terminal kernel and every fibre.**  Every monic polynomial has the unique
factorization

```text
f = Q(f) g,       Q(g)=1.
```

Let `K_(q,p,n)` count monic exact-degree-`n` kernel elements.  The degree OGF
and coefficients are

```text
K_(q,p)(z) = (1-q z^p)/(1-qz),

K_(q,p,n) = q^n,                         0<=n<p,
             q^n-q^(n-p+1),              n>=p.
```

If `h` is invariant of degree `m`, then among inputs of exact degree `N` the
fibre of `Q` over `h` has size `K_(q,p,N-m)` (zero when `N<m`).  On the
degree-at-most-`D` phase its size is

```text
sum_(0<=n<=D-m) K_(q,p,n).
```

The terminal image in that phase contains
`sum_(0<=j<=floor(D/p)) q^j` states.

### 3.3 Proof skeleton

There are two substantive proof spines and a factorization-free control.

1. **Divisibility-semilattice spine.**  GCD commutes with the automorphism
   `sigma`.  Induction gives the sliding-window formula.  The order-`p`
   identity `sigma^p=1` makes the terminal gcd invariant.  Unique
   factorization turns each irreducible orbit into a cyclic sliding-minimum
   system and proves the run-length depth rule.
2. **Artin--Schreier/transfer spine.**  A translation-fixed irreducible is
   `h(x^p-x)`.  Capelli plus Artin--Schreier theory says irreducibility is
   controlled by nonzero absolute trace of a root of `h`; Möbius inversion
   over subfields yields `b_(pm)`.  On a nonfixed orbit, the support of the
   positive residual exponents is a cyclic binary word, while each selected
   coordinate contributes `y/(1-y)`.  The finite run automaton gives
   `R_(p,t)`, and the Euler product over irreducible orbits gives every depth
   layer.
3. **Terminal product spine.**  Subtract the common minimum exponent on each
   nonfixed orbit and remove every fixed factor.  This proves the unique
   product `f=Q(f)g`.  Dividing the OGF `1/(1-qz)` for all monic polynomials
   by `1/(1-qz^p)` for invariant monics gives the kernel OGF and every fibre.
   The verifier independently performs literal polynomial shifts and Euclidean
   GCDs; it does not factor its phase polynomials.

### 3.4 Counterexample and boundary stress

- `p=2` is not inferred from an odd-prime formula.  The exact-degree-seven
  CDF is `0,128`, and the terminal kernel fibre over `1` in degree at most
  seven has size 129.
- For `p=3,D=6`, the top-degree CDF is `9,540,729`; for `p=5,D=5` it is
  `5,2575,3025,3105,3125`.  Every cell is checked against literal iteration.
- The verifier checks `1`, invariant inputs, non-squarefree inputs, partial
  irreducible orbits, and the sharp missing-one-linear-factor witness.
- Characteristic zero has no finite order-`p` translation clock, so the
  theorem does not extend there.
- The dilation control `P02` shows that cyclic-automorphism erosion is a
  broader mechanism.  It is killed as a sibling; no uniqueness is claimed
  for the construction.
- The theorem contract allows `q=p^a`, but the present exact pilot uses prime
  fields.  An extension-field verifier is mandatory before any freeze.

### 3.5 Internal collision firewall and kill conditions

Literal separation from the four emphasized occupied papers is clear:

- P115 selects and inverse-Frobenius-transforms coefficient chains; `P01`
  takes gcds in the divisibility lattice under a translation automorphism.
- P119 is a group commutator/Engel image map.
- P124 is a synchronous pair of colon operations on bounded monomial ideals.
- P125 is a quadratic pair shear on `V x V` over `F_2`.

That separation is not a novelty certificate.  Re-entry is killed or
rewritten if any of the following occurs:

1. a primary source states the same all-depth Euler product or the same
   terminal quotient/kernel/fibre conjunction;
2. the extension-field version invalidates the trace-orbit count or loses a
   claimed boundary;
3. the global five-system value gate refuses re-entry of a prior reserve;
4. the result is judged to be only the generic finite-group gcd core with a
   mechanical specialization; or
5. the final package cannot keep the old sliding-window, clock, invariant
   ring, and depth tables visibly at zero contribution credit.

Current decision: **CONDITIONAL RE-ENTRY TO GLOBAL VALUE GATE / EXTERNAL
HOLD**.

## 4. Direct-owner screen

Only primary technical papers and author/official preprints are used here.
The searches are bounded and were run on 2026-08-31 UTC.

### 4.1 Translation--GCD owner subtraction

| direct source | what it directly owns | zero-credit subtraction here | residual not located in that source |
|---|---|---|---|
| J. Gerhard, M. Giesbrecht, A. Storjohann, E. V. Zima, [*Shiftless Decomposition and Polynomial-time Rational Summation*](https://doi.org/10.1145/860854.860887), ISSAC 2003 | dispersion sets, shifted polynomial gcds, and shiftless factorization for rational summation | shifted-gcd/dispersion vocabulary and algorithmic background | finite-characteristic iteration, depth layers, terminal fibres |
| D. Grigoriev, [*Testing shift-equivalence of polynomials by deterministic, probabilistic and quantum machines*](https://doi.org/10.1016/S0304-3975(96)00188-0), TCS 1997 | polynomial shift equivalence, including finite-field cases | the shift-equivalence problem and stabilizer search | the gcd self-map and its census |
| Z. Dvir, R. Oliveira, A. Shpilka, [*Testing Equivalence of Polynomials under Shifts*](https://doi.org/10.1007/978-3-662-43948-7_35), ICALP 2014 | randomized shift-equivalence testing and its PIT relation | modern shift-equivalence algorithms | gcd erosion, exponent minima, fibres |
| F. Reimers, [*Separating invariants of finite groups*](https://doi.org/10.1016/j.jalgebra.2018.03.022), J. Algebra 2018, Example 2.6 | for the additive `C_p` action, `K[x]^(C_p)=K[x^p-x]` | the fixed/invariant ring in the theorem | the projection dynamics and enumerators |
| R. Gow, G. McGuire, [*Invariant rational functions, linear fractional transformations and irreducible polynomials over finite fields*](https://doi.org/10.1016/j.ffa.2021.101991), FFA 2022 | `PGL_2` actions, invariant rational functions, and orbit-polynomial factorization patterns | translation action on irreducibles and generic orbit-polynomial language | the cyclic sliding-minimum depth transfer and terminal fibres |
| prior internal scout, `docs/papers112_116_sequence/scouting/ALGEBRAIC_SCOUT.md` plus its 382,545-assertion code | this exact literal map, sliding-window identity, sharp clock, invariant fixed set/count, enumerated depth profiles | all five old items, in full | this round's all-depth Euler product and terminal kernel/fibre formula |

Queries retained in the search log:

```text
polynomial gcd f(x) f(x+1) finite field translation invariant paper
finite field shift-free polynomial factorization translation gcd f(x+1)
"gcd(f(x), f(x+1))" polynomial finite field
"Shiftless Decomposition" polynomial gcd shifts Storjohann
polynomial shift equivalence finite fields translation gcd irreducible factors paper
finite field polynomial translation invariants x^p-x primary paper
"orbit gcd" polynomial automorphism
"invariant divisor" gcd group orbit polynomial
```

No direct source for the displayed all-depth Euler product plus every terminal
fibre was located in these bounded queries.  This is only a non-hit and does
not support novelty, priority, or release.

### 4.2 Comparator dead-road owner screen

`M01` was screened far enough to justify its kill, not to rescue it.

| direct source | owned boundary | consequence |
|---|---|---|
| J. Gerlach, [*Sorting in Lattices*](https://arxiv.org/abs/1303.5560) (2013) | symmetric meet-of-joins lattice sorting, nondecreasing output, idempotence, permutation invariance | lattice sorting itself is zero credit |
| J. Gerlach, [*Recursive Sorting in Lattices*](https://arxiv.org/abs/1306.0019) (2013) | quadratic recursive/insertion sorting in distributive lattices | comparator-recursion background is zero credit |
| B. Komarath, J. Sarma, K. S. Sunil, [*Comparator Circuits over Finite Bounded Posets*](https://doi.org/10.1016/j.ic.2018.02.002), I&C 2018 | meet/join comparator gates over finite lattices and posets | the literal gate and circuit vocabulary are zero credit |
| J. Goldman, G.-C. Rota, [*On the Foundations of Combinatorial Theory IV: Finite Vector Spaces and Eulerian Generating Functions*](https://doi.org/10.1002/sapm1970493239), 1970 | finite-vector-space lattice and `q`-enumeration background | Gaussian subspace/flag counts are zero credit |

Relevant queries were:

```text
"lattice sorting" meet join comparator network paper
"bubble sort" lattice meet join paper
"insertion sort" nondistributive lattice meet join
"adjacent comparator" meet join lattice
"comparator" "subspace lattice" meet join sorting
```

The bounded search did not locate the exact repeated one-way sweep theorem,
but the internal hard exclusion and lack of a nontrivial subspace-specific
second output are independently sufficient to kill it.

## 5. Mechanical evidence and reproduction

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers127_131_sequence/scouting/algebraic/verify_algebraic_scout.py

PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers127_131_sequence/scouting/algebraic/verify_algebraic_scout.py \
  | cmp -s - \
  docs/papers127_131_sequence/scouting/algebraic/CANONICAL.txt
```

Expected terminus:

```text
TOTAL_ASSERTIONS=740365
scope_sentinel=finite enumeration is falsification evidence, never proof or ownership
novelty_sentinel=bounded owner non-hit is not novelty or priority
```

The canonical transcript records every system's literal finite range,
per-system assertion count, metrics, signal, and decision.  A fresh run is
byte-identical to that transcript.  The source tree is not a Git repository;
no commit, tag, paper directory, or paper number was created.

## 6. Handoff

- **New literal discoveries promoted:** 0.
- **Conditional old-reserve re-entries:** 1 (`P01`, translation--GCD).
- **Killed controls/dead roads:** 26.
- **Exact assertions:** 740,365.
- **Next gate for `P01`:** compare its genuinely new all-depth and fibre
  package against the other four lanes; then run an extension-field verifier
  and a specialist owner audit before any proof dossier or paper freeze.

