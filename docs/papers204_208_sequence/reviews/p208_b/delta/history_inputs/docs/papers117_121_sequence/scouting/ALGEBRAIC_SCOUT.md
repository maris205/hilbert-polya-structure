# Algebraic Phase-2 scout for P117--P121

**Status:** cheap theorem pilots complete; no paper number assigned  
**Scope:** exactly twelve literal finite self-maps  
**External status:** `HOLD_EXTERNAL`

This is an idea-and-falsification ledger, not a novelty certificate.  The
P1--P116 firewall and the Stage-1 landscape were applied before ranking.  In
particular, ordinary finite-linear functional graphs, power maps, valuation
erasure, nilpotent-image dynamics, ideal powers, closure wrappers, and
one-coordinate Cartier decimation receive no credit.

## Candidate synopsis

| ID | literal self-map | first exact signal | disposition |
|---|---|---|---|
| A1 | Boolean-lattice zeta transform in characteristic `p` | first fixed-dimension excess is exactly `+1` at `n=2p-1` | **PROMOTE--CONDITIONAL** |
| A2 | `p^a`-th Hasse derivative on bounded polynomials | monomial depth is one plus one selected base-`p` digit | **RESERVE** |
| A3 | forward finite difference on bounded polynomials | `Delta^p=0`, with extra invariant directions after degree `p-1` | **KILL DIRECT/LINEAR** |
| A4 | commutator with one regular nilpotent matrix | nilpotency is a Lucas carry clock, not always `2d-1` | **KILL OWNER/INTERNAL** |
| A5 | sum of two shifted coordinate Cartier operators | coupled depth is the last carry-free binomial cell | **PROMOTE--CONDITIONAL** |
| A6 | Frobenius-twisted Fibonacci companion on `F_(p^a)^2` | split/inert/ramified period resonance at discriminant five | **KILL GENERIC LINEAR** |
| A7 | shear-orbit join on ideals of a non-PIR truncated ring | sharp global closure depth `min(d,p-1)` | **RESERVE HIGH-RISK** |
| A8 | Frobenius-root pullback on proper ideals of that ring | zero reaches the maximal ideal in `ceil(log_p(d+1))` steps | **KILL POWER/CLOSURE** |
| A9 | valuation-delay cyclic shift on `(Z/p^a Z)^r` | `T^r=pI` and a closed kernel CDF | **KILL DIRECT/INTERNAL** |
| A10 | Young-lattice up--down operator modulo `p` | at `n=p`, a length-two zero Jordan chain appears | **PROMOTE--CONDITIONAL** |
| A11 | cyclic McKay-support neighbor map | odd cycles fill; even cycles enter a parity two-cycle | **KILL GRAPH POWER** |
| A12 | tensor-square support on `Irr(C_m)` | it is literally sumset squaring | **KILL INTERNAL P97** |

## Twelve literal records

### A1. Boolean zeta transform

- **Phase/update/parameters.** For `q=p^b`, let
  `V_n(q)={f:2^[n]->F_q}` and
  `(Zf)(S)=sum_(A subset S) f(A)`, with parameters `(p,b,n)`.
- **Early anomaly.** `(Z^m)_(S,A)=m^|S\A|`, hence `Z^p=I`.  If
  `kappa_(n,p)=dim ker(Z-I)`, then for odd `p`,
  `kappa=binom(n,floor(n/2))` through `n=2p-2`, while
  `kappa_(2p-1,p)=binom(2p-1,p-1)+1`.  Thus all cycles have length `1` or
  `p`, but the fixed exponent has a sharp modular threshold.
