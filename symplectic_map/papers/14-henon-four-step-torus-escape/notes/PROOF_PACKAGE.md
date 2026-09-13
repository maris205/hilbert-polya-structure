# Proof Package

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

This is a proof-first source package. It is not an independent certification
and is not a manuscript.

## Claim

Let \(K\) be a field of characteristic zero, let \(d\ge2\), let
\(a,b,c\in K^\ast\), and let \(\Gamma\le K^\ast\) be a multiplicative
subgroup of finite rank \(r\). Define

\[
H(x,y)=(b x^d+a y+c,x)
\]

and

\[
T_m(H,\Gamma)
=
\{P\in\Gamma^2:H^j(P)\in\Gamma^2
  \text{ for }0\le j\le m\}.
\]

Then

\[
\boxed{
\#T_4(H,\Gamma)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
}
\]

For every \(d\ge2\), there is a number-field example with
\(\operatorname{rank}\Gamma=1\) and

\[
\#T_3(H,\Gamma)=\infty.
\]

If \(C_n^\Gamma(H)\) is the number of exact-period-\(n\) orbits wholly
contained in \(\Gamma^2\), then

\[
\sum_{n\ge1}n\,C_n^\Gamma(H)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\]

## Status

**PROVABLE AS STATED**, subject to the required independent source review.

No membership hypothesis on \(a,b,c,-1\) is used in the upper-bound proof.
The explicit sharpness example chooses coefficients inside its rank-one group
because that is convenient for constructing infinitely many survivors.

## Assumptions

- \(K\) has characteristic zero.
- \(d\) is an integer with \(d\ge2\).
- \(a,b,c\) are nonzero.
- \(\Gamma\le K^\ast\) has finite rank \(r\).
- Points of \(T_4\) have all coordinates at times \(0,\ldots,4\) in
  \(\Gamma\).

## Notation and index direction

For an initial state

\[
P=(x_0,x_{-1}),
\]

write

\[
H^j(P)=(x_j,x_{j-1}).
\]

The recurrence is

\[
x_{i+1}=b x_i^d+a x_{i-1}+c.
\]

For a local transition at index \(i\), put

\[
u=x_{i-1},\qquad v=x_i,\qquad z=x_{i+1},
\qquad \alpha=-\frac ca.
\]

The first letter of a word labels the recurrence at \(i\), the second at
\(i+1\), and so on. The labels are fixed throughout:

\[
\begin{aligned}
A_i&:\quad a x_{i-1}+c=0,
&&x_{i-1}=\alpha,\quad x_{i+1}=b x_i^d,\\
B_i&:\quad b x_i^d+c=0,
&&b x_i^d=-c,\quad x_{i+1}=a x_{i-1},\\
C_i&:\quad b x_i^d+a x_{i-1}=0,
&&b x_i^d=-a x_{i-1},\quad x_{i+1}=c.
\end{aligned}
\]

These definitions are part of the proof contract. Relabeling them would
change which free chains are called \(BA\) and \(CB\).

## External theorem used

The Evertse--Schlickewei--Schmidt theorem states that if \(G\) is a subgroup
of \((K^\ast)^n\) of finite rank \(R\), and
\(\lambda_1,\ldots,\lambda_n\in K^\ast\) are fixed, then the number of
solutions

\[
(y_1,\ldots,y_n)\in G,\qquad
\lambda_1y_1+\cdots+\lambda_ny_n=1,
\]

for which no nonempty proper subsum vanishes is at most

\[
\exp\!\bigl((6n)^{3n}(R+1)\bigr).
\]

For \(n=3\) and \(R=3r\), define

\[
E(3,3r)
=
\exp\!\bigl(18^9(3r+1)\bigr).
\]

The theorem allows arbitrary fixed nonzero coefficients. This exact feature
is what removes all coefficient-membership assumptions.

## Proof strategy

Partition \(T_4(H,\Gamma)\) into:

1. points having at least one nondegenerate local ESS equation among
   indices \(0,1,2,3\);
2. points for which all four local equations are degenerate.

The first set is bounded by four applications of ESS, with at most \(d\)
states above each ESS solution. The second set is encoded by words in
\(\{A,B,C\}^4\). A complete adjacent-transition table shows that only
\(BA\) and \(CB\) can be free. The \(BA\) chain closes at the third letter;
the only free extension of \(CB\) is \(CBA\), and that closes at the fourth
letter. Each word has at most \(d^2\) initial states.

## Dependency map

