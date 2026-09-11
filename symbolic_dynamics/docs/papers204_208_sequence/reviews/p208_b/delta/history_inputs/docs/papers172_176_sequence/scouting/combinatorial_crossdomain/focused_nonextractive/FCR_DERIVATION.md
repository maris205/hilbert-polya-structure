# First-frequency rotation: exact derivation and strict value gate

**Lifecycle:** `HOLD_EXTERNAL`.  This is a scouting theorem package, not a
paper allocation and not a novelty or priority statement.

## 1. Literal finite system

Let `R` be left rotation on a binary word and put

```text
m_a(w) = #{i : w_i=a},
T_n(w) = R^(m_(w_0)(w)) w,            w in {0,1}^n.
```

Thus the amount moved is the global multiplicity of the symbol currently at
the pointer.  Length and content are preserved.  No letter is extracted or
pruned and no parity-linear update is present.

Write `k=|w|_1`.  The two local branches are

```text
w_0=1: T_n(w)=R^k w,
w_0=0: T_n(w)=R^(n-k)w=R^(-k)w.
```

The second equality is an equality of rotations of an `n`-letter word.

## 2. Pointed-necklace reduction

Fix a cyclic word `u` and let `d|n` be its least rotational period.  Its `d`
distinct pointed states are `R^j u`, indexed by `j in Z/dZ`.  Because `d|n`,
the literal map is conjugate on this class to

```text
phi_u(j) = j+k   if u_j=1,
           j-k   if u_j=0.                         (2.1)
```

Put `h=gcd(k,d)` and `L=d/h`.  The undirected `+/-k` Cayley graph on
`Z/dZ` is the disjoint union of `h` cycles of length `L`.  Order each such
component by `j,j+k,...`.  A `1` points forward and a `0` points backward.
This elementary orientation gives the complete component dynamics.

- If `L=1`, every component vertex is fixed.
- If `L=2`, forward and backward have the same neighbour, so every component
  is one directed two-cycle.
- If `L>=3` and the component word is constant, it is one directed `L`-cycle.
- If `L>=3` and the component word is nonconstant, its recurrent edges are
  exactly the cyclic occurrences `10`; each is a two-cycle.  Every other
  vertex flows into one of them.  The component's maximum tail is one less
  than its longest cyclic constant run.

The last statement follows by inspecting a maximal block.  Every `1` walks
forward to the block's final `1`, every following `0` walks backward to that
same `10` edge, and the two boundary vertices exchange.  No cycle of length
at least three can turn direction, so the list is exhaustive.

This is both a pointwise algorithm and an all-parameter proof: factor a
pointed necklace into its `gcd(k,d)` generator cycles, read their constant
runs, and recover every tail, recurrent component, and period without
iterating the word map.

## 3. Complete possible-period inventory

For `n=1`, the possible period set is `{1}`.  For every `n>=2`, it is

```text
{1,2} union {ell : ell|n and 3<=ell<n}.             (3.1)
```

The upper bound follows from Section 2.  A long cycle has length
`L=d/gcd(k,d)`, hence divides `n`.  If `L=n`, then `d=n` and `gcd(k,n)=1`;
the one generator component could be uniformly oriented only if the word
were constant, contradicting `d=n>1`.  Thus every long period is a proper
divisor.

Constants realize period one, and the necklace with one `1` realizes a
two-cycle.  Conversely, fix a proper divisor `L>=3` and put `g=n/L>=2`.
Use an `n`-word of weight `g` whose support is

```text
{0,1,...,g-2,g}.
```

Its unique largest cyclic zero gap makes it aperiodic.  Under the generator
`k=g`, residue class `g-1 mod g` is all zero, so that component is a directed
`L`-cycle.  This realizes every entry of (3.1).

## 4. Sharp clock and deepest states

The exact global maximum preperiod is

```text
H_1=0,                 H_n=n-2 for n>=2.            (4.1)
```

Indeed, a nonconstant generator component of length `L` has no constant run
longer than `L-1`, so its tail is at most `L-2`.  Constant components are
recurrent.  Since `L<=n`, this proves the bound.  For `n>=3`, the word

