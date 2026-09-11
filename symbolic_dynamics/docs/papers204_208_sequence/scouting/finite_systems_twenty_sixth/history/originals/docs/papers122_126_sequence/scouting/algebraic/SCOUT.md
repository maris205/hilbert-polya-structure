# Algebraic dynamics intake for the P122--P126 sequence

> **Post-scout correction:** the later independent gate killed C1.  Its depth
> layers below confused image and kernel, and the identical map was already
> B2B-08 in the P117--P121 scout.  See
> `phase1/HOSTILE_GATE_ARITH_MATRIX.md`.  The scouting record is retained as
> an audit trail and must not be read as the final gate.

Date of bounded owner search: 2026-08-30 (UTC).

Status: **SCOUT ONLY — EXTERNAL HOLD.** The labels C1--C20 below are intake labels, not paper numbers. No candidate has been assigned to P122--P126 and no novelty claim is made.

## Outcome

This pass defined 20 literal finite dynamical systems across matrix algebras, subspace and ideal lattices, finite groups, and truncated/path algebras. Twelve were implemented in an exact deterministic standard-library pilot. The run made **3,673,684 assertions** and passed. Strict subtraction leaves three candidates with an early theorem-shaped signal (C1, C3, C6), two reserves whose first invariant is real but whose temporal theorem is not yet closed (C8, C12), and fifteen killed or parked controls.

The present recommendation is therefore not “five papers.” It is:

- advance C1, C3, and C6 to proof dossiers and a second, map-specific owner search;
- retain C8 and C12 only as reserves;
- do not promote any other item from this intake;
- keep every item on external HOLD until a direct-owner audit and theorem proof are complete.

### Triage: scope, proof risk, and order

| Candidate | Is the present signal enough for one paper? | Proof-completion risk | Recommended role |
|---|---|---|---|
| C1 | **Not yet confidently.** The complete (2\times2) functional graph would make a crisp short note, but the state family is small and (T^2=0) makes the temporal side shallow. Treat it as standalone only if the direct-owner audit stays clean and either a higher-rank/involutive-algebra extension or a comparably strong family theorem is added. | **Low** for the displayed (2\times2) image/fibre theorem; **medium-high** for an extension with real scope. | Close first as a fast theorem/no-go test; otherwise fold it into a broader involution-defect paper rather than force a slot. |
| C3 | **Potentially yes**, once the exact-iterate/depth theorem is supplemented by fixed/2-cycle or depth-layer enumeration over general (q,d). | **Low** for closed iterates and eventual period; **medium-high** for sharp witnesses and useful (q)-enumeration. | Highest conceptual priority and best current mechanism-level candidate. |
| C6 | **Potentially yes**, if the 49-box census is proved uniformly and the diagonal depth drop is explained. | **Medium-high**: the staircase update is elementary, but classifying every recurrent state and proving the sharp diagonal exception may be delicate. Owner risk from toggles/rowmotion is also high. | Highest exact-census upside, but run after an early symbolic staircase derivation/owner kill test. |

Accordingly, the recommended **work order** is C1 (cheap closure/scope test), C3 (main proof effort), then C6 (high-upside but higher kill risk). The recommended **publication-potential order on present evidence** is C3, C6, C1; C8 and C12 remain distant reserves.

## Historical firewall and zero-credit rules

The candidate definitions were checked against the P1--P121 paper directories and the preceding algebraic scout. The following receive zero credit here even when they supply useful controls:

- ordinary finite linear functional graphs or affine recurrences;
- coordinatewise power maps and disguised power maps;
- standard Lang, Engel, Cartier, Frobenius-root, or Hasse-derivative dynamics;
- closure-operator idempotence by itself;
- generic radical/valuation filtration descent by itself;
- the already occupied Boolean zeta, forward-difference, regular-nilpotent commutator, coupled-Cartier, semilinear-Fibonacci, non-PIR shear-ideal, modular Young, McKay-support, tensor-sumset, sumset-squaring, valuation-erasure, group-algebra norm, double-adjugate, annihilator-power, nilpotent-image, shift-join, fixed-Engel, and related mechanisms.

In particular, C2, C4, C7, and C13 are deliberately coded subtraction controls rather than attempts to inflate the surviving count.

## Candidate ledger

Here (q) is a prime power, (N) is a fixed regular nilpotent endomorphism, (C_{ij}) replaces coordinates (i,j) by their meet and join, and every displayed state space is finite.

