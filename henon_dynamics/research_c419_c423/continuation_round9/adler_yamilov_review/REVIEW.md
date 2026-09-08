# AY9 independent nonauthor auxiliary review

2026-09-08 UTC. Internal AI-assisted hand review by the AS1 spectral
helper/CP9 reviewer, who did not author these AY9 statements. Only this
review directory is written. This is not journal peer review, a full
atlas claim, paper admission or a formal Route-A evaluation.

## Verdict and fixed target

**PASS for the stated AY9 auxiliary claims. No mandatory mathematical
correction was identified.**

The reviewed [author proof](../adler_yamilov/PROOF_PACKAGE.md) has exactly
400 lines and SHA-256
556f831e7d079ed4baa5c5548511fa46740bf62808854a7aba29bc17fe91fcec.
The author explicitly confirmed this frozen version before the review
was finalized and stated that high-order exploration had stopped. No
unwritten or later high-order argument is included in this verdict.

The new conclusions verified are:

1. Every nonzero ordinary integral cycle at nonzero integer $k$ meets a
   section $h=\pm1$; the normalized invariants $\gamma,\lambda$ are
   integers, and $h_nh_{n-1}\mid k$.
2. The quotient-order-three stratum consists exactly of the two stated
   families and their native cyclic rotations. Their least native
   periods are three for $\gamma=-1$ and six for $\gamma=1$.
3. The quotient-order-four stratum occurs only at $k=\pm4$, consists
   exactly of the displayed factorizations and rotations, and has
   least native period eight.
4. The quotient-order-five integral periodic stratum is empty.

**The original all-integer-parameter AY7 structural atlas remains
NOT CLOSED.** Quotient orders $6,7,8,9,10,12$ remain unclassified here.
In particular the possible-native-period set has not been reduced to
$\{3,6,8\}$ by this review. No unproved Miller-function/scaling-multiplier
relation is used, and no helper is promoted to a replacement contract.

## Complete reading and imported-input boundary

The reviewer read the entire fixed 400-line proof and entire
[FROZEN_ATTEMPT.md](../adler_yamilov/FROZEN_ATTEMPT.md), the AY7 portion
of the [original question](../../continuation_round7/nonlinear_scout/SCOUT_REPORT.md),
the complete 408-line
[round-eight proof](../../continuation_round8/adler_yamilov/PROOF_PACKAGE.md),
and its complete
[accepted nonauthor review](../../continuation_round8/adler_yamilov/COORDINATOR_HELPER_REVIEW.md).

The accepted quotient identity, exact translation by $P$, singular-point
exclusion, rational quotient-order list, and zero-safe scaling lift are
imported inputs. Reading those proofs to delimit the dependencies is not
a rerun of their census or a claim to have reconstructed Mazur's theorem.
The new deductions below are checked directly from those accepted inputs.
No old mathematical program or accepted finite diagnostic was rerun.

The native ordinary domain still requires every forward denominator
$1+ps$ and every inverse denominator $1+rq$ to be nonzero along the
entire two-sided orbit. Individual coordinate zeros are retained.
The $k=0$ pair-swap boundary and the origin remain inherited results.

## 1. Forced unit coefficient and arithmetic normalization

The identically zero $p$ channel cannot hide a nonzero periodic state:
then $D_n=1$ and $h_n=k$ throughout. Multiplying
$s_{n+1}-s_{n-1}=ks_n$ by $s_n$ and summing over a native period
makes the left side zero by cyclic reindexing. Since the coordinates
are real integers and $k\ne0$, all $s_n$ vanish. The lag identities
then force all four coordinates to vanish.

