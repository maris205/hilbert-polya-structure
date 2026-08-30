# Proof spike: odd-component complementation on labelled graphs

**Status:** all-size structural theorem proved; bounded owner/value audit still
open.  **External status:** `HOLD_EXTERNAL`.

## 1. The map

For a finite simple labelled graph \(G\), complement the induced graph on
every connected component of odd order, synchronously, and leave every
even-order component unchanged.  Denote the result by \(\Phi(G)\).

No edge between two old components is ever created.  Hence every component
of \(\Phi(G)\) is contained in an old component: component partitions only
refine along an orbit.

## 2. Recurrent states and the period ceiling

Consider one connected component \(H\).

- If \(|H|\) is even, it is fixed forever.
- If \(|H|=1\), complementation changes nothing.
- If \(|H|>1\) is odd and \(\overline H\) is connected, the next step keeps
  the same vertex set as one component and the following step returns to
  \(H\).
- If \(|H|\) is odd and \(\overline H\) is disconnected, the component
  splits permanently into the connected components of \(\overline H\).

It follows that every eventual period is one or two.  A graph is recurrent
if and only if every nontrivial odd component is **co-connected** (its
complement is connected).  It is fixed if and only if every component is
either a singleton or has even order.  In particular, every nonfixed
recurrent graph lies on a genuine two-cycle.

## 3. Exact transient clock and a sharp family

Follow a nested lineage of odd components.  Whenever a nonrecurrent odd
component of order \(s\) splits, any odd child has order at most \(s-2\):
the vertices outside that child have positive even cardinality.  Consequently

\[
                    \operatorname{depth}(G)
                    \le \left\lfloor\frac{n-1}{2}\right\rfloor. \tag{1}
\]

This is sharp for every \(n\ge1\).  Define connected graphs on odd orders by

\[
 H_1=K_1,\qquad
 H_{2r+1}=\overline{\,H_{2r-1}\sqcup K_2\,}.              \tag{2}
\]

The complement in (2) is connected because it is a join across the displayed
components.  One update sends \(H_{2r+1}\) to
\(H_{2r-1}\sqcup K_2\); the even component freezes and the first component
continues.  Thus \(H_{2r+1}\) has depth exactly \(r\).  For even
\(n=2r+2\), the graph \(H_{2r+1}\sqcup K_1\) has the same depth \(r\),
proving sharpness in (1).

More precisely, if \(D(H)\) denotes depth for a connected odd graph, then

\[
D(H)=\begin{cases}
0,&\overline H\text{ is connected},\\
1+\max\{D(C): C\text{ is an odd component of }\overline H\},
  &\overline H\text{ is disconnected},
\end{cases}                                               \tag{3}
\]

where the maximum over no odd component is zero.  The depth of an arbitrary
graph is the maximum depth of its odd components.  Formula (3) is an exact
non-iterative clock in terms of the alternating component/co-component
decomposition tree.

## 4. Exact labelled enumerators for every depth layer

Let \(c_n\) be the number of connected labelled graphs on \([n]\), and put

\[
C_{\mathrm{even}}(x)=\sum_{n\ge2,\ n\ \mathrm{even}}c_n\frac{x^n}{n!}.
\]

For odd \(n\), the number \(q_n\) of connected and co-connected graphs is

\[
             q_1=1,\qquad q_n=2c_n-2^{\binom n2}\quad(n\ge3\text{ odd}). \tag{4}
\]

Indeed, for \(n\ge2\), a graph and its complement cannot both be
disconnected; complementation bijects the two disconnected classes.
Let

\[
Q(x)=\sum_{n\ge1,\ n\ \mathrm{odd}}q_n\frac{x^n}{n!}.
\]

Write \(O_t(x)\) for the EGF of connected odd graphs of depth at most \(t\).
Then

\[
O_0(x)=Q(x),                                               \tag{5}
\]

and, coefficientwise on odd degrees,

\[
O_t(x)=Q(x)+\operatorname{Odd}\!\left(
 e^{C_{\rm even}(x)+O_{t-1}(x)}-1-C_{\rm even}(x)-O_{t-1}(x)
\right),\qquad t\ge1.                                    \tag{6}
\]

The exponential term assembles the components of a disconnected complement:
even components are unrestricted connected graphs and odd components must
have depth at most \(t-1\).  Removing the empty and one-component assemblies
makes the decomposition disjoint, so (6) is exact rather than asymptotic.

Therefore the EGF for **all** labelled graphs of depth at most \(t\) is

\[
                 F_t(x)=e^{C_{\rm even}(x)+O_t(x)}.        \tag{7}
\]

The exact depth-\(t\) layer is \(n![x^n](F_t-F_{t-1})\), with the recurrent
layer given by \(F_0\).  Fixed graphs have EGF

\[
                 F_{\rm fix}(x)=e^{x+C_{\rm even}(x)}.    \tag{8}
\]

Equations (5)--(8) give every finite-size fixed, recurrent, and transient
layer from the classical connected-graph numbers.

## 5. Computational control and claim ceiling

The independent exhaustive scout checks all \(2^{\binom n2}\) labelled
graphs through \(n=6\), including component refinement, orbit period, exact
depth, the recurrent/fixed criteria, indegrees, and the assembly counts.  It
records fixed counts

\[
1,1,2,4,48,216,27920
\]

and recurrent counts

\[
1,1,2,4,48,648,30512
\]

for \(0\le n\le6\).

Graph complementation, connected/co-connected decomposition, labelled SET
assembly, and the connected-graph recurrence are zero-credit background.
The proposed residual is the literal parity-triggered component map together
with the recurrent criterion, sharp clock (1)--(3), and all-depth recursion
(5)--(8).  A bounded exact-map search found no direct owner, but that miss is
not a novelty certificate.

**Internal verdict:** `PROVED / SEND TO HOSTILE OWNER-VALUE GATE`.