| ID | Literal system | Earliest exact signal | Subtraction / decision |
|---|---|---|---|
| C1 | On (M_2(\mathbb F_q)), (T(A)=AA^{\mathsf T}-A^{\mathsf T}A). | (T^2=0); exact characteristic-dependent image, fibre, and depth formulas. | **PROMOTE TO PROOF DOSSIER.** No exact-map owner found in the bounded search; ordinary commutator and bilinear-form work is zero-credit background. |
| C2 | On (M_2(\mathbb F_q)), (T_+(A)=AA^{\mathsf T}+A^{\mathsf T}A). | In characteristic two it is literally C1; in odd characteristic the symmetric image evolves by (B\mapsto2B^2). | **KILL:** C1 collision in characteristic two and a disguised power map otherwise. |
| C3 | On (\operatorname{Sub}(\mathbb F_q^d)^2), (T(U,V)=(V,U+N(V))). | Closed semiring-Fibonacci iterates, eventual periods only 1 or 2, and pilot-sharp maximum transient (d). | **PROMOTE TO PROOF DOSSIER.** Static nilpotent-subspace literature is substantial, but the exact recurrence was not found. |
| C4 | On the same lattice, (T^\vee(U,V)=(V,U\cap N^{-1}V)). | Same period ceiling and pilot-sharp depth as C3. | **KILL:** order-dual control of C3, not a separate paper mechanism. |
| C5 | On (\operatorname{Sub}(\mathbb F_q^d)^3), iterate the comparator word (C_{12}C_{23}), with (C_{12}C_{23}C_{12}) as the full-sort control. | Over (\mathbb F_2), the first word settles after a second pass and the full word is idempotent. | **KILL:** direct lattice-sorting ownership and bounded closure behaviour. |
| C6 | For monomial ideals (I\triangleleft R_{a,b}=k[x,y]/(x^a,y^b)), (T(I)=x(I:y)+y(I:x)). | For (2\le a,b\le8): only periods 1,2; with (m=\min(a,b)), exactly (m) fixed ideals, (2(m-1)) states on 2-cycles, (3m-2) recurrent states, and sharp maximum depth (m) off the diagonal and (\max(1,m-2)) on (a=b=m). | **PROMOTE TO PROOF DOSSIER.** Exact operator not found; colon-ideal and monomial-staircase theory must be fully subtracted. |
| C7 | On the same ideal lattice, (S(I)=(xI:y)+(yI:x)). | Only periods 1,2 in all coded boxes; depth shadows C6 except on some square boxes. | **KILL:** within-batch cross-colon sibling with weaker structure and no independent theorem route. |
| C8 | Vieta fold on (\mathbb F_q^2): (T(a,b)=(a+b,ab)). | For odd (q), image size (q(q+1)/2), (q) singleton fibres and (q(q-1)/2) double fibres; exactly (q) fixed states. | **RESERVE.** First-step quotient is elementary-symmetric/S2 ownership; observed periods and depths do not yet have a clean parameter law. |
| C9 | Cubic Vieta fold on (\mathbb F_q^3): (T(a,b,c)=(a+b+c,ab+ac+bc,abc)). | Static fibres are controlled by root multiplicity and the (S_3)-stabilizer, with characteristic 2 and 3 ramification. | **KILL/PARK:** the signal is a standard symmetric quotient, not a temporal theorem. |
| C10 | On (H_p^2), for the finite Heisenberg group (H_p), (T(x,y)=(y,xy)). | Exact pilot cycle censuses: (p=2:{1:1,3:9,6:6}), (p=3:{1:1,8:91}), (p=5:{1:1,4:31,20:775}), (p=7:{1:1,16:7353}). | **KILL:** classical Nielsen transformation plus severe internal collision with the earlier Heisenberg word/area lane. |
| C11 | Hurwitz map on (G^2), tested on (H_p^2): (T(x,y)=(y,y^{-1}xy)). | (xy) is invariant, (T^2) is simultaneous conjugation by (xy), and cycles in (H_p^2) divide (2p). | **KILL:** this is the standard two-strand Hurwitz action. |
| C12 | On (M_2(\mathbb F_q)^2), (T(A,B)=(AB,BA)). | Both component ranks decrease; exhaustive maxima are depth/cycle (3/2) for (q=2) and (5/4) for (q=3). | **RESERVE.** Genuine noncommutative coupling, but no general depth/cycle theorem and high AB/BA-owner density. |
| C13 | On the strictly upper-triangular radical (J_n(\mathbb F_q)), (T(A)=ANA), with (N) the regular shift. | Radical degree obeys (r\mapsto2r+1), giving logarithmic nilpotence depth; the (q=2,n\le6) bound is sharp. | **KILL:** disguised power/sandwich filtration, too close to occupied radical and power mechanisms. |
| C14 | For fixed nonsingular symmetric (J), on (M_n(\mathbb F_q)), (T(A)=A^{\mathsf T}JA-J). | Characteristic-two alternating/symmetric boundary and congruence-class fibres. | **PARK:** quadratic-form congruence dominates; no independent temporal law. |
| C15 | On (\mathrm{GL}_n(\mathbb F_q)), the cosquare map (T(A)=A^{-\mathsf T}A). | Image constrained by bilinear-form/cosquare invariants. | **KILL:** established cosquare/congruence mechanism; owner-heavy before dynamics begin. |
| C16 | On ideal pairs of a finite ring, (T(I,J)=(I\cap J,I+J)). | One-step comparator/idempotence and lattice fibres. | **KILL:** direct lattice sorting/closure, no new temporal mechanism. |
| C17 | On subsets (or generated subalgebras) of (M_n(\mathbb F_q)), (T(S)=C(C(S))), where (C) is the centralizer. | Extensive and idempotent double-centralizer closure. | **KILL:** standard Galois closure/double-centralizer theorem. |
| C18 | In the radical of the line-quiver path algebra, for a fixed arrow sum (\delta), (T(a)=a\delta a). | Minimum path length follows the same doubling-plus-one law as C13. | **KILL:** exact mechanism collision with C13 and occupied filtration lanes. |
| C19 | On (M_2(\mathbb F_q)^2), (T(A,B)=(AB-BA,AB+BA)). | The two outputs collapse together in characteristic two; odd characteristic permits recovery of (AB,BA). | **PARK:** a sharp characteristic threshold exists, but it is presently only a coordinate change of product data, not a closed dynamical theorem. |
| C20 | On pairs of normal subgroups of a finite (p)-group, (T(H,K)=([H,K],HK)), with ([H,K]) the subgroup generated by commutators. | Lower-central descent in the first coordinate coupled to join growth in the second. | **KILL:** standard commutator-series/subgroup-lattice machinery; insufficient independent signal. |

