# Algebraic / arithmetic / group / linear / finite-ring breadth scout

## Freeze and scope

- Stage: breadth scout only; no manuscript and no paper number is allocated.
- The labels `A01`--`A16` are local scout identifiers, not sequence numbers.
- External state: **HOLD_EXTERNAL**.  No posting, submission, author contact, or priority claim is authorized.
- Exact enumeration is counterexample pressure only.  It is neither an all-parameter proof nor an ownership certificate.
- Historical comparison was made against the P1--P156 roster before ranking.  Three tempting but invalid roster entries were removed before this freeze: `gcd(f(X),f(X+1))` is literally P128; `A -> A^T A` is P102's involutive-norm primitive moved to a matrix star-algebra; and binary shift-difference is the `q=2` specialization of `A01`.  None of those three is counted among the sixteen systems below.

The deterministic control is `verify_algebraic_scout.py`; `CANONICAL.txt` is its frozen stdout.  The current freeze covers 49 parameter boxes and 37,400 exact assertions.

## Triage summary

| ID | finite self-map | strongest exact signal | verdict |
|---|---|---|---|
| A01 | Frobenius difference on a finite field | primary/nilpotent split with exact depth census | `KILL_OWNER_GENERIC_LINEAR` |
| A02 | derivative--GCD on a capped divisor box | residue descent, every depth and every target fibre | `KEEP_RESERVE_OWNER_GATE` |
| A03 | gcd--lcm comparator on divisor pairs | idempotent sorting and Boolean fibre weights | `KILL_SHALLOW` |
| A04 | field norm used as a self-map | one-step descent followed by a scalar power map | `KILL_OWNER_COLLISION` |
| A05 | substitution on a cyclic group algebra | non-coprime image collapse plus periodic multiplier core | `KEEP_PRIMARY_OWNER_GATE` |
| A06 | Cayley--Newton map on principal units | Cayley conjugacy turns the map into squaring | `KILL_DIRECT_OWNER` |
| A07 | cyclic shift-boundary extraction | idempotence and product fibres over target gaps | `KILL_SHALLOW_INTERNAL_MOTIF` |
| A08 | squaring on the symmetric group | cycle-type depth and root enumeration | `KILL_DIRECT_OWNER` |
| A09 | formal derivative on bounded polynomials | characteristic-`p` nilpotence | `KILL_GENERIC_LINEAR` |
| A10 | trace used as a field self-map | `T^2=mT` | `KILL_GENERIC_LINEAR` |
| A11 | `p`th power on principal units | valuation clock | `KILL_CLASSICAL_AND_INTERNAL_COLLISION` |
| A12 | ideal plus annihilator | clipped reflection, then idempotence | `KILL_INTERNAL_COLLISION` |
| A13 | scalar Riccati defect `x-x^2` | exact one-step quadratic fibres, no uniform temporal signal | `KILL_WEAK_SIGNAL` |
| A14 | projective Möbius map `1+1/x` | one PGL element, hence a permutation | `KILL_THIN` |
| A15 | fixed-element Heisenberg commutator | two-step collapse to the identity | `KILL_INTERNAL_COLLISION` |
| A16 | transpose-commutator on `2 x 2` matrices | two-step collapse and an exact quadric fibre law | `KILL_RECOMBINATION_SHALLOW` |

## System cards

### A01 — Frobenius-difference dynamics (`FAD`)

