# Derivation Package — Paper 46

## Frozen theorem chain

1. **Support lemma.** \(m+n=2^a\) implies \(v_2(m)=v_2(n)\).
2. **Schur lemma.** For \(\sigma>0\), the absolute row sums are uniformly
   bounded and vanish at infinity.
3. **Compactness lemma.** Vanishing row sums plus finite row-tail control
   gives norm approximation by finite compressions.
4. **Row-one obstruction.** The row \(m=1\) is not in \(\ell^2\) for
   \(\sigma\le0\).
5. **Anti-diagonal lemma.**
   \[
   \|H_s\|_2^2=\sum_{a\ge1}\sum_{m=1}^{2^a-1}
   [m(2^a-m)]^{-\sigma}.
   \]
6. **Central-matching lemma.** Disjoint \(Q_j=4^j\) matchings have
   trace-dual mass comparable to \(Q_j^{1-\sigma}\).
7. **Valuation lemma.**
   \(H_s\cong\bigoplus_{k\ge0}2^{-ks}A_s\).
8. **Cycle lemma.** Iteration of \(n_{i+1}=q_i-n_i\) gives the exact
   odd/even closing equation.
9. **Ideal consequence.** The three sharp walls are \(0,1/2,1\).
10. **Determinant consequence.** Only after Step 9, the direct sum yields
    the trace-power and \(\det_2\) product in \(\sigma>1/2\).

## Endpoint bookkeeping

| Property | Strict legal domain | Boundary witness |
|---|---|---|
| bounded/compact | \(\sigma>0\) | row \(1\) for \(\sigma=0\) |
| \(S_2\) | \(\sigma>1/2\) | central anti-diagonal mass |
| \(S_1\) | \(\sigma>1\) | disjoint central matching |
| ordinary trace/determinant | \(\sigma>1\) | \(S_1\) wall |
| \(r\ge2\) trace powers and \(\det_2\) | \(\sigma>1/2\) | \(S_2\) wall |

## Algebraic cycle solver

For \(q_i=2^{a_i}\),

$$
n_i=(-1)^{i-1}n_1+
\sum_{j=1}^{i-1}(-1)^{i-1-j}q_j.
$$

Closing gives

$$
(1-(-1)^r)n_1=\sum_{j=1}^r(-1)^{r-j}q_j.
$$

This formula is the sole source of the odd/even distinction. Positivity and,
for the odd block, odd parity are checked after the algebraic closing
condition.

## Independence of theorem components

Removing the generic Schur and Schatten estimates leaves the support,
valuation, and full cyclic solver. Removing the cyclic solver leaves the
independently sharp ideal theorem. Thus no numerical fit or one-lemma
corollary is carrying the package.

## Proof status

All ten steps have complete proofs in PROOF_PACKAGE.md. The later experiment
is a falsification and reproducibility layer, not a substitute for any
endpoint proof.

