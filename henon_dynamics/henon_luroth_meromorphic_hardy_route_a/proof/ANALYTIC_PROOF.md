# C392 analytic proof: a meromorphic operator with determinant-invisible poles

## 1. Source, Hilbert space and endpoint boundary

For n>=1 let a_n=1/[n(n+1)], b_n=1/(n+1), h_n(z)=b_n+a_n z.
The real map is T(x)=n(n+1)x-n on (1/(n+1),1/n], with T(0)=0.
Its source clock is one map step. The operator below codes the positive
branch component only; the isolated fixed point 0 has no branch derivative
weight and is not silently included. C241 already proves the coded periodic
point/primitive necklace theorem; here it also follows directly by contraction:
each word h_w has slope a_w in (0,1), fixed point b_w/(1-a_w)>0,
and its positive branch itinerary is that word. Equality at a right endpoint
is handled by the stated half-open interval; left endpoints are excluded.

Put H=H²(D_2), with orthonormal basis e_j(z)=(z/2)^j, j>=0.
For Re s>1/2 define L_s f=sum_n a_n^s f(h_n), with real log a_n.
The weight is the inverse derivative to power s, not a fitted arithmetic label.

## 2. Trace class, full spectrum and quantitative finite sections

For |z|<=2, |h_n(z)|/2<=(n+2)/[2n(n+1)]<=3/4.
Writing f=sum_j <f,e_j>e_j, composition by h_n is a sum of rank-one
operators with trace norms at most (3/4)^j. Hence
||C_hn||_1<=4 and ||L_s||_1<=4 A(Re s), where A(v)=sum_n a_n^v.
Uniform convergence on compact subsets of Re s>1/2, also after s derivatives,
proves a trace-class holomorphic family. If P_J projects onto j<J, then
||L_s-L_s P_J||_1<=4 A(Re s)(3/4)^J.
The range of L_s P_J is contained in P_J H, since every h_n is affine.
In the polynomial basis its diagonal is lambda_j(s)=A(s+j).
Thus trace-norm convergence and continuity of the Fredholm determinant give
D(u,s)=det(I-uL_s)=product_(j>=0)(1-u A(s+j)).
All nonzero spectral values are precisely the nonzero A(s+j), with algebraic
multiplicity counted by occurrences in the product. No complex-parameter
simplicity or absence of Jordan chains is assumed. Zero belongs to the
spectrum by compactness on the infinite-dimensional H.

The bound |A(s+j)|<=A(Re s)2^-j gives local uniform convergence in u, and
|product_(j>=J)(1-u A(s+j))-1|
<=exp(2^(1-J)|u| A(Re s))-1.
For real s>1/2 these eigenvalues are strictly decreasing and positive, since
0<a_n<1. They are simple. Polynomial eigenvectors exist recursively from
the triangular matrix; no claim of an orthonormal or Riesz eigenbasis follows.

## 3. Periodic trace and two distinct products

For each word w of length r, C_hw is trace class with trace 1/(1-a_w),
by its triangular diagonal a_w^j. Absolute trace-norm summability permits
multiplication and trace interchange:
tr L_s^r=sum_w a_w^s/(1-a_w)=sum_(j>=0) A(s+j)^r.
Therefore, when Re s>1/2 and |u| A(Re s)<1,
D(u,s)=product_(primitive positive cycles gamma) product_(j>=0)
[1-u^length(gamma) a_gamma^(s+j)].
This is the stability product with the flat trace denominator, not C241's
unstabilized scalar word product. The latter is exactly
Z_word(u,s)=1/[1-uA(s)]=D(u,s+1)/D(u,s).
Reversal of a word preserves a_gamma because multiplication commutes,
but generally changes its coded point; repetitions have slope a_gamma^r.
All identities have absolute convergence in the displayed domain.
A meromorphic continuation is not an assertion of convergence of these products
outside that domain. The isolated source point 0 is not part of either product.

## 4. Entire-plane scalar continuation

Let t_n=(n+1/2)^-1. Then a_n=t_n²/(1-t_n²/4).
The absolutely convergent binomial expansion gives, initially for Re s>1/2,
A(s)=sum_(r>=0) (s)_r/(4^r r!) zeta(2s+2r,3/2).
Here zeta(v,b) is Hurwitz zeta and (s)_r is a rising factorial.
On any compact s set the r-th term is bounded by a polynomial in r times
9^-r for large r: the rising-factorial quotient grows only polynomially,
and the absolutely convergent Hurwitz series starts at b=3/2.
Thus this identity continues A meromorphically throughout C.

