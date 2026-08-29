# Evidence and experiment plan

## Claim ledger

The proof claims are: the exact derivative of
\(V=x^2+y^2+(z-\rho-\sigma)^2\); the scalar absorbing inequality and global
forward bound; the complete equilibrium set for positive parameters; both
characteristic polynomials; the Routh–Hurwitz margin and Hopf factorization;
and the zero-rate equilibrium families with their transverse spectra.

## Frozen regression design

- Ten exact rational positive-parameter rows cover \(\rho<1\), \(\rho=1\),
  stable wings, two exact Hopf points, post-Hopf instability, negative \(\rho\),
  and the no-finite-Hopf regime \(\sigma\le\beta+1\).
- Five rational phase-space points test the Lyapunov cross-term cancellation by
  two independently written formulas.
- Three boundary ledgers cover \(\sigma=0\), \(\beta=0\), and
  \(\sigma=\beta=0\).

## Verification gates

1. Produce canonical JSON from frozen exact inputs.
2. Reconstruct all rows in a producer-independent checker.
3. Re-derive generic identities with SymPy.
4. Reproduce the evidence byte-for-byte in a clean process.
5. Reject stale hashes, repaired semantic changes, nested unknown keys,
   provenance changes and forbidden claim flags.
6. Build three content-distinct paper revisions with a fixed epoch, embedded
   subset fonts, clean logs and visual inspection.
7. Close exactly 27 payload files plus a self-excluded release manifest.

Finite regression rows are controls for formulas proved symbolically; they are
not numerical evidence for a global strange-attractor classification.
