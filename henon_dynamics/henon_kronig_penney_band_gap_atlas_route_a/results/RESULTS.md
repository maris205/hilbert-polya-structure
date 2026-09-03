# C327 results

## Theorem result

For every lattice spacing `a>0` and real coupling `g`, the periodic delta-comb
form is a lower-semibounded self-adjoint Hamiltonian.  Its determinant-one
monodromy has half trace

\[
\Delta(E)=\cos(ka)+g\sin(ka)/(2k),
\]

with the exact continuous zero and hyperbolic negative-energy interpretations.
The spectrum is exactly `|Delta|<=1`, is purely absolutely continuous, and has
Bloch multiplicity two in band interiors.  Every nonzero-coupling edge is a
simple periodic/antiperiodic fibre edge; free positive Bragg contacts are
double.

For attraction, `h=-ga` gives edge equations
`h=2y tanh(y/2)` and `h=2y coth(y/2)`.  The second begins at four, proving the
three exact regimes and the special `ga=-4` zero threshold.  Positive partners
obey `ga=2x tan((x-n pi)/2)`.  This yields every band and gap, proves all
nonzero-coupling Bragg gaps open, and gives

\[
|G_n|=2|g|/a+O_{ga}(n^{-2}a^{-2})
\]

with a two-term expansion and controlled `O(n^-4)` remainder in the proof.
The IDS and DOS follow from the correctly unwrapped alternating Bloch phase.

## Evidence result

- 5 attractive negative-atlas rows.
- 9 low-edge rows.
- 216 Bragg rows (`n=1..24`, nine nonzero dimensionless couplings).
- 150 transfer-matrix rows at three physical scales.
- 70 band-indexed IDS/DOS rows.
- 5,428 owned scalar leaves.
- Independent checker: 5,607 checks.
- SymPy: 295 exact identities.
- Hostile suite: 55/55 rejected.
- Isolated producer replay: byte identical.

For `ga<-4,n=1`, evidence names `positive_axis_gap_portion` and leaves the
full-width field null, because the complete first gap begins at a negative
energy.

## Route result

`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
`ROUTE_A_REJECTED`; Route B remains locked.
