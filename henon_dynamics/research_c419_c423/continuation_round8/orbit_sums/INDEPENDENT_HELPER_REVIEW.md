# FC7: independent review of the eighth-pass helper

2026-09-08 UTC. Reviewer: the nonlinear-lane agent, not the author of
this FC7 package. This review writes only this file; it does not amend
the author proof, the original contract or the batch admission record.

## Verdict and exact scope

**PASS_HELPER_ONLY.** The exact lag-one and lag-two evaluations, the
lag-three formula and uniform bound, the four-shift moment estimate,
and the explicit logarithmic-shift estimate are correct as stated.
No mandatory mathematical correction was found in the reviewed snapshot.

**Original FC7: NOT CURRENTLY JUSTIFIED.** The helper proves neither
uniform power saving on every cycle of length at least
$p^{1/2+\eta}$ nor an unbounded-prime obstruction. Its negative
conclusion concerns the specified completed second-moment argument,
not the truth of FC7 or the impossibility of other methods.

**Increment/admission: no paper-level or batch admission verdict.**
The general moment and Gauss/Weil mechanism is classical; these formulas
are useful map-specific specializations and a precise method boundary.
The source comparison remains bounded and does not establish global
novelty or original-body access to the 2010 article.

## Actual inputs and snapshot

The reviewer read the complete eighth-pass proof package, source audit
and frozen attempt, as well as the original FC7 contract and the current
round plan. SHA-256 receipts for the files reviewed are:

| File | SHA-256 |
| --- | --- |
| [PROOF_PACKAGE.md](PROOF_PACKAGE.md) | `cff038ec27e3bea1b06a59df840bbf1aadef3d0f1b84988c7ce685d41aab1ac6` |
| [SOURCE_AUDIT.md](SOURCE_AUDIT.md) | `33f7496492cac9d7107b131999f4d204fff408ff6ecd1f6146d0d05e23c06cf3` |
| [FROZEN_ATTEMPT.md](FROZEN_ATTEMPT.md) | `3fcc39d9c7590c28e17673d0e0cd7e2e6d241339427d8dae4346e0de53c748d4` |

The original input is the native polynomial permutation
$F(x,y)=(y,y^2+1-x)$ over every odd-prime field, a complete ordinary
cycle of least length $L$, and every nonzero frequency $(r,s)$.
No frequency, coordinate-zero state, small odd characteristic or
exceptional lag is removed. One step means one application of $F$.
The target length and quantifiers from
[the seventh-pass contract](../../continuation_round7/arithmetic_scout/SCOUT_REPORT.md)
are preserved.

## Independent mathematical check

### 1. Completion, signs and multiplicities

The inverse $(x,y)\mapsto(x^2+1-y,x)$ is correct. Complete-cycle
invariance gives the exact identity $HS=\sum_{P\in\mathcal O}
\sum_{h<H}\psi(\ell(F^hP))$ with no endpoint error and no restriction
that $H\le L$. Cauchy--Schwarz contributes the factor $L/H^2$.
Enlarging the sum of squared magnitudes to all $p^2$ points is valid
because those summands are nonnegative.

In the expansion of $M_H$, the diagonal contributes $Hp^2$. For
$h>j$, substitution $Q=F^jP$ gives $C_{h-j}$, and the reverse
pair contributes its conjugate. There are exactly $H-d$ pairs of
positive lag $d$. Thus equations (1)--(2), including the sign of
the phase and the factor $2\operatorname{Re}$, are correct.

The change $(u,v)\mapsto(u-v,u+v)$ used to prove $|G(a)|^2=p$
is bijective precisely because $p$ is odd. The completion-of-square
formula has the correct constant $c-b^2/(4a)$. These elementary
parts introduce no additional cancellation assumption.

### 2. Exact first and second correlations

Independent expansion of the first phase gives
$-(r+s)x+sy^2+(r-s)y+s$. Therefore $C_1=0$ unless $r=-s$.
On that line, $s\ne0$ and the phase is $s(y-1)^2$, so
$C_1=pG(s)$ and its magnitude is exactly $p^{3/2}$.
This really does refute a uniform $O(p)$ claim for these ambient
lag correlations, but it says nothing by itself against FC7.

For lag two, using $u=y^2+1-x$ gives the independent phase
$su^2+2ru-ry^2-2sy+s-r$. The substitution preserves the full
summation set. If $r=0$, the nonzero linear coefficient in $y$
kills the sum; if $s=0$, the nonzero linear coefficient in $u$
does so. Otherwise completing both squares gives exactly

