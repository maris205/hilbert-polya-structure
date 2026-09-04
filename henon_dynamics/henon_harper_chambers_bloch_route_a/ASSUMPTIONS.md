# Assumptions and conventions

- The main theorem uses a reduced flux `p/q` with `q>=3`, `lambda>0`,
  horizontal hopping one, and vertical hopping `lambda`.
- Landau gauge is fixed by the magnetic phase `exp(2 pi i p m/q)` on the
  vertical hop at horizontal coordinate `m`.
- The fiber coordinate satisfies
  `u_(m+q)=exp(i q k_x)u_m`.  Thus `q k_x`, not `k_x`, is the total
  horizontal boundary phase.  Likewise the last cosine in Chambers'
  identity is `cos(q k_y)`.
- The characteristic convention is `D(E)=det(E I-H_fiber)`.  With this
  convention both Bloch terms have a minus sign.
- The spectrum means the spectrum of the full two-dimensional magnetic
  lattice Hamiltonian, equivalently the union of all finite magnetic
  Bloch-fiber spectra.
- A "multiple band edge" means a multiple root of the algebraic edge
  polynomial `P(E)^2-4(1+lambda^q)^2`.  It records coalescing edge labels;
  no assertion that every complementary gap is open is made.
- With `C=2(1+lambda^q)`, the factors `P-C` and `P+C` use the real
  symmetric fibers at `(k_x,k_y)=(0,0)` and `(pi/q,pi/q)`, respectively.
- Lamoureux--Mingo use `h_(theta,L)=u+u^-1+(L/2)(v+v^-1)`; comparison with
  the present vertical hopping fixes `L=2 lambda`.
- The `q=1` and `q=2` matrices accumulate coincident periodic neighbors.
  They are direct boundary fibers, not obtained by silently reusing the
  sparse `q>=3` matrix display.
