# G0 Strict-Extension Obstruction

Evidence status: **PROVED**

## Setup

Let

\[
X=\bigsqcup_{k\ge0}X_k
\]

be the Stage-01 wheel-sieve tail-path space, with
\(\sigma(X_k)\subseteq X_{k+1}\).  The components are disjoint.

## Proposition 1 — no strict extension creates periodic points

Let \((Y,S)\) be any dynamical system and let \(\pi:Y\to X\) satisfy

\[
\pi\circ S=\sigma\circ\pi.
\]

Then \(S\) has no periodic point of positive period.

### Proof

If \(S^ny=y\) for some \(n\ge1\), semiconjugacy gives

\[
\sigma^n(\pi(y))=\pi(S^ny)=\pi(y).
\]

But if \(\pi(y)\in X_k\), then
\(\sigma^n(\pi(y))\in X_{k+n}\), which is disjoint from \(X_k\).
This is a contradiction.  Therefore
\(\operatorname{Fix}(S^n)=\varnothing\) for every \(n\ge1\). \(\square\)

## Proposition 2 — the standard inverse-limit extension is empty

The inverse-limit set

\[
\varprojlim(X,\sigma)=
\{(x_0,x_{-1},\ldots):\sigma(x_{-j})=x_{-j+1}\}
\]

is empty.

### Proof

Suppose \(x_0\in X_k\) had an infinite backward orbit.  Because every
application of \(\sigma\) raises the level exactly once, \(x_{-j}\) would
have to lie in \(X_{k-j}\).  For \(j>k\), no nonnegative level \(k-j\)
exists.  Hence no point has a full backward orbit. \(\square\)

Equivalently,

\[
\sigma^n(X)\subseteq\bigsqcup_{k\ge n}X_k,
\qquad
\bigcap_{n\ge0}\sigma^n(X)=\varnothing.
\]

## Consequence and scope

The phrase “stationary natural extension” cannot mean a strict extension of
the frozen `SD-C05` self-map if the objective is to obtain primitive cycles.
That branch is closed before numerical work.

This does **not** rule out every quotient, factor, recoding, or independently
defined stationary grammar.  Such an object is not an extension in the above
sense and must be frozen as a new candidate, re-establish arithmetic A0, and
show that its cycles retain the same endogenous clock.  The separate finite
strong-bisimulation and clock-decoder obstructions narrow this live class, but
they are not theorems about every infinite symbolic recoding.  Stage 02
therefore requires a complete observational-recoding source lock before any
finite experiment.
