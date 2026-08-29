# Theorem package: Landau–Zener–Weber crossing

## Frozen model and conventions

Let `v>0`, `g∈R`, and
\[
 H(t)=\frac{vt}{2}\sigma_z+g\sigma_x,
 \qquad i\,\partial_t\psi=H(t)\psi,
 \quad \sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
The diabatic basis is fixed at both ends.  Put
`delta=g^2/v`.  All phases below use the displayed gauge; a constant
`sigma_z` conjugation changes the sign of `g` and is the only sign gauge used.

## Theorem 1 (Weber reduction and connection law)

For `g≠0`, eliminating the lower component gives
\[
 a''(t)+\left(g^2+\frac{v^2t^2}{4}+\frac{i v}{2}\right)a(t)=0,
\qquad
 b''(t)+\left(g^2+\frac{v^2t^2}{4}-\frac{i v}{2}\right)b(t)=0.
\]
After the standard rotation and affine rescaling these are parabolic-cylinder
equations.  The connection formula between their two Stokes sectors, with
incoming/outgoing diabatic amplitudes normalized to unit flux, is
\[
 S(\delta)=\begin{pmatrix}
 \sqrt P&-\sqrt{1-P}\,e^{i\phi_S}\\
 \sqrt{1-P}\,e^{-i\phi_S}&\sqrt P
 \end{pmatrix},
 \qquad P=e^{-2\pi\delta},
\]
where
\[
 \phi_S=\frac\pi4+\delta(\log\delta-1)+\arg\Gamma(1-i\delta).
\]
The continuous value at `delta=0` is `phi_S(0)=pi/4`; changing asymptotic
phase conventions conjugates `S` by diagonal unitary matrices but leaves `P`.

*Proof sketch.* Substitute `b=(i a'-(vt/2)a)/g` into the first equation and
use the second; the two displayed scalar equations result.  The Weber
parabolic-cylinder basis has a constant Wronskian.  Applying its connection
identity to the rotated arguments gives the two amplitudes above; the modulus
identity `|Gamma(1+i delta)|^2=pi delta/sinh(pi delta)` reduces the diagonal
modulus to `exp(-pi delta)`.  This is a source-local special-function
calculation; no target data enter it.

## Theorem 2 (Wronskian/unitarity and monotonicity)

For real `v,g`, `H(t)` is Hermitian.  Hence every finite-time propagator
`U(t_2,t_1)` preserves the Hermitian form.  The Weber Wronskian gives the same
flux identity at infinity, so `S^*S=I` and `det S=1` in the gauge above.  The
crossing probabilities satisfy
\[
 \frac{dP}{d\delta}=-2\pi e^{-2\pi\delta}<0\quad(\delta>0),
 \qquad \frac{\partial P}{\partial g}\bigg|_v=-\frac{4\pi g}{v}e^{-2\pi g^2/v}.
\]
The phase derivative used in the ledger is
\[
 \phi_S'(\delta)=\log\delta-\Re\psi(1-i\delta),
\]
with `psi` the digamma function.

## Theorem 3 (limits and finite-window control)

As `delta↓0`, `P=1-2pi delta+O(delta^2)` and the mixing amplitude is
`O(sqrt(delta))`; as `delta→∞`, `P~exp(-2pi delta)` and the transition is
adiabatic.  At `g=0`, the channels decouple exactly and `P=1`.  The limit
`v→∞` is sudden (`delta→0`), whereas `v↓0` at fixed nonzero `g` is adiabatic.
At finite `T`, the receipt integrates the original ODE on `[-T,T]` with a
fixed 2048-step classical RK4 scheme in 80-digit arithmetic.  It reports all
four entries of the resulting matrix and the Gram residual.  This is a
controlled approximation and is not identified with an exact finite-time
Weber propagator.

## Route-A boundary

The result is a complete physical scattering theorem for one nonautonomous
crossing.  It has no primitive periodic-orbit repetition law, rational-prime
owner, target divisor, or target zero correspondence.  It is therefore
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)` and
`ROUTE_A_REJECTED`; Route B remains false.  In particular, the object is not
the autonomous conserved-excitation block decomposition of C223.

## Evidence map

`results/c224_landau_zener_evidence.json` contains five exact rational
scattering rows, fifteen finite-window rows, six boundary rows, and a
content hash.  The independent checker reconstructs every formula without
importing producer functions.  The SymPy script checks the scalar equations,
Pauli algebra, SU(2) invariants, coupling-sign gauge, and monotonicity.  Replay
and repaired/stale-hash mutations are separate processes.
