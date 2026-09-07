# Algebraic scout for P107--P111

Status: **SCOUTING FREEZE / EXTERNAL HOLD**
Scope: finite algebra, arithmetic, matrices, semigroups, and finite module
dynamics.  This document assigns no paper number by itself.  In particular,
`NO DIRECT HIT LOCATED` below records a bounded search, not a claim of
absolute novelty.

## 1. Historical firewall: P1--P106

The paper directories, batch READMEs, recent system firewalls, and candidate
kill ledgers were inspected before generating the pool.  The occupied action
families are summarized here; the summary is deliberately about the
*dynamical action*, not merely vocabulary.

| range | already occupied or explicitly rejected actions |
|---|---|
| P1--P43 | tensor/Fredholm and arithmetic-incidence systems; affine, modular, holonomy, and verifier shifts |
| P44--P61 | q-adic boundaries, fibre retractions, operator ideals, tree and Toeplitz shifts, finite-memory/countable shifts, forbidden-word and synchronized SFTs, covers, CA cylinders, periodic realization, routing, Sturmian/Ostrowski, and graph splitting |
| P62--P76 | random substitutions, rank-one XOR, beta shifts, two-dimensional and free-group SFTs, plaquette/hom/flat/Heisenberg shifts, zip and higher-rank graphs, Jordan substitutions, Dyck/Motzkin, Coxeter and IET systems |
| P77--P91 | automatic towers, sandpiles, hidden de Bruijn, graph majority, relation shifts, Fredkin CA, renewal systems, unitary Cayley shifts, periodic alphabets, hidden products, chain-ring shifts, parity/reset systems, Rule 184, and dihedral relations |
| P92--P101 | recurrence-avoidance, push--pop and S-adic systems, no-repeat shifts, finite subsets under circle expansion, sumset squaring, equal block sums, HNF shear, digit erasure, and random cap--floor synchronization |
| P102--P106 | cyclic group-algebra involution norm, double adjugate, random monomial cocycle, permutation cycle pruning, and synchronous MIS polarity |

The most relevant standing exclusions are generic affine/linear functional
graphs, ordinary finite-relation SFTs, generic group power maps, Schur-square
closure, graph-neighborhood polarity, and unqualified `0`-Hecke/sorting
repackagings.  A repository-wide search found no existing occurrence of the
four exact strings/actions `Drazin`, `subspace sweep`, `matrix Möbius`, or the
map `U -> N(U)`.  That lexical fact is only an internal cross-check.

## 2. Ranked result

| rank | candidate | internal decision | external decision | reason in one line |
|---:|---|---|---|---|
| 1 | order-three matrix Möbius action | **GO** | **HOLD** | complete 1/3-cycle census with a split/inert/ramified fixed-point transition |
| 2 | regular-nilpotent image dynamics on the subspace lattice | **GO** | **HOLD** | exact absorption CDF, every rank transition, sharp depth, and parameter recovery |
| 3 | meet/join sweep on subspace tuples | RESERVE | HOLD | strong exact depth census, but lattice-sorting is a direct neighboring owner and generic sorting was previously firewalled |
| 4 | Drazin-inverse dynamics | KILL INTERNAL | HOLD | formulas are complete, but P103/P106 and classical Drazin/Fitting theory leave too little independent space |
| 5 | Newton--Schulz inverse basin modulo `p^r` | KILL DIRECT/INTERNAL | HOLD | exact error squaring is already the standard modular inverse iteration and approaches P100/P102 |
| 6 | nilpotent-matrix squaring | KILL INTERNAL/OWNER | HOLD | Jordan block halving is clean but is a matrix power-map version of an occupied squaring/absorber engine |
| 7 | translation on irreducible polynomials | KILL DIRECT OWNER | HOLD | this is a special `PGL_2(F_q)` action with a direct invariant-polynomial literature |
| 8 | polynomial Euclidean-remainder dynamics | KILL DIRECT OWNER | HOLD | exact length distributions for the finite-field Euclidean algorithm are already published |
| 9 | Hurwitz map on finite-group pairs | KILL DIRECT OWNER | HOLD | the action and its finite-orbit problem are directly owned |
| 10 | subspace-product squaring in a prime field extension | KILL INTERNAL | HOLD | linear Kneser gives the signal, but it is P97/Schur-square closure in multiplicative dress |
| 11 | centralizer polarity on subgroup lattices | KILL INTERNAL/DIRECT | HOLD | the triple-collapse is exactly the P106 polarity engine and centralizer lattices are owned |

