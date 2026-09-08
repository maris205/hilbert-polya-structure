# Independent current-team review of the AY7 and PG7 helpers

2026-09-08 UTC. This is a bounded nonauthor mathematical review, not an
external-model review, publication assessment, novelty certification or
admission decision. The reviewer did not coauthor either helper. The
coordinator contributed to the AY bound and therefore is not represented
as its independent reviewer.

## Outcome

| Item actually checked | Finding | What is not established |
| --- | --- | --- |
| AY displayed map/inverse, native domain, divisor condition, zero-channel argument, fixed-parameter height bound and finite-graph equivalence | **PASS as stated.** No mathematical gap found. | No uniform all-$k$ structural cycle atlas. |
| PG displayed map/inverse, native corner chart, products and fixed-$(n,P,Q)$ finite-factorization graph | **PASS as stated**, for every $n\ge4$, including even sizes. | No all-size/all-product structural atlas or exceptional-fibre classification. |
| AY second-invariant correction and dependency impact | **Correction verified.** The former $+kpq$ claim fails; $+krs$ is correct for the frozen map. | No source amendment, author intent, global priority or new integrability claim. |

The original AY7 and PG7 structural questions remain **NOT CLOSED**.
Neither helper becomes an admitted contract. HK7 is outside the mathematical
proof scope of this review; reading its report context is not a review of
its global classification problem.

## Exact read scope and fixed inputs

All of the following local files were read completely, including the
correction-stage versions. Their hashes were checked after the author
reported the affected inputs final. Links are relative to this review.

| Input | Lines | SHA-256 |
| --- | ---: | --- |
| [CHEAP_CHECKS.md](../nonlinear_scout/CHEAP_CHECKS.md) | 212 | `ef7bb645031e39b556fc283982e328c610ae07aee8a1268ace2ad3688e936cf4` |
| [SCOUT_REPORT.md](../nonlinear_scout/SCOUT_REPORT.md) | 414 | `a6519b3cfdd8a7a6052d55890f25ecbb418d2df76d5035fd127aa44ce0b8dcf2` |
| [CORRECTION_RECEIPT.md](../nonlinear_scout/CORRECTION_RECEIPT.md) | 97 | `892da1ff646408db0b4fc8b95e8bca63164456ca36a16a407e2153f4e000b698` |

The full report was read for frozen contracts, definitions, scope and
closure boundaries. Mathematical verification below concerns only AY and
PG, plus the specified AY source discrepancy. The report's wider source
search and all HK assertions are not independently certified here.

The main reviewer read the selected `research-review` and `proof-writer`
instructions completely. The explicit current-team review authorization
replaces legacy external-model examples. Proof discipline required a
separate helper verdict and original-contract verdict, and retention of
the native poles, zero strata and one-step clocks.

## AY: map, inverse and ordinary domain

For the frozen map write
$$
D=1+ps,\qquad h=k/D,\qquad
Y_k(p,q,r,s)=(r-hp,s,p,q+hs).
$$
At the image, the denominator of the displayed inverse is
$1+r'q'=1+ps=D$. Substitution therefore returns
$$
(p,(q+hs)-hs,(r-hp)+hp,s)=(p,q,r,s).
$$
Conversely, let $E=1+rq\ne0$ and $t=k/E$. The proposed inverse is
$$
G_k(p,q,r,s)=(r,s-tq,p+tr,q).
$$
The forward denominator there is $1+rq=E$, so its image is
$(p+tr-tr,q,r,s-tq+tq)=(p,q,r,s)$. Both compositions are correct with
the displayed labels; no parameter exchange or time rescaling is used.

These identities do not extend the contract through excluded poles.
The native set requires the displayed forward and inverse formulas to be
defined at every positive and negative iterate. In particular, an allowed
state has $1+ps\ne0$ and $1+rq\ne0$. Zero coordinates are otherwise
permitted. At $k=0$, the displayed holes remain excluded despite the
algebraically simplified pair-swap formula.

## AY: complete check of the height argument

On an ordinary integral orbit, write the time index as $j$ and set
$D_j=1+p_js_j$. The first update gives $D_j\mid kp_j$.
Since every common divisor of $D_j$ and $p_j$ divides
$D_j-s_jp_j=1$, it follows that
$$
D_j\mid k,\qquad h_j=k/D_j\in\mathbb Z.
$$
This includes $p_j=0$, when $D_j=1$. For $k\ne0$, $h_j\ne0$.
The lag coordinates give $r_j=p_{j-1}$, $q_j=s_{j-1}$, hence
$$
p_{j+1}=p_{j-1}-h_jp_j,\qquad
s_{j+1}=s_{j-1}+h_js_j.                         \tag{1}
$$
Put $B=|k|+1$. If $p_js_j\ne0$, then
$|p_js_j|=|D_j-1|\le B$, so both integer factors have magnitude at most $B$.

