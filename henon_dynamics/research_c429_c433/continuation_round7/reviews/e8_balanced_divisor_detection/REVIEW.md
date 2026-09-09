# E8 independent full review: the balanced quadratic divisor atom

2026-09-10 UTC. Current-team nonauthor mathematical review under the
proof-writer, research-review and repository batch instructions.
Only the allocated R7 review is written; frozen R6 inputs are not
reopened or modified. No external-model review is claimed.

## Exact reviewed version and verdict

The reviewer read the complete actual
[A1 report](../../a1_balanced_divisor_detection/REPORT.md), all 379 lines,
and independently checked its arguments and boundary cases by hand.
The reviewed SHA256 is
`59f79d718d85e0c2b4bbaea2e8d78416b5cb48e52927fe044605fb5847bc6e8f`.
The hash was checked again after the mathematical audit.

**The auxiliary parameter reduction and the all-parameter non-torsion
statement are PROVABLE AS STATED.** Mathematical must-fixes: **0**.
Imported-source applicability must-fixes: **0**. Required minor repairs:
**0**. No correction of the author's mathematical claim is required.

**The original full atom sublemma remains NOT CURRENTLY JUSTIFIED.**
The surviving family $f=x^2-1$, $a=\pm1$, for every odd prime, is not
settled by the report. This review neither proves (CP) in that family
nor proves infinitely many bad cycles there. The complete MS6 existence
implication remains open as well.

## Claim, assumptions, notation and dependency map

Fix any odd prime $p$, $k=\overline{\mathbf F}_p$, $c\in k$ and
$a\in k^\times$. The map and observable are

$$f(x)=x^2+c,\qquad w(x)=g_a(x)=\frac{x-a}{x+a}.$$

The native time step is one application of $f$. A good ordinary
primitive cycle avoids $\{a,-a\}$ and has product of $w$ equal to one,
with each distinct point used once. Condition (CP) says that all but
finitely many primitive cycles are good. No prime-to-$p$ restriction
is imposed on the cycles in this definition.

The original all-parameter sublemma asks for infinitely many bad cycles
disjoint from the support, for every allowed $p,c,a$. What is proved is

$$
(\mathrm{CP})\Longrightarrow c=-1,\quad a\in\{1,-1\},
$$

together with infinite order of every $[w]$ in
$k(x)^\times/\{h\circ f/h:h\in k(x)^\times\}$.
Consequently the infinite-bad conclusion holds outside, but is not
established inside, the displayed residual family.

The checked dependency chain is:

1. Return-germ conjugacy and prime repetition control the multiplicities
   used in aggregate products, without altering ordinary cycle products.
2. An elementary Euclidean argument controls an integer dividing
   $\ell-1$ for every sufficiently large prime $\ell$.
3. Aggregate products at $\ell$ and at one force a signed support point
   onto a cycle of period at most two.
4. A separate aggregate after removing the support root rules out every
   noncritical support cycle, regardless of its period.
5. The remaining critical cycle has precisely the stated parameters.

The divisor non-torsion proof is independent of this chain. Neither it
nor the R6 conditional saturation theorem supplies the missing (CP)
existence implication.

## 1. Multiplicities on arbitrary cycles: PASS

For $F_n=f^{\circ n}-X$, all root products in the proof use polynomial
multiplicities. If a cycle of least period dividing $n$ contains the
critical point, the derivative of $f^{\circ n}$ is zero at every point
of that cycle. The derivative of $F_n$ is then $-1$, and all those
roots are simple. This includes periods divisible by $p$.

Otherwise each map between successive cycle points has a nonzero
derivative, hence an inverse as a formal local coordinate change.
Commutation of $f$ with $f^{\circ n}$ conjugates the return germs.
An invertible coordinate change preserves the order of a germ minus
the identity, giving the same multiplicity at every cycle point.

For the repetition claim, $N$ and a finite set in $\operatorname{Fix}
(f^{\circ N})$ are fixed before choosing $\ell$. If the local
multiplier $\theta$ is zero, both multiplicities are one. If
$\theta\ne0,1$, its order $t$ is finite in $k^\times$ and exceeds
one. A prime $\ell>t$ cannot be divisible by $t$, so
$\theta^\ell\ne1$; both multiplicities are again one.

If $\theta=1$, the return germ is not the identity: otherwise the
nonzero polynomial $f^{\circ N}-X$, of degree $2^N>1$, would have
zero formal expansion. Write its first difference as $uz^m$ with
$u\ne0$ and $m\ge2$. Composition adds this first coefficient, so
the first difference of the $\ell$th return is $\ell uz^m$.
For $\ell\ne p$ this is nonzero and the multiplicity stays $m$.

There are only finitely many original points, so a common prime bound
exists. The proof does not assume any bound on the multiplicities of
new cycles appearing in $F_{N\ell}$, or on all periodic points at once.
Their potentially wild multiplicities are harmless because the ordinary
product of each new good cycle is one.

