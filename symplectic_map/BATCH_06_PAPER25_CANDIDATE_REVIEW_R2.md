# Paper 25 Independent Candidate Review R2

## Review identity and method

- Candidate: `support_rank_sharp_unbounded_perron_v1`
- Working title: **Sharp Support-Rank Bounds and Unbounded Perron Degree in Hamiltonian Product Shears**
- Review date: 2026-08-25 UTC
- Review mode: mutually blind, offline, proof-first, and computation-free
- Inputs used: the frozen theorem package in the review instruction and the local scientific scope records of Papers 20--24
- External search: none
- CAS, numerical experiment, parameter scan, and finite-iterate evidence: none
- Project creation, manuscript, build, release, network, and external effect: none

This review treats every supplied formula as unproved. It independently derives
the support-rank factorization, parameter construction, selector cone, carry and
visibility induction, characteristic polynomial, finite-field irreducibility,
Perron degree, and minimal scalar recurrence. It assigns no global literature
priority because it is deliberately offline.

## Verdict and scores

The complete corrected theorem below is provable as stated once two pieces of
notation are made explicit:

1. a primitive element `c` means a generator of the full group
   \(\mathbb F_p^\times\), of order \(p-1\); and
2. the selector cone \(\mathcal K_R\) contains both a coordinate-ratio band
   and the weighted ordering \(a_1u_1<a_i u_i\).

These are clarifications required to state the supplied construction
unambiguously, not new hypotheses added to rescue a failed argument.

- Proof confidence: **9.6 / 10**
- Standalone mathematical value after subtracting Papers 22 and 23: **8.5 / 10**
- Internal portfolio separation: **PASS**
- External novelty score: **not assigned in this offline review**

The abstract kernel lemma alone is not a paper, and the cases \(d=3\) and
\(d=4\) remain occupied locally. The substantial new delta is the uniform
all-\(d\) sharp construction, unbounded algebraic degree, and exact
minimal-order visible recurrence.

## Corrected frozen theorem

Let \(K\) be a field of characteristic zero.

### Part I: support-rank factorization

Let

\[
 A=-I_n+\mathsf P\mathsf Q,
 \qquad
 B=-I_n+\mathsf R\mathsf S,
 \qquad
 C=BA,
\]

where the products are defined over \(K\), and put

\[
 r=\operatorname{rank}
 \begin{pmatrix}\mathsf Q\\ \mathsf S\end{pmatrix}.
\]

Then there is an explicit monic degree-\(r\) polynomial \(Q_r(t)\) such that

\[
 \boxed{\chi_C(t)=(t-1)^{n-r}Q_r(t).}
\]

This gives only a lower bound \(n-r\) for the algebraic multiplicity of the
unit eigenvalue. The factor \(Q_r\) is allowed to contain additional factors
of \(t-1\).

### Part II: sharp families in every degree

For every integer \(d\ge2\), choose the parameters in the following order.

1. Choose a prime \(p\equiv1\pmod d\).
2. Choose \(c\in\mathbb F_p^\times\) of order \(p-1\).
3. Choose ordered positive integer lifts
   \(a_1<\cdots<a_d\) of all the \(d\)-th roots of unity in
   \(\mathbb F_p\), with
   \[
   a_1+1>4d.
   \]
4. Put
   \[
   S_a=\sum_{i=1}^d a_i,
   \qquad M=a_d.
   \]
5. Choose an arbitrarily large integer \(b\ge2\) in the residue class
   \[
   bd\equiv1-(-1)^dc\pmod p
   \]
   such that, with
   \[
   R=1+\frac{2M}{bS_a},
   \]
   one has
   \[
   R^2<2
   \]
   and, for every \(i>1\),
   \[
   b(a_i-a_1)S_a>a_i^2R-a_1^2.
   \]

On \(\mathbb A_K^{2d}\), define

\[
 V(q)=\prod_{j=1}^d q_j^2+\sum_{i=1}^d q_i^{a_i+1},
 \qquad
 W(p)=\prod_{j=1}^d p_j^b,
\]

\[
 S_V(q,p)=(q,p+\nabla V(q)),
 \qquad
 T_W(q,p)=(q+\nabla W(p),p),
 \qquad
 F=T_W\circ S_V.
\]

