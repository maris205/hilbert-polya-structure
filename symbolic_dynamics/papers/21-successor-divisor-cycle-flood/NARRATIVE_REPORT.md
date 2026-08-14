# Narrative Report — SD-C23

## One-sentence contribution

The successor–divisor countable Markov shift is genuinely recurrent and has a
sharp trace-class Fredholm determinant for
\(\operatorname{Re}s>1/2\), but an exact finite-window theorem exposes a
primitive-cycle flood that rules out the Riemann Euler ledger at its first
marked coefficient.

## The question inherited from Paper20

The previous two projects isolated a structural dilemma.  A complete
arithmetic verifier can create the desired support, but transient computation
is determinant-invisible.  Forcing the verifier to recur introduces long
computation clocks and destroys compactness.  The next honest move was to
remove the accept-loop architecture and let the local semiring relation itself
generate recurrent transitions.

The full-shift skeleton contains addition by one and multiplication of
alphabet cardinalities:

\[
 F_{n+1}\cong F_d\boxtimes F_q
 \quad\Longleftrightarrow\quad
 n+1=dq.
\]

Using every nonunit factor produces the successor–divisor graph

\[
 n\to d\iff d\mid n+1,\ d\ge2.
\]

This construction is source-intrinsic.  It does not decide primality before
the dynamics begin.

## The positive result

The graph is more dynamically coherent than the verifier candidates.
Every vertex reaches \(2\) in at most two steps, and successor edges reach
every vertex from \(2\).  The graph is therefore strongly connected.

The same two local mechanisms create canonical cycles:

\[
 C_k=(k,k+1,\ldots,2k-1).
\]

Successor edges traverse the interval, and the last vertex returns to \(k\)
because \(k\mid2k\).  Cycles of lengths two and three imply period one, so the
countable Markov shift is mixing in the path sense.

The key new estimate is finite confinement.  At the maximal vertex \(M\) of a
length-\(r\) closed walk, the next vertex is a proper divisor
\(d\le(M+1)/2\).  Since subsequent edges increase a vertex by at most one,
returning to \(M\) in \(r-1\) steps forces

\[
 M\le2r-1.
\]

Equality forces the canonical cycle.  Infinite-graph traces at fixed order
are consequently finite combinatorial sums with a certified cutoff.

## The analytic advance

The natural endpoint roof is

\[
 \tau(n,d)=\log n+\log d,
\]

and the weighted adjacency is

\[
 L_s e_n
 =
 \sum_{d\mid n+1,\ d\ge2}(nd)^{-s}e_d.
\]

Rows indexed by \(d\) have sources \(kd-1\).  Their rank-one nuclear norms are
bounded by a constant times \(d^{-2\sigma}\), where
\(\sigma=\operatorname{Re}s\).  Summing rows proves trace class for
\(\sigma>1/2\).

The converse is equally intrinsic.  Fourier extraction of the first
superdiagonal selects the successor weighted shift with singular values
\([n(n+1)]^{-\sigma}\).  Trace class of \(L_s\) would imply summability of
these values, which holds only for \(\sigma>1/2\).  The half-plane is exact.

This yields a holomorphic whole Fredholm determinant

\[
 D_{\rm SD}(s,z)=\det(I-zL_s)
\]

and a same-object primitive/repetition ledger.

## Why the candidate still fails

The positive dynamical and analytic properties are not selective.  There is
no loop because \(n\nmid n+1\), hence

\[
 \operatorname{Tr}L_s=0.
\]

The marked Riemann Euler determinant

\[
 \prod_p(1-zp^{-s})
\]

has first trace \(\sum_pp^{-s}\), which is positive for real \(s>1\).
The two germs cannot agree.

The roof adds a second obstruction.  Around a closed orbit \(\gamma\), the
edge weights multiply to

\[
 N(\gamma)^{-2s},
\qquad
 N(\gamma)=\prod_{v\in\gamma}v.
\]

Every orbit contains at least two vertices greater than one, so
\(N(\gamma)\) is composite and the natural orbit norm \(N(\gamma)^2\) is a
composite square.

## The control that settles selectivity

Retain only successor edges \(q=1\) and midpoint returns \(q=2\).  This pruned
spine remains strongly connected, mixing, and trace class on the same sharp
half-plane.  It also retains every \(C_k\).  The full divisor inventory is
therefore unnecessary for the decisive signal.

The control margin is zero.  The construction proves too much: a tiny
two-quotient grammar already generates the cycle flood.

## Strict interpretation

SD-C23 is not a failed determinant construction.  Its determinant theorem is
one of the strongest analytic results in the Session.  It is a failed
prime-orbit construction.  The correct synthesis is:

\[
\text{source-intrinsic recurrence}
\quad+\quad
\text{sharp trace-class determinant}
\quad-\quad
\text{arithmetic selectivity}.
\]

That distinction supports

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL})
\]

and

\[
\mathrm{ROUTE\_A\_REJECTED}.
\]

## The next symbolic move

Paper22 should expose quotient labels \(q=(n+1)/d\) and classify finite-state
transition filters or same-object cocycles.  A memoryless positive filter is
already blocked: retaining \(q=1\) and any \(q\ge2\) creates

\[
 C_{d,q}=(d,d+1,\ldots,qd-1)
\]

at every length \(d(q-1)\).  The next paper must therefore prove a finite-state
no-go or exhibit coefficientwise cancellation without hiding cycles in
unreported blocks.
