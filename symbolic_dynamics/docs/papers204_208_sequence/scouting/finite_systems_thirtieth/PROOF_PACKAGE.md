# MRT: complete elementary time formula, complete old-engine subtraction

Author: `/root/thirtieth_finite_scout`. No independent review is claimed.

## Claim and status

For the exact carrier and simultaneous rule in INTAKE.md, the orbit formula,
tail/period classification and constrained-root one-step decoder below are
**PROVABLE AS STATED**. A genuinely fresh two-axis theorem package is
**NOT CURRENTLY JUSTIFIED**: the temporal axis is completely spent by the
old involution-sandwich mechanism, not merely bounded by an old factor.

Assume $n\ge0$, $(a,b)\in I_n^2$, right-to-left composition, and put $r=ab$.
Let $m=\operatorname{ord}(r)$, including $m=1$ for $r=1$. Let $v_3(m)$ be
the exponent of $3$ in $m$. For an integer $u$ coprime to a positive modulus
$d\ge2$, $\operatorname{ord}_d(u)$ denotes its multiplicative order modulo
$d$. No finite data, external theorem, or additional carrier assumption is
used in these deductions.

## Strategy and dependency map

1. The bijective coordinates $(a,b)\leftrightarrow(a,r=ab)$ satisfy
   $a^2=1$ and $ara=r^{-1}$.
2. Direct multiplication gives the full coordinate update and its iterate.
3. Equality of ordered pairs reduces to one exact divisibility condition,
   yielding both the minimal tail and minimal eventual period.
4. Independently solve the one-step target equations for the product $r$.
5. Compare the entire formula with the original B2B-06 sandwich rule and
   its commuting coordinate swap. This is an exact old-engine adapter,
   not a similarity of titles or a no-hit novelty assertion.

## 1. Full coordinates and all iterates

Since $r=ab$ and $a^2=b^2=1$, we have $b=ar$ and
$ara=ba=r^{-1}$. Conversely, if $a^2=1$ and $ara=r^{-1}$, the element
$b=ar$ has square $ara r=1$, proving the asserted bijection.

The first output is $bab=a r^2$. The second is $aba=a r^{-1}$.
Their product is $a r^2 a r^{-1}=r^{-3}$. Thus the complete update is

$$ (a,r)\longmapsto (a r^2,r^{-3}). \tag{1}$$

For $t\ge0$ set $k_t=(-3)^t$ and $e_t=(1-k_t)/2$, which is an integer.
Then

$$T_n^t(a,b)=\bigl(a r^{e_t},\ a r^{e_t+k_t}\bigr),
\qquad r_t=r^{k_t}. \tag{2}$$

At $t=0$ this is $(a,ar)=(a,b)$. Suppose (2) holds at $t$. Applying (1)
adds $2k_t$ to the first-coordinate exponent. Since
$e_t+2k_t=(1+3k_t)/2=e_{t+1}$ and $k_{t+1}=-3k_t$, this proves the
induction and hence (2) for every $t$.

## 2. Exact recurrence, minimal tail and period

For integers $s\ge0$ and $p\ge1$, formula (2) implies

$$T_n^{s+p}(a,b)=T_n^s(a,b)
\iff 2m\mid (-3)^s\bigl((-3)^p-1\bigr). \tag{3}$$

Indeed equality of the first coordinates is equivalent to
$m\mid e_{s+p}-e_s$, hence to the right-hand condition. This same condition
implies $m\mid k_{s+p}-k_s$, so it also forces equality of the second
coordinates. Necessity of (3) already follows from the first coordinate.

Write $m=3^h u$ with $h=v_3(m)$ and $\gcd(u,3)=1$. Because
$(-3)^p-1$ is not divisible by $3$, condition (3) cannot hold when $s<h$.
When $s\ge h$, its $3$-part is satisfied and its remaining part is

$$(-3)^p\equiv1\pmod{2u},$$

since $(-3)^s$ is invertible modulo $2u$. The modulus $2u$ is at least
two and is coprime to $3$. Therefore the exact transient length and exact
eventual period are

$$\mu(a,b)=v_3(m),\qquad
\lambda(a,b)=\operatorname{ord}_{2m/3^{v_3(m)}}(-3). \tag{4}$$

