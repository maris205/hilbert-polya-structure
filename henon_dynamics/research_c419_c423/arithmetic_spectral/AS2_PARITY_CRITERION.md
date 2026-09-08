# Proof package: second, parity-sensitive AS2 candidate

2026-09-07. This is a new explicitly labelled repair of the same all-level
question, after the original conjecture failed at $N=50$ and its first
repair failed at $N=100$. No parameter family or basis convention changes.

## Claim

Define $\mathcal P(N)$ by requiring, for every primitive character $\chi$
of conductor $q$ with $q^2\mid N$,

$$
\chi^4=1,\qquad
\chi(p)^2=1\quad\text{whenever }p\mid N,\ p\nmid q,
\text{ and }v_p(N)\text{ is odd}.
$$

The first equation is an identity on units. The second imposes no
condition at ramified primes and no condition at even prime exponents.

**Arithmetic lemma.** $\mathcal P(N)$ is equivalent to all of:

1. $v_2(N)\le9$, $v_3(N)\le3$, $v_5(N)\le3$, and
   $v_p(N)\le1$ for primes $p\ge7$.
2. If $v_5(N)\ge2$, every prime $p\ne5$ with $v_p(N)$ odd satisfies
   $p\equiv\pm1\pmod5$.
3. If $v_2(N)\ge8$, every odd prime $p$ with $v_p(N)$ odd satisfies
   $p\equiv\pm1\pmod8$.

**Separate analytic theorem.** The original full cusp scattering family
is pairwise commuting at all regular parameters if and only if
$\mathcal P(N)$. The [assembled analytic proof](independent_review/REPAIRED_CLASSIFICATION.md)
supplies this equivalence. Its nonauthor review has passed, and the
coordinator has admitted this full classification as one contract.

## Status

Arithmetic lemma: **PROVABLE AS STATED**.

Analytic theorem: **COMPLETE PROOF; NONAUTHOR REVIEW PASS**.
The full fixed-coordinate character/tensor argument and both necessity
mechanisms are explicitly assembled, and the coordinator has read them.
The principal block and local phase-parity results alone were insufficient;
the [proof index](AS2_PROOF_INDEX.md) identifies the additional arguments.
The full classification is admitted as one contract; this status does not
assert worldwide literature novelty or a completed manuscript.

## Assumptions and notation

Use positive integer levels and the unchanged width-one, trivial-nebentypus
contract. Set $m=\prod_p p^{\lfloor v_p(N)/2\rfloor}$ and
$m^{(p)}=m/p^{v_p(m)}$. Finite unit groups, primitive inducing characters
and the classical duality/prime-power facts are exactly those explicitly
listed in the [first arithmetic proof](AS2_REPAIRED_CRITERION.md).

## Proof strategy and dependency map

The conductor-square clause is unchanged. Only the set of primes at which
the additional unit congruence is required changes. Steps 1–2 of the first
arithmetic proof determine the exponent bounds; its Step 3 is now applied
only at primes of odd exponent, and Step 4 resolves the same congruences.
No unproved analytic implication is a premise of this elementary lemma.

## Proof

### Step 1. The conductor-square part

All primitive characters with conductors dividing $m$ correspond to the
complete dual of $U_m$. Requiring their fourth powers to be trivial says
that $U_m$ has exponent dividing $4$. By its prime-power decomposition,
this occurs precisely for $m=2^r3^u5^v$ with $r\le4$ and $u,v\le1$.
Taking floors in the definition of $m$ gives item 1 exactly.

### Step 2. The odd-exponent part

Fix a prime $p$ for which $v_p(N)$ is odd. The permitted primitive
characters whose conductors are coprime to $p$ comprise the dual of
$U_{m^{(p)}}$. Their values at $p$ all have square $1$ if and only if
every dual character is trivial on $p^2$, hence if and only if

$$
p^2\equiv1\pmod {m^{(p)}}.
$$

This equivalence is character separation, with no statement imposed
at a prime of even exponent.

### Step 3. Resolve the congruences

All units have square $1$ modulo $3$ and modulo $2^r$ for $r\le3$.
The only further restrictions are modulo $5$, when $5\mid m$, and
modulo $16$, when $16\mid m$. For $p\ne5$, the first is equivalent to
$p\equiv\pm1\pmod5$. For odd $p$, the second is equivalent to
$p\equiv\pm1\pmod8$. Applying these only to the primes selected in
Step 2 gives items 2 and 3. CRT proves sufficiency for every factor of
$m^{(p)}$, completing the equivalence. $\square$

## Why the second repair is materially different

The first repair wrongly excluded every imaginary unramified quartic
phase. In the actual local incoming matrices, its effect depends on the
parity of the oldform-chain length. At an even exponent a constant phase
change reduces both paired directions to the same principal matrix
family. At an odd exponent a fixed half-chain sign interchanges the two
central eigenchannels. The analytic proof must justify this reduction on
the full cusp space and rule out cancellation among different primes.

Thus $N=50$ is still excluded, but $N=100$ satisfies the new condition.
Mixed even powers such as $N=2^8 5^2$ are not discarded merely because
both quartic conductors are available. These are consequences/predictions
of the candidate condition, not a new computational level census.

## Open risks and boundaries

The assembled analytic proof explicitly addresses the full fixed-character
decomposition, general-level nonreal-square necessity with imprimitive
Euler factors, odd-phase necessity despite tensor products, and regular
exceptional parameters. Independent internal review checked those
arguments and their source applicability with no unresolved blocker;
see the [proof index and completed review](AS2_PROOF_INDEX.md).

The arithmetic lemma and small counterexamples alone remain too thin for
a paper slot. No chronological clock, target Euler-factor/root-number
dictionary, zero correspondence or Hilbert–Pólya realization is supplied.