Only s_m=1/2-m, m>=0, are poles. Exactly one term r=m is singular at s_m;
its nonzero residue is
r_m=(1/2-m)_m/(2*4^m*m!)=(-1)^m binom(2m,m)/(2*16^m).
The factor 1/2 is the chain rule for the Hurwitz pole at 1.
At nonpositive integers the apparent rising-factorial zero/pole cancellations
must be evaluated by limits, not by substituting each factor separately.
This scalar formula imports only the classical Hurwitz continuation theorem.

## 5. Operator continuation and finite-rank residues

For |t|<=1/3 define
h_t(z)=[t+(z-1/2)t²]/(1-t²/4),
E_s(t)f(z)=(1-t²/4)^(-s) f(h_t(z)).
For |z|<=2, |h_t(z)|<=22/35<2.
The rank-one expansion from section 2 proves E_s(t) is jointly holomorphic
with values in trace-class operators in a neighborhood of |t|<=1/3.
Use the analytic logarithm of 1-t²/4 equal to zero at t=0.
Let E_s(t)=sum_(l>=0) E_l(s)t^l. Cauchy estimates give, locally uniformly in s,
||E_l(s)||_1<=M_K 3^l.
For n>=4, t_n<=2/9, and
L_s=sum_(n=1)^3 a_n^s C_hn
    +sum_(l>=0) E_l(s) zeta(2s+l,9/2).
For large l the last zeta is O_K((9/2)^(-l)); hence the trace-class
series converges normally with geometric ratio 2/3 away from its displayed
poles. Equality on Re s>1/2 proves a unique meromorphic continuation on C.

The coefficient of input monomial z^j is
E_l(s)z^j=[t^(l-j)] (1+(z-1/2)t)^j (1-t²/4)^(-s-j);
it vanishes for j>l and has degree at most floor(l/2).
Consequently the residue at s=(1-l)/2 is R_l=E_l((1-l)/2)/2,
with range in polynomials of degree <=floor(l/2), using only input derivatives
through order l. The formula is also a constructive exact finite matrix.

If l=2m, the restriction to degree<=m is triangular. Its j-th diagonal is
r_(m-j), j=0,...,m, all nonzero. Thus rank R_2m=m+1.
If l=2m+1, s=-m: for j<=m,
t^j(1+(z-1/2)t)^j(1-t²/4)^(m-j) has degree at most 2m,
so R_(2m+1) annihilates every polynomial of degree<=m.
Its range lies in that same space, hence R_(2m+1)^2=0.
For input degrees j=m+1,...,2m+1 the output leading degree is 2m+1-j,
with nonzero coefficient (1/2)binom(j,2m+1-j).
These leading degrees are distinct, so rank R_(2m+1)=m+1.
In particular *every* s=(1-l)/2 is an actual operator pole.
At s=0 its residue is f -> f'(0)/2, a nonzero square-zero rank-one map.
This is not a scalar pole of A.

## 6. Determinant continuation and the obstruction

Away from operator poles, polynomial finite sections and trace-norm convergence
give the same determinant product as before. Alternatively analytic continuation
of section 2 gives this identity; on compact s sets its tail converges normally
because Re(s+j)>1/2 for sufficiently large j and A(s+j)=O_K(2^-j).
Thus D(u,s) is entire in u and meromorphic in s, with possible poles only at
s=1/2-m. It is holomorphic at all s=0,-1,-2,... despite the nonzero square-zero
operator residues there. This is determinant blindness, not a removable
operator singularity and not a defined original branch sum at those points.

For u=1, the pole at s=1/2-m has exact order m+1.
Indeed the j=0,...,m factors have nonzero simple-pole residues -r_(m-j).
All remaining factors at s=s_m are 1-A(1/2+j-m), j>=m+1.
Their arguments are >=3/2, and 0<A(v)<A(1)=1 for v>1
(the equality A(1)=1 follows by telescoping); their convergent product is nonzero.
There is no cancellation. Thus D(1,s) cannot equal e^g(s) times an entire
target function for entire g. In particular this frozen determinant cannot
satisfy the evaluator's zero-free-entire-normalization target.
Replacing D by a differently normalized object or a quotient changes the
candidate and is not an achieved repair. No assertion about matched target
zeros is needed or made.

## 7. Verification boundary and ownership

Finite exact matrices, residues and word traces test all normalizations and
counterexamples; they do not prove the infinite spectrum or continuation.
The proofs above supply those quantifiers. Classical Lüroth coding belongs
to the Lüroth literature; analytic trace/determinant machinery belongs to
Ruelle, Mayer and Bandtlow–Jenkinson. The special residue calculation is
derived here, without a certified literature-priority assertion.

No rational-prime carrier emerges from the composite slopes n(n+1), nor from
rewriting a source sum using Hurwitz zeta. A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL,
A4_FORMAL_HINT; ROUTE_A_REJECTED. NO_BAD_EULER_OR_ROOT_NUMBER.
