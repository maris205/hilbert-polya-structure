# Proof package: arithmetic form of a repaired AS2 criterion

2026-09-07. AI-generated repair after the independently found $N=50$
counterexample. This is an arithmetic lemma and a separately labelled
scattering conjecture, not an admission or a paper.

## Claim

For $N\ge1$, define condition $\mathcal C(N)$ as follows. Every primitive
Dirichlet character $\chi$ of conductor $q$ with $q^2\mid N$ satisfies

$$
\chi^4=1\quad\hbox{on }(\mathbb Z/q\mathbb Z)^\times,
\qquad
\chi(p)^2=1\quad\hbox{for every prime }p\mid N\hbox{ with }p\nmid q.
$$

The arithmetic claim is that $\mathcal C(N)$ is equivalent to all of:

1. $v_2(N)\le9$, $v_3(N)\le3$, $v_5(N)\le3$, and
   $v_p(N)\le1$ for every prime $p\ge7$.
2. If $v_5(N)\ge2$, every prime $p\ne5$ dividing $N$ satisfies
   $p\equiv1$ or $-1\pmod5$.
3. If $v_2(N)\ge8$, every odd prime $p\mid N$ satisfies
   $p\equiv1$ or $-1\pmod8$.

**Separate conjecture:** the full width-one cusp scattering family from
[the original contract](FROZEN_CONTRACTS.md) commutes at all regular
parameters if and only if $\mathcal C(N)$. Nothing in the elementary proof
below establishes that analytic equivalence.

## Status

Arithmetic equivalence: **PROVABLE AS STATED**, by the proof below.

Scattering equivalence: **FALSE AS A PROPOSED NECESSARY CONDITION**.
Subsequent fixed-coordinate analysis shows that an imaginary quartic phase
at an even unramified oldform exponent can cancel. In particular the full
level $N=100$ family commutes, although item 2 above fails. The full-sector
proof is recorded; the arithmetic equivalence in this file remains correct
and unchanged. The second, separately stated
[parity-sensitive theorem](AS2_PARITY_CRITERION.md) now has a complete
proof and passed nonauthor review.
Neither this failed repair nor the original conjecture is silently erased.

## Assumptions and notation

- $v_p(N)$ is the nonnegative prime exponent in the positive integer $N$.
- Set $m=\prod_p p^{\lfloor v_p(N)/2\rfloor}$. Then $q^2\mid N$ if and
  only if $q\mid m$.
- $U_d=(\mathbb Z/d\mathbb Z)^\times$, with $U_1$ trivial.
- The exponent of a finite group is the least positive integer annihilating
  all its elements. A real-valued character here has values in $\{1,-1\}$
  on units; its value at a prime dividing its conductor is zero and is not
  constrained by the second condition.

## Proof strategy and dependency map

Use finite abelian character duality to replace the quantifier over primitive
conductors by conditions on unit groups. Then apply the classical structure
of unit groups of prime powers and the Chinese remainder theorem (CRT).

The only imported algebraic facts are: every Dirichlet character is induced
from a unique primitive character; characters separate elements of a finite
abelian group and its dual has the same exponent; $U_{p^r}$ is cyclic of
order $(p-1)p^{r-1}$ for odd $p$; and
$U_{2^r}\simeq C_2\times C_{2^{r-2}}$ for $r\ge3$, with the usual
trivial and order-two cases at $r=0,1,2$. These are classical inputs, not
new results. No scattering formula, computation or density theorem enters
this lemma.

## Proof

### Step 1. Replace primitive conductors by a single unit group

The characters of $U_m$ are in bijection with primitive characters whose
conductors divide $m$: pull a primitive character back along reduction and,
in the reverse direction, take its unique primitive inducing character.
Pullback preserves its image and order. Thus the first clause of
$\mathcal C(N)$ says precisely that the exponent of the dual of $U_m$
divides $4$. Finite abelian duality makes this equivalent to
$\operatorname{exp}(U_m)\mid4$.

### Step 2. Determine all possible square-root levels