Otherwise let $M=\max_n|p_n|>0$. If every $|h_n|\ge2$, at a
maximizing index
$$
2M\le |h_np_n|=|p_{n-1}-p_{n+1}|\le2M.
$$
Equality forces $|h_n|=2$, both adjacent moduli equal to $M$, and
$p_{n+1}=-p_{n-1}$. Repeating this argument at those neighboring
maxima propagates around the whole finite orbit. Thus
$$
h_n=2p_{n-1}/p_n,\qquad h_{n+1}=-h_n.
$$
All denominators $D_n=k/h_n$ are two-periodic, giving quotient
period at most two, which the accepted nonzero-periodic-lift theorem
excludes. This verifies the forced unit section without assuming an
individual coordinate is everywhere nonzero in advance.

At such a section, $D=\varepsilon k$ with $\varepsilon=\pm1$, and
the zero-safe product formula gives
$$
pq=\varepsilon E-L/k.
$$
Hence $\lambda=L/k$ is an integer; $\gamma=C/k=\lambda+I$ is
also an integer. The definitions
$A=\gamma+\lambda-k$ and $B=\gamma\lambda+1$ therefore give
integers with $a=kA$ and $e=k^2B$.

At every orbit point,
$$
\frac{DE}{k}=pq+\lambda\in\mathbb Z
\quad\Longrightarrow\quad
\frac{k}{h_nh_{n-1}}\in\mathbb Z.
$$
This is precisely signed divisibility $h_nh_{n-1}\mid k$;
neither factor is zero. Substitution into the quotient curve gives
$$
E^2-(\varepsilon A+1)E+B-\varepsilon k=0.
$$
Together with $E\mid k$ and $E\ne0$, reduction modulo $E$ gives
$E\mid B$. No unjustified division by $p,s,pq$ or $rs$ occurs.

## 2. Low-order chord conditions, including singular fibres

The stated shear of the accepted cubic cancels the square
$(Ax+k)^2/4$ and yields
$$
y^2+Axy+ky=x^3-Bx^2,\qquad P=(0,0).
$$
At $P$, the derivative with respect to $y$ is $k\ne0$, so $P$
is nonsingular. The accepted irreducibility and smooth-locus group
description remain available on singular fibres. An actual nonzero
periodic quotient is not the singular point, by the accepted input.
Thus the following chord computations have the needed group domain.

The tangent $y=0$ meets the cubic with factor $x^2(x-B)$.
Reflection is $(x,y)\mapsto(x,-y-Ax-k)$, hence
$2P=(B,-AB-k)$. This gives order three exactly when $B=0$.

For $B\ne0$, put $u=AB+k$. The line through $P$ and $2P$
has slope $-u/B$. After removing one intersection factor $x$
for $P$, the product of the two residual abscissae is $ku/B$, giving
$$
x(3P)=ku/B^2,\qquad y(3P)=k(x(3P)/B-1).
$$
Consequently:

- $2P$ is a nonidentity two-torsion point exactly when $u=0$,
  yielding exact order four.
- $3P=-2P=(B,0)$ exactly when $ku=B^3$, yielding exact order
  five. Orders one and two are unavailable, and $B\ne0$ excludes
  the order-three branch.

The computations are explicit group calculations, not a smooth-generic
specialization or a claim that torsion alone produces a periodic lift.

## 3. Quotient order three: necessity, all zero strata and native lift

Order three gives $B=0$, so the two integer parameters satisfy
$\gamma\lambda=-1$. Hence $\gamma=\pm1$, $\lambda=-\gamma$,
$I=2\gamma$ and $J=k\gamma-1$.

Write a denominator cycle as $(u,v,w)$. Subtracting the recurrence
expressions for $a$ at $u$ and $v$ gives
$(u-v)(w+k^2/(uv))=0$. Since a least-three cycle has two distinct
entries, cyclic relabeling yields $uvw=-k^2$. The same recurrence
with $a=-k^2$ gives $uv+uw+vw=-k^2$. Therefore its coefficient
triple has product $-k$ and sum $k$.

For nonzero integers satisfying $abc+a+b+c=0$, two entries of
absolute value at least two would give
$|c|=|(a+b)/(ab+1)|<1$. The author's separate same-sign and
opposite-sign inequalities prove this strict bound and have no zero
denominator in that range. Thus there is a unit. Substituting a
unit makes the remaining expression factor and forces the opposite
unit. The coefficient multiset is consequently $(1,-1,k)$ and
the denominator multiset is $(k,-k,1)$. This remains true with
repeated entries at $k=\pm1$.