- **Carrier:** `F_{q^m}`, represented in a normal basis over `F_q`, where `q=p^a`.
- **Update rule:** `L(x)=x^q-x`; in normal coordinates, `L=sigma-I` with `sigma` the cyclic coordinate shift.
- **Small exact signature:** `(q,m)=(2,4)` gives 16 states, one fixed/recurrent state, maximum tail 4, cycle histogram `{1:1}`, and indegrees `{0:8,2:8}`.  `(2,6)` instead has 16 recurrent states and cycles `{1:1,3:1,6:2}`.
- **Candidate sharp theorem:** if `s=p^{v_p(m)}`, the generalized zero-primary block has dimension and nilpotency index `s`, while the complementary block is invertible.  Thus the recurrent set has size `q^{m-s}`, maximum depth is `s`, and the number of states of depth at most `t` is `q^{m-s+min(t,s)}`.
- **Independent second axis:** factor `(Z^m-1)/(Z-1)^s` over `F_q` to obtain every periodic-point count and cycle count on the invertible block; all nonempty iterated fibres are uniform by rank-nullity.
- **P1--P156 collision:** heavy machinery collision with P109's nilpotent-linear decomposition and P115's finite-field coefficient dynamics; the literal map is also covered by the established linearized-polynomial literature.
- **Verdict:** `KILL_OWNER_GENERIC_LINEAR`.  The signature is crisp but the residual specialization is too small after owner subtraction.

### A02 — derivative--GCD multiplicity descent (`DGD`)

- **Carrier:** let `G=prod_{i=1}^s P_i` be squarefree and monic over a finite field of characteristic `p`; for `M=p(L+1)-1`, use all monic divisors of `G^M`.
- **Update rule:** `Delta(f)=gcd(f,f')`, with the monic GCD convention and `gcd(f,0)=f`.
- **Small exact signature:** `p=3,L=2,s=3,M=8` gives 729 states, 27 fixed/recurrent states, maximum tail 2, 27 singleton components, and indegrees `{0:513,1:27,2:81,4:81,8:27}`.
- **Candidate sharp theorem:** writing `f=prod P_i^{e_i}`, one has
  `v_{P_i}(Delta^t(f)) = e_i-min(t,e_i mod p)`.
  Consequently recurrence equals fixation, the fixed set consists exactly of exponent vectors divisible by `p`, the maximum depth is `p-1`, and for `u=min(t,p-1)` the depth-`<=t` census is `((u+1)(L+1))^s`.
- **Independent second axis:** for a target exponent `y`, the one-coordinate `t`-step fibre is `u+1` when `y mod p=0`, is 1 when `1 <= y mod p <= p-1-u`, and is 0 otherwise.  Multiplying these local factors gives every target fibre, including all empty fibres.
- **P1--P156 collision:** P128 already owns a different translation--GCD map; P107/P142 own valuation-product reductions; P115 owns a characteristic-`p` coefficient operator.  The literal derivative--GCD descent is not any of those maps, but its algebraic primitive is the classical square-free factorization step and must receive zero credit.
- **Verdict:** `KEEP_RESERVE_OWNER_GATE`.  This is a complete two-axis theorem package with a transparent proof, but direct-algorithm ownership risk is substantial.

### A03 — gcd--lcm divisor comparator (`DCS`)

- **Carrier:** ordered pairs `(d,e)` of positive divisors of `N=prod_i ell_i^{a_i}`.
- **Update rule:** `C(d,e)=(gcd(d,e),lcm(d,e))`; valuation-wise this sorts every pair of coordinates.
- **Small exact signature:** exponent caps `(2,3)` give 144 states, 60 fixed/recurrent states, maximum tail 1, and indegrees `{0:84,1:12,2:30,4:18}`.
- **Candidate sharp theorem:** `C^2=C`; the fixed count is `prod_i binom(a_i+2,2)`.
- **Independent second axis:** a sorted target `(u_i<=v_i)` has fibre size `2^{#{i:u_i<v_i}}`, while every unsorted target is a Garden-of-Eden state.
- **P1--P156 collision:** the valuation-box reduction is already central in P107 and P142, even though this literal comparator is different.
- **Verdict:** `KILL_SHALLOW`.  The full story is one comparator identity and does not support a sufficiently deep temporal axis.

### A04 — norm-power descent (`NPD`)

