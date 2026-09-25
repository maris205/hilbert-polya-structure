# Independent raw-card proof — variable-multiplier admission

Screen: `ANG-SCREEN-20260921-VMA01`. Date: 2026-09-21.
Reviewer: `/root/algebraic_henon_author`; internal AI, `NOT_CALIBRATED`.
Disposition: **MAIN F FAIL / A FAIL; all three OWN controls F PASS / A PASS.**

## Input, instruction use and independence boundary

Sole scientific input: [candidate-card](../candidate-card.md), all lines 1–93,
including its EOF marker; `wc -l` confirmed 93 and SHA-256 was
`0755f26b9b18287cca9f0a0c6ab4ad42e0e3c56703e4011389abe43d8bb9cba8`.
No main manuscript, peer/scout report, other package, old proof or web source
was opened. The card itself discloses root's anticipated obstruction and older
workflow statements: exposure is acknowledged, not a blind-discovery claim.
The decisive mathematics was sent to root before this report was written.

ARS instruction record: its complete 488-line `SKILL.md` had already been read
in this agent context and was reread in full in this task, without truncation.
The complete deep-research workflow, model-runtime policy and Devil's Advocate
role had been read in preceding tasks and were reused, not newly reread here.
The installed router is at
`/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/3.22.0/skills/academic-research-suite/SKILL.md`.
This is a scoped raw-card proof after root's CP1 release, not a Hénon/C-paper
workflow. No auxiliary agent, numerical experiment, model change or scoring quota.

## 1. Entire image and every predecessor fibre

Write `K=product_p Z_p`, with product normalized Haar, and `X=K²`.
For a target `(a,b)`, every predecessor is `(u,a)` with `a*u=b-1`.
For each prime p, the complete coordinate condition is:

- if `a_p=0`, require `b_p=1`, and then allow EVERY `u_p in Z_p`;
- if `a_p!=0`, require `b_p-1 in a_p Z_p`; then the unique solution is
  `(b_p-1)/a_p` in `Z_p` (division is performed in `Q_p`).

If any coordinate condition fails the fibre is empty. Otherwise assemble all
coordinate solutions; equivalently it is `(u0+Ann_K(a)) x {a}`, where
`Ann_K(a)` has coordinate `Z_p` when `a_p=0` and `{0}` otherwise.
Thus the exact image is `I={(a,b): b-1 in aK}`; it is compact/Borel because
T is continuous on compact X. No component, annihilator translate or null
state was removed. In particular `T^-1(0,1)=K x {0}`.
For ordinary integers `d>=1,n`, `du=n` is solvable in K iff `d|n`:
necessity follows by reduction modulo d, and sufficiency by the integer quotient.

## 2. F fails: the entire image is Haar-null

For each prime p put
`C_p={(a,b): a not congruent 0 mod p OR b congruent 1 mod p}`.
The preceding equation gives `I subset C_p`, and counting residue pairs gives

    mu(C_p)=((p-1)*p+1)/p²=1-1/p+1/p².

CRT and product Haar imply, for every finite prime set P,

    mu(intersection_(p in P) C_p)=product_(p in P)(1-1/p+1/p²).

These products tend to zero. Indeed each factor is at most `exp(-1/(2p))`,
and `sum_p 1/p` diverges. For completeness, convergence of that sum would bound
`product_(p<=N)(1-1/p)^-1`, using `-log(1-u)<=2u` for `0<=u<=1/2`.
But expansion of this finite Euler product includes every term `1/n`, `n<=N`,
so it dominates the divergent harmonic partial sum, a contradiction.
Continuity of measure for the decreasing finite intersections now gives
`mu(intersection_p C_p)=0`, hence `mu(I)=0`.
Nevertheless `T^-1(I)=X`. Thus `T_*mu(I)=1` and `T_*mu` is singular with
respect to mu; in particular **F fails**. This is an infinite exact image
argument, not a finite-modulus extrapolation or a fibre-cardinality argument.

