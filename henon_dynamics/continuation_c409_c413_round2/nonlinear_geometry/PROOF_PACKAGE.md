# Integral recurrence for the Fibonacci trace map: proof package

Date: 2026-09-06. Author-side status: `PROVABLE AS STATED`.
Admission status: `AWAITING_NONAUTHOR_REVIEW_AND_OWNERSHIP_ADJUDICATION`.
This is an unnumbered research contract, not a manuscript or a formal Route-A
evaluation. The four previously accepted contracts and the sealed package are
unchanged. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.

## 1. Object, quantifiers, and the proposed residual contribution

Fix the single polynomial automorphism

\[
 T:\mathbb Z^3\longrightarrow\mathbb Z^3,
 \qquad T(x,y,z)=(y,z,yz-x).
\]

Its inverse is \(T^{-1}(x,y,z)=(xy-z,x,y)\). The time variable is the
ordinary iterate \(n\in\mathbb Z\), not a return-time subsequence or a word
length in a group. Put

\[
 K(x,y,z)=x^2+y^2+z^2-xyz,\qquad
 S_k(\mathbb Z)=\{P\in\mathbb Z^3:K(P)=k\},\quad k\in\mathbb Z.
\]

Direct substitution gives \(K\circ T=K\). The question is to classify
**every periodic point of this single map on all of \(\mathbb Z^3\)**,
equivalently on every integer level \(S_k\), with no bound on the period,
coordinates, or level.

The map, invariant, axis cycles, low-period algebraic curves, and sign symmetry
are classical. In particular the existence of the 4-, 6-, and 12-periodic
families below is not claimed as new. The proposed residual result is the
global arithmetic **exhaustiveness** statement and its exact level-by-level
consequences. Ownership of that exhaustiveness statement remains separately
under review; a complete proof does not establish literature priority.

## 2. Main theorem

For \(m\geq1\), let

\[
 A_m=\operatorname{Orb}_T(m,0,0),\quad
 B_m=\operatorname{Orb}_T(-1,m,-1),\quad
 C_m=\operatorname{Orb}_T(1,m,1).
\]

Also set

\[
 O=\{(0,0,0)\},\quad E=\{(2,2,2)\},\quad
 D=\{(-2,-2,2),(-2,2,-2),(2,-2,-2)\}.
\]

**Theorem.** The complete periodic set is the disjoint union

\[
 \operatorname{Per}(T,\mathbb Z^3)
 =O\sqcup E\sqcup D\sqcup\bigsqcup_{m\geq1}(A_m\sqcup B_m\sqcup C_m).
 \tag{1}
\]

The exact periods are respectively \(1,1,3,6,4,12\). Thus the complete
set of periods is \(\{1,3,4,6,12\}\). The orbit heights, defined as the
largest absolute scalar coordinate anywhere in an orbit, are \(m\) for
each of \(A_m,B_m,C_m\). Their invariant levels are

\[
 K(A_m)=m^2,\qquad K(B_m)=K(C_m)=m^2-m+2.
 \tag{2}
\]

A point has a bounded forward orbit, or a bounded backward orbit, if and only
if it belongs to (1). Every other integral point satisfies

\[
 \|T^nP\|_\infty\longrightarrow\infty\quad\text{as }n\to+\infty
 \quad\text{and as }n\to-\infty.
 \tag{3}
\]

This is a classification over \(\mathbb Z\), not over \(\mathbb Q\).

## 3. Scalar coordinates and exact cycle verification

Write an orbit as \(T^iP=(x_i,x_{i+1},x_{i+2})\), so that, for every
\(i\in\mathbb Z\),

\[
 x_{i+3}=x_{i+1}x_{i+2}-x_i,
 \qquad x_{i-1}+x_{i+2}=x_ix_{i+1}.
 \tag{4}
\]

Any three consecutive coordinates determine the entire two-sided sequence.
The following scalar words, read cyclically, obey (4). Each consecutive
triple is one point of the corresponding orbit:

\[
 \begin{aligned}
 A_m:&\quad(m,0,0,-m,0,0),\\
 B_m:&\quad(-1,m,-1,1-m),\\
 C_m:&\quad(1,m,1,m-1,-1,-m,1,1-m,1,-m,-1,m-1).
 \end{aligned}
 \tag{5}
\]

