# A full-period intersection-weight calculation for logarithmic wild polynomials

2026-09-06. Internal proof package, not a paper acceptance or an ordinary
Artin–Mazur count. No C-number is assigned. The local ramification theorems
below belong to the cited authors; the proposed contribution is their
logarithmic-form specialization, global first-return inversion, and the
resulting explicitly owned weighted observable.

## 1. Object, clock, and the main statement

Let k be an algebraically closed field of odd characteristic p. Let
H in k[x] be nonconstant with H(0)=1, and put

    f(x)=x H(x)^p,  e=deg H,  d=pe+1,  m0=ord_0(H−1).

The clock n is ordinary compositional iteration of f; it is not a field
extension degree or a Frobenius-composition clock. We work on the affine line
and exclude its fixed point 0 from the following observable. Infinity is
also excluded. All geometric fixed-point sets are finite because
deg(f^n−x)=d^n.

For a nonzero periodic point a, let l(a) be its least positive period and set

    w(a) = ord_a(f^{l(a)}(x)−x)/p.

This is a positive integer and is constant along each cycle. It is an
intrinsic first-return local intersection length divided by the forced
factor p. It need not be 1; thus the phrase “Frobenius-reduced” would mean
removing one forced p, NOT taking the reduced subscheme.

Define

    W_n = sum_{a ≠ 0, f^n(a)=a} w(a),
    Z_w(t) = exp(sum_{n≥1} W_n t^n/n).

The full-period statement to be checked by a non-author is

    W_n = (d^n−1)/p
          − (p−1)/p sum_{j=1}^{v_p(n)} (d^{n/p^j}−1) − m0.       (1)

Its formal Euler product is

    Z_w(t) = product_{nonzero primitive cycles C}
               (1−t^{|C|})^{−w(C)} in 1+t Z[[t]],                (2)

and its explicit expression, with branches normalized to value 1 at 0, is

    Z_w(t) = (1−t)^{m0+1/p} (1−dt)^{−1/p}
             product_{j≥1}
             ((1−d t^{p^j})/(1−t^{p^j}))^{(p−1)/p^{j+1}}.        (3)

The power series has radius 1/d and is transcendental over C(t), indeed
non-holonomic. Its logarithmic derivative t Z_w'/Z_w has a single-valued
meromorphic continuation throughout |t|<1, and the unit circle is a natural
boundary for that MEROMORPHIC continuation. This carefully distinguished
statement does not assert holomorphy of Z_w throughout the unit disk: Z_w
already has a branch point at 1/d.

## 2. Explicit classical inputs

Here a formal germ g fixes 0 with derivative 1 and
i_r(g)=ord_0(g^{p^r}−id)−1.

* If p divides i_0(g), then i_r(g)=p^r i_0(g). This is Sen's classical
  identity, explicitly stated in Nordqvist–Rivera-Letelier, §1.2, and in
  Nordqvist, §2.2.
* Nordqvist–Rivera-Letelier, Theorem 2: for odd p and
  1≤q=i_0(g)≤p−1, the condition
  resit(g)=(q+1)/2−Res_0(1/(u−g(u)))≠0 is equivalent to
  i_r(g)=q(1+p+...+p^r) for every r.
* Nordqvist, Definition 2.2 and Theorem A: if q=i_0(g)>p is not divisible
  by p, let ell be its least nonnegative residue modulo p and set
  iota_1(g)=Res_0(u^{q−ell}/(u−g(u))). If iota_1(g)≠0, then
  i_r(g)=ell(1+...+p^{r−1})+q p^r for every r≥1.

