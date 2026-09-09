# R6 E6 — Independent review of the nine-point reflection-direction classification

2026-09-10 UTC. Bounded, nonauthor, proof-only review.

## 1. Verdict and inspected scope

**PASS: zero mathematical or source-related must-fix findings.**

The complete claim in E2's report is proved for its precisely specified class:
single triangular reflections in integral unimodular affine coordinates that
individually preserve the frozen nine-point set. There are exactly three
nonidentity induced permutations. Adding all such restrictions to the known
affine permutation leaves the group \(S_3\times C_3\), so this operation cannot
produce a nine-cycle.

This is not a classification of the full integral tame stabilizer, not a
nonexistence theorem for integral period nine, not a solution of the complete
native integer period spectrum, and not a new fifth contract.

I read the whole 407-line
[E2 report](../../e2_nine_reflection_directions/REPORT.md), and the actual
frozen first 155 lines, Sections 1–4, of the dependent
[C2 report](../../c2_nine_point_stabilizer/REPORT.md).
The C2 file has subsequently acquired an appendix; none of that additional
material is a premise of this review or certified here.

The source bindings are:

| Inspected source | SHA-256 |
| --- | --- |
| E2 REPORT.md, all 407 lines | 8b3c3da72824eb1c53aee2728f05bcbfcac673085bc18a339ffcc0214051fa73 |
| C2 REPORT.md, exactly its first 155 lines | d28b4671f8380ff2927fdd20ec7ceef04ce3a4f988650a448deeeaf1b22474dc |

E2 uses labels \(0,\ldots,8\); C2 uses labels \(1,\ldots,9\).
Throughout this review a label \(j\) means E2's \(C_j\), hence C2's label
\(j+1\). Composition of permutations is from right to left.

The review independently reconstructs the finite differences, coordinate
reduction, fiber conditions, polynomial values and permutation relations.
No mathematical program, external-model/API call, new agent, Git operation,
PDF, numerical search or old checker was used. The sole new write is this
review. No author report or shared state was edited.

## 2. Frozen data and the scope of the candidate class

The points actually used are

\[
\begin{array}{c|rrrrrrrrr}
j&0&1&2&3&4&5&6&7&8\\ \hline
x_j&0&1&1&3&0&-1&-1&1&2\\
y_j&0&0&1&1&2&-2&0&-1&2 .
\end{array}
\]

The displayed maps
\[
A(x,y)=(1-y,x-y),\qquad
I(x,y)=(x,q_0(x)-y),\qquad
q_0(t)=-t^4+4t^3-2t^2-3t+2
\]
give
\[
a=(0\,1\,2)(3\,4\,5)(6\,7\,8),\qquad
i_0=(0\,4)(2\,7)(5\,6).
\]
The point coordinates, the affine substitution for \(A\), and the five
values of \(q_0\) checked below agree with the actual C2 dependency.

The exact candidate class is
\[
\mathcal R=\{B^{-1}\rho_QB:
B(z)=Uz+b,\ U\in\operatorname{GL}_2(\mathbb Z),\
b\in\mathbb Z^2,\ Q\in\mathbb Z[t]\},\qquad
\rho_Q(u,v)=(u,Q(u)-v).
\]
There is no degree bound on \(Q\), coordinate-size bound, coefficient window,
or restriction on the allowed integral translation.

Each member is an involution. Thus a nonidentity restriction preserving the
finite set must exchange at least one pair. If \(B=(\ell,m)\), then
\[
R(z)-z=U^{-1}(0,Q(\ell(z))-2m(z)).
\]
All nonzero displacements therefore lie along the primitive integral vector
\(U^{-1}(0,1)\). It is primitive because \(U^{-1}\) is integral unimodular.
Consequently its unoriented direction occurs among point-pair differences.
This argument reduces all quantified affine coordinate choices to a finite
list; it is not a heuristic search restriction.

An identity restriction need not enter this direction argument and cannot
enlarge the induced permutation group in any event.

## 3. Independent exhaustive reconstruction of the directions

Here is the direct triangular enumeration of all differences
\(\Delta_{jk}=C_k-C_j\), \(j<k\). The last column divides out the positive
coordinate gcd and chooses positive first coordinate, or \((0,1)\) for a
vertical vector. Every entry was obtained from the frozen coordinates.