The recurrent states are precisely those whose product has order coprime
to three. These formulas cover $m=1$, $n=0$ and $n=1$: in each case
the modulus is $2$, the multiplicative order is one, and the state is fixed.
They also show directly that $T_n(a,b)=(a,b)$ iff $m\mid2$, equivalently
the two involutions commute.

The factor $r\mapsto r^{-3}$ alone would lose ordered orientation. For
example, if $m=4$, the product is fixed because $-3\equiv1\pmod4$, whereas
the pair period is two because $-3\equiv5\pmod8$. Such an example occurs
in $S_4$: take $r=(1\,2\,3\,4)$, $a=(2\,4)$ and
$b=ar=(1\,4)(2\,3)$. The next pair is
$((1\,3),(1\,2)(3\,4))$, and a second update returns the original.
This is a symbolic substitution, not an executed finite pilot.

## 3. Every target's one-step source set

Fix any target $(c,d)\in I_n^2$ and write $s=cd$. Define

$$R(c,d)=\{r\in S_n:r^3=s^{-1},\quad crc=r^{-1}\}. \tag{5}$$

There is a bijection

$$R(c,d)\longrightarrow T_n^{-1}(c,d),\qquad
r\longmapsto (c r^{-2},c r^{-1}). \tag{6}$$

For necessity, let $T_n(a,b)=(c,d)$ and put $r=ab$. Equation (1) gives
$s=r^{-3}$ and $c=a r^2$. Therefore $r^3=s^{-1}$ and
$crc=a r^3 a r^2=r^{-3}r^2=r^{-1}$. Solving $c=a r^2$ gives the two
coordinates in (6).

Conversely, choose $r$ satisfying (5). Put $a=c r^{-2}$ and $b=c r^{-1}$.
Since $c$ inverts $r$, both $a^2=r^2r^{-2}=1$ and
$b^2=r r^{-1}=1$. Their product is $ab=r^2r^{-1}=r$. Equation (1) then
gives first output $a r^2=c$ and second output
$a r^{-1}=c r^{-3}=c s=d$. The product of a reconstructed source recovers
the chosen $r$, so there is no overcounting. This proves (6), including
unreachable targets, identity products, and empty vertex sets.

Consequently $|T_n^{-1}(c,d)|=|R(c,d)|$. This is a target-local root and
reverser decoder, not a closed evaluated enumeration of those roots and
not an all-target sharp maximum theorem. It carries no claimed novelty.

## 4. Complete original-mechanism subtraction

The original file
`docs/papers117_121_sequence/scouting/ALGEBRAIC_PHASE2B_SCOUT.md`,
section B2B-06, defines on pairs of involutions

$$S(a,b)=(aba,bab)$$

and proves, in the same product coordinates,

$$S^t(a,r)=\bigl(a r^{-(3^t-1)/2},r^{3^t}\bigr).$$

Let $J(a,b)=(b,a)$. Then $J^2=1$, $SJ=JS$ by direct substitution, and
the literal here is $T_n=JS$ on the full original $I_n^2$. Hence

$$T_n^t=J^tS^t. \tag{7}$$

Equations (2)–(4) are exactly the signed version of this already explicit
dihedral word-power formula. All orientation motion is accounted for by
(7); no unspecified factor lift or missing cocycle is being treated as
solved. Transporting matching edges is precisely permutation conjugation,
so the matching description changes no state or transition. Restricting
the old all-finite-group carrier to $S_n$, retaining labels, or increasing
$n$ produces no independent time mechanism.

This is an old-mechanism collision with a commuting swap, not an assertion
that $T_n$ and $S$ are literally identical or necessarily conjugate. No
independent involution-pair period is imported without its orientation
correction. The elementary constrained-root inverse cannot compensate for
the eliminated temporal contribution. **KILL_OLD_SIGNED_POWER_ENGINE /
NO_PROMOTION**.

## Open risks and nonclaims

No global novelty, direct external ownership clearance, sharp fibre maximum,
new labelled root-counting theorem, candidate-gate acceptance, or paper is
claimed. This negative deduction does not show that no other matching or
finite incidence dynamics can work. It closes only the declared literal and
the recorded bounded survey; it does not authorize a new lane.
