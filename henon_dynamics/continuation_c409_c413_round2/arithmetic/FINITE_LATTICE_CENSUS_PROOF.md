# Finite-lattice orbit census: two-period recovery and complete local-conjugacy fibres

Status: author proof for independent review; not an admitted fifth result and not a
priority claim. The ownership audit is separate, with a material older-source
gate explicitly retained below. Scope is exclusively hyperbolic matrices in
`SL(2,Z)` and ordinary fixed-point cardinalities on labelled finite lattices.

## 1. Native object and statements

For an integer matrix (M), let (c(M)) be the positive gcd of its entries when
(M\ne0). Let

\[
 A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z),
 \qquad t=\operatorname{tr}A,\quad |t|>2.
\]

The observation is the labelled array

\[
 F_A(q,n)=\#\ker\bigl(A^n-I:(\mathbb Z/q\mathbb Z)^2
                  \longrightarrow(\mathbb Z/q\mathbb Z)^2\bigr),
 \qquad q,n\ge1.                                                   \tag{1}
\]

Here (n) is ordinary forward iteration time; (q) is the lattice modulus, not
a second dynamical time, a prime label, or a fitted spectral parameter. Set

\[
 k=c(A-I),\qquad h=c(2A-tI),\qquad g=\gcd(b,c,d-a).
\]

All three gcds are nonzero under the hyperbolicity assumption.

**Theorem A (complete observation invariant).** For any two such matrices (A,B),
the following statements are equivalent:

1. (F_A(q,n)=F_B(q,n)) for every (q,n\ge1).
2. (F_A(q,j)=F_B(q,j)) for every (q\ge1) and (j\in\{1,2\}).
3. Their pairs ((t,h)) agree.

When the signed trace is already fixed, the (n=2) row alone suffices.
No assertion of a uniform finite modulus cutoff is included.

**Theorem B (all admissible invariants and all fibres).** Quotient the matrices
in Theorem A by conjugacy in (\mathrm{GL}_2(\widehat{\mathbb Z})), where
(\widehat{\mathbb Z}=\prod_p\mathbb Z_p). The map from this quotient to the
ordinary census (1) has the following complete fibres.

* For odd (t), its possible labels are precisely the positive odd integers
  (h) with (h^2\mid t^2-4). Each fibre contains one local-conjugacy class,
  having (g=h).
* For even (t=2T), its possible labels are precisely (h=2r), where (r>0)
  and (r^2\mid T^2-1). Put (D=(T^2-1)/r^2). Each fibre contains a class with
  (g=r). It contains one additional class, with (g=2r), if and only if
  (D\equiv1\pmod4). There are no further classes.

The two-class case is an exactly classified loss of one 2-adic content bit.
It does not assert that a fibre contains only two integral-conjugacy classes.

**Corollary C (smallest trace and infinite occurrence).** The smallest possible
absolute trace of a two-class fibre is (18). In particular

\[
 A=\begin{pmatrix}1&4\\4&17\end{pmatrix},\qquad
 B=\begin{pmatrix}5&8\\8&13\end{pmatrix}                           \tag{2}
\]

have identical observations (1) for every (q,n), but are not conjugate even
modulo (8). Two-class fibres occur for infinitely many positive traces.

These theorems say nothing about Riemann zeros, an Euler product over rational
primes, a target functional equation, or a Hilbert--Pólya operator.

## 2. Dependencies and proof order

The proof uses elementary Smith normal form, Cayley--Hamilton, and one explicitly
attributed classification theorem:

> For integer (2\times2) matrices, equality of trace, determinant, and matrix
> gcd is equivalent to conjugacy over every finite quotient, and to conjugacy
> over (\widehat{\mathbb Z}).

