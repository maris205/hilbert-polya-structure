# Hostile Review Ledger

Status: two author-side internal adversarial passes plus one independent
internal cross-hostile repair completed; theorem package **GO** for internal
freeze and **HOLD** for external circulation.

This file is a closure ledger, not an external referee report. No external
reviewer identity, score, or endorsement is claimed. Both passes attacked
the formulas from first principles, reran the exact verifier, and rebuilt
the paper through `pdflatex -> bibtex -> pdflatex -> pdflatex`.

## Round 1 — composition, normal form, ties, and endpoints

### Attack

1. Recomputed `F_u o K_[a,b]` and `C_u o K_[a,b]` under the stated forward
   convention `Phi_n=g_n o ... o g_1`.
2. Tested all four strict/non-strict branches at `u=a` and `u=b`, including
   the fact that equality creates a constant.
3. Checked that once a constant occurs, subsequent cap/floor maps may move
   its value but cannot restore positive diameter.
4. Reproved the global criterion: `A_n<B_n` excludes every earlier crossing
   by monotonicity of the records; `A_n>=B_n` forces a first crossing.
5. Attacked the endpoint claim: atomlessness rules out thresholds exactly at
   zero or one, so finite pure-cap/pure-floor words remain nonconstant.
6. Scanned the introduction, abstract, and conclusion for absolute novelty,
   priority, or unqualified external-release language.

### Findings and repairs

- **MAJOR presentation risk, fixed:** the composition convention was stated
  but had no diagnostic example. Added
  `C_(1/4) o F_(3/4)=kappa_(1/4)` versus
  `F_(3/4) o C_(1/4)=kappa_(3/4)` and added a 13-assertion script sentinel.
- **MINOR proof gap, fixed:** the endpoint remark asserted pathwise decay for
  uniform thresholds without showing it. Added
  `P(min_{i<=n}U_i>epsilon)=(1-epsilon)^n` and the symmetric floor argument.
- **No theorem error:** the weak crossing inequality is necessary in the
  deterministic theorem, while stochastic equality disappears under
  atomlessness. The manuscript keeps those scopes separate.
- **No owner overclaim:** general iterated functions, monotone
  synchronization, contraction semigroups, and standard rank facts were
  already subtracted; external status remained HOLD.

### Round-1 closure

The repaired exact run passed 6,948,366 assertions. The four-stage build
produced a five-page PDF with no final log warning or box warning.

## Round 2 — probability law, metric specialization, and terminology

### Attack

1. Reconditioned on the complete type word and on `N_n=j`; verified that the
   binomial coefficient cancels exactly once, leaving
   `sum_j p^j q^(n-j)`.
2. Summed the survival series independently and used
   `(1-E[z^T])/(1-z)` to rederive the pgf.
3. Convolved the two geometric masses and independently recomputed
   `E[T]` and `Var(T)` under the support convention `{1,2,...}`.
4. Checked the critical tail `(n+1)2^(-n)`, the off-critical prefactor, and
   both `p=0,1` endpoints without taking an invalid interior limit.
5. Reproved the uniform-diameter identity using the spacing between order
   statistics `V_(j)` and `V_(j+1)`, including `j=0,n`.
6. Challenged every use of “quenched,” “annealed,” and “Lyapunov.” Exact
   pathwise absorption and expected-diameter decay had to remain distinct.
7. Rechecked the three bibliographic records and the owner-subtracted HOLD
   language against the claims actually made.

### Findings and repairs

- **MAJOR formal ambiguity, fixed:** the initial record definition omitted
  the explicit range `1<=i<=n`. Both record sets now exclude future
  thresholds syntactically, not merely by context.
- **MINOR sign ambiguity, fixed:** the manuscript now names the signed
  logarithmic rate `lambda_a=lim n^(-1)log D_n` and the positive decay
  exponent `gamma_a=-lambda_a` separately.
- **MINOR conditioning compression, fixed:** the spacing proof now
  conditions first on a full type word, states independence of rank labels
  and ordered values, and derives the mean spacing from exchangeability and
  the unit sum.
- **MINOR evidence strengthening, fixed:** added the exact mass formula for
  `T`, plus 300 rational assertions that convolution mass through a cutoff
  plus the surviving tail equals one.
- **No theorem error:** the pgf, independent-geometric decomposition, mean,
  variance, critical/off-critical formulas, endpoint laws, and diameter
  constants all survived rederivation.
- **No terminology overreach:** mixed paths are described as finite-time
  absorption. The note explicitly declines to call the post-collapse
  `log 0` behavior a conventional finite Lyapunov exponent.

### Round-2 pre-cross-review checkpoint

Before the independent cross-hostile audit, the Round-2 exact run passed
**6,948,666** registered assertions and its then-current four-stage build
produced `main.pdf`, five pages and 302,887 bytes. These are historical,
pre-repair checkpoint figures: the later audit removed 305 tautological
assertions and regenerated the artifact. Citation, cross-reference, warning,
box, text, font, and page-render checks passed at that checkpoint.

## Pre-cross-review decision and residual risk

- **Internal theorem package:** GO.
- **External posting/submission/priority language:** HOLD.
- **Mathematical residual risk:** low after exact rederivation; the finite
  verifier is still bounded and does not replace the symbolic proofs.
- **Literature residual risk:** material. The three cited sources subtract
  broad owner frameworks, but a direct specialist search could still find
  the same cap–floor specialization or its law under different terminology.
- **Scope residual risk:** the exact diameter formula is uniform-law only;
  arbitrary atomless laws retain the survival law but not that metric
  constant.

## Independent internal cross-hostile audit and mandatory repair

This third audit was performed by a separate internal agent and is not an
external peer review. Its classification was **0 CRITICAL / 1 MAJOR / 2
MINOR**.

### MAJOR — conditioning on null events

The survival proof and the conditional-diameter theorem initially wrote
formulas given `N_n=j` for every `p` and every `j`. At `p=0` or `p=1`, most
such events have probability zero, so those conditional expressions were
not defined. The repair now restricts every conditional probability and
expectation to `P(N_n=j)>0`. For `0<p<1` every `j` remains reachable; at
`p=0` only `j=0` is reachable and at `p=1` only `j=n` is reachable. The
unconditional survival law remains valid for all `p`. The endpoint diameter
identity is now additionally proved directly: pure caps use the minimum
uniform order statistic and pure floors use the complementary maximum.

### MINOR 1 — incomplete source authorship

The bibliography entry with DOI `10.12958/adm1816` omitted coauthor
M. M. Zubairu. The entry now credits A. Umar and M. M. Zubairu, and the
owner-subtraction ledger names Umar–Zubairu. This is a source correction,
not a change to the theorem's ownership boundary.

### MINOR 2 — tautological evidence count

The law lane counted 305 assertions comparing `s/(n+1)` with the same
freshly recomputed expression. Those assertions have been deleted. The
independent rank-gap enumeration and endpoint checks remain intact, so the
registered exact total changes from 6,948,666 to **6,948,361** without loss
of substantive evidence.

### Cross-hostile disposition

All three findings are repaired. The conditional scopes, endpoint proof,
bibliographic attribution, stored control output, evidence documents,
production PDF, and checksum manifest were regenerated together. Internal
status remains GO; external circulation remains HOLD.
