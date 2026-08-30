# P125 hostile review B — round one

## Decision

**GO / GO_INTERNAL.  External release remains HOLD.**

I found no critical error, no major mathematical error, and no major
owner-scope overstatement in the repaired round-one package.  The two
Review-A repairs are genuine:

1. directed cycle decorations are now canonicalized under cyclic rotation
   only, and an asymmetric sentinel fails if reflection is reintroduced;
2. the pointwise proof now gives the matrix products and a complete
   eight-row matrix-word/landing table, rather than hiding the point periods
   behind a compressed calculation.

The quotient, pointwise depths and periods, inverse fibres, Walsh pair
census, image tower, depth layers, six literal component types, cycle
counts, and zeta product all survive independent reconstruction.  A fresh
canonical run passed \(27{,}405{,}887\) exact assertions and matched the
stored stdout byte for byte.  An independent reviewer-side implementation
added \(86{,}944\) exact checks.

Severity summary:

- **CRITICAL:** none.
- **MAJOR (mathematics):** none.
- **MAJOR (owner/scope):** none.
- **MINOR B1:** Remark 2.3 changes notation from \(\Phi\) to \(R\) in the
  quantum Yang--Baxter identity without defining \(R\).  The displayed
  witness is correct when \(R=\Phi\), but the manuscript should say
  “put \(R=\Phi\)” or use \(\Phi_{ij}\) throughout.  This is an executable
  notation repair, not a theorem failure.

The admissible claim ceiling remains the exact finite functional graph of
this literal state-gated map.  Static quadratic counts, transvection theory,
Yang--Baxter theory, generic functional-graph enumeration, and Artin--Mazur
bookkeeping receive zero contribution credit.  No priority or novelty claim
is supported by the bounded search.

## Role, material, and independence

I acted as a nonauthor Reviewer B.  I did not participate in the P125
authoring or round-one repair.  I read the current manuscript, bibliography,
round-one PDF, verifier, canonical output, support documents, and
HOSTILE_REVIEW_A.md solely to check the two requested repairs.  I did not
edit any manuscript, code, bibliography, support file, or PDF.

The pinned round-one inputs were:

- main.tex:
  505a1dd841a5e09c1ab8124634f037d1959d8b6b5812f785752a72c088ceceb9
- references.bib:
  138ccfc9deec2c31fc8fad76c7046b2f3ce6c3b34e2dba3f60f8cd64a39c3017
- code/verify.py:
  57d9770d3054d28e06ab54bf6faab57140b61dd24f3d6e7f4c7c5d70d55ba96c
- code/verification_output.txt:
  484d8734adfd36a5e562a206fc833fa13eb5240f3ebc36c67ad3c02e2b54ceb0
- main.pdf and main_round1.pdf:
  8dd8ecf6ba49912b5984b5755e8b240cfd97be0d5931e944925e5253469f6d50

The live PDF is byte-identical to the frozen round-one PDF.  The preserved
round-zero PDF was not used as mathematical evidence.

## Review-A repair audit

### A1: rotation-only directed-cycle signature — RESOLVED

The current canonicalizer is

    def canonical_cycle(sequence):
        rotations = [sequence[i:] + sequence[:i] for i in range(len(sequence))]
        return min(rotations, key=repr)

There is no reflected candidate.  The verifier then uses three distinct
rooted decorations

    asymmetric = ((), ((),), (((),),))

and asserts that its rotation class differs from the rotation class of its
reversal.  This sentinel is genuinely asymmetric: writing the entries as
\(A,B,C\), the rotation classes of \(ABC\) and \(CBA\) are disjoint.

This is the correct equivalence for a directed functional cycle.  A directed
cycle isomorphism commutes with the successor map and hence acts by a cyclic
rotation, not an arbitrary dihedral symmetry.  The literal component
traversal also passed after this repair.  The canonical assertion total
increased by exactly one, from \(27{,}405{,}886\) to
\(27{,}405{,}887\), as claimed in the improvement log.

### A2: expanded matrix-word and landing table — RESOLVED

The manuscript now displays

\[
 A_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad
 A_1=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\]

\[
 A_0^2=I,\qquad A_1^3=I,\qquad
 A_1A_0=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
 A_0A_1=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]

and records all eight quotient rows.  I multiplied the matrices
independently.  The two mixed products square to \(I\), and their fixed
equations are exactly

\[
 (A_1A_0)(x,y)=(x,y)\iff x=0,
 \qquad
 (A_0A_1)(x,y)=(x,y)\iff y=0.
\]