## Mechanical evidence

The sole pilot is [`algebraic_pilots.py`](algebraic_pilots.py). It uses only the Python standard library, exact finite arithmetic, deterministic enumeration, and raises on the first failed invariant. Its canonical stdout is [`CANONICAL_OUTPUT.txt`](CANONICAL_OUTPUT.txt).

Run:

```bash
python3 docs/papers122_126_sequence/scouting/algebraic/algebraic_pilots.py
```

Coverage:

- C1: all matrices in (M_2(\mathbb F_q)) for prime (q=2,3,5,7), including every fibre and every second iterate;
- C2: all matrices for (q=2,3,5);
- C3: every ordered pair of subspaces of (\mathbb F_2^d), (1\le d\le5), checking each closed iterate through (2d+3) and the full orbit;
- C4: every subspace pair for (1\le d\le4);
- C5: every subspace triple for (1\le d\le4);
- C6 and C7: every monomial ideal in all 49 boxes (2\le a,b\le8);
- C8: every point of (\mathbb F_q^2) for eight primes through 19;
- C10: every pair in (H_p^2) for (p=2,3,5,7), including an explicit inverse and complete cycle census;
- C11: every pair in (H_p^2) for (p=2,3,5);
- C12: all pairs of (2\times2) matrices for (q=2,3);
- C13: every strictly upper-triangular binary matrix for (2\le n\le6).

The pilot is falsification evidence, not a proof. In particular, its arithmetic helper treats the tested (q)'s as prime fields; prime-power extensions must be handled symbolically or with an explicitly audited field implementation in any later dossier.

## The strongest signals and proof routes

### 1. C1 — transpose self-commutator

Write

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
u=b-c,\quad v=b+c,\quad w=a-d.
\]

Then

\[
T(A)=\begin{pmatrix}uv&-uw\\-uw&-uv\end{pmatrix}.
\]

Every image is symmetric, so (T^2=0). In odd characteristic the change to (u,v,w,a+d) is invertible and gives:

\[
|\operatorname{im}T|=q^2,\quad
|T^{-1}(0)|=q^3+q^2-q,\quad
|T^{-1}(B)|=q(q-1)\quad(B\ne0).
\]

Thus the exact depth counts are (1,q^2-1,q^4-q^2) at depths (0,1,2). In characteristic two the parametrization degenerates to the Frobenius-constrained plane (\bigl(\begin{smallmatrix}u^2&uw\\uw&u^2\end{smallmatrix}\bigr)), predicting image size (q^2-q+1), zero fibre (q^3), and nonzero fibres (q^2). The proof dossier should establish this over every finite field (not only the prime fields in the pilot), state the characteristic boundary cleanly, and then decide whether the (2\times2) theorem alone has enough scope or admits a controlled higher-rank extension.