$$
G(s)G(-r)\psi\left(s-r-r^2/s+s^2/r\right),
$$

of magnitude $p$. All divisions have nonzero denominators in
the case in which they are used.

### 3. Lag three, including every exceptional case

With $v=u^2+1-y$, independent expansion of
$rv+s(v^2+1-u)-r(y^2+1-u)-sy$ gives

$$
\begin{aligned}
A&=s-r,\\
B&=-2su^2-r-3s,\\
C&=su^4+(r+2s)u^2+(r-s)u+2s.
\end{aligned}
$$

If $r=s\ne0$, the $y$ coefficient is $-2r(u^2+2)$.
Its vanishing imposes $u^2=-2$, on which
$C=r(u^2+1)(u^2+2)=0$. Hence the claimed
$C_3(r,r)=p(1+\chi(-2))$ is exact. In particular, at $p=3$
the two roots are retained and this value is $6$.

If $A\ne0$, square completion yields $G(A)$ times a univariate
sum with phase

$$
-\frac{rs}{A}u^4-\frac{(r+s)^2}{A}u^2
+(r-s)u+2s-\frac{(r+3s)^2}{4A}.
$$

The quartic and quadratic coefficients follow, respectively, from
$s-s^2/A$ and $(r+2s)-s(r+3s)/A$; thus the reduction has no
hidden sign cancellation. The necessary case audit is:

| Frequency/characteristic | Check and consequence |
| --- | --- |
| $r=s\ne0$, any odd $p$ | The exact root-count formula above applies. |
| $r=0$, $s\ne0$ | Reduced phase is $-s(u+1/2)^2$, so in fact $C_3=G(s)G(-s)=p$. |
| $s=0$, $r\ne0$ | Reduced phase is $r(u+1/2)^2$, so in fact $C_3=G(-r)G(r)=p$. |
| $r=-s\ne0$ | $A=2s\ne0$; the reduced phase is $(s/2)u^4-2su+3s/2$. Its missing quadratic term does not remove the nonzero quartic coefficient. |
| $rs\ne0$, $r\ne s$, $p\ge5$ | The degree is exactly $4<p$, giving the asserted $3p$ bound after the Gauss factor. |
| $rs\ne0$, $r\ne s$, $p=3$ | The ambient bound is $p^2=9=3p$; no invalid quartic Weil estimate is invoked. |

These cases exhaust all nonzero frequencies and all odd primes.
The author only claims magnitude $p$ on the coordinate axes;
the exact values noted above are optional strengthening, not a
correction required for the proof. Equation (10) is valid uniformly.

### 4. Four shifts: constants and logical direction

For $H=4$, the weights of $(C_1,C_2,C_3)$ are $(3,2,1)$.
Consequently their total possible contribution to the real moment
is bounded in magnitude by $6p^{3/2}+4p+6p$.
Both the upper and lower displayed estimates for $M_4$ are correct.
The lower estimate can be negative for a small prime; that does
not make it invalid or affect the uniform asymptotic statement.

Thus $M_4=4p^2+O(p^{3/2})$, and the actual right-hand side supplied
by this completion remains at $|S|$ scale $p\sqrt L$.
At $L=p^{1/2+\eta}$ the corresponding relative scale is
$p^{3/4-\eta/2}$. This is the size of an upper-bound expression,
not a lower bound for an individual orbit sum. The author makes
that distinction correctly. Exact knowledge of these three lags
cannot alter the leading scale of this four-shift ambient moment.

### 5. Longer lags and the explicit logarithmic estimate

In the recurrence $X_{n+1}=X_n^2+1-X_{n-1}$, the polynomial
$X_n\in\mathbb F_p[x][y]$ is monic in $y$ of degree $2^{n-1}$
for every $n\ge1$. The base cases $X_1=y$ and
$X_2=y^2+1-x$ also handle the otherwise exceptional degree of
$X_0=x$. At each later step the lower-degree subtraction cannot
cancel the squared leading term, in any characteristic.

For $s\ne0$, the lag-$d$ phase has constant leading coefficient
$s$ and degree $2^d$ in $y$. For $s=0,d\ge2$, its leading
coefficient is $r$ and its degree is $2^{d-1}$. The remaining
case $s=0,d=1$ has zero complete correlation by linear
orthogonality. There is therefore no exceptional fixed-$x$
fibre with vanishing leading coefficient.