For the \(c=0,ab=11\) row, one \(A_1\) step lands at
\((y,x+y)\) of type \(10\), so the landing cycle shortens precisely when
\(x+y=0\), equivalently \(x=y\).  For \(c=1,ab=00\), a fixed point of
\(A_0\) would require \(x=y\), contradicting \(B(x,y)=1\).  For
\(c=1,ab=11\), the only fixed pair of \(A_1\) is \((0,0)\), again excluded.
Thus the table proves the pointwise claims rather than merely listing them.

In the PDF, the lead-in ends on page 2 and the complete table begins at the
top of page 3.  No row is split, clipped, or crowded.  The placement is
acceptable.

## Independent mathematical reconstruction

### 1. Literal map and zero-dimensional boundary

Let \((V,Q)\) be nonsingular of dimension \(2m\) over \(\mathbb F_2\), with

\[
 B(x,y)=Q(x+y)+Q(x)+Q(y),
\qquad
 \Phi(x,y)=(y,x+Q(x)y).
\]

For \(m=0\), \(V=\{0\}\), \(N=S=1\), and the sole state is fixed.  Only the
plus sign exists.  Every later formula specializes correctly to this case.
For \(m\ge1\), write

\[
 N=2^{2m},\qquad S=\varepsilon2^m,\qquad S^2=N.
\]

The two Witt signs and the counts
\(N_0=(N+S)/2\), \(N_1=(N-S)/2\) are standard background.

### 2. Three-bit quotient and all pointwise clocks

With

\[
 a=Q(x),\qquad b=Q(y),\qquad c=B(x,y),
\]

polarization gives

\[
\begin{aligned}
 Q(y)&=b,\\
 Q(x+ay)&=a+ab+ac=a(1+b+c),\\
 B(y,x+ay)&=c.
\end{aligned}
\]

Hence

\[
 (a,b,c)\longmapsto (b,a(1+b+c),c).
\]

For \(c=0\), the quotient graph is

\[
 00\to00,\qquad01\leftrightarrow10,\qquad11\to10.
\]

For \(c=1\), it is

\[
 00\to00,\qquad01\to10\to00,\qquad10\to00,\qquad11\to11.
\]

Combining these transitions with the repaired matrix table gives:

- \(c=0,00\): period \(1\) iff \(x=y\), otherwise \(2\);
- \(c=0,01\): period \(2\) iff \(x=0\), otherwise \(4\);
- \(c=0,10\): period \(2\) iff \(y=0\), otherwise \(4\);
- \(c=0,11\): depth \(1\), eventual period \(2\) iff \(x=y\), otherwise
  \(4\);
- \(c=1,00\): exact period \(2\);
- \(c=1,01\): exact depth \(2\), then exact period \(2\);
- \(c=1,10\): exact depth \(1\), then exact period \(2\);
- \(c=1,11\): exact period \(3\).

There is no unexamined quotient row or possible divisor of a listed matrix
order.  The depth-two stratum has size

\[
 A=\frac{N(N+S-2)}8.
\]

It has size \(2\) in the plus plane, \(0\) in the minus plane, and is
positive in both signs for \(m\ge2\).  This confirms the stated sharp
small-form boundary.

### 3. Braid and quantum Yang--Baxter witnesses

In a hyperbolic plane choose singular \(e,f\) with \(B(e,f)=1\), and put
\(g=e+f\), so \(Q(g)=1\).  Literal evaluation gives

\[
 \Phi_{12}\Phi_{23}\Phi_{12}(g,e,f)=(f,e,f),
 \qquad
 \Phi_{23}\Phi_{12}\Phi_{23}(g,e,f)=(f,e,e).
\]

With operators composed right-to-left, and interpreting the undefined
\(R\) in Remark 2.3 as \(R=\Phi\),

\[
 R_{12}R_{13}R_{23}(g,g,e)=(e,f,e),
 \qquad
 R_{23}R_{13}R_{12}(g,g,e)=(e,f,0).
\]

Both failures are correct.  MINOR B1 asks only that the second display
define \(R\).

### 4. Every fibre and its histogram

If \(\Phi(x,y)=(u,v)\), then \(y=u\) and

\[
 v=x+Q(x)u.
\]

The two cases \(Q(x)=0,1\) give

\[
 \Phi^{-1}(u,v)=
 \{(v,u):Q(v)=0\}\cup
 \{(u+v,u):Q(u+v)=1\}.
\]

If both candidates were equal, then \(u=0\) and the same vector \(v\) would
have to satisfy \(Q(v)=0=1\), impossible.  Thus the fibre sizes are
\(0,1,2\).

