# Exact validation plan

This is a proof package.  No stochastic or GPU experiment is relevant; code
reconstructs and attacks exact identities.

## Frozen inputs

- \(H(q,p)=(q^2+p^2)/2\) on \(\mathbb R^2\).
- \(\theta\in\mathbb R\) is physical time and one time step is one strobe;
  \(T_{\theta+2\pi}=T_\theta\) only after classical projection.
- \(q-ip=re^{i\varphi}\) and
  \(d\gamma=\pi^{-1}e^{-r^2}\,dq\,dp\).
- \(U_\theta f=f\circ T_\theta\) and
  \(Q_\theta=e^{-i\theta\widehat H}\).
- \(U_{\theta+2\pi}=U_\theta\), while
  \(Q_{\theta+2\pi}=-Q_\theta\) and
  \(Q_{\theta+4\pi}=Q_\theta\); the global sign is not quotiented.
- Exact algebra only; no target data or fitted parameter.

## Gates

1. **Classical group gate:** reconstruct the rotation group law, fixed-set
   dichotomy, rational order, irrational fixed counts, and reversor.
2. **Cardinality gate:** refuse a finite coefficient whenever a resonant
   iterate fixes \(\mathbb R^2\).
3. **Gaussian gate:** check the Laguerre normalization, angular phase, dense
   irrational spectrum, rational root spectrum, and radial multiplicities.
4. **Quantum gate:** check Hermite energies, exact-real-time rational phases,
   the metaplectic \(2\pi\) sign and \(4\pi\) return, oscillator commutators,
   Egorov rotation, and conjugation reversal on the same clock.
5. **Operator-ideal gate:** separate unitarity from compactness, finite
   Schatten membership, trace class, and ordinary Fredholm ownership.
6. **Clock gate:** label heat, Wick, and finite Hermite variants as different
   operators rather than repairs.
7. **Adversarial gate:** reject repaired-hash semantic mutations and one
   stale-hash mutation.
8. **Release gate:** byte replay, two independent fixed-epoch builds,
   embedded fonts, visual inspection, and 27-file manifest closure.

## Finite sentinels

The ledger records all reduced rational representatives in \([0,1)\) through
denominator 12, their explicit \(2\pi\)- and \(4\pi\)-shifted quantum phases,
and iterates through 36, three exact irrational controls, Laguerre indices
\(|m|\le9\), \(k\le10\), and Hermite levels through 15.  These finite rows
detect implementation drift.  The theorems carry every unbounded and
all-angle quantifier.

## Success and pivot rule

Success means one complete theorem-backed decision, including an exact
rejection.  Any failure of the fixed-set, basis, Egorov, or clock identities
would weaken or replace the model.  The identities survive, while the
determinant and arithmetic obstructions remain visible.
