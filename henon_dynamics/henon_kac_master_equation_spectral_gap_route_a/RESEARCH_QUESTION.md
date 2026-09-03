# Research question

For Kac's uniform binary-collision walk, can one obtain the exact dimension-dependent relaxation rate from a complete geometric induction rather than a finite spectral experiment?

The frozen state space is `S^{N-1}(sqrt(N))`, an unordered pair is selected uniformly, its plane is rotated by a uniform angle, and the positive generator is `L_N=N(I-Q_N)`.  The package asks for the exact gap, a slow eigenfunction that meets the lower bound, uniqueness away from the exceptional two-particle base, sharp `L2` semigroup decay, and explicit treatment of positive-energy scaling and the degenerate `E=0` face.

The answer is yes.  The proof slices the `N`-particle Dirichlet form into `(N-1)`-particle forms, computes the exact spectrum of the coordinate conditional-expectation operator, and uses `P=TT*/N` to reduce the full nonzero projection spectrum to two explicit index-space branches of `T*T/N`.  This yields `kappa_N=3/(N^2-1)` and telescopes the resulting gap recursion.  Finite polynomial matrices verify the algebra but do not prove the infinite-dimensional lower bound.
