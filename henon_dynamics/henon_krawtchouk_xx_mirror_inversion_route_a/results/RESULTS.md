# Results — HCS-C366

The canonical evidence contains:

- 66 Krawtchouk spectral/orthogonality rows for (0\le N\le10);
- 65,534 individual Fock basis states for (0\le N\le14), each with
  exact energy, reflected mask, and mirror phase;
- the complete sectorwise energy-multiplicity histograms;
- 231 formal all-time endpoint cells through $N=20$, including amplitude
  phase, binomial radicand, sine power, and cosine power;
- all 136 recursively defined Gaussian $q$-binomial coefficient polynomials
  through order 15;
- explicit route, scope, theorem, and boundary records.

The canonical JSON is 14,106,891 bytes. Its file SHA-256 is
`4db662e17cad51818fee60b6a54fcf508ae80e675f31dc445ce013d272a734f4`,
and its self-excluding payload SHA-256 is
`6d8b4572ce0188268b65ebd69286ae5871d72887b55caec9eaf6d2d58e5000b5`.

The producer-independent checker reconstructs every combinatorial quantity.
The SymPy lane builds the tridiagonal matrices independently, checks their
characteristic polynomials and eigenvectors, verifies Krawtchouk
orthogonality, and compares the complete product and recursive Gaussian
polynomials coefficient by coefficient. The replay lane
reproduces the JSON in two isolated directories.  The hostile suite repairs
each payload hash before demanding rejection.

These finite rows do not prove the all-$N$ theorem. The proof is the
spin-representation identification followed by fermionic exterior powers.
The independent checker passed 877,612 assertions; the separate SymPy lane
passed 4,001 identities; isolated replay reproduced all 14,106,891 bytes; and
all 100 hostile mutations were rejected.