Every orbit therefore has a section with $D=1$, where $ps=0$.
If $s=0$, the product equations force $pq=2\gamma$ and
$rq=\gamma k-1$, yielding exactly
$$
\left(2\gamma/q,\ q,\ (\gamma k-1)/q,\ 0\right),
\qquad q\ne0,\ q\mid2,\ q\mid(\gamma k-1).
$$
If $p=0$, they force $rs=2\gamma$ and $rq=-\gamma k-1$,
yielding exactly
$$
\left(0,\ (-\gamma k-1)/r,\ r,\ 2\gamma/r\right),
\qquad r\ne0,\ r\mid2,\ r\mid(-\gamma k-1).
$$
There is no missing overlap $p=s=0$, since that would give
$I=0$ rather than $2\gamma$. Signed divisors and individual
coordinate zeros are included.

I independently multiplied the scalar channel matrices. For the first
family, with coefficients $(k,-\gamma,\gamma)$, their three-step
products are
$$
\begin{pmatrix}-\gamma&0\\1-\gamma k&\gamma\end{pmatrix},
\qquad
\begin{pmatrix}\gamma&0\\1-\gamma k&-\gamma\end{pmatrix}.
$$
For the second family the coefficients are $(k,\gamma,-\gamma)$,
and the two products are
$$
\begin{pmatrix}\gamma&0\\1+\gamma k&-\gamma\end{pmatrix},
\qquad
\begin{pmatrix}-\gamma&0\\1+\gamma k&\gamma\end{pmatrix}.
$$
Substitution of the respective initial channel vectors gives exactly
$Y_k^3(v)=-\gamma v$ in both cases. The denominator words are
$(1,-\gamma k,\gamma k)$ and $(1,\gamma k,-\gamma k)$,
respectively, so no forward pole occurs. They have least period
three for every $k\ne0$, and the states are nonzero. This verifies
the exact native periods three and six as claimed, not only a
divisor bound. The closed periodic orbit also retains every inverse
denominator $E=D_{\mathrm{previous}}\ne0$.

## 4. Quotient order four: exhaustion of invariant branches

The order-four condition becomes
$$
k\gamma\lambda=(\gamma\lambda+1)(\gamma+\lambda),
\qquad B\ne0.
$$
If $\gamma\lambda=0$, both parameters vanish. Otherwise
$k=\gamma+\lambda+1/\gamma+1/\lambda$, and the reciprocal
sum is an integer.

For opposite signs that sum lies strictly between $-1$ and $1$;
it must vanish, forcing $k=0$, outside this stratum. For two
positive integers it is one or two. These give respectively
$(2,2)$ or $(1,1)$; changing both signs gives the negative
cases. Thus the displayed invariant list is exhaustive.

For $(\gamma,\lambda)=(0,0)$, the unit-section equation is
$E^2+(t-1)E+1-t=0$, where $t=\varepsilon k$.
$E=1$ is not a root. For $E\ne1$, integrality of
$t=-E-1/(E-1)$ leaves only $E=0$ or $2$.
The former is a pole; the latter forces $|k|=3$, incompatible
with $E=2\mid k$. This removes the whole arbitrary-$k$ branch.

The involution $U(p,q,r,s)=(s,r,q,p)$ directly satisfies
$Y_{-k}U=UY_k$. It preserves both denominators and sends
$(\gamma,\lambda)$ to $(-\lambda,-\gamma)$, so the negative
branches are fully covered by the positive checks.

For $(\gamma,\lambda,k)=(2,2,5)$, the two section equations
are $E^2=0$ and $E^2-2E+10=0$, giving no nonzero real $E$.
At $(1,1,4)$ they are $(E-1)(E+2)=0$ and
$E^2-3E+6=0$. The latter has negative discriminant; either
root of the former gives the same cycle of ordered quotient
states, with denominator word $(1,4,-2,4)$.