For completeness, the successive triples for \(C_m\) are

\[
\begin{array}{c|c@{\qquad}c|c}
 j&T^j(1,m,1)&j&T^j(1,m,1)\\\hline
0&(1,m,1)&6&(1,1-m,1)\\
1&(m,1,m-1)&7&(1-m,1,-m)\\
2&(1,m-1,-1)&8&(1,-m,-1)\\
3&(m-1,-1,-m)&9&(-m,-1,m-1)\\
4&(-1,-m,1)&10&(-1,m-1,1)\\
5&(-m,1,1-m)&11&(m-1,1,m).
\end{array}
 \tag{6}
\]

The last triple maps to the first. The \(A_m\) word contains the positive
value \(m\) exactly once, proving exact period 6. For \(m\geq2\), the
\(B_m\) and \(C_m\) words contain the positive value \(m\) exactly once,
proving periods 4 and 12. For \(m=1\), the four \(B_1\) triples and twelve
\(C_1\) triples in (5)–(6) are visibly pairwise distinct within each list;
this also proves their exact periods without a generic-parameter assumption.
The four points in \(E\sqcup D\) have coordinates of modulus 2 with
positive coordinate product. On them \(yz=2x\), so \(T\) is cyclic
permutation. This proves the asserted fixed point and 3-cycle.

Substitution at the representatives gives (2). Distinct exact periods prevent
overlap between different named families. Within any one family, different
values of \(m\) have different orbit heights. The special orbits have
period 1 or 3, and are therefore disjoint from all three families.

## 4. Uniform maximum lemma, including all equality cases

Let \((x_i)\) be a periodic integral solution of (4), and put
\(M=\max_i|x_i|\). If \(M=0\), the sequence is the origin. Suppose
\(M\geq2\), shift the index to arrange

\[
 x_0=u,\quad |u|=M,\quad x_{-1}=a,\quad x_1=b.
\]

The two instances of (4)

\[
 au=x_{-2}+b,\qquad ub=a+x_2
 \tag{7}
\]

give \(M|a|\leq2M\) and \(M|b|\leq2M\). Consequently
\(|a|,|b|\leq2\). We have not assumed that \(u\) is positive and have
not replaced \(T\) by \(T^3\).

### 4.1. A neighbour of modulus 2

First assume \(b=2\eta\), \(\eta\in\{\pm1\}\). Equality in
\(ub=a+x_2\) forces

\[
 a=x_2=\eta u.
\]

Then \(au=x_{-2}+b\) implies

\[
 M^2=|au|\leq M+2.
 \tag{8}
\]

For an integer \(M\geq2\), (8) forces \(M=2\). Writing
\(u=2\varepsilon\), we obtain the consecutive triple

\[
 (a,u,b)=(2\eta\varepsilon,2\varepsilon,2\eta).
\]

Its entries all have modulus 2 and their product is positive. It belongs to
\(E\sqcup D\), whose complete future and past have already been verified.

If instead \(|a|=2\), apply the same argument to the reversed scalar
sequence \(y_i=x_{-i}\). Equation (4) is preserved under reversal: the
identity required for \(y\) is the identity for \(x\) with the indices
reversed. Thus this case also lies in \(E\sqcup D\).

All other periodic orbits with \(M\geq2\) therefore satisfy

\[
 a,b\in\{-1,0,1\}.
 \tag{9}
\]

### 4.2. Both neighbours zero

If \(a=b=0\), the triple is \((0,u,0)\). The axis itinerary (5) shows
that its orbit is \(A_M\), for either sign of \(u\).

### 4.3. Exactly one neighbour zero: explicit contradiction

Suppose \(a=0\) and \(b=t\in\{\pm1\}\). Starting with
\((x_{-1},x_0,x_1)=(0,u,t)\), recurrence (4) gives, successively,

\[
 x_2=ut,\quad x_3=0,\quad x_4=-t,\quad x_5=-ut,
 \quad x_6=u,\quad x_7=t(1-u^2).
 \tag{10}
\]

