# P71 Official Round-1 Hostile Mathematical Review

## Provenance

- Date: 2026-08-25.
- Review posture: user-requested `GPT-5.4, xhigh` hostile first-round review, performed directly in-thread without delegation.
- Files read for substance: `main.tex`, `math_commands.tex`, `references.bib`, all manuscript sections `sections/0_abstract.tex` through `sections/8_conclusion.tex`, the proof/control/claim/source ledgers in the package root, `code/verify_degree_pressure.py` and its recorded output, and all prior review/resolution files under `reviews/` and `rounds/`.
- I did not rely on generated PDF/image/auxiliary artifacts for theorem correctness.

## Overall verdict

**Internal theorem verdict:** **PASS**  
**Release posture:** **HOLD**

I tried to break the manuscript at the four places most likely to fail:

1. the earlier illicit replacement of Bowen entropy by type-counting capacity entropy;
2. the countable-union / variable-length Carath\'eodory step;
3. the endpoint `t -> +/- infinity` handling in the Legendre formula;
4. periodic negative-coordinate phase/index alignment.

In the current draft I do **not** find a live mathematical defect in any of those places. The pressure theorem, uniqueness of the Bernoulli equilibrium, derivative/curvature formulas, Bowen-spectrum proof, endpoint formulas, natural-extension entropy bridge, profile recovery, conjugacy iff profile, and weighted periodic/zeta identities all close under independent reconstruction.

## Severity-ranked defects

### CRITICAL

None.

### MAJOR

None.

### MINOR

None that block theorem correctness.

### Residual release gate that is **not** a theorem defect

- The package still does **not** have an external specialist priority/source clearance. The bounded citation audit is not a novelty certificate, and the active neighboring thermodynamic zip-shift work remains a real release risk. This is a release gate, not a proof gap.

## Theorem-by-theorem reconstruction

### 1. Local degree and natural extension

- `sections/2_model_extension.tex:23-37` is correct. For fixed `x`, every preimage `y` is forced at all coordinates except `y_0`, and `y_0` must lie in `tau^{-1}(x_{-1})`, so `d_tau(x)=k_{x_{-1}}`.
- `sections/2_model_extension.tex:53-95` also closes. An inverse history records exactly the forgotten symbol at each negative time, so the inverse limit is canonically `S^Z`, and the lifted potential is `log k_{tau(t_{-1})}`.
- The invariant-measure bridge is adequately proved, not merely asserted: equation `(2.5)` gives the unique affine lift, and the generating-partition argument is sufficient for equality of metric entropies.

### 2. Pressure, uniqueness, and derivatives

- `sections/3_pressure.tex:11-57` is mathematically sound.
- After the natural-extension reduction, the potential is one-coordinate on the full two-sided `|S|`-shift. For any invariant process with one-symbol marginal `p`, entropy rate is at most `H(p)`, and the Gibbs/log-sum inequality gives
  `H(p) + t sum_s p(s) log k_{tau(s)} <= log sum_s k_{tau(s)}^t`.
- Equality forces the stated marginal `p_t(s) proportional to k_{tau(s)}^t`, and entropy-rate equality forces Bernoulli independence. That gives both the pressure formula
  `P_tau(t)=log sum_z k_z^(t+1)`
  and uniqueness of the equilibrium state.
- Differentiating the finite log-sum gives the `r_t`-mean and `r_t`-variance of `log k_z`; strict convexity fails exactly in the uniform-profile case.

### 3. Metric/folding entropy bridge

- `sections/3_pressure.tex:72-90` uses Martins--Mattos--Var\~ao exactly where it should and does not overclaim ownership.
- For the Bernoulli equilibrium, `H(p_t)=P_tau(t)-tP_tau'(t)` by direct averaging of `-log p_t`.
- Because `p_t` is uniform inside each fibre, the conditional entropy within a fibre is `log k_z`, and averaging over `r_t` gives folding entropy `P_tau'(t)`.

### 4. Weighted periodic identity and zeta

- `sections/4_periodic_rigidity.tex:6-32` is closed. The coordinate formula
  `x_i=s_{i mod n}` for `i>=0` and `x_{-j}=tau(s_{(-j) mod n})` for `j>=1`
  fixes the cyclic phase correctly.
- The degree list along one `n`-orbit is the cyclic permutation
  `k_{tau(s_{n-1})}, k_{tau(s_0)}, ..., k_{tau(s_{n-2})}`, so the weighted sum factorizes to `Q_tau(t)^n`.
- I independently spot-checked the periodic coordinate formula on small examples; I found no indexing shift.
- `sections/4_periodic_rigidity.tex:43-55` then gives the zeta identity immediately.

### 5. Profile recovery and conjugacy iff profile

