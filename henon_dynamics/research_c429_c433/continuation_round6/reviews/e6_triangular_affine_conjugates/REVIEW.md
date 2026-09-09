# R6 E6 — Independent review of single triangular conjugates of A

2026-09-10 UTC. Bounded internal, nonauthor, hand-only mathematical review.

## 1. Verdict and actual source binding

**PASS; zero mathematical or source-related must-fix findings.**

For every
\[
E(x,y)=(\alpha x+c,\beta y+f(x)),\qquad
\alpha,\beta\in\{1,-1\},\quad c\in\mathbb Z,\quad f\in\mathbb Z[t],
\]
the condition \(E^{-1}AE(C)=C\) implies
\[
(E^{-1}AE)|_C\in\{a,iai,a^{-1},ia^{-1}i\}.
\]
Thus adjoining these restrictions cannot enlarge the previously established
\(\langle a,i\rangle\cong S_3\times C_3\).

I read all of the new Section 6, lines 292–378, of the actual
[C2 report](../../c2_nine_point_stabilizer/REPORT.md), and reread the frozen
first 155 lines supplying \(C,A,I,q,a,i\) and the existing restriction group.
Section 5 is not reviewed or used as a premise. The byte bindings are:

| Artifact scope | SHA-256 |
| --- | --- |
| Current complete 378-line C2 report | cbab243d0092fced85a85c02a1a02339b9e7d184566e92595364ad829625f87e |
| Unchanged first 290 lines, integrity check only | 062341bd7dfd496b6884876118600a3bbfffed66e719dac613570bf4ad5d350f |
| Actual dependency, frozen first 155 lines | d28b4671f8380ff2927fdd20ec7ceef04ce3a4f988650a448deeeaf1b22474dc |

The complete-file and prefix hashes bind scope; they do not replace the
independent mathematical checks below. Labels, when used, are C2's \(1\)–\(9\).
No old review or author file was modified. Only this new review was written;
there was no mathematical program, external-model/API call, new agent, Git
operation, PDF, coefficient search or checker rerun.

## 2. Centroid forces the original first-coordinate fibers

