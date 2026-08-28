# Hostile review — P89

Audit date: 2026-08-28 UTC.

Disposition: **GO for internal theorem-bearing freeze; EXTERNAL HOLD**.

## Independent two-round audit record

### Round 1 — theorem and control attack

The reset factorization, renewal rate, mean-matrix identity, strict Jensen
normalization, and regenerative variance were recalculated independently.
Both control layers were rerun: 66,787 integer/rational assertions and 10
floating diagnostics passed.  The formulas survived, but the CLT proof's
intermediate identity silently measured cycle time from the first reset while
centering by absolute time.  The proof now introduces the initial delay
`tau`, the elapsed renewal clock `S_m`, and a delayed count `J_n`, then removes
the fixed `h tau` term on the `sqrt(n)` scale.

### Round 2 — overstatement, owner, reproduction, and layout attack

The exact matrix identity and model-specific phrases were searched against
the cited primary owner lines; no direct source for the full two-matrix
formula package was found, so collision risk remains medium and external
release remains HOLD.  Definition-level enumeration, exhaustive short-word
factorization, and exact annealed checks reproduced.  Reverse reading found
the TeX typo `\overline M_p^{,n}` in the annealed finite-time identity; it is
now `\overline M_p^{\,n}`.  The six-page PDF was rebuilt and inspected page
by page with zero warnings or box defects.

## Bottom line

The five required theorem components survive direct rederivation:
`E A^k E = F_(k+2) E`, the quenched entropy series, the annealed Perron
exponent, the strict gap, and the renewal CLT with explicit positive
variance.  The model is genuinely regenerative, and the random matrix
boundary is `o(sqrt(n))`; no numerical limit is being promoted to a proof.

The mathematical package is compact but owner-sensitive.  Every general
mechanism is classical, and a close specialization may exist under different
terminology.  The internal result is therefore usable; external release and
priority language remain on HOLD.

## Formula audit

### 1. Reset identity and path-count factorization — PASS

For `k>=1`,

```text
A^k = [[F_(k+1), F_k], [F_k, F_(k-1)]].
```

Left and right multiplication by `E=[[1,1],[0,0]]` gives exactly
`F_(k+2)E`; at `k=0`, this is `E^2=E=F_2 E`.  Consequently every product

```text
A^ell E A^k1 E ... E A^q
```

collapses to the product of the internal Fibonacci gains times
`A^ell E A^q`.  Direct state-path enumeration agrees with the matrix count
for all short environments, and the factorization agrees for every binary
environment through length 15.

### 2. Quenched entropy — PASS

Consecutive reset gaps have

```text
P(K=k)=p(1-p)^k,
L=K+1,
R=log F_(K+2),
E[L]=1/p.
```

Thus the renewal-reward rate is

```text
E[R]/E[L] = p^2 sum_(k>=0) (1-p)^k log F_(k+2).
```

The only matrix-product terms not included in completed cycles are the
initial and terminal boundaries.  A union bound followed by Borel--Cantelli
shows that the longest reset-free run in the first `n` coordinates is
`O(log n)` almost surely.  The boundary path count has logarithm bounded by
that run length times `log 2`, so it is negligible both on the `n` and
`sqrt(n)` scales.

The wording "block meeting the window" in an intermediate draft could have
included an exterior extension not controlled by the displayed union bound.
It was corrected to the longest run inside the finite environment word.

### 3. Annealed exponent — PASS

Successive integration of independent matrix factors gives

```text
E[N_n] = 1^T ((1-p)A+pE)^n 1
```

exactly.  The mean matrix is `[[1,1],[1-p,0]]`, whose characteristic
polynomial is `t^2-t-(1-p)`.  Its Perron root is
`(1+sqrt(5-4p))/2`.  The endpoints are handled directly: `A` has Perron
root the golden ratio, while `E` is idempotent with spectral radius one.

### 4. Strict quenched--annealed gap — PASS

Let `lambda` be the annealed Perron root and set

```text
Z = F_(K+2) / lambda^(K+1).
```

The Fibonacci generating function and `lambda^2=lambda+(1-p)` give
`E[Z]=1` exactly.  The substitution lies strictly inside the generating
function's convergence disk because `(1-p)/lambda=lambda-1<1/phi`.  The
values of `Z` at `K=0` and `K=1` are unequal, so strict Jensen yields

