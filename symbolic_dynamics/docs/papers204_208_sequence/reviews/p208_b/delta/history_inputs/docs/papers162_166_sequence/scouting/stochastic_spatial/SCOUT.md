# Stochastic/spatial breadth scout — P162–P166 intake

**Date:** 2026-09-02 UTC  
**Route:** breadth-first, random/spatial/Markov lane  
**External status:** `HOLD_EXTERNAL`  
**Paper assignment:** none

## Outcome first

This lane tested **16 genuinely different literal systems**.  Every system was
executed in exact integer or rational arithmetic.  The verifier made
**1,180,122 assertions** and froze a canonical transcript.

The result is an **empty paper-sized pool**.  This is intentional, not a failed
quota:

- `DCI` first looked strongest: its odd-dihedral centralizer-intersection chain
  has a four-type all-time law, exact target fibres, a closed absorption tail,
  and one-depth parameter recovery.  However, its survival event is exactly
  the event that the sampled tuple commutes pairwise.  The 2026 higher-
  commutativity paper directly owns the finite-spectrum temporal and inverse
  engine.  The remaining four target counts are a one-line partition of that
  owned count.  **Kill.**
- `LSC` has a clean spatial realization and unusually neat formulas: a product
  PGF, mean `1+d H_m`, a two-level Green kernel, and dimension recovery.  But
  its radius chain is exactly the lower weak-record-value chain for the finite
  shell distribution.  Exact finite-support weak-record distributions are
  directly owned.  The lattice-simplex shell count only chooses the parent
  distribution.  **Kill.**
- The other fourteen candidates hit a direct primary owner, an exact P1–P161
  specialization/conjugacy, or a permanent rank/group-walk/linear-operator/
  classical-process exclusion.  None is promoted by lowering the value floor.

No bounded search non-hit is interpreted as novelty, priority, or ownership.

## Historical collision firewall

Before selecting candidates, this scout read the paper-directory inventory for
P1–P161, the Stage-2 theorem maps through P161, and the recent stochastic and
replacement ledgers for P127–P161.  The following are hard exclusions here:

- generic coupon collection, birthday/refinement, sample minimum/maximum/range,
  random deletion, quota exposure, linear-extension/hook scheduling;
- standard Glauber/heat-bath, voter, exclusion, annihilation, random greedy,
  RSA, matching, coalescing-walk, urn-first-passage, and ordinary gambler's-
  ruin wrappers;
- graph/forest/ear peeling, bootstrap/core closure, local complementation,
  triangulation/tiling flips, generic matroid-basis moves;
- generic finite-group walks, independent-coordinate contractions, random
  finite-field rank, and fixed-slot reversible chains unless a map-specific
  second theorem survives subtraction.

None of the sixteen rows below is a parameter change of one of those forbidden
models.  Some rows nevertheless *reduce* to a forbidden proof engine; those are
recorded as exact negative controls and killed.

## Exact executable contract