- **Carrier:** `F_{q^m}` with its canonical embedded subfield `F_q`.
- **Update rule:** `T(x)=N_{F_{q^m}/F_q}(x)` viewed again as an element of `F_{q^m}`.
- **Small exact signature:** `(q,m)=(5,2)` gives 25 states, two fixed/recurrent states, maximum tail 3, and indegrees `{0:20,1:1,6:4}`.
- **Candidate sharp theorem:** `T^t(x)=N(x)^{m^{t-1}}` for `t>=1`; hence `#Fix(T^t)=1+gcd(m^t-1,q-1)`, with least-period counts by Möbius inversion.
- **Independent second axis:** the norm has uniform nonzero fibres of size `(q^m-1)/(q-1)`; composing with the scalar `m^{t-1}` power map gives an exact empty/nonempty `t`-fibre criterion and size.
- **P1--P156 collision:** P102 already makes norm blocks followed by scalar power dynamics a zero-credit core mechanism.
- **Verdict:** `KILL_OWNER_COLLISION`.  After the first step the system is only a classical cyclic-group power map.

### A05 — substitution-collapse endomorphism (`SCE`)

- **Carrier:** the whole cyclic group algebra `R=F_q[X]/(X^m-1)`, including zero divisors.
- **Update rule:** `S_k(f)(X)=f(X^k) mod (X^m-1)`, for `k>=1`; no coprimality between `k` and `m` is assumed.
- **Small exact signature:** `(q,m,k)=(2,12,6)` gives 4,096 states, two fixed/recurrent states, maximum tail 2, two singleton components, and indegrees `{0:4092,1024:4}`.  `(2,10,4)` gives 32 recurrent states with cycles `{1:8,2:12}`.
- **Candidate sharp theorem:** set `g_t=gcd(k^t,m)`, let
  `m_parallel=prod_{ell|k} ell^{v_ell(m)}` and `m_perp=m/m_parallel`.  Then
  `S_k^t(f)=f(X^{k^t})`; its image is exactly the coefficient subspace supported on multiples of `g_t`, every nonempty `t`-fibre has size `q^{m-m/g_t}`, the recurrent core is the subspace supported on multiples of `m_parallel`, and the sharp maximum depth is
  `h=max_{ell|gcd(k,m)} ceil(v_ell(m)/v_ell(k))` (empty maximum 0).  The exact depth-`<=t` census is `q^{m-m/g_t+m_perp}`.
- **Independent second axis:** on the recurrent core, multiplication by `k` permutes the `m_perp` coefficient positions.  For `r>=1`,
  `#Fix(S_k^r)=q^{c_r}` with
  `c_r=sum_{d|m_perp} phi(d)/ord_d(k^r)` (and `ord_1=1`); Möbius inversion gives all least-period points, cycles, and the finite zeta product.
- **P1--P156 collision:** P102 uses the same ambient cyclic group algebra but a nonlinear involutive norm `a -> aa*`; A05 is a coefficient-pushforward algebra endomorphism and is not a carrier change of that map.  Generic finite-linear functional graphs and coprime cyclic-code multipliers must nevertheless be given zero credit.  P115 is an additional linear-collapse machinery collision.
- **Verdict:** `KEEP_PRIMARY_OWNER_GATE`.  The non-coprime collapse, exact all-time fibres/depth CDF, and residual multiplier core form the strongest surviving conjunction.

### A06 — Cayley--Newton principal-unit dynamics (`CNI`)

- **Carrier:** principal units `1+p Z/p^a Z`, for odd `p`.
- **Update rule:** `N(x)=(x+x^{-1})/2 mod p^a`.
- **Small exact signature:** `(p,a)=(3,5)` gives 81 states, only 1 recurrent, maximum tail 3, and indegrees `{0:70,6:9,9:1,18:1}`.
- **Candidate sharp theorem:** the Cayley coordinate `c(x)=(x-1)/(x+1)` satisfies `c(N(x))=c(x)^2`; therefore the depth of `x!=1` is the least `t` with `2^t v_p(c(x))>=a`.
- **Independent second axis:** valuation shells and the squaring map give every image size and every target fibre on the principal-unit domain.
- **P1--P156 collision:** scalar power-map mechanisms recur in P102/P137; more decisively, this is Roberts' classical Newton sign iteration and its standard Cayley-to-squaring conjugacy.
- **Verdict:** `KILL_DIRECT_OWNER`.