Owner risk: **medium-high**. Matrix self-commutators, transpose involutions, and quadratic-form fibres are mature topics. The bounded exact-string search found no source stating this finite dynamical map or these fibres, which is only `BOUNDED_NO_DIRECT_HIT`, never a novelty certificate.

### 2. C3 — nilpotent subspace Fibonacci dynamics

If (X_0=U,X_1=V), then (X_{t+2}=X_t+NX_{t+1}), and induction in the idempotent semiring of subspaces gives

\[
X_{2r}=\sum_{j=0}^{r-1}N^{2j}U+\sum_{j=0}^{r-1}N^{2j+1}V,
\]

\[
X_{2r+1}=\sum_{j=0}^{r-1}N^{2j+1}U+\sum_{j=0}^{r}N^{2j}V.
\]

For a regular nilpotent (N^d=0), these formulas force eventual period dividing two. The exhaustive binary pilot shows the universal bound (d) is sharp for every (d=2,3,4,5). The next proof task is to give an explicit sharp witness for all (q,d), characterize fixed points and 2-cycles through the even/odd Krylov sums, and derive at least one exact layer enumerator (likely by flags relative to the regular nilpotent chain). A mere depth bound is not enough for promotion.

Owner risk: **medium**. Nilpotent invariant/characteristic subspace lattices, Krylov spaces, and splitting subspaces are established. The exact two-register join recurrence was not found in the bounded search, but any enumeration must subtract that static machinery explicitly.

### 3. C6 — cross-colon dynamics on rectangular monomial ideals

Encode a monomial ideal of (R_{a,b}) by the monotone staircase of thresholds in its (a\times b) exponent rectangle. Colon by (x) or (y), multiplication by the opposite variable, and ideal sum become local shifts and coordinatewise minima of that staircase. This should turn C6 into a deterministic boundary update. The proof target suggested by all 49 exhaustive boxes is:

\[
\#\operatorname{Fix}(T)=m,\quad
\#\{\text{states on 2-cycles}\}=2(m-1),\quad
\#\operatorname{Rec}(T)=3m-2,
\]

with no longer cycles and maximum transient

\[
D(a,b)=\begin{cases}
m,&a\ne b,\\
\max(1,m-2),&a=b=m.
\end{cases}
\]

The proof dossier must derive the exact staircase update, identify all recurrent staircases, construct sharp-depth witnesses, and prove the diagonal cancellation responsible for the (m-2) exception. It should also explain why C7 is not an independent theorem.

Owner risk: **high**. Colon identities and staircase encodings of monomial ideals are standard, and the map could be a disguised toggle/rowmotion-style boundary action. No exact occurrence of (I\mapsto x(I:y)+y(I:x)) was found in the bounded search; this remains `BOUNDED_NO_DIRECT_HIT` pending a dedicated commutative-algebra/combinatorics audit.

### 4. C12 — product-exchange reserve

The rank Lyapunov function is exact, and noncommutativity permits nontrivial recurrent strata after rank stabilizes. However, the two small fields give different maximum cycles and no parameter law. A useful next step would need to classify the stabilized full-rank lane up to simultaneous conjugacy and prove a rank-deficient transient bound. Until then this is a computational anomaly, not a paper route.

Owner risk: **high** because AB/BA spectral, similarity, semigroup, and word-map literatures are dense.

### 5. C8 — Vieta-fold reserve

The first-step fibre theorem is exact: it is the unordered-root quotient, with the discriminant-zero locus giving singleton fibres. But iteration feeds coefficients back as roots; the measured maximum cycles (1,1,4,1,6,4,10,8) for (q=2,3,5,7,11,13,17,19) do not yet expose a theorem. Promotion requires a semiconjugacy or invariant that explains both cycles and transient depths. Fibre counting alone is fully owner-subtracted and earns no paper slot.

Owner risk: **high** because the symmetrization map is classical and finite-field polynomial dynamics is broad.

## Bounded direct-owner audit

Only primary papers or official publisher records were retained. Exact formula searches were run for C1, C3, C6, C8, C10/C11, C12, and C13, plus mechanism searches for their nearest neighbors. A search miss means only that no direct owner was found in this bounded pass.

