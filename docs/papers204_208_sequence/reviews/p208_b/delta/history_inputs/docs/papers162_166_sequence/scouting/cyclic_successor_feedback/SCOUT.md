# Cyclic successor-feedback: exact scout and strict value gate

**Handle:** `CSF`  
**Decision:** `KILL_DIRECT_ECA_TAIL_AND_BATCH_COLLISION`  
**Mathematics:** `PASS_EXACT`  
**Paper allocation:** none  
**External status:** `HOLD_EXTERNAL`

## Outcome first

For `n,q>=3`, let `X_(n,q)=(Z/qZ)^n` and define

```text
T_q(w)_i = 1{w_(i+1)=w_i+1 mod q},       i in Z/nZ.       (1)
```

The candidate is exactly soluble.  Its full functional graph has height two;
its stable image is the set of cyclic binary independent sets, on which the
map is rotation.  The one-step mask fibres, all positive-time target fibres,
the full depth census, every rooted transient cell, all periods, and the zeta
function all have closed formulas.  No counterexample was found in the
independent exhaustive audit.

It nevertheless fails the strict paper gate.  On binary states its local rule
is

```text
U(b)_i=(1-b_i)b_(i+1),                                      (2)
```

which is standard Wolfram elementary cellular automaton Rule 34 (the same
two-input truth table is sometimes called Rule 2 when the unused left input
is omitted).  The direct CA literature already records that this rule enters
a forbidden-adjacency subshift after one step and is a shift there.  Thus the
entire temporal/recurrent axis is owned.  Lucas hard-core counts, constrained
necklaces, transfer matrices, and Möbius orbit extraction are also classical.
After those deductions and the same-batch CEF architecture are subtracted,
the q-ary front and cyclic-gap weighted fibre are clean but too closely tied
to one elementary transfer/character-sum mechanism to constitute two
independent residual theorem axes.

This is a value/portfolio kill, not a mathematical failure and not a claim
that the exact q-ary conjunction has a direct owner.

## 1. First step: the complete q-ary mask fibre

For a binary target `b`, write `r=|b|`, `m=n-r`, and

```text
epsilon_(n,q) = q-1,  if q divides n,
                -1,  otherwise.
```

Then the exact one-step source count is

```text
K_(n,q)(r)=(q-1)^(n-r)+epsilon_(n,q)(-1)^(n-r).             (3)
```

Every nonbinary target has zero sources at positive time.

### Proof of (3)

Set `d_i=w_(i+1)-w_i mod q`.  A word maps to `b` precisely when
`d_i=1` at every one of `b` and `d_i!=1` at every zero, subject to the
single cyclic constraint `sum_i d_i=0`.  Once such a difference word is
chosen, `w_0` has `q` choices.

Apply additive-character orthogonality to the difference sum.  The trivial
character contributes `(q-1)^m`.  For a nontrivial character `chi`,

```text
sum_(a!=1) chi(a) = -chi(1),
```

so its contribution is `(-1)^m chi(1)^n`.  The sum of `chi(1)^n` over the
nontrivial characters is `q-1` when `q|n` and `-1` otherwise.  The factor
`1/q` from orthogonality cancels the `q` choices of `w_0`, proving (3) for
arbitrary, not necessarily prime, `q`.

Because `q-1>=2`, (3) has exactly the following zeros:

```text
q divides n:      K(r)=0 iff r=n-1;
q does not divide n: K(r)=0 iff r=n.
```

Therefore

```text
|im T_q| = 2^n-n,  if q divides n,
           2^n-1,  otherwise.                              (4)
```

The edge cases in (4) are real: when `q|n`, the all-one mask is supported
with fibre `q`, but each mask with one zero is absent; when `q` does not
divide `n`, the all-one mask alone is absent.

## 2. Binary tail and stable image

For binary `b`, (1) reduces directly to (2).  Two adjacent coordinates of
`U(b)` cannot both be one, because the first would require `b_(i+1)=1` and
the second would require `b_(i+1)=0`.  Thus

```text
U({0,1}^n) subset I_n,
I_n={c in {0,1}^n : c_i c_(i+1)=0 for every i}.             (5)
```

Let `sigma(c)_i=c_(i+1)`.  If `c in I_n`, then

