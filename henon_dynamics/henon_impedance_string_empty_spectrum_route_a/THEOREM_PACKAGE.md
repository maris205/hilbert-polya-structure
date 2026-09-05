# Complete theorem contract

For every L,c>0 and finite eta>=0, use the energy space and generator domain
in ASSUMPTIONS.md. The unitary U in proof section 1 has transport domain
w(tau)=q w(0), tau=2L/c, q=(eta-1)/(eta+1).

1. The exact semigroup has multiplier q^floor((s+t)/tau), with wrapped input;
   its norm is |q|^floor(t/tau), including all endpoint times.
2. If q is nonzero, the full spectrum is
   (log|q|+i(arg q+2pi n))/tau for every integer n, algebraically simple,
   with a complete Riesz basis. The specified multiplication similarity has
   condition number 1/|q|, not an asserted optimal basis invariant.
3. If q=0, the full spectrum is empty; the semigroup is norm one before tau
   and zero at and after tau. The all-plane inverse is the exponential
   upper-triangular Volterra kernel.
4. Its exact norm is tau sin(theta)/theta when x tau=-theta cot(theta)>-1;
   tau at x tau=-1; and tau sinh(h)/h when x tau=-h coth(h)<-1.
   Lowest-root selection is proved. Every strict epsilon-pseudospectrum is
   the left half-plane with this norm threshold.
5. All transparent resolvents are HS but not trace class, quasinilpotent,
   with det2 identically one. Their singular values at z=0 are
   tau/[pi(n+1/2)]. The semigroup is noncompact before extinction.
6. Reciprocal positive impedances preserve norm and shift spectra. Physical
   reversal changes eta to minus eta; positive damping is not reversible
   within the frozen family.

Proof status: PROVABLE_AS_STATED. The classical absorbing-wave mechanism
belongs to Driscoll–Trefethen 1996. No literature-priority or target theorem.