At its $(D,E)=(1,4)$ section the products are
$pq=ps=rs=0$ and $rq=3$. Since $r,q$ are nonzero, both
$p,s$ must vanish. Thus every integral factorization has exactly
the claimed form $(0,q,r,0)$ with $qr=3$.

Direct native substitution gives
$$
(0,q,r,0)\to(r,0,0,q)\to(-r,q,r,q)
\to(-r,q,-r,-q)\to(0,-q,-r,0).
$$
The four denominators are nonzero, the quotient has least period
four, and the last state is the negative of the first. The map
commutes with simultaneous negation, so the least native period
is exactly eight. The $U$ images prove all statements at $k=-4$.
No rational scaling orbit has been presumed integral or periodic:
all integral factors and their actual returns have been checked.

## 5. Quotient order five: both discriminant branches

With $d=\gamma\lambda$, $S=\gamma+\lambda$ and $B=d+1$,
the order-five equation is $dk^2-BSk+B^3=0$ with $B\ne0$.

For $d\ne0$, its quadratic discriminant is exactly
$$
B^2\big((\gamma-\lambda)^2-4\gamma^2\lambda^2\big).
$$
For nonzero integer parameters,
$|\gamma-\lambda|\le|\gamma|+|\lambda|\le2|\gamma\lambda|$.
Equality throughout requires opposite signs and both absolute
values one, which gives $B=0$, excluded. The discriminant is
therefore strictly negative in the permitted branch, so there
is no real $k$.

For $d=0$, $B=1$ and the equation reduces to $kS=1$.
Thus $k=\pm1$. The inherited divisibility $D\mid k$
restricts each nonzero denominator to $\{1,-1\}$.
There are at most four ordered states $(D,E)$, and a deterministic
ordinary quotient orbit cannot have least period five among them.
This completes the zero-product invariant branch as well.

## Remaining issues and limits

**Mandatory corrections: none.** The arithmetic equalities,
inequality directions, signs, coefficient/native clocks, zero-coordinate
branches, pole exclusions, and necessity/sufficiency steps all check
out for the frozen auxiliary statements.

This PASS does not supply a mechanism for quotient orders
$6,7,8,9,10,12$. For those orders the rational multiplier may still
fail to be $\pm1$, or the needed integral rank-one factorization may
fail; neither issue is decided here. No unproved relationship between
a Miller function and the native scaling multiplier may be used to
remove this boundary. In particular an exhaustive list of possible
rational orders is not an exhaustive ordinary integral atlas.

The new unit-section/divisibility lemma and complete low-order strata
are valid helper progress. The full frozen contract remains open, and
these helpers are not recommended as another independent paper slot.
The independently handled CP9 decision does not change that conclusion.

## Source, skill and execution receipt

All external mathematics used here is either an explicitly accepted
round-eight input or elementary arithmetic/chord calculation written
out above. This reviewer did not perform fresh external source
verification for AY9 and does not claim the older author's primary
paper accesses as its own. Mazur, the classical source map/invariants,
QRT reduction and the group framework retain their earlier ownership.
New source checks subsequently recorded by the author are not silently
incorporated into this hash-pinned proof review.

The already read proof-writer and research-review instructions
govern exact claims and adversarial checking. Repository/current-team
instructions replace legacy external-model review examples; ARS is
limited to honest source-status boundaries, not a new full pipeline.
Current-task fresh web queries: **0**. Mathematical programs: **0**.
Old diagnostics/builds/proof checks rerun: **0**. External models,
GPU, PDF downloads, Git writes and author-file edits: **0**.

A first document-write orchestration call had a JavaScript string
delimiter error and executed no patch or shell command. The corrected
document write is not a mathematical diagnostic.

Final disposition: the four AY9 auxiliary claims **PASS** for the
fixed hash above, with **zero remaining mandatory corrections**.
The original all-parameter structural atlas is **NOT CLOSED**.
