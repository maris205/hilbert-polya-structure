# A classical model law by small Schatten moments

2026-09-06. New proof candidate for the **classical model input** only.
This does not create another research contract or assert a new Widom law.
Its purpose is to eliminate dependence on a disputed reported constant
in the square-Hankel citation. Independent review is still required.

## 1. Model and Fourier convention

Let `E(u)=integral_1^infinity exp(-u lambda) d lambda/lambda`, and let
H_E be its positive Hankel operator on `L^2(0,infinity)`. We prove

    lim_(q down to 0) q^2 Tr(H_E^q)=1/pi^2,
    N(exp(-L);H_E) ~ L^2/(2 pi^2).

The Fourier transform on the line is unitary with kernel
`(2 pi)^(-1/2) exp(-i xi x)`. The convolution operator with kernel
`1/(2 cosh((x-y)/2))` has multiplier `b(xi)=pi/cosh(pi xi)`.
This transform identity follows, for example, from the beta integral
after the substitution `r=exp(x-y)`.

For any positive density sigma for which
`integral sigma(lambda) d lambda/lambda` is finite, factor its Hankel
kernel through the Laplace operator with kernel
`exp(-t lambda) sqrt(sigma(lambda))`. The two products have the same
nonzero eigenvalues. The product on the lambda space has kernel

    sqrt(sigma(lambda) sigma(mu))/(lambda+mu).

The unitary substitution `lambda=exp(x)` turns this product into

    K_a = sqrt(a(X)) b(D) sqrt(a(X)),   a(x)=sigma(exp(x)).

Its trace is `1/2 integral a(x) dx`, as is also seen directly from
the Laplace factorization. For H_E the weight is
`a_E(x)=exp(-x) 1_(x>=0)`. In particular its trace is 1/2.

## 2. Classical trace inequality supplies the lower bound

We use the Araki–Lieb–Thirring inequality for positive bounded
Hilbert-space operators, with traces interpreted in `[0,infinity]`:
for `0<q<1`,

    Tr((A^(1/2) B A^(1/2))^q)
        >= Tr(A^(q/2) B^q A^(q/2)).                         (2.1)

This is the reverse-exponent specialization of the classical ALT
inequality, not a new inequality. The upper-bound argument in Section 3
is independent of ALT and proves finiteness of `Tr(H_E^q)`; it may be
read first, so the application does not rely on a formal infinite-trace
substitution. Take `A=a_E(X)`, `B=b(D)`.
The trace on the right is the squared Hilbert–Schmidt norm of
`b(D)^(q/2) a_E(X)^(q/2)`, and its Fourier kernel gives exactly

    Tr(H_E^q) >= (1/(2 pi)) integral a_E(x)^q dx
                                * integral b(xi)^q d xi.    (2.2)

The first integral is `1/q`. Since

    pi exp(-pi |xi|) <= b(xi) <= 2 pi exp(-pi |xi|),

we have `q integral b^q -> 2/pi`. Thus

    liminf_(q down to 0) q^2 Tr(H_E^q) >= 1/pi^2.             (2.3)

No finite-dimensional compression identity for powers is presumed.
Equation (2.1) is used in its bounded Hilbert-space form; the exact
classical source statement must be retained in the source notes.

## 3. Soft majorants and their coherent-state upper bound

Fix an even integer `M>=2`, and put

    sigma_M(lambda) = lambda^(-1) (lambda/(1+lambda))^M,
    a_M(x) = exp(-x) (1+exp(-x))^(-M).

The corresponding H_M and K_M are positive trace class. Pointwise
`sigma_E <= 2^M sigma_M`, so on the original t space the positive
Laplace forms give `H_E <= 2^M H_M`. This is a form comparison before
changing spaces; no monotonicity of `sqrt(a) b(D) sqrt(a)` in a is
needed.

Let `g(t)=pi^(-1/4) exp(-t^2/2)` and
`psi_(x,xi)(t)=g(t-x) exp(i xi t)`. Their resolution of the identity is

    (1/(2 pi)) integral |psi_(x,xi)><psi_(x,xi)| dx d xi = I. (3.1)

Indeed, first Plancherel in xi and then `integral |g(t-x)|^2 dx=1`
give the identity on every vector. Concavity of `v^q`, spectral Jensen
and Tonelli therefore give, for every bounded positive K,

    Tr(K^q) <= (1/(2 pi)) integral
                       <psi_(x,xi),K psi_(x,xi)>^q dx d xi. (3.2)

This is an extended nonnegative trace identity followed by a scalar
inequality; it does not assume in advance that K^q is trace class.

We claim the uniform estimate

    <psi_(x,xi),K_M psi_(x,xi)>
        <= C_M a_M(x) exp(-pi |xi|).                         (3.3)

Here C_M is independent of x, xi and q. To prove it, fix
`s in (pi/2,pi)` and define `F_x(t)=sqrt(a_M(t)) g(t-x)`.
As M is even, the square-root weight
`exp(-t/2)(1+exp(-t))^(-M/2)` is holomorphic in `|Im t|<pi`.
For real r and `|v|<=s`,

    |1+exp(-r-i v)| >= cos(s/2)(1+exp(-r)).

Also `|(log a_M)'(r)| <= M-1`. The complex Gaussian and these two
inequalities imply

    |F_x(r+i v)| <= C_(M,s) sqrt(a_M(x))
          exp((M-1)|r-x|/2 -(r-x)^2/2),                     (3.4)