- **Owner subtraction.** General finite-linear dynamics is owned by Elspas,
  Hernandez Toledo, and Reis.  Modular tensor products of unipotent blocks
  are owned by [Glasby--Praeger--Xia](https://arxiv.org/abs/1403.4685), and
  Pascal-related transforms are a close matrix owner.  Internally, generic
  linear and coefficient-transform claims are firewalled.
- **Two routes.** (I) Count intermediate subsets and use the modular
  `C_p` Green-ring recurrence for `V_2^(tensor n)`; (II) exact modular ranks
  of the literal zeta matrix plus small full functional graphs.
- **Decisive kill.** Kill if backward chaining finds the displayed
  `V_2^(tensor n)` fixed-dimension threshold, or if owner subtraction leaves
  only the generic `1/p` cycle census.

### A2. A selected Hasse derivative

- **Phase/update/parameters.** On `F_q[x]_(<=n)`, with `q=p^b`, set
  `T=H_(p^a)`, so `T(x^k)=binom(k,p^a)x^(k-p^a)`; parameters are
  `(p,b,a,n)`.
- **Early anomaly.** If `k_a` is the `a`-th base-`p` digit of `k`, then
  `tau(x^k)=k_a+1`, `T^p=0`, and
  `dim ker T^t=#{0<=k<=n:k_a<t}`.  Degree/order heuristics are false.
- **Owner subtraction.** Successive Hasse-derivative identities and Lucas
  digit control are classical; recent derivative/Hasse rank work uses the
  same weighted-shift decomposition.  Internally this approaches P100's
  digit clock and P115's coefficient chains.
- **Two routes.** (I) Lucas' theorem on every monomial; (II) literal
  coefficient matrices and kernel ranks.
- **Decisive kill.** Kill if no theorem survives beyond the one-digit shift,
  or if the full phase is only a generic nilpotent linear graph.  Reserve only
  for a genuinely multi-digit order not reducible to P100.

### A3. Forward finite difference

- **Phase/update/parameters.** On `F_q[x]_(<=n)`, set
  `T(f)=f(x+1)-f(x)`; parameters `(p,b,n)`.
- **Early anomaly.** `T^p=0`, its nilpotency index is `min(n+1,p)`, and
  `dim ker T=floor(n/p)+1`, reflecting `F_q[x^p-x]`.
- **Owner subtraction.** Translation actions on polynomials lie in the
  `PGL_2` program of [Gow--McGuire](https://arxiv.org/abs/2105.11247), and
  the remaining graph is ordinary finite-linear dynamics.
- **Two routes.** (I) use `T=E-I`, `E^p=I`, and the invariant ring;
  (II) Pascal-matrix ranks and literal iteration.
- **Decisive kill.** Already met: the temporal package is a direct linear
  corollary with no residual second engine.

### A4. Regular-nilpotent commutator

- **Phase/update/parameters.** On `M_d(F_q)`, let `J=J_d(0)` and
  `T(A)=JA-AJ`; parameters `(p,b,d)`.
- **Early anomaly.** The expansion
  `T^t(A)=sum_k (-1)^k binom(t,k)J^(t-k)AJ^k` makes the exact nilpotency
  index one plus the last `t` admitting a feasible nonzero binomial
  coefficient modulo `p`.  The tempting least-`p`-power formula fails at
  `(p,d)=(5,9)`: the index is `15`, not `17`.
- **Owner subtraction.** This is a Kronecker-sum/Jordan-partition problem,
  directly adjacent to [modular tensor-product theory](https://arxiv.org/abs/1711.06860).
  P73 and P109 are internal Jordan/nilpotent neighbors.
- **Two routes.** (I) commuting left/right multiplication plus Lucas;
  (II) exact ranks of the `d^2` by `d^2` commutator matrix.
- **Decisive kill.** Already met unless a statistic not determined by the
  owned modular Jordan partition is found.

### A5. Coupled shifted-Cartier sum

- **Phase/update/parameters.** For `q=p^b`, let `V_h` be bivariate
  polynomials with both exponents below `p^h`.  Define
  `C_x f=sum sigma^(-1)(c_(pi+p-1,j))x^i y^j` and analogously `C_y` in the
  second coordinate; set `T=C_x+C_y`.  Parameters `(p,b,h)`.
- **Early anomaly.** `C_x,C_y` commute and are nilpotent of index `h+1`.
  The sharp depth is
  `1+max{t: some k satisfies k<=h, t-k<=h, binom(t,k) != 0 mod p}`.
  For `h<p` this is `min(2h+1,p)`, but `(p,h)=(5,8)` gives `15`, not the
  naive `17`.  This is a genuine two-chain Lucas clock rather than P115's
  single index chain.
- **Owner subtraction.** All modular Jordan products are zero-credit via
  Glasby--Praeger--Xia; all one-coordinate Cartier iterates, cores, fibres,
  and generic finite-linear components are zero-credit via P115 and its
  cited owners.
- **Two routes.** (I) decompose coefficient indices into two trailing-digit
  chains and apply Lucas carry criteria; (II) construct the literal
  coefficient operator and compare all power ranks with the chain product.
- **Decisive kill.** Kill if the full rank/fibre census is merely mechanical
  substitution into an existing Jordan-partition theorem.  Promote only if
  the coefficient-chain multiplicities yield a new closed temporal law and
  parameter recovery after that subtraction.

### A6. Frobenius-twisted Fibonacci companion

- **Phase/update/parameters.** On `F_(p^a)^2`, set
  `T(x,y)=(y^p,x^p+y^p)`; parameters `(p,a)`.
- **Early anomaly.** With Frobenius `sigma` and
  `B=[[0,1],[1,1]]`, `T^t=B^t sigma^t` and `T^a=B^a`.  The discriminant
  `5` gives split, inert, and characteristic-five ramified period regimes.
- **Owner subtraction.** Restriction of scalars makes this an ordinary
  finite-linear system; semilinear notation does not escape Elspas/Wang/
  Hernandez Toledo.  P108 is an internal Fibonacci motif neighbor.
- **Two routes.** (I) companion-matrix/Frobenius factorization; (II) direct
  extension-field orbit enumeration.
- **Decisive kill.** Already met by the generic-linear firewall.

### A7. Shear-orbit join on a non-principal ideal lattice

- **Phase/update/parameters.** Let
  `R_(p,d)=F_p[x,y]/(x,y)^(d+1)`, let `alpha(x)=x+y`, `alpha(y)=y`, and on
  the full ideal lattice set `T(I)=I+alpha(I)`; parameters `(p,d)`.
- **Early anomaly.** `T^t(I)=sum_(k=0)^t alpha^k(I)`.  Every ideal stabilizes
  by `min(d,p-1)`, and the bound is sharp for the principal top-degree ideal
  generated by `x^m y^(d-m)`, `m=min(d,p-1)`.
- **Owner subtraction.** Cyclic-`p` modular invariant/submodule closure is
  background.  Internally this is close to P109 saturation and P110 join
  closure; non-PIR vocabulary alone earns nothing.
- **Two routes.** (I) write `alpha=1+N` on each homogeneous layer and use
  modular Krylov spans; (II) exact row-space ideals, multiplication closure,
  and literal shear iteration.
- **Decisive kill.** Kill unless a closed all-ideal depth/fibre enumerator is
  found; a sharp maximum alone cannot clear the closure firewall.

### A8. Frobenius-root pullback on proper ideals

- **Phase/update/parameters.** On proper ideals of the same `R_(p,d)`, set
  `T(I)=F^(-1)(I)={r:r^p in I}`; parameters `(p,d)`.
- **Early anomaly.** The maximal ideal `m` is fixed; every proper ideal is
  absorbed by it, and the zero ideal has sharp depth
  `ceil(log_p(d+1))`.
- **Owner subtraction.** Frobenius roots, radicalization, and primary-ideal
  structure are classical.  The clock is another degree/valuation power
  contraction near P100/P107/P115.
- **Two routes.** (I) total-degree behavior under Frobenius; (II) literal
  enumeration of all elements in small truncated rings and exact ideal
  preimages.
- **Decisive kill.** Already met: no independent temporal invariant beyond
  the Frobenius nilpotence height was found.

### A9. Valuation-delay module shift

- **Phase/update/parameters.** On `M=(Z/p^a Z)^r`, set
  `T(x_0,...,x_(r-1))=(x_1,...,x_(r-1),p x_0)`; parameters `(p,a,r)`.
- **Early anomaly.** `T^r=pI`, the sharp depth is `ar`, and for `t=qr+s`,
  `0<=s<r`,
  `#ker T^t=p^((r-s)min(a,q)+s min(a,q+1))`.
- **Owner subtraction.** Linear dynamics over finite rings is directly
  treated by [Xu--Zou](https://www.sciencedirect.com/science/article/pii/S0021869308004936).
  P100 and P107 already spend valuation clocks.
- **Two routes.** (I) the identity `T^r=pI` plus coordinate valuations;
  (II) literal modular matrix orbits and kernel counts.
- **Decisive kill.** Already met by direct generic owner and internal engine.

### A10. Modular Young up--down dynamics

- **Phase/update/parameters.** Let `P(n)` be the partitions of `n` and work
  on `F_p^P(n)`.  On a basis partition `lambda`, remove one corner in every
  possible way and then add one corner in every possible way, with path
  multiplicity reduced modulo `p`.  This is the `Ind Res` operator on the
  complex-character basis of `S_n`; parameters `(p,n)`.
- **Early anomaly.** Over characteristic zero the eigenvalues are
  `0,1,...,n` with differential-poset multiplicities.  At the first resonance
  `n=p`, the zero eigenvalue is not semisimple:
  `nullity(T^2)=nullity(T)+1` for `p=2,3,5,7` in the spike.
- **Owner subtraction.** Differential-poset up/down theory is classical;
  [Shah 2024](https://alco.centre-mersenne.org/articles/10.5802/alco.393/)
  proves Smith-normal-form results for associated operators.  All SNF,
  characteristic-zero spectrum, and generic linear graph consequences are
  zero-credit.
- **Two routes.** (I) the differential relation and integral/Smith
  filtrations; (II) branching-rule matrices with exact modular ranks of all
  powers.
- **Decisive kill.** Kill if the SNF/canonical-form literature already gives
  every modular Jordan block, or if the length-two chain is the only residual.
  Promote only toward a closed all-power kernel law with a second temporal
  output.

### A11. Cyclic McKay-support neighbors

- **Phase/update/parameters.** For `G=C_m`, write `Irr(G)=Z/mZ`, take
  `rho=chi+chi^(-1)`, and on nonempty subsets set
  `T(S)=supp(rho tensor directsum_(j in S) chi^j)=(S+1) union (S-1)`.
- **Early anomaly.** From a singleton, odd `m` reaches all irreducibles in
  sharp depth `m-1`; even `m` reaches the two parity classes, which form a
  two-cycle.
- **Owner subtraction.** This is exact-length reachability on a cycle McKay
  graph.  Graph powers and McKay adjacency are direct background; P96/P97/
  P84 are internal subset/Cayley neighbors.
- **Two routes.** (I) cyclic character fusion and parity; (II) bit-mask
  support iteration.
- **Decisive kill.** Already met: representation notation hides an ordinary
  graph-neighborhood power.

### A12. Tensor-square fusion support

- **Phase/update/parameters.** Again identify `Irr(C_m)=Z/mZ`; on nonempty
  supports set
  `T(S)=supp((directsum_(j in S)chi^j) tensor 2)=S+S`; parameter `m`.
- **Early anomaly.** For prime `m`, all supports of size at least two absorb
  at the full set, while nonzero singletons have period `ord_m(2)`.
- **Owner subtraction.** This is literally P97 sumset squaring after
  relabeling; power-map functional-graph owners are additional background.
- **Two routes.** (I) representation-ring multiplication; (II)
  Cauchy--Davenport and literal subset enumeration.
- **Decisive kill.** Already met by exact internal identity with P97.

## Cheap exact pilots and false conjectures

All scripts use only the Python standard library, fixed finite parameter
boxes, exact integer/modular arithmetic, and deterministic iteration.

| script | candidates checked | exact assertions | principal falsification |
|---|---|---:|---|
| `proof_spikes/alg_bad_characteristic.py` | A1--A4 | 666 | Boolean first excess at `2p-1`; global least-`p`-power commutator shortcut fails at `(5,9)` |
| `proof_spikes/alg_coupled_cartier.py` | A5 | 115 | additive depth `2h+1` and the naive `p`-power shortcut both fail; `(5,8)` has depth `15` |
| `proof_spikes/alg_nonpir_ideals.py` | A7--A8 | 1,018 | shear depth saturates at `p-1`; Frobenius-root depth is logarithmic, not the Loewy length |
| `proof_spikes/alg_module_representation.py` | A9--A12 | 15,825 | Young reduction is nonsemisimple at `n=p`; A12 is an exact P97 collision |
| **total** | ten coded lanes; A6 owner-killed on paper | **17,624** | all assertions pass |

The scripts record the false conjectures in their canonical terminal output.
No large exhaustive search was used; the largest enumerations are small
finite rings, bounded coefficient matrices, partitions through rank nine,
and cyclic supports through order thirteen.

## Ranked promote/reserve/kill ledger

| rank | ID | decision | reason after subtraction |
|---:|---|---|---|
| 1 | A10 | **PROMOTE--CONDITIONAL** | natural representation-data family and a sharp first modular Jordan resonance; must beat the 2024 SNF owner |
| 2 | A1 | **PROMOTE--CONDITIONAL** | sharp `2p-1` anomaly and complete cycle package; ordinary-linear firewall remains live |
| 3 | A5 | **PROMOTE--CONDITIONAL** | genuinely coupled coefficient chains and a nontrivial Lucas clock; modular Jordan ownership is severe |
| 4 | A7 | **RESERVE HIGH-RISK** | non-PIR phase and sharp characteristic ceiling, but the action is still a closure process |
| 5 | A2 | **RESERVE** | exact digit CDF is clean, but currently too close to P100/P115 and standard Hasse identities |
| 6 | A4 | **KILL OWNER/INTERNAL** | modular Jordan partitions determine the engine |
| 7 | A8 | **KILL POWER/CLOSURE** | only the classical Frobenius nilpotence height survives |
| 8 | A9 | **KILL DIRECT/INTERNAL** | generic finite-ring linear system plus an occupied valuation clock |
| 9 | A3 | **KILL DIRECT/LINEAR** | translation invariants and generic nilpotent linear dynamics suffice |
| 10 | A6 | **KILL GENERIC LINEAR** | restriction of scalars removes the apparent semilinear novelty |
| 11 | A11 | **KILL GRAPH POWER** | exact-length walks on a cycle, not a new representation-dynamical engine |
| 12 | A12 | **KILL INTERNAL P97** | literal equality with sumset squaring |

No `PROMOTE--CONDITIONAL` entry is frozen or assigned a paper number.  Each
requires a dedicated direct-owner search before any larger spike.  Novelty,
priority, external posting, and submission remain **HOLD_EXTERNAL**.