```text
h_q - log(lambda) = p E[log Z] < 0.
```

This supplies a linear-rate strictness mechanism; the proof does not infer a
positive asymptotic gap merely from finite-time Jensen inequalities.

### 5. Renewal CLT and variance — PASS with a named classical input

For the centered cycle reward

```text
W = log F_(K+2) - h_q(K+1),
```

the geometric gap law gives all moments and `E[W]=0`.  The classical
renewal-reward CLT has variance rate

```text
Var(W)/E[L]
= p^2 sum_(k>=0) (1-p)^k
    (log F_(k+2)-(k+1)h_q)^2.
```

The initial delay, current unfinished cycle, and exact matrix boundary are
all `O(log n)` almost surely, so Slutsky transfer to `log N_n` is valid.
Variance positivity follows without decimals: if `W` vanished almost surely,
the cases `K=0` and `K=1` would force both `h_q=0` and `log 2=2h_q`.

The corrected proof makes the delayed clock explicit: conditional on the
almost-surely finite first-reset time `tau`, future cycles are iid, the
renewal-reward CLT is centered by `h(n-1-tau)`, and replacing that center by
`hn` costs only the fixed random quantity `h(tau+1)`.

The manuscript cites Asmussen for the classical regenerative CLT rather than
pretending to reprove the general random-time invariance principle.  All
conditions used from that theorem are checked in the text.

## Corrections made during the hostile pass

1. Corrected the parity sign in the diagnostic Binet formula.  The original
   diagnostic underestimated odd Fibonacci numbers; no integer or rational
   assertion depended on it.
2. Separated **66,787 exact assertions** from **10 floating diagnostics** so
   the control banner no longer overstates numerical exactness.
3. Tightened the longest-run wording to match the Borel--Cantelli event.
4. Added the convergence-radius check before substituting into the Fibonacci
   generating function.
5. Kept the endpoint entropy statements separate from the interior CLT and
   strict-gap claims.
6. Replaced the implicit absolute-time renewal identity by an explicit
   delayed-renewal clock and centering.
7. Removed the stray comma from the exponent in the finite-time annealed
   matrix power.

## Ownership and collision audit

- Furstenberg--Kesten positively own the general random-matrix-product
  framework.
- Kifer and Denker--Kifer--Stadlbauer positively own broad random-subshift
  thermodynamic formalism.
- Asmussen is cited for classical renewal and regenerative limit theory.
- Lind--Marcus is cited for standard symbolic-dynamics background.
- The model differs from a random substitution: the iid symbols select
  time-dependent adjacency constraints.  It also differs from a hidden
  finite-dependence process: the random object here is a fibre path count.

A bounded search through 2026-08-28 using the exact formula and combinations
of `random golden mean shift`, `Bernoulli reset`, `quenched entropy`, and
`random SFT` found no direct primary owner for the entire conjunction.  This
is not an exhaustive priority search.  Collision risk is assessed as
**medium** because every component technique is classical and the model is
only two dimensional.

## Surviving limitations and known risks

- The environment is iid Bernoulli.  Markov or correlated reset schedules
  are not covered.
- The reset matrix has a zero row, so the manuscript does not invoke random
  Perron--Frobenius theorems whose hypotheses require every row to be
  nonzero; all needed statements are proved directly.
- The CLT is stated only for `0<p<1`; both endpoints have degenerate
  deterministic fluctuations.
- The explicit variance is a rapidly convergent series, not an elementary
  radical expression.
- The literature firewall is bounded by date and keywords.  External expert
  review is required before any novelty statement or submission.

## Final reproducibility record

- Exact layer: **66,787 integer/rational assertions, PASS**.
- Floating diagnostics: **10, PASS**, excluded from exact evidence.
- Four-stage TeX/BibTeX build: all exits zero.
- PDF: **6 A4 pages, 320,648 bytes, PDF 1.5**.
- Undefined references/citations: **0/0**.
- Warnings and overfull/underfull boxes: **0**.
- Fonts: **24/24 embedded, subsetted, and Unicode-mapped**.
- Visual inspection: **6/6 pages**, no clipping, collision, or stray glyph.
- PDF SHA-256:
  `6782a62b934d40f7c1821cd161415a17e308cf4a78391886ecc6f2b639f04c0f`.