The displayed \(E\) is an integral polynomial automorphism, with inverse
\[
E^{-1}(u,v)=
\bigl(\alpha(u-c),\,\beta[v-f(\alpha(u-c))]\bigr).
\]
Consequently \(C'=E(C)\) has nine distinct points, and the hypothesis is
equivalent to \(A(C')=C'\), with no assumption that \(E\) itself preserves \(C\).

For an affine map, averaging commutes with applying the map; hence the
centroid of \(C'\) is fixed by \(A(x,y)=(1-y,x-y)\).
The equations \(x=1-y\), \(y=x-y\) give the unique fixed point
\((2/3,1/3)\). Summing the actual nine coordinates of \(C\) gives
\(\sum x=6\), \(\sum y=3\), the same centroid.
The first-coordinate average therefore forces
\[
\frac{2\alpha}{3}+c=\frac23.
\]
For \(\alpha=-1\) this gives the impossible integral value \(c=4/3\).
For \(\alpha=1\) it gives \(c=0\). Thus every surviving \(E\) fixes the
first coordinate, including when \(\beta=-1\) and for arbitrary degree of \(f\).
The five first-coordinate multiplicities of \(C'\) are exactly
\[
(m_{-1},m_0,m_1,m_2,m_3)=(2,2,3,1,1).
\]

## 3. Exhaustive finite intermediate-set classification

The actual formula \(A^2(x,y)=(1-x+y,1-x)\) shows that membership of the
first coordinates of \(P,AP,A^2P\) in \([-1,3]\) forces
\[
-1\le x\le3,\qquad -2\le y\le2,\qquad |x-y|\le2.
\]
The resulting integral rows can be reconstructed without any search:

| \(x\) | All permitted heights \(y\) | Count |
| --- | --- | --- |
| \(-1\) | \(-2,-1,0,1\) | 4 |
| \(0\) | \(-2,-1,0,1,2\) | 5 |
| \(1\) | \(-1,0,1,2\) | 4 |
| \(2\) | \(0,1,2\) | 3 |
| \(3\) | \(1,2\) | 2 |

Direct substitution into \(A\), including each last-to-first arrow, gives
the following six disjoint cycles; together they contain every row entry:

\[
\begin{array}{c|ccc}
O_1&(0,0)&(1,0)&(1,1)\\
O_2&(3,1)&(0,2)&(-1,-2)\\
O_3&(-1,0)&(1,-1)&(2,2)\\
O_4&(-1,-1)&(2,0)&(1,2)\\
O_5&(-1,1)&(0,-2)&(3,2)\\
O_6&(0,-1)&(2,1)&(0,1)
\end{array}
\]

This checks both completeness and actual orbit membership, not only a count
of 18 candidate points. Since \(A^3=1\) and its unique fixed point is not
integral, an invariant nine-point subset is a union of exactly three cycles.
Their first-coordinate multiplicity vectors are
\[
\begin{array}{c|ccccc}
&-1&0&1&2&3\\ \hline
O_1&0&1&2&0&0\\
O_2&1&1&0&0&1\\
O_3&1&0&1&1&0\\
O_4&1&0&1&1&0\\
O_5&1&1&0&0&1\\
O_6&0&2&0&1&0 .
\end{array}
\]
Multiplicity one at \(x=3\) requires exactly one of \(O_2,O_5\).
Multiplicity two at \(x=-1\) then requires exactly one of \(O_3,O_4\).
The remaining cycle must be \(O_1\), since the chosen two contribute only
one point at \(x=1\), while \(O_1\) contributes two and \(O_6\) contributes zero.
Each of the resulting four combinations has the entire required vector.
Thus the four claimed candidates, and no others, survive the multiplicities.

At \(x=-1\), the original fiber is \(\{-2,0\}\), of gap two.
The choices \((O_2,O_4)\) and \((O_5,O_3)\) instead give
\(\{-2,-1\}\) and \(\{0,1\}\), respectively, both of gap one.
The map \(y\mapsto\beta y+f(-1)\) preserves the absolute gap, so both mixed
choices are impossible for either sign of \(\beta\).
The only surviving intermediate sets are
\[
C=O_1\cup O_2\cup O_3,\qquad D=O_1\cup O_5\cup O_4.
\]

## 4. Exact maps to the two surviving sets

Let \(R(x,y)=(x,x-y)\). Directly, \(R^2=1\);
it sends \(O_1\) to \(O_1\), \(O_2\) to \(O_5\), and \(O_3\) to \(O_4\).
Thus \(R(C)=D\), with actual equality of the listed sets.
Moreover
\[
RAR(x,y)=(1-x+y,1-x)=A^2(x,y)=A^{-1}(x,y).
\]
This is a genuine global identity, not an inferred identity of restrictions.

For each supported first coordinate \(t\), write
\(S_t=\{y:(t,y)\in C\}\). The already checked polynomial \(q\) satisfies
\(q(t)-S_t=S_t\); its five values are \((-2,2,0,4,2)\).
The corresponding fiber of \(D\) is \(t-S_t\).
A translation between two finite nonempty subsets of the line, if it exists,
is unique by comparing their minima. A reflection parameter is likewise
unique, since the source minimum maps to the target maximum.
It follows that:

| Target \(C'\) | \(\beta\) | Forced \(f(t)\) on all five supported \(t\) | Exact \(E\vert_C\) |
| --- | --- | --- | --- |
| \(C\) | \(1\) | \(0\) | \(1\) |
| \(C\) | \(-1\) | \(q(t)\) | \(I\vert_C\) |
| \(D\) | \(-1\) | \(t\) | \(R\vert_C\) |
| \(D\) | \(1\) | \(t-q(t)\) | \((RI)\vert_C\) |

For the last row, \(t-S_t=S_t+(t-q(t))\), since \(q(t)-S_t=S_t\).
Also \(RI(x,y)=(x,y+x-q(x))\), so this is an actual triangular polynomial
map of the prescribed form. All four rows are realized globally by
\(1,I,R,RI\), respectively; their polynomials lie in \(\mathbb Z[t]\).
No sufficiency claim about arbitrary integer interpolation is needed.
Other polynomials agreeing at these five values have the same restriction,
and the argument nowhere bounds their degree or coefficients.

## 5. The inverse restrictions have the correct domains

If \(E|_C=F|_C\) for one of the four displayed maps, then both are bijections
\(C\to C'\). For every \(w\in C'\), the unique inverse image in \(C\)
is therefore the same: \(E^{-1}(w)=F^{-1}(w)\).
Since \(A(C')=C'\), it follows on \(C\) that
\[
E^{-1}AE=F^{-1}AF.
\]
In the two cases with \(C'=D\), this argument uses the inverse on \(D\);
it does not substitute an unproved equality of inverse maps on \(C\).
In particular, \((RI)^{-1}=IR\), not \(RI\). The four conjugate restrictions
are consequently
\[
a,\qquad iai,\qquad (RAR)|_C=a^{-1},\qquad
(IRARI)|_C=ia^{-1}i .
\]
This verifies the stated list while allowing the intermediate map to leave
\(C\). Each belongs to the existing restriction group, so arbitrary products
of the allowed new set-preserving conjugates still lie in that group.
The no-nine-cycle conclusion uses this group inclusion and its established
\(S_3\times C_3\) structure, not the insufficient observation that each
individual conjugate has order three.

## 6. Disposition and unproved boundary

All new reasoning is supplied by affine identities, finite sets, integer
coordinates and fiberwise isometries. No external theorem, Section 5 claim,
numerical evidence or new literature attribution is required.
The research-review and henon-route-a-batch skills were used for actual-file,
nonauthor checking and explicit claim boundaries; their external-model,
integration and release workflows were not executed.

The proposition fully closes this single vertical triangular conjugator
class. It does not classify arbitrary tame conjugators or general returning
words with multiple intermediate sets and changing triangular directions.
It neither produces nor excludes integral period nine for that larger class,
does not settle the complete native integer period spectrum, and supplies
no new contract-admission decision. No author correction is required.
