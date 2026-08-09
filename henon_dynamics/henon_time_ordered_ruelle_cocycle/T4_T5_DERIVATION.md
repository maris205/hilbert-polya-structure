# HCS-C22 T4 theorem and orbitwise scalar-T5 obstruction

**Date:** 2026-08-09
**Status:** T4 proved; common complex-domain subgate proved; frozen orbitwise
scalar denominator-cancellation gate refuted

## 1. Result in one statement

The local two-letter Hénon skew product has a well-defined intrinsic
instability Euler determinant

\[
D_{\mathrm{inst}}(z,s)
=\prod_{\gamma\in\mathscr P}
 \left(1-z^{n_\gamma}e^{-s\ell_\gamma}\right),
\qquad
\ell_\gamma=\log|\lambda_u(\gamma)|,
\]

which converges normally and is nonzero on an explicit nonempty domain.  Its
Euler logarithm is exactly the fixed-point instability trace series.  Both
frozen Hénon letters also share one strict complex pinning domain.

The remaining frozen **orbitwise geometric scalar** claim nevertheless fails
before any spectrum is computed.  A scalar pinning trace carries a
fixed-point denominator.  Cancelling it separately at a primitive saddle
determines a scalar orbit weight whose square cannot cancel the denominator
on the double repetition.  Thus the standard scalar construction cannot
realize the pure-instability weight term by term (equivalently, after
adjoining independent formal markers for primitive orbits).  This does not
exclude an accidental aggregate trace identity in which distinct orbits of
the same period compensate.  A graded exterior-algebra Ruelle--Lefschetz
complex is the canonical denominator-cancelling pivot; it is a new candidate
and not a result of this project.

## 2. Frozen dynamical object

Let

\[
H_a(q,p)=(1-aq^2-p,q),
\qquad a_0=\frac{59}{10},\quad a_1=\frac{61}{10},
\]

and

\[
\mathcal F(\omega,z)
=\bigl(\sigma\omega,H_{a_{\omega_0}}z\bigr)
\]

on the T1-certified local survivor.  A length-
\(n\) word always means

\[
H_{a_{\omega_{n-1}}}\circ\cdots\circ H_{a_{\omega_0}}.
\]

The primitive objects are joint parameter--state cyclic orbits.  Parameter
and state words are never rotated separately.  Reversal is an exact symmetry
control but is not removed from the Euler multiplicity.

Let \(\mathscr P\) be the set of primitive joint orbits.  For
\(\gamma\in\mathscr P\), write \(n_\gamma\) for its microperiod,
\(M_\gamma\) for its chronological fibre monodromy, and
\(\lambda_u(\gamma)\in\mathbb R\) for its signed unstable eigenvalue.

## 3. T4: intrinsic instability determinant

### Theorem 1 -- repetition and fixed-point trace

Define

\[
D_{\mathrm{inst}}(z,s)
=\prod_{\gamma\in\mathscr P}
 \left(1-z^{n_\gamma}|\lambda_u(\gamma)|^{-s}\right),
\]

where

\[
|\lambda|^{-s}:=\exp(-s\log|\lambda|)
\]

uses the real positive logarithm.  Put
\(Z_{\mathrm{inst}}=D_{\mathrm{inst}}^{-1}\).

For every repetition number \(r\ge1\),

\[
M_{\gamma^r}=M_\gamma^r,
\qquad
\lambda_u(\gamma^r)=\lambda_u(\gamma)^r,
\qquad
\ell_{\gamma^r}=r\ell_\gamma.
\]

Consequently the instability weight is exactly multiplicative under
repetition.

For a fixed point \(x\) of \(\mathcal F^n\), let

\[
\ell_n(x)=\log|\Lambda_{u,n}(x)|
\]

and define

\[
B_n(s)=
\sum_{x\in\operatorname{Fix}(\mathcal F^n|\Lambda_{\mathcal F})}
e^{-s\ell_n(x)}.
\]

Where the series converges normally,

\[
\boxed{
-\log D_{\mathrm{inst}}(z,s)
=\sum_{n\ge1}\frac{z^n}{n}B_n(s).
}
\]

#### Proof

If a primitive orbit has length \(d\mid n\), it supplies \(d\) marked
fixed points to \(\operatorname{Fix}\mathcal F^n\), and its return is
repeated \(r=n/d\) times.  Its contribution to \(B_n/n\) is therefore

