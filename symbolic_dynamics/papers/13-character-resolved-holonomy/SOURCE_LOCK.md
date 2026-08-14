# SD-C15 Source Lock

- **Primary family:** Symbolic Dynamics only.
- **Arithmetic atoms:** tensor-indecomposable full shifts `F_p`, ordered by
  topological entropy `h(F_p)=log p`.
- **Base grammar:** one loop at every atom and both adjacent arrows
  `F_(p_n) <-> F_(p_(n+1))`.  The base graph is strongly connected and
  aperiodic.
- **Extension group:** `Z`, with lift coordinate `k`.
- **Frozen cocycle:** loops have charge `0`; every cross edge, in either
  direction, has charge `+1`.  Thus a lifted cross edge sends `k` to `k+1`.
- **Equivariant primitive ledger:** modulo deck translation, a periodic
  lifted path must have total charge zero.  Positivity of the cocycle therefore
  leaves only the atom loops and their repetitions; without the quotient each
  loop has infinitely many translated copies.
- **Clock:** the loop at `F_p` has roof `log p`.  Cross amplitudes use the
  endpoint-symmetric rule
  `a_n(s)=(p_n^(-s)+p_(n+1)^(-s))/2`.
- **Bloch/character fibers:** for `w=exp(i theta)` on the unit circle,

  ```text
  L_s(w) = D_s + w A_s,
  D_s e_n = p_n^(-s)e_n,
  A_s = sum_n a_n(s)(E_(n+1,n)+E_(n,n+1)).
  ```

  This is the Fourier decomposition of the same `Z`-extension, not a second
  candidate.  Complex `w` off the circle is only the analytic continuation of
  the Fredholm family, not a deck character.
- **Function space and trace:** `l^2(N)` in each Bloch fiber.  The lifted
  operator is affiliated to
  `M=B(l^2(N)) bar-tensor L(Z)` and is trace class only for the semifinite
  trace `Phi=Tr bar-tensor tau_Z`; it is not ordinary trace class on
  `l^2(N) tensor l^2(Z)`.
- **Lifted transfer:**
  `Ltilde_s=D_s tensor 1 + A_s tensor U`, where `U` is the bilateral deck
  shift.  Both orientations use the same `U`, not `U` and `U^*`.
- **Determinant convention:** for `Re(s)>1`, `L_s(w)` is trace class and
  `D_SD(s,z,w)=det(I-z L_s(w))` is the resolved Fredholm family.  The
  canonical zero Fourier mode is defined coefficientwise from the trace-log
  germ at `z=0`; global logarithm branches are not silently identified.
- **Same-parent target extraction:** the zero Fourier coefficient of
  `log D_SD` is
  `sum_p log(1-z p^(-s))`, while nonzero Fourier modes record charged mixed
  base returns.  No genuine unitary Bloch fiber has the exact Euler ledger;
  exactness belongs to the equivariant coefficient-zero sector.
- **Frozen primary parameters:** equal-endpoint coefficient `1/2`, charges
  all `+1`, and no fitted scale, offset, phase, cutoff, or zero location.
- **Predeclared controls:** inverse/reversal charges `(+1,-1)`, entropy and
  rank coboundaries, the entropy-roof character, forward-DAG grammar,
  positive random integer charges, composite-only masses, shuffled masses,
  and seeded random-increasing masses.
- **Allowed data:** tensor multiplication, entropy, exact path/charge words,
  finite Fredholm determinants, Fourier coefficients, singular values, and
  matched controls.
- **Forbidden data:** Riemann-zero tables, target-fitted phases, selected
  characters after inspection, inserted von Mangoldt weights, cross-family
  repairs, or coordinatewise combination with Paper 06--12 determinants.
- **Route B:** locked; `route_b_invocation_allowed=false`.

## Claim boundary

SD-C15 asks whether retaining the full character family makes the formerly
trace-invisible recurrent sector visible in the *same parent* equivariant
Fredholm family without destroying the exact Euler zero mode.  Even if
successful, character
motion is not target evidence unless it is selective against the frozen
nonprime and random controls and is not merely a coboundary gauge or a
reparameterization of `s`.