This is Baake--Roberts--Weiss (2008), Theorem 2 and Corollary 4, not a theorem
claimed here. See the [original author-hosted published paper](https://web.maths.unsw.edu.au/~jagr/BRW08.pdf).

Proof order: Smith reconstruction → odd/even matrix identities → reduction of
(k) to ((t,h)) → Theorem A → admissibility and explicit representatives →
the attributed conjugacy theorem → minimality and infinite family. There is no
use of finite sampling to establish any universal quantifier.

## 3. Smith data and recovery from all moduli

If (M\in M_2(\mathbb Z)) has nonzero determinant, write its positive Smith
invariants as (s_1\mid s_2). Then

\[
 s_1=c(M),\qquad s_2=|\det M|/s_1,\qquad
 \#\ker(M\bmod q)=\gcd(q,s_1)\gcd(q,s_2).                         \tag{3}
\]

Indeed the unimodular matrices in a Smith reduction remain invertible modulo
every (q), and the scalar congruence (sx=0\pmod q) has exactly
(\gcd(q,s)) solutions.

Conversely the kernel cardinalities for every (q) determine (s_1,s_2).
For a fixed prime (p), put (\alpha_i=v_p(s_i)), and let

\[
 e_j=\log_p\#\ker(M\bmod p^j)
     =\min(j,\alpha_1)+\min(j,\alpha_2),\qquad e_0=0.
\]

Then (e_j-e_{j-1}=\#\{i:\alpha_i\ge j\}). This recovers the two ordered
exponents, including any zero exponents. Applying this to every prime recovers
the positive integers (s_i). Also

\[
 \max_{q\ge1}\#\ker(M\bmod q)=s_1s_2=|\det M|,                   \tag{4}
\]

with equality for any multiple of (s_2). Equation (4) is an inference from the
specified array, not a replacement of it by unlabelled toral counts.

This cardinality-to-group reconstruction is classical: BRW Proposition 3 and
Neumärker (2012), Proposition 3.3.3, already describe it. It is included here to
make the precise observation loss explicit.

## 4. Two identities controlling all periods

Define integers (u_0=0,u_1=1), and

\[
 u_{m+1}=t u_m-u_{m-1}\quad(m\ge1).
\]

Cayley--Hamilton gives (A^{-1}=tI-A) and

\[
 A^m=u_mA-u_{m-1}I\quad(m\ge1).                                  \tag{5}
\]

For every (m\ge0), respectively (m\ge1), one has

\[
 A^{2m+1}-I=(u_{m+1}+u_m)A^m(A-I),                               \tag{6}
\]
\[
 A^{2m}-I=u_mA^m(2A-tI).                                         \tag{7}
\]

Here is a direct verification valid also for negative traces. The distinct roots
of (X^2-tX+1) are (\lambda,\lambda^{-1}), with (\lambda\ne\pm1), and

\[
 u_m=\frac{\lambda^m-\lambda^{-m}}{\lambda-\lambda^{-1}}.
\]

Thus the right side of (7), on a (\lambda)-eigenvector, is
(u_m\lambda^m(\lambda-\lambda^{-1})=\lambda^{2m}-1).
For (6),

\[
 (u_{m+1}+u_m)\lambda^m(\lambda-1)
 =\frac{(\lambda^{m+1}+\lambda^m-\lambda^{-m-1}-\lambda^{-m})
         \lambda^m(\lambda-1)}{\lambda-\lambda^{-1}}
 =\lambda^{2m+1}-1.
\]

The same identities hold on the other eigenvector; diagonalizability proves
the matrix equalities. At (m=0), (6) also directly reads (A-I=A-I).

Multiplication on the left or right by an integral unimodular matrix preserves
content: one divisibility follows from integral linear combinations of entries,
and the other follows using its integral inverse. Therefore, if
(s_1(n),s_2(n)) are the Smith invariants of (A^n-I), then

\[
 s_1(2m+1)=k\,|u_{m+1}+u_m|,\qquad
 s_1(2m)=h\,|u_m|,                                                \tag{8}
\]
\[
 s_2(n)=\frac{|2-\operatorname{tr}(A^n)|}{s_1(n)}.                 \tag{9}
\]

The scalar factors in (8) are nonzero because no eigenvalue of (A) is a root
of unity. In particular (s_1(1)=k), (s_1(2)=h).

For implementation, the traces (v_n=\operatorname{tr}(A^n)) satisfy
(v_0=2,v_1=t,v_{n+1}=t v_n-v_{n-1}). Equations (3), (8), (9) compute the
whole array from ((t,k,h)) using only exact integer arithmetic.

## 5. The apparent third invariant is redundant

For every (A),

\[
 k=\gcd(a-1,g).                                                   \tag{10}
\]

This follows by replacing the pair (a-1,d-1) by (a-1,d-a) in the gcd.

### 5.1 Odd signed trace

If (t) is odd, (d-a) is odd, so (g) is odd. The formula

\[
 h=\gcd(2b,2c,a-d)
\]

then gives (h=g). Since (2a\equiv t\pmod g), and multiplication by (2)
is invertible modulo every divisor of the odd number (g), (10) yields

\[
 k=\gcd(h,t-2).                                                   \tag{11}
\]

All gcds use absolute values of their integer arguments when needed.

### 5.2 Even signed trace

Let (t=2T), and write

\[
 A=TI+rN,\qquad
 N=\begin{pmatrix}x&y\\z&-x\end{pmatrix},\qquad
 \gcd(x,y,z)=1,\qquad r=c(A-TI)>0.
\]

Then

\[
 h=2r,\qquad x^2+yz=D:=\frac{T^2-1}{r^2}\in\mathbb Z_{>0},\qquad
 g=r\gcd(y,z,2x)\in\{r,2r\}.                                   \tag{12}
\]

The final inclusion follows because a common odd prime factor, or an additional
factor (4), in the normalized gcd would contradict primitivity. More directly,
(\gcd(y,z,2x)) divides (2\gcd(y,z,x)=2).

If (g=r), (10) immediately gives (k=\gcd(T-1,r)).
If (g=2r), necessarily (x) is odd and (y,z) are even. Consequently

\[
 D\equiv1\pmod4,\qquad k=\gcd(T-1+r,2r).                         \tag{13}
\]

We show that the last gcd still equals (\gcd(T-1,r)). First (r) cannot be
odd: if it were, reducing (r^2D=T^2-1) modulo (4) would give respectively
(1\equiv3) or (1\equiv0), according as (T) is even or odd. Thus (r) is
even and (T) is odd. Set

\[
 e=v_2(r),\qquad f=v_2(T-1),\qquad \ell=v_2(T+1).
\]

All are finite since (|T|>1). Since (D) is odd,

\[
 2e=f+\ell,\qquad \min(f,\ell)=1,\qquad \max(f,\ell)\ge2.
\]

It follows that (e\ne f): otherwise (f=\ell=e), contradicting the last
two conditions. Therefore

\[
 v_2(T-1+r)=\min(f,e),
\]

and both gcds in question have 2-adic valuation (\min(f,e)). At every odd
prime their valuations agree simply by reducing (T-1+r) modulo (r). Thus
for both possibilities in (12),

\[
 k=\gcd(T-1,r)=\gcd(t/2-1,h/2).                                  \tag{14}
\]

This proves that ((t,h)) determines (k), for both signs and parities of (t).

## 6. Proof of Theorem A

Statement 1 implies 2 trivially. Under statement 2, apply (4) to periods (1,2)
to recover

\[
 D_1=|2-t|,\qquad D_2=t^2-4.
\]

The second number determines (|t|=\sqrt{D_2+4}). The first distinguishes its
sign: it equals (|t|-2) for positive (t), and (|t|+2) for negative (t).
The two numbers are different. Smith reconstruction at period (2) recovers
(h=s_1(2)). Hence statement 3 follows.

Conversely statement 3, (11) or (14), and (8)--(9) imply equality of the Smith
invariants of (A^n-I,B^n-I) at every period. Formula (3) then proves statement
1. With the signed trace fixed, only the (n=2) Smith reconstruction is needed.

## 7. Proof of Theorem B, including realization

For odd (t), necessity of odd (h) was proved above. Since every entry of
(2A-tI) is divisible by (h),

\[
 h^2\mid |\det(2A-tI)|=t^2-4.
\]

Conversely let (h>0) be odd with (h^2\mid t^2-4), and put
(E=(t^2-4)/h^2). We have (E\equiv1\pmod4). The integer matrix

\[
 A_{t,h}=\begin{pmatrix}
 (t+h)/2 & h\\
 h(E-1)/4 & (t-h)/2
 \end{pmatrix}                                                   \tag{15}
\]

has determinant (1), trace (t), (g=h), and centered content (h).
The attributed BRW theorem shows that this is exactly one local-conjugacy class
for each label. It also shows that distinct (h)'s cannot represent the same class.

For even (t=2T), necessity of (h=2r), (r^2\mid T^2-1), and
(g\in\{r,2r\}) follows from (12). For every such (r), the matrix

\[
 A_0(T,r)=\begin{pmatrix}T&r\\rD&T\end{pmatrix},\qquad
 D=(T^2-1)/r^2,                                                   \tag{16}
\]

has determinant (1), trace (2T), centered content (2r), and (g=r).
The possibility (g=2r) requires (D\equiv1\pmod4), as shown in (13).
Under exactly this condition the matrix

\[
 A_1(T,r)=\begin{pmatrix}T+r&2r\\r(D-1)/2&T-r\end{pmatrix}        \tag{17}
\]

is integral and has determinant (T^2-r^2-r^2(D-1)=1). Its normalized centered
matrix has (x=1,y=2,z=(D-1)/2\in2\mathbb Z), so its centered content is
(2r) and (g=2r). These two distinct values of (g) give two distinct
local-conjugacy classes by BRW, while each possible value gives only one such
class. Theorem A says that both classes have the same census.

This proves every necessity, sufficiency, existence and uniqueness assertion in
Theorem B. No assumption concerning fundamental discriminants or class numbers
was made.

## 8. Proof of Corollary C

In the two-class case the valuation argument above gives (e\ge2), hence
(r\ge4). Thus (|T|\ge5). For (5\le |T|<9), even (T) cannot occur.
For (|T|=5), (T^2-1=24) has no square divisor (r^2) with (4\mid r).
For (|T|=7), the only possibility is (r=4), giving (D=48/16=3\not\equiv1
\pmod4). At (|T|=9,r=4), (D=5\equiv1\pmod4). Therefore the minimum
absolute trace is (2|T|=18).

The matrices (2) have ((t,k,h)=(18,4,8)), but (g(A)=4,g(B)=8). More
elementarily (B\equiv5I\pmod8), while (A\bmod8) is not scalar. A scalar
matrix is fixed by every conjugation, so they are not conjugate modulo (8).
Their all-modulus, all-period census equality follows from Theorem A.

For every integer (j\ge0), choose (T=32j+9,r=4). Then

\[
 D=(T^2-1)/16=64j^2+36j+5\equiv1\pmod4.
\]

Equations (16)--(17) give two-class fibres of trace (64j+18), proving infinite
occurrence without a density claim.

## 9. What is and is not recovered

For each fixed modulus (q), the map is a permutation, and Möbius inversion
recovers the number of its (n)-cycles from (F_A(q,n)). Thus the theorem is
equivalently about the ordinary finite-lattice Artin--Mazur zeta functions

\[
 \zeta_{A,q}(z)=\exp\left(\sum_{n\ge1}F_A(q,n)z^n/n\right).
\]

At a fixed (q), (\zeta_{A,q}^{-1}=\det(I-zP_{A,q})) for the permutation
matrix on the finite set. This finite determinant is not a quantization of the
real toral map and is not a target Riemann determinant.

Equal census means isomorphic permutations at each labelled modulus, and
isomorphic abelian groups of toral periodic points at each period. It does not
imply additive (equivalently, linear over the finite base ring) conjugacies,
compatible additive conjugacies across moduli, or isomorphism of the periodic
groups as modules carrying the action of (A). No claim is made here that
arbitrary nonlinear compatible conjugacies cannot exist.

For completeness, in a two-class case choose a modulus (q) at which the
matrices are not linearly conjugate, and take (n) divisible by their two
orders modulo (q). The (q)-torsion subgroup of each toral period-(n) group
is then the whole lattice ((\mathbb Z/q\mathbb Z)^2). An action-preserving
group isomorphism of those period groups would restrict to an additive
conjugacy of the lattices. Every such additive isomorphism is represented
by a matrix in (\mathrm{GL}_2(\mathbb Z/q\mathbb Z)), a contradiction.
Thus census equivalence is strictly weaker than strong principal
Bowen--Franks equivalence in these cases. Also (A^{-1}) has the same
(t,h,g) as (A); inversion alone stays in one BRW local-conjugacy class
and is not the collision proved here.

## 10. Ownership gate still open

The elementary forward recurrence, Smith machinery, and the local-conjugacy
classification must be credited to their established literature. The potential
post-classical claim is the exact forgetful quotient: equality of the whole
ordinary ((q,n))-census iff ((t,h)) agrees, and the complete two-class fibre
criterion with realization. Its proof above is not evidence of publication priority.

Most importantly, Rodrigues--Sousa Ramos,
[arXiv:math/0303185](https://arxiv.org/abs/math/0303185), explicitly point to
earlier two-dimensional Bowen--Franks recurrences in Rodrigues's 1996 MSc thesis
and their 1999 Grazer Mathematische Berichte paper. Those older exact sources
must be checked before an independent-new-result recommendation. The 2022
[principal Bowen--Franks module paper](https://arxiv.org/abs/2207.00922) retains
the action, unlike (1), but this difference alone does not clear the older gate.

No C-number, manuscript slot, formal Route-A score or frozen prior result is
modified by this author proof.