\[
\frac dn |\lambda_u(\gamma)|^{-sr}
=\frac1r|\lambda_u(\gamma)|^{-sr},
\]

which is exactly the \(r\)-th logarithmic term of its Euler factor.  Normal
convergence below justifies regrouping by primitive orbit and repetition.
\(\square\)

### Theorem 2 -- explicit all-period multiplier bounds

In the T1 normalized tangent chart,

\[
D\widehat H_a(q,p)=
\begin{pmatrix}
-2aq&-123/112\\
112/123&0
\end{pmatrix}.
\]

The forward invariant cone has slope at most \(1/2\).  Its certified
dominant-coordinate denominator is

\[
d_u=\frac{11371}{3360}.
\]

Therefore a vector in the unstable cone expands by at least

\[
E^2=\frac{d_u^2}{1+(1/2)^2}
=\frac{129299641}{14112000},
\qquad E=3.026943925255\ldots.
\]

The Frobenius norm gives the uniform upper bound

\[
U^2=
\left(\frac{61}{8}\right)^2
+\left(\frac{123}{112}\right)^2
+\left(\frac{112}{123}\right)^2
=\frac{11420060341}{189778176},
\]

with \(U=7.757308535412\ldots\).  Since the same normalized chart is used
at the start and end of a periodic return and its unstable eigenline lies in
the cone,

\[
\boxed{
E^{n_\gamma}
\le |\lambda_u(\gamma)|
\le U^{n_\gamma}.
}
\]

Thus

\[
n_\gamma\log E
\le\ell_\gamma
\le n_\gamma\log U.
\]

### Theorem 3 -- explicit normal-convergence domain

The joint symbolic adjacency is \(J_2\otimes A\), where

\[
\operatorname{spec}(A)
=\{\varphi,-\varphi^{-1},i,-i\},
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]

Hence the exact number of marked period-\(n\) points is

\[
N_n=2^n\operatorname{tr}(A^n)
\le4(2\varphi)^n.
\]

For \(t=\Re s\), put

\[
\chi(t)=
\begin{cases}
E^{-t},&t\ge0,\\
U^{-t},&t<0.
\end{cases}
\]

The multiplier bounds give

\[
|B_n(s)|
\le4\bigl(2\varphi\chi(t)\bigr)^n.
\]

It follows that the product and logarithmic series converge locally
uniformly, define holomorphic functions, and have no Euler-factor zeros on

\[
\boxed{
\mathfrak D_{\mathrm{exp}}
=\{(z,s):2\varphi|z|\chi(\Re s)<1\}.
}
\]

Equivalently,

\[
|z|<\frac{E^{\Re s}}{2\varphi}
\quad(\Re s\ge0),
\qquad
|z|<\frac{U^{\Re s}}{2\varphi}
\quad(\Re s<0).
\]

Some exact-certificate landmarks are

| \(\Re s\) | guaranteed \(z\)-radius |
|---:|---:|
| \(-1\) | \(0.03983559413219978\ldots\) |
| \(0\) | \(0.30901699437494742\ldots\) |
| \(1\) | \(0.93537711392410391\ldots\) |
| \(2\) | \(2.83133407281602334\ldots\) |

At \(z=1\), this coarse all-period theorem only guarantees convergence for

\[
\Re s>
\frac{\log(2\varphi)}{\log E}
=1.0603180797198193\ldots.
\]

That last inequality is important: the physically interesting pressure
boundary at \(z=1\) is not reached by absolute Euler convergence.  Any
claim there requires a genuine continuation or determinant theorem, not a
longer finite-cycle section.

For real \(t\), the pressure-sharp absolute domain is

\[
\mathfrak D_P
=\{(z,s):|z|e^{P(-\Re(s)\tau)}<1\},
\]

and \(\mathfrak D_{\mathrm{exp}}\subseteq\mathfrak D_P\).  No continuation
across the pressure boundary is claimed.

### Exact \(s=0\) control

At \(s=0\), the weighted determinant becomes the finite symbolic
determinant

\[
D_{\mathrm{inst}}(z,0)
=\det(I-z(J_2\otimes A))
=1-2z-8z^3-16z^4.
\]

It factors as

\[
-(4z^2+1)(4z^2+2z-1).
\]

Thus \(1/(2\varphi)\) is the exact logarithmic/Euler radius at \(s=0\),
although the resulting polynomial itself extends to the plane.  This is a
control, not arithmetic structure.