[`verify_scout.py`](verify_scout.py) is self-contained.  It imports no author or
earlier-scout code and uses no seed, random sampling, floating point,
third-party package, timestamp, or network access.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_scout.py > /tmp/p162_stochastic_spatial.out
cmp -s CANONICAL.txt /tmp/p162_stochastic_spatial.out
```

[`CANONICAL.txt`](CANONICAL.txt) is the frozen stdout.  Enumeration supplies
counterexample pressure only; the deductions below, not the finite sweeps, are
the all-parameter arguments.

## Sixteen-system theorem ledger

| ID | literal carrier and update | exact small signature | all-parameter distribution/clock theorem | independent second axis | owner/internal collision | decision |
|---|---|---|---|---|---|---|
| `DCI` | In `D_(2n)`, odd `n`, start at `G`; sample iid uniform `g_t` and replace the state by its intersection with `C_G(g_t)`. | `n=5,t=3`: fibres `(G,A,each reflection C_j,Z)=(1,124,7,840)` among 1,000 histories. | `P(T>t)=[n^t+n(2^t-1)]/(2n)^t`, with `T` the first time the meet is the centre. | Every one of the `n+3` targets has an exact fibre; `n=3/(4P(T>2)-1)`. | Higher commuting probabilities own the survival spectrum and its inverse; P135/P154 occupy centralizer/dihedral structure. | **`KILL_DIRECT_TEMPORAL_OWNER`** |
| `LSC` | In the lattice simplex `Delta_m^d={u>=0:sum u_i<=m}`, sample a uniform point and replace the radius by its shell `sum u_i`; stop at radius zero. | `d=2,m=3`: mean `14/3`, PGF at `z=1/2` is `1/8`, Green occupation of shell 1 from above is `2`. | `E[z^T]=z product_(j=1)^m j/(j+d(1-z))`; hence `E T=1+dH_m`. | `G(m,k)=(k+d)/k` if `m=k`, `d/k` if `m>k`; known `m` and the mean recover `d`. | Exactly a lower weak-record chain for shell weights; exact finite-support weak-record laws are owned. | **`KILL_DIRECT_RECORD_ENGINE`** |
| `QHI` | Start with `F_q^d`; intersect with the kernel of an iid uniform nonzero covector each epoch. | `q=2,d=t=3`: codimension counts `(0,7,168,168)`. | Codimension `r` has count `[d choose r]_q S_q(t,r)`, where `S_q` counts spanning nonzero `t`-tuples by subspace Möbius inversion; full absorption is the `r=d` term. | Every fixed codimension-`r` target has exactly `S_q(t,r)` histories. | Finite-field random-rank law and P109's nilpotent subspace fibre machinery. | **`KILL_RANK_ENGINE`** |
| `HCI` | In the order-`p^3` Heisenberg group, repeatedly intersect centralizers of iid uniform elements. | `p=3,t=3`: `(whole,maximal-abelian,centre)=(1,104,624)` after projection. | Centralizer codimension is the rank of `t` iid vectors of `F_p^2`; the complete law is the ordinary random-matrix rank law. | Each maximal abelian target line has `p^t-1` projected histories; centre/whole fibres follow. | Exact transfer to random rank plus P109/P111/P135. | **`KILL_EXACT_RANK_TRANSFER`** |
| `ORW` | In a nonright orthocentric quartet over `F_p`, choose one of the current triangle's three vertices uniformly and replace it by the orthocenter. | At `p=7`, quartet `((0,0),(1,0),(2,1),(2,5))`; after four steps counts are `(21,20,20,20)`. | On the missing-vertex coordinate this is the loopless `K_4` walk: return mass `1/4+3(-1/3)^t/4`, each other mass `1/4-(-1/3)^t/4`. | The four target triangles reconstruct the same quartet, but all fibres are degree-three walk fibres. | Exact stochastic wrapper of P161's owned orthocentric four-window. | **`KILL_INTERNAL_P161`** |
| `KMP` | Feed iid uniform letters into the longest-prefix/suffix automaton of a fixed word and stop on the full match. | Binary pattern `010`: mean `10`; first-hit counts at lengths 1–7 are `(0,0,1,2,3,5,9)`. | For every word, `P(T=t)=e_0 Q^(t-1)r`; `E T=sum_(ell in borders) q^ell`. | Complete prefix-state-resolved pre-hit law and autocorrelation/border recovery. | Guibas–Odlyzko own correlation-polynomial pattern avoidance; P92/P134 occupy recurrence/border data. | **`KILL_DIRECT_PATTERN_OWNER`** |
| `GSW` | On a labelled graph, choose a vertex uniformly and toggle its entire incident star. | `n=5,t=4`: 65 histories return to the starting switching class. | For cut `delta(S)`, the history count is `N_t(S)+N_t(S^c)` with `N_t(S)=2^-n sum_Y (-1)^(|S cap Y|)(n-2|Y|)^t`. | Components are graph cosets modulo cut space; size `2^(n-1)`, period 2 for even `n`, aperiodic for odd `n`. | Bit-for-bit vertex-push/cut-space dynamics of P145. | **`KILL_EXACT_INTERNAL_CONJUGACY`** |
| `TTW` | On a labelled graph, choose a vertex triple uniformly and toggle its three boundary edges. | `n=5,t=4`: 400 histories return to zero. | In each degree-parity coset, Fourier inversion gives `P^t(0,H)=|C|^-1 sum_[F] (-1)^(F dot H)(1-2o(F)/C(n,3))^t`. | Triangle boundaries span the `K_n` cycle space; there are `2^(n-1)` components and the walk has period 2. | Generic finite-abelian Fourier and P67/P127 cycle/parity carriers leave no map-specific residual. | **`KILL_GENERIC_GROUP_WALK`** |
| `PTW` | On a binary edge field of an `r x c` square torus, toggle the boundary of a uniform plaquette. | `3x3,t=4`: 225 histories return to zero. | The `rc` face generators have their sole relation `sum faces=0`; endpoint counts equal parity-vector walk counts modulo complement. | Boundary image size is `2^(rc-1)`; there are `2^(rc+1)` syndrome/homology cosets in the full edge space. | Exact conjugacy to the folded parity walk plus P67's plaquette-matroid carrier. | **`KILL_EXACT_GROUP_CONJUGACY`** |
| `CDP` | For a binary cyclic word of length `n=2^a`, choose `I+S` or `I+S^-1` fairly at each epoch. | `n=8,x=e_0,t=3`: four shifted targets have history multiplicities `(1,1,3,3)`. | If `K_t` backward choices occurred, `X_t=S^(-K_t)(I+S)^tX_0`; absorption depth is the deterministic nilpotence depth. | `dim ker(I+S)^t=t`; the image has `2^(n-t)` points and every target has `2^t` sources. | Random phase adds no theorem beyond occupied linear-CA/module results P63/P86/P98/P115. | **`KILL_INTERNAL_LINEAR_OPERATOR`** |
| `UDC` | Replace an integer by a uniform divisor of its current value; iterate to 1. | Exponent profile `(2,3)`, time 3: absorption CDF `35275/62208`. | Prime-exponent coordinates are independent uniform-descending chains; the full clock CDF is the product of coordinate absorption CDFs and the total clock is their maximum. | Every-time/every-target transition law factorizes over prime exponents. | Exact product transfer from the prior RCR contraction plus P142's valuation/divisor lane. | **`KILL_INTERNAL_PRODUCT_TRANSFER`** |
| `SBW` | From a coprime positive pair `(a,b)`, choose `(a,a+b)` or `(a+b,b)` fairly. | Depth 6 has 64 distinct states; sum range `[8,34]`. | Every length-`t` word has probability `2^-t` and a distinct state; subtraction gives the unique inverse word and hence the exact depth. | Minimum coordinate sum is `t+2`; maximum is `F_(t+3)`, attained by alternating growth. | Calkin–Wilf directly own the tree; P131 owns the continued-fraction/subtractive decoder interface. | **`KILL_DIRECT_TREE_OWNER`** |
| `BSR` | On `Z/2^hZ`, apply `x -> 2x+B_t` with iid fair bits. | `h=5,t=5`: all 32 targets occur once from every source. | For `t<h`, the `2^t` targets are `2^t x+r`; for `t>=h`, every target has `2^(t-h)` histories. | Common-noise coupling erases every source difference sharply at time `h`. | De Bruijn/shift-register fact plus P93/P101 synchronization and inverse-window engines. | **`KILL_INTERNAL_SHIFT_REGISTER`** |
| `ECR` | Chinese-restaurant cycle growth with mutation weight `theta`: create a singleton with weight `theta`, otherwise insert after a current label. | `theta=2,n=5`: cycle-count law `(1/15,5/18,7/18,2/9,2/45)`. | `P(K_n=k)=c(n,k)theta^k/(theta)^(overline n)` for unsigned Stirling `c(n,k)`. | Every cycle shape `lambda` has Ewens mass `n! theta^ell(lambda)/((theta)^(overline n)z_lambda)`; two extreme shapes recover `theta`. | Ewens sampling formula directly owns both axes; P135/P155 occupy cycle-shape transforms. | **`KILL_DIRECT_EWENS`** |
| `PLU` | Classical two-colour Pólya reinforcement: draw a ball and add one of the drawn colour. | `(alpha,beta,t)=(2,3,4)`: red-addition law `(3/14,2/7,9/35,6/35,1/14)`. | The count is beta-binomial: `C(t,k)(alpha)_k(beta)_(t-k)/(alpha+beta)_t`. | Every colour word with the same count has identical probability; first-step and total mass recover the initial ratio. | Pólya/Blackwell–MacQueen directly own exchangeability and the urn law. | **`KILL_DIRECT_URN_OWNER`** |
| `BGW` | Critical branching frontier: every particle independently has 0 or 2 children with probability 1/2. | `P(Z_4=0)=24305/32768`. | `E[s^(Z_t)]=f^t(s)` for `f(s)=(1+s^2)/2`; this is the exact all-generation law. | `P(total progeny=2k+1)=Catalan_k/2^(2k+1)`. | Literal Galton–Watson process; both iterate-PGF and total-progeny tree are classical owners. | **`KILL_DIRECT_BRANCHING_OWNER`** |

## Two strongest false starts

### DCI: complete theorem, direct temporal owner

Write `D_(2n)=<r,s | r^n=s^2=1, srs=r^-1>` with odd `n>=3`.
Its centre is `{1}`.  A nonidentity rotation has centralizer `A=<r>`, and
the centralizer of `sr^j` is `{1,sr^j}`.  Thus after `t` samples the common
centralizer is exactly one of

```text
G                       1 history
A                       n^t-1 histories
{1,sr^j}                2^t-1 histories for each j
{1}                     (2n)^t-n^t-n(2^t-1) histories.
```

This proves the target fibres and the absorption tail.  It also exposes the
fatal owner identity: `T>t` iff all `t` sampled elements commute pairwise.
Consequently the principal clock is the odd-dihedral specialization of the
higher-commuting hierarchy, and its two exponential bases are part of the
owned finite spectrum.  A four-row centralizer refinement is not sufficient
residual mass for a paper.

### LSC: complete spatial formula, exact record reduction

The number of points in shell `k` of `Delta_m^d` is
`w_k=C(k+d-1,d-1)` and `W_m=sum_(k<=m)w_k=C(m+d,d)`.  Hence

```text
P(m -> k)=w_k/W_m,               0<=k<=m,
w_m/W_m=d/(m+d).
```

First-step subtraction gives

```text
E_m[z^T] = z product_(j=1)^m j/(j+d(1-z)).
```

The probability of ever hitting `k` from above is `w_k/W_k=d/(k+d)`;
the mean dwell at `k` is `(k+d)/k`.  Multiplying gives the Green values in
the ledger.  All identities are correct and sharp.

Nevertheless, fix any parent distribution with masses proportional to
`w_0,...,w_m`.  Successive lower weak record values have exactly the kernel
`w_k/W_current`, including equality holds.  The simplex is therefore a visual
realization of an owned record-value chain, not a new dynamical mechanism.

## Breadth disposition

The sixteen updates cover group-centralizer meets, spatial shell contraction,
finite-geometry sections, nilpotent group centralizers, metric geometry,
pattern automata, cut and cycle-space walks, lattice gauge plaquettes, random
linear cellular operators, arithmetic divisor contraction, rational trees,
shift registers, exchangeable cycle growth, reinforcement, and branching.

The pool remains empty after owner and collision subtraction:

```text
systems tested                 16
paper-sized owner-thin kept     0
direct/exact-owner kills         8
exact P1--P161/conjugacy kills   8
external status                 HOLD_EXTERNAL
```

No candidate receives a paper number.  Re-entry requires a different literal
update and a second theorem that survives the controlling owner; changing a
parameter, scheduler, carrier name, or geometric drawing is insufficient.