The zero cases were checked separately, not inferred from this product
bound:

1. If $p_j$ is identically zero, then $h_j=k$. Multiply the second
   recurrence by $s_j$ and sum over a period. The two adjacent-product
   sums cancel by cyclic reindexing, leaving $k\sum_j s_j^2=0$.
   Thus $s_j$ is also identically zero. Reversing the channel roles gives
   the same conclusion with $-k\sum_jp_j^2=0$. The only orbit with an
   identically-zero channel is the origin.
2. Two consecutive zeros of either channel propagate both forward and
   backward by (1), since the opposite-time coefficient is $1$.
   Consequently a nonzero periodic orbit has isolated channel zeros.
3. If $p_j=0$ on such an orbit, both neighboring $p$ values are nonzero.
   Their paired $s$ values have magnitude at most $B$: either they vanish
   or the product bound applies. At time $j$, $h_j=k$, and therefore
   $|k|\,|s_j|=|s_{j+1}-s_{j-1}|\le2B$. Hence $|s_j|\le4$.
   The symmetric argument for $s_j=0$ gives $|p_j|\le4$.
   A simultaneous zero is included in these arguments.

This proves $|p_j|,|s_j|\le C_k=\max(|k|+1,4)$ at every time.
The lag identities bound $q_j,r_j$ by the same constant. Negative
parameters, negative divisors, the origin, isolated zeros and periods one
or two create no omitted case in the cyclic-sum argument. No invariant
or generic-fibre theorem is used.

## AY: finite graph and the zero parameter

For fixed nonzero $k$, the stated integer box is finite. Remove vertices
with either displayed current-state pole; retain only exact forward edges
to another retained integer vertex for which the displayed inverse is
defined and returns the source. Every directed cycle then supports all
positive and negative iterates in the prescribed ordinary domain. It is
an integral periodic orbit. Conversely the height proof places every
ordinary integral periodic orbit in this graph, and its native edges are
retained. The length of a cycle with distinct vertices is its least native
period. Thus this equivalence needs no guessed period cutoff.

For $k=0$, $Y_0(p,q,r,s)=(r,s,p,q)$ and its square is the identity.
The two excluded-pole conditions are exchanged by the map. The admissible
states with $(p,q)=(r,s)$ are fixed; all other admissible states have least
period two. No claim is made at the removed holes.

The finite algorithm is exhaustive for each fixed $k$. This is not the
frozen request for a substantive uniform structural classification across
all integer parameters.

## PG: both inverse compositions and the chart

Use $i\in\mathbb Z/n\mathbb Z$ and $\phi_i=1-x_iy_i$. The forward map is
$$
X_i=x_i\frac{\phi_{i-1}}{\phi_{i+1}},\qquad
Y_i=y_{i+1}\frac{\phi_{i+2}}{\phi_i}.
$$
It satisfies
$$
X_iY_{i-1}
=\left(x_i\frac{\phi_{i-1}}{\phi_{i+1}}\right)
 \left(y_i\frac{\phi_{i+1}}{\phi_{i-1}}\right)=x_iy_i.
$$
Thus $\psi_i=1-X_iY_{i-1}=\phi_i$, and the proposed inverse immediately
recovers $x_i,y_i$. Conversely, the inverse formulas
$$
x_i=X_i\frac{\psi_{i+1}}{\psi_{i-1}},\qquad
y_i=Y_{i-1}\frac{\psi_{i-1}}{\psi_{i+1}}
$$
give $x_iy_i=X_iY_{i-1}$, again yielding $\phi_i=\psi_i$.
The forward $x$ formula returns $X_i$, and its $y$ formula returns
$$
\left(Y_i\frac{\psi_i}{\psi_{i+2}}\right)
\frac{\psi_{i+2}}{\psi_i}=Y_i.
$$
This works for every frozen cyclic size $n\ge4$, without a parity
restriction, relabelling quotient or two-step replacement.