Under the bijection \((u,v)\mapsto(v,w=u+v)\), zero fibres have
\(Q(v)=1,Q(w)=0\), and double fibres have
\(Q(v)=0,Q(w)=1\).  Both counts are \(N_0N_1=N(N-1)/4\).  The remaining
targets give

\[
 d_0=d_2=\frac{N(N-1)}4,
\qquad
 d_1=N^2-d_0-d_2=\frac{N(N+1)}2.
\]

The edge-mass check
\(d_1+2d_2=N^2\) closes the histogram.

### 5. Walsh pair census

For

\[
 C_{abc}=\#\{(x,y):Q(x)=a,Q(y)=b,B(x,y)=c\},
\]

expanding three binary indicators produces

\[
\begin{aligned}
8C_{abc}={}&N^2+(-1)^aNS+(-1)^bNS+(-1)^{a+b}S^2\\
&+(-1)^cN
\{1+(-1)^a+(-1)^b+(-1)^{a+b}S\}.
\end{aligned}
\]

The four polar character sums are \(N,N,N,NS\); the last follows from
\(Q(x)+Q(y)+B(x,y)=Q(x+y)\).  Substituting \(S^2=N\) gives exactly

\[
\begin{aligned}
H=C_{000}&=\frac{N(N+3S+4)}8,\\
M=C_{010}=C_{100}=C_{110}&=\frac{N(N-S)}8,\\
A=C_{001}=C_{011}=C_{101}&=\frac{N(N+S-2)}8,\\
Z=C_{111}&=\frac{N(N-3S+2)}8.
\end{aligned}
\]

I checked every sign in the unsimplified expression.  The \(m=0\), plus
plane, and minus-plane specializations are integral and agree with literal
enumeration.

### 6. Image tower and depth layers

For a target of type \((a,b,c)\), the two inverse candidates occur according
to

\[
 {\bf1}_{b=0}+{\bf1}_{a+b+c=1}.
\]

This gives the displayed fibre table

\[
\begin{array}{c|cccc}
c&00&01&10&11\\ \hline
0&1&1&2&0\\
1&2&0&1&1.
\end{array}
\]

The first image is therefore the recurrent set together with the
\((c,a,b)=(1,1,0)\) stratum.  That extra stratum maps in one step to
\((1,0,0)\), while each recurrent point has arbitrarily long predecessors
along its cycle.  Thus the claimed equality is setwise:

\[
 \operatorname{im}\Phi^2=\operatorname{Rec}(\Phi),
\]

not merely an equality of cardinalities.  It follows that

\[
 |\operatorname{im}\Phi|=\frac{N(3N+1)}4,
\qquad
 |\operatorname{im}\Phi^t|
 =\frac{N(5N-S+4)}8\quad(t\ge2),
\]

and

\[
 L_2=A,\qquad L_1=M+A=\frac{N(N-1)}4,
\qquad
 L_0=N^2-L_1-L_2=\frac{N(5N-S+4)}8.
\]

All \(t=0\), \(t=1\), \(m=0\), and minus-plane boundaries are explicit and
correct.

### 7. Six directed functional components

The forward quotient and the inverse table determine the reverse trees:

1. In \(c=0,00\), the map is the swap.  The \(N_0\) diagonal states are
   fixed, and the remaining states give \((H-N_0)/2\) bare 2-cycles.
   Targets of this type have indegree one, so no tree is attached.
2. The \(c=0\) mixed types alternate.  The \(N_1\) cycles containing a zero
   coordinate have length two; their type-10 vertex has one type-11 leaf.
3. The remaining mixed states form \((M-N_1)/2\) 4-cycles.  Each has
   type-10 vertices in the two alternating positions, and each of those
   vertices has one type-11 leaf.
4. Each \(c=1,00\) exact 2-cycle has, at each cycle vertex, the chain
   \(01\to10\to00\).  This gives \(A/2\) components with two length-two
   tails.
5. The \(c=1,11\) states form \(Z/3\) bare 3-cycles.

The type-11 leaves in \(c=0\) and type-01 leaves in \(c=1\) have zero
indegree.  Since the global indegree ceiling is two, no deeper or branched
tree is missing.  This proves exactly the six table rows.  The repaired
rotation-only canonicalizer is consistent with these directed placements;
in particular, “alternating” is not accidentally replaced by an undirected
dihedral convention.

### 8. Cycle census and zeta

Adding the component cycles gives

