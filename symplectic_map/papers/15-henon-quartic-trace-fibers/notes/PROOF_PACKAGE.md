# Proof Package

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_FRESH_INDEPENDENT_REVIEW / NO_SOURCE_LOCK / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Claim

Let

\[
f_{a,p}(x,y)=(a y+p(x),x),
\]

where \(a\in\mathbb C^\ast\) and \(p\) is monic centered of degree \(d\).
Let \(\operatorname{Trace}_n(f)\) be the formal-period-\(n\) trace multiset,
including scheme-theoretic multiplicity, and let

\[
\mathfrak T_{\le P}
=
(\operatorname{Trace}_1,\ldots,\operatorname{Trace}_P).
\]

The author-side claim is the following unified package.

1. Over any algebraically closed characteristic-zero field, if
   \(s=1-a\), \(q=p-sx\), and
   \[
   C_f(T)=
   \det\!\left(T-M_{p'}\mid k[x]/(q)\right),
   \]
   then
   \[
   C_f'(s)=0.
   \]
   Hence pure fixed trace data leaves at most \(d-1\) Jacobian candidates.

2. Over \(\mathbb C\), on \(\mathcal H^1_4\), the exact
   non-quasi-finite locus of \(\mathfrak T_{\le2}\) is
   \[
   E=\{a=1,\ p=(x^2-L)^2:L\in\mathbb C\}.
   \]
   Its common lower trace fiber is
   \[
   (0^{\times4},2^{\times12}),
   \]
   and
   \[
   E/\mu_3\simeq\mathbb A^1_{L^3}.
   \]

3. Over \(\mathbb C\), \(\mathfrak T_{\le3}\) is quasi-finite on
   \(\mathcal H^1_4\) and on the finite quotient
   \(\mathcal H^1_4/\mu_3\), whereas \(\mathfrak T_{\le2}\) is not. Thus the
   sharp pure-formal-trace cutoff on this single-factor normalized quartic
   space is \(3\).

On \(E\), the second power sum of the formal period-three trace multiset is

\[
\boxed{
S_2^{(3)}(L)
=-1296000-1572864L^3.
}
\]

The formal period-three zero-cycle has pointwise length \(60\), and its
cyclewise second moment is

\[
-432000-524288L^3.
\]

## Status

**PROVABLE AS STATED at the author-proof level, with Parts 2--3 restricted
to \(\mathbb C\).**

This is not a source-lock certification. The final source-stage synthesis
assigned proof confidence \(8.7/10\), below the required \(9.0\), because
the long exact period-three transcription and the external theorem scopes
still require a fresh replay. Lifecycle progression is therefore blocked
pending an independent proof-and-citation review, not by a known
mathematical counterexample.

No descent of Cantat--Dujardin Theorem 4.2 or Sugiyama's complex moduli
theorem to an arbitrary algebraically closed characteristic-zero field is
claimed. Part 1 is the only separately field-general statement.

## Assumptions

- In Part 1, the base field is algebraically closed of characteristic zero.
- In Parts 2--3, the base field is \(\mathbb C\).
- The source is the single-factor monic-centered normalized space
  \(\mathcal H^1_d\), not a multifactored normal form.
- The trace data is formal-period data with intersection multiplicities.
- Cantat--Dujardin Theorem 4.2 is used only after the Jacobian has been
  restricted to finitely many candidates and only for \(a\ne1\).
- Sugiyama is used only for a quartic one-variable polynomial with four
  simple fixed points.
- The standard trace--residue identity for a finite zero-dimensional
  complete intersection is used in the explicit period-three calculation.

## Notation

- \(J(f)=-a\) is the Jacobian.
- \(s=1-a=1+J(f)\).
- \(q=p-sx\); fixed points correspond to roots of \(q\).
- For a finite algebra \(A\) and \(h\in A\), \(M_h\) is multiplication by
  \(h\). Its formal value multiset is the root multiset of
  \(\det(T-M_h)\).
- \(\operatorname{Sym}^r(\mathbb C)\) denotes the symmetric product, viewed
  through elementary symmetric coordinates.
- In the period-three calculation, all cyclic indices lie in
  \(\mathbb Z/3\mathbb Z\).

## External theorem scopes

### Cantat--Dujardin

The controlling source is the author PDF dated May 10, 2026.

- Theorem 3.7 gives existence of some finite period cutoff depending on the
  degree. It does not give \(P(4)=3\).
- Theorem 4.2 says that, for a complex single Hénon map of given degree with
  Jacobian different from \(-1\), the data consisting of the Jacobian and
  formal traces in periods one and two has finite fibers.
- Example 4.3 gives the Jacobian-\(-1\) quartic family
  \(p_\lambda=(x^2-\lambda^2)^2\) with constant period-one and period-two
  trace data.

Theorem 4.2 does not remove the Jacobian input. Step 2 below does that
before Theorem 4.2 is invoked.

### Sugiyama

For a one-variable degree-\(d\) polynomial with no multiple fixed point, the
unordered fixed-multiplier map has finite fibers in polynomial moduli. It is
used below only on the root partition \([1111]\). It is not used for any
multiple-root stratum.

## Proof strategy

1. Encode the formal fixed traces in one characteristic polynomial and
   prove the derivative identity \(C_f'(s)=0\).
2. Enumerate finitely many Jacobians from pure trace data.
3. Apply Cantat--Dujardin at every candidate \(a\ne1\).
4. On \(a=1\), show period two is a formal consequence of period one and
   classify all five quartic root partitions.
5. Identify \(E\) as the unique positive-dimensional lower-period fiber.
6. Reconstruct the formal period-three calculation on \(E\), including the
   two-term support argument, two slope ledgers, the constant ledger, formal
   fixed subtraction, and local lengths.
7. Use the nonzero \(L^3\)-coefficient to make all period-\(\le3\) fibers
   finite, then apply the finite-type criterion for quasi-finiteness.

## Dependency map

1. Part A depends only on the fixed algebra and the monic-polynomial residue
   identity \(\sum q'(\alpha)^{-1}=0\).
2. The \(a\ne1\) locus depends on Part A and Cantat--Dujardin Theorem 4.2.
3. The \(a=1\), \([1111]\) stratum depends on Sugiyama within its
   no-multiple-fixed-point domain.
4. The \([31]\) and \([211]\) strata depend on explicit root coordinates.
5. The exceptional curve depends on the \([22]\) and \([4]\) partitions.
6. The period-three separator depends on the monic complete intersection,
   trace--residue identity, coefficient ledgers, zero fixed contribution,
   and local-length calculation.
7. Global quasi-finiteness depends on finite geometric fibers of a
   finite-type morphism.

## Proof

### Step 1. Formal trace morphisms and the residual finite action

For fixed \(n\), the formal-period cycle has constant degree \(p_n\) over
the normalized parameter space. The trace function

\[
(f,z)\longmapsto\operatorname{tr}(D_zf^n)
\]

is regular on that cycle. Taking its elementary symmetric functions defines
a regular map

\[
\operatorname{Trace}_n:
\mathcal H^1_d\longrightarrow
\operatorname{Sym}^{p_n}(\mathbb C).
\]

For \(\zeta^{d-1}=1\), let

\[
h_\zeta(x,y)=(\zeta x,\zeta y).
\]

A direct calculation gives

\[
h_\zeta^{-1}f_{a,p}h_\zeta(x,y)
=
\left(
a y+\zeta^{-1}p(\zeta x),x
\right).
\]

The transformed polynomial is again monic centered because
\(\zeta^{d-1}=1\). Conjugacy preserves all formal trace multisets, so every
\(\mathfrak T_{\le P}\) descends through the finite
\(\mu_{d-1}\)-quotient.

### Step 2. The fixed-algebra identity \(C_f'(s)=0\)

A fixed point satisfies \(y=x\) and

\[
p(x)-(1-a)x=0.
\]

Thus, with \(s=1-a\),

\[
A_q=k[x]/(q),
\qquad
q=p-sx.
\]

The derivative matrix is

\[
Df(x,y)=
\begin{pmatrix}
p'(x)&a\\
1&0
\end{pmatrix},
\]

so the formal fixed trace multiset is exactly the formal value multiset of
\(p'\) in \(A_q\). Hence it determines

\[
C_f(T)=\det(T-M_{p'}\mid A_q),
\]

a monic polynomial of degree \(d\).

We prove \(C_f'(s)=0\) in two exhaustive cases.

#### Case 2.1. The polynomial \(q\) is squarefree

Let \(\alpha_1,\ldots,\alpha_d\) be its roots. Since

\[
p'=q'+s,
\]

we have

\[
C_f(T)
=
\prod_{i=1}^d
\bigl(T-s-q'(\alpha_i)\bigr).
\]

No \(q'(\alpha_i)\) vanishes. Therefore

\[
\frac{C_f'(s)}{C_f(s)}
=
\sum_{i=1}^d
\frac{1}{s-p'(\alpha_i)}
=
-\sum_{i=1}^d\frac1{q'(\alpha_i)}.
\]

For completeness, the last sum is zero. Lagrange interpolation of the
constant polynomial \(1\) gives

\[
1
=
\sum_{i=1}^d
\frac{q(x)}{q'(\alpha_i)(x-\alpha_i)}.
\]

The coefficient of \(x^{d-1}\) on the left is zero because \(d\ge2\);
on the right it is \(\sum_iq'(\alpha_i)^{-1}\). Thus

\[
\sum_i\frac1{q'(\alpha_i)}=0
\]

and \(C_f'(s)=0\).

#### Case 2.2. The polynomial \(q\) is not squarefree

Choose a root \(\alpha\) of multiplicity \(m\ge2\). In its length-\(m\)
local factor, \(q'\) lies in the maximal ideal and is nilpotent. Since

\[
p'=s+q',
\]

multiplication by \(p'\) on that factor has only the eigenvalue \(s\), with
algebraic multiplicity \(m\). Consequently

\[
(T-s)^m\mid C_f(T).
\]

Because \(m\ge2\), \(C_f'(s)=0\).

The two cases prove the identity.

Since \(C_f\) is monic of degree \(d\) and the characteristic is zero,
\(C_f'\) is nonzero of degree \(d-1\). Thus a prescribed
\(\operatorname{Trace}_1\), equivalently a prescribed \(C_f\), allows at
most \(d-1\) values of \(s\). Because \(J=s-1\), it allows at most
\(d-1\) Jacobians. In degree four the bound is \(3\).

### Step 3. Finite lower-period fibers for every candidate \(a\ne1\)

Fix a value of \(\mathfrak T_{\le2}\) in degree four. Step 2 restricts
\(s\), hence \(a=1-s\), to at most three possibilities. Values with \(a=0\)
do not lie in the Hénon parameter space and are discarded.

For every remaining candidate \(a\ne1\), the Jacobian \(-a\) is different
from \(-1\). Cantat--Dujardin Theorem 4.2 applies over \(\mathbb C\) and
says that fixed \(a\), \(\operatorname{Trace}_1\), and
\(\operatorname{Trace}_2\) leave only finitely many normalized maps. A
finite union over the at most three candidate values is finite.

This step uses no hidden Jacobian input: the candidates were derived from
\(\operatorname{Trace}_1\) before the theorem was applied.

### Step 4. On \(a=1\), formal period two is determined by period one

Now set \(a=1\). Fixed points satisfy \(p(x)=0\), so

\[
A_1=\mathbb C[x]/(p).
\]

Let the formal eigenvalues of \(M_{p'}\) be

\[
r_1,\ldots,r_4,
\]

repeated with local-algebra multiplicity. This is
\(\operatorname{Trace}_1\).

A point fixed by \(f^2\) satisfies

\[
p(x)=0,
\qquad
p(y)=0.
\]

Hence the full \(f^2\)-fixed algebra is

\[
A_2
=
\mathbb C[x,y]/(p(x),p(y))
\simeq A_1\otimes_\mathbb C A_1
\]

of length \(16\). Direct matrix multiplication gives

\[
\operatorname{tr}(Df^2)
=
2+p'(x)p'(y).
\]

Its full formal value multiset is therefore

\[
\{\,2+r_i r_j:1\le i,j\le4\,\}.
\]

On the embedded fixed cycle, the value is

\[
2+r_i^2
\]

with fixed local multiplicity. Formal period two is the full length-\(16\)
cycle minus this length-\(4\) fixed cycle. Thus its length is \(12\), and
its trace multiset is determined functorially by
\(\{r_1,\ldots,r_4\}\).

This subtraction is scheme-theoretic. It does not discard nonreduced
support or replace nilpotents by reduced points.

It follows that, on the \(a=1\) slice, the fibers of
\(\mathfrak T_{\le2}\) are exactly the fibers of
\(\operatorname{Trace}_1\).

### Step 5. Complete quartic root-partition analysis on \(a=1\)

The formal eigenvalue attached to a root \(\alpha\) of \(p\) is
\(p'(\alpha)\), repeated with the root's local length. Every monic centered
quartic has one of the five partitions below.

#### Partition \([1111]\)

All roots of \(p\) are simple, so every \(p'(\alpha)\ne0\). Put

\[
h(x)=x+p(x).
\]

The roots of \(p\) are the fixed points of \(h\), and their multipliers are

\[
h'(\alpha)=1+p'(\alpha)\ne1.
\]

Thus the multiplier tuple lies in Sugiyama's open set \(V_4\), where there
are no multiple fixed points. Sugiyama's finite-fiber theorem gives only
finitely many affine conjugacy classes of \(h\). Every class has only
finitely many monic-centered representatives, differing by the residual
\(\mu_3\)-action. Therefore every fixed-trace fiber in the \([1111]\)
stratum is finite.

No Sugiyama result is used outside this stratum.

#### Partition \([31]\)

Let the triple root be \(r\). Centering forces the simple root to be
\(-3r\), so

\[
p(x)=(x-r)^3(x+3r).
\]

The triple root contributes \(0\) three times. At the simple root,

\[
p'(-3r)=(-3r-r)^3=-64r^3.
\]

Thus

\[
\operatorname{Trace}_1
=
\{0,0,0,-64r^3\}.
\]

A prescribed trace multiset determines \(r^3\), hence leaves at most three
values of \(r\) in the normalized slice and one value modulo \(\mu_3\).
The fiber is finite, including the boundary \(r=0\), which is the
\([4]\) point.

#### Partition \([211]\)

Write the double root as \(r\), and the two simple roots as

\[
r+u,\qquad r+v.
\]

The stratum conditions are

\[
u\ne0,\qquad v\ne0,\qquad u\ne v.
\]

Centering gives

\[
4r+u+v=0.
\]

At the two simple roots the derivative values are

\[
A=u^2(u-v),
\qquad
B=-v^2(u-v).
\]

The double root contributes \(0\) twice. Hence

\[
\operatorname{Trace}_1=\{0,0,A,B\}.
\]

Choose one of the two possible orderings of the nonzero values \(A,B\).
Then

\[
\frac BA=-\left(\frac vu\right)^2.
\]

The ratio determines \(z=v/u\) up to at most two choices. Since \(z\ne1\),

\[
A=u^3(1-z)
\]

determines \(u^3\), hence leaves at most three choices for \(u\). Then
\(v=zu\) and \(r=-(u+v)/4\). Accounting for the possible interchange of
\(A\) and \(B\) still leaves a finite set.

The excluded boundary cases are all already covered:

- \(u=0\) or \(v=0\) gives \([31]\);
- \(u=v\ne0\) gives \([22]\);
- \(u=v=0\) gives \([4]\).

#### Partitions \([22]\) and \([4]\)

For \([22]\), centering makes the two double roots opposite:

\[
p(x)=(x-r)^2(x+r)^2=(x^2-L)^2,
\qquad
L=r^2.
\]

The case \(L=0\) is \([4]\). Conversely every \(p=(x^2-L)^2\) has only
multiple roots. Therefore these two partitions form exactly the curve

\[
E=\{a=1,\ p=(x^2-L)^2\}.
\]

Every fixed trace is zero, so

\[
\operatorname{Trace}_1=0^{\times4}.
\]

Step 4 then gives

\[
\operatorname{Trace}_2=2^{\times12}.
\]

The converse is also exact: if
\(\operatorname{Trace}_1=0^{\times4}\), then \(p'(\alpha)=0\) at every
root, so every root is multiple. The only degree-four partitions are
\([22]\) and \([4]\), hence \(p=(x^2-L)^2\).

### Step 6. Exact non-quasi-finite locus and quotient coordinate

Steps 3 and 5 show that every \(\mathfrak T_{\le2}\)-fiber outside \(E\) is
finite. Every point of \(E\) lies in the positive-dimensional fiber

\[
(0^{\times4},2^{\times12}).
\]

In fact the preimage of this displayed trace value is exactly \(E\). Its
fixed characteristic polynomial is \(C_f(T)=T^4\), so Step 2 gives

\[
0=C_f'(s)=4s^3,
\]

hence \(s=0\) and \(a=1\). Step 5 then forces
\(p=(x^2-L)^2\).

The trace map is of finite type. At every point outside \(E\), its geometric
fiber is finite, so that point is a quasi-finite point. At every point of
\(E\), the same fiber contains the curve \(E\), so the map is not
quasi-finite. Thus the exact non-quasi-finite locus is \(E\).

For \(\zeta^3=1\),

\[
\zeta^{-1}(\zeta^2x^2-L)^2
=
(x^2-\zeta L)^2.
\]

Therefore the residual action is \(L\mapsto\zeta L\), whose invariant ring
is \(\mathbb C[L^3]\). Hence

\[
E/\mu_3\simeq\mathbb A^1_{L^3}.
\]

### Step 7. The formal period-three complete intersection on \(E\)

Put

\[
p_L(x)=(x^2-L)^2,
\qquad
q_L(x)=p_L'(x)=4x(x^2-L).
\]

Introduce a deformation parameter \(\varepsilon\) and cyclic equations

\[
F_i
=
(x_i^2-L)^2
+\varepsilon(x_{i-1}-x_{i+1}).
\]

At \(\varepsilon=1\), these are the three recurrence equations for
\(\operatorname{Fix}(f_L^3)\). Their leading monomials are
\(x_0^4,x_1^4,x_2^4\), which are pairwise coprime. Thus

\[
\mathcal A
=
\mathbb C[L,\varepsilon,x_0,x_1,x_2]/(F_0,F_1,F_2)
\]

is free of rank \(4^3=64\) over \(\mathbb C[L,\varepsilon]\), with standard
monomials \(x_0^{e_0}x_1^{e_1}x_2^{e_2}\), \(0\le e_i<4\).

The Jacobian determinant is

\[
t_\varepsilon
=
q_0q_1q_2
+\varepsilon^2(q_0+q_1+q_2),
\qquad
q_i=4x_i(x_i^2-L).
\]

At \(\varepsilon=1\), direct multiplication of the three derivative
matrices gives the same expression:

\[
t_1=\operatorname{tr}(Df_L^3).
\]

For a finite complete intersection, the trace--residue identity says

\[
\operatorname{Tr}_{\mathcal A/\mathbb C[L,\varepsilon]}
(M_h)
=
\operatorname{Res}(h\,t_\varepsilon).
\]

Taking \(h=t_\varepsilon^2\), the raw \(f^3\)-fixed second trace moment is

\[
\operatorname{Tr}(M_{t_\varepsilon^2})
=
\operatorname{Res}(t_\varepsilon^3),
\]

which equals the coefficient of \(x_0^3x_1^3x_2^3\) in the normal form of
\(t_\varepsilon^3\).

### Step 8. Why only two parameter monomials survive

Give weights

\[
\operatorname{wt}(x_i)=1,
\qquad
\operatorname{wt}(L)=2,
\qquad
\operatorname{wt}(\varepsilon)=3.
\]

Then \(F_i\) has weight \(4\), \(q_i\) has weight \(3\), and
\(t_\varepsilon\) has weight \(9\). The quotient trace of
\(t_\varepsilon^2\) has weight \(18\). Therefore the only initially
possible parameter monomials are

\[
\varepsilon^6,\qquad
L^3\varepsilon^4,\qquad
L^6\varepsilon^2,\qquad
L^9.
\]

At \(\varepsilon=0\), the algebra is the tensor product of three copies of

\[
\mathbb C[L,x]/((x^2-L)^2).
\]

In every factor \(q_i^2=0\), while \(t_0=q_0q_1q_2\). Thus
\(t_0^2=0\), and the \(L^9\) term vanishes.

It remains to eliminate \(L^6\varepsilon^2\). It is enough to work at
\(L\ne0\), a Zariski-dense parameter set. Choose the two roots of
\(x^2=L\), work over an algebraic closure of the Puiseux field in
\(\varepsilon\), and normalize \(v(\varepsilon)=1\). Flatness clusters all
\(64\) solutions around triples

\[
(\alpha_0,\alpha_1,\alpha_2),
\qquad
\alpha_i^2=L.
\]

Write \(x_i=\alpha_i+\delta_i\). Because \(\alpha_i\ne0\),

\[
(x_i^2-L)^2=c_i\delta_i^2+O(\delta_i^3),
\qquad
q_i=d_i\delta_i+O(\delta_i^2),
\]

with \(c_i,d_i\ne0\).

If exactly two \(\alpha_i\) agree, cyclically relabel so
\(\alpha_0=\alpha_1\ne\alpha_2\). The first two equations have nonzero
constant coupling terms, so

\[
v(q_0)=v(q_1)=\tfrac12.
\]

The remaining coupling has valuation at least \(3/2\). If
\(v(\delta_2)<3/4\), its square would be the unique lowest-valuation term,
which cannot cancel. Thus

\[
v(q_2)\ge\tfrac34,
\qquad
v(t_\varepsilon)\ge\tfrac74.
\]

If all three roots agree, let \(r\) be the least valuation of a nonzero
\(\delta_i\). Every coupling has valuation at least \(1+r\). If \(r<1\),
the square term at an index attaining \(r\) has strictly smaller valuation
\(2r\), again impossible. Hence

\[
v(t_\varepsilon)\ge3
\]

on every nontrivial branch in that cluster.

The exact diagonal fixed branch has zero contribution to the second moment,
as Step 9 proves. A finite-algebra trace is the sum of support values
weighted by local length; nilpotent parts have trace zero. Hence every
nonfixed cluster contributes to the trace of \(t_\varepsilon^2\) with
\(\varepsilon\)-valuation strictly greater than \(2\). The coefficient of
\(L^6\varepsilon^2\) must vanish.

Therefore there are integers \(C_2,D_2\) such that

\[
S_2(L,\varepsilon)
=
C_2\varepsilon^6
+D_2L^3\varepsilon^4.
\]

### Step 9. Formal fixed subtraction in period three

On the fixed algebra

\[
B_1=\mathbb C[x]/((x^2-L)^2),
\]

all three cyclic coordinates agree. Put \(q=4x(x^2-L)\). Then

\[
q^2=0
\]

in \(B_1\), and

\[
t_\varepsilon=q^3+3\varepsilon^2q.
\]

Consequently

\[
t_\varepsilon^2=0.
\]

At \(\varepsilon=1\), the full fixed contribution to the second trace
moment is zero. Thus the formal period-three moment, defined by subtracting
the formal fixed cycle from the \(f^3\)-fixed cycle, equals the raw residue
moment \(S_2(L,1)\).

### Step 10. First exact slope ledger

Define, for the finite coefficient certificate,

\[
H(r,k)
=
\sum_{\substack{u+v=k\\2u\le r,\ 2v\le r}}
\binom{k}{u}\binom{r}{2u}\binom{r}{2v}
\]

and

\[
A_{m,r}
=
\sum_{k=\lceil m/2\rceil}^{\min(m-1,r)}
(-1)^{r+k}
\binom{m-1}{2(m-k)-1}H(r,k).
\]

The coefficient extraction for the family
\((x^m-a)^2\), specialized here only as a finite algebraic ledger, is

\[
D_m
=
3\sum_{j=0}^{\lfloor m/2\rfloor}
\binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j}.
\]

At \(m=2\),

\[
H(2,1)=2,
\qquad
A_{2,2}=-2,
\qquad
A_{2,1}=0.
\]

Indeed the two admissible pairs for \(H(2,1)\) are
\((u,v)=(0,1),(1,0)\), while no pair survives the \(r=1\) parity bounds.
Substitution gives

\[
\boxed{
D_2
=
3\cdot4^9(-2)
=
-1572864.
}
\]

This is a separate finite provenance certificate reproduced inside the
package. Logical self-containment of the quartic theorem does not require
accepting an unstated all-\(m\) derivation: the next step starts again from
the defining quartic residue and independently reconstructs the same value.

### Step 11. Independent tensor-Laurent slope ledger

Put

\[
P_L(x)=(x^2-L)^2,
\qquad
g_L(x)=x(x^2-L),
\qquad
\Lambda_i=x_{i-1}-x_{i+1}.
\]

Then

\[
F_i=P_L(x_i)+\varepsilon\Lambda_i,
\]

and

\[
t_\varepsilon
=
4^3g_0g_1g_2
+4\varepsilon^2(g_0+g_1+g_2).
\]

Thus

\[
t_\varepsilon^3
=
\sum_{j=0}^3
\binom3j4^{9-2j}\varepsilon^{2j}G_j,
\]

where

\[
G_j
=
(g_0g_1g_2)^{3-j}
(g_0+g_1+g_2)^j.
\]

Define

\[
\mathscr L_j(L,\varepsilon)
=
[x_0^{-1}x_1^{-1}x_2^{-1}]
\frac{G_j}{F_0F_1F_2}.
\]

The desired \(L^3\varepsilon^4\)-coefficient is

\[
\mathcal C_{2,j}
=
[L^3\varepsilon^{4-2j}]
\mathscr L_j(L,\varepsilon),
\]

and

\[
D_2
=
\sum_{j=0}^3
\binom3j4^{9-2j}\mathcal C_{2,j}.
\]

Weighted homogeneity makes the selected coefficient a constant multiple of
\(L^3\), so set \(L=1\) inside the one-variable Laurent evaluation. Write

\[
P(x)=(x^2-1)^2,
\qquad
g(x)=x(x^2-1).
\]

Expand

\[
\frac1{P_i+\varepsilon\Lambda_i}
=
\sum_{h_i\ge0}
(-1)^{h_i}\varepsilon^{h_i}
\frac{\Lambda_i^{h_i}}{P_i^{h_i+1}}.
\tag{11.1}
\]

Define

\[
\rho_{n,h}(e)
=
[x^{-1}]
\frac{x^e g(x)^n}{P(x)^{h+1}}.
\]

From

\[
\frac{g^3}{P}=x^3(x^2-1),
\qquad
\frac{g^3}{P^2}=\frac{x^3}{x^2-1},
\qquad
\frac{g^3}{P^3}=\frac{x^3}{(x^2-1)^3},
\]

one obtains

\[
\rho_{3,0}(e)=0\quad(e\ge0),
\]

\[
\rho_{3,1}(0)=\rho_{3,1}(2)=1,
\qquad
\rho_{3,1}(1)=0,
\]

and

\[
\rho_{3,2}(0)=\rho_{3,2}(1)=0,
\qquad
\rho_{3,2}(2)=1.
\]

For \(j=0\), equation (11.1) must supply total denominator increment

\[
h_0+h_1+h_2=4.
\]

The \(\rho_{3,0}\)-vanishing forces all \(h_i\ge1\), so the only cases are
the three cyclic arrangements of \((2,1,1)\). For
\((h_0,h_1,h_2)=(2,1,1)\), the tensor coefficient is

\[
(\rho_{3,2}\otimes\rho_{3,1}\otimes\rho_{3,1})
(\Lambda_0^2\Lambda_1\Lambda_2).
\]

Here

\[
\Lambda_0=x_2-x_1,
\quad
\Lambda_1=x_0-x_2,
\quad
\Lambda_2=x_1-x_0,
\]

and

\[
\Lambda_1\Lambda_2
=
-x_0^2+x_0(x_1+x_2)-x_1x_2.
\]

Taking the required \(x_0\)-coefficient leaves

\[
-(x_2-x_1)^2.
\]

The remaining two Laurent coefficients give

\[
-(1+0+1)=-2.
\]

All three cyclic placements give \(-2\), and the sign
\((-1)^4\) is positive. Therefore

\[
\mathcal C_{2,0}=-6.
\]

For \(j=1\), every monomial of \(G_1\) has exponent type
\((3,2,2)\), while the required total denominator increment is \(2\).
At a coordinate with \(h_i=0\), both

\[
\frac{g^2}{P}=x^2
\quad\text{and}\quad
\frac{g^3}{P}=x^3(x^2-1)
\]

are polynomials. Nonnegative powers coming from the \(\Lambda_i\) cannot
create an \(x_i^{-1}\)-term. Nonvanishing would require all three
\(h_i\ge1\), contradicting total increment \(2\). Hence

\[
\mathcal C_{2,1}=0.
\]

For \(j=2\), the required internal \(\varepsilon\)-degree is zero. Put

\[
\mu_n=[x^{-1}]\frac{g(x)^n}{P(x)}.
\]

Direct Laurent expansion gives

\[
\mu_1=1,
\qquad
\mu_2=0,
\qquad
\mu_3=0.
\]

The square terms in \(G_2\) have exponent type \((3,1,1)\), and the cross
terms have type \((2,2,1)\). Their tensor coefficients are respectively

\[
\mu_3\mu_1^2
\quad\text{and}\quad
\mu_2^2\mu_1,
\]

both zero. Thus

\[
\mathcal C_{2,2}=0.
\]

The \(j=3\) summand already contains \(\varepsilon^6\) and cannot contribute
to \(\varepsilon^4\). Consequently

\[
\boxed{
D_2=4^9(-6)=-1572864,
}
\]

exactly matching Step 10.

### Step 12. Exact constant ledger

Set \(L=0\) and \(\varepsilon=1\). Then

\[
F_i=x_i^4+x_{i-1}-x_{i+1}
\]

and

\[
t
=
64x_0^3x_1^3x_2^3
+4(x_0^3+x_1^3+x_2^3).
\]

Let \(R(e_0,e_1,e_2)\) be the coefficient of
\(x_0^3x_1^3x_2^3\) in the normal form of
\(x_0^{e_0}x_1^{e_1}x_2^{e_2}\). The defining equations give the exact
recurrences

\[
\begin{aligned}
R(e_0,e_1,e_2)
&=
R(e_0-4,e_1+1,e_2)
-R(e_0-4,e_1,e_2+1),\\
R(e_0,e_1,e_2)
&=
-R(e_0+1,e_1-4,e_2)
+R(e_0,e_1-4,e_2+1),\\
R(e_0,e_1,e_2)
&=
R(e_0+1,e_1,e_2-4)
-R(e_0,e_1+1,e_2-4).
\end{aligned}
\tag{12.1}
\]

The terminal value is \(R(3,3,3)=1\), and every other standard exponent
triple has value zero. Repeated application of (12.1) gives the complete
ledger needed for \(t^3\):

| Exponent pattern | \(R\)-value |
|---|---:|
| \((9,9,9)\) | \(-6\) |
| cyclic permutation of \((9,6,6)\) | \(2\) |
| cyclic permutation of \((9,3,3)\) | \(0\) |
| cyclic permutation of \((6,6,3)\) | \(-1\) |
| permutation of \((9,0,0)\) | \(0\) |
| permutation of \((6,3,0)\) | \(0\) |
| \((3,3,3)\) | \(1\) |

Each application of (12.1) lowers total exponent by \(3\), so this
certificate terminates at standard exponent triples. The table is therefore
fully replayable from the three displayed recurrences without a hidden
reduction rule.

For two explicit checks,

\[
R(9,6,6)
=
R(5,7,6)-R(5,6,7)
=
1-(-1)
=2,
\]

and

\[
R(9,9,9)
=
2R(5,10,9)
=
2(1-4)
=-6.
\]

Put

\[
Q=64x_0^3x_1^3x_2^3,
\qquad
R_0=4(x_0^3+x_1^3+x_2^3).
\]

Grouping \((Q+R_0)^3\) by the preceding patterns gives:

| Source | Top-coefficient contribution |
|---|---:|
| \(Q^3\) | \(262144(-6)=-1572864\) |
| \(3Q^2R_0\) | \(3\cdot49152\cdot2=294912\) |
| square terms in \(3QR_0^2\) | \(0\) |
| mixed terms in \(3QR_0^2\) | \(3\cdot6144(-1)=-18432\) |
| pure and \(2+1\) terms in \(R_0^3\) | \(0\) |
| fully mixed term in \(R_0^3\) | \(384\) |

Their sum is

\[
\boxed{
C_2
=
-1572864+294912-18432+384
=
-1296000.
}
\]

Combining Steps 8, 11, and 12 gives

\[
\boxed{
S_2(L,\varepsilon)
=
-1296000\varepsilon^6
-1572864L^3\varepsilon^4.
}
\]

At \(\varepsilon=1\), Step 9 identifies this with the formal
period-three second moment.

### Step 13. Fixed-branch local lengths and cyclewise normalization

Let \(\alpha\) be a root of \(p_L\) of multiplicity \(r\ge2\). Put

\[
\delta=x_0-\alpha,
\qquad
u=x_1-x_0,
\qquad
v=x_2-x_0.
\]

At \((\delta,u,v)=(0,0,0)\), the \((u,v)\)-Jacobian of
\((F_1,F_2)\) at \(\varepsilon=1\) is

\[
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\]

which is invertible. Formal elimination therefore gives

\[
u=-p_L(\alpha+\delta)+O(\delta^{2r-1}),
\qquad
v=p_L(\alpha+\delta)+O(\delta^{2r-1}).
\]

The remaining equation is

\[
F_0
=
p_L(\alpha+\delta)+v-u
=
3p_L(\alpha+\delta)+O(\delta^{2r-1}).
\]

Since \(2r-1>r\) and the characteristic is zero, its order is exactly
\(r\). Thus the local length of the \(f^3\)-fixed scheme at every fixed
point equals its fixed-scheme length. No residual fixed support remains
after the prime-period subtraction.

The full \(f^3\)-fixed algebra has length \(64\), and the fixed algebra has
length \(4\). Hence the formal period-three zero-cycle has pointwise length

\[
64-4=60.
\]

Every remaining orbit has exactly three points. Matrix trace is cyclically
invariant along the orbit, so the pointwise second moment is three times
the cyclewise moment. Therefore

\[
\frac{-1296000-1572864L^3}{3}
=
-432000-524288L^3.
\]

### Step 14. Global quasi-finiteness and sharpness

For a value of \(\mathfrak T_{\le3}\), first forget period three.

- If the corresponding lower-period fiber lies outside \(E\), Steps 3--6
  show it is finite, so adding period-three equality keeps it finite.
- If the lower-period value is
  \((0^{\times4},2^{\times12})\), Step 2 gives
  \(C(T)=T^4\), hence \(C'(s)=4s^3\) and \(s=0\). Thus \(a=1\), and Step 5
  says the entire lower-period fiber is exactly \(E\).
- On \(E\), equality of the full formal period-three trace multiset implies
  equality of its second power sum:
  \[
  -1296000-1572864L^3
  =
  -1296000-1572864M^3.
  \]
  Since the coefficient is nonzero, \(L^3=M^3\). There are at most three
  normalized representatives and exactly one quotient coordinate.

Thus every geometric fiber of \(\mathfrak T_{\le3}\) is finite. The source
and target are finite-type complex varieties. Stacks Project Tag 02NH
therefore makes \(\mathfrak T_{\le3}\) quasi-finite.

Because the trace map is \(\mu_3\)-invariant and the quotient is finite, the
same finite-fiber argument proves quasi-finiteness on
\(\mathcal H^1_4/\mu_3\).

On the other hand, \(\mathfrak T_{\le2}\) has the curve \(E\) as one fiber,
and its quotient map has the curve
\(E/\mu_3\simeq\mathbb A^1_{L^3}\) as one fiber. Period two is therefore
insufficient, while period three is sufficient. The cutoff is sharply
\(3\).

This completes the author-side proof. \(\square\)

## Corrections and scope controls

- The quartic Jacobian candidate count is \(3\), not \(7\).
- Parts B and C are over \(\mathbb C\); no base-change descent is silently
  asserted.
- Cantat--Dujardin is used with fixed Jacobian and only after finite
  candidate enumeration.
- Sugiyama is used only on \([1111]\).
- Quasi-finite does not mean injective.
- The pointwise moment separates \(E\), not the entire quartic moduli space
  by itself.
- The formula uses formal period-three multiplicities, not only reduced
  exact-period points.

## Open risks

- A fresh reviewer must replay both slope ledgers and every row of the
  constant ledger; the current \(8.7/10\) synthesis score reflects
  transcription risk in these exact integers.
- The finite-type/quasi-finite passage and the descent through the finite
  quotient must be checked in the exact target-coordinate model chosen for
  any manuscript.
- The precise statement of Sugiyama used on \([1111]\) and the
  formal-period convention in Cantat--Dujardin must be reopened in the
  controlling primary sources.
- No claim is made about an exact global degree, a branch locus, or
  injectivity.
- No all-degree period-three statement is present.