1. The fixed-coefficient ESS lemma gives at most
   \(dE(3,3r)\) states at a specified nondegenerate index.
2. Invertibility of \(H\) transfers a local-state count back to initial
   states.
3. The nine-transition table identifies the only two free adjacent words.
4. The \(BA\) continuation closes every \(BA\)-prefix by length three.
5. The \(CB\) continuation leaves only \(CBA\) free at length three.
6. The \(CBA\) continuation closes at length four.
7. Simultaneous degeneracy is covered by the union over all words.
8. The two parts sum to the asserted \(T_4\) bound.
9. A direct rank-one family proves \(T_3\) sharpness.
10. Orbit containment gives the weighted periodic corollary.

## Proof

### Step 1. Fixed-coefficient ESS normalization

For each local recurrence, write

\[
\frac1c x_{i+1}
-\frac bc x_i^d
-\frac ac x_{i-1}
=1.
\]

The variable triple

\[
Y_i=(x_{i+1},x_i^d,x_{i-1})
\]

lies in \(\Gamma^3\). Since \(\Gamma\) has rank \(r\), the direct product
\(\Gamma^3\) has rank \(3r\). The coefficients

\[
\frac1c,\qquad -\frac bc,\qquad -\frac ac
\]

are fixed elements of \(K^\ast\). ESS therefore bounds the number of
nondegenerate triples \(Y_i\) by

\[
E(3,3r)
=
\exp\!\bigl(18^9(3r+1)\bigr).
\]

This argument neither asserts nor requires that a coefficient-normalized
triple belongs to \(\Gamma^3\). The variables belong to \(\Gamma^3\);
the coefficients remain fixed coefficients.

### Step 2. Each ESS solution has at most \(d\) local states

An ESS solution specifies

\[
x_{i+1},\qquad x_i^d,\qquad x_{i-1}.
\]

The polynomial

\[
X^d-x_i^d
\]

has at most \(d\) roots in \(K\). Hence there are at most \(d\) possible
values of \(x_i\), and therefore at most \(d\) local states
\((x_i,x_{i-1})\) over a fixed ESS triple.

The inverse map is

\[
H^{-1}(X,Y)
=
\left(
Y,\frac{X-bY^d-c}{a}
\right),
\]

so \(H\) is an automorphism. For each fixed \(i\), the map

\[
P\longmapsto H^i(P)=(x_i,x_{i-1})
\]

is injective.

If at least one of the four local equations \(i=0,1,2,3\) is nondegenerate,
a union bound gives

\[
\#\{\text{points with a nondegenerate local equation}\}
\le
4dE(3,3r).
\]

### Step 3. The three degeneracy types are exhaustive

Let the three nonzero summands be

\[
L_1=\frac{x_{i+1}}c,\qquad
L_2=-\frac{b x_i^d}c,\qquad
L_3=-\frac{a x_{i-1}}c.
\]

They satisfy

\[
L_1+L_2+L_3=1.
\]

Because every \(L_j\) is nonzero, a degenerate ESS solution must have a
vanishing two-term subsum. The three possibilities are:

\[
\begin{array}{c|c|c}
\text{label}&\text{vanishing pair}&\text{recurrence form}\\ \hline
A&L_1+L_2=0&
  x_{i-1}=\alpha,\ x_{i+1}=b x_i^d\\
B&L_1+L_3=0&
  b x_i^d=-c,\ x_{i+1}=a x_{i-1}\\
C&L_2+L_3=0&
  b x_i^d=-a x_{i-1},\ x_{i+1}=c.
\end{array}
\]

Thus every degenerate local equation has at least one of the labels
\(A,B,C\).

### Step 4. Complete nine-transition table

The first letter is imposed at \(i\), the second at \(i+1\). The table gives
all constraints on the initial local state \((u,v)=(x_{i-1},x_i)\).

| Word | Constraints on \((u,v)\) | Upper bound |
|---|---|---:|
| \(AA\) | \(u=\alpha,\ v=\alpha\) | \(1\) |
| \(AB\) | \(u=\alpha,\ b^{d+1}v^{d^2}=-c\) | \(d^2\) |
| \(AC\) | \(u=\alpha,\ b^{d+1}v^{d^2}=-av\) | \(d^2-1\) |
| \(BA\) | \(v=\alpha,\ b\alpha^d=-c\); if compatible, \(u\) is free | free |
| \(BB\) | \(v^d=-c/b,\ u^d=-c/(ba^d)\) | \(d^2\) |
| \(BC\) | \(v^d=-c/b,\ u^d=-v/(ba^{d-1})\) | \(d^2\) |
| \(CA\) | \(v=\alpha,\ u=-b\alpha^d/a\) | \(1\) |
| \(CB\) | \(bc^d=-c,\ u=-bv^d/a\); if compatible, \(v\) is free | free |
| \(CC\) | \(v=-bc^d/a,\ u=-bv^d/a\) | \(1\) |

