# Proof package

## 1. Frozen H6 object

Let

\[
H_6(q,p)=(1-6q^2-p,q)
\]

be restricted to the compact mixing four-state hyperbolic survivor certified
in HCS-C31.  Write

\[
\tau=\log J^u,
\qquad
\widehat\tau=h_*\tau,
\qquad
P(-h_*\tau)=0,
\qquad
0.277980<h_*<0.277987.
\tag{1.1}
\]

The roof is positive, Hölder and non-lattice.  If \(\gamma\) is a primitive
orbit, set

\[
\ell_\gamma=S_{m(\gamma)}\tau=\log\Lambda_\gamma,
\qquad
\widehat\ell_\gamma=h_*\ell_\gamma.
\tag{1.2}
\]

HCS-P53 attaches the Mahler spectral height

\[
\mathcal H_\gamma=\log M(f_\gamma)>0
\tag{1.3}
\]

and proves, initially for

\[
\Re s>\sigma_0
=\frac{\log(2\phi)}{h_*\log J_*}
<3.125207,
\tag{1.4}
\]

the all-orbit Abel amplitude

\[
\mathcal A(s)=\frac3{\pi^2}
\sum_\gamma \mathcal H_\gamma e^{-s\widehat\ell_\gamma}.
\tag{1.5}
\]

The objective is not to assert a continuation of (1.5), but to determine
exactly which summand already has a pressure-critical theorem.

## 2. Physical/Galois decomposition

For an embedding of the trace field, choose from each reciprocal pair a root
\(\rho\) with \(|\rho|\ge1\).  HCS-P53 proves

\[
\mathcal H_\gamma=\sum_{\rho}\log|\rho|.
\tag{2.1}
\]

One pair is the physical real unstable pair and contributes
\(\ell_\gamma=\log\Lambda_\gamma\).  Define

\[
\mathcal E_\gamma
:=\mathcal H_\gamma-\ell_\gamma
=\sum_{\rho\ \mathrm{nonphysical}}\log|\rho|.
\tag{2.2}
\]

### Proposition 2.1 (canonical Galois-excess splitting) — **PROVED**

For every primitive H6 orbit,

\[
\boxed{\mathcal H_\gamma=\ell_\gamma+\mathcal E_\gamma},
\qquad
\mathcal E_\gamma\ge0.
\tag{2.3}
\]

Consequently, in the common domain of absolute convergence,

\[
\mathcal A(s)=\mathcal A_{\rm phys}(s)+\mathcal A_{\rm Gal}(s),
\tag{2.4}
\]

where

\[
\mathcal A_{\rm phys}(s)=\frac3{\pi^2}
\sum_\gamma \ell_\gamma e^{-s\widehat\ell_\gamma},
\qquad
\mathcal A_{\rm Gal}(s)=\frac3{\pi^2}
\sum_\gamma \mathcal E_\gamma e^{-s\widehat\ell_\gamma}.
\tag{2.5}
\]

#### Proof

Equation (2.1) is a sum of nonnegative terms.  Isolate the physical
reciprocal pair and call the remaining sum \(\mathcal E_\gamma\).  This gives
(2.3), and termwise substitution in the P53 half-plane gives (2.4). \(\square\)

## 3. The physical pressure pole

Define the entropy-one suspension zeta

\[
\zeta_{\widehat\tau}(s)
=\prod_{\gamma\ \mathrm{primitive}}
\left(1-e^{-s\widehat\ell_\gamma}\right)^{-1}.
\tag{3.1}
\]

The base SFT is mixing and the normalized roof is positive, Hölder and
non-lattice, hence its suspension is weak mixing.  Parry--Pollicott,
Theorem 6.3 and Corollary 6.3.1, give a nonzero meromorphic germ at \(s=1\)
and