Thus \(|x_7|=M^2-1>M\) for every integer \(M\geq2\), contrary to the
definition of the maximum. If \(b=0\) and \(a=\pm1\), apply (10) to
the reversed sequence. This branch is excluded for \(M=2\) as well as
for all larger maxima; no small exceptional parameter is hidden here.

### 4.4. Both neighbours nonzero: exact signed classification

Let \(a,b\in\{\pm1\}\). If \(abu<0\), then \(bu\) and \(a\)
have opposite signs, and

\[
 |x_2|=|bu-a|=M+1,
\]

again contradicting maximality. Hence \(abu>0\), or
\(u=abM\). There are exactly four possible triples:

\[
\begin{array}{c|c|c}
 (a,b)&(a,u,b)&\text{already verified orbit}\\\hline
 (-1,-1)&(-1,M,-1)&B_M\\
 (1,1)&(1,M,1)&C_M\\
 (-1,1)&(-1,-M,1)&T^4(1,M,1)\in C_M\\
 (1,-1)&(1,-M,-1)&T^8(1,M,1)\in C_M.
\end{array}
 \tag{11}
\]

The time labels 4 and 8 are the ordinary iterates from (6). In particular no
sign quotient has incorrectly identified a 4-cycle with a 12-cycle.

Sections 4.1–4.4 prove the classification for every \(M\geq2\).

## 5. The complete small remainder, without a computer dependency

The only remaining case is \(M=1\), so every entry belongs to
\(\{-1,0,1\}\). If a triple has no zero entries and negative product,
then \(yz=-x\) and the next coordinate is \(-2x\), of modulus 2. Such
a triple cannot occur in this case.

All other triples in the unit cube are the following 23 possibilities:

- the origin: 1 point;
- exactly one nonzero coordinate: 6 points;
- exactly two nonzero coordinates: 12 points;
- three nonzero coordinates with positive product: 4 points.

The origin and \(A_1\) give the first two sets. By (5)–(6), \(B_1\)
and \(C_1\) are two disjoint cycles of total size 16, all of whose points
lie in the union of the last two sets. Since that union also has size 16,
they exhaust it. This supplies the full small-case proof.

In particular the cube \([-2,2]^3\) contains precisely 49 points whose
entire orbit stays in that cube: \(O\), \(E\), \(D\), and
\(A_m,B_m,C_m\) for \(m=1,2\). For each of the other 76 initial states,
the forward orbit must leave the cube within at most 125 iterates: otherwise
126 successive states in a set of size 125 repeat, making the initial point
periodic by invertibility and contradicting the proved classification.
The same bound holds backward. This is a finite escape certificate implied
by the proof, not a numerical assumption used by it.

## 6. Boundedness and two-sided proper escape

The map \(T\) is a bijection of the discrete set \(\mathbb Z^3\). A
bounded forward orbit repeats a state, hence is eventually periodic; applying
the inverse of \(T\) shows that its initial point is already periodic.
The argument is identical backward. This proves the boundedness assertions.

For a nonperiodic point, all iterates \(T^nP\), \(n\in\mathbb Z\), are
distinct. For every finite \(R\geq0\), the finite cube
\([-R,R]^3\cap\mathbb Z^3\) can therefore contain only finitely many
of these iterates. Beyond the largest positive and negative visiting times
the orbit never returns to that cube. This proves both limits in (3).
No exponential rate or real/complex escape theorem is asserted.

## 7. Complete level-by-level arithmetic return law

For an integer \(k\), define the Boolean indicators

\[
 s_k=\mathbf1_{\{k=m^2\text{ for some integer }m\geq1\}},\qquad
 q_k=\mathbf1_{\{k=m^2-m+2\text{ for some integer }m\geq1\}}.
\]

The second condition is equivalent to \(4k-7\) being a positive odd
square. Both parametrizations are injective for \(m\geq1\).

**Corollary.** Every integer level has finitely many integral periodic
points. Its exact-period orbit counts are

\[
 c_1(k)=\mathbf1_{k=0}+\mathbf1_{k=4},\quad
 c_3(k)=\mathbf1_{k=4},\quad c_4(k)=q_k,\quad
 c_6(k)=s_k,\quad c_{12}(k)=q_k,
 \tag{12}
\]

