# Theorem and boundary package — C122

## Proposition 1 — polynomial automorphism

For

\[
G(x,y,a)=(x^2+a-y,x,a/2+3x-1/2),
\]

the inverse is

\[
G^{-1}(X,Y,A)=(Y,Y^2+2A-6Y+1-X,2A-6Y+1),
\]

and `det DG=1/2` identically.

## Proposition 2 — exact low-period ledger

There are two certified fixed points

\[
(x,x,6x-1),\qquad x=-2\pm\sqrt5,
\]

and one named primitive two-cycle

\[
(1,-1,-3)\leftrightarrow(-1,1,1).
\]

Its chronological monodromy is

\[
M=\begin{pmatrix}-2&2&-3/2\\2&-1&1\\15/2&-3&13/4\end{pmatrix},
\]

so `tr M=1/4`, `det M=1/4`, and

\[
\det(I-zM)=1-z/4+(5/2)z^2-z^3/4.
\]

## Proposition 3 — feedback control

With the target states fixed, contraction `1/2` forces gain `3` and offset
`-1/2`.  Replacing the gain by `0` gives a parameter residual `-3`; gain
`5/2` gives residual `-1/2`.  Thus the displayed closure uses the feedback
channel.

## Boundary

The exact intrinsic witnesses support only `A1_WEAK`: the displayed fixed
points and oriented two-cycle have no prime-like target correspondence.
`A2_FAIL` because tangent monodromy supplies neither a target-divisor match
nor an analytic bridge; `A3_FAIL` because no global analytic structure or
continuation theorem is established; `A4_FAIL`.  The canonical tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`.
Completeness, analytic Fredholm/nuclear ownership, arithmetic promotion,
Hilbert–Pólya, and Route B remain unestablished.
