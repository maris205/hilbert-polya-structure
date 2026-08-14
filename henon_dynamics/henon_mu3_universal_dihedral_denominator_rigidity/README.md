# HCS-C54: universal dihedral symmetry and split-denominator rigidity

Status: **DOCS_FINAL_NO_MORE_EDITS against the persistent scoped code/results
RELEASE_CANDIDATE and 44-entry full-project inventory; implementation-commit
provenance remains pending**.

The source lock is the rationally descended HCS-C53 family.  Put

\[
K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0,
\]

and, for \(n\ge2\) and \(N=2n\), put

\[
C_n=\sum_{i=0}^{N-1}x_i^3,
\qquad
Q_{n,\rho}=\sum_{i=0}^{N-2}x_ix_{i+1}+\rho x_{N-1}x_0.
\]

## Result in one paragraph

For every \(n\ge2\), the full **projective monomial stabilizer of the
homogeneous ideal** \((C_n,Q_{n,\rho})\) is

\[
G_n\cong\operatorname{Dih}(C_{3n}),\qquad |G_n|=6n.
\]

This is not a classification of the full projective linear automorphism
group.  The HCS-C53 semilinear reversal transports the generators by
\(r\mapsto r^{-1}\) and \(s\mapsto rs\).  It therefore produces a
nonconstant finite etale \(\mathbf Q\)-group scheme \(\mathscr G_n\) of
rank \(6n\), split by \(K\), with exactly two rational geometric elements.
Both assertions are equation-level theorems for every \(n\); neither uses
smoothness.

For a packet-admissible smooth row, let the rational pure packets
\(\mathsf E_n\) and \(\mathsf O_n\) have weights zero and one and ranks

\[
e_n=\frac{4^n+5}{3},\qquad
o_n=\frac{2(4^n-4)}3.
\]

Here **ordinary** is project shorthand for realization by an actual
finite-rank compatible system with integral multiplicities, not \(p\)-adic
or Newton-polygon ordinarity.

An actual finite-rank rational compatible system realizes the
complete prescribed split-local exponent \(4/n\) if and only if
\(n\mid4\).  Thus the only rows \(n\ge2\) are \(n=2,4\).  HCS-C53
certifies the required pure packet data only for \(n=2,3,4\); every statement
about later rows is conditional on construction of the stated packets.  No
semisimplicity theorem is inherited from HCS-C53.  In the necessity proof,
one fixes \(\ell\) and applies Brauer--Nesbitt to semisimplifications, which
preserve traces, characteristic polynomials, ranks, and purity.

At \(n=3\), an exact character calculation over the common geometric group
\(G_3=\operatorname{Dih}(C_9)\) proves that no nonzero central
source-isotypic sector clears the \(4/3\) denominator on both pure rails.
This common-group theorem is first a theorem over \(K\).  The standard
rational Fermat form and the HCS-C53 complete-intersection form are not
silently treated as representations of the same rational group scheme.

## Proof firewall

Proved here:

- the exhaustive all-\(n\) projective-monomial ideal stabilizer;
- its nonconstant rational group form and its two rational points;
- split-trace and complete split-factor ordinary realization exactly when
  \(n\mid4\), for packet-admissible rows;
- the exact \(n=3\) common-geometric-group character and central-sector
  no-go;
- the counterpacket statement that a split-invisible virtual rational class
  restricts to zero over \(K\) and cannot alter a \(K\)-rail rank or
  isotypic multiplicity.

Not claimed:

- that \(G_n\) is the full automorphism group in \(\operatorname{PGL}\);
- smoothness, a Chow motive, or a compatible packet for \(n\ge5\);
- that all \(6n\) geometric automorphisms descend as rational points;
- a global or inert-prime fractional Euler root;
- uniqueness of a rational extension from split traces;
- automorphy, meromorphic continuation, a functional equation, or RH.

The persistent scoped code/results release-candidate tuple, 44-entry
full-project inventory, and frozen PDF digest are recorded in
INTEGRITY_REPORT.md.  Only the implementation-commit provenance remains for a
later stage.  No theorem depends on that later identifier, and its backfill
must not reopen the paper.
