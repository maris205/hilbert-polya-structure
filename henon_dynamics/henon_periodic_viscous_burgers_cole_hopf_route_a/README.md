# HCS-C195: periodic viscous Burgers via the positive projective heat cone

This package freezes the real periodic viscous Burgers semiflow

\[
 u_t+u u_x=\nu u_{xx},\qquad x\in\mathbb T_L,\quad \nu>0,\quad L>0,
\]

on every Sobolev leaf of prescribed mean \(m\). Its single-paper increment is an
all-parameter phase portrait: the Cole--Hopf map is a global conjugacy to the
strictly positive projectivized drift--heat semigroup; every orbit exists for all
positive physical time and converges to the unique constant equilibrium; no
nonconstant point is periodic or recurrent; the first active Fourier mode of the
positive lift gives the exact leading decay; and the complete linearized spectrum
is explicit.

The transformation and the underlying viscous-Burgers solution method are classical
Hopf--Cole mathematics. No priority claim is made. The package contribution is a
carefully normalized theorem/certificate/rejection bundle under the source lock.

## Release inventory

- `THEOREM_PACKAGE.md`: hypotheses, theorem, proofs, and exact boundary.
- `SOURCE_AUDIT.md`: classical ownership, conventions, and source firewall.
- `results/c195_burgers_evidence.json`: deterministic exact-rational regression oracle.
- `code/c195_burgers_checker.py`: producer-independent checker.
- `paper/main.pdf`: final paper after two substantive internal review rounds.
- `C195_RELEASE_MANIFEST.json`: self-excluded hash ledger for the 27 payload files.

The finite trigonometric-polynomial census is regression evidence only. It is not
the proof of the infinite-dimensional theorem. The frozen route tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A is rejected and Route B
is not authorized. Scope is exactly `NO_BAD_EULER_OR_ROOT_NUMBER`.
