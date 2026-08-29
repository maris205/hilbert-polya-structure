# Paper plan

## Positioning

The paper is a compact theorem note about a finite dynamical system on
integer partitions. It has one main theorem: exact first-gap growth and the
resulting sharp depth. All one-step material is explicitly subtracted, and
all other temporal statements are labelled low-credit corollaries. External
novelty, priority, and dissemination remain **HOLD**; a bounded negative
owner search is not evidence of originality.

## State space and map

For `lambda` in `P(n)`, let `d` be its Durfee size and let

```text
alpha_i = lambda_i - i,
beta_i  = lambda'_i - i,
h_i     = alpha_i + beta_i + 1.
```

The map is `H(lambda)=(h_1,...,h_d)`. The principal hooks partition the
Ferrers diagram, so `H` preserves `n`; strict Frobenius arms and legs imply
adjacent gaps at least two.

## Theorem contracts

### Contract 0 — itemized owner inputs, zero credit

- The principal-hook length partition `hl(lambda)` and
  `hl_1(lambda)=lambda_1+ell(lambda)-1` are directly owned by Gutschwager.
- `im(H)={h : h_i-h_{i+1}>=2}`.
- `#H^{-1}(h)=h_r product_{i<r}(h_i-h_{i+1}-1)`.
- Empty product convention: one.
- Proof route: split every prescribed hook length into strict Frobenius arms
  and legs.
- The image/fibre product is directly owned by Goupil.
- Chern--Yee directly precede this note on diagonal-hook data and an
  involution preserving every diagonal-hook length; standard one-step
  diagonal-hook symmetries receive zero credit.
- Andrews supplies standard partition/Frobenius background.

### Contract 1 — global absorption, low-credit corollary

- `(H lambda)_1=lambda_1+ell(lambda)-1`.
- This is strictly larger than `lambda_1` off `(n)`.
- Define a globally absorbing fixed point to mean a fixed point reached in
  finite time from every state.
- `(n)` is globally absorbing and is the unique fixed and periodic point.
- The displayed identity is owned; only the immediate finite-dynamical
  deduction is retained, explicitly at low credit.

### Main Contract 2 — exact gap increment

Set `g(lambda)=lambda_1-lambda_2`, padding `lambda_2=0`, and let `m_1`
count parts equal to one.

- If `d>=2`,
  `g(H lambda)-g(lambda)=ell(lambda)-lambda'_2+2=2+m_1(lambda)>=2`.
- If `d=1` and `lambda` is nonterminal, then
  `lambda=(a,1^b)`, `H(lambda)=(n)`, and the increment is `b+1>=2`.
- Proof route: subtract the first two principal-hook lengths.

### Main Contract 3 — sharp depth

- `tau(lambda)<=floor((n-g(lambda))/2)<=floor(n/2)`.
- For `n>=2`, if `b=floor(n/2)`, the balanced two-row partition uses
  `(a,b)->(a+1,b-1)` exactly `b-1` times (zero when `b=1`), followed by the
  final hook step `(n-1,1)->(n)`; its total depth is `b`.
- Therefore the global maximum is exactly `floor(n/2)`.
- Boundaries: at `n=1`, `(1)` is already terminal and the maximum is zero;
  `n=2` has layers of sizes one and one.

### Contract 4 — layer transport, low-credit corollary

For `A_t(n)=#{lambda:tau(lambda)=t}`:

- `A_0(n)=1`.
- `A_1(n)=n-1`.
- for `t>=2`, sum the owned fibre weight over gap partitions `h` of
  depth `t-1`.
- Empty sums are zero; layers vanish above `floor(n/2)`.
- This is a state/depth-weighted transport identity over first images, not a
  closed scalar recurrence in `(n,t)` or in `A_t(n)` alone.

### Contract 5 — conjugation and fixed-weight zeta, low-credit corollaries

- Conjugation swaps Frobenius arms and legs, hence
  `H(lambda)=H(lambda')` and all positive-time images agree.
- Depths agree unless `n>1` and the pair is `(n),(1^n)`; those depths are
  zero and one.
- For each fixed `n>=1`, `#Fix(H_n^m)=1` for every `m>=1`.
- `zeta_{H_n}(z)=exp(sum_m #Fix(H_n^m)z^m/m)=(1-z)^(-1)`.
- No zeta function on the disjoint union of all weights is asserted.

## Two independent proof routes

1. **Frobenius/fibre route:** strict arm/leg splittings verify the owned
   one-step image and fibre formula; this route receives zero credit.
2. **Ferrers/gap route:** direct subtraction of the first two hooks proves
   the sole main theorem, exact gap growth and sharp depth. The first-hook
   identity itself is owned; its absorption consequence is low credit.

The layer transport is the only statement that joins the routes, and it is
explicitly low credit and nonclosed.

## Section architecture

1. Introduction, ownership subtraction, and P110 firewall.
2. Definitions and itemized zero-credit one-step owners.
3. Defined global absorption plus the exact-gap/sharp-depth main theorem.
4. Low-credit layer transport, conjugation timing, periodic points, and
   fixed-weight zeta.
5. Proof-route separation and killed-overclaim controls.

## Scope exclusions

- No claim of novelty for the one-step image or fibre formula.
- No claim of novelty for the principal-hook partition, first-hook identity,
  standard diagonal-hook setup, or standard one-step symmetries.
- No use of an undefined “attractor”; only the defined globally absorbing
  fixed-point property is asserted.
- No claim that the layer identity is a closed scalar recurrence.
- No all-weights interpretation of the zeta function.
- No complete classification of deepest states.
- No claim that `H` is idempotent.
- No unconditional claim that depth is conjugation-invariant.
- No transfer of P110's labelled lattice-join engine.
