# Research Question

## Frozen object

Let \(u\) be the unique real root of

\[
Q(U)=U^3-2U^2+2U-2
\]

and set \(g(z)=z^2-u\).  Equivalently, in the usual quadratic family
\(g_c(z)=z^2+c\), the parameter \(c=-u\) satisfies
\(c^3+2c^2+2c+2=0\).  The critical orbit is

\[
0\mapsto-u\mapsto a=u^2-u\mapsto-a\mapsto-a,
\]

so the parameter is PCF of type \((3,1)\).  It is inherited verbatim from
Paper 2 of Batch 01 and may not be retuned.

For an exact period-\(n\) cycle \(C=(z_0,\ldots,z_{n-1})\), write

\[
\Lambda_C=(g^n)'(z_0)=2^nB_C,
\qquad B_C=\prod_{j=0}^{n-1}z_j.
\]

## Primary question

What exact restriction does the unique prime above \(2\) impose on all
higher-period multipliers of this frozen map?

The theorem-level answer sought and frozen here is

\[
n\ge2\quad\Longrightarrow\quad
w(\Lambda_C)=n\,w(2)
\]

for every extension \(w\) of the parameter's 2-adic valuation to a cycle
field.  In particular,

\[
\Lambda_C\in\mathbb Q
\quad\Longrightarrow\quad
\Lambda_C=2^n m,\qquad m\in2\mathbb Z+1.
\]

## Residual equality question

The inherited exponent-prime boundary is

\[
\Lambda_C\in\mathbb Q,qquad |\Lambda_C|=2^n,
\]

equivalently \(B_C=\pm1\).  This paper does **not** assume that the valuation
theorem decides that equality.  It asks what exact necessary conditions can
be proved and audits the equality through a finite, development-seen cutoff.

## Semantic separations

- Rational equality: \(\Lambda_C=\pm2^n\).
- Complex modulus only: \(|\Lambda_C|=2^n\) without rationality.  This is
  outside the arithmetic equality certificate.
- Characteristic exponent:
  \(\chi_C=n^{-1}\log|\Lambda_C|\).  The equation
  \(\chi_C=\log2\) is equivalent to the modulus-only predicate and is not
  excluded here.
- A repeated orbit creates no new rational base-2 target only under the
  separately proved local root-of-unity condition; primitive and repeated
  predicates may not otherwise be conflated.

## Frozen claims

1. A standard local lemma for \(f(z)=z^2+c\) with \(0<|c|<1\) forces every
   exact cycle of period at least two onto the unit circle and hence onto the
   sharp multiplier boundary \(|\Lambda|=|2|^n\).
2. The frozen cubic is 2-Eisenstein.  The local lemma therefore gives exact
   valuation at every cycle-field place over two and an odd normalized
   quotient for every rational multiplier.
3. Every local cycle is the unique Hensel lift of a Frobenius cycle; its
   normalized multiplier is the corresponding unramified norm.
4. Reduction modulo \(2\) gives a two-coefficient necessary condition for
   \(B_C=\pm1\), which excludes periods two and three exactly but is known to
   be insufficient from period four onward.
5. An exact audit through period seven may falsify the frozen formulas and
   document finite equality absence, but it cannot close the all-period
   equality question.

## Mandatory nonclaims

- No all-period exclusion of \(\Lambda_C=\pm2^n\).
- No conclusion for nonrational multiplier modulus alone.
- No all-PCF or all-quadratic rigidity theorem.
- No prime-orbit correspondence, prime spectrum, zeta-zero statement,
  quantization, Hilbert--Polya claim, Route-A advance, or Route-B opening.
- No claim that a finite null ledger is blind, prospective, or theorem-level.