| Pair | Raw difference \(\Delta_{jk}\) | Primitive unoriented representative |
| --- | --- | --- |
| 01 | \((1,0)\) | \((1,0)\) |
| 02 | \((1,1)\) | \((1,1)\) |
| 03 | \((3,1)\) | \((3,1)\) |
| 04 | \((0,2)\) | \((0,1)\) |
| 05 | \((-1,-2)\) | \((1,2)\) |
| 06 | \((-1,0)\) | \((1,0)\) |
| 07 | \((1,-1)\) | \((1,-1)\) |
| 08 | \((2,2)\) | \((1,1)\) |
| 12 | \((0,1)\) | \((0,1)\) |
| 13 | \((2,1)\) | \((2,1)\) |
| 14 | \((-1,2)\) | \((1,-2)\) |
| 15 | \((-2,-2)\) | \((1,1)\) |
| 16 | \((-2,0)\) | \((1,0)\) |
| 17 | \((0,-1)\) | \((0,1)\) |
| 18 | \((1,2)\) | \((1,2)\) |
| 23 | \((2,0)\) | \((1,0)\) |
| 24 | \((-1,1)\) | \((1,-1)\) |
| 25 | \((-2,-3)\) | \((2,3)\) |
| 26 | \((-2,-1)\) | \((2,1)\) |
| 27 | \((0,-2)\) | \((0,1)\) |
| 28 | \((1,1)\) | \((1,1)\) |
| 34 | \((-3,1)\) | \((3,-1)\) |
| 35 | \((-4,-3)\) | \((4,3)\) |
| 36 | \((-4,-1)\) | \((4,1)\) |
| 37 | \((-2,-2)\) | \((1,1)\) |
| 38 | \((-1,1)\) | \((1,-1)\) |
| 45 | \((-1,-4)\) | \((1,4)\) |
| 46 | \((-1,-2)\) | \((1,2)\) |
| 47 | \((1,-3)\) | \((1,-3)\) |
| 48 | \((2,0)\) | \((1,0)\) |
| 56 | \((0,2)\) | \((0,1)\) |
| 57 | \((2,1)\) | \((2,1)\) |
| 58 | \((3,4)\) | \((3,4)\) |
| 67 | \((2,-1)\) | \((2,-1)\) |
| 68 | \((3,2)\) | \((3,2)\) |
| 78 | \((1,3)\) | \((1,3)\) |

The row counts by first label are \(8,7,6,5,4,3,2,1\); this enumerates
every unordered pair once, not merely 36 possibly repeated entries.
The normalized vectors are exactly the author's 18 distinct representatives.
Grouping the actual pairs reproduces each entry of E2's direction table.

The linear part \(M\) of \(A\) sends \((r,s)\) to \((-s,r-s)\).
Renormalizing sign after each arrow yields these six disjoint three-cycles:

\[
\begin{array}{c|ccc}
&v&Mv&M^2v\\ \hline
\mathcal O_0&(0,1)&(1,1)&(1,0)\\
\mathcal O_1&(3,1)&(1,-2)&(2,3)\\
\mathcal O_2&(1,-1)&(1,2)&(2,1)\\
\mathcal O_3&(3,-1)&(1,4)&(4,3)\\
\mathcal O_4&(4,1)&(1,-3)&(3,4)\\
\mathcal O_5&(2,-1)&(1,3)&(3,2).
\end{array}
\]

All three arrows, including the return arrow, hold in each row. There are
\(15,3,9,3,3,3\) original pairs respectively in these six orbits, totaling 36.
Since \(A(C)=C\), conjugation by the actual integral affine map \(A\)
preserves the candidate class and the set-preserving property, while
changing the direction by \(M\). One representative test per row is valid.

## 4. Affine coordinate independence and forced fiber values

Fix an integral unimodular linear coordinate system \((\ell,m)\) whose
first row annihilates the selected primitive direction. Any other integral
unimodular affine coordinate system with the same unoriented direction has
\[
\ell'=\eta\ell+c,\qquad
m'=\alpha m+\beta\ell+d,\qquad
\eta,\alpha\in\{1,-1\},\quad \beta,c,d\in\mathbb Z.
\]
Indeed, primitive integral rows with the same rational kernel differ only
by sign. Writing the other row in the unimodular dual basis gives integral
coefficients, and the determinant condition makes its \(m\) coefficient
\(\pm1\). This also handles opposite orientations.

