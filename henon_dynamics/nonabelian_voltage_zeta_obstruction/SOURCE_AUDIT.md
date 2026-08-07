# Primary-source and novelty audit

## Verdict

The broad proposal “nonabelian voltage cover + delete the trivial
representation + Artin--Ihara determinant” is established mathematics. The
project therefore makes no novelty claim for the factorization, for
Heisenberg graph zetas, or for the linear zero density of exponential
polynomials. The scoped contribution is their combined use as a
Hilbert--Pólya exclusion package, together with:

- an explicit non-dihedral Heisenberg pair with identical cyclic directed
  bigram counts but distinct same-order central holonomy;
- a fixed-finite-memory zero-density ruling that also covers finitely many
  incommensurable roofs;
- an exact conductor-resolved \(q=243\) Rayleigh certificate and its use as a
  frozen Hilbert--Pólya/new-sector-gap obstruction after every abelian sector
  is removed.

## Source map

### Finite graph covers and Artin--Ihara factors

- Stark and Terras established the multivariable and covering framework in
  [Zeta Functions of Finite Graphs and Coverings](https://doi.org/10.1006/aima.1996.0050)
  and its
  [Part II](https://doi.org/10.1006/aima.2000.1917).
- Mizuno and Sato gave determinant and covering results in
  [Zeta Functions of Graph Coverings](https://doi.org/10.1006/jctb.2000.1983).
- Sato's
  [Weighted Zeta Functions of Graph Coverings](https://doi.org/10.37236/1117)
  directly implies the local lift factor

  \[
  (1-w(P)^o u^{|P|o})^{-|G|/o}.
  \]

  The order-only regular-minus-trivial formula in this project is a direct
  specialization and application of this result.
- Hashimoto's edge operator and Bass's determinant formula are the standard
  finite graph inputs:
  [Hashimoto 1990](https://doi.org/10.1142/S0129167X90000204) and
  [Bass 1992](https://doi.org/10.1142/S0129167X92000357).

### Heisenberg and noncommutative towers

- DeDeo, Martínez, Medrano, Minei, Stark, and Terras already studied finite
  Heisenberg graph spectra and explicitly constructed their finite-ring
  irreducible Schrödinger/Harper blocks in
  [Spectra of Heisenberg Graphs over Finite Rings](https://doi.org/10.3934/proc.2003.2003.213).
  They studied coverings and Artin factors in
  [Zeta Functions of Heisenberg Graphs over Finite Rings](https://doi.org/10.1007/0-387-24233-3_8).
  Consequently, neither the deck group nor its Hofstadter/Harper blocks are
  new objects here.
- Béguin, Valette, and Żuk directly studied the discrete Heisenberg random
  walk and Harper-operator norm in
  [On the Spectrum of a Random Walk on the Discrete Heisenberg Group and the Norm of Harper's Operator](https://doi.org/10.1016/S0393-0440(96)00024-1).
  The near-zero-flux spectral-edge mechanism is therefore prior structure.
- Kleine and Müller treat uniform noncommutative pro-\(p\) voltage towers,
  special values, and noncommutative Iwasawa structure in
  [On the non-commutative Iwasawa main conjecture for voltage covers of graphs](https://doi.org/10.1007/s11856-026-2914-7).
  A generic “take the tower limit” proposal is therefore not a novelty claim.
- Higher Milnor invariants and residue-symbol information in arithmetic
  Ihara/Galois representations also have substantial prior art. They are not
  imported as if they were graph-zeta discoveries.

### Exponential-polynomial zeros

- Langer's
  [On the Zeros of Exponential Sums and Integrals](https://doi.org/10.1090/S0002-9904-1931-05133-8)
  is a classical source for zero distribution of exponential sums.
- Heittokangas and Wen give a modern generalization of Pólya theory in
  [Generalization of Pólya's Zero Distribution Theory for Exponential Polynomials](https://doi.org/10.1007/s40315-020-00336-7).
- This project includes a self-contained Jensen proof because only the upper
  bound \(O(T)\) is needed. The exponential-sum theory itself is not claimed
  as new.

### Target zero count

- The comparison is the classical Riemann--von Mangoldt law. The primary
  source is von Mangoldt,
  [Zur Verteilung der Nullstellen der Riemannschen Funktion \(\xi(t)\)](https://doi.org/10.1007/BF01447494).

## Novelty matrix

| Component | Status | Allowed claim |
|---|---|---|
| regular-cover Artin factorization | established | background/control only |
| delete trivial representation via \(Z_Y/Z_X\) | established | background/control only |
| order-only local aggregate | direct Sato corollary | observability interpretation, not new factorization |
| Heisenberg graph/Ihara/Hofstadter block | established | explicit control only |
| equal-bigram, non-dihedral \(H_7\) witness | no exact collision found | project-specific explicit chronology counterexample |
| finite-roof determinant is exponential polynomial | elementary/classical | scoped HP exclusion synthesis |
| \(O(T)\) exponential-sum zero count | classical | self-contained proof and Route-A application |
| finite-ring Schrödinger/Harper block and spectral-edge behavior | established | background/control only |
| conductor-resolved \(q=243\) Rayleigh certificate and branch return in \(H(\mathbb Z/3^m)\) | standard Weyl/Følner ingredients; exact frozen certificate/application not found in audited sources | scoped uniform-new-sector-gap obstruction with proof |
| Hilbert--Pólya realization | absent | no positive claim |

## Claim boundaries forced by the audit

1. “Order-only” applies to each canonical, regular-multiplicity aggregate
   local factor. The full scalar zeta can still encode the distribution of
   holonomy orders over all primitive words.
2. A representation-resolved ledger recovers conjugacy information. A single
   central character is not canonical unless the dynamics supplies extra
   arithmetic data selecting it.
3. The \(O(T)\) theorem concerns one fixed finite-state, finite-memory
   determinant with constant finite-dimensional twist and a fixed affine
   spectral variable. It does not rule out a proved infinite-dimensional
   determinant or a moving nonuniform limit.
4. The tower theorem rules out the uniform Ramanujan/new-sector-gap version
   of the frozen amenable Heisenberg proposal, including its primitive
   nonabelian sectors. It does not rule out a separately renormalized
   determinant or subtraction scheme, nor nonamenable property-\(\tau\)
   towers.
5. Graph “Riemann hypothesis” means the Ramanujan pole-circle condition. It
   must not be conflated with the classical Riemann hypothesis.
