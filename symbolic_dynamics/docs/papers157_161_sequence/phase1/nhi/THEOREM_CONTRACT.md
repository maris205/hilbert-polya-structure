# Frozen theorem contract — Newton--Hensel dynamics modulo $2^n$

## Status

**FOUNDATIONAL OWNER HIT / RESIDUAL FINITE-ATLAS CANDIDATE /
HOLD_EXTERNAL.** The cubic idempotent-lifting polynomial and its quadratic
error improvement are prior art and receive zero contribution credit.

## Literal dynamics

For $n\ge1$, let

\[
F_n:\mathbb Z/2^n\mathbb Z\longrightarrow\mathbb Z/2^n\mathbb Z,
\qquad
F_n(x)=3x^2-2x^3.
\]

Select the endpoint error by parity:

\[
e(x)=
\begin{cases}
x,&x\equiv0\pmod2,\\
1-x,&x\equiv1\pmod2.
\end{cases}
\]

Use the truncated convention $v_2(0\bmod 2^n)=n$. The first entry time into
$\{0,1\}$ is denoted $\tau_n(x)$.

## Theorem A — exact pointwise and global temporal atlas

For every $x$ and $t\ge0$,

\[
v_2(e(F_n^t(x)))=\min\{n,2^t v_2(e(x))\}. \tag{A1}
\]

The endpoint is $x\bmod2$, and

\[
\tau_n(x)=\min\{t\ge0:2^t v_2(e(x))\ge n\}. \tag{A2}
\]

For every $t\ge0$,

\[
\#\{x:\tau_n(x)\le t\}
=2^{n-\lceil n/2^t\rceil+1}. \tag{A3}
\]

Thus every exact temporal shell is the difference of two consecutive values
in (A3), the maximum entry time is

\[
M_n=\lceil\log_2 n\rceil,
\]

and the exact temporal polynomial is

\[
D_n(z)=A_{n,0}
+\sum_{t=1}^{M_n}(A_{n,t}-A_{n,t-1})z^t,
\quad
A_{n,t}=2^{n-\lceil n/2^t\rceil+1}.
\]

The only recurrent states are the fixed points $0$ and $1$.

## Theorem B — complete one-step image and every-target fibres

For a nonendpoint target $y$, define its even reflection

\[
y^\flat=
\begin{cases}
y,&y\equiv0\pmod2,\\
1-y,&y\equiv1\pmod2.
\end{cases}
\]

It is in the image if and only if $v_2(y^\flat)=2v<n$ for an integer $v\ge1$
and, with $N=n-2v$ and $u=y^\flat/2^{2v}$,

\[
u\equiv
\begin{cases}
1\pmod2,&N=1,\\
3\pmod4,&N=2,\\
7\pmod8,&N\ge3,\ v=1,\\
3\pmod8,&N\ge3,\ v\ge2.
\end{cases} \tag{B1}
\]

Every such target has exactly

\[
2^{v+\min(N-1,2)}
=2^{v+\min(n-2v-1,2)} \tag{B2}
\]

preimages. Every inadmissible nonendpoint target has none. The endpoint
fibres are

\[
|F_n^{-1}(0)|=|F_n^{-1}(1)|=2^{\lfloor n/2\rfloor}. \tag{B3}
\]

Consequently,

\[
|\operatorname{im}F_n|
=2+2\sum_{1\le v<n/2}2^{\max(0,n-2v-3)}. \tag{B4}
\]

## Mandatory small-quotient boundary

The $N=1,2$ cases in (B1)--(B2) are not abbreviations of the $N\ge3$
four-to-one statement. Any manuscript must display them explicitly. The
focused verifier checks them independently for six valuation strata and all
$N\le11$.

## Independent theorem axes

The temporal theorem discards the normalized odd unit and retains only its
valuation. The inverse theorem requires that unit and distinguishes the
first nonzero valuation stratum from every later stratum modulo $8$. Neither
axis determines the other without additional information.

## Claim ceiling

Allowed residual claims are the complete finite-state temporal census and the
normalized-unit image/fibre atlas. Forbidden contribution claims include:

- invention of $3x^2-2x^3$;
- Newton or Hensel lifting of idempotents;
- quadratic improvement of the idempotent error;
- the smoothstep interpretation;
- generic valuation doubling.

No odd-prime or general finite-ring extension is claimed. External release
remains forbidden until focused owner subtraction and two hostile reviews
close.
