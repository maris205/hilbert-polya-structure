# Paper 21 — Successor–Divisor Cycle Flood

**Candidate:** SD-C23
**Primary family:** Symbolic Dynamics only
**Title:** *The Successor–Divisor Shift: A Sharp Trace-Class Determinant with an All-Length Primitive-Cycle Flood*
**Status:** exact positive construction plus a scoped Route-A rejection
**Target-zero data:** none
**Route B:** locked

## One-paragraph result

Starting only from alphabet successor and tensor factorization of full shifts,
SD-C23 freezes the countable Markov graph

\[
 n\longrightarrow d
 \quad\Longleftrightarrow\quad
 d\ge2,\qquad d\mid n+1.
\]

The graph is strongly connected and mixing.  For every \(k\ge2\), it contains
the simple primitive cycle

\[
 C_k=(k,k+1,\ldots,2k-1).
\]

Every length-\(r\) closed walk is confined to the finite window
\(\{2,\ldots,2r-1\}\), with the extremal walk uniquely \(C_r\) up to rotation.
For the natural endpoint weight \((nd)^{-s}\), the whole weighted adjacency
satisfies the sharp theorem

\[
 L_s\in\mathcal S_1
 \quad\Longleftrightarrow\quad
 \operatorname{Re}s>\frac12.
\]

Thus SD-C23 has a genuine same-object Fredholm determinant across the open
half-plane to the right of the critical line.  It nevertheless fails the
Riemann Euler target before any zero calculation: the graph has no loops, so
\(\operatorname{Tr}L_s=0\), whereas the marked prime Euler determinant has
first trace \(\sum_p p^{-s}\).  Every natural orbit norm is also a composite
square.

## Strongest advances

1. **Genuine recurrence.**  Unlike the transient verifier constructions,
   arithmetic changes recurrent transitions among all nonunit full-shift
   objects.
2. **Exact finite confinement.**  Infinite-graph traces of order \(r\) are
   certified by the induced prefix through \(2r-1\).
3. **Sharp operator theorem.**  A row-nuclear decomposition proves trace class
   for \(\operatorname{Re}s>1/2\); Fourier extraction of the successor
   superdiagonal proves necessity.
4. **Exact obstruction.**  Simple primitive cycles occur at every length
   \(k\ge2\), the first marked trace vanishes, and the natural orbit norms are
   composite squares.
5. **Selective control failure.**  The pruned quotient spine
   \(q\in\{1,2\}\) retains strong connectivity, mixing, all canonical cycles,
   and the same sharp trace-class threshold.

## First trace ledger

\[
\operatorname{Tr}L_s=0,
\qquad
\operatorname{Tr}L_s^2=2\,6^{-2s},
\qquad
\operatorname{Tr}L_s^3=3\,60^{-2s},
\]

\[
\operatorname{Tr}L_s^4
=2\,6^{-4s}+4\,120^{-2s}+4\,840^{-2s}.
\]

Primitive rotations and temporal repetitions are kept separate throughout.

## Exact certificate snapshot

The frozen exact suite records:

- **19/19 tests passed**, with no failures, skips, target-zero data, or
  forbidden source calls;
- **32 exact unweighted trace orders**, ending at
  \(T_{32}=14{,}532{,}674\) and \(P_{32}=454{,}021\);
- **667 explicit primitive rotation classes** through length \(16\);
- **48 exact weighted traces** and **51 determinant coefficients**, with zero
  mismatch between the Newton recurrence and independent primitive-factor
  multiplication;
- a **30,626-edge source audit** with zero quotient mismatch and zero loops;
- **225 quotient-family**, **20 graph-control**, **64 positive-weight**, and
  **56 trace-class diagnostic** rows.

Two complete regeneration runs produced the identical frozen results ledger:

    10ed2d1409b9de69b16a3a11244660f666dfcd52207bca6b9945e4126a01cc6a

These artifacts are exact regressions of the analytic proofs.  Floating
prefixes are used only as trace-class diagnostics and do not decide the
\(\operatorname{Re}s=1/2\) threshold.

## Strict route decision

\[
\begin{aligned}
(&\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\\
 &\mathrm{A1\_WEAK},\\
 &\mathrm{A2\_ANALYTIC\_DETERMINANT},\\
 &\mathrm{A3\_FAIL},\\
 &\mathrm{A4\_FAIL}).
\end{aligned}
\]

Overall:

\[
\mathrm{ROUTE\_A\_REJECTED}.
\]

Stop labels:

- STOP_PRIME_ORBIT_LEDGER;
- CYCLE_FLOOD;
- PRUNING_PERSISTS;
- PROVES_TOO_MUCH;
- STOP_SCOPED;
- ROUTE_B_LOCKED.

The A2 label certifies the determinant of the frozen symbolic object.  It does
not assert that this determinant matches the Riemann target.  A3 fails because
no functional equation, Gamma factor, completed divisor, Riemann–von Mangoldt
law, or Weil compression is derived.

## Claim boundary

This project proves the graph, cycle, confinement, trace-class, trace,
determinant, and pruning theorems recorded above.  It does not prove an
identity with \(1/\zeta(s)\), analytic continuation to the critical line, an
explicit formula, RH, or a Hilbert–Pólya operator.

## Shareable paper

The shareable manuscript is main.pdf.  Its modular LaTeX sources are
main.tex, math_commands.tex, the sections directory, the figures directory,
and references.bib.

## Next smallest symbolic task

Paper22 should expose the unique quotient \(q=(n+1)/d\) on edge symbols and
classify relabel-natural finite-state quotient filters or same-object
cocycles.  The memoryless positive case is already blocked: retaining
\(q=1\) and any \(q\ge2\) creates the simple cycles

\[
 C_{d,q}=(d,d+1,\ldots,qd-1)
\]

of length \(d(q-1)\).  Any proposed cancellation must therefore be verified
coefficientwise at the trace level and must not move unwanted cycles between
unreported blocks.