```text
U(c)_i=(1-c_i)c_(i+1)=c_(i+1),
U(c)=sigma(c).                                               (6)
```

Every `c in I_n` has a binary `U`-preimage.  The zero word has the two
preimages `0^n,1^n`; the nonzero case is counted explicitly in Section 3.
At least one of these binary preimages also belongs to `im T_q`:

- if `q` does not divide `n`, the only unsupported mask is `1^n`, which is
  not a preimage of nonzero `c`, while `0^n` handles `c=0`;
- if `q|n`, the only unsupported weights are `n-1`; a target with at least
  two ones has preimages of weight at most `n-2`, and a singleton target has
  preimages of every weight `1,...,n-1`, so a weight-one choice survives.

Consequently

```text
im T_q^2 = I_n,
im T_q^t = I_n for every t>=2,
T_q^t(w)=sigma^(t-2)(T_q^2(w)) for every t>=2.              (7)
```

There are no transient cycles.  The recurrent part is exactly rotation on
`I_n`.

## 3. Cyclic-gap inverse polynomial

Let `c` be a nonzero member of `I_n`, with `k=|c|`.  Read cyclically from
one `1` of `c` to the next and let the successive gaps be

```text
ell_1,...,ell_k >= 2,       sum_j ell_j=n.                  (8)
```

For each gap, a binary source `b` satisfying `U(b)=c` has a positive run of
ones of some length `j in {1,...,ell-1}` immediately before the forced
`0,1` transition that creates the next target one.  The choices in distinct
gaps are independent.  Hence

```text
P_c(x)=product_(j=1)^k (x+x^2+...+x^(ell_j-1)),             (9)
[x^r]P_c(x)=#{b in {0,1}^n: U(b)=c, |b|=r}.                (10)
```

In particular,

```text
P_c(1)=product_j(ell_j-1),
P_c(-1)=(-1)^k if every ell_j is even, and 0 otherwise.     (11)
```

For `c=0`, the separate source enumerator is `1+x^n`.

Combining (3) and (10) gives the exact q-ary two-step fibre.  For nonzero
`c in I_n`,

```text
F_(n,q)(c)
 = (q-1)^n P_c(1/(q-1))
   +epsilon_(n,q)(-1)^n P_c(-1).                           (12)
```

The first term in (12) is an integer when expanded as
`sum_r [x^r]P_c(x)(q-1)^(n-r)`.  At the zero target,

```text
F_(n,q)(0)
 = K_(n,q)(0)+K_(n,q)(n)
 = (q-1)^n+1+epsilon_(n,q)((-1)^n+1).                      (13)
```

The gap multiset, and therefore `F`, is rotation invariant.  Equations
(7), (12), and (13) give the complete time-target atlas:

```text
t=0: identity fibres, one at every q-ary target;
t=1: K_(n,q)(|b|) for binary b, zero for nonbinary targets;
t>=2: F_(n,q)(c) for c in I_n, zero otherwise.              (14)
```

Although the target at time `t` is reached through a rotation by `t-2`, its
fibre cardinality is the same value in (12).  The mass identities are

```text
sum_(b in {0,1}^n) K_(n,q)(|b|)=q^n,
sum_(c in I_n) F_(n,q)(c)=q^n.                             (15)
```

### Exact examples

```text
n=6, c=100100, gaps=(3,3),
P_c(x)=x^2+2x^3+x^4,       F(c)=(36,144,400) at q=(3,4,5).

n=7, c=1010000, gaps=(2,5),
P_c(x)=x^2+x^3+x^4+x^5,    F(c)=(60,360,1360).

n=8, c=10001000, gaps=(4,4),
P_c(x)=x^2+2x^3+3x^4+2x^5+x^6,
F(c)=(195,1524,7055).
```

The even-gap correction is visible in the first and third examples; it is
zero for the mixed-parity gap example at `n=7`.

## 4. Exact depths and the sharp shell

Let

```text
A_n(x)=sum_(r=0)^floor(n/2) a_(n,r)x^r,
a_(n,r)=n/(n-r) binom(n-r,r).                              (16)
```

This is the independence polynomial of the labelled cycle.  Its total is
the Lucas number

```text
|I_n|=A_n(1)=L_n=F_(n-1)+F_(n+1),                          (17)
```

