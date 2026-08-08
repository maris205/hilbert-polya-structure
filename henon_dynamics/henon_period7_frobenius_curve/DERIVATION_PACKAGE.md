# HCS-C19 derivation package

## 1. Frozen object

Paper 5 uses

\[
q_{t+1}=1-aq_t^2-q_{t-1}.
\]

For \(a\ne0\), the change \(x_t=aq_t\) gives the Hamiltonian recurrence

\[
x_{t+1}=a-x_t^2-x_{t-1}.
\]

Endler--Gallas give the period-seven chiral factor

\[
C_7(\sigma)=\sigma^2-2\sigma-a
\]

and print a monic degree-seven coordinate polynomial in their Eq. (16).  The
printed final term is

\[
-2a^3+6a^2+2a+3(a^3-4a^2+a-2)\sigma.
\]

Taken literally, it does not encode their stated period-seven orbits: after
the chiral substitution its \(x\)-discriminant has degree 42 in \(\sigma\),
and it fails the exact modular witness in Section 2.  The block selected at
that specialization and generically certified in Section 3 is

\[
-2a^3+6a^2+2a+3+(a^3-4a^2+a-2)\sigma.
\]

We call the adopted polynomial \(\bar P_7^{\rm corr}\) and freeze

\[
P(\sigma,x)=\bar P_7^{\rm corr}(x;\sigma,\sigma^2-2\sigma)
\]

and let \(C\) be the smooth projective normalization of \(P=0\).  The
parameter line \(C_7=0\) itself is rational; the genus-three statement applies
only to the explicit septic cover \(C\to\mathbb P^1_\sigma\).  The neighbor
theorem proves that it is generically one exact-period-seven Hénon component;
exhaustion of the full saturated scheme is not asserted.

At \(a=0\), equivalently \(\sigma=0,2\), the Paper-5/Hamiltonian coordinate
change degenerates.  Those fibres remain boundary points of the algebraic
closure \(C\); no direct Paper-5 orbit interpretation is asserted there.

## 2. Exact correction witness and polynomial

Work over \(\mathbb F_{103}\) with \(a=6\) and \(\sigma=26\).  The two ordered
state cycles

\[
\begin{aligned}
&(10,54),(58,10),(31,58),(17,31),(98,17),(67,98),(54,67),\\
&(10,58),(54,10),(67,54),(98,67),(17,98),(31,17),(58,31)
\end{aligned}
\]

are exchanged by \((x,y)\mapsto(y,x)\), satisfy
\((x,y)\mapsto(6-x^2-y,x)\) exactly, and have coordinate sum 26.  The
adopted polynomial has roots

\[
\{10,17,31,54,58,67,98\},
\]

whereas the literal printed polynomial has roots \(\{55,60\}\).  This proves
that the printed expression cannot encode the claimed cycles at this exact
specialization.  The project records an apparent print error, not an official
publisher erratum.  Generic dynamical certification is supplied independently
by the neighbor correspondence below.

Writing \(a=\sigma^2-2\sigma\),

\[
\begin{aligned}
P={}&x^7-\sigma x^6-(3a-2\sigma)x^5
 -(2a-(3a-4)\sigma-4)x^4\\
&+(3a^2-2(2a-1)\sigma+1)x^3\\
&+(4a^2-10a-(3a^2-8a+1)\sigma-2)x^2\\
&-(a-1)(a^2-2a\sigma+a+2)x\\
&-2a^3+6a^2+2a+3+(a^3-4a^2+a-2)\sigma.
\end{aligned}
\]

Specializing the adopted curve at \(\sigma=-3\) and reducing modulo 2 gives

\[
x^7+x^6+x^5+x^4+1,
\]

which is irreducible over \(\mathbb F_2\).  Monicity in \(x\) proves
irreducibility over \(\mathbb Q(\sigma)\).  The cover has prime degree seven
and nontrivial geometric inertia below, so its geometric monodromy is
transitive; hence the curve is geometrically integral.

## 3. Generic neighbor correspondence and oriented lift

In \(A=\mathbb Q(\sigma)[x]/(P)\), the gcd in \(y\) of

\[
P(\sigma,y),\qquad P(\sigma,a-y^2-x)
\]

has degree two.  Writing its last nonzero subresultant as
\(c_2y^2+c_1y+c_0\), exact quotient reduction gives

\[
c_1=c_2(x^2-a).
\]

The quadratic discriminant and its diagonal value at \(y=x\) are nonzero in
\(A\).  Hence the seven roots carry a simple two-regular neighbor graph.  The
relation is symmetric because the other neighbor of \(x\) is
\(a-x^2-y\).  Geometric monodromy is transitive and preserves components; in
prime degree seven the graph must therefore be one seven-cycle.

The ordered edges define a generic degree-14 cover \(\widetilde C\), with

\[
\tau(x,y)=(a-x^2-y,x),\qquad R(x,y)=(y,x),
\]

and

\[
\tau^7=R^2=1,\qquad R\tau R=\tau^{-1}.
\]

The involution \(J=R\tau\) fixes \(x\) and exchanges the two neighbors, so
\(C=\widetilde C/\langle J\rangle\) generically.  Full proof and certificate
details are in `NEIGHBOR_CORRESPONDENCE.md`.

## 4. Finite branch analysis

Exact elimination gives

\[
\operatorname{Disc}_xP=(4\sigma-9)^2Q_6(\sigma)^3,
\]

with