### A07 — cyclic shift-boundary extraction (`SBE`)

- **Carrier:** all subsets `S` of the cyclic group `C_m`.
- **Update rule:** `B(S)={i in S : i+1 notin S}` (indices modulo `m`).
- **Small exact signature:** `m=7` gives 128 states, 29 fixed/recurrent states, maximum tail 1, and indegrees `{0:99,2:8,4:7,6:14}`.
- **Candidate sharp theorem:** `B^2=B`; the fixed states are cyclic independent sets and are counted by the Lucas number `L_m`.
- **Independent second axis:** a nonempty target has nonzero fibre exactly when it is independent; if its cyclic successive gaps are `d_1,...,d_r`, its fibre size is `prod_j(d_j-1)`.  The empty target has two preimages, the empty and full sets.
- **P1--P156 collision:** strong motif overlap with cyclic-run papers P117 and P147 and with the extraction/idempotence lane surrounding P155--P156.
- **Verdict:** `KILL_SHALLOW_INTERNAL_MOTIF`.

### A08 — permutation squaring (`PSG`)

- **Carrier:** the symmetric group `S_n`.
- **Update rule:** `Q(sigma)=sigma^2`.
- **Small exact signature:** `n=5` gives 120 states, one fixed state, 45 recurrent states, maximum tail 2, cycles `{1:1,2:10,4:6}`, and indegrees `{0:60,1:24,2:35,26:1}`.
- **Candidate sharp theorem:** if the cycle lengths of `sigma` are `j`, its tail is `max_j v_2(j)`; it is recurrent exactly when every cycle length is odd, and its eventual period is the multiplicative order of 2 modulo the odd part of `ord(sigma)`.
- **Independent second axis:** if a target has `a_j` cycles of length `j`, its number of square roots factors over `j`, pairing equal cycles into `2j`-cycles; this gives the standard exact finite sum over pairings and an EGF for every fibre class.
- **P1--P156 collision:** the carrier also occurs in P105/P155 but the literal rule is different.  The fatal issue is external: enumeration and root formulas for square permutations are directly owned in the classical literature.
- **Verdict:** `KILL_DIRECT_OWNER`.

### A09 — bounded formal-derivative dynamics (`FPD`)

- **Carrier:** `F_q[X]_{<d}` in characteristic `p`.
- **Update rule:** `D(f)=f'`, padded with zero coefficients to stay in the same `d`-dimensional space.
- **Small exact signature:** `(p,d)=(3,6)` gives 729 states, only zero recurrent, maximum tail 3, and indegrees `{0:648,9:81}`.
- **Candidate sharp theorem:** `D^t(X^j)=(j)_t X^{j-t}` and `D^p=0`; the sharp maximum depth is `min(p,d)`.
- **Independent second axis:** count nonzero falling factorials modulo `p` to give the rank of every `D^t`, hence every image and uniform nonempty fibre.
- **P1--P156 collision:** this is a textbook nilpotent linear map, with very heavy overlap with P109/P115's proof machinery.
- **Verdict:** `KILL_GENERIC_LINEAR`.

### A10 — trace self-dynamics (`TSD`)

- **Carrier:** `F_{q^m}` with `F_q` embedded.
- **Update rule:** `T(x)=Tr_{F_{q^m}/F_q}(x)`.
- **Small exact signature:** `(q,m)=(3,3)` gives 27 states, only zero recurrent, maximum tail 2, and indegrees `{0:24,9:3}`; `(3,4)` gives 3 recurrent states and maximum tail 1.
- **Candidate sharp theorem:** `T^2=mT`.  If `p|m`, the map is square-zero; otherwise the recurrent core is the embedded `F_q` and the restriction is multiplication by `m`.
- **Independent second axis:** the trace has rank one over `F_q`, so its nonempty fibres have size `q^{m-1}`; the order of `m` in `F_q^*` gives the complete periodic census.
- **P1--P156 collision:** pure rank-one finite-linear dynamics, beneath the generic machinery already used around P73/P109/P115.
- **Verdict:** `KILL_GENERIC_LINEAR`.

