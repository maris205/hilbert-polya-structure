# Preregistration — SD-C24

**Freeze date:** 2026-08-14  
**Candidate:** SD-C24  
**Primary family:** Symbolic Dynamics  
**Zero-data firewall:** active  
**Review loop:** excluded by project instruction

## 1. Research question

Does the source-intrinsic cofactor label

\[
 q(n,d)=\frac{n+1}{d}
\]

on the successor–divisor shift create a holonomy or character-resolved
Fredholm ledger that is arithmetically selective enough to improve the
prime-orbit obstruction found in Paper21?

## 2. Frozen candidate

\[
 V=\{2,3,\ldots\},
 \qquad
 n\to d\iff d\ge2,\ d\mid n+1,
\]

\[
 L_{s,u}e_n
 =\sum_{d\mid n+1,\ d\ge2}
   (nd)^{-s}\left(\frac{n+1}{d}\right)^{-u}e_d.
\]

The graph, cofactor, two roofs, function space, column-source convention,
group completion, character normalization, and determinant convention are
fixed before any comparison with the target Euler ledger.

## 3. Primary hypotheses

**H1 — positive holonomy.**  Every closed path satisfies

\[
 Q(\gamma)=\prod_j\left(1+\frac1{n_j}\right)\in\{2,3,\ldots\}.
\]

**H2 — neutral-sector extinction.**  The regular group extension has no
periodic path and every identity-holonomy trace coefficient vanishes.

**H3 — gauge decomposition.**  The cofactor cocycle is cohomologous to the
source potential \(1+1/n\), with only the imaginary-power gauges giving
automatic bounded unitary equivalence.

**H4 — exact first class.**  \(Q=2\) holds exactly on

\[
 C_k=(k,k+1,\ldots,2k-1),\qquad k\ge2,
\]

up to rotation, with one primitive orbit at each length.

**H5 — atomic classes.**  For a multiplicative atom \(p\), \(Q=p\) holds
exactly on \(C_{k,p}=(k,\ldots,pk-1)\), and repetitions do not enter this
class.

**H6 — exact connected coefficient.**  Haar extraction from the character
family returns the holonomy class of the trace logarithm; in particular,

\[
 \mathcal H_2(s,z)=
 \sum_{k\ge2}z^k
 \left(\frac{(2k-1)!}{(k-1)!}\right)^{-2s}.
\]

**H7 — sharp two-parameter nuclear domain.**  With
\(\sigma=\Re s\) and \(a=\Re u\),

\[
 L_{s,u}\in\mathcal S_1
 \iff
 \sigma>\frac12
 \quad\text{and}\quad
 \sigma+a>\frac12.
\]

**H8 — lift distinction.**  The regular lift is semifinite \(L^1\) exactly
for \(\Re s>1/2\) but is not ordinarily compact; the neutral local
semifinite determinant is one.

**H9 — Fredholm trilemma.**  Pure cofactor weight, honest endpoint Fredholm
regularity, and length selectivity cannot be obtained simultaneously from
the frozen abelian product cocycle.

**H10 — control persistence.**  First-return induction and every positive
inventory preserve the infinite canonical support.

All ten hypotheses are theorem-level claims.  Finite computation is an audit
only.

## 4. Evidence and coefficient conventions

Closed directed paths are quotiented by cyclic rotation only.  A primitive
orbit is not a positive temporal power.  The rooted group-algebra trace is

\[
 \mathcal T_r(s)=
 \sum_{\gamma\in\operatorname{Fix}_r}
 N(\gamma)^{-2s}[Q(\gamma)],
\]

and the connected ledger is

\[
 \mathscr L_s(z)=\sum_{r\ge1}\frac{z^r}{r}\mathcal T_r(s).
\]

Holonomy coefficients are extracted from \(\mathscr L_s=-\log D\), not from
the determinant itself.  This freezes the primitive/repetition bookkeeping
and prevents products of unrelated primitives from masquerading as one
holonomy class.

## 5. Analytic tests

The sufficiency proof must use the exact output-row decomposition

\[
 R_d=\sum_{q\ge q_0(d)}
 [d(dq-1)]^{-s}q^{-u}E_{d,dq-1},
\]

where \(q_0(2)=2\) and \(q_0(d)=1\) for \(d\ge3\).  It must establish

\[
 \|R_d\|_1^2
 =\sum_{q\ge q_0(d)}
 d^{-2\sigma}(dq-1)^{-2\sigma}q^{-2a}
 \asymp d^{-4\sigma}
\]

precisely when \(\sigma+a>1/2\), followed by summation in \(d\).

Necessity must use two independent witnesses:

1. the fixed output row \(d=2\), which is not in \(\ell^2\) if
   \(\sigma+a\le1/2\);
2. contractive Fourier extraction of the \(q=1\) successor diagonal, whose
   trace norm is
   \(\sum_{n\ge2}[n(n+1)]^{-\sigma}\).

Neither boundary may be inferred from a finite numerical plot.

## 6. Exact finite audit protocol

On induced prefixes \(V_N=\{2,\ldots,N\}\):

1. construct edges only from \((n+1)\bmod d=0\);
2. compute \(q=(n+1)/d\) by exact division;
3. enumerate simple cycles and verify
   \(Q=\prod q=\prod(n+1)/n\) using exact arithmetic;
4. certify that every \(Q=2\) cycle is a rotation of \(C_k\);
5. post-freeze, audit atomic classes \(p\in\{2,3,5,7\}\);
6. propagate sparse group-algebra trace dictionaries at fixed periods and
   verify the exact \([1]\) and \([2]\) formulas;
7. reconstruct those finite coefficients from a nonaliasing character grid;
8. verify the gauge formula on finite windows;
9. audit the two independent trace-class boundary mechanisms;
10. compare pure-cofactor and endpoint-regularized return diagonals without
    identifying them.

No prime test may affect graph construction.  No zero table may be loaded.

## 7. Controls

The frozen inventory controls are

\[
 \mu(n)\in
 \left\{
 n, n+1, n^2+n, n^2+1, 2^n,
 n+\frac{1+((37n+11)\bmod97)}{97}
 \right\}.
\]

Every control must preserve the \(Q=2\) support and may change only its
positive magnitudes.  A transported presentation control must transport
successor and tensor together.  Cancellation across different holonomy
classes is not a selector.

## 8. Stop conditions

Stop the abelian product-holonomy branch once all of the following are
proved:

- the neutral sector removes every recurrent orbit;
- all characters retain the canonical \(Q=2\) spine;
- pure cofactor weight is non-Fredholm at the whole-operator level;
- endpoint regularization gives factorial, not logarithmic-prime, roofs;
- every atomic holonomy has infinitely many representatives \(C_{k,p}\);
- arbitrary positive inventories preserve the support.

Every stop condition fires.

## 9. Frozen route tuple

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

No zero search, continuation experiment, review loop, or Route-B
construction is authorized after this verdict.
