# Round 2 A3 — full-layer local AS nonvanishing

2026-09-09 UTC. Author `/root/c429_a3_wild_tower`. Frozen before new mathematical execution or substantial new proof. First-pass author/reviewer files are read-only.

## Frozen lemma and scope

For **every odd prime $p$ and every integer $e\geq1$**, put

$$
k=\overline{\mathbb F}_p,\quad R=k[[s]],\quad K=k((s)),
\quad v_s(s)=1,\quad n=p^e,\quad m=p^{e-1},
$$

$$
P_s(z)=(1+s)z+z^2,\qquad
Q_e(z,s)=\frac{P_s^{\circ n}(z)-z}{P_s^{\circ m}(z)-z}.
$$

Let $M_e\in R[z]$ be the unique monic Hensel factor of $Q_e$ whose reduction is $z^n$. Write $E_e=K[z]/M_e$, $\alpha=[z]$, and $\sigma\alpha=P_s(\alpha)$. The finite étale algebra $E_e$ is a native $C_n$-torsor, not assumed to be a field. Define

$$
w_e=\frac{\alpha^{n-1}}{M_e'(\alpha)},\qquad
y_e=-\sum_{i=0}^{n-1}(i\bmod p)\sigma^i(w_e),\qquad
a_e=y_e^p-y_e\in K.
$$

The exact target is

$$
\operatorname{red}_{\mathrm{AS}}(a_e)\neq0\quad\text{for all odd }p\text{ and all }e\geq1,
\tag{AS-full}
$$

where $\operatorname{red}_{\mathrm{AS}}$ is the unique finite negative-power representative with exponents prime to $p$ modulo $\wp(K)=\{b^p-b:b\in K\}$. Success means a uniform proof, or a rigorously verified counterexample to (AS-full); a finite positive table does not prove it. A counterexample defeats this local route, not automatically the original global component claim.

The coordinate substitution $c=(1-s^2)/4$, $x=z+(1+s)/2$ is a tame proof device inside the original quadratic family. One application of $P_s$, equivalently $f_c(x)=x^2+c$, is one native tick. The original PC424-D asks for all geometric irreducible components of the full reduced dynatomic curve, for all odd $p,e$, including $(3,1)$. Even (AS-full) leaves the global native-cycle quotient transitivity problem open. Local lengths are not ordinary distinct point counts.

## Accepted inputs and source subtraction

The current Hénon AGENTS, CONTINUOUS_RUN, FIRST_PASS_DECISION, the complete E2 final review and relevant A4 proof interfaces were read. The proof-writer skill is used to preserve exact quantifiers and an explicit gap if the proof stops.

- LRL Theorem C already gives the unique small native cycle and optimal root valuation $v_s(\alpha)=(p-1)/p$ for this exact $\lambda=1+s$ family, all odd $p,e$. Its minimally ramified iterate formula and these consequences are fully subtracted.
- First-pass A3/E2 give the canonical Hensel factor, generic separability/exact period, splitting group $H_e\leq C_n$, $p\mid |H_e|$, and full inertia at $e=1$.
- A4/E2 give the trace-one formula, choice-independent class $[a_e]$, and the equivalence $(\mathrm{AS\!\! -\!\!full})\Longleftrightarrow H_e=C_n$ at each pair.
- E2 gives the fixed-pair pole bound $a_e\in s^{-pD_e}R$, where $D_e=v_s\operatorname{Disc}_z(Q_e)<\infty$. It is accepted as a precision interface, not a performed computation or uniform nonvanishing theorem.

## Initial strategy and execution boundary

Try to force the missing unit rotation by local ramification, native iteration identities or a uniform leading polar coefficient in $a_e$. A relation between the degree-$p$ quotients at different levels must be proved, not assumed. We will not treat the prime-level class as the first quotient of every higher cycle.

No mathematical execution is authorized yet. Before any diagnostic, send the coordinator explicit $(p,e)$ inputs, the discriminating alternatives, pole/truncation precision, algorithm and bounded time/memory estimate. No old rerun, census, LaTeX/PDF, formal evaluation, shared-file/Git write or external-model upload is permitted.

## Status at freeze

**NOT CURRENTLY JUSTIFIED** for (AS-full) beyond the accepted $e=1$ case. No new result or mathematical execution claimed.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.

## Proposed bounded diagnostic — not yet allocated or run

**Discriminating pair:** only $(p,e)=(3,2)$, so $n=9$, $m=3$ and $\deg_zQ_e=504$. This is the first level not covered by the accepted valuation argument. Outcomes $\operatorname{red}_{\rm AS}(a_2)=0$ and $\ne0$ distinguish a genuine counterexample to (AS-full) from evidence supporting one further layer; a nonzero outcome will not be generalized to all pairs.

**Exact algorithm:** over $\mathbb F_3[[s]]$ truncated at an explicit order, form the nine iterates and exact dynatomic quotient, isolate the degree-$9$ factor $M_2\equiv z^9\pmod s$ by coprime Hensel lifting, compute the determinant valuation $\delta=v_s\operatorname{Disc}(M_2)$, and evaluate the accepted trace-one resolvent inside the rank-$9$ algebra. Compute all negative coefficients through the certified bound $3\delta$, then AS-reduce the finite polar polynomial. A regular part is irrelevant over $\overline{\mathbb F}_3$.

**Precision/cost cap:** initially $s^{128}$, then at most one refinement to $s^{512}$; abort as inconclusive unless the determinant's first nonzero coefficient is actually visible and the propagated precision proves every required negative coefficient. A conservative acceptance threshold is $N>4\delta+8$, with all inverse/substitution precision losses tracked explicitly. No larger pair, no automatic precision increase, and no root-factor census. Proposed resource envelope: at most 20 CPU minutes and 2 GiB RAM, in the assigned new lane only; choose exact finite-field polynomial arithmetic available locally. Program execution still requires the coordinator's separate allocation.

The diagnostic is motivated by a genuine alternative: the source-owned root slope forces only degree divisible by $p$, and higher native cycles could conceivably split into several conjugate factors over the same smaller cyclic local extension. Nothing in the accepted theorem excludes this. It is not a conjectured counterexample before execution.

## Allocated diagnostic 1 — actual result

The coordinator explicitly allocated exactly the proposed pair/precision envelope. [diagnostic_p3_e2.py](diagnostic_p3_e2.py) was created with `apply_patch`. Actual command, from this directory:

```sh
bash -o pipefail -c 'timeout --kill-after=5s 1500s prlimit --cpu=1200 --as=2147483648 -- python3 -u diagnostic_p3_e2.py 2>&1 | tee execution.log'
```

The complete [execution.log](execution.log) records one parameter pair and **exit 2 / INCONCLUSIVE_AT_ALLOCATED_CAP**. Exact Hensel checks passed through $s^{512}$. The determinant valuation is certified as

$$
\delta=v_s\operatorname{Disc}(M_2)=144,
$$

with leading coefficient $1$. The initial $s^{128}$ stage could not see the determinant; the $s^{512}$ stage sees it but fails the precommitted strict acceptance condition $N>4\delta+8=584$. The program therefore did **not** evaluate or claim the AS class. Actual reported time was about $0.84$ CPU seconds and $0.77$ wall seconds, well within the allocated limits. No larger input or automatic precision escalation occurred.

A separate request was sent for one changed-precision continuation on the same pair at $s^{1024}$, under a new $60$ CPU-second / $120$ wall-second / $2$ GiB cap. It remains unallocated at this record point. The first code/log are preserved. This is a concrete newly measured precision requirement, not evidence for either AS vanishing or nonvanishing.

## Allocated diagnostic 2 — changed precision, same pair

The coordinator subsequently approved exactly that continuation. The unchanged first producer is imported by the separately written [N1024 driver](diagnostic_p3_e2_n1024.py). Actual command:

```sh
bash -o pipefail -c 'timeout --kill-after=5s 120s prlimit --cpu=60 --as=2147483648 -- python3 -u diagnostic_p3_e2_n1024.py 2>&1 | tee execution_n1024.log'
```

Actual result: **exit 0 / CERTIFIED_PAIR**, approximately $1.88$ CPU seconds, $1.82$ wall seconds, peak RSS $47{,}352$ KiB. The [complete log](execution_n1024.log) reports

$$
\delta=144,\qquad
\operatorname{polar}(a_2)=s^{-6}+2s^{-4},\qquad
\operatorname{red}_{\mathrm{AS}}(a_2)=2s^{-4}+s^{-2}\ne0.
$$

Thus the author-level computer-assisted result is $H_2=C_9$ **only at $(p,e)=(3,2)$**. All exact Hensel, determinant/Cramer, trace-one, native difference and scalar-output checks passed. The [precision proof](PROOF_SUPPLEMENT.md) proves that $N-4\delta=448>0$ certifies the full negative part through the pole bound $432$. The log includes the complete computed $M_2\bmod s^{1024}$. Independent code/proof review has been allocated but is not claimed complete.

There were **two actual mathematical executions on one parameter pair**, the first inconclusive and the second at the separately authorized precision. First code/log bytes remain unchanged. No further pair or precision was run.

The computed degree-$3$ quotient has break $4$, unlike the accepted first-level break $2$. Consequently the first degree-$3$ subextensions at these two native levels are genuinely different over $K$. This rules out a naive cross-level identification, not full inertia or the original global question.

## Current mathematical disposition

The single-pair local result is nonzero and useful; **the frozen all-odd-$p$, all-$e$ lemma remains NOT CURRENTLY JUSTIFIED**. A uniform nonvanishing mechanism has not been obtained from one computation. PC424-D's separate global quotient transitivity remains open. No new paper, manuscript/PDF or formal evaluation is proposed.
