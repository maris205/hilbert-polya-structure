# Proof spike: synchronous balanced refinement of compositions

Status: **PROVED / OWNER-VALUE GATE REQUIRED / EXTERNAL HOLD**.

## 1. Literal system

For an integer composition `a=(a_1,...,a_k)` of `n`, replace every part
`m>=2` simultaneously by

```text
(floor(m/2), ceil(m/2)),
```

and retain every part `1`.  Denote the resulting composition by `Phi(a)`.
The map is a substitution on the free monoid of positive integers: it acts
independently on letters and respects concatenation.

Weight is preserved.  Every changed part becomes two positive parts, so word
length increases strictly until the unique fixed composition `1^n` is
reached.  Thus there are no nontrivial cycles and every state lies in one
basin.

## 2. Exact pointwise and global clock

After `t` rounds, the largest descendant of a single part `m` is

```text
ceil(m/2^t).
```

This follows inductively from balanced halving.  Hence

```text
depth(a)=max_i ceil(log_2 a_i),
max_{a composition of n} depth(a)=ceil(log_2 n),
```

with the global maximum attained by the one-part composition `(n)`.

Generic balanced binary splitting and this logarithmic divide-and-conquer
clock are background mechanisms, not by themselves paper-scale contribution.

## 3. Codewords and every iterated fibre

Let `W_t(m)=Phi^t((m))`.  Then

```text
W_0(m)=(m),
W_(t+1)(1)=(1),
W_(t+1)(m)=W_t(floor(m/2)) W_t(ceil(m/2))  for m>=2.
```

Because `Phi` is a monoid substitution, a source composition
`(m_1,...,m_r)` maps after `t` rounds to the concatenation
`W_t(m_1)...W_t(m_r)`.  Therefore the complete fibre over a target word is
in bijection with its factorizations into codewords `W_t(m)`.  The source is
recovered by replacing each factor by its weight, so there is no multiplicity
or unique-decoding assumption hidden in the statement.

For a target `a_1...a_k`, let `H_0=1` and

```text
H_j = sum_{0<=i<j} H_i * 1[(a_(i+1),...,a_j)=W_t(a_(i+1)+...+a_j)].
```

Since every codeword has length at most `2^t`, the sum needs only the last
`2^t` cut positions.  Then

```text
|Phi^{-t}(a)|=H_k,
```

and the target lies in the `t`-step image iff `H_k>0`.  This is an exact
pointwise all-iterate fibre/image algorithm.

For `t=1`, the codewords are `(1)`, `(r,r)`, and `(r,r+1)`.  Thus the DP
specializes to tilings by the monomer `(1)` and the compatible dimers
`(r,r)` or `(r,r+1)`.

## 4. Exact maximum iterated fibre

Put `K=2^t` and define the `K`-step Fibonacci numbers by

```text
F_K(0)=1,
F_K(n)=sum_{ell=1}^{min(K,n)} F_K(n-ell).
```

In any codeword factorization of a target prefix, the final factor has length
at most `K`.  For each possible length there is at most one source letter,
because that letter must equal the factor weight.  Induction in the preceding
DP gives

```text
|Phi^{-t}(a)| <= F_K(length(a)) <= F_K(n).
```

For the all-one target `1^n`, every segment of length `ell<=K` is exactly
`W_t(ell)`, because `ell` fully splits within `t` rounds.  Every inequality is
therefore equality:

```text
max_{a composition of n} |Phi^{-t}(a)| = F_(2^t)(n),
```

attained by `1^n`.  At `t=1` this is the ordinary Fibonacci number
`F_{n+1}` under the convention `F_0=0,F_1=1`.

## 5. Aggregate one-step image and Garden recurrence

For a target prefix define the Boolean parsing recurrence

```text
d_0=1,
d_j = (d_(j-1) and a_j=1)
      or (d_(j-2) and a_j in {a_(j-1),a_(j-1)+1}).
```

To aggregate without listing compositions, after a nonempty prefix retain
`(last,d_(j-1),d_j)` together with its total weight.  Initialization by a
first part `r` gives `(r,1,[r=1])`.  Appending `s` sends

```text
(r,p,q) -> (s,q, (q and s=1) or (p and s in {r,r+1})).
```

Summing states with final bit one gives the one-step image number `I_n` for
every `n`; the Garden count is `2^(n-1)-I_n` for `n>=1`, with the empty
composition handled separately.  This is an explicit all-size arithmetic
recurrence; minimality and a closed rational OGF are not claimed.

## 6. Owner and value ceiling

A bounded exact-map search found standard divide-and-conquer balanced
splitting, substitutions and composition enumeration, but no source stating
this literal self-map together with all iterated codeword fibres, exact
maximum fibres and the aggregate image recurrence.  That is only a bounded
non-hit.  An independent gate must inspect rewriting-system, morphism,
fragmentation and composition-pattern sources and subtract any direct engine.

The residual claim, if it survives, is the conjunction of all-iterate
codeword factorization, exact `2^t`-step-Fibonacci maximum fibres, and the
aggregate image automaton.  No novelty, priority, asymptotic, minimal-state or
external-release claim is allowed.