### A11 — principal-unit `p`th power (`PUP`)

- **Carrier:** `1+p Z/p^a Z`, for odd `p`.
- **Update rule:** `P(u)=u^p mod p^a`.
- **Small exact signature:** `(p,a)=(3,5)` gives 81 states, only 1 recurrent, maximum tail 4, and indegrees `{0:54,3:27}`.
- **Candidate sharp theorem:** by LTE, `v_p(u^{p^t}-1)=min(a,v_p(u-1)+t)`; hence the depth is `a-v_p(u-1)` and the exact depth-`d` shell has size `p^d-p^{d-1}` for `d>=1`.
- **Independent second axis:** the principal-unit group is cyclic of order `p^{a-1}`, so every iterated image and every nonempty fibre follow from the kernel sizes of the `p^t` power homomorphism.
- **P1--P156 collision:** this is classical cyclic `p`-group theory and repeats the valuation clocks central to P107/P137/P142.
- **Verdict:** `KILL_CLASSICAL_AND_INTERNAL_COLLISION`.

### A12 — ideal plus annihilator (`ISA`)

- **Carrier:** all ideals of `R=prod_i Z/p_i^{a_i}Z`, encoded by valuation exponents `0<=e_i<=a_i`.
- **Update rule:** `J(I)=I+Ann(I)`, so `e_i -> min(e_i,a_i-e_i)`.
- **Small exact signature:** caps `(3,4)` give 20 states, 6 fixed/recurrent states, maximum tail 1, and indegrees `{0:14,2:2,4:4}`.
- **Candidate sharp theorem:** `J^2=J`; the fixed count is `prod_i(floor(a_i/2)+1)`.
- **Independent second axis:** a fixed target exponent has one preimage on a midpoint coordinate and two otherwise; products give all target fibres.
- **P1--P156 collision:** same ideal/annihilator carrier and clipped-reflection mechanism as P107, with P124/P142 nearby.
- **Verdict:** `KILL_INTERNAL_COLLISION`.

### A13 — scalar Riccati-defect polynomial (`RPD`)

- **Carrier:** `F_p`.
- **Update rule:** `R(x)=x-x^2`.
- **Small exact signature:** `p=5` gives cycles `{1:1,2:1}` and maximum tail 1; `p=7` has only one recurrent point and maximum tail 4; `p=11` gives cycles `{1:1,3:1}`.  The lack of a stable pattern is itself the signal.
- **Candidate sharp theorem:** the only honest all-parameter formulation found in this pass is through the factorization of the dynatomic polynomials `R^r(X)-X` over `F_p`; no closed arithmetic census emerged.
- **Independent second axis:** the one-step indegree of `y` is exactly `1+chi(1-4y)` with `chi(0)=0`, so the first fibre layer is explicit.
- **P1--P156 collision:** adjacent to P125's quadratic finite map and P150's finite-field rational dynamics, though not literally either system.
- **Verdict:** `KILL_WEAK_SIGNAL`.  Variable small-prime graphs without a new uniform invariant are not enough.

### A14 — projective Möbius dynamics (`PMB`)

- **Carrier:** `P^1(F_p)`.
- **Update rule:** `M(x)=1+1/x`, with `M(0)=infinity` and `M(infinity)=1`.
- **Small exact signature:** `p=7` is one 8-cycle; `p=11` has two fixed points and one 10-cycle.  Every indegree is 1.
- **Candidate sharp theorem:** diagonalize the representing matrix `[[1,1],[1,0]]` over `F_{p^2}`; its projective order and whether 5 is a square determine the complete orbit partition.
- **Independent second axis:** the map is a bijection, so all fibres are singleton and the zeta function is the direct product over its PGL cycle lengths.
- **P1--P156 collision:** generic finite-field rational/PGL dynamics, with no transient geometry; P150 already occupies the richer rational-map lane.
- **Verdict:** `KILL_THIN`.

### A15 — Heisenberg fixed-element commutator (`HPC`)