- `sections/4_periodic_rigidity.tex:61-113` is correct.
- Under conjugacy, preimage sets are bijected pointwise, so local degree is preserved. On fixed points, degree-`k` points are counted by `N_k = k m_k`, which recovers the multiplicity `m_k`.
- Equal profiles clearly give the one-block conjugacy `(beta, alpha)` with `kappa alpha = beta tau`.
- If pressure curves agree for all `t`, then
  `R_tau(u)=exp(P_tau(u-1))=sum_k m_k k^u`
  agrees identically. Since this is a finite positive exponential sum, the largest base `K` is `lim_{u->infty} R_tau(u)^{1/u}`, its coefficient is `lim_{u->infty} R_tau(u)/K^u`, and finite recursion recovers the entire profile multiset. No coefficient-loss bug remains.

### 6. Bowen spectrum: upper bound

- This was the historical danger point. In the current draft, `sections/5_multifractal.tex:89-119` is a genuine Bowen-Carath\'eodory argument, not a disguised capacity argument.
- `sections/5_multifractal.tex:23-65` first proves the exact cylinder identity for `(n,2^{-M})` Bowen balls:
  one must fix the past block `[-M,-1]` and the future block `[0,n+M-1]`, and nothing more.
- That identity is the missing bridge between the two-sided zip system and one-sided type counting. It shows the past and terminal-future overhead contributes only `|Z|^M |S|^M`, independent of `n`.
- Then `Y_{N,eta}` is covered at **arbitrary** lengths `n>=N`, not one fixed length. The Carath\'eodory sum is bounded by
  `const(M) * poly(n) * exp(-n(s-H_{alpha,eta}))`,
  which tends to `0` for each `s > H_{alpha,eta}`. This is the correct Bowen upper-bound mechanism.
- The countable-union step is now explicit: the exact level set lies in `union_N Y_{N,eta}`, and countable stability of Bowen entropy gives the conclusion. I do not see an unproved countable-union leap remaining.

### 7. Bowen spectrum: lower bound, fibre optimization, Legendre duality

- `sections/5_multifractal.tex:121-155` also closes.
- The lower bound uses the right object: a fixed-past / Bernoulli-future law `nu_p` on the zip space. It is not required to be invariant; it is only used for the entropy-distribution principle.
- For `nu_p`-generic futures, the degree exponent is `alpha`, and the Bowen-ball mass has exponential rate `H(p)` because the Bowen-cylinder identity fixes exactly one future block of length `n+M`. This is the correct local-entropy lower bound.
- The fibre-grouping step is exact:
  `H(p) = H(r) + sum_z r_z H(p(.|z)) <= H(r) + sum_z r_z log k_z = H(r) + alpha`,
  with equality when mass is uniform inside each fibre.
- The Legendre upper bound is the Gibbs inequality rewritten. For interior `alpha`, equality is attained at the unique `t` with `P_tau'(t)=alpha`.

### 8. Endpoint cases

- I specifically checked the endpoint danger that often gets mishandled when passing from the interior Legendre formula.
- For `alpha = log k_max`, the feasible measures are exactly those supported on symbols lying over maximal fibres, so the entropy maximum is `log(k_max m_{k_max})`. Likewise for `k_min`.
- On the pressure side,
  `P_tau(t) - t log k_max = log(sum_z k_z^(t+1)) - t log k_max`
  tends to `log(k_max m_{k_max})` as `t -> +infinity`, and similarly at `-infinity` for `k_min`.
- So the endpoint formulas in `sections/5_multifractal.tex:157-166` are correct. I do not see a surviving `t/q` endpoint error.

## Earlier known failure modes: status

- Earlier Bowen-versus-capacity flaw: **closed** by `sections/5_multifractal.tex:89-119`.
- Earlier countable-union / variable-length cover gap: **closed** by `sections/5_multifractal.tex:101-119`.
- Earlier periodic indexing-shift risk: **closed** by `sections/4_periodic_rigidity.tex:18-31`.
- Earlier endpoint risk: **closed** by the current endpoint handling in `sections/5_multifractal.tex:147-166`.

## Exact required fixes

### Required mathematical fixes

None.

### Required release/posture fixes

1. Keep the manuscript on **external hold** until a specialist source audit is done against the current zip-shift / extended-shift thermodynamic literature.
2. Do not convert the bounded source search into a novelty or priority claim.
3. Preserve the current owner-subtraction posture for Lamei--Mehdipour and Martins--Mattos--Var\~ao.

## Remaining source/priority gates

- The package correctly states that the bounded search found no exact source collision, but that statement is not a certificate.
- The active neighboring project on thermodynamic formalism for zip shifts is enough reason to keep release frozen until a specialist checks whether any exact pressure/multifractal/profile-rigidity overlap already exists in current or in-press work.
- This gate is external-literature risk, not an internal-proof risk.

## Final hostile verdict

I do **not** find a mathematical basis to reject P71 on theorem correctness in its current form. The current draft survives hostile reconstruction of the pressure theorem, Bernoulli equilibrium uniqueness, derivative formulas, Bowen-spectrum proof, endpoint cases, natural-extension entropy bridge, profile rigidity, full profile recovery, and weighted periodic/zeta identities.

**Internal status:** **PASS**  
**External status:** **HOLD**

## EXTERNAL RELEASE HOLD

Do not externally release, claim novelty, or claim priority until the specialist source/priority audit is completed.
