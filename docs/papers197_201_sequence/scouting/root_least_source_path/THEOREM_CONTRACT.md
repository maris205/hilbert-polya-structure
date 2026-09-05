# Least-source path orientations (LSPO): theorem contract

Status: `PROVISIONAL_PROMOTE / OWNER_RED_AMBER / HOLD_EXTERNAL`.

This is an internal theorem contract, not a novelty or priority claim.  Source-to-sink
clicks, acyclic orientations, exclusion-process language, subset-sum generating
functions, and generic finite-map terminology receive zero contribution credit.

## Literal system

Let `P_n` be the labelled path `1--2--...--n`, with `n>=2`.  A state is an
orientation of every edge.  At each synchronous time choose the least-labelled
source and reverse every edge incident with it.  A source always exists because a
path orientation is acyclic.

Encode edge `i--(i+1)` by a particle at site `i` when it is oriented `i -> i+1`.
Writing a state as `A subseteq [m]`, `m=n-1`, the literal update becomes

```text
Phi(empty) = {m};
Phi(A) = A\{1},                         if min(A)=1;
Phi(A) = (A\{p}) union {p-1},           if p=min(A)>1.       (1)
```

Thus the selected click moves the leftmost particle one site left, removes it at
the left boundary, and injects at the right boundary only when the word is empty.
This conjugacy is a proof device; the orientation rule above is the definition.

## Theorem A: complete pointwise dynamics

For `A={a_1<...<a_k}` put

```text
tau(A)=0                                  if k<=1,
tau(A)=a_1+...+a_(k-1)                    if k>=2.             (2)
```

Then `tau(A)` is the exact entrance time into

```text
C_m={empty,{1},...,{m}}.                                         (3)
```

The restriction to `C_m` is the single `n`-cycle

```text
empty -> {m} -> {m-1} -> ... -> {1} -> empty.                    (4)
```

Consequently `C_m` is exactly the recurrent set, there are no other cycles, and
the sharp global tail is

```text
H_n=binom(n-1,2),                                                 (5)
```

attained uniquely by the all-rightward orientation `A=[m]` for `n>=3`.
For `n=1,2` every state is already recurrent and the maximum tail is zero.

More precisely, set `S_j=a_1+...+a_j` and `S_0=0`.  If
`S_(j-1)<=t<S_j` before entrance, then

```text
Phi^t(A)={a_j-(t-S_(j-1)),a_(j+1),...,a_k}.                       (6)
```

After time `tau(A)`, equation (4) gives every later iterate.  Equations (2),
(4), and (6) are a complete orbit algorithm, not only a height bound.

The complete depth polynomial is

```text
H_m(u)=1+sum_(r=1)^m product_(i=1)^(r-1) (1+u^i).                (7)
```

Its coefficient of `u^d` is the number of states of exact tail `d`.

## Theorem B: every-time labelled inverse atlas

Let `q_s(e)=[u^e] product_(i=1)^s(1+u^i)`, with `q_s(e)=0` outside
`0<=e<=s(s+1)/2`.

If the target `B={b_1<...<b_l}` has at least two particles, then for every
`t>=0`

```text
|Phi^(-t)(B)| = sum_(r=0)^(b_2-b_1-1) q_(b_1+r-1)(t-r).          (8)
```

Indeed a predecessor consists uniquely of a removed subset
`R subseteq [b_1+r-1]` of sum `t-r`, the currently moving particle
`b_1+r`, and the unchanged suffix `b_2,...,b_l`.

Index the core by `c_0=empty` and `c_s={s}` for `1<=s<=m`.  For a core target,

```text
|Phi^(-t)(c_s)| = 1
 + sum_(r=1)^m sum_(e=1)^t q_(r-1)(e)
       1{s == r+e-t (mod n)}.                                   (9)
```

The first term is the unique core ancestor.  The remaining terms count
transient states with rightmost particle `r`, entrance time `e`, and the
required phase.  Equations (8)--(9) cover every target, every time, and all
zero fibres.

At one step, for `m>=2`, the fibre histogram is especially rigid:

```text
number of 0-fibres = 2^(m-2),
number of 1-fibres = 2^(m-1),
number of 2-fibres = 2^(m-2).                                   (10)
```

Equivalently the image has size `3*2^(m-2)` and maximum indegree two.  The
nonimages are exactly the states containing both sites 1 and 2.  For `m=1`
the map is the two-cycle and both fibres have size one.

## Proof split and claim boundary

The temporal proof is a queue argument: until only the rightmost particle
remains, the least particle alone moves and consumes exactly its site label in
time.  The inverse proof reconstructs the already-consumed strict subset and is
independent of the queue clock except for its exact timestamp.

The internal closest neighbour is P145, which studies a *random* uniformly
chosen vertex push on a push orbit and identifies a folded-hypercube Markov
kernel.  LSPO is a deterministic state-dependent source scheduler on all path
orientations; its triangular subset-sum clock and target-resolved inverse atlas
are not consequences of P145's spectrum.  That separation is internal only.

Promotion requires a hostile check against deterministic source-to-sink click
literature and against P145.  A direct owner for the literal least-source path
map or a transfer of (2) and (8)--(9) from an occupied internal system changes
the disposition to `KILL`.
