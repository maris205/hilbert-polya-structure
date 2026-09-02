# Frozen theorem contract — cut-intersection collapse

## Status

**OWNER-THIN INTERNAL CANDIDATE / HOLD_EXTERNAL.** This contract is not a
novelty or priority claim. Graph cuts, binary history coding, complete
bipartite components, and inclusion--exclusion are owned background and
receive zero contribution credit.

## Literal dynamics

Fix a labelled vertex set $[n]$, with $n\ge2$, and start from $G_0=K_n$.
At epoch $s\ge1$, independently assign a fair bit $b_s(v)$ to every vertex.
Let $C_s$ contain the edge $uv$ exactly when $b_s(u)\ne b_s(v)$, and set

\[
G_s=G_{s-1}\cap C_s.
\]

The absorption time is

\[
T=\min\{s\ge1:E(G_s)=\varnothing\}.
\]

No update rule, conditioning, quotient, or stopping convention may be changed
without reopening Stage 1.

## Frozen notation

For $t\ge1$, let $R=2^{t-1}$. The $2^t$ binary words of length $t$ form $R$
unordered complementary pairs. Define, for $R,m\ge0$,

\[
A_R(m)=\sum_{j=0}^{R}(-1)^{R-j}\binom Rj2^j j^m
      =m![x^m](2e^x-1)^R.
\]

The boundary conventions are

\[
A_0(0)=1,\qquad A_0(m)=0\ (m>0),\qquad A_R(0)=1.
\]

For a labelled graph $H$, let $z(H)$ be its number of isolated vertices. If
every nontrivial connected component is complete bipartite, let $r(H)$ be the
number of those components.

## Theorem A — exact all-time absorption law

For every $n\ge2$ and $t\ge1$,

\[
\Pr(T\le t)=\frac{A_{2^{t-1}}(n)}{2^{tn}}. \tag{A}
\]

Consequently, with $F_0=0$ and
$F_t=A_{2^{t-1}}(n)/2^{tn}$ for $t\ge1$,

\[
\Pr(T=t)=F_t-F_{t-1}.
\]

Moreover,

\[
\Pr(T>t)\le \binom n2\,2^{-t},
\]

so absorption occurs almost surely and

\[
\mathbb E T
=1+\sum_{t\ge1}\left(1-\frac{A_{2^{t-1}}(n)}{2^{tn}}\right)
\le1+\binom n2.
\]

## Theorem B — complete image and every-target fibre atlas

For each vertex $v$, define its length-$t$ history word

\[
c_t(v)=(b_1(v),\ldots,b_t(v)).
\]

Pathwise,

\[
uv\in E(G_t)\quad\Longleftrightarrow\quad
c_t(u)=\overline{c_t(v)}. \tag{B1}
\]

A labelled graph $H$ has a positive time-$t$ fibre if and only if:

1. every nontrivial connected component of $H$ is complete bipartite;
2. $r(H)\le R$; and
3. either $z(H)=0$ or $r(H)<R$.

For every graph in this class,

\[
\#\{(b_s(v)):G_t=H\}
=(R)_{r(H)}\,2^{r(H)}A_{R-r(H)}(z(H)), \tag{B2}
\]

where $(R)_r=R(R-1)\cdots(R-r+1)$. Formula (B2) is also valid as a
zero-valued formula when $r(H)=R$ and $z(H)>0$. Every graph outside the class
has fibre zero. Dividing (B2) by $2^{tn}$ gives the complete one-time law.

As a labelled image-size corollary, put

\[
B(x)=\frac{(e^x-1)^2}{2}.
\]

Then

\[
|\operatorname{im}(G_t)|
=n![x^n]\left[
 e^x\sum_{j=0}^{R-1}\frac{B(x)^j}{j!}
 +\frac{B(x)^R}{R!}\right]. \tag{B3}
\]

The first term allows isolates only while fewer than $R$ nontrivial
components are used; the second supplies the isolate-free $r=R$ boundary.

## Mandatory boundary example

At $n=5,t=2$, one has $R=2$. A graph consisting of two disjoint edges and
one isolate has $r=R=2,z=1$ but is not attainable:

\[
(2)_2\,2^2A_0(1)=0.
\]

This example must remain in the manuscript or in an equally explicit remark;
it prevents the false shorthand that $r\le R$ alone characterizes the image.

## Independence of the two theorem axes

Theorem A counts only the empty target. Theorem B determines every labelled
target, including the exact zero-fibre boundary and nonempty component
profiles. Neither theorem may be advertised as independent progress if the
other is removed and merely reconstructed by summing an unstated atlas.

## Exact-control obligation

The focused verifier must:

- enumerate all word assignments in the frozen small parameter window;
- enumerate every labelled simple target graph in that window;
- compare every observed fibre with (B2), including zero fibres;
- compare the empty fibre with (A);
- check the first edge moment and the temporal tail inequality;
- replay byte-identically twice from a clean process.

Computation is counterexample pressure only and is never cited as proof.

## Claim ceiling

Allowed residual claims are the conjunction of the exact absorption law and
the complete labelled image/fibre atlas for this literal process. Forbidden
claims include the invention of cuts, binary codes, inclusion--exclusion,
bipartite cluster graphs, or random intersection graph methods. External
release remains forbidden until a direct-owner audit and both hostile reviews
close without a critical issue.