## 2. Every atom has infinite multiplicative order: PASS

The divisor $D=[a]-[-a]$ is nonzero because $2a\ne0$, and
$f_*D=0$ because $f(a)=f(-a)$. Divisors can be taken on
$\mathbf P^1$, including infinity; this does not change the affine
cycle observable. If $w^m=h\circ f/h$ for $m\ge1$, then

$$mD=f^*E-E,\qquad 2E=f_*E,\qquad E=\operatorname{div}(h).$$

The identity $f_*f^*E=2E$ counts ramification multiplicities and
therefore applies to critical fibers as well. The finite-support real
$\ell^1$ norm satisfies $\|f_*E\|_1\le\|E\|_1$ by the triangle
inequality after coefficients with the same image are merged. Thus
$2\|E\|_1\le\|E\|_1$, so $E=0$ and $mD=0$, a contradiction.

These are integer divisor coefficients, not elements of $k$. In
particular, multiplication by $p$ cannot erase $D$. All positive
integer-power relations, including every $p$-power transfer, are
excluded. This is a non-torsion theorem, not a proof that (CP) fails.

## 3. The all-large-prime Euclidean argument: PASS

Assume that an integer $t>2$ divides $\ell-1$ for every prime
$\ell$ exceeding a fixed bound $B$. Enlarge $B$ if necessary and
let $Q$ contain each prime at most $B$ not dividing $t$ once.
Then $tQ-1>1$ has no prime factor at most $B$: such a prime divides
either $t$ or $Q$, and in either case $tQ-1$ is $-1$ modulo it.

Every prime factor of $tQ-1$ must therefore be $1$ modulo $t$.
Multiplying with the actual prime-factor exponents gives
$tQ-1\equiv1\pmod t$, whereas its definition gives $-1$.
This forces $t\mid2$, contradicting $t>2$.

The same argument with $t=p>2$ gives arbitrarily large primes not
congruent to one modulo $p$. Excluding the single prime $p$ or any
other fixed finite set does not affect the conclusion. No progression
theorem, prime-density estimate or unproved prime-distribution premise
is used.

## 4. Aggregate products force a short support cycle: PASS

If a signed support point is fixed, the desired short-cycle conclusion
already holds. Otherwise neither is fixed. Choose every prime $\ell$
above the periods of all (CP) exceptions and above any period of a
periodic signed support point. Also impose the finite multiplicity bound
for $F_1$ and $\ell\ne p$. The support is then disjoint from both
root sets $F_1=0$ and $F_\ell=0$.

Every root of $F_\ell$ is fixed or has exact period $\ell$.
Every latter cycle is good, and its common root multiplicity raises
its ordinary product one to an integer power. The original fixed-point
multiplicities agree. Hence the aggregate products at these two levels
are equal even when the original fixed cycles themselves are bad.

For a monic $F_n$, the two signs in the numerator and denominator
root products cancel. Evenness of $f^{\circ n}$ gives the exact ratio

$$
\prod_{F_n(\alpha)=0}w(\alpha)
=\frac{F_n(a)}{F_n(-a)}
=\frac{f^{\circ n}(a)-a}{f^{\circ n}(a)+a}.
$$

The products here include multiplicities. None of these numerator or
denominator values vanishes at the two levels being compared.
Since $2a\ne0$, equality of the ratios forces
$f^{\circ\ell}(a)=f(a)$ for every sufficiently large prime $\ell$.

Put $b=f(a)$. A single such equality makes $b$ periodic, and its
least period $t$ divides $\ell-1$ for all those primes. Section 3
gives $t\le2$. The predecessor $u$ of $b$ in its periodic cycle
satisfies $u^2=a^2$, so $u=a$ or $u=-a$. This also handles strictly
preperiodic support: periodicity of $a$ was not assumed to obtain
periodicity of $b$ and of one of its two signed predecessors.

The conclusion depends on the full sufficiently-large-prime quantifier,
not on a chosen infinite congruence class of primes.

## 5. The noncritical support and the exact scaling factor: PASS

Replacing $a$ by $-a$ inverts $w$, preserving (CP) and bad cycles.
Assume therefore that $a$ is periodic of least period $r$, with
nonzero return multiplier $\lambda$. The other signed point cannot
be periodic: a point on a periodic cycle has exactly one periodic
predecessor, whereas $f(a)=f(-a)$ and $a\ne-a$.

Let $t$ be the finite order of $\lambda$ and fix $N=rt$ before
varying $\ell$. The germ of $f^{\circ N}$ has multiplier one
and nonzero first difference $uz^m$. At $N\ell$, for
$\ell\ne p$, that coefficient is exactly $\ell u$ and the
multiplicity at $a$ remains $m$.

