# Primary-source audit

## Exact equivalence lock

Paper 5 uses

\[
q_{t+1}=1-Aq_t^2-q_{t-1}.
\]

For \(A\ne0\), the coordinate change \(x_t=Aq_t\) gives

\[
x_{t+1}=A-x_t^2-x_{t-1}.
\]

This is precisely the \(b=-1\) Hamiltonian Hénon recurrence used by Endler and
Gallas.  Their parameter \(a\) equals our \(A\); no fitted scale or limiting
argument is involved.

## Direct primary sources

| Source | Verified content | Consequence for C12C |
|---|---|---|
| [Endler--Gallas 2002](https://doi.org/10.1103/PhysRevE.65.036231) | period-four orbital polynomial and parameter-dependent orbit marker for the two-parameter Hénon family | a parameter-varying cyclic orbit-marker curve already appears at period four |
| [Endler--Gallas 2004](https://doi.org/10.1016/j.physa.2004.06.019) | \(P_6(x,\sigma;a,b)\) and a degree-nine \(S_6(\sigma;a,b)\) whose roots label the nine genuine period-six cycles | an exact-period cyclic orbit marker at period six is explicit prior work |
| [Endler--Gallas 2006](https://doi.org/10.1016/j.physleta.2006.04.042) | for the Hamiltonian family, \(S_k=C_k^2D_kN_k\); chiral pairs share the \(C_k\) marker, while \(D_k,N_k\) are self-conjugate; explicit periods 6--8 and computations through 20 | at the displayed periods, squarefree reduction implements reversal-pair identification |
| [Gallas 2007](https://doi.org/10.1016/j.physleta.2006.08.065) | arbitrary-period Möbius formulas for all cycles, axial/parabolic points, and diagonal/non-diagonal/chiral classes | Burnside degrees and the first chiral period are already counted for every period |
| [Endler--Gallas 2006, orbital sums](https://doi.org/10.1016/j.physleta.2006.01.031) | period-five and period-six orbital sums, discriminants, and number-field structure | low-period elimination and ordinary Galois data are also prior art |
| [Hutz 2010](https://nyjm.albany.edu/j/2010/16-8p.pdf) | general dynatomic cycles for projective morphisms, including formal/primitive-period caveats | terminology precedent only; a plane Hénon automorphism is not itself a projective morphism of \(\mathbb P^2\) |

The author-hosted PDFs of the two most decisive papers are also available
directly: [conjugacy classes (2006)](https://inaesp.org/PublicJG/conjugacy_classes_PLA_356_1_2006.pdf)
and [counting formulas (2007)](https://inaesp.org/PublicJG/counting_PLA360_512_2007.pdf).

## Period-six formula lock

For the Hamiltonian family, Endler--Gallas give

\[
C_6(\sigma)=\sigma-2,
\quad D_6(\sigma)=\sigma^2+4\sigma-4A,
\]

and

\[
\begin{aligned}
N_6(\sigma,A)={}&\sigma^5+2\sigma^4-4(5A+4)\sigma^3
 +8A\sigma^2\\
&+4(16A^2+12A+9)\sigma+128A^2-96A+72.
\end{aligned}
\]

The source states \(S_6=C_6^2D_6N_6\).  The square on \(C_6\) is not a
scheme multiplicity to ignore casually: it records two cyclic orbits exchanged
by reversal and having the same marker.  The source's orbit-reconstruction
statement and the degree count show that, on the generic period-six fiber,
squarefree reduction separates exactly the eight dihedral classes.  We do not
promote this low-period fact to the unproved all-period function-field identity
\(\mathbb Q(\mathcal P_n)^{D_n}=\mathbb Q(A,\sigma)\).

## Source-table consistency note

Equations (2)--(7) of Gallas (2007) give at period 14

\[
M_{14}=1161,\qquad D_{14}=56,\qquad N_{14}=119,
\]

so the number of chiral doublets is

\[
\frac{M_{14}-D_{14}-N_{14}}2=493.
\]

The paper's displayed table appears to say 500, which is internally
inconsistent because
\(2\cdot500+56+119=1175\ne1161\).  The script compares our manual
transcription of that displayed value against the published formulas; it does
not automatically parse the PDF.  The apparent table typo does not create a
novelty opening because the general formulas are unambiguous.

## Unclaimed territory

The audit did not find a uniform theorem on the geometric monodromy or genus
growth of every normalized exact-period cover with all non-trivial
\(D_n\)-isotypic coefficient systems retained.  C12C did not define such an
object, and the present project does not claim that this harder equivariant
tower is impossible.