## 3. A fails independently of any etale requirement

K is uncountable (already its `Z_2` coordinate is). Every source set U on
which T is injective contains at most one point of `K x {0}`, the complete
fibre over `(0,1)`. Countably many such U cannot cover that fibre.
Therefore no countable full injective inverse atlas exists, even before
Borel regularity or the IMAGE densities are imposed: **A fails**.

There is also a separate measured-atlas contradiction from Section 2. If A
held, every `V_i` would lie in I and have measure zero. Taking `E=V_i` in its
required every-Borel identity gives `mu(U_i)=integral_(V_i) J_i dmu=0`.
A countable collection of such U_i cannot cover the probability space X.
Neither argument discards zero divisors or chooses an inverse representative.

## 4. FIXED: its own full inverse and IMAGE

Multiplication by 2 is injective on K: each `Z_p` has characteristic zero
and no zero divisors. Its image `2K` is clopen with Haar measure `1/2`.
Consequently `T_F(x,y)=(y,2x+1)` is a homeomorphism from X onto
`V_F=K x (1+2K)`, with inverse `theta_F(a,b)=((b-1)/2,a)`.
Both inverse identities follow by substitution, with division unique on `2K`.

The pushforward of Haar under `x->2x` is normalized Haar on `2K`:
it is translation-invariant there and has total mass one. Thus it equals
`2*h|_(2K)`. Translation by 1 and exchanging independent coordinates yield,
for EVERY Borel N in X, `mu(T_F^-1 N)=2*mu(N intersect V_F)`.
In particular for EVERY Borel E in V_F,
`mu(theta_F(E))=2*mu(E)`. The one-branch atlas has `U_F=X`, `J_F=2`
at every retained point. Hence **FIXED F/A both pass**; surjectivity onto X
is neither asserted nor required.

## 5. UNIT-FEEDBACK: its own full inverse and IMAGE

Let `epsilon(a)=1-2(a mod 2)`. The global inverse of
`T_U(x,y)=(y,epsilon(y)*x+1)` is
`theta(a,b)=(epsilon(a)*(b-1),a)`; `epsilon(a)^2=1` proves both identities.
Parity is clopen, so these maps are continuous. The specified two branches
are exactly `U_j={y mod2=j}`, `V_j={a mod2=j}` and their full inverses.
For any Borel E in V_j write `E_a={b:(a,b) in E}`. Fubini and Haar invariance
under translation and multiplication by ±1 give

    mu(theta_j(E))=integral h(epsilon(a)*(E_a-1)) dh(a)
                 =integral h(E_a) dh(a)=mu(E).

Thus `J_j=1` on EVERY V_j, including null states. Applying the same identity
globally shows `T_U*mu=mu`. **UNIT-FEEDBACK F/A both pass** on its own X.

## 6. ADDITIVE: its own full inverse and IMAGE

`T_A(x,y)=(y,x+y+1)` has the continuous global inverse
`theta_A(a,b)=(b-a-1,a)`; substitution proves both identities.
For every Borel E in X, its sections give
`mu(theta_A(E))=integral h(E_a-a-1) dh(a)=integral h(E_a) dh(a)=mu(E)`.
Thus the full one-branch atlas has `J_A=1`, and `T_A*mu=mu`.
**ADDITIVE F/A both pass**, by its own translation calculation.

## 7. Scoped conclusion

Stop/fork the MAIN admission route specified in this card. All full sources,
images and fibres remain intact; controls do not repair MAIN. No clock was
supplied or constructed, and passing control F/A does not establish arrow-clock
coherence, packets, primitive periods or a flow. This does NOT exclude arbitrary
non-etale groupoids, uncountable Haar systems, conditional fibre measures,
other reference measures or other clocks. T2/T3 were not audited; classical
A0/A1/A2 are not applicable; formal Route unassigned and B not invoked.
