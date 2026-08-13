# SD-C13 Source Lock

- **Primary family:** Symbolic Dynamics only.
- **Arithmetic atoms:** tensor-indecomposable full shifts `F_p`, ordered by
  entropy `h(F_p)=log p`.
- **Base grammar:** one primitive loop at every atom; its `r`th traversal is
  the repetition attached to `p^r`.
- **Fiber:** a frozen finite-dimensional unitary `U_p(theta)` on `C^d`, with
  one common finite `d` in the main branch and `U_p(0)=I_d`.
- **Positive ledger:** the faithful normalized matrix trace
  `tau_d=d^(-1)Tr`; ordinary trace is a separate control.
- **Twisted repetition weight:** `tau_p(U_p^r)`.
- **Formal potential:** `z p^(-s) U_p` at the `p`-atom loop.
- **Function space:** `H=ell^2(P) tensor C^d`; equivalently the tracial
  direct-sum algebra `direct-sum_p M_d(C)` with trace
  `Phi=sum_p tau_d`.
- **Transfer:** `T_s(theta)=direct-sum_p p^(-s)U_p(theta)`.
- **Determinant convention:** on `Re(s)>1` and
  `|z|2^(-Re(s))<1`,
  `D_tau=exp[-sum_(r>=1) z^r Phi(T_s^r)/r]`; the ordinary Fredholm
  determinant is audited separately and is not identified with `D_tau`.
- **Recurrent control:** a finite triangle or two parallel return paths with
  unitary holonomy, audited first in independent atom variables.
- **Forbidden data:** Riemann-zero tables, target-fitted phases, inserted
  von Mangoldt weights, cross-family repairs, or changing the fiber after
  inspecting repetitions.
- **Primary theorem obligation:** decide whether nontrivial positive unitary
  fibers can preserve every prime repetition coefficient while producing
  visible determinant motion.
- **Route status:** Route B is locked.

The exact-ledger and nontrivial-motion requirements are tested simultaneously.
The untwisted tensor-prime base is retained as a control, not promoted as a
new Bloch success.