Only candidates 1 and 2 are recommended for a theorem contract.  Candidate 3
is a diversity reserve, not a recommendation to spend a paper slot.

## 3. Candidate records

### A1. Order-three matrix Möbius action -- GO / external HOLD

**Update rule.**  For a prime power `q` and `d>=1`, let

```text
X(d,q) = {A in M_d(F_q) : A and I-A are invertible},
T(A)   = (I-A)^(-1).
```

The two invertibility conditions make this an honest finite self-map.  The
empty boundary `X(1,2)=empty` must remain in every theorem statement.

**First two exact signals.**  Direct rational manipulation gives

```text
T^2(A) = I-A^(-1),             T^3(A)=A.
```

The fixed equation is `A^2-A+I=0`.  Thus the fixed census changes sharply
according as this quadratic is split, irreducible, or ramified over `F_q`.
The exact probe found, for example,

```text
(q,d)=(2,4): |X|=5824, Fix=112, 1904 three-cycles;
(q,d)=(3,3): |X|=6291, Fix=105, 2062 three-cycles;
(q,d)=(7,2): |X|=1687, Fix=58,  543 three-cycles.
```

**Prospective theorem package.**  Write `G_d(q)=|GL_d(q)|` and use Gaussian
binomials.  Inclusion--exclusion in the subspace lattice gives the phase size

```text
D_d(q) = sum_{k=0}^d [d k]_q (-1)^k q^(k(k-1)/2)
                         q^(k(d-k)) G_{d-k}(q)
       = G_d(q) sum_{k=0}^d (-1)^k / product_{i=1}^k (q^i-1).
```

The fixed count `F_d(q)` is

```text
char(F_q)=3:
  sum_{0<=r<=d/2} [d r]_q [d-r r]_q G_r(q);

char(F_q)!=3 and q=1 (mod 3):
  sum_{r=0}^d [d r]_q q^(r(d-r));

q=2 (mod 3):
  0                                      if d is odd,
  G_d(q)/G_{d/2}(q^2)                    if d is even.
```

Consequently every orbit has length one or three,

```text
#Per_1 = F_d(q),   #Per_3 = (D_d(q)-F_d(q))/3,
Fix(T^n) = F_d(q) if 3 does not divide n, and D_d(q) otherwise,
zeta_T(z)=(1-z)^(-F_d(q))(1-z^3)^(-(D_d(q)-F_d(q))/3).
```

The characteristic-three line follows from `A=-I+N`, `N^2=0`; the split line
counts ordered eigenspace decompositions; the inert line is one semisimple
`F_{q^2}`-module orbit.

**Two independent proof/control routes.**

1. Prove the order-three rational identity in the matrix ring, then use
   Möbius inversion on the subspace lattice and rational canonical form for
   the three fixed-point regimes.
2. Enumerate literal matrices, invert by finite-field Gauss--Jordan, build the
   functional graph, and compare independently evaluated Gaussian-binomial
   formulas; no characteristic polynomial routine is used by the control.

