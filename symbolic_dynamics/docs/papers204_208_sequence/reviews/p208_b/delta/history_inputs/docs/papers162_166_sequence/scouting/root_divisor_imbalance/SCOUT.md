# Divisor-imbalance dynamics — exact scout

**Date:** 2026-09-03 UTC  
**Status:** `KILL_EXACT_INTERNAL_X01_DUPLICATE`  
**External state:** `HOLD_EXTERNAL`

## Outcome first

**Post-hostile disposition.**  This dossier is mathematically correct but is
not a live candidate: independent review found that its carrier and literal
update are exactly the permanently killed historical D01/X01 complementary-
divisor tent system.  The derivation below is retained only as negative
evidence; it cannot receive a paper number or serve as a reserve.

Fix (N>1).  On the finite divisor set \(\mathcal D(N)\), define

\[
 \Phi_N(d)=\frac{\operatorname{lcm}(d,N/d)}
                  {\gcd(d,N/d)}
          =\frac{N}{\gcd(d,N/d)^2}.
\]

This literal gcd--lcm imbalance map has a complete functional graph.  If
\(N=\prod_i p_i^{e_i}\) and \(d=\prod_i p_i^{a_i}\), then each coordinate is

\[
 a_i\longmapsto |2a_i-e_i|.                 \tag{1}
\]

After subtracting the static gcd/lcm identity and the classical tent/doubling
semiconjugacy, the candidate contribution is the simultaneous arithmetic
package: exact point and global tails for every prime-exponent box, a closed
fixed/cycle inventory, exact images at every time, and a codomain-wide
arbitrary-time fibre atlas whose endpoint factors differ from its interior
factors.  These are deductive statements; the verifier only attacks them.

## The folded-doubling coordinate

For one exponent (e\ge1), set (x=e-a\), (M=2e\), and

\[
 \operatorname{fold}_M(r)=\min(r\bmod M,M-(r\bmod M)).
\]

The complement of (1) is the full tent map on the rational grid:

\[
 x\longmapsto e-|e-2x|=\operatorname{fold}_{2e}(2x).
\]

Consequently, for every (t\ge0),

\[
 \Phi_e^t(a)=e-\operatorname{fold}_{2e}\bigl(2^t(e-a)\bigr).       \tag{2}
\]

This is the quotient of multiplication by two on \(\mathbb Z/(2e)\) by the
reflection (r\sim-r\).  The proof of every formula below is carried out in
this quotient, including the two reflection-fixed endpoint classes; simply
dividing an ordinary doubling fibre by two would give wrong endpoint counts.

## Theorem contract A — point tails and the complete depth census

Write

\[
 L(e)=\nu_2(2e)=\nu_2(e)+1,\qquad e=2^{L(e)-1}m(e),\quad m(e)\text{ odd}.
\]

With \(\nu_2(0)=+\infty\), the exact tail of (a\in\{0,\ldots,e\}\) is

\[
 \delta_e(a)=\max\{0,L(e)-\nu_2(e-a)\}.                         \tag{3}
\]

The number of points of each exact depth is

\[
 H_e(0)=H_e(1)=\frac{m(e)+1}{2},\qquad
 H_e(r)=2^{r-2}m(e)\quad(2\le r\le L(e)).                       \tag{4}
\]

For (N=\prod_i p_i^{e_i}\), the depth of (d=\prod_i p_i^{a_i}\) is
\(\max_i\delta_{e_i}(a_i)\).  Hence, if
\(C_e(r)=\sum_{j\le r}H_e(j)\), the global exact-depth census is

\[
 \#\{d:\delta_N(d)=r\}=\prod_i C_{e_i}(r)-\prod_i C_{e_i}(r-1). \tag{5}
\]

The sharp global height is

\[
 \max_i L(e_i)=1+\max_i\nu_2(e_i),                              \tag{6}
\]

witnessed by (d=N/p_i\) at a maximizing coordinate.  Thus the clock depends
on the two-adic valuations of the *prime exponents* of (N), not on the
sizes of its prime divisors.

