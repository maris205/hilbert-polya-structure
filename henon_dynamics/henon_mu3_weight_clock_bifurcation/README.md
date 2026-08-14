# HCS-C51: weight--clock bifurcation in Hénon moments

Status: **mathematical package and manuscript in preparation; release provenance pending**

Implementation commit: PENDING_RELEASE_COMMIT.

## Main result

HCS-C51 asks whether the cohomological packets extracted from the second,
third, and fourth chronological Hénon moments admit one source-native
completion with a common functional-equation center.  The exact answer
bifurcates.

For \(n=2,3,4\), let \(S_n\) be the Fermat cubic hypersurface and let
\(X_n\) be the source-ordered \((2,3)\) complete intersection produced by
the genuine \(2n\)-step Hénon phase.  At every good split prime define

\[
 E_n=\mathbf Q_\ell(0)\oplus
 H^{2n-2}_{\mathrm{prim}}(S_n)(n-1),\qquad
 O_n=H^{2n-3}(X_n)(n-2).
\]

The packets \(E_n\) and \(O_n\) have weights zero and one, respectively,
and their Frobenius traces satisfy

\[
 C_{p,n}=-2\left(
 \operatorname{Tr}(F_p\mid E_n)+\operatorname{Tr}(F_p\mid O_n)
 \right).
\]

For any smooth member of this complete-intersection family,

\[
 \operatorname{rank}E_n=\frac{4^n+5}{3},\qquad
 \operatorname{rank}O_n=\frac{2(4^n-4)}{3},\qquad
 \operatorname{rank}(E_n\oplus O_n)=4^n-1.
\]

The Hénon applications are restricted to \(n=2,3,4\), where C48--C50
supply smoothness outside finite bad sets.  The formula for larger \(n\)
is a conditional smooth-complete-intersection identity, not an all-\(n\)
smoothness assertion.

## Exact logarithmic extraction

With

\[
 \ell_n(s)=\sum_{p\equiv1\;(\mathrm{mod}\;3)}c_{p,n}p^{-ns},
 \qquad
 F_n(s)=\exp\!\left(-\frac{\ell_n(s)}{n}\right),
\]

one has, initially for \(\Re s>1/(2n)\),

\[
 F_n(s)=
 \exp\!\left(\frac{2}{n}\operatorname{Log}_0
 L_K^{(S)}(E_n\oplus O_n,ns+1)\right)H_{n,S}(s),
\]

where \(S\) is the frozen finite set of rational primes that ramify in
\(K\) or belong to the inherited source-defined bad-reduction sets, and
\(H_{n,S}\) is holomorphic and
nonzero on \(\Re s>0\).  For
\(n=3,4\), the exponents \(2/3\) and \(1/2\) denote canonical
origin-normalized logarithmic germs.  They are not asserted to be
meromorphic roots or ordinary finite-rank determinants.

The exact denominator expansion

\[
 \frac{1}{p-1}=\sum_{j\ge1}p^{-j},\qquad u_{n,j}=ns+j
\]

maps a pure weight-\(w\) standard center to

\[
 s_{n,j}(w)=\frac{(w+1)/2-j}{n}.
\]

Thus the leading odd rail, \(w=1\) and \(j=1\), aligns at \(s=0\).
The leading even rails lie at

\[
 -\frac14,\qquad-\frac16,\qquad-\frac18.
\]

Higher denominator terms move the odd centers to \(-(j-1)/n\), so the
full tower has no common factorwise standard pure-motive center.
Consistent Tate twisting, including a formal half twist, leaves these
mapped centers invariant.

The fractional leading roots cannot be realized by a **semisimple direct
source-native \(K\)-compatible system preserving the same split-prime
trace and the \(E_n/O_n\) weight decomposition**: at \(n=3\) the
required weightwise ranks are \(46/3\) and \(80/3\), and at \(n=4\) the
required total rank is \(255/2\).
This scoped obstruction does not exclude restriction of scalars,
Galois-orbit counterpackets, or normalized semifinite determinants.
Indeed, restriction from \(K\) to \(\mathbf Q\) removes the bare
\(n=4\) parity obstruction by doubling rank, although it changes the
object and prime organization; the doubled \(n=3\) ranks remain
\(92/3\) and \(160/3\).

## Positive survivor and next gate

After clearing denominators, the leading odd skeleton

\[
 \mathcal O_6(s)=
 \Lambda(O_2,2s+1)^6
 \Lambda(O_3,3s+1)^4
 \Lambda(O_4,4s+1)^3
\]

has the single expected reflection \(s\mapsto-s\).  Only the \(n=2\)
factor has a proved continuation and functional equation in this
package.  The \(n=3,4\) entries are a motivic expected-center ledger,
not theorems about their full Hasse--Weil functional equations.

For \(n=4\), the twisted middle Hodge types are

\[
 O_4:\quad
 (2,-1)^1+(1,0)^{83}+(0,1)^{83}+(-1,2)^1.
\]

Consequently \(O_4\) is not itself the \(H^1\) of an abelian variety.
HCS-C52 must construct or obstruct a \(K\)-rational algebraic projector
whose realizations are \(\ell\)-compatible and which separates the
rank-two extreme piece from the rank-166 level-one piece.

## Route A

The evaluator-compatible tuple is

\[
 (\mathrm{A1\_WEAK},
  \mathrm{A2\_ANALYTIC\_DETERMINANT},
  \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
  \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Overall status: **ROUTE_A_EXPLORATORY**.  HCS-C51 inherits C50's
holomorphic continuation to \(\Re s>1/5\) and its normalized-semifinite
\(\operatorname{Det}_{10}\) realization.  It does not improve that
half-plane, construct a full Hénon archimedean completion, prove a full
Hénon functional equation, identify a Riemann divisor, or produce a
self-adjoint Hilbert--Pólya generator.  Route B is not authorized.

## Project files

- RESEARCH_QUESTION.md states the locked question and kill gates.
- THEOREM_PACKAGE.md records the exact theorem and scope boundaries.
- DERIVATION_PACKAGE.md and PROOF_PACKAGE.md give the calculation and proof.
- SOURCE_AUDIT.md separates inherited theorems, standard facts, and the new
  source-locked synthesis.
- METHODOLOGY_BLUEPRINT.md and EXPERIMENT_PLAN.md specify reproducible checks.
- NARRATIVE_REPORT.md and PAPER_PLAN.md map results to the manuscript.
- INTEGRITY_REPORT.md records proof, source, checker, and PDF scope.
- route_a_evaluation.yaml and its archive copy carry the Route-A decision.
- paper/ contains the manuscript; its PDF remains preliminary until the
  code/results provenance freeze.