\[
-\frac{\zeta'_{\widehat\tau}}{\zeta_{\widehat\tau}}(s)
=\frac1{s-1}+G_0(s),
\tag{3.2}
\]

with \(G_0\) holomorphic near \(1\).  In the initial convergence half-plane,

\[
-\frac{\zeta'_{\widehat\tau}}{\zeta_{\widehat\tau}}(s)
=\sum_\gamma\sum_{k\ge1}
\widehat\ell_\gamma e^{-sk\widehat\ell_\gamma}.
\tag{3.3}
\]

The prime-orbit theorem gives

\[
\#\{\gamma:\widehat\ell_\gamma\le T\}\sim e^T/T.
\tag{3.4}
\]

Therefore the repeated-orbit tail

\[
R(s)=\sum_\gamma\sum_{k\ge2}
\widehat\ell_\gamma e^{-sk\widehat\ell_\gamma}
\tag{3.5}
\]

converges normally for \(\Re s>1/2\).  On a compact half-plane
\(\Re s\ge\sigma>1/2\), let \(L_{\min}>0\) be the minimum primitive
suspension length.  Then

\[
\sum_{k\ge2}\widehat\ell_\gamma
|e^{-sk\widehat\ell_\gamma}|
\le
\frac{\widehat\ell_\gamma e^{-2\sigma\widehat\ell_\gamma}}
{1-e^{-\sigma L_{\min}}}.
\]

The prime-orbit theorem makes the sum of this majorant finite because
\(2\sigma>1\).

### Theorem 3.1 (physical Mahler pressure pole) — **PROVED**

The physical amplitude has a meromorphic germ at \(s=1\), with

\[
\boxed{
\mathcal A_{\rm phys}(s)
=\frac{3}{\pi^2h_*}\frac1{s-1}+G_{\rm phys}(s)},
\tag{3.6}
\]

where \(G_{\rm phys}\) is holomorphic near \(1\).  Its residue satisfies

\[
1.093445200412297389\ldots
<\operatorname*{Res}_{s=1}\mathcal A_{\rm phys}
<1.093472735186032499\ldots.
\tag{3.7}
\]

#### Proof

Subtract (3.5) from (3.3).  Equations (3.2) and normal convergence of the
tail show

\[
\sum_\gamma\widehat\ell_\gamma e^{-s\widehat\ell_\gamma}
=\frac1{s-1}+G_1(s).
\]

Since \(\ell_\gamma=\widehat\ell_\gamma/h_*\), multiplying by
\(3/(\pi^2h_*)\) proves (3.6).  The residue decreases with \(h_*\); inserting
the two certified endpoints in (1.1) gives (3.7). \(\square\)

This is an actual pressure pole for a canonical summand of P53, not a finite
cycle-section fit.

## 4. Exact Galois witnesses and the scalar-roof no-go

If \(t\in\mathbb R\) is the trace of a real reciprocal pair with
\(|t|>2\), its Mahler contribution is

\[
L(t)=\operatorname{arcosh}(|t|/2).
\tag{4.1}
\]

The three exact inherited trace polynomials give:

\[
\begin{array}{c|c|c}
\text{orbit}&\text{trace roots}&\mathcal E_\gamma\\ \hline
m=1&2\pm2\sqrt7&\operatorname{arcosh}(\sqrt7-1)>0\\
m=3&-38\pm42\sqrt5&\operatorname{arcosh}(21\sqrt5-19)>0\\
m=4&578&0.
\end{array}
\tag{4.2}
\]

Numerically,

\[
\begin{array}{c|ccc}
m&\ell_\gamma&\mathcal H_\gamma&\mathcal E_\gamma\\ \hline
1&1.9673466291&3.0501161905&1.0827695614\\
3&4.8820992058&8.9056092911&4.0235100852\\
4&6.3595708754&6.3595708754&0.
\end{array}
\tag{4.3}
\]

### Theorem 4.1 (no scalar pressure retuning) — **PROVED**

There are no constant \(c\) and function \(u\) on the symbolic survivor for
which all primitive periodic sums satisfy

\[
\mathcal H_\gamma
=c\ell_\gamma+S_{m(\gamma)}(u-u\circ\sigma).
\tag{4.4}
\]

Equivalently, the Galois excess is not a constant multiple of the instability
roof modulo a coboundary.

#### Proof

A coboundary has zero sum on every periodic orbit.  The period-four row in
(4.2) has \(\mathcal H_4=\ell_4>0\), so (4.4) forces \(c=1\).  The period-one
row would then force \(\mathcal H_1=\ell_1\), contradicting
\(\mathcal E_1>0\). \(\square\)

This refutes only the natural one-parameter/coboundary shortcut.  It does not
refute a genuinely new Hölder observable.

## 5. The Galois-excess abscissa trichotomy

Let

\[
\sigma_{\rm Gal}
=\inf\left\{\sigma\in\mathbb R:
\sum_\gamma \mathcal E_\gamma
e^{-\sigma\widehat\ell_\gamma}<\infty\right\}.
\tag{5.1}
\]

The P53 positive majorant gives

\[
\sigma_{\rm Gal}\le\sigma_0<3.125207.
\tag{5.2}
\]

Because both summands in (2.5) have nonnegative coefficients and the physical
summand has abscissa one, the defining series for \(\mathcal A\) has abscissa

\[
\sigma_{\mathcal A}=\max\{1,\sigma_{\rm Gal}\}.
\tag{5.3}
\]

### Theorem 5.1 (pressure-access trichotomy) — **PROVED**

Exactly one of the following regimes occurs.

1. If \(\sigma_{\rm Gal}<1\), then \(\mathcal A_{\rm Gal}\) is holomorphic
   near \(s=1\), and the full amplitude has the physical pole and residue
   in (3.6).
2. If \(\sigma_{\rm Gal}=1\), then the excess has the same critical
   abscissa, but the abscissa alone determines neither boundary convergence
   nor a singularity or residue at one.  Those data require a weighted
   thermodynamic theorem or equivalent analytic input.
3. If \(\sigma_{\rm Gal}>1\), the positive defining series for the excess
   already loses convergence before the physical pressure line.

This trichotomy concerns access by the defining Dirichlet series.  Case 3
does not by itself rule out some separately proved analytic continuation.

## 6. Conditional Hölder completion

Assume there exists one real Hölder function \(\psi:\Sigma_A\to\mathbb R\)
such that, for every primitive orbit represented by \(x_\gamma\),

\[
\mathcal E_\gamma=S_{m(\gamma)}\psi(x_\gamma).
\tag{6.1}
\]

This is a mathematical hypothesis, not a definition by interpolation.  Put

\[
\zeta(s,z)=\prod_\gamma
\left(1-e^{-s\widehat\ell_\gamma+z\mathcal E_\gamma}\right)^{-1}.
\tag{6.2}
\]

Parry--Pollicott Theorem 6.4 and Corollary 6.4.1 use
\(P(g-cf)=0\) and the fixed-point zeta
\(\exp\sum_{n\ge1}n^{-1}\sum_{\sigma^nx=x}
e^{S_ng-csS_nf+zS_nk}\).  With
\(f=\widehat\tau\), \(g=0\), \(c=1\), and \(k=\psi\), this is exactly the
primitive Euler product (6.2), and the source theorem implies

\[
\left.\partial_z\log\zeta(s,z)\right|_{z=0}
=\frac{\int\psi\,d\mu}{\int\widehat\tau\,d\mu}
\frac1{s-1}+G_\psi(s),
\tag{6.3}
\]

where \(\mu\) is the equilibrium state of \(-\widehat\tau\).  The left side
contains all repetitions.  If \(a=\min\widehat\tau>0\), then
\(m(\gamma)\le\widehat\ell_\gamma/a\) and
\(|\mathcal E_\gamma|\le
\|\psi\|_\infty\widehat\ell_\gamma/a\).  Thus the \(k\ge2\) weighted
repetition tail is absolutely and normally dominated by the Section 3 tail.

### Theorem 6.1 (Hölder-excess completion) — **CONDITIONAL_THEOREM**

Under (6.1), the full P53 amplitude has a meromorphic simple-pole germ at
\(s=1\) with residue

\[
\boxed{
\operatorname*{Res}_{s=1}\mathcal A(s)
=\frac3{\pi^2}
\frac{\int(\tau+\psi)\,d\mu}
{\int h_*\tau\,d\mu}}.
\tag{6.4}
\]

#### Proof

The primitive part of (6.3) has the same principal part after subtracting
the holomorphic repetition tail.  Add its residue to the physical residue
from Theorem 3.1 and use \(\widehat\tau=h_*\tau\).  For real \(s>1\), the
excess Euler series has nonnegative coefficients, so its residue in (6.3) is
nonnegative.  The physical residue is strictly positive; hence the full
residue cannot cancel. \(\square\)

The theorem is deliberately conditional.  No current source identifies the
arithmetic quantity \(\mathcal E_\gamma\), which depends on all algebraic
conjugates of a return multiplier, with a Hölder function on the physical
symbolic survivor.

## 7. Finite certificate

The executable certificate independently checks:

1. eight inherited SHA-256 dependency locks;
2. all three exact trace polynomials and reciprocal-pair contributions;
3. the exact excess formulas in (4.2);
4. the certified residue interval in (3.7);
5. the scalar-roof contradiction;
6. three finite identities separating the primitive term from the
   repetition tail in \(-\zeta'/\zeta\);
7. twelve claim/schema mutations rejected by a checker that does not import
   the producer.

These checks certify the finite algebra and theorem wiring.  They are not a
numerical proof of the source zeta theorem.

## 8. Claim boundary

### Strongest positive result

The physical component of the P53 Mahler amplitude is now an exact
pressure-critical object with a simple pole and certified universal residue.

### Strongest obstruction

The nonphysical Galois excess is not a scalar instability roof modulo
coboundary, and no exact Hölder realization is known.

### Open theorem

Prove (6.1), establish an adequate asymptotically additive replacement, or
determine \(\sigma_{\rm Gal}\) directly.

### Explicitly not proved

- continuation of the actual Galois-excess series;
- a rational-prime or von Mangoldt trace;
- a completed Riemann determinant;
- a self-adjoint Hilbert--Pólya operator.

## 9. Source lock

The external theorem interface is William Parry and Mark Pollicott,
*Zeta Functions and the Periodic Orbit Structure of Hyperbolic Dynamics*,
Astérisque 187--188 (1990):

- Theorem 6.3 and Corollary 6.3.1, pp. 95--96: simple pole and logarithmic
  derivative for a weak-mixing normalized suspension;
- Theorem 6.4 and Corollary 6.4.1, pp. 97--98: two-parameter weighted zeta and
  equilibrium-average residue;
- Theorem 6.9, p. 109: prime orbit theorem.

Official source:
<https://www.numdam.org/item/AST_1990__187-188__1_0/>.

All H6 hypotheses and Mahler identities are inherited only through the eight
hash-locked repository dependencies listed in the finite certificate.