- **Carrier:** `H_p={(a,b,c):a,b,c in F_p}`, the order-`p^3` Heisenberg group.
- **Update rule:** for a fixed noncentral `h`, take `K(g)=[g,h]`; in the chosen coordinates `K(a,b,c)=(0,0,a-b)`.
- **Small exact signature:** `p=5` gives 125 states, only the identity recurrent, maximum tail 2, and indegrees `{0:120,25:5}`.
- **Candidate sharp theorem:** `K^2=e` because the image is central and the second commutator vanishes.
- **Independent second axis:** each central target has exactly `p^2` preimages and every noncentral target has none.
- **P1--P156 collision:** direct Heisenberg/unitriangular/Engel overlap with P70, P111, P119, and P137.
- **Verdict:** `KILL_INTERNAL_COLLISION`.

### A16 — transpose-commutator descent (`TCD`)

- **Carrier:** `M_2(F_p)` for odd `p`.
- **Update rule:** `C(A)=AA^T-A^TA`.
- **Small exact signature:** `p=5` gives 625 states, only zero recurrent, maximum tail 2, and indegrees `{0:600,20:24,145:1}`.
- **Candidate sharp theorem:** `C(A)` is traceless symmetric, hence `C^2(A)=0` for every `A`; zero is the unique recurrent state.
- **Independent second axis:** the image is all matrices `[[a,b],[b,-a]]`.  Every nonzero image target has `p(p-1)` preimages, zero has `p^3+p(p-1)`, and all other targets have none.
- **P1--P156 collision:** this recombines the involutive-norm primitive from P102, transpose from P127, and commutator themes from P119; it is not the forbidden `A^T A` carrier transfer, but the residual is still shallow.
- **Verdict:** `KILL_RECOMBINATION_SHALLOW`.

## Surviving recommendations and theorem contracts

### Recommendation 1: A05 (`SCE`)

Proceed only through a dedicated owner gate.  The proposed theorem contract is exactly:

1. for every prime power `q`, integers `m,k>=1`, and every `t>=0`, prove the iterate, image subspace, empty/nonempty target criterion, uniform nonempty fibre size, and depth-`<=t` census stated in A05;
2. prove the sharp stabilization height `h` and identify the recurrent core as the `m_perp`-dimensional coefficient subspace;
3. independently derive every fixed count `q^{c_r}`, least-period count, cycle count, and zeta factor from multiplier orbits on `Z/m_perp Z`;
4. explicitly subtract generic finite-linear dynamics, cyclic-code multipliers in the coprime case, and P102's group-algebra ambient machinery.

The paper-worthy residual, if ownership survives, is the **non-coprime substitution collapse plus exact target fibres/depth CDF coupled to the residual multiplier core**.  A mere statement that substitution is linear or that coprime multipliers permute coordinates is zero credit.

### Recommendation 2: A02 (`DGD`)

Proceed as a compact reserve only after direct square-free-factorization ownership is resolved.  The proposed theorem contract is exactly:

1. fix `G` squarefree and the complete cap `M=p(L+1)-1`; prove the coordinate iterate `e -> e-min(t,e mod p)` for every `t`;
2. prove the sharp depth `p-1`, all fixed/recurrent states, and every cumulative depth layer;
3. independently prove the complete every-target `t`-step fibre product, including the residue obstruction that makes a fibre empty;
4. treat `s=0`, `L=0`, `t=0`, and `t>=p-1` explicitly and make the independence from the degrees of the `P_i` explicit;
5. give zero contribution credit to `gcd(f,f')` as a square-free-decomposition primitive and make no novelty/priority claim from a bounded non-hit.

The residual is the **exact temporal/fibre package for the bounded divisor self-map**, not the derivative or GCD algorithm itself.

## Gate decision

- **Advance to a focused algebraic Stage 2:** A05 first, A02 second.
- **Do not revive without a new invariant:** A03, A04, A07, A09--A16.
- **Do not revive without overturning a direct owner:** A01, A06, A08.
- The owner searches in `OWNER_SEARCH_LOG.md` are bounded scope checks only.  They do not establish novelty, absence, or priority.
