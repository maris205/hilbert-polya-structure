# WEX provisional theorem contract

**Status:** `SELECT_INTERNAL_PROOF_GATE`; `HOLD_EXTERNAL`; no paper number and no
novelty claim.  This contract may be frozen only after Gate C below has a
complete deductive proof.

## Carrier and literal map

For `N>=1`, the carrier is

```text
P_{<=N}=disjoint_union_{1<=n<=N} S_n.
```

For `pi in S_n`, retain precisely the entries at weak-excedance positions and
standardize:

```text
W(pi)=std(pi_i : pi_i>=i).
```

Write `d(pi)=max_i(i-pi_i)` and let `tau(pi)` be the first hitting time of the
identity at the current rank.  The map never reaches an empty permutation.

## Theorem A — exact all-rank images and right sections

For every `sigma in S_m` and `n>=m`,

```text
sigma in W(S_n) iff n>=m+d(sigma).                         (A1)
```

For every admissible `n`, with `h=n-m`,

```text
R_n(sigma)=(sigma_1+h,...,sigma_m+h,1,...,h)               (A2)
```

is a right section.  Thus the minimum source rank of `sigma` is exactly
`m+d(sigma)`.

**Proof status:** closed.  Necessity is the selected-position/value inequality
`i<=p_i<=a_{sigma_i}<=n-m+sigma_i`; sufficiency is direct substitution in
(A2).

## Theorem B — target-resolved fibres

Let `A={a_1<...<a_m}` and `P={p_1<...<p_m}` range over subsets of `[n]` with
`p_i<=a_{sigma_i}`.  If `B=[n]\A` and
`Q=[n]\P={q_1<...<q_h}`, define

```text
C(B,Q)=prod_{j=1}^h(#{b in B:b<q_j}-(j-1)),               (B1)
```

with value zero if a factor is nonpositive.  Then

```text
|W_n^{-1}(sigma)| = sum_{admissible A,P} C(B,Q).           (B2)
```

**Proof status:** closed.  Selected entries are forced.  Process deficient
positions `q_j` increasingly; every previously used complement value is also
below `q_j`, giving the factor in (B1).  The construction is reversible and
disjoint over `A,P`.

## Theorem C — pointwise Fibonacci clock

With `F_0=0,F_1=1`, the proposed theorem is

```text
tau(pi)>=t  =>  |pi|>=F_{t+2}, d(pi)>=F_{t+1};             (C1)
max_{pi in S_n} tau(pi)=max{t:F_{t+2}<=n}.                (C2)
```

Sharp witnesses start with `w_0=1,w_1=21` and satisfy

```text
w_{t+1}=R_{|w_t|+d(w_t)}(w_t).                            (C3)
```

Consequently

```text
(|w_t|,d(w_t),tau(w_t))=(F_{t+2},F_{t+1},t).              (C4)
```

### Sole proof gate

Prove the following without enumeration:

```text
D=d(pi)  =>  tau(W(pi)) <= M(D),                           (C5)
M(D)=max_{rho in S_D} tau(rho), M(0)=0.
```

The intended construction scans the plot of `pi` through the `D` lower
diagonals, records only changes of the rank-defect frontier, and produces a
permutation skeleton on at most `D` points.  It must provide a semiconjugacy or
layer-surjection from the nonidentity `W`-orbit of `W(pi)` to that skeleton.
Merely restating `M(D)` or choosing a deepest orbit representative is not an
acceptable proof.

Given (C5), simultaneous induction proves (C1): for `q=W(pi)` with
`tau(pi)>=t`, (C5) and the rank induction give `d(pi)>=F_{t+1}`; Theorem A and
the induction hypotheses for `q` give

```text
|pi|>=|q|+d(q)>=F_{t+1}+F_t=F_{t+2}.
```

Equations (C3)–(C4) prove sharpness and (C2).

## Exact falsifiers

The deterministic verifier checks:

1. every state through rank nine for closure, absorption, fixed points,
   monotonicity of maximum drop, (C1), and (C5);
2. (A1) for every target/source rank pair through rank nine;
3. (A2) for every target through rank eight;
4. (B2) for all targets and zero fibres through source rank seven; and
5. the witness recurrence through `w_5` of rank thirteen.

The frozen replay has 3,998,688 assertions across the full fourteen-system
scout.  A passing finite replay never substitutes for the proof of (C5).

## Owner and portfolio firewall

- Excedance-set enumeration, Eulerian distributions, maximum-drop statistics,
  bounded-drop generating functions, and generic rook-board counting are
  subtracted in full.
- P149's endpoint-local peak selector, alternating right section, peak packing,
  and zigzag/pinnacle fibres are subtracted in full.
- Eligible residual: the exact WEX iteration together with C + A + B.
- If C5 fails or cannot be proved cleanly, downgrade to `RESERVE`; A+B alone do
  not justify filling a batch slot.
- A fresh direct-owner audit is mandatory before any paper freeze.