With $2^d<p$, the stated univariate Weil input can be applied
for each $x$. Summing its bound over $p$ values gives
$|C_d|\le2^dp^{3/2}$, with room in the constant. The explicit
degree restriction excludes Artin--Schreier polynomial-function
degeneracies; a claim for arbitrary formal nonconstant phases
is neither needed nor used.

For $p\ge17$, let $H=\lfloor(\log_2p)/4\rfloor$. The checks are
$H\ge1$, $2^H\le p^{1/4}$, and $2^d<p$ for every $1\le d<H$.
The estimate $\sum_{d=1}^{H-1}(H-d)2^d\le H2^H$ holds also
for $H=1$, when the left side is empty. Hence

$$
M_H\le Hp^2(1+2p^{-1/4})\le2Hp^2.
$$

The last inequality is valid since $p>16$. The floor bound
$H\ge(\log_2p)/8$ then gives
$|S|^2\le16Lp^2/\log_2p$. Thus the constant $4$, the log
base and the stated prime range in (14) all check. Retaining
$|S|\le L$ for the smaller odd primes is sufficient.

The expression in (14), divided by $L$, is below one exactly
when $L>16p^2/\log_2p$. At the target lower length it is
$4p^{3/4-\eta/2}/\sqrt{\log_2p}$ and grows for the entire
specified range of $\eta$. Even at $L=p^2$ this displayed
estimate supplies only a logarithmic, not a power, gain.
No replacement of the frozen threshold has occurred.

## Independent source and ownership check

The reviewer directly accessed the following two primary research
papers. This is a bounded body check, not a claim to have read either
entire paper or independently repeated the author's search ledger.

- [Roy--Steiner, arXiv:2204.01802v1](https://arxiv.org/html/2204.01802v1):
  read the explicit Assumption 5.2, the relevant section 5.1--5.2
  statements and moment discussion, and section 5.5. The last section
  does report $O(N^{1/2}p^{n/2}/\sqrt{\log p})$ as a generic bound
  attributed to the 2010 work. Its $n=2$ scale agrees with (14).
  This confirms the later attribution only. The stronger moment
  statement uses an additional assumption on combinations of iterates;
  the FC7 package does not import it. No later-version persistence is
  certified here.
- [Ostafe--Shparlinski, arXiv:0902.3884](https://arxiv.org/pdf/0902.3884):
  read the section 2.1 triangular construction and degree conditions,
  and section 3.2's Lemma 3, Theorem 4 statement and surrounding shifted
  moment argument. The theorem has a last affine coordinate and
  substantive triangular/slow-growth hypotheses, not the present
  Hénon hypotheses. This supports classical mechanism ownership,
  not a transfer of its power-saving theorem. The reviewed proof uses
  the safer explicit univariate degree-below-$p$ Weil statement.

The original Ostafe--Pelican--Shparlinski 2010 theorem body was not
independently obtained or read in this review. The author transparently
records its access limitation; secondary reproduction does not remove
it. The independently checked proof of (14) does not depend on unseen
2010 hypotheses. Therefore that limitation is not a mathematical gap
in this helper, while it remains a limit on broader source clearance.

The three exact short-lag computations are short specializations of
classical methods, not evidence of a new general cancellation
mechanism. Nothing here establishes that every existing result fails
to answer FC7, and nothing grants this helper a manuscript slot.

## Review receipt and disposition

The batch workflow and proof-writer preserve the original/helper
separation. Research-review is implemented by this actual nonauthor
current-team review, not by an external-model template. The completed
hand rederivations above are independent of the author calculations;
the author's execution and search counts are not recertified merely
because they were read.

New mathematical programs in this review: **0**. Old mathematical or
build reruns: **0**. New search queries: **0**; the two specified
sources were opened/found directly. No GPU, paid model API, source-PDF
download, author-file amendment, Git mutation, global admission,
manuscript or formal Route-A evaluation was performed.

Final disposition: **PASS for all stated FC7 helpers in the recorded
snapshot; no mandatory correction; original FC7 remains unclosed.**
The next substantive requirement is an estimate on the actual
invariant cycle at the frozen length, or a genuine unbounded-prime
obstruction, not a repetition of this completed method check.
NO_BAD_EULER_OR_ROOT_NUMBER.