Solving the transformed reflection equation back in \((\ell,m)\) gives
\[
m_{\rm new}=-m+
\alpha Q(\eta\ell+c)-2\alpha\beta\ell-2\alpha d.
\]
Thus its center polynomial in the selected coordinates is genuinely in
\(\mathbb Z[t]\). Integral translations and all admissible row changes are
included. Reversibility of the coordinate change also supplies the converse,
although only this direction is needed for the exclusions.

In a finite nonempty fiber with height set \(S_t\), preservation under
\(m\mapsto Q(t)-m\) forces
\[
Q(t)=\min S_t+\max S_t.
\]
The reflection reverses order, so the minimum must map to the maximum.
This fixes the whole restriction on that fiber, if it exists.
For a singleton the value is \(2m\); for a two-point fiber it is the sum
of the two heights. A three-point fiber additionally needs its middle
height to be the midpoint. The report does not silently omit this last
condition in its one surviving three-point fiber.

Finally, \(u-v\mid Q(u)-Q(v)\) follows term by term for every
\(Q\in\mathbb Z[t]\). It is used only as a necessary condition.
Nothing assumes that pairwise divisibility is generally sufficient for
integral-coefficient interpolation.

## 5. The five excluded orbits

For each of \(\mathcal O_1,\mathcal O_3,\mathcal O_4,\mathcal O_5\),
the representative direction has exactly one parallel pair. Hence it has
one two-point fiber and seven singleton fibers. Using \(m=y\), the following
independently checked data already contradict integral coefficients:

| Representative and first coordinate | Two-point fiber | Singleton fiber | Contradiction |
| --- | --- | --- | --- |
| \((3,1)\), \(\ell=x-3y\) | \(03:\ (\ell;m)=(0;0,1)\), so \(Q(0)=1\) | \(2:\ (-2;1)\), so \(Q(-2)=2\) | \(2\nmid 1-2\) |
| \((3,-1)\), \(\ell=x+3y\) | \(34:\ (6;1,2)\), so \(Q(6)=3\) | \(0:\ (0;0)\), so \(Q(0)=0\) | \(2\nmid 3-0\) |
| \((4,1)\), \(\ell=x-4y\) | \(36:\ (-1;1,0)\), so \(Q(-1)=1\) | \(1:\ (1;0)\), so \(Q(1)=0\) | \(2\nmid 1-0\) |
| \((2,-1)\), \(\ell=x+2y\) | \(67:\ (-1;0,-1)\), so \(Q(-1)=-1\) | \(1:\ (1;0)\), so \(Q(1)=0\) | \(2\nmid -1-0\) |

Each coordinate matrix here has determinant one. Input differences are
even and output differences odd. The contradictions apply to arbitrary
polynomial degree, and the coordinate lemma prevents translations or
another complementing row from avoiding them. Conjugation excludes all
12 directions in these four orbits.

For \(\mathcal O_2\), use \(\ell=x+y,m=y\), again determinant one.
Direct evaluation at all nine points yields:

\[
\begin{array}{c|c|c|r}
t&\text{labels}&S_t&\text{forced }Q(t)\\ \hline
-3&5&\{-2\}&-4\\
-1&6&\{0\}&0\\
0&0,7&\{0,-1\}&-1\\
1&1&\{0\}&0\\
2&2,4&\{1,2\}&3\\
4&3,8&\{1,2\}&3
\end{array}
\]

The inputs \(2,-3\) differ by five, while the required values differ by
seven. This excludes \(\mathbb Z[t]\) at every degree, despite the
individual finite fibers having reflection centers over the rationals.
Conjugation excludes the other two directions of this orbit.

## 6. Actual realizations and uniqueness in the remaining orbit

For the vertical direction, the successive fibers at
\(x=-1,0,1,2,3\) have height sets
\[
\{-2,0\},\quad\{0,2\},\quad\{-1,0,1\},\quad\{2\},\quad\{1\}.
\]
Their forced values are \((-2,2,0,4,2)\).
Substitution into the actual quartic gives
\[
\begin{aligned}
q_0(-1)&=-1-4-2+3+2=-2,&q_0(0)&=2,\\
q_0(1)&=-1+4-2-3+2=0,&
q_0(2)&=-16+32-8-6+2=4,\\
q_0(3)&=-81+108-18-9+2=2.
\end{aligned}
\]
The triple \(\{-1,0,1\}\) has the required midpoint zero.
This proves existence in \(\mathbb Z[t]\), not just rational interpolation
or existence of an integer-valued polynomial.

