# Root cross-class breadth scout — P157--P161

**Systems tested:** 16. **Exact assertions:** 1,088,653.
**External state:** HOLD_EXTERNAL.

## Outcome

One genuinely nonlinear finite-ring system passes the Stage-1 gate. One
graph-decomposition system remains a collision reserve. The otherwise clean
Artin--Schreier system is downranked because P115 already occupies its
linear core/depth/fibre/cycle proof silhouette. Thirteen further systems
are killed before manuscript allocation.

| rank | ID | carrier and literal update | early exact signal | second axis | closest collision / owner | verdict |
|---:|---|---|---|---|---|---|
| 1 | NHI | $\mathbb Z/2^n\mathbb Z$, $x\mapsto3x^2-2x^3$ | error valuation doubles exactly; only 0 and 1 recur; sharp pointwise clock | complete image strata and every-target nonuniform fibres | idempotent lifting owns the polynomial and quadratic convergence, but not the finite atlas | **KEEP** |
| 2 | CMD | ordered path components, simultaneously delete the center(s) of each component | a part $m$ becomes two copies of $\lfloor(m-1)/2\rfloor$; exact survivor profile | bounded-composition census across starting linear forests | centroid decomposition; P114/P126 binary peeling/refinement | RESERVE_COLLISION |
| 3 | ASD | $\mathbb F_{q^m}$, $x\mapsto x^q-x$ | the $p$-part of $m$ is the exact tail height; closed layer sizes | polynomial-gcd fixed counts and cycle census | Artin--Schreier/normal basis; P115 same linear theorem silhouette | DOWNRANK |
| 4 | DGD | bounded monic polynomials, $f\mapsto\gcd(f,f')$ | irreducible multiplicities decrement synchronously | target-fibre Euler products | square-free factorization; P128 meet/Euler product | KILL_DIRECT_OWNER |
| 5 | AGW | divisor words, adjacent entries replaced by their gcd | rank-$t$ entries are length-$(t+1)$ window gcds | Boolean-prime image automaton | P128/P110 consecutive meet/join engine | KILL_INTERNAL |
| 6 | DFD | finite-field words, adjacent forward differences | every rank map is surjective with uniform fibres | binomial iterate formula | classical finite differences; generic linear rank loss | KILL_GENERIC |
| 7 | RAD | positive integers, $n\mapsto n/\operatorname{rad}(n)$ | prime exponents decrement; height is maximum exponent | square-free coprime predecessor series | P107/P142 valuation and ideal/exponent descent | KILL_INTERNAL |
| 8 | BRG | finite graphs, delete every bridge | all samples and the block theorem give one-step idempotence | no independent temporal axis | standard bridge decomposition | KILL_WEAK |
| 9 | TWN | graphs, quotient true/false twin classes | recursive trees can expose new twins | quotient fibres depend on modules | leaf/contraction portfolio plus modular decomposition | KILL_COLLISION |
| 10 | SEC | finite simplicial complexes, erase all free codimension-one faces | nontrivial collapse layers | possible target expansions | elementary collapse is direct owner; pruning silhouette | KILL_OWNER |
| 11 | FRO | nilpotent truncated polynomial ideals, $f\mapsto f^p$ | monomial valuations multiply by $p$ | coefficient fibres | P100/P115 valuation erasure and Cartier/Frobenius | KILL_INTERNAL |
| 12 | DRV | degree-bounded polynomials in characteristic $p$, formal derivative | $D^p=0$; support residue gives height | exact image ranks | classical derivative plus generic nilpotent linear map | KILL_GENERIC |
| 13 | DGR | finite groups, $G\mapsto[G,G]$ on a bounded object closure | dihedral samples die in at most two steps | object-fibre enumeration is unnatural | derived series directly owns the clock | KILL_WEAK |
| 14 | RGC | positive integer matrices, alternate row- and column-gcd normalization | sampled matrices fix after one full pass | no temporal axis | matrix normalization | KILL_WEAK |
| 15 | NVE | graphs, delete edges whose endpoints have equal closed-neighbourhood data | sampled families are idempotent | target fibres unstable | twin/module reduction | KILL_WEAK |
| 16 | CYC | cyclic finite-group words, cyclic forward difference | Fitting tail is the characteristic part of the word length | cycle count from a circulant gcd | literally the normal-basis model of ASD | KILL_CONJUGATE |

## Frozen NHI theorem contract

Let

\[
F_n(x)=3x^2-2x^3\pmod {2^n},
\qquad
e(x)=
\begin{cases}
x,&x\equiv0\pmod2,\\
1-x,&x\equiv1\pmod2.
\end{cases}
\]

The manuscript gate is the following conjunction, with generic Newton
convergence explicitly deducted.

1. **Temporal theorem.** The endpoint is the parity bit of $x$, and
   \[
   v_2(e(F_n^t(x)))=\min\{n,2^t v_2(e(x))\}.
   \]
   Hence the entry time is the least $t$ with
   $2^t v_2(e(x))\ge n$, and
   \[
   \#\{x:\tau(x)\le t\}=2^{\,n-\lceil n/2^t\rceil+1}.
   \]
   This gives every exact shell and sharp height
   $\lceil\log_2 n\rceil$.
2. **Inverse theorem.** Apart from endpoints, even image values have
   valuation $2v<n$. After division by $2^{2v}$, their odd unit is
   $7\pmod8$ for $v=1$ and $3\pmod8$ for $v\ge2$, with the modulus
   truncated when $n-2v<3$. Every such target has
   \[
   2^{\,v+\min(n-2v-1,2)}
   \]
   predecessors; odd targets are the reflections $1-y$. Each endpoint has
   $2^{\lfloor n/2\rfloor}$ predecessors. Consequently
   \[
   |\operatorname{im}F_n|
   =2+2\sum_{1\le v<n/2}2^{\max(0,n-2v-3)}.
   \]

The proof obligation not supplied by standard lifting sources is the
four-to-one odd-unit lemma for
$u\mapsto u^2(3-2^{v+1}u)$ modulo $2^N$, including $N=1,2$ boundary
truncations. The exact verifier checks every state through $n=16$.

## Reserve and kill discipline

CMD may be reconsidered only if other lanes fail to produce five systems,
and only after a proof-engine comparison against P114, P126, and P148. ASD
is mathematically complete but may not be promoted merely because its
formulas are attractive: the internal collision is substantive. The other
thirteen verdicts are terminal for this batch.

## Replay

From the repository root, run

    python docs/papers157_161_sequence/scouting/root/verify_root_scout.py

and byte-compare stdout with CANONICAL.txt.
