# HCS-C317 — Newton–Schulz full basin and pseudoinverse

This package classifies the exact-arithmetic dynamics
`X_{k+1}=X_k(2I-AX_k)` beyond the usual sufficient norm condition. For invertible square `A`, it proves the spectral-radius iff basin and the sharp nonnormal Jordan rate. For arbitrary rectangular `A`, it proves a compatibility-plus-spectral-radius iff theorem for convergence to the Moore–Penrose inverse. The canonical start `X_0=alpha A*` is resolved on every face of its sharp corridor, including repeated maximal singular values and rank zero.

The evidence includes 14 square Jordan cases, six compatible rectangular cases, six off-support counterexamples, and 19 canonical-alpha cases. It uses exact rational/Gaussian-rational arithmetic and is not a floating-point stability claim.

Run `python3 code/c317_release_manifest.py` for the closed-release audit. Route A has five failures and overall rejection under `NO_BAD_EULER_OR_ROOT_NUMBER`.
