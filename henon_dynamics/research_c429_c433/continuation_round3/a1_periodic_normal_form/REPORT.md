# R3 A1: author proof of PC424-L by stabilized carry coefficients

2026-09-09 UTC. Full proof:
[PROOF_PACKAGE.md](PROOF_PACKAGE.md). Latest mathematical status:
**core proof passed two independent checks; the full author proof and
finite-detection corollary passed E8; zero open mathematical repairs**.
Broader source-priority and admission gates remain pending. No paper
admission or evaluation is claimed.

## Original contract preserved

For every odd prime $p$, every $c\in k=\overline{\mathbb F}_p$,
$f=x^2+c$, and $h\in k[x]$, the proof establishes

$$\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive cycle }O
\quad\Longleftrightarrow\quad
h=Q\circ f-Q\text{ for some }Q\in k[x].$$

Periods divisible by $p$ are included; each orbit point is counted once.
The native one-step clock and all original parameter/degree quantifiers
remain unchanged. This is the original PC424-L equality, not a restricted
case or an auxiliary lemma substituted for the contract.

## New mechanism and its source subtraction

The existing all-$c$ binary coefficient theorem in the full cyclic
algebra was already sufficient for scheme-level detection and already
covered the monomial control. Re-proving it via Böttcher coordinates
would not address the missing reduced-point step.

The actual new lemma concerns multiplication by the full cyclic product.
Let a positive-degree normal representative $v$ have odd leading degree
$D$, let $m=\lfloor\log_2D\rfloor$, and let $E_D$ be its binary support.
In the full cyclic squarefree basis define

$$C_n=[P_{E_D}]\left(P_{\rm all}\sum_i v(X_i)\right).$$

The proof establishes $C_n=C_{n+1}$ for every $n\ge3m+4$:

1. One sequential circuit exactly reduces each
   $P_{\rm all}X_i^d$, for odd $d\le D$, by a weighted carry recurrence.
   The final carry is at most one and lands on an initial exponent zero.
2. Every path producing the nonempty short target has source
   $i\in[-m,m+1]\pmod n$.
3. A zero site can be inserted or deleted in the long complementary
   interval. Its transition is necessarily $1\to1$ of weight one.
   This is a bijection of all source/path pairs, including the lower
   odd monomials. Constant terms contribute only to the full-support
   monomial and do not affect the target.

Ordinary-cycle vanishing supplies the already proved necessary identity
$(2^nP_{\rm all}-1)H_n(v)=0$. The already proved leading coefficient is
$[P_{E_D}]H_n(v)=a_D$. At two consecutive levels these give
$2^nC_n=a_D=2^{n+1}C_{n+1}$. Stabilization forces $a_D=0$.
Fixed points then exclude a nonzero constant normal remainder.

The earlier one-level Jacobian counterexample does not contradict this
argument: no converse to Jacobian annihilation is used at a single level.
No individual coefficient functional is claimed to descend to the
radical quotient. No Böttcher series is evaluated at a finite point,
and no infinite Laurent tail is discarded.

## Finite certificate from the same theorem

The coordinator's corollary is proved in Section 5. For $\deg h\le M$
with $M\ge1$, put $n=3\lfloor\log_2M\rfloor+4$. Then $h$ is a
polynomial coboundary if and only if both

$$F_j\mid F_j'\widetilde H_j(h)\qquad(j=n,n+1)$$

hold, where $F_j=f^{\circ j}-x$ and
$\widetilde H_j(h)=\sum_{s<j}h\circ f^{\circ s}$.
Equivalently, the two return sums vanish at every ordinary root of
the corresponding $F_j$. The constant normal remainder is handled
separately using the adjacent scalars $n,n+1$.

Every noncoboundary of degree at most $M$ is consequently detected by
an ordinary primitive cycle of length dividing $n$ or $n+1$, hence
at most $3\lfloor\log_2M\rfloor+5$. Both iterate polynomials in the
certificate have degree at most $32M^3$. This corollary is part of
the same PC424-L result, not a second paper.

## Verification and handoff

The complete 444-line author proof was sent to the coordinator and
both assigned independent checkers, E8 and E2. Proof hash at dispatch:
06d0d06c1798b55d5a052b7ae3874bd176338ff31887a129b80041c5e1147450.
The exact same proof bytes subsequently passed
[E8's full readback](../reviews/e8_carry_stabilization/REVIEW.md),
including the finite-detection corollary, with zero mathematical repairs.
[E2's separate derivation](../reviews/e2_carry_independent/REVIEW.md)
also passed the core stabilization and original PC424-L implication
without reading the author proof or E8's review; that review did not
cover the subsequently appended corollary. The proof file's pending
review language records its dispatch state and has not been rewritten
after the checks.

The proof-writer skill determined the exact claim, dependency map,
carry-bound checks and explicit separation of author proof from
independent acceptance.

Only this assigned Round-3 directory was edited. No mathematical program,
old rerun, manuscript/PDF, formal evaluation, shared index, Git action,
external model/API call or new credential was used. Broader source
collision and original-contract admission remain coordinator gates.