\[
Q_6=64\sigma^6-448\sigma^5+848\sigma^4+80\sigma^3
 -1048\sigma^2+152\sigma-151.
\]

The branch polynomial is irreducible and

\[
\operatorname{Disc}(Q_6)=2^{63}\cdot97.
\]

Modulo \(Q_6\), the last nonzero subresultant of \(P,P_x\) has degree three;
the degree-two, degree-one, and constant subresultants vanish.  Thus each
root of \(Q_6\) has three double roots of \(P\).  The resultant of \(P\) and
\(P_\sigma\) is coprime to \(Q_6\), so all 18 points are smooth.  In
characteristic zero they are tame ramification points of index two.

At the remaining finite discriminant value, put

\[
t=\sigma-\frac94,
\qquad y=x-\frac14.
\]

The quadratic tangent cone is

\[
-\frac18(y^2-10ty+137t^2),
\]

whose discriminant is \(-7t^2\).  It has two distinct nonvertical tangent
lines over \(\mathbb Q(\sqrt{-7})\), so this point is an ordinary node.  Both
normalization branches use \(t\) as a uniformizer and contribute no
ramification to \(C\to\mathbb P^1_\sigma\).

## 5. Infinity

Set \(t=1/\sigma\) and \(y=x/\sigma\).  The integral polynomial

\[
F(t,y)=t^7P(1/t,y/t)
\]

has special fibre

\[
F(0,y)=(y-1)^4(y+1)^3.
\]

Successive weighted initial forms are

\[
\begin{aligned}
y=1+z:&\quad 8z(t+z)^2(2t+z),\\
y=-1+z:&\quad16(z-2t)(z-t)^2,\\
y=1-t+w:&\quad-4t^2w(t^2+2w),\\
y=-1+t+w:&\quad-8t(t^2-2w)(t^2-w).
\end{aligned}
\]

One further linear initial equation separates the remaining \(w=0\) branch
above \(y=1\).  These charts give four branches above \(y=1\) and three above
\(y=-1\), all rational and unramified over the \(t\)-line.  The order of
\(\operatorname{Disc}_yF\) at \(t=0\) is 22.  Since the branches are
unramified, their total index/\(\delta\) contribution is 11.

## 6. Genus

The only ramification comes from the six roots of \(Q_6\), three simple
points above each root.  Riemann--Hurwitz gives

\[
2g(C)-2=7(-2)+18=4,
\qquad g(C)=3.
\]

The plane model is a septic of arithmetic genus 15.  Its finite node has
\(\delta=1\) and its infinity singularities have total \(\delta=11\), giving
the independent check \(15-1-11=3\).

## 7. Branch-corrected counts and candidate local numerators

For each screened prime and extension degree \(r\), let \(A_{p,r}\) be the
affine count of \(P=0\).  Applying the characteristic-zero branch ledger adds
seven rational branches at infinity, while the rational plane node is
replaced by two rational tangent directions when \(-7\) is a square and by
none when it is a nonsquare.  Define the branch-corrected count

\[
\widehat N_{p,r}=A_{p,r}+7+\epsilon_{p,r},
\qquad
\epsilon_{p,r}=\begin{cases}1&-7\text{ square},\\-1&-7\text{ nonsquare}.
\end{cases}
\]

With \(\widehat S_r=p^r+1-\widehat N_{p,r}\), Newton identities and a formal
genus-three reciprocal completion give the candidate

\[
\begin{aligned}
\widehat L_p(T)={}&1-\widehat S_1T+\frac{\widehat S_1^2-\widehat S_2}{2}T^2
-\frac{\widehat S_1^3-3\widehat S_1\widehat S_2+2\widehat S_3}{6}T^3\\
&+p\frac{\widehat S_1^2-\widehat S_2}{2}T^4-p^2\widehat S_1T^5+p^3T^6.
\end{aligned}
\]

The producer verifies the affine singular projection, squarefreeness of
\(Q_6\), and the displayed leading infinity coefficients at every recorded
prime.  These checks support, but do not prove, simultaneous normalization or
good reduction.  Accordingly \(\widehat L_p\) is not asserted to be a local
factor of the characteristic-zero curve.

## 8. Chronology and Route-A boundary

The oriented edge cover reconstructs the marked variables

\[
(a,x_0,\ldots,x_6),\qquad
x_{i+1}=a-x_i^2-x_{i-1},
\]

with time shift \(\tau x_i=x_{i+1}\).  For states indexed as
\((x_i,x_{i-1})\), the reversor acts on coordinate labels by
\(Rx_i=x_{-1-i}\), whereas the scalar deck involution
\(J=R\tau\) acts by \(Jx_i=x_{-i}\).  It obeys

\[
\tau^7=R^2=1,
\qquad R\tau R=\tau^{-1}.
\]

The scalar curve \(C\) keeps only \((\sigma,x)\) and does not carry \(\tau\),
but \(\widetilde C\) restores the missing neighbor choice and hence genuine
chronology.  The correct next arithmetic data are

\[
\#\operatorname{Fix}(\operatorname{Frob}_p^r\tau^s\mid\widetilde C),
\]

with \(r\), \(s\), and the fixed Hénon period \(n=7\) kept distinct.  No such
joint traces, cross-period determinant, Riemann divisor, or self-adjoint lift
are presently constructed.  The updated Route-A tuple is

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\]

with overall status `ROUTE_A_EXPLORATORY` and Route B closed.
