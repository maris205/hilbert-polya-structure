# Source and convention audit

## Literal permutation

The frozen object is

\[
\pi_0=\begin{pmatrix}1&2&3&4\\4&3&2&1\end{pmatrix}.
\]

It is irreducible because the top and bottom prefix sets differ at widths
one, two, and three.  It is the four-letter hyperelliptic central permutation,
after a literal relabeling of the alphabet used by Avila--Matheus--Yoccoz.
The program finds exactly seven labeled states and fourteen directed edges,
in agreement with the hyperelliptic word model of lengths below three.

The crossing form is

\[
\Omega_0=
\begin{pmatrix}
0&1&1&1\\
-1&0&1&1\\
-1&-1&0&1\\
-1&-1&-1&0
\end{pmatrix}.
\]

Its determinant is one and its rank is four.  Thus \(2g=4\).  Since the
number of exchanged intervals satisfies \(d=2g+s-1\), one obtains \(s=1\);
the unique zero has order \(2g-2=2\).  The stratum is \(\mathcal H(2)\), and
the relative-to-absolute kernel vanishes in this example.

## Labeled move and matrix convention

Let \(\alpha_t\) and \(\alpha_b\) be the rightmost top and bottom labels.

- In a `t` move, \(\alpha_t\) wins and \(\alpha_b\) loses; remove the loser
  from the bottom row and insert it immediately after the winner.
- In a `b` move, \(\alpha_b\) wins and \(\alpha_t\) loses; make the analogous
  change in the top row.

The forward chronological homology matrix is

\[
B_e=I+E_{\mathrm{loser},\mathrm{winner}}.
\]

For a path \(e_1,\ldots,e_n\),

\[
B_w=B_{e_n}\cdots B_{e_1}.
\]

This is the transpose of the common column-length visitation convention.
Mixing the two is a chronology error, not a cosmetic transpose.

The code stays in fixed labels.  Under the relabeling
\(-3,-1,1,3\mapsto1,2,3,4\), the AMY central vertex is literally \(\pi_0\).
A bottom move gives the fixed-label state `1423/4321`; a reduced convention
that renumbers the top row to the identity may instead display one-line
`2431`.  The program never performs this second renumbering, and matrices
from the two conventions are not mixed.

The open-edge identity is

\[
B_e\Omega_{\rm src}B_e^T=\Omega_{\rm dst}.
\]

Therefore open edges transport a symplectic lattice bundle.  They do not all
preserve \(\Omega_0\).  For a closed loop at a state \(v\), inversion gives

\[
B_w^T J_v B_w=J_v,
\qquad J_v=\Omega_v^{-1}.
\]

A deterministic spanning tree supplies integral frames between all seven
fibers; the certificate verifies all fourteen fixed-frame matrices exactly.

## Periodic and accelerated data

Entrywise positivity depends on the cyclic cut, so it is not used after an
arbitrary canonical rotation.  A free cycle passes only if every cyclic phase
matrix is eventually positive.  For a four-by-four nonnegative matrix the
Wielandt bound makes the exact finite test \(M^q>0\) for some \(q\le10\);
the observed maximum is three.

All original elementary edges are retained.  The ledger additionally stores
maximal cyclic runs of `t` and `b`, namely the combinatorial
same-type/Zorich-run itinerary, and the exact first-return branch words at the
central state.  These derived records never replace the chronological
product; a `(type,length)` run list is interpreted only together with the
retained labeled edge tokens and start state.  This release does not construct
an accelerated roof or a canonical analytic Zorich transfer space.

For an eventually positive closed path, the Perron eigenvector realizes the
periodic projective induction.  Indeed, if
\(M=B_{e_n}\cdots B_{e_1}\), the column-length visitation product is
\(R=M^T=R_{e_1}\cdots R_{e_n}\), where \(R_e=B_e^T\).  Let
\(v>0\) satisfy \(Rv=\rho v\), set \(\lambda^{(0)}=v\), and set
\(\lambda^{(n)}=v/\rho\).  Reconstruct the intermediate vectors by the
factored relation \(\lambda^{(k-1)}=R_{e_k}\lambda^{(k)}\).  Since
\(R_{e_k}=I+E_{w_k,\ell_k}\),
\[
\lambda^{(k-1)}_{w_k}
=\lambda^{(k)}_{w_k}+\lambda^{(k)}_{\ell_k}
>\lambda^{(k)}_{\ell_k}
=\lambda^{(k-1)}_{\ell_k}.
\]
Every prescribed Rauzy comparison is strict, and the ray returns with scale
\(1/\rho\).  For the normalized induction, the roof telescopes to
\(\log(\|\lambda^{(0)}\|_1/\|\lambda^{(n)}\|_1)=\log\rho\); proper
repetitions obey the clock exactly.

Throughout, primitive means ``not a proper power'' as a closed directed
edge-token word in the fixed-label Rauzy coding, modulo cyclic rotation only.
Each selected word therefore gives a primitive periodic point of the labeled
projective Rauzy return map.  The project does not audit the possible forgetful
identifications produced by erasing interval labels, the marked separatrix,
or other marking data.  Thus the counts 828, 146, and 21 are coded-orbit
counts; they are not asserted to count pairwise distinct or primitive closed
Teichmüller geodesics in unmarked moduli space.  The singular-weight
obstruction survives: every selected code is an admissible periodic ray, and
one singular monodromy already prevents the regular point formula from
defining a finite weight on the full coded system.

## Metaplectic boundary

After a symplectic trivialization, each edge/return matrix lies in a fixed
real symplectic group and has two metaplectic lifts.  No endpoint matrix alone
chooses between them.  The coherent lift/sign remains unresolved required
data; the project takes no quotient by it.  The atomic theorem applies
uniformly to any coherent choice and aggregates equal projected atoms only
after inserting their actual central signs.

Thomas's Weil character is a distribution.  On the regular set
\(\det(g-I)\ne0\), it is represented by a phase (depending on the lift and
Weil/Maslov convention) times \(|\det(g-I)|^{-1/2}\).  This value is not the
ordinary Hilbert-space trace of the single unitary \(\mu(\widetilde g)\).
On \(\det(g-I)=0\), even this regular point-value formula is unavailable.

## Primary controls

1. J.-C. Yoccoz, *Interval exchange maps and translation surfaces*, Pisa
   lectures, especially the Rauzy moves, crossing form, genus/stratum, and
   cocycle sections:
   <https://www.college-de-france.fr/sites/default/files/documents/jean-christophe-yoccoz/UPL15305_PisaLecturesJCY2007.pdf>.
2. A. Avila, C. Matheus, and J.-C. Yoccoz, *Zorich conjecture for
   hyperelliptic Rauzy--Veech groups*, especially Sections 2.1--2.2:
   <https://arxiv.org/abs/1606.01227>.
3. A. Zorich, *Flat Surfaces*, for labeled/reduced conventions and Zorich
   acceleration:
   <https://math.uchicago.edu/~masur/zorich_leshouches.pdf>.
4. T. Thomas, *The Character of the Weil Representation*, for the
   distribution character, regular set, determinant amplitude, and
   Weil/Maslov phase:
   <https://arxiv.org/abs/math/0610644>.

The classical Rauzy/KZ and Weil results are inputs.  The claimed C24 delta is
only their exact compatibility obstruction for the frozen ordinary Fredholm
proposal.