\[
\begin{aligned}
c_1&=\frac{N+S}{2},\\
c_2&=\frac{N^2+2NS+3N-6S}{8},\\
c_3&=\frac{N(N-3S+2)}{24},\\
c_4&=\frac{N^2-NS-4N+4S}{16}.
\end{aligned}
\]

There are no other recurrent periods, so the usual cycle product is

\[
 \zeta_\Phi(t)=
 (1-t)^{-c_1}(1-t^2)^{-c_2}
 (1-t^3)^{-c_3}(1-t^4)^{-c_4}.
\]

The conversion from cycle counts to this product is routine and is
correctly zero-credited.

## Fresh exact verification

From the paper directory I ran

    set -o pipefail
    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py |
      cmp - code/verification_output.txt

Result:

    fresh_stdout_byte_compare_exit=0

The canonical transcript ends with

    ASSERTIONS 27405887
    PASS

It contains the zero-dimensional plus lane and both Witt signs for
\(1\le m\le5\).  The largest lane has \(|V|=1024\) and
\(|V|^2=1{,}048{,}576\) literal states.  The run checks the literal update,
polarization, quotient, every state orbit, every target fibre, pair counts,
image sets, depth layers, cycles, and actual connected components.  It uses
no sampling, floating point, external CAS, or network access.

I also ran an independently written, ephemeral standard-library control over
the \(m=0\) plus case and both signs for \(1\le m\le3\).  It did not import
the paper verifier.  It reconstructed all successors and predecessors,
checked every quotient transition and orbit, all inverse candidates and
Walsh counts, literal set equality
\(\operatorname{im}\Phi^2=\operatorname{Rec}(\Phi)\), all layers and cycles,
directed component decorations, the asymmetric reflection sentinel, the
four matrix identities, and both Yang--Baxter witnesses.  It returned

    independent reviewer control: PASS
    ASSERTIONS 86944

These computations are falsification evidence; the symbolic arguments above
support the all-dimension statements.

## Owner and internal-collision audit

### External owner subtraction

The exact search was repeated through 2026-08-30 with the literal formula
and the following families of formulations:

- \((y,x+Q(x)y)\), \(x+Q(x)y\), and \(x+q(x)y\);
- quadratic-form switch, quadratic-state shear, and state-dependent
  transvection over \(\mathbb F_2\);
- finite-field ordered-pair dynamics and Fibonacci/shear map;
- braid switch, rack/biquandle switch, and bijective or nonbijective
  set-theoretic Yang--Baxter map;
- orthogonal-equivariant maps on \(V\times V\);
- exact image, fibre, component, and cycle descriptions.

No primary source in this bounded search states or classifies the literal
map, a conjugate map, or the complete theorem conjunction above.  This is
only a bounded non-hit.  The formula is short enough that a missed direct
owner remains a serious possibility, so external HOLD is necessary.

The cited owner regions were checked against primary or publisher-hosted
records:

