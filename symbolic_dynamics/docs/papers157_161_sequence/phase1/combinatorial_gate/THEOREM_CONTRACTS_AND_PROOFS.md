# LCP/PAE theorem contracts and shortest complete proof sketches

**Gate date:** 2026-09-02 UTC  
**Portfolio boundary:** P1--P156  
**External state:** `HOLD_EXTERNAL`  
**Status:** both contracts are mathematically viable; neither survives the
collision gate.

The purpose of proving these statements is to distinguish a false conjecture
from a true but portfolio-occupied theorem.  The proofs below are independent
of the finite verifier.  The verifier is counterexample pressure only.

## 1. `LCP`: whole-first-child-subtree deletion

### Literal carrier and rule

Let `PT_{<=N}` be the finite disjoint union of plane rooted trees with at most
`N` vertices.  Write a tree recursively as `T=(T_1,...,T_k)` and the singleton
as `()`.  Define

```text
L(T_1,...,T_k)=(L(T_2),...,L(T_k)).
```

Thus the entire first-child subtree at every currently surviving vertex is
discarded in parallel.

### Contract LCP-A: all iterates and sharp clock

Give every nonroot vertex its Ulam--Harris address
`a(v)=(j_1,...,j_d)`, where `j_s` is its child index at depth `s`.  Put

```text
b_T(v)=min(j_1,...,j_d),
tau(T)=least t with L^t(T)=().
```

The exact claim is

```text
L^t(T_1,...,T_k)=(L^t(T_(t+1)),...,L^t(T_k)),
tau(T)=max_(v != root) b_T(v),
max_(|T|=n) tau(T)=n-1.
```

The maximum over an empty vertex set is zero.  The `(n-1)`-leaf star attains
the last bound.  The singleton is the unique recurrent state, and every
nonfixed step strictly loses vertices.

#### Proof

One update keeps precisely the original addresses all of whose coordinates
are at least two and sends

```text
(j_1,...,j_d) -> (j_1-1,...,j_d-1).
```

Induction on `t` therefore says that rank `t` keeps precisely those addresses
with every coordinate greater than `t`, subtracting `t` from every coordinate.
Reading the first coordinate gives the displayed recursive iterate formula.
A nonroot vertex survives through rank `t` exactly when `b_T(v)>t`; hence the
least empty rank is the maximum bottleneck.  A nonsingleton has a child of
index one, so at least that child root disappears and strict descent follows.
Finally every bottleneck is at most the root degree, which is at most `n-1`,
while the star has leaf addresses `1,...,n-1`.  This proves every assertion.

### Contract LCP-B: every-target, every-time inverse

Let

```text
T(z)=sum_(n>=1) Catalan_(n-1) z^n=z/(1-T(z)),
S_t(u)=1+u+...+u^t,
P_(t,U)(z)=sum_(V:L^t(V)=U) z^|V|.
```

For a target `U`, let `i(U)` and `l(U)` be its numbers of internal vertices
and leaves.  Then

```text
P_(t,())(z)=z S_t(T(z)),
P_(t,(U_1,...,U_r))(z)
  =z T(z)^t product_a P_(t,U_a)(z)       (r>=1),
P_(t,U)(z)=z^|U| T(z)^(t i(U)) S_t(T(z))^l(U).
```

Consequently the exact rank-`n` fibre is `[z^n]P_(t,U)(z)`.  For `t>=1` it is
positive exactly when

```text
n>=|U|+t i(U).
```

#### Proof

If the target is a leaf, the source root may have `0,1,...,t` children; every
one of those subtrees is arbitrary because the root-level prefix is gone by
time `t`.  This gives `z S_t(T)`.  If the target has `r>0` children, its source
must have exactly `t+r` children: the first `t` are arbitrary and the remaining
ones independently map in `t` steps to `U_1,...,U_r`.  This is the second
recursion.  Multiplying it over target vertices gives the closed product: each
internal target vertex supplies `T^t`, each leaf supplies `S_t(T)`, and every
target vertex supplies `z`.

