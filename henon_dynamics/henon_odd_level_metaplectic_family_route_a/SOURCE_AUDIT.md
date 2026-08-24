# Source audit

The source object is fully defined inside this package: the integer matrix
`A`, the odd residue rings, Weyl generators, half-phase, discrete Fourier
matrix, chirp, unitary, and antiunitary.  The all-level proof uses finite
Fourier orthogonality and modular identities only.  No external data or
fitted parameter is used.

The producer proves the certified cases using integer modular arithmetic.
The independent checker does not import it and reconstructs every headline
field and every case digest.  SymPy supplies a third recurrence and phase
check.  The certificate levels are sentinels for the proved all-odd theorem;
they are not a finite sample promoted into a universal conclusion.

No prime table, zero table, target spectrum, Euler factor, root number,
automorphy, or Hilbert--Pólya claim occurs.  No literature novelty search or
external referee assessment was performed, and none is claimed.