- J. D. Fulton, “Representations by Quadratic Forms in a Finite Field of
  Characteristic Two,” Mathematische Nachrichten 77 (1977), 237–243,
  [DOI 10.1002/mana.19770770117](https://doi.org/10.1002/mana.19770770117),
  is an appropriate static quadratic-count boundary.
- J. Sjöstrand, “Orbits under Dual Symplectic Transvections,” Linear Algebra
  and its Applications 710 (2025), 507–530,
  [DOI 10.1016/j.laa.2025.02.010](https://doi.org/10.1016/j.laa.2025.02.010),
  studies fixed-vector symplectic transvections and their invertible group
  action.  It does not own this state-gated nonbijective pair map.
- P. Etingof, T. Schedler, and A. Soloviev, “Set-Theoretical Solutions to
  the Quantum Yang--Baxter Equation,” Duke Mathematical Journal 100 (1999),
  169–209,
  [DOI 10.1215/S0012-7094-99-10007-X](https://doi.org/10.1215/S0012-7094-99-10007-X),
  is a direct owner of the classical bijective set-theoretic solution
  region.
- F. Catino, I. Colazzo, and P. Stefanelli, “Set-Theoretic Solutions to the
  Yang--Baxter Equation and Generalized Semi-Braces,” Forum Mathematicum 33
  (2021), 757–772,
  [DOI 10.1515/forum-2020-0082](https://doi.org/10.1515/forum-2020-0082),
  explicitly includes nonbijective finite-order solutions.  The present map
  fails the defining identities and is not presented as a solution.
- M. Artin and B. Mazur, “On Periodic Points,” Annals of Mathematics 81
  (1965), 82–99,
  [DOI 10.2307/1970384](https://doi.org/10.2307/1970384),
  owns the zeta background.

The manuscript subtracts these areas accurately.  It does not use a search
non-hit as evidence of novelty, and it explicitly says that a direct prior
classification would supersede the residual claim.

### Internal collision ceiling

The internal firewall is correctly scoped:

- P99 is a fixed bijective unipotent action on integer sublattices, not a
  quadratic state-gated map.
- P103 uses adjugate/rank and scalar-power dynamics, not the present
  quadratic/polar quotient.
- P106 is the closest shallow finite-map silhouette, but its depth and
  periods stop at one and two; it has no Witt-sensitive pair census.
- P109 is a nilpotent subspace-image process with one recurrent state.
- P118 already occupies quotient/fibre/basin/zeta package architecture, but
  on a multipartite mex carrier with a labelled-EGF engine.

A broader source scan also encounters P102 and other algebraic finite
functional graphs, but none shares the literal map, the three-bit quotient,
the nonuniform two-candidate fibres, or the six Witt-sensitive components.
The manuscript correctly claims no value for the generic package.  Its
residual is only the exact conjunction for this map.

## Isolated four-stage build and artifact audit

I copied only main.tex and references.bib into a fresh temporary directory
and ran:

1. pdflatex with nonstop and halt-on-error;
2. bibtex;
3. pdflatex with the same flags;
4. pdflatex with the same flags.

All stages returned zero:

    stages=0/0/0/0

The settled fourth-stage log and BLG had:

- zero LaTeX or package warnings;
- zero errors;
- zero undefined references or citations;
- zero rerun requests;
- zero overfull or underfull boxes;
- all \(6/6\) bibliography keys cited and resolved.

The isolated PDF had SHA-256

    8dd8ecf6ba49912b5984b5755e8b240cfd97be0d5931e944925e5253469f6d50

and was byte-identical to both main.pdf and main_round1.pdf.

Artifact checks:

- 5 pages;
- 367,956 bytes;
- A4, rotation \(0\);
- Author, Title, Subject, and Keywords metadata empty;
- no CreationDate or ModDate reported;
- no custom metadata or metadata stream;
- no form, JavaScript, encryption, or embedded file;
- 26 fonts, all embedded, subsetted, and Unicode-mapped;
- no text sentinel such as “??”, “[?]”, “undefined”, TODO, TBD, FIXME,
  VERIFY, internal-draft text, or review-round leakage.

I rendered and visually inspected all five pages at high resolution.  There
is no clipping, overlap, missing glyph, broken link text, unresolved marker,
or malformed formula.  The repaired matrix table is complete and legible on
page 3; the component table and zeta display fit cleanly on page 4; all six
references are visible on page 5.  The generous unused lower space on the
last page is harmless.

The qpdf utility was unavailable in the environment; pdfinfo, pdffonts,
pdftotext, pdfdetach, direct PDF rendering, and byte comparison supplied the
reported checks.  pdfdetach reported zero embedded files.

## Severity-ranked actionable findings

### CRITICAL

None.

### MAJOR (mathematics)

None.  All displayed formulas, implications, and small-parameter boundaries
are provable as stated.

### MAJOR (owner/scope)

None.  The manuscript stays below the evidence ceiling, itemizes zero-credit
background, uses bounded non-hit language, and keeps external release on
hold.

### MINOR

**B1 — define \(R\) in Remark 2.3.**  The quantum Yang--Baxter display uses
\(R_{12}R_{13}R_{23}\) after the paper has defined only \(\Phi\).  Add
“put \(R=\Phi\)” immediately before the display, or replace every \(R\) by
\(\Phi\).  The two computed triples are already correct.

## Claim ceiling and final verdict

The internally admissible contribution is:

1. the exact three-bit quotient and complete pointwise depth/period table for
   \(\Phi(x,y)=(y,x+Q(x)y)\);
2. every target fibre and the \(0/1/2\) histogram;
3. the setwise image tower and exact Witt-sensitive depth layers;
4. the six directed decorated component types and their counts;
5. the resulting exact cycle census and routine zeta corollary; and
6. explicit proof that this particular map is neither a braid switch nor a
   quantum Yang--Baxter solution.

The paper must not claim ownership of quadratic-form counts, transvection
orbits, Yang--Baxter theory, generic functional-graph methods, zeta
conversion, first occurrence, or novelty.  It presently obeys that ceiling.

**Final verdict: GO / GO_INTERNAL, with MINOR B1 recommended before the next
freeze.  External posting, submission, priority language, and release remain
HOLD.**
