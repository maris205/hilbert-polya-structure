# HCS-C337 / HEN-O321

This package proves the complete positive-integer resonance sheet of the quantum kicked rotor

$$U_\tau=e^{-i\tau\widehat n^2/2}e^{-i\kappa\cos\theta},\qquad \tau=2\pi\ell.$$

Even $\ell$ gives an exact Bessel propagator and ballistic momentum moments; odd $\ell$ gives the operator identity $U^2=I$.  The result holds for every real kick strength, every integer momentum seed and every nonnegative kick count.  General rational resonance and detuning are excluded.

The proof is in `THEOREM_PACKAGE.md`, executable receipts are in `results/c337_kicked_rotor_evidence.json`, and the final paper is `paper/main.pdf`.  Run the producer, independent checker, SymPy lane, byte replay, hostile mutation suite and release gate from `code/README.md`.

Route-A tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.  Overall verdict: `ROUTE_A_REJECTED`; Route B is disabled under `NO_BAD_EULER_OR_ROOT_NUMBER`.