The union of displayed forward denominator exclusions is exactly
$\phi_i\ne0$ for all $i$, and that of inverse denominator exclusions is
$\psi_i\ne0$ for all $i$. These must accompany, not replace, the frozen
base chart $x_i,y_i\notin\{0,1\}$. A retained directed cycle whose every
state lies in that chart and whose displayed inverse returns its preceding
state lies in the maximal two-sided native domain. No pole resolution or
enlarged zero stratum is being used.

## PG: invariant slices and completeness

Multiplication over the cyclic index cancels the numerator and denominator
products in both updates. Therefore $\prod_iX_i=\prod_ix_i=P$ and
$\prod_iY_i=\prod_iy_i=Q$. This cancellation is parity-independent.

For nonzero integer $P,Q$, each integral $x_i$ is a signed divisor of $P$
and each $y_i$ a signed divisor of $Q$. There are finitely many ordered
factorization arrays with those products. Restrict them to the chart and
retain the exact ordinary forward/inverse edges described above. Every
retained directed cycle is an ordinary integral periodic orbit; every such
orbit in this fixed invariant slice appears because the two products are
preserved. Its least period is the native directed-cycle length. Empty
slices are harmless; a nonempty slice was not assumed.

This proves the stated fixed-$(n,P,Q)$ helper. No graph was constructed or
executed. It neither supplies a structural list over all $n,P,Q$ nor
settles generic or exceptional Jacobian torsion/integrality questions.

## Independent verification of the AY correction

The reviewer reopened the primary PDFs and read the affected formulas:
[Kassotakis, Example 2.4, printed p. 7](https://sigma-journal.com/2019/048/sigma19-048.pdf)
prints the base polynomial plus $a pq+b rs$ with the displayed map having
$k=a-b$; [Konstantinou-Rizos–Mikhailov, Section 4.1.1, equations (28)–(31)](https://arxiv.org/pdf/1205.4910)
gives the same map and the invariant $(a+pq)(b+rs)+ps+qr+1$.
The served arXiv PDF's stamp was checked as version 1205.4910v3. Only the
relevant source portions, not either complete paper or its global proofs,
were reviewed. No original 1994-source access is claimed.

Independently repeating the one-step arithmetic, at $k=5$ the state
$(1,2,3,4)$ maps to $(2,4,1,6)$ and reverses under the displayed inverse.
For $K=pqrs+ps+qr$, the values are $34$ and $64$. Hence $K+kpq$ changes
from $44$ to $104$, while $K+krs$ is $94$ at both states. This is a
counterexample to the former preservation claim, not a claim of an
integral periodic orbit.

For general ordinary input, set $D=1+ps$, $h=k/D$ and
$d=rs-pq-hps$. Direct substitution gives
$$
p'q'-pq=d,\qquad r's'-rs=-d,\qquad
K'=D(r-hp)(q+hs)+ps,
$$
so $K'-K=Dh(rs-pq-hps)=kd$. Thus
$$
(K+krs)'-(K+krs)=0,\qquad
(K+kpq)'-(K+kpq)=2kd.
$$
The corrected polynomial agrees with the second primary source after
$(a,b)=(k,0)$ and deletion of the constant $1$. Fixed parameters and the
frozen map are unchanged. The two printed formulas in the first source
are incompatible as that fixed-map/invariant pair; no source erratum or
authorial intention is inferred. The correction receipt's explanation
and numerical values pass. The height proof's dependency chain uses
neither invariant and is unaffected.

## Review provenance and closure

The main reviewer performed all derivations above. An additional
nonauthor current-team agent, `pg_inverse_check`, separately read the
relevant PG contract and helper context and returned a hand-check pass on
both inverse compositions, the exact chart, products and graph-cycle
equivalence. This is supplementary internal checking, not an external
review or independent source-ownership audit.

Review activity: local text reads, line counts and hashes; direct primary
PDF opens and within-source finds; symbolic hand derivations; static
checks of this review. Fresh web search-query submissions in this review:
**0**. Direct source access comprised **3 PDF opens across 2 distinct PDFs**
(the third open checked the arXiv version stamp) and **3 within-source find
operations**. These are not search-query submissions. Mathematical program
executions, censuses, old-check reruns, GPU runs, paid external-model
calls and Git operations: **0**. Only this review file was written.

There is no outstanding mathematical repair request for the two helpers
at the hashes above. The original full AY7/PG7 questions remain unproved,
HK7 receives no global-proof verdict, and no accepted artifact, global
index, paper number or admission state changes. Correct helper proofs
alone do not establish a paper-level increment. In particular,
`NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged: no target Euler factors,
root numbers, automorphy or zero-matching theorem follows here.
