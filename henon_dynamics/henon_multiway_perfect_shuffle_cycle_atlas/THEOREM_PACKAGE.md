# Theorem package

Fix integers \\(k\\ge2\\), \\(n\\ge1\\), set \\(M=kn+1\\), and let
\\(D_M=\\{1,\\ldots,M-1\\}\\).  The frozen multiway perfect shuffle is
\\[
  \\rho(i)=ki\\pmod M.
\\]
Since \\(M\\equiv1\\pmod k\\), \\(\\gcd(k,M)=1\\); hence \\(\\rho\\) permutes
\\(D_M\\).  For every iterate \\(r\\ge1\\), the fixed congruence is
\\((k^r-1)i\\equiv0\\pmod M\\).  It has \\(\\gcd(k^r-1,M)\\) residue solutions
including zero, so
\\[
  F_r=\\operatorname{Fix}(\\rho^r)=\\gcd(k^r-1,M)-1.                 \\tag{1}
\\]

The gcd of a position with \\(M\\) is invariant.  For a card position \\(i\\),
write \\(q_i=M/\\gcd(i,M)\\).  Its least period is exactly
\\[
  \\tau(i)=\\operatorname{ord}_{q_i}(k),                              \\tag{2}
\\]
because \\(q_i\\) is the smallest modulus on which the congruence
\\(k^r i\\equiv i\\) reduces to \\(k^r\\equiv1\\).  If
\\(E_r\\) denotes the number of points of exact period \\(r\\), Möbius inversion
and cyclic phase division give
\\[
  E_r=\\sum_{d\\mid r}\\mu(r/d)F_d,\\qquad C_r=E_r/r.                 \\tag{3}
\\]
All \\(C_r\\) are nonnegative integers and vanish unless \\(r\\mid
\\operatorname{ord}_M(k)\\).  Direct cycle traversal exhausts \\(D_M\\), so the
finite atlas is a completeness check rather than a fitted period sample.

For the permutation matrix \\(P\\) (or its Koopman action \\(U\\)), each cycle of
length \\(r\\) contributes one factor.  The source-local dynamical zeta and
characteristic polynomial therefore are
\\[
 Z_{k,n}(z)=\\prod_{r\\ge1}(1-z^r)^{-C_r},\\qquad
 \\det(\\lambda I-U)=\\prod_{r\\ge1}(\\lambda^r-1)^{C_r}.              \\tag{4}
\\]
These are finite products for each parameter pair.  The exact receipt covers
\\(2\\le k\\le6,1\\le n\\le10\\), all positions in seven additional pairs, and
small zeta-denominator and Koopman-polynomial coefficient rows checked
independently by SymPy.

This is a source-local permutation theorem.  The modulus, card labels and
one-shuffle clock have no intrinsic rational-prime carrier or logarithmic
weight; (4) is not asserted to be a target divisor, Euler product, zero set,
or Hilbert--Pólya operator.
