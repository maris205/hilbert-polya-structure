# Round 3 A3: interlevel contact and local degree

2026-09-09 UTC. Exclusive author lane allocated by the coordinator. All first-pass and round-2 author/review files are read-only. Proof-only work; no mathematical execution allocated or performed in this lane.

## Frozen question and bounded control

The original local target remains unchanged: for every odd prime $p$ and $e\ge1$, the canonical small factor $M_e$ of the native period-$p^e$ dynatomic polynomial for

$$
P_s(z)=(1+s)z+z^2,\qquad K=\overline{\mathbb F}_p((s)),\quad v(s)=1
$$

is irreducible of degree $p^e$ over $K$, equivalently its first reduced AS quotient is nonzero. The original global PC424-D additionally requires global cycle-quotient transitivity; it is not replaced by this local question.

The new mechanism compares a level-$e$ root $\alpha$ with a native prime-level root $\beta$ and studies the Galois compositum rather than a single branch different. One native application of $P_s$ remains one tick.

**Bounded control theorem:** at $(p,e)=(3,2)$, prove irreducibility from the accepted polynomial discriminant value $v_s\operatorname{Disc}(M_2)=144$, the small-cycle inputs, and prime-level inertia. The level-two AS calculation and its nonzero conclusion are expressly excluded as premises. Success is a complete noncircular contact/ramification proof; failure is a precisely located missing implication. This does not authorize another computation of the discriminant or AS class.

**Uniform proof obligation:** identify an explicit contact hypothesis at all levels which would force the full degree, prove the resulting criterion, and separate that criterion from any unproved assertion that the actual contacts satisfy it. Subsequent proof work has now computed the actual prime-level contact uniformly, yielding the second-layer theorem stated below and refuting that particular higher-level contact hypothesis.

## Source subtraction and exact inputs

- The unique small cycles, degree-$p^e$ Hensel factors, exact native periods and common valuation $r=(p-1)/p$ are the accepted LRL/first-pass A3 inputs.
- The root field of a single small cycle is the cyclic splitting field of degree $p^h$, $1\le h\le e$. Its actual Galois subgroup acts by multiples of $p^{e-h}$ native steps. It is not assumed that a one-step rotation is a field automorphism.
- The prime-level field is cyclic degree $p$ with break $p-1$. These accepted inputs are not new results here.
- The bounded control's only computational input is the order/polynomial discriminant value $144$ from the existing round-2 producer. [E2's complete review](../../continuation_round2/reviews/e2_local_as/REVIEW.md) independently audits that value's computation/precision. E2's separate AS result is true but not used. The new uniform second-layer proof uses neither this discriminant value nor any higher-level AS computation.
- Classical ramification numbering, quotient compatibility, and the prime-valuation displacement lemma are stated with their hypotheses in the [proof supplement](PROOF_SUPPLEMENT.md). These are not new ramification theory.

The proof-writer skill governs the separation of proved claims from the uniform contact gap. The existing batch workflow governs review and author-lane boundaries. No paper or evaluation is proposed.

## Current result

**Author proofs complete; independent review pending.** The [supplement](PROOF_SUPPLEMENT.md) proves a general contact-degree criterion, the bounded discriminant-only control, and a stronger uniform theorem requiring no computation:

$$
v(\alpha_e-\beta_1)=\frac{2(p-1)^2}{p^2},
\qquad [K(\alpha_e):K]\ge p^2
\quad\text{for every odd }p,\ e\ge2.
\tag{Second layer}
$$

In particular, **$M_2$ is irreducible for every odd prime $p$**. This is a complete uniform second layer, not the all-level theorem. Section 6 derives the contact by differentiating the dynatomic quotient identity at a prime-level root, evaluating its multiplier valuation, and equalizing the resulting root contacts. No level-two AS nonvanishing is used as an input.

The decisive pair contact is

$$
v(\alpha-\beta)=\frac89.
$$

If the level-two field had degree $3$, its compositum with the prime-level field would have degree $9$. The difference $\alpha-\beta$ would have integer-normalized valuation $8$, prime to $3$, and would force the compositum's first lower/upper break to be $4$. Its prime-level quotient already has break $2$, a contradiction.

For arbitrary odd $p$, $e\ge2$ and $2\le\nu\le e$, the proved criterion says that a contact $d=v(\alpha-\beta)$ satisfying

$$
p^\nu d\in\mathbb Z\setminus p\mathbb Z,
\qquad
d<2r-\frac{p-1}{p^\nu}
\tag{C$_\nu$}
$$

forces $[K(\alpha):K]\ge p^\nu$. The actual uniform contact above satisfies it for $\nu=2$.

The initially proposed contact law with $\nu=e$ is **refuted for every $e\ge3$** by the exact formula: the denominator remains $p^2$. This is a failure of that sufficient proof route, not a counterexample to full inertia. The uniform higher-level target remains **NOT CURRENTLY JUSTIFIED** for $e\ge3$. The inequality alone is not enough: the exact denominator is essential.

The same proof gives the exact native displacement $v(P_s^{\circ p}(\alpha_e)-\alpha_e)=2(p-1)$ for all $e\ge2$. All these are theorem deductions from the accepted small-cycle setup, not new executions or finite-table extrapolations.

## Remaining work and invariants

The next dynamical task is a genuinely higher-level comparison with an already understood cycle of level at least $2$, including its clustered distance profile and known quotient ramification. The prime-level contact calculation is now complete and demonstrably stops at degree $p^2$. No higher-level induction is claimed. B4's separate single-field discriminant/upper-bound lane remains distinct.

No new mathematical run, producer rerun, source/old-artifact modification, manuscript/PDF, formal evaluation, Git action, external model upload or new agent allocation occurred here.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