Sources: [Nordqvist–Rivera-Letelier, arXiv:1904.04494](https://arxiv.org/pdf/1904.04494),
[Nordqvist, arXiv:1909.10782](https://arxiv.org/pdf/1909.10782).
These are inputs, not claims of new local ramification theory.

## 3. Differential structure and local calculation

Direct differentiation gives

    f'(x)=H(x)^p=f(x)/x,     f^*(dx/x)=dx/x.                     (4)

Inductively, if

    K_n(x)=product_{j=0}^{n−1} H(f^j(x)),

then f^n(x)=x K_n(x)^p. Hence

    f^n(x)−x=x (K_n(x)−1)^p.                                  (5)

Any nonzero periodic orbit avoids 0 and all zeros of H. Thus f is étale
along that orbit, and (f^n)'(a)=f^n(a)/a=1 whenever f^n(a)=a.
Local inverse coordinates show that first-return germs at points of the
same cycle are formally conjugate. This proves the constancy of w(a).

Fix such a point a, put l=l(a), and translate its first return to the
origin: g(u)=f^l(a+u)−a. Write

    T(u)=K_l(a+u)−1=c u^m+O(u^{m+1}),    c≠0.

Then

    g(u)−u=(a+u) T(u)^p,
    ord_0(g−id)=mp,       q=i_0(g)=mp−1.                       (6)

In particular m=w(a). Let ell=p−1. Whether m=1 or m≥2, the residue needed
for the relevant classical theorem is

    Res_0 u^{(m−1)p}/(u−g(u)) = −(ac)^{−p} ≠ 0.               (7)

To verify (7), expand its Laurent series as

    −c^{−p} u^{−p} (a+u)^{−1} (1+O(u))^{−p}.

The last factor is 1+O(u^p), so it cannot affect the coefficient of u^{−1}.
That coefficient is −c^{−p}a^{−p}, since the coefficient of u^{p−1} in
(a+u)^{−1} is a^{−p} for odd p. No unknown higher coefficient enters.

If m=1, (7) is the residue fixed-point index. As (q+1)/2=p/2=0 in k,
resit(g)=(ac)^{−p}≠0. Theorem 2 therefore gives

    i_r(g)=(p−1)(1+p+...+p^r)=p^{r+1}−1.

If m≥2, q=mp−1>p and (7) is Nordqvist's second residue. Theorem A gives

    i_r(g)=(p−1)(1+...+p^{r−1})+(mp−1)p^r
           =m p^{r+1}−1.

Both cases prove

    ord_a(f^{l p^r}−id)=w(a) p^{r+1} for every r≥0.            (8)

For a tangent-to-identity germ h(u)=u+A u^s+O(u^{s+1}) and an integer
b prime to p, induction on b shows
h^b(u)=u+bA u^s+O(u^{s+1}). Thus multiplication of the return time by b
does not change the first nonzero degree. Applying this to (8), for every
n divisible by l(a),

    ord_a(f^n−id)=p w(a) p^{v_p(n/l(a))}.                      (9)

At 0, (5) with n=1 gives i_0(f)=p m0. Sen's identity, followed by the
same prime-to-p iteration observation, gives

    ord_0(f^n−id)=1+m0 p^{v_p(n)+1}.                           (10)

The derivation covers arbitrary k and arbitrary H satisfying the stated
hypotheses. It does not assume that any first-return equation is squarefree.

## 4. Global inversion: proof of (1)

Let A_m be the sum of w(a) over nonzero points of exact period m. Total
intersection length on the affine line is d^n. Equations (9) and (10) give

    B_n := (d^n−1)/p − m0 p^{v_p(n)}
          = sum_{m|n} p^{v_p(n/m)} A_m.                        (11)

Write n=s p^r with p not dividing s, and define
E_k=sum_{h|s} A_{h p^k}. Equation (11) says

    B_{s p^j}=sum_{k=0}^j p^{j−k} E_k.

Consequently E_0=B_s and E_k=B_{s p^k}−p B_{s p^{k−1}} for k≥1.
Since W_n=sum_{k=0}^r E_k, telescoping yields

    W_n=B_n−(p−1)sum_{j=0}^{r−1} B_{s p^j}.

The contribution from m0 is exactly −m0, because
p^r−(p−1)(1+p+...+p^{r−1})=1. Substitution proves (1), including r=0
with an empty sum. The Möbius inversion formula

    A_n=sum_{h|n} mu(n/h) W_h

then gives total first-return weights at exact period n, not the number of
such points. The integer A_n/n equals the total w(C) over n-cycles.

## 5. Generating function and analytic singularities

Cycle constancy of w proves (2) by expanding −log(1−t^{|C|}). Since each
weight is a positive integer, (2) has integral coefficients. This is a
weighted orbit Euler product over primitive cycles, not an arithmetic
Euler product over primes.

Set A(t)=log(1−t)−log(1−dt), initially at t=0. Substituting n=p^j h in
the correction sum in (1) gives, coefficient by coefficient,

    log Z_w(t)=A(t)/p − (p−1)/p sum_{j≥1} p^{−j} A(t^{p^j})
                +m0 log(1−t).

This proves (3). Analytically the product converges normally, in logarithms,
on compact subsets of |t|<1/d. Put

    L(t)=t Z_w'(t)/Z_w(t).

Differentiating on that disk gives

    L(t)= 1/p [dt/(1−dt)−t/(1−t)] −m0 t/(1−t)
          −(p−1)/p sum_{j≥1}
             [d t^{p^j}/(1−d t^{p^j})
                         −t^{p^j}/(1−t^{p^j})].              (12)

On each compact subset of |t|<1 away from the displayed poles, the tail
converges normally: once |t|≤rho<1 and j is sufficiently large,
d rho^{p^j}<1/2, and each summand is O_d(rho^{p^j}). Thus (12) defines a
single-valued meromorphic continuation of L to the entire open unit disk.

For j≥1, each a satisfying a^{p^j}=1/d is a pole contributed by precisely
one summand: different j give different absolute values. All denominators
1−t^{p^i} remain nonzero there. The residue of L at a is

    Res_a L = (p−1)a/p^{j+1},

so Res_a(L/t)=(p−1)/p^{j+1}, which is nonzero and not an integer. At
a=1/d the residue of L/t is −1/p. Locally integrating L/t along any
continuation path avoiding these isolated poles shows

    Z_w(t)=(t−a)^{(p−1)/p^{j+1}} U(t)   (j≥1),

where U is holomorphic and nonzero after a local branch is selected.
Therefore these are genuine algebraic branch points, not zeros at which
Z_w happens to be holomorphic. In particular 1/d is a branch point and
the original Taylor series has radius exactly 1/d.

There are infinitely many distinct branch points. An algebraic function
over C(t) has only finitely many branch points; therefore Z_w is
transcendental. A solution of a linear differential equation over C(t) has
no singularities away from the finitely many poles/leading-coefficient
zeros of that equation. The same infinite branch-point set excludes
holonomicity as well.

Finally d^{−1/p^j} tends to 1 and the p^j-th roots of unity become dense
on the unit circle. Thus every point of that circle is an accumulation
point of genuine poles of L from inside. A meromorphic extension through
any such point would have an interior accumulation of poles, which is
impossible. This proves precisely the meromorphic natural-boundary
claim in §1. No claim about the ordinary dynamical zeta function follows.

## 6. A genuinely non-dynamically-affine subfamily

For every odd prime p the specialization H=1+x is

    f=x(1+x)^p=x+x^{p+1}.

It is not dynamically affine on P^1 in the usual finite-group-quotient
sense. Here is a check using the five-family classification in
[Bridy, §§2–5](https://arxiv.org/pdf/1306.5267).

1. Degree p+1 is not a power of p. Additive and subadditive quotients of
   affine maps of G_a have degree a power of p, since degrees in the finite
   semiconjugacy diagram cancel. They are excluded.
2. The finite critical point is uniquely −1, of local degree p: writing
   x=−1+u gives f(x)=−u^p+u^{p+1}. Infinity has local degree p+1.
   A separable positive or negative power map of degree p+1 has two
   critical points both of local degree p+1. Local degrees are Möbius
   conjugacy invariants, excluding power maps.
3. The normalized Chebyshev polynomial D_{p+1}, defined by
   D_{p+1}(t+t^{−1})=t^{p+1}+t^{−p−1}, has p distinct finite critical
   points when p is odd. Indeed t^{2(p+1)}=1 has 2(p+1) distinct roots;
   remove t=±1 and identify t with t^{−1}. The remaining 2p roots give
   p distinct points, where the quotient t↦t+t^{−1} is unramified and
   differentiating the displayed identity makes D' vanish. Its derivative
   has degree p, so these exhaust it. Including infinity gives p+1 critical
   points, whereas f has only two. Conjugate Chebyshev maps are excluded.
4. A separable Lattès map of degree d>1 cannot have a totally invariant
   point. To see this, let pi:E→P^1 be its finite quotient and psi:E→E its
   affine lift of degree d. Since p does not divide d=p+1, psi is a
   separable isogeny followed by a translation, hence each fiber of psi^n
   has d^n distinct geometric points. If b were totally invariant under f,
   the finite nonempty set S=pi^{−1}(b) would satisfy psi^{−n}(S)⊂S.
   But the left side has d^n |S| points. This contradiction excludes the
   Lattès case, since infinity is totally invariant for our polynomial.

For p=2 this argument does not apply: x+x^3=D_3(x), so that specialization
is a Chebyshev map. Odd characteristic is a genuine structural hypothesis,
not an omitted small case. The whole H-family is NOT asserted to consist
only of non-dynamically-affine maps.

## 7. Why the observable cannot silently be ordinary counting

In characteristic 3 take H=1+x+x^2, so f=x+x^4+x^7. Exact squarefree
factorization gives

    f^2−x=x^4 (x^2+2x+2)^6 Q(x)^3,
    Q=x^11+2x^9+x^8+2x^7+x^5+x^4+2x^3+2x+2.

The three displayed factors are pairwise coprime and squarefree, and
gcd(x^2+2x+2, f−x)=1. Its two roots therefore have exact period 2,
first-return multiplicity 6, and weight 2. There are 13 distinct nonzero
points fixed by f^2, but W_2=15. All fixed points themselves outside 0
have first-return weight 1 in this example, so the distinction first
appears at a genuinely new cycle, not merely from a repeated fixed root.

For H=1+x in odd characteristic, the bounded checks have not yet found
such extra first-return weights. They do NOT prove their absence for all
periods. Ordinary Artin–Mazur counting remains unproved even for that
subfamily in this package.

## 8. Independent verification and scientific boundary

The accompanying exact probe reconstructs each fixed-point polynomial from
its squarefree factors, isolates exact-period factors by gcd, checks the
predicted multiplicity at all earlier return factors, and independently
sums their FIRST-RETURN weights. It then compares that sum with (1).
It is not a proof search over all periods. No floating-point counts,
finite-extension point enumeration, or guessed linear recurrence is used.

The mathematical implication from the explicitly attributed classical
inputs is closed for (1)–(3) and (12). Scientific novelty remains a separate
gate: the residue calculation and divisor inversion are short, and this
may be a useful corollary rather than a standalone paper. No current claim
of priority, no solution of Bridy's ordinary-count conjecture, no arithmetic
local factors, no root number, and no Hilbert–Pólya zero correspondence are
made. Formal acceptance is reserved to the coordinator after non-author
source/independence review.