The lowest degree is `|U|+t i(U)`.  All coefficients from that degree onward
are positive: for a leaf target the term `zT` already covers every source rank
at least two in addition to the singleton; for an internal target at least one
arbitrary inserted tree factor is present, and its Catalan series has positive
coefficients at every positive degree.  This also proves the exact image
criterion rather than merely a lower bound.

### Mathematical status and gate status

Both contracts are `PROVABLE_AS_STATED`.  They are nevertheless
`KILL_PROOF_ENGINE_TRANSFER`: P148 uses the identical plane-tree carrier and
the same two-step engine---track original coordinates under a local deletion,
then multiply a reversible local inverse recursively over target vertices.
Replacing “depth divisible by `2^t`” by “every address coordinate exceeds `t`”
mechanically yields LCP-A; replacing P148's block-and-gap factor by an arbitrary
prefix factor yields LCP-B.  The change from depth to sibling index is not a
new paper-scale proof architecture.

## 2. `PAE`: parity-agreement extraction

### Literal carrier and rule

On `S_0 disjoint-union ... disjoint-union S_N`, including the empty
permutation, define

```text
A(pi)=std(pi_i : i congruent pi_i (mod 2)).
```

Odd parity is encoded by `1` and even parity by `0` below.

### Contract PAE-A: loss, fixed locus, and sharp clock

For every `pi in S_n`:

1. `n-|A(pi)|` is even.
2. `A(pi)=pi` exactly when every `pi_i` has the parity of `i`; the fixed count
   is `ceil(n/2)! floor(n/2)!`.
3. Every nonfixed update loses at least two letters and
   `max tau=floor(n/2)`.

For sharpness define `E_0=()` and `E_1=21`.  Given `E_(r-1)` at rank `2r-2`:

- if `r` is even, use retained positions `1,...,2r-2`, retained values
  `[2r]` without `{2r-3,2r}`, place them in relative order `E_(r-1)`, and put
  `2r,2r-3` in the last two positions;
- if `r` is odd, use retained positions
  `1,...,2r-4,2r-2,2r-1`, retained values `1,...,2r-2`, place them in relative
  order `E_(r-1)`, and put `2r` at position `2r-3` and `2r-1` at position
  `2r`.

Then `A(E_r)=E_(r-1)`.  At odd rank use `1 direct-sum E_r`.

#### Proof

Let `h_oe` count odd positions carrying even values and `h_eo` count even
positions carrying odd values.  Since the source contains the same numbers of
odd positions and odd values, `h_oe=h_eo=h`; exactly `2h` letters are removed.
Rank is unchanged precisely when `h=0`, which is precisely parity preservation;
then standardization changes nothing.  Odd and even positions may be permuted
independently, giving the fixed count.  Otherwise at least two letters vanish,
so the tail is at most `floor(n/2)`.

For the recursive witnesses use the following slightly stronger induction
invariant.  For even `r>=2`, the only mismatches of `E_r` are its final two
positions, which carry values `2r` and `2r-3`.  For odd `r>=3`, the only
mismatches are positions `2r-3` and `2r`, which carry the two largest values
`2r` and `2r-1`.  The base cases `E_1=21`, `E_2=3241`, and
`E_3=326415` are immediate.

If `r` is even, `E_(r-1)` is in the odd case: its only mismatched entries are
its two largest values.  Embedding its value ranks into `[2r]` without
`{2r-3,2r}` preserves the parity of every other rank and reverses the parity
of precisely those two largest ranks, so all embedded old entries now agree.
The appended entries mismatch and establish the even invariant.  If `r` is
odd, `E_(r-1)` is in the even case: its only mismatched positions are its last
two.  Embedding those position ranks into
`1,...,2r-4,2r-2,2r-1` reverses precisely their parities, so again every old
entry agrees; the two inserted entries mismatch and establish the odd
invariant.  Thus the retained word is always the stated order embedding of
`E_(r-1)`, and `A(E_r)=E_(r-1)`.  Induction gives tail `r`.  Finally, for
even-rank `pi`, direct inspection gives
`A(1 direct-sum pi)=1 direct-sum A(pi)`, proving sharpness at odd rank too.

### Contract PAE-B: sharp target threshold and closed fibres

For a binary word `c=(c_1,...,c_m)` define