Each entry follows directly:

- Under \(A_i\), \(u=\alpha\) and \(x_{i+1}=bv^d\). Applying
  \(A_{i+1},B_{i+1},C_{i+1}\) gives the first row.
- Under \(B_i\), \(bv^d=-c\) and \(x_{i+1}=au\). Applying the three next
  labels gives the second row.
- Under \(C_i\), \(u=-bv^d/a\) and \(x_{i+1}=c\). Applying the three next
  labels gives the third row.

For \(AC\), division by \(v\ne0\) leaves a polynomial equation of degree
\(d^2-1\). All other finite entries use polynomials of the displayed degrees.
Since \(d\ge2\), every finite entry is at most \(d^2\).

The only adjacent words that can carry a free parameter are

\[
BA\quad\text{and}\quad CB.
\]

### Step 5. Every \(BA\) branch closes at the third letter

Assume the compatibility condition

\[
b\alpha^d=-c.
\]

Parameterize the \(BA\) branch by

\[
t=x_{i-1}.
\]

The coordinates are

\[
x_{i-1}=t,\qquad
x_i=\alpha,\qquad
x_{i+1}=at,\qquad
x_{i+2}=ba^dt^d.
\]

The third label gives:

| Word | Equation for \(t\) | Upper bound |
|---|---|---:|
| \(BAA\) | \(at=\alpha\) | \(1\) |
| \(BAB\) | \(b^{d+1}a^{d^2}t^{d^2}=-c\) | \(d^2\) |
| \(BAC\) | \(b^{d+1}a^{d^2}t^{d^2}=-a^2t\) | \(d^2-1\) |

In the \(BAC\) line, \(t\ne0\), so division by \(t\) gives a nonzero
polynomial of degree \(d^2-1\). Thus every word beginning with \(BA\) has at
most \(d^2\) initial states before the fourth label is considered. Adding a
fourth condition cannot increase that number.

### Step 6. The only free three-letter extension of \(CB\) is \(CBA\)

The \(CB\) compatibility condition is

\[
bc^d=-c,
\qquad\text{equivalently}\qquad
bc^{d-1}=-1.
\]

Parameterize by

\[
t=x_i.
\]

Then

\[
x_{i-1}=-\frac ba t^d,\qquad
x_i=t,\qquad
x_{i+1}=c,\qquad
x_{i+2}=at.
\]

The third label gives:

| Word | Condition | Upper bound |
|---|---|---:|
| \(CBB\) | \(ba^dt^d=-c\) | \(d\) |
| \(CBC\) | \(ba^dt^d=-ac\) | \(d\) |
| \(CBA\) | \(c=-c/a\) | free only if \(a=-1\) |

Consequently the only free three-letter word is

\[
CBA,\qquad a=-1,\qquad bc^{d-1}=-1.
\]

### Step 7. The \(CBA\) branch closes at the fourth letter

Under the two exceptional coefficient relations, the coordinates are

\[
x_{i-1}=bt^d,\qquad
x_i=t,\qquad
x_{i+1}=c,\qquad
x_{i+2}=-t,\qquad
x_{i+3}=b(-t)^d.
\]

The fourth label gives:

| Word | Condition | Upper bound |
|---|---|---:|
| \(CBAA\) | \(-t=c\) | \(1\) |
| \(CBAB\) | \(b^{d+1}(-t)^{d^2}=-c\) | \(d^2\) |
| \(CBAC\) | \(b^{d+1}(-t)^{d^2}=-t\) | \(d^2-1\) |

For \(CBAC\), division by \(t\ne0\) gives degree \(d^2-1\). Hence every
four-letter word in \(\{A,B,C\}^4\) has at most \(d^2\) initial states.

There are \(3^4=81\) words, so

\[
\#\{\text{points with four degenerate local equations}\}
\le81d^2.
\]

### Step 8. Simultaneous degeneracy

A local equation may satisfy two labels. In terms of
\((L_1,L_2,L_3)\), the possibilities are

