# R4 A1 report: optimal-cycle probability measures

2026-09-09 UTC. Author status: **PROVABLE AS STATED, pending independent
actual-file review**. This is not a paper-admission or source-priority
decision.

## Exact question and outcome

The proof retains the full parameters of Lindahl–Rivera-Letelier
[Problem 1.3](https://arxiv.org/html/1311.4478v3#S1.SS3): every odd prime
$p$, every complete algebraically closed ultrametric field $K$ of
characteristic $p$, and every $\lambda$ with $0<|\lambda-1|<1$.
For $P(z)=\lambda z+z^2$ and its actual single cycle $\Pi_e$ of least
period $p^e$ in the open unit disk, the real probability measures
$\mu_e=p^{-e}\sum_{\alpha\in\Pi_e}\delta_\alpha$ converge weakly on
the Berkovich projective line. The proof additionally puts all the
measures and their limit on one compact subset of the classical field.

The full 470-line author proof is [PROOF_PACKAGE.md](PROOF_PACKAGE.md).
Its SHA-256 at this review handoff is

`038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e`.

## Reusable arithmetic interface

Set $s=\lambda-1$, $v(s)=1$, and $r=(p-1)/p$. For any
$\beta\in\Pi_d$ put $\delta_j=v(P^{\circ p^j}(\beta)-\beta)$ and
$A_d=v((P^{\circ p^d})'(\beta)-1)$. Steps 3–5 prove

$$A_d=\delta_{d-1}+
\sum_{j=0}^{d-1}(p-1)p^{d-j-1}\delta_j<\infty,$$

and, for every $e>d$,

$$\frac1{p^e}\sum_{\alpha\in\Pi_e}v(\beta-\alpha)
=c_d:=\frac{p-1}{p^{d+1}}A_d
\ge d r^3+r^2(1+1/p)\longrightarrow+\infty.$$

At least one contact is at least its average. The exact isometry
$P(x)-P(y)=(x-y)(1+s+x+y)$ then yields an aligned native-orbit
coupling of $\mu_e,\mu_d$ supported on distances at most
$|s|^{d r^3+r^2(1+1/p)}$, uniformly over every $e>d$. Step 6 proves
total boundedness and applies the Riesz representation theorem on
the resulting compact classical space; no ambient local compactness
or whole-Berkovich-space metrizability is assumed.

## Source subtraction and dependencies

- The source supplies the actual distinct cycle, its common sphere,
  and minimal ramification of the reduction $z+z^2$.
- The canonical small-factor/Hensel interface is proved again in
  Step 1, including an isometric coefficient embedding
  $\overline{\mathbb F}_p((t))\hookrightarrow K$, $t\mapsto s$.
  Every source-provided cycle point is a root, and degree identifies
  the whole simple factor; no extra genericity premise is introduced.
- The B4 exponential displacement lemma is reproduced directly over
  arbitrary $K$ in Step 3. The R3 low-anchor derivative identities
  motivated the new all-anchor average, but their full-inertia and
  oriented-cluster conclusions are not premises.
- The proof does not guess exact higher displacements, assert nested
  field extensions, or substitute top-cluster matching for convergence.
- Initial bounded primary-source searches did not identify a checked
  later solution. The coordinator assigned a separate source-status
  review. Neither this report nor an old source question establishes
  current openness or priority.

## Review and scope

E2 was allocated the independent arithmetic and specialization review;
the exact file above is now ready. D1 supplies a separately written
general isometric-cycle/odometer criterion, but no unreviewed D1 theorem
is needed for this proof's convergence conclusion. An odometer
identification is not claimed by the A1 theorem.

All R3 admitted files, shared state, manuscripts and Git remain
unchanged. No mathematical computation or external model upload was
performed. No mathematical gap is known in this author proof; source
status and independent review remain explicit external checks.