**Proof.**  Under multiplication by two modulo
\(2e=2^{L(e)}m(e)\), exactly (L(e)-\nu_2(x)\) steps are needed to erase the
two-primary component when that number is positive.  Reflection does not
alter that entry time.  The recurrent subgroup has odd order (m(e)), so its
reflection quotient has \((m(e)+1)/2\) classes.  At depth one there are
\(m(e)\) residues of valuation (L(e)-1); negation has the one fixed class
\(e\), giving \((m(e)+1)/2\) classes.  For (r\ge2\), the
\(2^{r-1}m(e)\) residues of valuation (L(e)-r) have no reflection-fixed
class and yield (2^{r-2}m(e)\) quotient points.  Products take the maximum
of coordinate tails, proving (3)--(6).

## Theorem contract B — recurrence and all cycles

For (k\ge1), the number of fixed points of the (k)-th iterate in one
coordinate is

\[
 F_e(k)=\frac{\gcd(2^k-1,m(e))+\gcd(2^k+1,m(e))}{2}.             \tag{7}
\]

Therefore

\[
 \operatorname{Fix}(\Phi_N^k)=\prod_i F_{e_i}(k),\qquad
 \operatorname{Cyc}_N(\ell)=\frac1\ell
 \sum_{k\mid\ell}\mu(\ell/k)\operatorname{Fix}(\Phi_N^k).     \tag{8}
\]

The recurrent set has size \(\prod_i(m(e_i)+1)/2\).

**Proof.**  A reflection class is fixed by the (k)-th doubled map precisely
when \((2^k-1)x=0\) or \((2^k+1)x=0\) modulo the odd recurrent modulus
\(m(e)\).  The two solution sets meet only at zero.  Passing to reflection
classes adds the zero fixed class in Burnside's count and gives (7).  Product
and Möbius inversion give (8).

## Theorem contract C — every-time images and every-target fibres

For (t\ge0\), the local image size is

\[
 I_e(t)=
 \begin{cases}
 e/2^t+1,&0\le t<L(e),\\
 (m(e)+1)/2,&t\ge L(e).
 \end{cases}                                                   \tag{9}
\]

Thus \(|\operatorname{im}\Phi_N^t|=\prod_i I_{e_i}(t)\).

More strongly, fix a target exponent (b\in\{0,\ldots,e\}\), put
\(y=e-b\), and, for (t\ge1\), put \(g=2^{\min(t,L(e))}\).  Its exact local
fibre factor is

\[
 K_{e,t}(b)=
 \begin{cases}
 0,&g\nmid y,\\
 g/2+1,&y=0,\\
 g/2,&y=e,\\
 g,&\text{otherwise}.
 \end{cases}                                                   \tag{10}
\]

The (y=e\) line automatically vanishes when (g\nmid e\).  At (t=0) the
factor is one.  For (b_i=\nu_{p_i}(c)\), every target divisor (c\mid N\)
has

\[
 |(\Phi_N^t)^{-1}(c)|=\prod_i K_{e_i,t}(b_i).                   \tag{11}
\]

**Proof.**  Multiplication by (2^t) on \(\mathbb Z/(2e)\) has kernel size
\(g\) and image the multiples of (g\).  A nonendpoint target reflection
class consists of two residues and hence gives (2g\) residue sources, or
\(g\) reflection classes.  The zero target has (g) residue sources and the
two reflection-fixed sources (0,e\), yielding (g/2+1\).  When present, the
opposite endpoint (e\) has (g) sources and no reflection-fixed source,
yielding (g/2\).  This proves (9)--(11), including fibre mass.

## Exact evidence

`verify_scout.py` independently checks the literal gcd/lcm map, (2)--(11),
pointwise depths, fixed points, images, fibres, and all mass identities.  Its
grid comprises exponents (1\) through (192), times (0\) through (17),
thirteen multi-prime exponent boxes, and twenty literal integers.  The frozen
transcript is `CANONICAL.txt`.

## Claim boundary

- The gcd/lcm product identity, prime-exponent factorization, continuous tent
  map, and its doubling/reflection semiconjugacy receive zero contribution
  credit.
- A bounded search located the exact static expression in OEIS A332618 as a
  summand, but no inspected record iterated this divisor self-map or stated
  the conjunction (3)--(11).  This non-hit is not a novelty or priority claim.
- The candidate remains anonymous and internal.  Independent hostile proof,
  owner, and P1--P161 collision review is mandatory before paper allocation.

That mandatory review has now returned `KILL_EXACT_INTERNAL_X01_DUPLICATE`;
see `phase1/ddi_hostile_gate/HOSTILE_GATE.md`.  The preceding bullet is kept
only as the historical author-side boundary.