\[
\begin{aligned}
A\cap B&:\quad (L_1,L_2,L_3)=(-1,1,1),\\
A\cap C&:\quad (L_1,L_2,L_3)=(1,-1,1),\\
B\cap C&:\quad (L_1,L_2,L_3)=(1,1,-1).
\end{aligned}
\]

All three labels cannot occur simultaneously: the three pair-sum equations
would imply \(2L_j=0\) and then \(L_j=0\), contradicting nonzero summands in
characteristic zero.

At each degenerate index, choose any label the point satisfies. This assigns
the point to at least one four-letter word. A point with multiple choices may
be counted more than once in the union bound, but it cannot be missed. Every
word bound above is an upper bound for the full realization set of that word,
so simultaneous degeneracy does not alter \(81d^2\).

### Step 9. Combine the two parts

Every point in \(T_4(H,\Gamma)\) either has a nondegenerate local equation
among \(i=0,1,2,3\), or all four are degenerate. Therefore

\[
\begin{aligned}
\#T_4(H,\Gamma)
&\le
4dE(3,3r)+81d^2\\
&=
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\end{aligned}
\]

This proves the primary upper bound.

### Step 10. Short periodic orbits

No step assumes that the states

\[
P,H(P),H^2(P),H^3(P),H^4(P)
\]

are distinct. If \(P\) has period \(1\), \(2\), \(3\), or \(4\), some local
coordinates repeat, but all four indexed recurrence equations remain valid.
Repeated equations only impose additional compatibility; they do not create
new choices. Injectivity of \(H^i\) also remains valid. Thus short orbits
require no separate correction term.

### Step 11. Rank-one \(T_3\) sharpness

Fix \(d\ge2\). Choose \(c\in\overline{\mathbb Q}\) satisfying

\[
c^{d-1}=-1,
\]

and set

\[
K=\mathbb Q(c),\qquad
b=1,\qquad a=-1,\qquad
\Gamma=\langle2,c,-1\rangle.
\]

Since \(c^{2(d-1)}=1\), both \(c\) and \(-1\) are torsion. The element \(2\)
is non-torsion, hence

\[
\operatorname{rank}\Gamma=1.
\]

For \(t=2^n\), \(n\ge0\), put

\[
P_t=(t,t^d).
\]

Direct substitution gives

\[
\begin{aligned}
H(P_t)
&=(t^d-t^d+c,t)
=(c,t),\\
H^2(P_t)
&=(c^d-t+c,c)
=(-t,c),\\
H^3(P_t)
&=((-t)^d-c+c,-t)
=((-t)^d,-t).
\end{aligned}
\]

All these coordinates lie in \(\Gamma\), and the \(P_t\) are pairwise
distinct. Thus

\[
\#T_3(H,\Gamma)=\infty.
\]

In the fixed labeling, this family realizes the free word \(CBA\).

### Step 12. Weighted periodic-orbit corollary

Let \(C_n^\Gamma(H)\) count exact-period-\(n\) orbits
\(\mathcal O\subseteq\Gamma^2\). Every point on such an orbit belongs to
\(T_4(H,\Gamma)\). Distinct exact-period orbits are disjoint and each has
\(n\) points. Hence

\[
\sum_{n\ge1}n\,C_n^\Gamma(H)
\le
\#T_4(H,\Gamma),
\]

which gives the claimed weighted bound.

This argument does not apply to the larger set
\(\operatorname{Per}(H)\cap\Gamma^2\) unless the full orbit-containment
hypothesis is imposed.

## Corrections or missing assumptions

No correction to the stated constant is required. The following formulations
would be incorrect and are excluded:

- saying that coefficient-normalized variables lie in \(\Gamma^3\);
- saying that \(b\) must belong to \(\Gamma\), or that \(\Gamma\) must be
  enlarged to contain \(b\); this is a false residual from the discarded
  coefficient-absorption route;
- adding an unnecessary coefficient-membership assumption;
- replacing \(T_4\) by \(T_3\);
- interpreting torus-valued periodic points as periodic points having only
  one representative in \(\Gamma^2\);
- admitting \(d=1\) without a new degeneracy analysis.

## Open risks and held-back secondary claims

- The proof uses the published ESS constant without optimizing it.
- The \(81d^2\) union bound is deliberately coarse.
- The exact classification of all infinite \(T_3\) strata is not promoted.
- A \(T_2/T_3\) coefficient stratification is a possible secondary theorem
  but remains pending independent proof.
- No computational check is admissible as a substitute for reviewing the
  table.
