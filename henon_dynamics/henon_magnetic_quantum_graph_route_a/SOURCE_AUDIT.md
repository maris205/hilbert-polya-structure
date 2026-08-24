# Source audit

## Frozen object

- Candidate: `HCS-C138`.
- Graph: two vertices joined by three edges of lengths `(1,2,3)`.
- Directed-bond order: `(+1,+2,+3,-1,-2,-3)`.
- Vertex law: degree-three Kirchhoff matrix `C=(2/3)11^T-I_3`.
- Global scattering and reversal: `S=[[0,C],[C,0]]`, `J=[[0,I],[I,0]]`.
- Magnetic split: forward/backward phases `exp(i(k l_j ± alpha_j)/2)`.
- Hilbert space: `C^6`; clock: one metric edge length per traversed directed bond.

C133 supplies the zero-flux baseline shape, but C138 independently reconstructs the matrices, determinant, walk ledger, and recovery identity.  No external target data are used.

## Allowed evidence

Exact rational scattering amplitudes, symbolic Laurent monomials, Gaussian/radical values in the `pi/2` control, finite directed-walk ledgers, block determinants, gauge conjugations, and antiunitary identities are allowed.

## Forbidden evidence and claims

Prime and zero tables, fitted phases, arithmetic local factors, root numbers, target divisors, Gamma factors, automorphy assumptions, and Route-B inputs are forbidden.  A finite-dimensional unitary scattering family is an A4 candidate, not a Hilbert–Pólya operator or an external spectral match.

Active firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