and, from the two roots of `lambda^2=lambda+x`,

```text
A_n(-1)=2 cos(n pi/3).                                     (18)
```

A state has depth zero precisely when it lies in `I_n`.  It has depth at
most one precisely when its first image lies in `I_n`.  Therefore, with
`a=q-1`,

```text
C_1(n,q)
 := #{w: depth(w)<=1}
 = a^n A_n(1/a)+epsilon_(n,q)(-1)^n A_n(-1).               (19)
```

The complete depth histogram is

```text
D_0=L_n,
D_1=C_1(n,q)-L_n,
D_2=q^n-C_1(n,q).                                          (20)
```

The height is exactly two for every `n,q>=3`.  If `q|n`, the supported
non-independent mask `1^n` witnesses depth two.  If `q` does not divide
`n`, the supported mask `110^(n-2)` does so.  Formula (7) supplies the upper
bound.

## 5. Complete labelled functional graph

The preceding formulas determine not only aggregate depths but every
component.  For `c in I_n`, put `k=|c|` and

```text
B(c)=2,                         if c=0,
B(c)=P_c(1),                    otherwise.                  (21)
```

The core vertex `c` has `K_(n,q)(k)` immediate predecessors.  Exactly one,
`sigma^(-1)c`, lies on its recurrent rotation cycle.  Of the remaining
immediate predecessors,

```text
B(c)-1                    are binary depth-one states,
K_(n,q)(k)-B(c)           are nonbinary depth-one states.   (22)
```

Every binary transient child `b` in (22) is non-independent.  It has
`K_(n,q)(|b|)` predecessors, all nonbinary depth-two leaves, because the
image of a binary word under `U` is always independent.  Summing over those
children gives

```text
number of depth-two leaves rooted at c = F_(n,q)(c)-K_(n,q)(k).   (23)
```

More finely, for a nonzero target the number of binary transient children of
weight `r` is

```text
[x^r]P_c(x)-1{r=k};
```

each such child has exactly `K_(n,q)(r)` incoming leaves.  For the zero target
the same statement uses `1+x^n` in place of `P_c`.  Hence the individual
branch-degree multiset, not merely its total, is fixed by the displayed data.

Thus the rooted cell attached to `c`, after cutting its incoming cycle edge,
has shell sizes

```text
(depth 0, depth 1, depth 2)
= (1, K_(n,q)(k)-1, F_(n,q)(c)-K_(n,q)(k)),                (24)
```

and total size `F_(n,q)(c)`.  If the rotation orbit of `c` has length `d`,
the whole connected component has shell sizes `d` times (24) and total size
`d F_(n,q)(c)`.  Equations (8)--(13) therefore classify every component by
its cyclic gap word.

## 6. Periods and finite-map zeta function

A configuration fixed by `T_q^m` must be recurrent and hence belongs to
`I_n`.  On `I_n`, the map is `sigma`.  A word fixed by `sigma^m` repeats a
cyclic independent word of length `gcd(n,m)`, so

```text
Fix(T_q^m)=L_gcd(n,m),                 m>=1.                (25)
```

In particular, `0^n` is the unique fixed point.  For each `d|n`, let

```text
p_d=sum_(e|d) mu(d/e)L_e.                                  (26)
```

Then `p_d` is the number of points of exact period `d`, and there are
`p_d/d` recurrent cycles of that length.  The Artin--Mazur zeta function of
the full finite map is

```text
zeta_T(z)=product_(d|n) (1-z^d)^(-p_d/d).                  (27)
```

The transient trees do not affect (25)--(27).

The abstract labelled functional graph also identifies the parameters: its
recurrent-state count is the strictly increasing `L_n`, which recovers
`n>=3`; its total vertex count `q^n` then recovers `q`.  This is correct but
receives no rescue credit because it is an immediate size consequence of the
already classified core.

## 7. Boundary pressure