```text
ell(c)=m+#{i<m:c_i=c_(i+1)}+1[c_1=0],
C_m={c:#ones(c)=ceil(m/2)}.
```

For `sigma in S_m`, let `sigma^{-1}` act on positions and put

```text
beta_j=c_(sigma^{-1}(j)),
M(sigma)=min_(c in C_m) max(ell(c),ell(beta)),
mu(sigma)=m+2 ceil((M(sigma)-m)/2).
```

Then

```text
sigma in A(S_n)
  iff n>=mu(sigma) and n congruent m (mod 2).
```

This is gap-free in the admissible parity.  Define

```text
E_n(c)=0                                      if n<ell(c),
E_n(c)=binom(m+floor((n-ell(c))/2),m)         otherwise.
```

For `n=m+2h`, the complete target fibre is

```text
|A_n^(-1)(sigma)|
  =(h!)^2 sum_(c in C_m) E_n(c) E_n(c o sigma^(-1)).
```

For the empty target the fibre is zero at odd rank and `(n/2)!^2` at even
rank, including value one at rank zero.

#### Proof

First prove the alternating-host lemma.  The greedy increasing embedding of
`c` starts at `1` for an odd letter and `2` for an even letter, then advances
by one after a parity change and by two after a repeat.  Its last coordinate is
exactly `ell(c)`, proving necessity and sufficiency.  Every other embedding is
uniquely

```text
p_i=q_i+2s_i,    0<=s_1<=...<=s_m<=floor((n-ell(c))/2),
```

where `q` is greedy.  Stars and bars gives `E_n(c)`.

Now suppose a source maps to `sigma`.  Write its selected positions as
`p_1<...<p_m`, its selected values as `a_1<...<a_m`, and let `c_i` be the
parity of `p_i`.  The forced selected assignment is
`p_i -> a_(sigma_i)`, so the value-color word satisfies
`beta_j=c_(sigma^{-1}(j))`.  The unselected positions and values must be
matched across parity.  Balance is possible exactly when `n congruent m`
and `c` has `ceil(m/2)` odd letters.  The two selected sets therefore embed
exactly when `n>=max(ell(c),ell(beta))`; minimizing over `c` and rounding up
to the parity of `m` gives `mu`.

Conversely choose a minimizing color word, take both greedy embeddings, and
match every remaining odd position bijectively to an even value and every
remaining even position to an odd value.  This constructs a source.  Adding
two unused host coordinates preserves the same construction, proving the
gap-free all-rank section.

For the fibre, fix `c`.  There are independently `E_n(c)` selected position
sets and `E_n(beta)` selected value sets.  Their selected assignment is forced
by `sigma`.  Each complement contains `h` positions and values of each cross
parity, giving `h!` bijections in each direction.  Summing the disjoint color
classes proves the formula and all boundary conventions.

### Mathematical status and gate status

Both contracts are `PROVABLE_AS_STATED`; the rank-eight excess profile
`{0:576,2:39012,4:732}` is genuine.  The candidate is nonetheless
`KILL_PERMANENT_SELECTOR_EXTRACTION` and `KILL_PROOF_ENGINE_TRANSFER`.

P156 already proves its target threshold by choosing selected position/value
sets, forcing the assignment through `sigma`, deriving a compatibility
obstruction, constructing a minimum high/low section, and counting complement
matchings.  PAE changes inequalities to two colors but preserves every step.
P155 supplies the same target-dependent minimum-rank scheduler, every-rank
section, and factorially weighted support sum; P149 supplies the selected-word
standardization and iterated section architecture.  The explicit permanent
rule in `phase1/HISTORICAL_OCCUPANCY.md` rejects another selector obtained by
changing parity or standardization.  A later small-rank anomaly cannot override
that literal and proof-engine transfer.

## 3. Verification boundary

Run

```bash
python -B docs/papers157_161_sequence/phase1/combinatorial_gate/verify_collision_gate.py
```

The frozen transcript is `COLLISION_CANONICAL.txt`.  It checks the literal
maps, LCP addresses and inverse coefficients, PAE thresholds, closed fibres,
all-rank sections in bounded lanes, and the sharp PAE witness tower.  It does
not establish novelty, priority, or paper value.
