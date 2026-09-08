# CP9 complete proof candidate: a period-two escape parameter

2026-09-08 UTC. **Author proof candidate; not an admitted contract.**
This proves the exact question frozen in [FROZEN_QUESTION.md](FROZEN_QUESTION.md),
subject to independent mathematical/source review. No mathematical program
was run. There is no extension here to arbitrary equal-weight binomials.

## Theorem

Let L be any field of characteristic 3, let Lbar be an algebraic closure,
and let k denote the algebraic closure of F_3 in Lbar. Set

\[
 f(X)=X^4+X^6,\qquad F_\lambda(X)=f(X)+\lambda.
\]

For all a,b in L, the set of lambda in Lbar for which both a and b are
preperiodic under ordinary iteration of F_lambda is infinite if and only if

\[
 a,b\in k\qquad\text{or}\qquad f(a)=f(b).
\]

## Two explicit imported results

From [Lee–Nam, arXiv:2509.15079v2](https://arxiv.org/html/2509.15079v2):

1. Theorem 1.5/4.4 specializes to: infinitude for a pair not both in k
   forces f(b)-f(a) in {0,1,-1}. Its hypotheses hold since the two
   exponent weights are 3^0(4-1)=3^1(2-1)=3 and both prime-to-3 parts
   exceed 1.
2. Theorem 2.1, stated there from Ghioca–Hsia Theorem 2.13: over a finite
   extension of the perfect closure of k(t), infinitely many distinct
   common-preperiodicity parameters imply equality of the two local
   canonical heights, at every place and every parameter in its completed
   algebraic closure. Its polynomial hypotheses are monic, degree at least
   2 and f(0)=0; they do not require a strict exponent-weight inequality.

These results, including the field and parameter quantifiers in the second,
were read in the primary HTML. Their proofs are not reconstructed here.
The original Ghioca–Hsia publisher item was read at abstract level only.
The new step below is the explicit two-cycle/escape witness excluding both
nonzero values; Lee–Nam Remark 4.5 leaves precisely those values open for f.

## Lemma 1: infinitely many preperiodicity parameters for one point

For every a in L, there are infinitely many lambda in Lbar for which a
is preperiodic under F_lambda.

Proof. If a is in k, every lambda in k works: a and lambda belong to a
common finite field, which is preserved by F_lambda.

Suppose a is not in k. Then a is transcendental over k. For n>=1 put

\[
 P_n(T)=F_T^n(a)-a\in k(a)[T].
\]

Induction shows that P_n is monic of degree 6^{n-1}. There is exactly one
parameter making a fixed, namely T_0=a-f(a). Since f'(X)=X^3, the chain
rule at this fixed parameter gives

\[
 P_n'(T_0)=1+a^3+\cdots+a^{3(n-1)}\ne0.
\]

The last inequality holds because a is transcendental and the displayed
polynomial has leading coefficient 1. Thus T_0 is a simple root of P_n.
For every prime integer ell>=2, P_ell has degree greater than 1 and so
has a root lambda_ell different from T_0. The ordinary least period of a
under F_{lambda_ell} divides ell, and it is not 1; hence it equals ell.
Distinct primes give distinct parameters. All roots belong to Lbar.
This proves the lemma. QED.

## Lemma 2: a universal parameter separating the exceptional pair

Suppose a is transcendental over k and f(b)=f(a)+1. Put

\[
 \lambda_* =1-a-f(a).
\]

Then a is periodic under F_{lambda_*}, whereas b has positive local
canonical height at every extension of the pole of a in k(a).

Proof. Direct expansion in characteristic 3 gives

\[
 f(-X)=f(X),\qquad f(X+1)=f(X)+X-1,
 \qquad f(X-1)=f(X)-X-1.
\]

Consequently the two exact orbit segments are

\[
 a\longmapsto 1-a\longmapsto a,
 \qquad
 b\longmapsto -a-1\longmapsto 0\longmapsto\lambda_*.
\]

Indeed, F_{lambda_*}(a)=1-a, and

\[
 F_{\lambda_*}(1-a)
 =f(a-1)+1-a-f(a)
 =-2a=a.
\]

For b, the first image follows from f(b)=f(a)+1 and 2=-1; the second is

\[
 F_{\lambda_*}(-a-1)
 =f(a+1)+1-a-f(a)=0.
\]

Let v be any extension of the pole valuation of a and write C=|a|_v>1.
The nonzero constants have absolute value 1. Distinct powers give

\[
 |f(a)|_v=C^6,\qquad |\lambda_*|_v=C^6.
\]

For any z with |z|_v>C, its sixth-power term strictly dominates both
the fourth-power term and lambda_*, so

\[
 |F_{\lambda_*}(z)|_v=|z|_v^6.
\]

Starting at F_{lambda_*}^3(b)=lambda_*, induction therefore yields

\[
 |F_{\lambda_*}^n(b)|_v=C^{6^{n-2}}\quad(n\ge3).
\]

By the definition of local canonical height,

\[
 \widehat h_{v,\lambda_*}(b)
 =\lim_{n\to\infty}6^{-n}\log^+|F_{\lambda_*}^n(b)|_v
 =\frac{\log C}{36}>0.
\]

The periodic orbit of a instead gives height zero. QED.

## Proof of the theorem, including arbitrary-field reduction

For sufficiency, if a,b lie in k, all parameters in k give two finite
orbits. If f(a)=f(b), then F_lambda(a)=F_lambda(b) for every lambda, so
the two points have the same orbit after one step. Lemma 1 supplies
infinitely many parameters for that common preperiodic tail.

For necessity, suppose the common-preperiodicity parameter set is infinite
and a,b are not both in k. Imported result 1 leaves only f(b)-f(a)=0,+1,-1.
The zero case is the required conclusion. In the two nonzero cases,
both a and b are transcendental over k: if one were constant, the equation
for the value of the other's nonconstant polynomial f would make the
other algebraic over the algebraically closed field k, hence constant.
Interchanging a and b changes the sign. We may therefore assume

\[
 f(b)=f(a)+1.
\]

This equation makes b algebraic over k(a). Write

\[
 K_0=\bigcup_{r\ge0} k(a^{1/3^r}),\qquad K=K_0(b)\subseteq\overline L.
\]

Then K is a finite extension of the perfect closure K_0 of the rational
function field k(a), exactly as required by imported result 2. Every
parameter lambda for which a is preperiodic is algebraic over k(a): a
relation F_lambda^n(a)=F_lambda^m(a), n>m>=0, is a nonzero polynomial
equation in lambda, since the degrees in lambda are 6^{n-1} and
6^{m-1} for m>=1, while m=0 gives the constant a. Therefore all of the
assumed infinitely many common parameters belong to the algebraic closure
of K inside Lbar. Passing to this function-field setting loses none of
the assumed infinite set.

Choose a place v of K above the pole of a in k(a); its extension has
|a|_v>1. Imported result 2 applies and asserts equality of the local
canonical heights of a and b at the parameter lambda_* in K. Lemma 2
gives respectively 0 and (log|a|_v)/36, a contradiction.

Both nonzero exceptions are impossible. This proves necessity and the
theorem. QED.

## Exact increment and review boundaries

The complete classification is for this fixed f and **all** fields and
starting pairs; it is not a theorem about a chosen a,b. The period-two
parameter is an intermediate uniform witness, not the contracted outcome.
The key cancellation of a two-cycle sends the exceptional second point
to the constant 0, whose subsequent orbit must escape at a pole.

The proof is short because the recent source already supplies both the
three-value reduction and the all-parameter local-height bridge. This
dependency is substantive and explicit. Resolving the authors' named
remaining example is different from claiming the whole unresolved
equal-weight family solved, and the coordinator must still decide whether
this exact increment satisfies the batch's fifth-contract standard.
No source novelty claim beyond the bounded current-source check, no
manuscript, no formal external evaluation and no admission is made here.

Independent review should attack: the two imported hypotheses; retention
of all parameters under K_0(b); inseparable field extensions and the pole;
the signs in the two orbit segments; the escape exponent/height; the
simple-root argument in Lemma 1; and the distinction from source coverage.
