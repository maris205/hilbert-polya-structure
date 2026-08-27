# C196 exact-validation plan

## Claim matrix

| Claim | All-parameter justification | Executable regression | Failure trigger |
|---|---|---|---|
| Hermitian/Lax convention | direct conjugation | every Gaussian-rational entry | sign mismatch |
| rank-one commutator | exact entry identity | 417 entries | any diagonal/off-diagonal defect |
| `Tr L^2=2H` and traces | algebra and unitary conjugacy | powers `1,...,N` | factor or imaginary part |
| all-time simple pencil | rank compression proof | 126 sampled spectra | sampled collision/order defect |
| Newton equations | Hermitian perturbation | transformed force residual | sign or `2g^2` defect |
| both scattering ends | nondegenerate perturbation | `T=256` at both ends | reversal/intercept defect |
| inverse atlas | commutator and simple diagonalization | reconstruct initial position spectrum `q` | denominator-sign defect |
| no bounded periodic motion | distinct asymptotic velocities | growth sentinel only | finite data never serves as proof |
| Route-A stop | source/scope audit | semantic mutations | target, novelty, or Route-B flag |

## Regression domain

- Every `N=2,...,7`, three deterministic seeds per `N`.
- Couplings `1/2`, `1`, `3/2`.
- Times `-64,-16,-4,0,4,16,64`; asymptotic sentinel `T=256`.
- 18 systems, 126 pencil rows, 417 Hermitian entries, 417 commutator
  entries, and 99 trace/energy checks.

This is deterministic finite regression, not a sample-based proof of the
all-parameter theorem.

## Independent paths

1. Producer: exact Gaussian-rational matrix products plus LAPACK Hermitian
   eigenvectors for finite sentinels.
2. Checker: no producer import; realified maximum-pivot Jacobi spectra,
   polynomial spectral projectors for intercepts, and centered-difference
   velocities.
3. SymPy: all exact powers and characteristic polynomials, a generic
   three-particle sign/factor sentinel, and the symbolic inverse-atlas sign.
4. Replay: exact byte equality.
5. Mutations: 135 repaired semantic hashes, including five unknown-key schema
   injections, and one stale hash.

## Release gates

- all five executable checks pass;
- baseline and two substantively revised PDFs are pairwise distinct;
- round 2 equals the final PDF;
- two fresh fixed-epoch builds are byte identical;
- fonts, final/fresh logs, extracted text, and all rendered pages are clean;
- a self-excluded 27-payload manifest closes a 28-file physical package.
