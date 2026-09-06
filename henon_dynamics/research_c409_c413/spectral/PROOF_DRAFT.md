# Logarithmic Dirichlet germs and Gram eigenvalues — proof candidate

2026-09-06. Mathematical candidate, not an admitted paper. The complete
transfer statement below is proposed as the increment, not a new generic
approximation method. Independent internal proof and ownership reports are
in the nonlinear_geometry directory. The classical model coefficient now
has a complete alternate derivation in MODEL_MOMENT_PROOF.md using ALT,
whose Hilbert-space statement has been source-checked. The inaccessible
original Widom text is retained as a source-history limitation, not a
hidden theorem dependency. No numerical evidence is used as proof.

## 1. Precise theorem under consideration

Let `(a_j)` be a locally finite sequence in `[a_*,infinity)`, `a_*>1`, and let
`w_j>0`. Repetitions of each frequency are allowed only finitely often.
Let rho be real. Assume

`D(s)=sum_j w_j a_j^(-s)`

converges for every real `s>rho`. Assume that for some `r>0`, `c>0`, and a
function A holomorphic on `|u|<r`,

`D(rho+u)=-c Log(u)+A(u)` for `Re(u)>0`, `|u|<r`,

where Log is the branch real on the positive axis. Define

`G_ij=sqrt(w_i w_j) (a_i a_j)^(-rho/2)/log(a_i a_j)`.

**Proposed conclusion.** G defines a positive trace-class operator on ell²,
with infinitely many positive eigenvalues, listed decreasingly with
multiplicity, and

`N(exp(-L);G) ~ L²/(2 pi²)`, equivalently
`log lambda_n(G) = -pi sqrt(2n)+o(sqrt(n))`.

For its ordinary Fredholm determinant,

`log det(I+exp(L)G) ~ L³/(6 pi²)`.

The result concerns positive eigenvalues only if repeated frequencies create
a zero eigenspace. Neither a leading multiplicative eigenvalue constant nor a
second asymptotic coefficient is asserted.

## 2. Positive Gram factorization and trace class

Put `b_j(t)=sqrt(w_j) a_j^(-rho/2) exp(-t log a_j)`, `t>0`.
Tonelli gives

`sum_j ||b_j||² = integral_0^infinity D(rho+2t) dt`.

The integral is finite: its integrand is `O(1+|log t|)` near zero; for `t>=eta`
positivity of the Dirichlet coefficients and the lower bound `a_j>=a_*` give

`D(rho+2t) <= D(rho+eta) a_*^(-(2t-eta))`.

Thus the map B from ell² to `L²(0,infinity)` with columns b_j is
Hilbert–Schmidt. Direct integration gives `G=B*B`. The nonzero eigenvalues,
with multiplicity, equal those of `BB*`, whose kernel is `D(rho+t+s)`.
This also proves trace class without assuming a prime number theorem.

Let `E(u)=integral_1^infinity exp(-u x) dx/x`, for `Re u>0`, and let H_E be
the corresponding Hankel operator. The classical expansion

`E(u)=-Log(u)-gamma - sum_{k>=1} (-u)^k/(k k!)`

shows that `R(u)=D(rho+u)-c E(u)` extends holomorphically through zero.
It is holomorphic on the union of a disk about zero and the right half-plane.
On every half-plane `Re u>=eta>0`,

`|R(u)| <= C_eta exp(-d Re u)`

for a fixed `d>0` (decrease d below `min(log a_*,1)` if needed).
Consequently `BB*=c H_E+H_R`.

## 3. Explicit analytic-remainder estimate

**Lemma.** Suppose R is holomorphic on `{Re u>0} union {|u|<r}` and satisfies
the exponential bound just stated for every eta>0, with one fixed d>0.
Then H_R is compact and, as L tends to infinity,

`N_s(exp(-L);H_R)=O(L log L)`.

Here `N_s` counts singular values exceeding the threshold. Constants may
depend on R, r and d, never on L.

**Proof.** Choose a positive h with `5h<r`. Partition the x half-line into
`I_0=[0,h]` and `I_k=[2^(k-1)h,2^k h]`, k>=1. Endpoints have measure zero.
For I_0 use Taylor expansion in x at `h/2`, with complex radius h. For fixed
y>=0 the whole circle in the variable u=x+y lies in the holomorphy domain:
if y<=2h its modulus is at most `7h/2<r`, while if y>2h its real part is
at least `y-h/2>0`. Compactness on the first region and the half-plane bound
on the second give a uniform circle bound `C exp(-d' y)` for some d'>0.
The Taylor ratio on I_0 is at most 1/2.

