# CT1 primary-source and substance audit

Actual browser access on 2026-09-07. No bibliographic resolver, paid API,
GPU experiment or external manuscript upload was used.

## Search scope

Eight formulations covered p-adic cycle Poincare series, polynomial
automorphism congruence-cycle generating functions, dynamical-zeta
rationality, Denef polynomial congruences, recent p-adic automorphism
rationality (183-day filter), desJardins--Zieve, p-adic orbit counting,
and Poonen interpolation. No relevant new theorem was established by
the recent-date search. Search-engine crawl dates for old PDFs were
not treated as publication dates. Secondary search results were leads,
not theorem evidence.

## Accessed primary inputs

- [Poonen, p-adic interpolation of iterates](https://arxiv.org/pdf/1307.5887),
  original 2013 version: all three pages read, especially Theorem 1 and
  Remarks 3--4. It interpolates coefficientwise sufficiently near-identity
  analytic maps; the threshold is strict. It does not identify an
  arbitrary finite-field permutation with polynomial identity. Our
  finite residue-ball normalization is needed before invocation.
- [Hrushovski--Martin--Rideau, with Cluckers' appendix](https://arxiv.org/pdf/math/0701011),
  version 5 (2017): introduction and the relevant appendix statements
  accessed, not all 89 pages. Appendix A.2 gives fixed-prime subanalytic
  equivalence-class generating-function rationality; the preceding
  paragraph explicitly permits several integer parameters/variables.
  The language allows restricted power series with integral coefficients.
  This is the closest decisive ownership input for the reconstructed
  qualitative CT1 theorem, not merely an analogy with group zeta functions.
- [Nguyen, Uniform rationality of the Poincare series of definable,
  analytic equivalence relations](https://arxiv.org/pdf/1610.07952),
  2016: introduction and Theorems 1.3.1--1.3.2 read. Its displayed uniform
  local-field claims use a sufficiently-large residue-characteristic
  threshold. We do not invoke them to cover $p=2$; the fixed-prime
  Cluckers appendix supplies the applicable statement.
- [desJardins--Zieve, Polynomial mappings modulo an odd prime power](https://arxiv.org/pdf/math/0103046),
  circulated 1994, arXiv 2001: introduction and Section 11 accessed, not
  a full-paper read. Their one-variable cycle-lifting theory is earlier
  ownership. It is not silently promoted to the all-dimensional CT1
  statement. The [author's publication page](https://sites.lsa.umich.edu/zieve/publications/)
  independently identifies this work and its scope.

Denef's 1984 paper was located at the CNRS-hosted original PDF, which
initially returned metadata and an excerpt; subsequent full accesses
timed out. EuDML access returned 403. No full Denef-paper read is claimed.
The proof does not rely on pretending those failed accesses succeeded:
the applicable later fixed-$p$ primary theorem was actually read.

## Residual and verdict

The [proof triage](PROOF_PACKAGE.md) encodes exact ordinary period
divisibility as a two-parameter subanalytic congruence condition. Its
rationality then follows from the cited machinery and Mobius inversion.
That is a coordinator inference from the sources, not a theorem title
found verbatim in them. The finite-jet/effectivity component remains
unspecified for arbitrary $p$-adic coefficients.

**NOT ADMITTED: CLASSICAL RECONSTRUCTION / EFFECTIVITY NOT CLOSED.**
We do not claim CT1 is false, globally unpublished, or an arithmetic
Euler-factor bridge. Neither a rational tower series nor its ordinary
clock establishes target Euler factors, root numbers or a zero divisor.
