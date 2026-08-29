# Claims–Evidence Map

Status: refrozen after two author-side hostile-review passes and one
independent internal cross-hostile repair; external release **HOLD**.

| Claim | Proof anchor | Independent exact control | Residual risk |
|---|---|---|---|
| Every finite chronological composition is an interval clamp or a constant | Theorem 2.1; update identities (6)–(7) | Exhaustive normal-form lane through length 7, including pointwise comparison at every rank breakpoint | Equivalent semigroup normal forms may exist in prior literature |
| Nonconstant exactly when the largest floor threshold is below the smallest cap threshold | Theorem 2.1 | Exhaustive record/crossing check for every type word and rank permutation through length 7 | Ties require the deterministic weak inequality; stochastic ties vanish only under atomlessness |
| Distribution-free survival `P(T>n)=sum_j p^j q^(n-j)` | Theorem 3.1 | Aggregate enumeration and a separately organized fixed-type rank lane | Conditional rank probabilities are stated only for reachable `N_n=j`; the unconditional law holds for all `p` |
| Survival PGF, exact mass, and `T =_d Geom(p)+Geom(q)` for `0<p<1` | Theorem 3.1 | Exact tail-difference versus convolution, rational coefficient recurrence, and mass-plus-tail closure | Endpoint laws are improper and are stated separately |
| `E T=1/(pq)` and `Var(T)=(1-3pq)/(p^2q^2)` | Theorem 3.1 | Exact rational moment identities at five interior parameters | None beyond the geometric convention stated in the theorem |
| Critical `(n+1)2^-n` and off-critical asymptotics | Corollary 3.2 | Exact rational identities through time 60 | Asymptotic equivalence itself rests on the displayed closed form |
| For uniform thresholds, `E diam(Phi_n(I))=P(T>n)/(n+1)` | Theorem 4.1 | Rank-gap sums in both exhaustive lanes | Conditional expectations require `P(N_n=j)>0`; endpoints use separate pure-map order-statistic proofs |
| Uniform-threshold critical, endpoint, and annealed rates | Theorem 4.1 | Exact rational special-case and endpoint lanes | The signed logarithmic rate and positive decay exponent use opposite signs; both are defined |
| Mixed paths collapse after finite time and are not assigned a conventional finite Lyapunov exponent | Remark 4.2 plus Theorem 3.1 | Exact normal-form absorption checks | Terminological boundary, not an independent stochastic limit theorem |

The script is a finite falsification control and does not replace the proofs.
Bibliographic search absence is not used as evidence of novelty.

## Assumption firewall

- The finite-word normal form is deterministic and includes threshold ties.
- Distribution-free probability statements require iid atomless thresholds
  and type/threshold independence.
- Every expression conditional on `N_n=j` is restricted to
  `P(N_n=j)>0`: all `j` are reachable for `0<p<1`, only `j=0` at `p=0`,
  and only `j=n` at `p=1`.
- The diameter identity and endpoint mean are specialized to Lebesgue-uniform
  thresholds; they are not asserted for an arbitrary atomless law.
- `p=0,1` are not limits silently imported from the geometric decomposition:
  they are proved separately and have `T=infinity` almost surely.
- “Quenched” is used only for the pathwise finite-absorption contrast. No
  finite Lyapunov exponent is claimed after the image becomes a singleton.

## Owner subtraction

The manuscript credits and subtracts general iterated-random-function
theory (Diaconis–Freedman), general iid monotone-map synchronization
(Matias–Silva), finite-chain contraction semigroups (Umar–Zubairu), and
standard rank/order-statistic facts. The residual conjunction still requires a
specialist direct-owner search before any external novelty claim.