For I_k=[v,2v], v>=h, use center `3v/2`, radius v. Its Taylor ratio is again
at most 1/2 and every u on the circle has real part at least `y+v/2>=h/2`.
The common half-plane estimate gives circle bound
`C exp(-d(y+v/2))`. Taylor truncation at degree m-1 therefore gives kernel
error at most

`C 2^(-m) exp(-d' y)` on I_0, and
`C 2^(-m) exp(-d(y+v/2))` on each I_k.

Keep the first K+1 intervals. Their Taylor kernels form an operator of rank
at most `(K+1)m`, because each interval contributes m functions of x times
functions of y. The squared Hilbert–Schmidt norm of the Taylor errors is
bounded by `C 4^(-m)`, independently of K: use
`sum_{k>=1} 2^(k-1)h exp(-d 2^(k-1)h)<infinity`.
On the omitted x tail `x>2^K h`, the half-plane estimate bounds the squared
Hilbert–Schmidt norm by `C exp(-2d 2^K h)`.

Choose `m=O(L)` large enough and `2^K h=O(L)` large enough that both error
norms are less than `exp(-L)/2`. Hence K=O(log L), and an operator of rank
O(L log L) approximates H_R within exp(-L) in operator norm. The minimax
characterization of singular values gives the assertion. The same estimates
also directly establish that H_R is Hilbert–Schmidt. QED.

This proof does not invoke smooth-error membership in all Schatten classes.
Such a weaker statement would not be enough on the present scale.

## 4. Classical model law, with a complete alternate proof

The model satisfies

`N(exp(-L);H_E) ~ L²/(2 pi²)`.

A complete independent derivation of the coefficient is in
`MODEL_MOMENT_PROOF.md`: its Laplace/Mellin factorization gives the weight
`a_E(x)=exp(-x) 1_(x>=0)` and Fourier multiplier
`b(xi)=pi/cosh(pi xi)`. The classical Araki–Lieb–Thirring inequality yields
the sharp lower bound for `q² Tr(H_E^q)` as q tends to zero. The soft
weights `exp(-x)(1+exp(-x))^(-M)` give upper form majorants; uniform
Gaussian coherent-state bounds yield limsup at most
`(1+1/(M-1))/pi²`. First fix even M, let q tend to zero, and then let
M tend to infinity. This proves `q² Tr(H_E^q)->1/pi²`. The supplement
proves the elementary required Karamata passage in full, giving the
factor 1/2 in the count. It invokes no unproved semiclassical Weyl rule.

This is a proof of a classical model input, **not another new theorem
contract**. For comparison with its classical owner, the following exact
Laguerre calculation explains its relationship with Widom's Hankel model.

Use the orthonormal Laguerre basis
`ell_j(t)=sqrt(2) exp(-t) L_j(2t)` of `L²(0,infinity)`. Its Laplace transform is

`integral_0^infinity exp(-x t) ell_j(t) dt
 = sqrt(2) (x-1)^j/(x+1)^(j+1)` for x>0.

For H_E, Fubini and `v=(x-1)/(x+1)` with x>=1 give its matrix

`J_theta(j,k)=integral_0^1 theta(v) v^(j+k) dv`,
`theta(v)=(1-v)/(1+v)`.

All identities can first be proved on finite linear combinations, then
extended by the positive trace-class bounds. Denote by J_f the moment
Hankel operator with a nonnegative weight f. Then weight inequalities imply
operator inequalities, since its form on a polynomial p is
`integral_0^1 f(v)|p(v)|² dv`.

Let `ell(v)=-log v`. For 0<v<1, `theta(v)<=ell(v)`. For any fixed
delta in (0,1), continuity and the positive endpoint ratio 1/2 imply that
there is `c_delta>0` with `theta(v)>=c_delta ell(v)` on `[delta,1)`.
Consequently

`c_delta (J_ell-J_low) <= J_theta <= J_ell`,

where `J_low=J_(ell 1_(0,delta))`.
The entries of J_ell are exactly `(j+k+1)^(-2)`.

**Classical source comparison W, no longer needed as a dependency.**
Widom's law for this particular matrix is reported as

`log lambda_n(J_ell)=-pi sqrt(2n)+o(sqrt(n))`.