and all other orbit counts vanish. For every ordinary time \(n\geq1\),

\[
 \#\operatorname{Fix}(T^n;S_k(\mathbb Z))
 =\mathbf1_{k=0}
 +\mathbf1_{k=4}(1+3\mathbf1_{3\mid n})
 +6s_k\mathbf1_{6\mid n}
 +q_k(4\mathbf1_{4\mid n}+12\mathbf1_{12\mid n}).
 \tag{13}
\]

Indeed each orbit of exact length \(d\) contributes \(d\) fixed points
if and only if \(d\mid n\); apply the theorem. The formal dynamical zeta
function on the integral points of this fixed level is consequently

\[
 \zeta_k(t)=
 \frac{1}{(1-t)^{\mathbf1_{k=0}+\mathbf1_{k=4}}
 (1-t^3)^{\mathbf1_{k=4}}(1-t^6)^{s_k}
 (1-t^4)^{q_k}(1-t^{12})^{q_k}}.
 \tag{14}
\]

The two infinite level sets overlap only at \(k=4\): if
\(r^2=m^2-m+2\), then

\[
 (2r-2m+1)(2r+2m-1)=7.
\]

Since \(r^2=(m-\tfrac12)^2+\tfrac74\) with \(r,m\geq1\), we have
\(r>m-\tfrac12\). Both factors are therefore positive integers; the
second is larger, so they are 1 and 7. This gives \(r=m=2\).
Thus the complete numbers of integral
periodic points are: 1 at \(k=0\); 26 at \(k=4\); 6 at every other
positive square level; 16 at every other level \(m^2-m+2\); and 0 on
every remaining integer level.

One must not define an ordinary finite-count zeta function for the entire
unrestricted lattice by silently using (14): for example \(T^6\) fixes
infinitely many axis points across different levels. Formula (14) is only
for the stated fixed level \(S_k(\mathbb Z)\).

## 8. Counterboundaries and ownership separation

1. **Not all rational points.** For example
   \(T(3,3/2,3)=(3/2,3,3/2)\) and \(T^2(3,3/2,3)=(3,3/2,3)\).
   This rational 2-cycle is not in (1). No assertion that rational periodic
   points are integral is made.
2. **Not the entire trace-map group.** The triple \((-1,3,-1)\) is in
   \(B_3\), with invariant 8. The Vieta transformation at its middle
   coordinate followed by transformations at other coordinates can generate
   unbounded values; the single-map theorem is not deduced from a theorem
   about finite orbits under every group element. More directly, Humphries's
   finite-group-orbit classification allows axes and special compact/torsion
   characters, and does not contain this non-axis level-8 example. Its
   quantifiers are different from those here.
3. **Classical families subtracted.** Roberts–Baake (1994), Eq. (29),
   Table I, and the discussion on printed pp. 851–852 already give the
   axis/low-period families and the 4-to-12 sign relation in half-trace
   normalization. Those results must be credited, not relabelled as the new
   theorem. A separate source ledger audits whether (1)'s exhaustiveness
   is already known.
4. **No target Euler factor.** Equations (13)–(14) count integral source
   orbits on a fixed Markoff level. They are not point counts over finite
   fields, an elliptic-curve local factor, a root number, a spectral
   determinant for Riemann zeros, or an asserted bridge to any of those.

## 9. Verification boundary

The theorem's proof is Sections 3–6 and is independent of any executable.
The finite exact scout in `scout_checks.py` found only the predicted cycles
inside \([-12,12]^3\); that check by itself cannot establish global
exhaustiveness. The separate verifier `verify_trace_contract.py` has passed
the symbolic itineraries, all small-cube escape certificates, a full graph
check in \([-20,20]^3\), layer return counts in an explicitly bounded
range, and the rational counterexample; see `VERIFICATION.md`. Those checks
remain supplementary to the quantified proof above.

Required external dependencies for the proof: none beyond integer arithmetic,
the triangle inequality, and finiteness of a bounded subset of \(\mathbb Z^3\).
Classical source dependencies concern attribution and context, not hidden
mathematical steps. Non-author internal review is still required.