The induced swaps are exactly \(i_0=(0\,4)(2\,7)(5\,6)\).
The global maps \(AIA^{-1}\) and \(A^{-1}IA\) are in \(\mathcal R\)
and preserve \(C\); their directions are \((1,1)\) and \((1,0)\).
Conjugating the actual transpositions gives
\[
i_1=(0\,8)(1\,5)(3\,7),\qquad
i_2=(1\,6)(2\,3)(4\,8).
\]
The forced fiber values make the restriction unique in each direction.
This is uniqueness of the finite permutation, not of a global polynomial.
The exhaustive direction reduction now proves the precise equality
\[
\{R|_C:R\in\mathcal R,\ R(C)=C,\ R|_C\ne1\}
=\{i_0,i_1,i_2\}.
\]

## 7. Independent finite-group check

Multiplying from right to left gives
\[
r=i_0i_1=(0\,8\,4)(1\,6\,5)(2\,7\,3).
\]
For example, its first cycle is \(0\mapsto8\mapsto4\mapsto0\);
the other two follow in the same direct way.
Conjugation of the three displayed cycles by \(a\) permutes those cycles,
and conjugation by \(i_0\) reverses each. Therefore
\[
ara^{-1}=r,\qquad i_0ri_0=r^{-1}.
\]
Also \(r^3=i_0^2=a^3=1\), and
\(ai_0a^{-1}=i_1=i_0r=r^{-1}i_0\).
These are finite-permutation equalities only.

Let
\[
D_0=\{0,4,8\},\quad D_1=\{1,5,6\},\quad D_2=\{2,3,7\}.
\]
Both \(r\) and \(i_0\) preserve each block. Their relations put every element
of \(H=\langle r,i_0\rangle\) in the form \(r^b i_0^\epsilon\) with
\(0\le b<3\), \(0\le\epsilon<2\). On \(D_0\) these are the six distinct
permutations generated by a three-cycle and a transposition.
Thus \(H\) has exactly six elements and is \(S_3\), without presuming
faithfulness merely from the existence of three blocks.

Put \(z=ar^2\). Since \(a\) commutes with \(r\), \(z^3=1\).
Moreover \(r^2i_0r^{-2}=ri_0\), and consequently
\[
zi_0z^{-1}=a(ri_0)a^{-1}=r(r^{-1}i_0)=i_0.
\]
It also centralizes \(r\). The map \(a\) cycles
\(D_0\to D_1\to D_2\to D_0\), so \(z\) has the same nontrivial block
action and has order exactly three. Since \(H\) fixes every block,
\(\langle z\rangle\cap H=\{1\}\). Finally \(a=zr\), proving
\[
\langle a,i_0\rangle=H\times\langle z\rangle\cong S_3\times C_3.
\]
Element orders in this direct product are \(1,2,3,6\), never nine.
Every set-preserving reflection under consideration induces one of the
three conjugates already in this group, or the identity. Adjoining any
number of them therefore cannot change the group or create a nine-cycle.

## 8. Source sufficiency, boundaries and disposition

All mathematical steps here are elementary finite calculations and integral
polynomial identities supplied explicitly in the inspected artifacts.
No external classification theorem, interpolation theorem, experimental
certificate or uninspected C2 appendix is needed. There is no new priority
claim requiring a literature conclusion.

The proof closes exactly the route of adjoining individually set-preserving
members of \(\mathcal R\) to \(A,I\) for this fixed set. In particular:

- A longer tame word may preserve \(C\) while its intermediate factors
  leave \(C\); this proof does not apply to such a factorization.
- A reflection conjugated by nonaffine tame coordinates is not thereby
  covered by the unimodular affine coordinate lemma.
- Other kinds of tame stabilizer elements, and other integral nine-point
  sets, remain outside the quantified class.
- Orders of restrictions to \(C\) do not establish finite orders of the
  corresponding global polynomial maps.

The author's final statements maintain each of these distinctions.
No correction is required before accepting this bounded auxiliary result.
The full tame stabilizer, the native integer period-nine problem, the
remaining full-spectrum questions and any contract-admission decision are
not settled by this review.
