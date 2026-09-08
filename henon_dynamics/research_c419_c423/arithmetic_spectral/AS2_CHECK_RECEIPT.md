# AS2 bounded oldform check receipt

Date: 2026-09-07 UTC. Actual command, repository root:

    python henon_dynamics/research_c419_c423/arithmetic_spectral/AS2_oldform_probe.py

Exit status 0; elapsed command time approximately 0.38 seconds.
Python 3.12.3; SymPy 1.14.0. The script printed its complete 40-row JSON
result to the execution output. No result-file write or old test rerun
was performed.

Input grid: $p\in\{2,3,5,7\}$, exponents $1\le e\le10$, regular
parameters $s=2,t=3$. All 40 reconstructed oldform blocks had exactly
zero commutator entries using rational arithmetic.

The reconstructed incoming matrix was
$$
C(s)_{j,a}=p^{s(e-\min(2a,e)+2\min(a,j)-j)},\qquad 0\le j,a\le e.
$$
The probe compares $P(s)=C(s)^{-1}C(1-s)$ in the fixed cusp-class
coordinates, after removing the common scalar level-one scattering
factor. It does not compare two independently diagonalized matrices.

This is a finite diagnostic conditional on the constant-term reduction.
It proves neither all-prime/all-exponent oldform commutativity nor the
primitive-character criterion. It also does not verify the true full
cusp matrix at any level containing nontrivial primitive-character
channels. Those are distinct proof obligations.

An independent reviewer has been assigned the primitive-character
normalization and conjugate-character blocks, not a redundant rerun
of this grid. The conjecture remains NOT CURRENTLY JUSTIFIED.