This is the alpha=2 instance of the formula reported in Tantalakis's
introduction. The public 2014 Pushnitski–Yafaev v1 reports a different
coefficient, apparently missing the subtraction of 1 in alpha-1. Original
text verification has not been obtained. The complete alternate proof above
removes dependence on either reported coefficient without asserting a new
Widom theorem or a primary-source audit that did not occur.

The low-weight operator has exponentially decreasing singular values:
retain its first m rows and first m columns, a rank at most 2m operation.
The remaining Hilbert–Schmidt norm is exponentially small in m. For example,
for j+k>=1,

`integral_0^delta (-log v) v^(j+k) dv
 <= delta^((j+k)/2) integral_0^delta (-log v) dv`.

Thus `N_s(exp(-L);J_low)=O(L)`. In this optional historical alternative
route only, from the form inequalities, the variational
counting inequality for a sum, and W, both upper and lower bounds give

`N(exp(-L);H_E)=N(exp(-L);J_theta) ~ L²/(2 pi²)`.

More explicitly, `J_high=J_ell-J_low` and
`N(2t;J_ell)<=N(t;J_high)+N(t;J_low)`, whereas
`N(t;J_theta)>=N(t/c_delta;J_high)`. Multiplying a positive threshold by a
fixed constant changes L by O(1), which does not affect the leading L² term.

## 5. Transfer and Fredholm determinant

For compact self-adjoint A and E, and t>0, the variational inequality gives

`N_+(2t;A+E)<=N_+(t;A)+N_s(t;E)`

and, by interchanging A+E and A,

`N_+(2t;A)<=N_+(t;A+E)+N_s(t;E)`.

Apply these with `A=c H_E`, `E=H_R`, and the estimate in Section 3.
The error O(L log L) is o(L²). Section 4 therefore gives the claimed counting
law for BB*, hence G. In particular there are infinitely many positive
eigenvalues, and elementary monotone inversion gives the lambda_n statement.

For completeness set `x_n=-log lambda_n`. These numbers have a finite lower
bound, and their counting function satisfies `M(x)~a x²`, `a=1/(2pi²)`.
The determinant logarithm equals `sum_n log(1+exp(L-x_n))`.
The identity

`log(1+exp(L-x))=integral_x^infinity (1+exp(t-L))^(-1) dt`

and Tonelli express this sum as
`integral_(x_min)^infinity M(t)/(1+exp(t-L)) dt`.
Its part below L is asymptotic to `a L³/3`. The difference caused by replacing
the logistic factor there by 1, and its tail above L, are O(L²+1), using
`M(t)=O(1+t²)` for t>=0 and exponential decay in |t-L|. A finite initial
negative-t interval contributes only O(1). This proves the stated cubic law.

## 6. Arithmetic application with source-checked classical inputs

For a fixed modulus q and a nonempty subset S of reduced residue classes,
take the primes with `p mod q in S`, weights one, and rho=1. Character
orthogonality and the Euler products of Dirichlet L-functions give

`sum_(p mod q in S) p^(-s)
 = (1/phi(q)) sum_chi (sum_(a in S) conjugate(chi(a))) log L(s,chi)
   - H(s)`,

where H is holomorphic for `Re s>1/2` near s=1: it comprises the absolutely
convergent prime-power terms with powers at least 2. The classical fact that
nonprincipal Dirichlet L-functions are nonzero at 1, and that the principal
L-function has a simple pole there, supplies the required local logarithmic
germ with `c=|S|/phi(q)>0`. All complex logarithms are local branches.

This is one application of the same theorem, not a separate C-number paper.
The density c disappears from the leading inverse-log counting coefficient;
one must not interpret that leading law as recovery of residue-class data.

## 7. Remaining gates

1. Sections 2–5 have received an independent internal mathematical check;
   the complete alternate model proof has separately been sent for review.
2. The bounded ownership audit found no exact direct owner of the entire
   transfer statement. It did find substantial ownership of the Gram and
   analytic-approximation methods, including Webb arXiv:2509.14017v4.
   The relevant report must accompany an admission decision.
3. Classical Dirichlet L-function facts were checked against DLMF §25.15,
   including (25.15.2), (25.15.9), and the pole/analyticity paragraph.
4. A nonauthor decision whether this closes a sufficiently substantial and
   independent question. Positivity or a classical model law alone would not.

No arbitrary-density beta-family, target arithmetic identity, Euler/root-number
claim, target zero correspondence or spectral realization is concluded.