| Candidate | Direct owner result | Nearest primary mechanism and subtraction |
|---|---|---|
| C1 | `BOUNDED_NO_DIRECT_HIT` for the exact iterate (A\mapsto AA^{\mathsf T}-A^{\mathsf T}A) and its finite-field fibres. | Ordinary matrix commutators, self-commutators, and transpose/bilinear-form theory remain zero-credit background; a specialist audit is still required. |
| C3/C4 | `BOUNDED_NO_DIRECT_HIT` for ((U,V)\mapsto(V,U+NV)). | [Astuti and Wimmer, *The characteristic subspace lattice of a linear transformation*](https://doi.org/10.1016/j.laa.2016.06.003) studies the static nilpotent characteristic/hyperinvariant lattice; [Aggarwal and Ram, *Splitting subspaces of linear operators over finite fields*](https://doi.org/10.1016/j.ffa.2021.101982) enumerates static splitting/Krylov subspaces, including cyclic nilpotent operators. Neither source, as inspected, states C3's recurrence. |
| C5/C16 | **DIRECT MECHANISM OWNER.** | [Gerlach, *Sorting in Lattices*](https://arxiv.org/abs/1303.5560) defines sorting using meet and join. This is enough to kill the comparator lane regardless of the small-depth computation. |
| C6/C7 | `BOUNDED_NO_DIRECT_HIT` for either exact cross-colon self-map. | [Dao and De Stefani, *On Monomial Golod Ideals*](https://doi.org/10.1007/s40306-020-00390-2) uses products of colon ideals and monomial structure, while [Colón-Reyes et al., *Monomial Dynamical Systems over Finite Fields*](https://arxiv.org/abs/math/0605439) concerns monomial coordinate maps. Both are mechanism-adjacent, neither is ownership of this ideal-lattice iteration. |
| C8/C9 | `BOUNDED_NO_DIRECT_HIT` for iteration of the Vieta coefficient tuple. | [Bergelson and Moreira, *Ergodic Theorem involving additive and multiplicative groups of a field and \(\{x+y,xy\}\) patterns*](https://arxiv.org/abs/1307.6242) owns an additive/multiplicative pattern, not this iteration. Elementary-symmetric quotient fibres are classical and fully subtracted. |
| C10 | No exact finite-Heisenberg census found. | The map is an elementary Nielsen transformation on a pair, and the earlier internal Heisenberg word/area lane is too close. This structural collision kills it without relying on a search miss. |
| C11 | **DIRECT MECHANISM OWNER.** | The formula is the standard braid/Hurwitz generator; the inspected primary owner record is [Baumeister et al., *On the Hurwitz action in finite Coxeter groups*](https://doi.org/10.1515/jgth-2016-0025). The Heisenberg restriction cannot support a fresh mechanism claim. |
| C12 | `BOUNDED_NO_DIRECT_HIT` for iteration of ((AB,BA)). | Ordinary AB/BA spectral and similarity results are adjacent and must be subtracted; no theorem is mature enough to justify a deeper audit yet. |
| C13/C18 | `BOUNDED_NO_DIRECT_HIT` for the literal sandwich iterate. | Its proved signal is only radical-degree doubling, already too close to power and filtration mechanisms. It is killed internally before novelty matters. |

Queries included exact strings and algebraically equivalent phrases such as `"AA^T-A^TA" finite field map`, `transpose self-commutator dynamics`, `"x(I:y)+y(I:x)"`, `cross colon monomial ideal dynamics`, `subspace lattice Fibonacci nilpotent recurrence`, `"(x+y,xy)" finite field dynamics`, `Heisenberg Nielsen transformation cycles`, `Hurwitz action pairs`, and `"(AB,BA)" matrix dynamics`. Searches were also made in arXiv and official publisher indexes. No secondary survey or search-result snippet is being treated as ownership evidence.

## Gate for the next algebraic pass

A candidate may leave scouting only if all four conditions hold:

1. a theorem is proved symbolically beyond the finite pilot;
2. it contains an exact layer/fibre/cycle statement or a sharp parameterized transient, not just eventual periodicity;
3. direct-owner and nearest-mechanism subtraction is written claim by claim;
4. a second implementation independently checks the theorem over fresh parameters (including non-prime finite fields where relevant).

Current gate decisions:

- C1: **GO_PROOF_DOSSIER / EXTERNAL_HOLD**;
- C3: **GO_PROOF_DOSSIER / EXTERNAL_HOLD**;
- C6: **GO_PROOF_DOSSIER / EXTERNAL_HOLD**;
- C8, C12: **RESERVE / EXTERNAL_HOLD**;
- C2, C4, C5, C7, C9--C11, C13--C20: **KILL_OR_PARK**.

No paper number is allocated by this report.