Let \(\mathbf1\) denote the all-ones column vector, let
\(\mathbf a=(a_1,\ldots,a_d)^{\mathsf T}\), let
\(D=\operatorname{diag}(a_1,\ldots,a_d)\), and let
\(J=\mathbf1\mathbf1^{\mathsf T}\). Then the exact selected half-step and
complete-step matrices are

\[
 A=D,
 \qquad
 B=bJ-I_d,
 \qquad
 C=BA=b\mathbf1\mathbf a^{\mathsf T}-D.
\]

Define

\[
 \mathcal K_R=
 \left\{
 u\in\mathbb R_{>0}^d:
 \begin{array}{l}
 u_i\le u_1<Ru_i,\\[2pt]
 a_1u_1<a_i u_i
 \end{array}
 \text{ for every }i>1
 \right\}.
\]

The ordinary seed \(\mathbf1\) lies in \(\mathcal K_R\), the spike row is
strictly selected in every coordinate of \(\nabla V\), and

\[
 C\mathcal K_R\subset\mathcal K_R
\]

with both coordinate inequalities strict after one application. All carried
coordinates are strictly dominated, the selected leading forms remain
nonzero, every new \(q\)-coordinate strictly dominates every new
\(p\)-coordinate, and \(q_1\) strictly dominates the other \(q\)-coordinates
after every positive iterate. Consequently

\[
 \boxed{\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1\quad(n\ge0),}
\]

with strict \(q_1\)-visibility for \(n\ge1\), and

\[
 \lambda_1(F)=\rho(C).
\]

The characteristic polynomial is

\[
 \boxed{
 \chi_C(t)
 =t^d+\sum_{k=1}^d(1-bk)e_k(a_1,\ldots,a_d)t^{d-k}.}
\]

It is irreducible over \(\mathbb Q\). Hence \(\rho(C)\) is a Perron
algebraic integer of degree exactly \(d\), and the visible scalar degree
sequence has minimal constant-coefficient recurrence order exactly \(d\).

## Proof of Part I: explicit Sylvester factorization

Direct multiplication gives

\[
 C-I_n=-\mathsf P\mathsf Q-\mathsf R\mathsf S
       +\mathsf R\mathsf S\mathsf P\mathsf Q.
\]

Put

\[
 U=\begin{pmatrix}\mathsf P&\mathsf R\end{pmatrix},
 \qquad
 V_0=
 \begin{pmatrix}
 -\mathsf Q\\
 \mathsf S\mathsf P\mathsf Q-\mathsf S
 \end{pmatrix}.
\]

Then \(C=I_n+UV_0\). Every row of \(V_0\) lies in the row span of
\(\mathsf Q\) and \(\mathsf S\). Choose a full-row-rank matrix
\(L\in K^{r\times n}\) whose rows form a basis of that span. There is a
matrix \(E\) such that \(V_0=EL\). With \(X=UE\),

\[
 C=I_n+XL.
\]

The rectangular Sylvester determinant identity gives, with
\(z=t-1\),

\[
 \det(zI_n-XL)=z^{n-r}\det(zI_r-LX).
\]

Therefore

\[
 \chi_C(t)
 =(t-1)^{n-r}
 \det\bigl((t-1)I_r-LX\bigr).
\]

Thus one may take

\[
 Q_r(t)=\det\bigl((t-1)I_r-LX\bigr).
\]

It is monic of degree \(r\). Equivalently,
\(\ker\mathsf Q\cap\ker\mathsf S\) has dimension \(n-r\), and \(C\)
acts as the identity there. Neither argument excludes additional unit roots
inside \(Q_r\), so no exact unit multiplicity is claimed.

## Parameter existence and quantifier order

Dirichlet's theorem on primes in arithmetic progressions supplies a prime
\(p\equiv1\pmod d\). Hence \(d\mid p-1\), and \(\mathbb F_p^\times\)
contains exactly \(d\) distinct \(d\)-th roots of unity and a generator
\(c\).

There is no ordering on the finite field being used. Choose any enumeration
of the \(d\)-th roots. For the first root, add a sufficiently large multiple
of \(p\) to obtain a positive lift \(a_1\) with \(a_1+1>4d\). Recursively,
for each remaining root add a sufficiently large multiple of \(p\) to obtain
a lift larger than its predecessor. This produces legitimate ordered positive
lifts without changing any residue or elementary symmetric function modulo
\(p\).

Since \(p\nmid d\), the congruence for \(b\) specifies one residue class
modulo \(p\). It contains arbitrarily large positive integers. Along that
class,