uniformly in x, r and v. Vertical contour ends vanish by the Gaussian.
Shifting the Fourier contour to `Im t=-s sign(nu)` gives

    |hat F_x(nu)| <= C_(M,s) sqrt(a_M(x)) exp(-s |nu|).      (3.5)

The expectation in (3.3) is
`integral b(eta) |hat F_x(eta-xi)|^2 d eta`. Since `2s>pi`,

    integral exp(-pi |eta|) exp(-2s |eta-xi|) d eta
      <= exp(-pi |xi|) integral exp(-(2s-pi)|eta-xi|) d eta,

which proves (3.3), with all constants uniform in x and xi.

It follows from (3.2)–(3.3) that

    Tr(K_M^q) <= C_M^q/(2 pi) * integral a_M(x)^q dx
                                     * 2/(pi q).           (3.6)

The spatial integral equals `B(q,(M-1)q)` by `r=exp(-x)`.
Equivalently, its positive and negative tails have slopes 1 and M-1.
Consequently

    q integral a_M(x)^q dx -> 1+1/(M-1),
    limsup q^2 Tr(H_M^q) <= (1+1/(M-1))/pi^2.               (3.7)

In particular these traces are finite for every q>0 sufficiently small.
The constant C_M may grow with M; M is fixed before q tends to zero.

## 4. Sharp moment limit and elementary Tauberian passage

Eigenvalue monotonicity applied to `H_E <= 2^M H_M` gives
`Tr(H_E^q) <= 2^(Mq) Tr(H_M^q)`. Thus (2.3) and (3.7), first as
q tends to zero and then along even M tending to infinity, prove

    q^2 Tr(H_E^q) -> 1/pi^2.                                (4.1)

The following elementary special case of Karamata's theorem fixes the
factor of two. If a positive locally finite measure mu on `[0,infinity)`
has Laplace transform `F(q) ~ C q^(-2)` at zero, then
`mu([0,L]) ~ C L^2/2`.

For completeness, set `nu_L(B)=L^(-2) mu(L B)`. Its Laplace transform
converges to `C/s^2` for each s>0. Tilt it to the finite measure
`omega_L(dx)=exp(-x) nu_L(dx)`, and push this measure forward under
`y=exp(-x)` to `[0,1]`. Its m-th moment converges to
`C/(m+1)^2` for every nonnegative integer m, including m=0.
These are the moments of the pushforward of `C x exp(-x) dx`.
Polynomial density on `[0,1]` proves weak convergence of the finite
measures. On `y in [exp(-1),1]`, the bounded function `1/y` is continuous
except for the two cutoff endpoints, which have no mass in the limit.
Its integrals therefore converge, giving

    nu_L([0,1]) -> integral_0^1 C x dx = C/2.

Apply this to the counting measure on shifted eigenvalue energies
`-log lambda_j(H_E)+h >= 0`. A fixed shift h multiplies its Laplace
transform by `exp(-qh)` and does not change the leading asymptotic.
Equation (4.1) now proves the model counting law. Strict versus closed
threshold conventions give the same asymptotic by bounding a threshold
at L between closed counts at `(1-epsilon)L` and `(1+epsilon)L`, and
then letting epsilon tend to zero. Monotone inversion
also gives `log lambda_n(H_E)=-pi sqrt(2n)+o(sqrt(n))`.

## 5. Dependencies and pending review

Only the bounded-operator ALT trace inequality is external to this
model proof apart from elementary Fourier/complex analysis and
standard spectral calculus. The classical model asymptotic remains
credited to Widom. The coherent-state method and Karamata passage
are classical techniques, not separate novelty claims.

The proposed new paper remains the single log-Dirichlet-germ to Gram
spectrum transfer contract in `PROOF_DRAFT.md`, if its ownership and
substantiality gates clear. This supplement must first receive an
independent check of the ALT specialization, soft-weight comparison,
uniform complex-strip estimate, moment-limit order and Tauberian step.

### Classical ALT source receipt

The coordinator read the official abstract and bibliographic record of
Araki, *On an inequality of Lieb and Thirring*, Letters in Mathematical
Physics 19 (1990), 167–170,
[DOI 10.1007/BF01045887](https://link.springer.com/article/10.1007/BF01045887).
It states the inequality for positive self-adjoint operators; the
subscription full text was not obtained or bypassed. For an unambiguous
readable statement with the Hilbert-space scope, the coordinator also
read Theorem 5.17, its equations (64)–(65), and the complete following
proof in Laurent Lafleche's author-hosted
[Semiclassical dynamics notes, Section 5.5.4](https://laurent-lafleche.perso.math.cnrs.fr/docs/Semiclassical%20dynamics.pdf).
Its finite-matrix proof is explicit and it attributes the general
operator approximation to Araki. The theorem is stated for positive
self-adjoint operators and every positive Schatten exponent r.

To remove any ambiguity about exponent orientation, use its norm form
`||AB||_(pr)^p <= ||A^p B^p||_r` with
`A=b(D)^(q/2)`, `B=a_E(X)^(q/2)`, `p=1/q`, `r=2q`, then raise to
power `2q`. The left side becomes the phase-integral Hilbert–Schmidt
norm squared and the right side becomes `Tr(K_E^q)`.
Audenaert's [arXiv:math/0701129v2, Theorem 1](https://arxiv.org/pdf/math/0701129)
was read as an additional matrix-form orientation check, not as the
sole justification of the infinite-dimensional use.