| boundary | exact disposition |
|---|---|
| `t=0` | The carrier is q-ary and every target fibre is one.  It is not covered by positive-time binary support statements. |
| `t=1` | Formula (3) applies to all binary targets; all nonbinary targets have fibre zero. |
| `t>=2` | Support is exactly `I_n`; target counts are time-independent because the tail is a rotation. |
| `c=0` | Must use (13), not the nonzero gap product.  Its two binary predecessors are `0^n` and `1^n`. |
| singleton `c` | Its sole gap is `ell=n`, not zero; `P_c=x+...+x^(n-1)`. |
| `q|n` | Exactly the weight-`n-1` masks are absent at time one.  The all-one mask has fibre `q`. |
| `q` not dividing `n` | Only the all-one mask is absent at time one. |
| `q=2` | Excluded essentially: at `n=4`, the time-one image has 8 states, not the `q>=3` prediction 12. |
| `n=2` | Excluded as a doubled-neighbour cycle convention; some displayed identities happen to persist, but none are claimed. |

## 8. Independent exact evidence

Run

```bash
python3 docs/papers162_166_sequence/scouting/cyclic_successor_feedback/verify_scout.py
```

The verifier imports no author or repository code.  It directly enumerates
the literal map and checks:

- 26 boxes with `3<=n<=9`, `3<=q<=7`, totaling 407,640 q-ary states;
- the first mask identity, exact support holes, and every binary target fibre;
- the Rule-34 identity, stable image, time `2,3,4,n+2` target fibres;
- exact depth CDF and a sharp depth-two witness in every box;
- every root's binary/nonbinary depth-one children and depth-two leaves;
- every recurrent orbit, component mass, exact-period count, and fixed count;
- every coefficient of every cyclic-gap polynomial through `n=15`, covering
  all `2^n` binary masks at each length;
- four mixed gap profiles and the excluded `q=2,n=2` sentinels.

Receipt:

```text
assertions             2,139,057
literal states         407,640
verifier SHA-256       bf4b014815cf9509ba1d6f65319eaff5610d90863bb7641f87765a6eda135ac2
canonical SHA-256      6405e171739b7e0e1bdb6d26fa71e5d6d720504b36618ec479b5235911a9ba98
fresh replay 1         byte-match
fresh replay 2         byte-match
py_compile             PASS
math status            PASS_EXACT
```

## 9. Strict gate

### What is mathematically substantial

The conjunction (3), (12)--(14), and (21)--(24) is an unusually complete
finite functional-graph calculation.  The weighted cyclic-gap inverse formula
is target-resolved, includes the `q|n` Fourier correction, and is stronger
than an aggregate preimage count.

### What receives zero contribution credit

1. The entire binary update (2), its one-step forbidden-adjacency image, and
   its shift action there: direct ECA Rule-34 background.
2. The height-two temporal law and recurrent-core characterization: immediate
   corollaries of the preceding owned fact.
3. Lucas independent-set counts, rotation orbits, hard-core necklaces,
   Möbius exact periods, and zeta product: classical constrained-word theory.
4. Character orthogonality and transfer-matrix enumeration of a prescribed
   cyclic edge statistic, plus the product-of-chains/P-partition reading of
   the gap choices: standard technique.
5. The package architecture “q-ary local comparison indicator -> binary CA
   tail -> mask multiplicity -> target-weighted fibres”: already represented
   more strongly by current same-batch CEF, whose tail has a sharp dyadic
   `n+1` nilpotent clock and two evaluated affine target spectra.

### Residual after subtraction

The literal successor front contributes (3)--(4), and its composition with
the gap inverse contributes (12)--(13).  Those are correct, compact, and may
be useful as an example or appendix.  They do not rescue a separate paper:

- the temporal axis is completely predetermined by a named elementary CA;
- the first and second fibre displays are two evaluations of the same local
  edge/difference transfer mechanism rather than independent axes;
- the functional graph, depth shells, periods, and zeta are mechanical
  packaging once Rule 34 and the fibres are known;
- CEF already occupies the batch slot for a q-ary comparison front feeding a
  binary CA, with a longer and less degenerate clock.

## Final decision

```text
CSF       KILL_DIRECT_ECA_TAIL_AND_BATCH_COLLISION
MATH      PASS_EXACT
OWNER     FAIL_VALUE_AFTER_SUBTRACTION
PAPER     DO_NOT_ALLOCATE
EXTERNAL  HOLD_EXTERNAL
```

The formulas may remain as frozen scout evidence, but CSF must not be promoted
to P162--P166 and must not be advertised as novel or externally circulated.