```text
010^(n-2)
```

has weight one and follows a zero run of length `n-1` into the unique
two-cycle, taking `n-2` steps.  Its complement gives a second witness.

There are exactly two deepest states for every `n>=3`.  Equality in the
bound forces `L=n` and a constant run of length `n-1`, hence exactly one
minority letter.  In each of the two resulting necklaces there is exactly
one pointer farthest from the recurrent `10` edge: the displayed word and
its complement.  At the small boundaries all two states are deepest for
`n=1`, and all four are deepest for `n=2`, because the maximum tail is zero.

## 5. Every-target labelled fibres

Let `y` have weight `k`.  If `k=0` or `k=n`, its only source is itself.  If
`0<k<n`, there are at most two sources and they are completely labelled by
their first bit:

```text
x_1 = R^(-k)y       exists iff y_(-k)=1,
x_0 = R^(-(n-k))y   exists iff y_k=0.               (5.1)
```

Necessity comes by undoing the forced rotation on the selected branch;
sufficiency is immediate.  The sources are distinct because their first bits
differ.  Thus (5.1) is simultaneously an every-target image test and the
complete predecessor list.

It also gives a closed fibre distribution.  For a fixed nonconstant weight
`k`, the two inspected target positions coincide exactly when `n|2k`.  In
that case every target has fibre one.  Otherwise, within that weight layer,

```text
N_0(n,k)=N_2(n,k)=C(n-2,k-1),
N_1(n,k)=C(n,k)-2C(n-2,k-1).                         (5.2)
```

Add the two constant targets to `N_1`.  In particular every fibre is
`0`, `1`, or `2`, and

```text
|Im T_n| = 2 + sum_(k=1)^(n-1)
  [ C(n,k) - 1_(n does not divide 2k) C(n-2,k-1) ]. (5.3)
```

This inverse axis is independent of the forward generator-component proof.

## 6. Fixed-point Möbius census

For a word of least period `d`, `T_n(w)=w` iff `d` divides the multiplicity
of its first symbol.  Since `d|n`, in the binary case this is simply `d|k`
and is independent of the pointer.  Let

```text
A(d,j)=sum_(e|gcd(d,j)) mu(e) C(d/e,j/e)
```

be the number of linear binary words of least period `d` and weight `j`.
Writing the full word as `n/d` repeats of that primitive block gives

```text
Fix(n) = sum_(d|n) sum_(j=0)^d
         1_(d divides (n/d)j) A(d,j).                (6.1)
```

This is a supporting static census.  Primitive-word/necklace enumeration and
Möbius inversion receive zero contribution credit.

## 7. Exact control and claim ceiling

`verify_fcr.py` independently enumerates every binary word through `n=18`.
It checks the literal successor, content preservation, every target in
(5.1), the full histogram (5.2), every pointed-necklace conjugacy (2.1),
every component tail and recurrent cycle, (3.1), (4.1), the deepest-state
census, and (6.1).  The canonical transcript reports `2,828,503` assertions.

The mathematical package is real, but value is controlled by the internal
gate in `COLLISION_FIREWALL.md`: P166 already reduces its different literal
system to the same phase-map architecture `j -> j+c_j` and also has a sharp
`n-2` clock plus target-indicator inverse theorem.  Ordinary coordinate-
rotation sources also own the fixed-weight necklace/class structure behind
the two frozen branches.  Those ingredients receive zero contribution
credit; Høyer--Špalek's separate quantum phase rotation is not treated as a
literal owner of either coordinate branch.  The portfolio ruling retains only the
facts not implied by P166's mass-exhaustion theorem: the `+/-k` Cayley-cycle
decomposition, multiple recurrent components, proper-divisor-plus-two period
inventory, binary `0/1/2` labelled fibres, and fixed census.  The status is

```text
AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL
```

This is not green and is never a novelty claim.  A direct owner, a literal
conjugacy into P166, or a proof showing that the residual component theorem
is merely a specialization of P166 immediately changes the status to
`KILL_INTERNAL_P166_PHASE_MAP`.
