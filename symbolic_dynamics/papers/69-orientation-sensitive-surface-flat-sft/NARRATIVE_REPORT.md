# Narrative report

## One-sentence result

A single finite-type flat-connection shift over the nonorientable genus-three
surface group has two explicit periodic-point spectra whose joint data recover
the order of the finite gauge group and every pair consisting of an irreducible
degree and its Frobenius--Schur indicator.

## Why the system matters

Periodic points of a group shift depend on the finite-index subgroup used to
probe the action.  Here that dependence is topological rather than merely
arithmetic.  One subgroup family stays nonorientable, while the other lies in
the orientation kernel.  The orientable counts see only inverse even moments
of character degrees.  The nonorientable counts insert powers of the
Frobenius--Schur indicator and therefore see whether a self-dual irreducible
representation is orthogonal or symplectic, while also detecting the
non-self-dual part.

## Proof narrative

1. Encode a finite-group connection by three edge labels at every vertex of
   the Cayley 2-complex and impose the relator holonomy locally.  This gives an
   honest SFT `X_K`.
2. An `H`-fixed configuration is a flat connection on the finite cover
   `H\tilde N_3`.  Rooted spanning-tree gauge fixing gives the exact identity

   ```text
   |Fix_H(X_K)| = |K|^([Lambda:H]-1) |Hom(H,K)|.
   ```

3. The homomorphism `f(x_1)=1, f(x_2)=-1, f(x_3)=0` produces an explicit
   nonorientable family `H_n`.  Restricting the same map to the orientation
   kernel produces an explicit orientable family `L_m`.
4. The Frobenius--Schur--Mednykh surface formulas give the two displayed
   fixed-point laws.
5. The orientable sequence first recovers `|K|`, then the multiplicity of each
   irreducible degree.  Even nonorientable indices recover the number of
   self-dual irreducibles of each degree.  Odd indices first recover
   `(c_d^+-c_d^-)/d`; multiplication by the already known degree recovers the
   difference between the `+1` and `-1` multiplicities.  A finite Vandermonde
   argument closes the inversion.
6. `D_8` and `Q_8` have the same degree multiset but opposite indicator on the
   unique two-dimensional irreducible.  Their orientable spectra coincide;
   their nonorientable spectra agree at even indices and differ at every odd
   index.

## Residual contribution after owner subtraction

The character formulas themselves are classical.  The residual theorem is
the construction of one surface-group SFT and two explicit cover families for
which periodic counts are jointly invertible to the full multiset
`(degree, FS indicator)`, together with the exact `D_8/Q_8` orientation
separation.  The manuscript makes no priority claim, and external release is
held pending a specialist collision search.

## Separation from P70

P69 is not a variant of P70's finite-Heisenberg calculation.  P69 acts by a
nonorientable surface group on nonabelian finite-group edge labels.  Its
periodic data are counts of flat connections on topological covers, and its
engine is complex character theory plus finite exponential-moment inversion.
P70 acts by the discrete Heisenberg group on an additive principal linear
shift over a finite field; its periodic data are kernel nullities on finite
Heisenberg quotients, and its engine is modular representation theory and
Schroedinger-block linear algebra.  The broad phrase “finite-index fixed
data” is the only shared scaffold.
