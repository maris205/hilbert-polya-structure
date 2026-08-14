# Preregistration — SD-C23

**Freeze date:** 2026-08-14
**Candidate:** SD-C23
**Primary family:** Symbolic Dynamics
**Zero-data firewall:** active
**Review loop:** excluded by project instruction

## 1. Research question

Can the local full-shift-semiring relation

\[
 F_{n+1}\cong F_d\boxtimes F_q
\]

produce a recurrent countable Markov shift with a natural primitive/repetition
ledger and a trace-class determinant that is selective enough for the
Riemann Euler target?

## 2. Frozen candidate

\[
 V=\{2,3,\ldots\},
\]

\[
 n\to d
 \quad\Longleftrightarrow\quad
 d\ge2,\ d\mid n+1,
\]

\[
 L_s e_n
 =
 \sum_{\substack{d\ge2\\d\mid n+1}}
 (nd)^{-s}e_d.
\]

No edge, weight, cutoff, or parameter may be changed after comparison with
the target.

## 3. Primary hypotheses

**H1 — recurrence.**  The graph is strongly connected.

**H2 — aperiodicity.**  The graph has period one and is path-sense
topologically mixing.

**H3 — canonical flood.**  For every \(k\ge2\),

\[
 C_k=(k,k+1,\ldots,2k-1)
\]

is a simple primitive cycle.

**H4 — exact confinement.**  Every length-\(r\) closed walk has maximal
vertex at most \(2r-1\); equality identifies \(C_r\) up to rotation.

**H5 — sharp nuclear domain.**

\[
 L_s\in\mathcal S_1
 \quad\Longleftrightarrow\quad
 \operatorname{Re}s>\frac12.
\]

**H6 — exact trace stabilization.**  The induced prefix through \(2r-1\)
has the exact infinite trace of order \(r\).

**H7 — target rejection.**  The marked determinant differs from the prime
Euler determinant already in degree one.

**H8 — pruning control.**  The \(q\in\{1,2\}\) spine preserves the decisive
cycle and trace-class obstructions.

All eight hypotheses are theorem-level statements in the proof package.
Finite computations are regressions.

## 4. Primitive and repetition conventions

Closed paths are directed.  Cyclic rotations are identified; reflections are
not.  A primitive class is not a positive temporal power of a shorter class.
If \(T_r\) counts rooted length-\(r\) closed walks and \(P_r\) counts primitive
rotation classes, the frozen ledger is

\[
 T_r=\sum_{d\mid r}dP_d,
\]

\[
 P_r=\frac1r\sum_{d\mid r}\mu(r/d)T_d.
\]

Signed or complex weights may not be replaced by absolute values in a trace
identity.  SD-C23 itself uses positive endpoint weights on real \(s\).

## 5. Determinant convention

\[
 D_{\rm SD}(s,z)=\det(I-zL_s)
\]

on \(\operatorname{Re}s>1/2\).  The target is

\[
 D_{\mathbb P}(s,z)=\prod_p(1-zp^{-s})
\]

on \(\operatorname{Re}s>1\).  The marked \(z\)-parameter is mandatory.
Comparing only the specialization \(z=1\) is insufficient.

## 6. Exact finite protocol

For every order \(1\le r\le64\):

1. form the induced sparse graph on \(2,\ldots,2r-1\);
2. propagate exact integer path counts;
3. compute \(T_r\);
4. recompute at cutoffs \(2r\) and \(4r\);
5. require exact stabilization;
6. recover \(P_r\) by Möbius inversion;
7. check the forward recurrence.

Cartesian enumeration of all \(N^r\) words is forbidden.

For exact weighted tests, use integer \(s=1,2,3\) and rational arithmetic
through order \(16\).  Check determinant coefficients independently from:

- the exponential/Newton recurrence on traces;
- multiplication of primitive factors through the same order.

## 7. Trace-class diagnostics

At

\[
 \sigma\in
 \{0.49,0.50,0.51,0.55,0.60,0.75,1.00,1.50\},
\]

record row-nuclear lower prefixes and successor-shift trace-norm prefixes at
dyadic cutoffs.  These plots are diagnostic only.  Slow growth just above
\(1/2\) is compatible with convergence because
\(\sum d^{-1.02}\) converges very slowly.

The analytic proof, rather than a finite plot, decides H5.

## 8. Controls

Run the same closed-walk census for:

1. the full graph;
2. the \(q\in\{1,2\}\) spine;
3. the successor-only \(q=1\) graph;
4. quotient inventories \(Q=\{1,q\}\);
5. positive vertex inventories \(n,n+1,n^2+1,2^n\).

The positive inventories are weight controls only.  The spine is the
arithmetic-graph selectivity control.

## 9. Source firewall

The source layer may call only:

- integer successor;
- divisor enumeration of \(n+1\);
- multiplication and equality;
- full-shift alphabet cardinality and entropy.

The source layer must contain no prime list, primality predicate, von Mangoldt
table, Riemann zeros, or target-fitted parameter.

## 10. Stop conditions

Stop SD-C23 and lock Route B once any of the following is proved:

- \(\operatorname{Tr}L_s=0\) while the target first trace is nonzero;
- primitive cycles occur at every length;
- all natural orbit norms are composite squares;
- the simpler spine preserves the obstruction;
- control margin is zero for the claimed arithmetic signal.

Every listed stop condition fires.

## 11. Frozen route tuple

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}).
\]

\[
\mathrm{ROUTE\_A\_REJECTED}.
\]

No zero search, continuation experiment, or Route-B construction is
authorized after this verdict.