\[
 R=1+\frac{2M}{bS_a}\longrightarrow1
\]

as \(b\to\infty\), so \(R^2<2\) eventually. For each fixed \(i>1\), the
left side of

\[
 b(a_i-a_1)S_a>a_i^2R-a_1^2
\]

grows linearly to infinity, whereas the right side converges to the fixed
number \(a_i^2-a_1^2\). There are only finitely many indices. One sufficiently
large \(b\) in the prescribed residue class satisfies every inequality
simultaneously. This proves existence in the required order

\[
 d\ \longrightarrow\ p,c\ \longrightarrow\ a_i\ \longrightarrow\ b,R.
\]

## Symplecticity and literal selected matrices

The two shears are polynomial automorphisms, with inverses obtained by
subtracting the same gradients. Their off-diagonal Jacobian blocks are the
symmetric Hessians of \(V\) and \(W\), so both preserve the standard
symplectic form.

For a positive \(q\)-degree vector \(u\), the product term in the
\(i\)-th component of \(\nabla V\) has weighted degree

\[
 2\sum_{j=1}^d u_j-u_i,
\]

whereas the pure spike has degree \(a_i u_i\). When the spikes are selected,
the half-step degree vector is

\[
 v=Du.
\]

The \(i\)-th derivative of \(W\) has exponent row

\[
 (b,\ldots,b)-e_i,
\]

so its degree is

\[
 (bJ-I_d)v.
\]

Thus the matrices are read from the literal gradient supports:

\[
 A=D,
 \qquad B=bJ-I_d,
 \qquad C=(bJ-I_d)D=b\mathbf1\mathbf a^{\mathsf T}-D.
\]

They are not free matrices inserted after the fact.

## Strict spike selection on \(\mathcal K_R\)

Let \(u\in\mathcal K_R\), write \(s=u_1\), and put
\(U=\sum_j u_j\). Then

\[
 u_j\le s,
 \qquad U\le ds,
 \qquad u_i>\frac{s}{R}\quad(i>1).
\]

For \(i=1\),

\[
 (a_1+1)u_1>4ds>2U.
\]

For \(i>1\), since \(R^2<2\) implies \(R<2\),

\[
 (a_i+1)u_i
 >(a_1+1)\frac{s}{R}
 >2ds
 \ge2U.
\]

Hence, for every \(i\),

\[
 a_i u_i>2U-u_i.
\]

All \(d\) spike rows are therefore strictly and simultaneously selected.

## Exact invariance of \(\mathcal K_R\)

Let

\[
 T=b\mathbf a^{\mathsf T}u,
 \qquad w=Cu,
 \qquad w_i=T-a_i u_i.
\]

All \(w_i\) are positive. For every \(i>1\), the weighted ordering in
\(\mathcal K_R\) gives

\[
 w_1-w_i=a_i u_i-a_1u_1>0.
\]

Thus \(w_i<w_1\). To prove the upper ratio wall, note that

\[
 \mathbf a^{\mathsf T}u>\frac{S_a}{R}s,
 \qquad a_i u_i\le Ms.
\]

Consequently

\[
\begin{aligned}
 Rw_i-w_1
 &=(R-1)T-Ra_i u_i+a_1s\\
 &>\left(\frac{2M}{R}-RM+a_1\right)s\\
 &=\left(M\frac{2-R^2}{R}+a_1\right)s>0.
\end{aligned}
\]

Hence \(w_1<Rw_i\).

Finally,

\[
 a_iw_i-a_1w_1
 =(a_i-a_1)T-a_i^2u_i+a_1^2s.
\]

Using the strict lower bound for \(T\), the upper bound \(u_i\le s\), and
the defining parameter inequality gives

\[
\begin{aligned}
 a_iw_i-a_1w_1
 &>\left(
 \frac{b(a_i-a_1)S_a}{R}-a_i^2+a_1^2
 \right)s\\
 &>a_1^2\left(1-\frac1R\right)s>0.
\end{aligned}
\]

Therefore \(w\in\mathcal K_R\), with strict coordinate ordering after the
first complete step. The ordinary seed belongs to the cone because its
coordinates are equal, \(R>1\), and \(a_1<a_i\) for \(i>1\).

## Carry, leading forms, and visibility

The matrix \(C\) is strictly positive:

\[
 C_{ii}=(b-1)a_i>0,
 \qquad C_{ij}=ba_j>0\quad(i\ne j).
\]

Moreover,

\[
 (Cu)_i
 =(b-1)a_i u_i+b\sum_{j\ne i}a_j u_j>u_i.
\]

Thus \(u_{n+1}>u_n\) componentwise. At every later \(V\)-phase, the fresh
spike degree \(a_i u_{n,i}\) strictly beats the carried momentum degree
\(a_i u_{n-1,i}\). At every \(W\)-phase, the fresh degree
\((Cu_n)_i\) strictly beats the carried position degree \(u_{n,i}\).
The first step is also strict because every \(a_i>1\).

The selector inequalities leave one highest-degree source in each coordinate.
The top forms are nonzero powers and products in a polynomial domain, and all
integer derivative coefficients remain nonzero in characteristic zero. Hence
no selected leading form can disappear.

It remains to compare the two phases globally. If \(v=Du\), then

\[
 v_j=a_j u_j\le Ms.
\]

For every \(i\),

\[
 w_i>\left(\frac{bS_a}{R}-M\right)s.
\]

Since \(R-1=2M/(bS_a)\),

\[
 \frac{bS_a}{R}-M
 =M\left(\frac{2}{R(R-1)}-1\right).
\]

The inequality \(R^2<2\) implies

\[
 R(R-1)=R^2-R<2-R<1,
\]

and therefore

\[
 \frac{bS_a}{R}-M>M.
\]

Thus every new \(q\)-coordinate has degree strictly greater than every new
\(p\)-coordinate. Within the \(q\)-block,

\[
 w_1-w_i=a_i u_i-a_1u_1>0\quad(i>1).
\]

Therefore \(q_1\) is the unique total-degree coordinate for every positive
iterate. Induction from \(u_0=\mathbf1\) gives

\[
 u_n=C^n\mathbf1,
 \qquad
 \deg(F^n)=e_1^{\mathsf T}C^n\mathbf1.
\]

Perron--Frobenius applied to the strictly positive matrix \(C\) then gives

\[
 \lambda_1(F)=\rho(C).
\]

## Characteristic polynomial

The matrix determinant lemma gives

\[
\begin{aligned}
 \chi_C(t)
 &=\det(tI_d+D-b\mathbf1\mathbf a^{\mathsf T})\\
 &=\prod_{i=1}^d(t+a_i)
   -b\sum_{i=1}^d a_i\prod_{j\ne i}(t+a_j).
\end{aligned}
\]

In the second sum, a product contributing to the elementary symmetric
function \(e_k(a_1,\ldots,a_d)\) is counted exactly \(k\) times. Hence

\[
 \chi_C(t)
 =t^d+\sum_{k=1}^d(1-bk)e_k(a_1,\ldots,a_d)t^{d-k}.
\]

## Reduction modulo \(p\) and the exact binomial criterion

Modulo \(p\), the residues of the \(a_i\) are precisely the roots of
\(t^d-1\). Therefore

\[
 e_k(a_1,\ldots,a_d)\equiv0\pmod p
 \quad(1\le k<d),
\]

and

\[
 e_d(a_1,\ldots,a_d)\equiv(-1)^{d+1}\pmod p.
\]

The congruence for \(b\) gives

\[
 1-bd\equiv(-1)^dc\pmod p.
\]

Thus

\[
 \boxed{\chi_C(t)\equiv t^d-c\pmod p.}
\]

For completeness, the finite-field binomial irreducibility criterion says
that \(t^d-c\in\mathbb F_p[t]\) is irreducible if and only if:

1. every prime divisor of \(d\) divides \(\operatorname{ord}(c)\);
2. \(\gcd\bigl(d,(p-1)/\operatorname{ord}(c)\bigr)=1\); and
3. if \(4\mid d\), then \(p\equiv1\pmod4\).

Here \(\operatorname{ord}(c)=p-1\). The first condition holds because
\(d\mid p-1\); the second becomes \(\gcd(d,1)=1\); and the third follows
from \(p\equiv1\pmod d\). This includes the two delicate boundaries:

- when \(d=2\), a generator of \(\mathbb F_p^\times\) is a nonsquare, so
  \(t^2-c\) is irreducible;
- when \(4\mid d\), the separate \(p\equiv1\pmod4\) requirement is
  genuinely used and is automatically satisfied.