## 4. The one-microstep Hölder roof

Let \(m^u(\xi)\) be the normalized unstable slope at the point coded by the
joint two-sided sequence \(\xi\).  The projective graph transform is

\[
G_{a,q}(m)=
\frac{112/123}{-2aq-(123/112)m}.
\]

On the certified cone its derivative in \(m\) is bounded by

\[
\rho\le d_u^{-2}
=\frac{11289600}{129299641}
=0.08731\ldots,
\]

which is smaller than the coordinate coding rate

\[
\theta=\sqrt{240/1003}<1/2.
\]

The T1 central-coordinate estimate and the graph-transform convolution imply

\[
|q_0(\xi)-q_0(\xi')|
\le\frac54\theta^N,
\qquad
|m^u(\xi)-m^u(\xi')|
\le C_u\theta^N
\]

whenever the codes agree on \([-N,N]\).  Consequently

\[
\tau(\xi)=
\log\frac{
\|D\widehat H_{a_{\omega_0}}v^u(\xi)\|
}{\|v^u(\xi)\|}
\]

is a positive Hölder one-microstep observable satisfying

\[
\log E\le\tau\le\log U.
\]

For every periodic orbit,

\[
S_{n_\gamma}\tau(\gamma)=\ell_\gamma
\]

exactly.  Changing the continuous norm changes \(\tau\) by a Hölder
coboundary and leaves all periodic sums unchanged.  A one-sided Hölder
representative exists by the standard Sinai--Bowen cohomology construction.
This is not a proof that the roof has finite memory.

## 5. T5 subgate: a common complex pinning domain

After swapping coordinates, write

\[
F_a(x,y)=(y,1-ay^2-x).
\]

Use the same disks for both parameter letters:

\[
X_\sigma=\overline D\!\left(\sigma\frac{23}{48},\frac7{48}\right),
\qquad
Y_\sigma=\overline D\!\left(\sigma\frac{121}{256},\frac{41}{256}\right).
\]

They satisfy \(X_\sigma\Subset Y_\sigma\) with margin \(1/128\).  For every
allowed chronological endpoint-sign pair \((t,r)\ne(+,+)\), both letters
have the holomorphic branch

\[
P_{a,\sigma}(w,z)
=\sigma\sqrt{\frac{1-w-z}{a}},
\qquad
P_{a,\sigma}(Y_t\times X_r)\Subset X_\sigma.
\]

The exact boundary audit is:

| \(a\) | \((t,r)\) | squared-image boundary gap |
|---:|:---:|---:|
| \(59/10\) | \((-,-)\) | \(15/1888\) |
| \(59/10\) | \((-,+)\) | \(23/4248\) |
| \(59/10\) | \((+,-)\) | \(259/33984\) |
| \(61/10\) | \((-,-)\) | \(5/244\) |
| \(61/10\) | \((-,+)\) | \(7/4392\) |
| \(61/10\) | \((+,-)\) | \(131/35136\) |

The minimum radicand modulus is \(55/488\), the minimum squared-image gap
is \(7/4392\), and the corresponding coordinate clearance is

\[
\frac45\frac7{4392}=\frac7{5490}.
\]

Each endpoint derivative obeys

\[
|\partial_wP|^2=|\partial_zP|^2
\le\frac{40}{649}<\frac1{16}.
\]

Thus the two-neighbor sup-norm Lipschitz constant has squared upper bound

\[
4\frac{40}{649}=\frac{160}{649}<1.
\]

This proves the common-domain subgate.  It does not prove that a desired
weighted scalar kernel has the correct trace.

## 6. T5 subgate: common projective lift and holomorphic weight

The real modulus in the instability weight is not inserted directly into a
complex kernel.  Instead use the normalized slope disk

\[
M=\overline D(0,1/2)
\]

and lift each Hénon branch by

\[
G_{a,q}(m)=
\frac{112/123}{-2aq-(123/112)m}.
\]

If \(q\in X_\varepsilon\), define the oriented expansion factor

\[
j_{a,\varepsilon}(q,m)
=-\varepsilon\left(-2aq-\frac{123}{112}m\right).
\]

Its image lies in the right-half-plane disk with center and radius

\[
C_a=2a\frac{23}{48},
\qquad
R_a=2a\frac7{48}+\frac{123}{224}.
\]

The two exact rows are

| \(a\) | \(C_a\) | \(R_a\) | \(C_a-R_a\) |
|---:|---:|---:|---:|
| \(59/10\) | \(1357/240\) | \(7627/3360\) | \(11371/3360\) |
| \(61/10\) | \(1403/240\) | \(7823/3360\) | \(11819/3360\) |

Thus \(j\) is nonzero on every branch, lies in one simply connected
right-half-plane sector, and has the common principal logarithm.  Moreover,

\[
|G_{a,q}(m)|
\le\frac{125440}{466211}
=0.26906\ldots<\frac12,
\]

with slope-disk image clearance

\[
\frac12-\frac{125440}{466211}
=\frac{215331}{932422}.
\]

The fibre derivative is bounded by

\[
|\partial_mG|
\le\frac{11289600}{129299641}
=0.08731\ldots<1.
\]

Consequently every periodic base branch has exactly one periodic lifted point
in \(M\).  It is the unstable section; the stable projective fixed point is
outside this domain, so the lift does not double-count periodic orbits.  On
the real invariant section, \(j>0\) at every step and

\[
\prod_{i=0}^{n-1}j_i=|\Lambda_{u,n}|.
\]

Therefore

\[
g_s=\exp(-s\operatorname{Log}j)
\]

is an honest one-step holomorphic weight whose periodic product is exactly
\(|\Lambda_u|^{-s}\).  This closes the geometric and weight-localization
parts of the projective pivot; it still does not remove the scalar flat-trace
denominator.

## 7. T5 kill theorem: no orbitwise scalar denominator cancellation

### Theorem 4 -- denominator/repetition obstruction

Consider a scalar holomorphic pinning or weighted-composition operator whose
contribution at a periodic saddle has the standard geometric form

\[
\frac{G_\gamma}{\det(I-M_\gamma)}
\]

or its real absolute/oriented counterpart, with \(G_\gamma\) the product of
a one-step scalar cocycle.  If the trace formula is required to match each
periodic-point summand separately, no such scalar cocycle can make every
primitive orbit and every repetition contribute the pure instability weight

\[
|\lambda_u(\gamma)|^{-sr}.
\]

#### Proof

Let \(M\) be the monodromy of any primitive area-preserving saddle and set
\(t=\operatorname{tr}M\), so \(|t|>2\).  The primitive return requires

\[
G_\gamma
=|\lambda_u|^{-s}\det(I-M).
\]

On the double return, scalar multiplicativity forces

\[
G_{\gamma^2}=G_\gamma^2.
\]

Compatibility would therefore require

\[
\det(I-M^2)=\det(I-M)^2.
\]

Since \(\det M=1\),

\[
\det(I-M)=2-t,
\qquad
\det(I-M^2)=4-t^2.
\]

Their signed difference is

\[
(4-t^2)-(2-t)^2=-2t(t-2),
\]

which is nonzero for \(|t|>2\).  The absolute convention also fails.  If
\(t>2\),

\[
|4-t^2|-|2-t|^2=4(t-2)>0;
\]

if \(t<-2\), the reverse difference is

\[
|2-t|^2-|4-t^2|=-4(t-2)>0.
\]

Hence the primitive and double-return equations are incompatible.
\(\square\)

The same obstruction survives the certified projective lift, so it is not
an artifact of working only on the two-dimensional base.  If \(\lambda\) is
the signed unstable multiplier, the lifted return is block triangular with
eigenvalues

\[
\lambda,\qquad \lambda^{-1},\qquad \lambda^{-2}.
\]

For \(\lambda=x>1\), the ratio of the absolute double-return denominator to
the square of the primitive denominator is

\[
\frac{(x+1)(x^2+1)}{(x-1)^3}>1,
\]

because the numerator minus the denominator is

\[
2(2x^2-x+1)>0.
\]

For \(\lambda=-x<-1\), the ratio is

\[
\frac{(x-1)(x^2+1)}{(x+1)^3}<1,
\]

because the denominator minus the numerator is

\[
2(2x^2+x+1)>0.
\]

Thus neither a base scalar kernel nor a scalar kernel on the natural
projective lift can cancel its geometric denominator orbit by orbit at all
repetitions.

The orbitwise hypothesis is essential.  It may equivalently be formalized by
attaching an independent marker \(u_\gamma\) to every primitive orbit and
requiring equality as a formal series in the \(u_\gamma\).  The proof does
**not** show that the unmarked aggregate equalities

\[
\operatorname{Tr}L_s^n=B_n(s)
\]

are impossible: without an additional independence or uniqueness theorem,
errors from distinct period-\(n\) fixed points could in principle cancel.

This obstruction is different from the earlier C02D constant-sign
obstruction.  It concerns the nonmultiplicativity of the full fixed-point
denominator itself.  It excludes the frozen orbitwise geometric scalar
realization.  It does not exclude an aggregate scalar representation, a
purely symbolic trace with no geometric denominator, or other operator
classes.

## 8. The canonical change of dynamical form

The fixed-point denominator has a standard algebraically honest cancellation:

\[
\sum_k(-1)^k\operatorname{tr}(\wedge^kM)
=\det(I-M).
\]

Therefore the authorized next candidate is a graded family
\(\mathcal L_{s,k}\)
whose flat traces satisfy

\[
\operatorname{tr}\mathcal L_{s,k}^n
=\sum_{x\in\operatorname{Fix}\Phi^n}
\frac{g_s^{(n)}(x)\operatorname{tr}(\wedge^kD\Phi^n_x)}
{\det(I-D\Phi^n_x)}.
\]

Then the supertrace cancels the denominator and the natural candidate is an
alternating Fredholm product

\[
D_{\mathrm{inst}}(z,s)
\stackrel{?}{=}
\prod_k\det(I-z\mathcal L_{s,k})^{(-1)^k}.
\]

The projective lift required to make \(|\lambda_u|^{-s}\) a local
holomorphic cocycle has now been certified.  In normalized coordinates it is

\[
(q,p,m)\longmapsto
\left(H_a(q,p),
\frac{112/123}{-2aq-(123/112)m}
\right).
\]

The common complex slope domain, exclusion of the stable projective fixed
point, nonvanishing sector, and logarithm branch have all passed.  The graded
candidate's remaining positive operator gate is genuinely functional analytic:
construct the four exterior-degree spaces and branch operators, prove
nuclearity on one common enlarged/nested domain, and verify the exact
supertrace formula without losing parameter chronology.

Even if these gates pass, the result is generally an alternating ratio of
nuclear determinants and hence may be meromorphic.  It is not automatically
one entire scalar Fredholm determinant and is not automatically a
Hilbert--Pólya operator.

## 9. Scope and Route-A interpretation

The round changes the internal analytic status but not the arithmetic score.

- A1 remains `A1_WEAK`: the joint primitive orbit theorem is rigorous but
  no prime-like law exists.
- A2 remains `A2_FAIL`: a local Euler product now exists in a proved domain,
  but there is no target divisor or \(\xi\)-normalization.
- A3 remains `A3_FAIL`: no continuation beyond the pressure boundary,
  functional equation, gamma factor, or Riemann counting law exists.
- A4 remains `A4_FORMAL_HINT`: the symplectic fibre and graded pivot are
  structural hints, not a self-adjoint lift.

The overall result remains `ROUTE_A_EXPLORATORY`.  The meaningful progress is
that C22 is now mathematically complete under its frozen orbitwise geometric
trace convention: T4 passes, the common complex geometry passes, and the
standard termwise scalar denominator-cancellation construction is rigorously
closed.  Nonexistence of every aggregate scalar representation is not
claimed.

## 10. Reproducibility and Material Passport

The exact producer reconstructs the multiplier bounds, symbolic counts,
Euler/log bookkeeping, all six two-letter complex-domain cases, both
projective-domain cases, the common logarithm sector, and the
double-repetition obstruction.  The independent checker imports no producer
code.  It also rejects missing-domain, altered-bound, altered-trace,
projective-multiplicity, and scope-expansion mutations.

Run

```bash
bash code/run_c22_t4.sh
```

from this project directory.

**Material Passport**

- Material: exact theorem/obstruction certificate and documentation.
- Input: hash-bound T1--T3 certificate, frozen rational parameters, and
  frozen joint chronology.
- Transform: exact rational and symbolic arithmetic; decimal values never
  decide a gate.
- Output: `results/c22_t4_certificate.json` and
  `results/c22_t4_independent_check.json`.
- Integrity: SHA-256 binding plus fail-closed tests.
- Exclusions: no prime data, Riemann-zero data, Ulam spectrum, fitted scale,
  averaged transition matrix, or finite-section root evidence.