**Nearest owners and subtraction.**  Matrix linear-fractional transformations
are classical in N. J. Young, *Linear fractional transformations in rings and
modules* ([DOI](https://doi.org/10.1016/0024-3795(84)90131-9)).  The phase
count is a q-derangement count; see M. K. Srinivasan, *The Eulerian generating
function of q-derangements* ([DOI](https://doi.org/10.1016/j.disc.2006.04.007)).
Quadratic matrix-equation solution counts also have a direct literature; see
Y. Chen and X. Zhang, *A Class of Quadratic Matrix Equations over Finite
Fields* ([DOI](https://doi.org/10.1142/S1005386723000147)).  A paper would
therefore have to subtract all three ingredients and sell only the exact
finite dynamical synthesis.  The closest internal neighbor is P103 (full
matrix phase), with secondary motif overlap with P102's 1/3-type block split.

**Kill condition.**  Kill immediately if a source is found that studies this
exact map on the same domain and already states the complete fixed/cycle/zeta
package, or if the quadratic-equation owner contains the same three-regime
dynamical corollary.

### A2. Regular-nilpotent image dynamics -- GO / external HOLD

**Update rule.**  Let `V=F_q^d`, let `N` be one regular nilpotent Jordan block,
and let `L(V)` be the full finite subspace lattice.  Define

```text
T_N : L(V) -> L(V),     T_N(U)=N(U).
```

This is not the previously falsified saturation action `U -> U+N(U)`.

**First two exact signals.**  Iteration is literal: `T_N^t(U)=N^t(U)`.  If
`tau(U)=min{t:N^tU=0}`, then

```text
#{U : tau(U)<=t} = G_min(t,d)(q),
G_j(q)=sum_{r=0}^j [j r]_q.
```

For example, the depth profiles are

```text
q=2,d=6: 1,1,3,11,51,307,2451;
q=3,d=5: 1,1,4,22,184,2452;
q=5,d=4: 1,1,6,56,1056.
```

**Prospective theorem package.**  For `0<=t<=d`, `0<=s<=r<=d`, the full
rank-transition law is

```text
#{U : dim U=r, dim N^t(U)=s}
 = [t, r-s]_q [d-t, s]_q q^((t-r+s)s),
```

with the convention that invalid Gaussian binomials vanish.  It follows that
zero is the unique periodic point, the sharp maximal depth is `d`, every
positive-period fixed count is one, and `zeta_T(z)=(1-z)^(-1)`.  The temporal
census also recovers the family: the maximal depth is `d`, while
`#{tau<=2}=q+3` recovers `q` when `d>=2` (the one-dimensional boundary must be
separated).

**Two independent proof/control routes.**

1. Use rank--nullity for `N^t|_U` and count subspaces with prescribed
   intersection with the flag `ker N^t`; the standard graph-of-a-linear-map
   argument supplies the power of `q`.
2. Generate every subspace from its unique RREF basis, apply the literal
   Jordan shift to all vectors, and compare every `(t,r,s)` cell and every
   depth CDF against independently evaluated Gaussian formulas.

**Nearest owners and subtraction.**  Gaussian subspace counts and prescribed
intersection counts are classical; a convenient official background source
is B. R. Butler, *Subgroup Lattices and Symmetric Functions* ([AMS DOI](https://doi.org/10.1090/memo/0539)),
and the finite-subspace counting background is also surveyed in
*Counting subspaces of a finite vector space* ([arXiv:1006.2193](https://arxiv.org/abs/1006.2193)).
Invariant/hyperinvariant subspace lattices of nilpotent transformations are a
separate mature subject.  The owner-subtracted object here is only the
finite-time image action and its joint temporal/rank census.  Internally it is
adjacent to P73 (Jordan structure) and to the killed saturation spike, but its
phase action, statistic, and formula are different.

**Kill condition.**  Kill if an induced-map-on-Grassmannians source already
states this exact absorption and joint rank-transition package, or if a full
proof reveals that the result is merely a one-paragraph corollary with no
second theorem beyond the standard intersection formula.

### A3. Meet/join sweep on subspace tuples -- RESERVE / external HOLD

**Update rule.**  For an `m`-tuple of subspaces, the adjacent comparator is

```text
C_i(...,U_i,U_{i+1},...)=(...,U_i intersect U_{i+1}, U_i+U_{i+1},...).
```

One left-to-right sweep is `S=C_{m-1}...C_1` (with `C_1` applied first).

**First two exact signals.**  One sweep has the literal formula

```text
S(U_1,...,U_m)_i=(U_1+...+U_i) intersect U_{i+1}  (i<m),
S(U_1,...,U_m)_m=U_1+...+U_m.
```

For triples, `S^3=S^2`, and

```text
S^2(U,V,W)=(U intersect V intersect W,
            (U intersect V)+((U+V) intersect W),
            U+V+W).
```

The second signal is a nontrivial exact depth census.  If `F` is the number of
weak flags and `H` the number of triples with `U intersect V <= W`, then

```text
depth 0 = F,   depth 1 = H-F,   depth 2 = G_d(q)^3-H,
F=sum_{a<=b<=c}[d c]_q[c b]_q[b a]_q,
H=sum_{a,b,k}[d k]_q[d-k,a-k]_q[d-a,b-k]_q
              q^((a-k)(b-k)) G_{d-k}(q).
```

Full small cases also support sorting in at most `m-1` sweeps, sharply attained
by `(V,...,V,0)`.  This general-`m` statement remains a proof obligation rather
than a frozen theorem.

**Two independent proof/control routes.**  Modular lattice identities and an
induction on the sorted suffix give the structural route; RREF enumeration
with precomputed meet/join tables gives the independent finite route.

**Nearest owner and subtraction.**  Jens Gerlach's *Recursive Sorting in
Lattices* directly owns lattice sorting in the distributive setting
([arXiv/DOI](https://doi.org/10.48550/arXiv.1306.0019)).  The present lattice is
modular and non-distributive, and the triple transient census is not in that
paper, but the headline comparator language is no longer clean.  Moreover the
P102--P106 kill ledger explicitly says generic `0`-Hecke candidates were
rejected.  The only defensible residue is the non-distributive subspace-lattice
depth law, so this is a reserve, not a GO.

**Kill condition.**  Kill on any direct modular-lattice sorting theorem giving
the same sweep bound, or if the general `m-1` proof reduces verbatim to the
known distributive sorting network.

### A4. Drazin-inverse dynamics -- KILL INTERNAL

**Update rule.**  On all of `M_d(F_q)`, set `T(A)=A^D`, the Drazin inverse.

**Signals and possible theorem.**  Fitting decomposition gives `T^3=T`; its
image is the group-invertible core.  With `G_r(q)=|GL_r(q)|`,

```text
Core_d(q)=sum_r [d r]_q q^(r(d-r)) G_r(q).
```

If `I_r(q)` counts involutions in `GL_r(q)`, then

```text
Fix_d(q)=sum_r [d r]_q q^(r(d-r)) I_r(q),
I_r(q)=sum_a [r a]_q q^(a(r-a))                         (q odd),
I_r(q)=sum_{s<=r/2}[r s]_q[r-s s]_q G_s(q)             (q even).
```

The fibre above a recurrent rank-`r` matrix has size
`q^((d-r)(d-r-1))`; the core has only one- and two-cycles and hence the full
fixed sequence and zeta are immediate.

**Two routes.**  Fitting/Drazin decomposition plus finite-matrix enumeration;
independently, compute the Drazin inverse from the index and period of the
monogenic power semigroup and audit every fibre.

**Owners/collision.**  The operation itself begins with M. P. Drazin,
*Pseudo-Inverses in Associative Rings and Semigroups*
([DOI](https://doi.org/10.1080/00029890.1958.11991949)); the nilpotent fibre
count is classical, e.g. M. Gerstenhaber
([DOI](https://doi.org/10.1215/ijm/1255629831)).  Internally, the full matrix
phase is P103 and the cubic polarity temporal skeleton is P106.  The exact
probe succeeds, but the candidate is killed for diversity.

**Kill condition.**  Already met: same phase family plus same `T^3=T` proof
shape inside the repository, with classical owners for both structural halves.

### A5. Newton--Schulz inverse basin modulo a prime power -- KILL

**Update rule.**  On `X={x mod p^r:x=1 mod p}`, let `T(x)=x(2-x)`.

**Signals/theorem.**  With `e=1-x`, `e(Tx)=e^2`.  Thus `1` is the unique
periodic point,

```text
tau(x)=ceil(log_2(r/v_p(1-x))),
#{tau<=t}=p^(r-ceil(r/2^t)),
max tau=ceil(log_2 r),      zeta=(1-z)^(-1).
```

The two routes are the exact error conjugacy/valuation count and exhaustive
modular iteration.  Jean-Guillaume Dumas directly studies this modular
Newton iteration ([DOI](https://doi.org/10.1109/TC.2013.94),
[arXiv](https://arxiv.org/abs/1209.6626)).  It also repeats P100's valuation
absorber and P102's squaring engine.

**Kill condition.**  Already met by the direct owner and internal mechanism.

### A6. Squaring on the nilpotent cone -- KILL INTERNAL/OWNER

**Update rule.**  On the nilpotent cone `Nil_d(F_q)`, set `T(A)=A^2`.

**Signals/theorem.**  If the largest Jordan block has size `nu(A)`, then
`tau(A)=ceil(log_2 nu(A))`; the sharp maximum is `ceil(log_2 d)`.  The depth
CDF is the sum of the classical conjugacy-class masses over partitions whose
largest part is at most `2^t`.  A Jordan-partition proof and a literal matrix
power/rank-sequence control are independent routes.

M. Gerstenhaber's nilpotent-matrix count is classical
([DOI](https://doi.org/10.1215/ijm/1255629831)); matrix power-map dynamics is
an active direct area, e.g. S. Panja's 2026 paper (which treats odd prime
powers and therefore is a nearby, not identical, owner)
([arXiv:2603.12295](https://arxiv.org/abs/2603.12295)).  Internally this is too
close to P97 squaring, P100 absorption, and P103 matrices.

**Kill condition.**  Already met by the internal action/proof-engine collision.

### A7. Translation on irreducible polynomials -- KILL DIRECT OWNER

**Update rule.**  On monic degree-`n` irreducibles over `F_q` of
characteristic `p`, set `T(f)(x)=f(x+1)`.

**Signals/theorem.**  `T^p=id`; hence only one- and `p`-cycles occur.  Fixed
polynomials lie in the invariant ring `F_q[x^p-x]`, forcing a degree divisibility
anomaly and an Artin--Schreier factorization problem.  Root-orbit analysis and
coefficient enumeration would be the two routes.

This is directly contained in the `PGL_2(F_q)` action on irreducible
polynomials studied by R. Gow and G. McGuire
([DOI](https://doi.org/10.1016/j.ffa.2021.101991),
[arXiv](https://arxiv.org/abs/2105.11247)).

**Kill condition.**  Already met by the direct action owner.

### A8. Polynomial Euclidean-remainder dynamics -- KILL DIRECT OWNER

**Update rule.**  On a finite degree-bounded disjoint union of ordered monic
polynomial pairs, use `(a,b)->(b,monic(rem(a,b)))`, with gcd states absorbing.

**Signals/theorem.**  The depth is exactly the Euclidean/continued-fraction
length, quotient-degree compositions stratify every transient layer, and the
zeta has only terminal fixed factors.  Continued fractions and quotient words
give one route; dynamic programming over all monic pairs gives another.

Exact length distributions were already obtained by A. and J. Knopfmacher
([DOI](https://doi.org/10.1112/S002557930001528X)); a fuller finite-field
algorithm analysis is K. Ma and J. von zur Gathen
([DOI](https://doi.org/10.1016/S0747-7171(08)80021-1)).

**Kill condition.**  Already met by direct exact-length owners.

### A9. Hurwitz map on finite-group pairs -- KILL DIRECT OWNER

**Update rule.**  For a finite group `G`, set
`H(x,y)=(xyx^{-1},x)` on `G^2`.

**Signals/theorem.**  The product `P=xy` is invariant and
`H^2(x,y)=(P x P^{-1},P y P^{-1})`.  Thus periods reduce to conjugation by
the conserved product; a class-by-class census and direct Cayley-table orbit
enumeration are independent routes.

Finite Hurwitz orbit problems are directly owned; see T. Ito, *Finite orbits
of Hurwitz actions on braid systems* ([arXiv](https://arxiv.org/abs/0912.0405))
and S. P. Humphries, *Finite Hurwitz braid group actions for Artin groups*
([DOI](https://doi.org/10.1007/BF02803499)).  P91 is an additional internal
group/reverser neighbor.

**Kill condition.**  Already met by the direct action literature.

### A10. Subspace-product squaring -- KILL INTERNAL

**Update rule.**  In a prime-degree extension `K/F_q`, on `F_q`-subspaces
`W<=K` containing `1`, define `T(W)=span_q(WW)`.

**Signals/theorem.**  Linear Kneser predicts
`dim T(W)>=min([K:F_q],2 dim(W)-1)` away from a stabilizer; in prime degree
the only fixed subalgebras are `F_q` and `K`.  Polynomial-basis subspaces give
sharp doubling-depth examples.  The routes are linear Kneser/stabilizer
analysis and exact extension-field multiplication tables.

The product-growth engine is owned by Hou--Leung--Xiang, *A Generalization of
an Addition Theorem of Kneser*
([DOI](https://doi.org/10.1006/jnth.2002.2793)).  More decisively, the action is
the multiplicative analogue of P97's sumset squaring and the previously killed
Schur-square-code closure.

**Kill condition.**  Already met by the internal squaring/closure firewall.

### A11. Centralizer polarity -- KILL INTERNAL/DIRECT

**Update rule.**  On the subgroup lattice of a finite group, set
`T(H)=C_G(H)`.

**Signals/theorem.**  The order-reversing Galois identity gives `T^3=T`;
recurrent states are centralizer subgroups and fixed states are self-centralizing
abelian subgroups.  An extraspecial-group calculation and literal subgroup
lattice enumeration are possible independent routes.

Centralizer lattices and their self-duality are direct classical objects; a
recent official reference is *Central products and the Chermak--Delgado
lattice* ([DOI](https://doi.org/10.1016/j.jpaa.2024.107769)).  Internally this
is precisely P106's antitone-polarity engine.

**Kill condition.**  Already met by both direct owner and P106.

## 4. Exact proof spikes

All scripts use only the Python standard library and recompute their formulas
from integers.  They do not import any paper implementation.

| script | lanes and strongest checks | fresh result |
|---|---|---:|
| `code/algebraic_matrix_mobius.py` | prime fields `q=2,3,5,7`, `d<=4`; literal inverse, domain invariance, `T^3`, fixed quadratic, orbit census, phase/fixed formulas | **104,783 PASS** |
| `code/algebraic_nilpotent_image.py` | `q=2,d<=6`; `q=3,d<=5`; `q=5,d<=4`; every subspace, iterate, depth CDF, every `(t,r,s)` cell | **136,487 PASS** |
| `code/algebraic_subspace_sweep.py` | complete triples through `(q,d)=(2,4),(3,3),(5,2)` and complete `m=4,5` lanes; closed `S^2`, depth criterion/census, sharp bound witnesses | **1,442,212 PASS** |
| `code/algebraic_drazin_inverse.py` | `q=2,3,5`, `d<=3`; semigroup-computed Drazin inverse, identities, core, fixed/cycle and every rank fibre | **161,892 PASS** |

Total fresh exact assertions: **1,845,374**, all passing.  The Drazin script is
retained as a documented successful dead road: mathematical cleanliness does
not override the collision firewall.

## 5. Frozen theorem contracts

### Contract 1: matrix Möbius

Freeze only the following conjunction: exact phase count; `T^3=id`; complete
split/inert/characteristic-three fixed census; complete 1/3-cycle and fixed
sequence; rational zeta; explicit boundary cases.  Subtract linear-fractional
matrix theory, q-derangements, and quadratic-matrix-equation counts.  External
status remains HOLD.

### Contract 2: nilpotent image on subspaces

Freeze: exact iterates; absorption CDF and sharp depth; full joint
dimension-transition formula; unique recurrent point and zeta; recovery of
`(q,d)` with `d=1` isolated; two independent proofs/controls.  Explicitly
separate it from `U -> U+NU`.  Subtract Gaussian intersection counts and the
classical invariant-subspace literature.  External status remains HOLD.

## 6. Search boundary

The owner audit combined title/keyword searches, DOI metadata, official arXiv
records, and the local kill/firewall ledgers.  It was designed to find reasons
to stop, not to certify novelty.  Before any external circulation, both GO
candidates still require a dedicated theorem-level direct-owner search using
the exact update rule, its conjugate formulations, and cited-reference
backward/forward chaining.  No statement in this report may be rewritten as
“first”, “new”, “novel”, or “previously unknown”.