CRT makes the exponent of $U_m$ the least common multiple of its prime-power
unit exponents. For an odd prime power $p^r\mid m$ with $r\ge1$, the
divisibility $(p-1)p^{r-1}\mid4$ forces $r=1$ and $p\in\{3,5\}$.
For $2^r\mid m$, the stated unit-group structure gives $r\le4$.
Therefore the first clause holds exactly when

$$
m=2^r3^u5^v,\qquad 0\le r\le4,\quad u,v\in\{0,1\}.
$$

The definition of $m$ translates this statement exactly into item 1 of
the claim, including odd exponents of $N$ and the boundary $N=1$.

### Step 3. Detect the extra-prime obstruction by duality

Fix a prime $p\mid N$ and put $m^{(p)}=m/p^{v_p(m)}$. The primitive
characters in our family whose conductors are prime to $p$ correspond
exactly to all characters of $U_{m^{(p)}}$. Since $p$ is a unit modulo
$m^{(p)}$, their values at $p$ all have square $1$ if and only if every
character of this group is $1$ on $p^2$. Character separation gives the
equivalent condition

$$
p^2\equiv1\pmod {m^{(p)}}.
$$

This step retains the conductor restriction: it does not incorrectly ask
for the nonzero value $\chi(p)$ when $p\mid q$.

### Step 4. Resolve each allowed prime-power congruence

Under Step 2, modulo $3$ every unit already has square $1$. Modulo $2^r$
for $r\le3$, every odd unit has square $1$. These factors impose no new
condition in Step 3.

If $5\mid m$, then for every $p\ne5$ dividing $N$ the remaining condition
is $p^2\equiv1\pmod5$. Factoring in the field $\mathbb F_5$ makes this
equivalent to $p\equiv\pm1\pmod5$. The hypothesis $5\mid m$ is exactly
$v_5(N)\ge2$, giving item 2.

If $16\mid m$, then for every odd $p\mid N$ the remaining condition is
$p^2\equiv1\pmod {16}$. Checking the four odd residue classes modulo $8$
gives square $1$ modulo $16$ precisely at $1$ and $7$ modulo $8$.
The hypothesis $16\mid m$ is exactly $v_2(N)\ge8$, giving item 3.

CRT now proves that items 2 and 3 are sufficient as well as necessary for
all congruences in Step 3. Together with Step 2 this proves the arithmetic
claim. $\square$

## Historical consequences used during analytic proof development

These are consequences of $\mathcal C(N)$ only, not an assertion that it
characterizes scattering.

- A quartic primitive character can occur only when $5^2\mid N$ or
  $2^8\mid N$. The two possibilities cannot occur together: item 2
  excludes the additional prime $2$, and item 3 excludes the prime $5$.
- In the first case $2$ and $3$ cannot divide $N$; in the second case
  $3$ and $5$ cannot divide $N$. All unramified oldform primes in a
  quartic sector therefore have exponent one in $N$.
- If neither possibility occurs, every character in the conductor family
  is real. At this stage, commutativity on every real-character oldform
  sector still required proof; a fixed character span was not enough.
  The final parity-sensitive proof now supplies that missing argument.
- At $N=50$, item 1 holds but item 2 fails because $2\not\equiv\pm1\pmod5$.
  The repair therefore excludes the known counterexample without changing
  its original object or its basis convention.

## Corrections and open risks

The elementary equivalence is a classical group-theoretic calculation and
is not a substantial paper by itself. Its connection to scattering was
only conjectural and is now disproved in the necessity direction: clause
(b), requiring reality at every unramified prime exponent, was too strong.
The replacement must retain exponent parity. Both directions on the
complete fixed cusp space, tensor products and exceptional spectral
parameters were outstanding obligations of that replacement. They are
now proved in the separately linked parity-sensitive theorem; that does
not rescue this false first repair. No $s$-dependent similarity may be
used to infer commutativity.

There is still no autonomous source clock, target Euler-factor dictionary,
root number, zero/divisor correspondence or Hilbert–Pólya realization.
NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.
