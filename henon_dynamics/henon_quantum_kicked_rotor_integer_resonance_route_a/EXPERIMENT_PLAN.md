# C337 exact-evidence plan

## Claim ladder

1. Prove self-adjoint/unitary ownership and reduce the free phase at $\tau=2\pi\ell$ using $n^2\equiv n\pmod 2$.
2. For even $\ell$, derive the exact Bessel kernel, characteristic function and central moments through order six.
3. For odd $\ell$, conjugate the kick by the half-turn and prove $U^2=I$ as an operator identity.
4. Close arbitrary $m$, all real $\kappa$, $\kappa=0$, both parity faces, and the stated operator ordering.
5. Apply Route-A v0.2.0 without widening the scope firewall.

## Deterministic evidence

- exact free-phase parity rows for $1\leq\ell\leq12$ and $-16\leq n\leq16$;
- exact Gaussian-rational Taylor coefficients of the Fourier kick kernel through degree 14, reconstructed two different ways;
- exact rational raw and central moment rows through order six on a finite regression grid;
- exact odd-sheet word reductions and amplitude-phase conventions;
- high-precision Bessel normalization, characteristic-function and moment spot checks, labeled numerical receipts rather than proof.

The producer and checker share no imports.  The checker rejects duplicate or nonfinite JSON, unowned fields, stale payload hashes, malformed YAML, every evaluator-leaf mutation, and all firewall changes.  Replay runs the producer in isolation and compares bytes.  The SymPy lane independently differentiates the characteristic function.

## Publication gate

Three substantively different PDF rounds are built twice from fresh directories with LuaLaTeX under `SOURCE_DATE_EPOCH=1788393600`.  Release requires 27 payload files, 28 physical files including the self-excluded manifest, embedded/subset fonts, clean logs, clean extracted text and successful rasterization of every page.