Therefore the reduction is irreducible. Since \(\chi_C\) is monic with
integer coefficients, Gauss's lemma and reduction modulo \(p\) show that
\(\chi_C\) is irreducible over \(\mathbb Q\).

## Exact Perron degree and exact minimal recurrence order

The matrix \(C\) is a strictly positive integer matrix, so its spectral radius
is a simple positive eigenvalue strictly larger in modulus than every other
eigenvalue. The irreducible polynomial \(\chi_C\) is its minimal polynomial.
Consequently \(\rho(C)\) is a Perron algebraic integer, and all of its
conjugates are the remaining roots of \(\chi_C\). Its algebraic degree is
exactly \(d\).

It does not follow from Cayley--Hamilton alone that the visible scalar sequence
has minimal order \(d\); reachability and observability must also be checked.
Because \(\chi_C\) is irreducible of degree \(d=\dim\mathbb Q^d\), the algebra
\(\mathbb Q[C]\) is a degree-\(d\) field and \(\mathbb Q^d\) is
one-dimensional over it. Every nonzero vector is therefore cyclic for \(C\),
and every nonzero covector is cyclic for \(C^{\mathsf T}\). In particular,

\[
 \mathbf1,C\mathbf1,\ldots,C^{d-1}\mathbf1
\]

is a basis, and

\[
 e_1,C^{\mathsf T}e_1,\ldots,(C^{\mathsf T})^{d-1}e_1
\]

is a basis of the dual space. The corresponding \(d\times d\) reachability
and observability matrices are invertible, so their product, the Hankel matrix

\[
 \bigl(e_1^{\mathsf T}C^{i+j}\mathbf1\bigr)_{0\le i,j<d},
\]

has rank \(d\). A scalar sequence satisfying a recurrence of order less than
\(d\) has Hankel rank less than \(d\). Hence the exact visible degree sequence
has no shorter constant-coefficient recurrence. Its minimal order is exactly
\(d\), over \(\mathbb Q\) and after any characteristic-zero scalar extension.

## Internal portfolio subtraction and standalone assessment

Paper 20 owns one two-mode stationary degree matrix and a quadratic Perron
formula. Paper 21 owns one three-mode stationary matrix and selected cubic
Perron subfamilies. Paper 22 owns the arbitrary-mode endpoint-spiked family in
which a rank-three profile forces cubic spectral collapse. Paper 23 owns one
four-mode full-profile family and an infinite quartic Perron subfamily; it also
records the common-kernel observation as explanatory, nonheadline
infrastructure.

Accordingly, none of the following can count as Paper 25 novelty:

- the general kernel lemma by itself;
- the cases \(d=2,3,4\) by themselves;
- Perron--Frobenius, Cayley--Hamilton, Sylvester's identity, or the binomial
  irreducibility criterion;
- another isolated five-mode matrix.

The surviving package is materially larger. It proves a support-rank upper
law, constructs a sharp Hamiltonian gradient-compatible family for every
\(d\), proves a strict ordinary-degree cone and complete carry/visibility
induction uniformly in \(d\), establishes irreducibility in every degree, and
shows that the actually visible scalar recurrence has exact unbounded minimal
order. That remains a credible proof-first article after the Paper 22 and
Paper 23 examples are removed rather than republished.

## Mandatory limitations

The candidate does not claim:

1. novelty from \(d=5\) alone;
2. novelty of the general support-kernel lemma alone;
3. realization of every Perron or weak-Perron number;
4. minimal ambient dimension or optimal support sparsity;
5. a forward-versus-inverse theorem;
6. higher dynamical degrees or a compactification theorem;
7. topological, metric, or arithmetic entropy equality;
8. arbitrary signs or coefficient specializations;
9. arbitrary Newton supports, exponent profiles, or shear words;
10. positive-characteristic validity;
11. a classification of selector cones or polynomial symplectomorphisms;
12. exact unit multiplicity in the general rank lemma;
13. a new Paper 22 cubic-collapse result;
14. a new Paper 23 quartic-family result; or
15. absolute external priority from this offline review.

## Final finding

No missing \(d\)-boundary, parameter-order failure, selector tie, carry gap,
visibility gap, modular-irreducibility exception, or scalar-recurrence gap
remains in the corrected frozen theorem. The all-degree sharpness and
unbounded visible Perron complexity pass the proof, standalone, and internal
portfolio gates.

PAPER25_CANDIDATE_GATE_PASS_R2