Choose primes above all exceptional-cycle periods and the common bound
for every root of $F_N$. If an exceptional period $s$ divides
$N\ell$, then $\ell>s$ gives $\gcd(s,\ell)=1$, hence $s\mid N$.
Thus no new exceptional cycle enters. All original multiplicities,
including those at the other points of the support cycle, are unchanged.

Define $J_n$ by removing the root $a$ entirely from the multiplicity
product, for $n=N,N\ell$. It has no remaining zero and no pole,
because $-a$ is never periodic. The other points of the support cycle
form an unchanged partial product. The other old exceptional cycles
are also unchanged; all remaining complete cycles contribute one.
This proves $J_{N\ell}=J_N$ without requiring the support cycle
itself to be good.

The independent factorization check is

$$
F_n(X)=(X-a)^mH_n(X),\quad H_n(a)=u_n,\quad
F_n(-a)=2a,\quad H_n(-a)=\frac{2a}{(-2a)^m}.
$$

Since $H_n$ is monic, its root-product ratio gives

$$
J_n=\frac{H_n(a)}{H_n(-a)}
=(-1)^m(2a)^{m-1}u_n.
$$

All factors divided by are nonzero. With $u_N=u$ and
$u_{N\ell}=\ell u$, this yields $J_{N\ell}=\ell J_N$,
where $J_N\ne0$. The unchanged-product equality would require
every sufficiently large prime $\ell$ to be one modulo $p$,
contradicting Section 3. The argument includes $r=1$, $t=1$, and
periods or tangency degrees divisible by $p$; no division by them
occurs.

## 6. Classification, infinitude and the residual interface: PASS

Under (CP), a signed nonzero support point lies on a cycle of period
one or two, and that cycle must have multiplier zero. Since $f'=2x$,
it contains the unique critical point zero. It cannot be a fixed
cycle, whose sole point would then be zero. Thus it is
$0\mapsto c\mapsto0$, with $c\ne0$ and $c^2+c=0$.
It follows that $c=-1$ and the nonzero cycle point is $-1$, giving
$a=\pm1$ exactly.

Outside those parameters, finitely many bad cycles disjoint from
the support would imply (CP), since at most two additional cycles
can meet the two support points. This contradicts the reduction.
The result is therefore infinitely many distinct bad primitive cycles,
not merely one bad cycle or a finite failed test.

For $f=x^2-1$, a cycle avoiding $\{1,-1\}$ also avoids zero:
zero belongs to the exceptional two-cycle containing $-1$.
Thus the additional avoidance used to define $A_O,B_O,C_O$ does
not secretly discard any otherwise eligible cycle. All three products
are nonzero. Permuting cycle points gives $B_O=A_O^2$ and
$B_OC_O=A_O$, hence

$$\prod_O g_1=A_O^{-3},\qquad \prod_O g_{-1}=A_O^3.$$

Both signs have exactly the same good-cycle criterion $A_O^3=1$.
Under (CP), with its one globally finite exceptional set, the nonzero
multiplier $\lambda_O=2^{|O|}A_O$ would satisfy
$\lambda_O^{3(p-1)}=1$. This follows from $2\in\mathbf F_p^\times$
and $A_O^3=1$; for $p=3$ the latter even implies $A_O=1$.
These are necessary interfaces only. No bounded-multiplier rigidity
theorem is supplied or inferred.

At the critical two-cycle every positive return has derivative zero,
so its difference from the identity has linear coefficient $-1$.
There is no varying nonzero $\ell u$ coefficient of the type used in
Section 5. This locates the failure of that argument but proves neither
(CP) nor its failure for any part of the remaining all-odd-prime family.

## Sources, remaining obligation and execution receipt

The mathematical proof in Steps 1--6 is direct. Its formal-coordinate,
root-factorization, finite-field and divisor identities have been
checked above; it imports no external theorem whose applicability is
needed for the positive verdict. R6 conditional saturation and the
R7 A2 existence interfaces are explicitly not used as existence inputs.

The author's search receipts and Levy scope discussion are not an
ingredient of this proof and are not independently recertified here.
No additional source search or proposed solution of the residual was
undertaken. The review makes no worldwide-priority or new-paper claim.

The exact remaining obligation is to prove, for every odd $p$, infinitely
many eligible cycles of $x^2-1$ with $A_O^3\ne1$, or exhibit specific
allowed parameters where only finitely many fail. Neither conclusion
is established. Non-torsion of the atom alone does not decide which
occurs, because the MS6 periodic-to-torsion implication is precisely
what is unavailable.

Verification consisted of the actual complete author text, independent
hand mathematics, file readback and read-only hashes. There were no
mathematical programs, new agents, external API/model calls, Git actions,
old/shared-author edits, manuscript changes or PDF work. The only new
workspace write is this allocated review. The batch skill retains the
result as an auxiliary discriminator rather than an admitted contract.
`NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
