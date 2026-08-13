# SD-C14 Source Lock

- **Primary family:** Symbolic Dynamics only.
- **Arithmetic atoms:** tensor-indecomposable full shifts `F_p`, ordered by
  entropy `h(F_p)=log p`.
- **Base grammar:** one primitive loop `gamma_p` at each atom; its `r`th
  traversal represents the `p^r` repetition.
- **Fiber algebra:** `A=C direct-sum L(Z)` with canonical Haar unitary `u` in
  `L(Z)`.
- **Fiber holonomy:** `W=1 direct-sum u`.
- **Positive trace:** `Phi_c(a direct-sum x)=a+c tau(x)`, with frozen `c>=0`.
  It is positive and faithful for `c>0`, but `Phi_c(1)=1+c`; it is not a
  normalized state unless `c=0`.
- **Moment ledger:** `Phi_c(W^r)=1` for all nonzero integers `r`.
- **Atom transfer:** `T_s=direct-sum_p p^(-s)W` in the semifinite tracial
  direct sum over tensor-prime atoms.
- **Analytic determinant:** the trace-log object
  `D_c(s,z)=exp[-sum_(r>=1)z^r Phi(T_s^r)/r]` on the honest Euler domain.
- **Single-block model:** `q=zp^(-s)` and
  `D_c(q)=exp[-sum_(r>=1)q^r Phi_c(W^r)/r]=1-q`.
- **Magnitude control:** Fuglede--Kadison determinant of `1-qW`, kept
  distinct from the analytic trace-log determinant.
- **Self-adjointization control:** `H=[[0,W],[W*,0]]`.
- **Recurrent control:** cross-fiber coupling is audited for balanced
  `uu^{-1}` identity words before any scalar specialization.
- **Allowed data:** exact Fourier coefficients, symbolic path words, finite
  cyclic approximants, and matched nonprime clocks.
- **Forbidden data:** Riemann-zero tables, target-fitted phases, inserted
  von Mangoldt weights, cross-family repairs, and coordinatewise mixing of
  analytic, Fuglede--Kadison, or self-adjoint data.
- **Route B:** locked; `route_b_invocation_allowed=false`.
