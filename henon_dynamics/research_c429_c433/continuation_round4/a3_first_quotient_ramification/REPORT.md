# A3/R4: the general first-quotient ramification break

2026-09-09 UTC. New proof-only task allocated by the coordinator. Every reviewed round-three file remains unchanged.

## Exact question and outcome

For every odd prime $p$, let $K=\overline{\mathbb F}_p((s))$, $v(s)=1$, and retain the original native map $P_s(z)=(1+s)z+z^2$. Let $L_e/K$ be its canonical degree-$p^e$ small-cycle field, and $F_e$ its unique degree-$p$ subfield. The full local theorem and the oriented identity $F_e=F_2$ for $e\ge2$ are accepted inputs, not new conclusions of this task.

The frozen new question is to determine the exact ramification break of $F_2/K$ for every odd $p$, not merely show that $F_2\ne L_1$ or infer a pattern from $p=3$.

**Author outcome: PROVABLE AS STATED; independent whole-proof review pending.** The complete argument in [PROOF_PACKAGE.md](PROOF_PACKAGE.md) gives

$$
b(F_e/K)=2(p-1)\qquad(e\ge2).
$$

Equivalently, the reduced first AS class at every such level has highest pole exactly $2(p-1)$. Its leading coefficient is nonzero; no formula for that coefficient or for the remaining coefficients at general $p$ is asserted. The already certified $p=3$ class remains $2s^{-4}+s^{-2}$.

## New mechanism and imported material

Work in the accepted disjoint compositum $B=L_2L_1$, of degree $p^3$, with $\eta=\alpha_2-\beta_1$. Exact imported contacts give

$$
a=v_B(\eta)=2p(p-1)^2,\qquad
v_B(g\eta-\eta)\ge A=2p^2(p-1),
$$

with equality for the independent native generators acting on one field at a time. The integer $a$ is divisible by $p$ but not by $p^2$, so the earlier prime-valuation lemma cannot be used directly.

A new explicit cancellation lemma shows that, at the first lower break $b_0$, the first nonzero uniformizer exponent of $\eta$ prime to $p$ is $a+(p-1)b_0$. The first ramification graded quotient has order $p$, and every later displacement is exactly that exponent plus its lower break. This deals with the cancellation rather than suppressing it. Elementary-abelian quotient bookkeeping excludes every ordering in which $b(F_2)\le p-1$, including coincident individual conductors and cancellation between their characters. The remaining ordering forces the displayed exact answer.

Classical inputs are explicitly subtracted: reduced AS representatives and their conductor, Hasse--Arf/Herbrand quotient compatibility, and the cyclic degree-$p^2$ inequality $u_2\ge p u_1$. The relevant primary statements were checked in Elder--Keating, [Section 2, Lemmas 2.1--2.2 and Theorem 2.3](https://arxiv.org/html/2503.16830v1), over arbitrary perfect residue fields. The uniform contacts, full local inertia, oriented stabilization, and $L_1\cap L_2=K$ remain the reviewed round-three inputs. No broad literature-priority claim is made for the elementary cancellation lemma or this corollary.

## Verification and boundaries

The author proof treats the entire first graded quotient, the uniformizer tail, the possibility of equal conductors with a lower-conductor character combination, persistence of the order-$p$ kernel, and the exact upper/lower normalization. A separately allocated B4 author-side crosscheck is complementary work, not independent whole-proof acceptance.

No mathematical program, new precision, old certificate rerun, manuscript/PDF, shared-state, evaluation or Git action was performed. Only this allocated report and its proof package were written. No higher-Witt coefficients, full-field nesting, all-level higher breaks, global cycle-quotient transitivity, or additional paper admission follows from this task.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
