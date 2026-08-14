# Methodology blueprint

## Frozen object

- Dynamics: the certified mixing four-state survivor of
  \(H_6(q,p)=(1-6q^2-p,q)\).
- Roof: \(\tau=\log J^u\), with normalized roof
  \(\widehat\tau=h_*\tau\) and \(P(-\widehat\tau)=0\).
- Arithmetic coefficient: the P53 Mahler spectral height
  \(\mathcal H_\gamma\).
- Forbidden inputs: prime tables, Riemann-zero tables, fitted roof values,
  post-hoc pressure normalization, and Route-B operator claims.

## Proof route

1. Split every reciprocal embedding pair into the physical pair and the
   remaining Galois pairs:
   \(\mathcal H_\gamma=\ell_\gamma+\mathcal E_\gamma\).
2. Identify the primitive physical amplitude with the first-repetition part
   of \(-\zeta'_{\widehat\tau}/\zeta_{\widehat\tau}\).
3. Apply Parry--Pollicott's simple-pole theorem and prove the repetition tail
   holomorphic near \(s=1\).
4. Define the Galois-excess abscissa and derive the three possible pressure
   regimes.
5. Apply the two-parameter weighted-zeta theorem conditionally, assuming one
   Hölder observable has the exact periodic sums \(\mathcal E_\gamma\).
6. Use the exact periods 1, 3 and 4 to attack the scalar-rescaling/coboundary
   shortcut.

## Evidence classes

- `PROVED`: the decomposition, physical pole, residue interval,
  scalar-roof obstruction and abscissa trichotomy.
- `CONDITIONAL_THEOREM`: full critical pole under an exact Hölder realization
  of the Galois excess.
- `OPEN`: existence of that realization or an asymptotically additive
  substitute.
- `NOT CLAIMED`: rational-prime trace, completed determinant, or operator.
