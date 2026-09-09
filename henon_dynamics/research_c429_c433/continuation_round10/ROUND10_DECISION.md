# Round 10: finite effectivity and native visibility

2026-09-09 UTC. Final mathematical/source coordinator adjudication under
the continuous research authorization, after all actual final reviews.
This is a research checkpoint and fifth-contract admission, not a
manuscript release; the downstream gates remain explicit.

## 1. Current outcome and scope

The coordinator has read A1's complete 455-line author proof and all
590 lines of E2's final nonauthor mathematical review, and independently
recomputed their final hashes. The full annihilator-ideal theorem is
accepted as an auxiliary result, with zero open mathematical or
source/provenance must-fixes. It resolves R9's unknown-annihilator degree
gap at the actual derivative-weighted scope, not the full ordinary CP
converse or the general multiplicative transfer-existence problem MS6.

A2's complete 411-line author proof and all 433 lines of E5's final
complete review have also been read and hand-checked. Its visibility
theorem and two controls are accepted as auxiliary results with zero
open must-fixes. A3's full
finite-CP proof is now 713 lines: root read the entire 708-line body
and the five-line provenance addition, and checked the final hash.
Root has also read all 429 lines of E8's final complete mathematical
review and all 293 lines of X2's final source/substantiality report,
and recomputed their final hashes. The three mathematical reviews
total **1,452 lines**. Every original A3 equivalence, parameter and
constant is accepted with zero open mathematical, source-applicability
or provenance must-fixes.

The coordinator admits **one integrated FCP10 finite-effectivity
contract**, for the independent-substance reasons in Section 4 and
[the formal admission](../ADMISSION_DECISIONS.md#6-fcp10--admit-one-complete-finite-cp-decision-contract).
Together with PC424-L, UL4, OM4 and RLG5 there are now five admitted
contracts and **zero completed papers**. No separate A1/A2 slot,
manuscript/PDF, formal evaluation, target-arithmetic upgrade or Route B
entry has occurred. The next research-to-paper gate is one coherent
five-contract outline and its independent review, not additional
scouting merely to fill a vacant slot.
All R10 tasks reuse existing current-session threads, with zero
mathematical program executions, external model/API calls or GPU jobs.
Matrix constructions and coefficient arguments are proofs, not claimed
executed finite certificates. The inherited eight untracked directories
and all earlier frozen rounds remain untouched.

## 2. A1: unknown annihilator becomes a finite ideal calculation

Author: [annihilator ideal](a1_annihilator_ideal/REPORT.md).
Nonauthor: [E2 complete review](reviews/e2_annihilator_ideal/REVIEW.md).

For every odd prime $p$, $k=\overline{\mathbb F}_p$, every $c\in k$
and every reduced rational norm-one function

$$w=\eta A/B,\qquad B(X)=(-1)^mA(-X),\qquad \eta\in\{1,-1\},$$

where $A,B$ are monic coprime degree-$m$ polynomials, put

$$f=x^2+c,\quad F_n=f^{\circ n}-x,\quad
H_n=\eta^n\prod_{i=0}^{n-1}A\circ f^{\circ i}
              -\prod_{i=0}^{n-1}B\circ f^{\circ i},$$

and

$$I_w=\{S\in k[x]:F_n\mid SF_n'H_n\text{ for all }n\ge1\}.$$

Let $b=m+2$, $D=4b^2$, $N=5D+1$, and define the explicit polynomials

$$S_* =\prod_{r=1}^{D}F_r,\qquad
q_n=\frac{F_n}{\gcd(F_n,F_n'H_n)},\qquad
L_N=\operatorname{lcm}(q_1,\ldots,q_N).$$

The accepted complete auxiliary theorem is

$$I_w=
\begin{cases}
(L_N),&L_N\mid S_*,\\
(0),&L_N\nmid S_*.
\end{cases}$$

In particular nonzero all-level annihilation is decidable by the
$1\le n\le N$ divisibility tests using $S_*$, whose degree is
$2^{D+1}-2$. This is a uniform theorem, not an optimized implementation
or a practical complexity claim.

The new bridge is substantive within this auxiliary question. Local
factorization shows that each $q_n$ is squarefree, with root set
$B_n=\{a:F_n(a)=0, e_n(a)H_n(a)\ne0\}$, where integer multiplicity
$e_n(a)$ is mapped into $k$ in this product. Thus $I_w\ne0$ is
equivalent to finiteness of $\mathcal B=\bigcup_nB_n$ and its generator
has exactly these roots. The exact logarithmic derivative identity gives

$$L_n(F_n'H_nR)=\sum_{a\in B_n}e_n(a)H_n(a)R(a),$$

with $L_n$ the top coefficient of the remainder modulo the monic $F_n$.
No inverse of a vanishing Jacobian is used.

The four inherited matrix blocks live in a space of dimension $D$.
Their word tensors have split rank at most $D$. The two monic binary
polynomial bases and ordinary interpolation on distinct points show
rank exactly $|B_n|$ once both halves are long enough. Each already
visible cycle persists at arbitrarily long suitable multiples: the
local multiplier branches $0$, $1$ and the other finite-order values
are all checked, while products are held fixed by one congruence
sequence, including one-sided zeros. Consequently, if $\mathcal B$
is finite, each of its cycles has native period at most $D$.

This argument does **not** claim $|\mathcal B|\le D$ or that all
cycles are simultaneously visible at one level. The period bound gives
the explicit $S_*\in I_w$. Only then is R9's already accepted fixed-$S$
word theorem applied: $k_{S_*}=D+1$ and the inherited horizon is at
most $D+1+4D=N$. Applying the same theorem to $L_N$ proves the whole
ideal formula, not merely the existence of some bounded annihilator.
The cyclic module generated by $(F_n'H_n\bmod F_n)_{n\ge1}$ is then
$k[x]/(L_N)$ when nonzero annihilation exists.

Root and E2 independently checked the complete proof, including
$n=1,2$, $c=0$, $m=0$, constant generators, empty visible sets,
periods divisible by $p$, nonreduced roots and arbitrary root powers.
E2 required no author repair. The author discloses coordinator rank
and persistence suggestions; the review is independent nonauthor
reconstruction after reading the actual manuscript, not blind review.

No proof that every nonconstant norm-one $w$ has $I_w=(0)$ has been
obtained. The theorem does not identify annihilation with ordinary CP,
and the existence direction of full MS6 is still open.

## 3. A2: an exact native visibility boundary

A2's [native visibility report](a2_native_jacobian_visibility/REPORT.md)
and [E5's complete review](reviews/e5_native_jacobian_visibility/REVIEW.md)
have both been read completely, including the self-contained local
ramification proof and both infinite native-blind controls. No author
repair was required, and their final hashes agree with the bindings below.

At a cycle $O$ of native period $r$, let $e_O(k)$ be its integer
root multiplicity in $F_{rk}$ and $\lambda_O$ the native multiplier.
For $\lambda_O=1$, all multiplicities satisfy
$e_O(k)\equiv e_O(1)\pmod p$. For $\lambda_O=0$ they are all one.
For $\lambda_O\ne0,1$ the native root is simple, but a resonant
multiple need not be. Thus native-blind means $p\mid e_O(1)$ and
is exactly permanent blindness at every multiple; native-visible
means $p\nmid e_O(1)$ and the native layer itself detects the cycle.

The formal weak Sen congruence is proved by a triangular Laurent
orbit-product basis, including negative powers/iterates, and a finite
trace cancellation contradiction. All infinite-series valuation,
noncancellation, infinite-order and phase-conjugacy steps were checked
by root and E5. The classical congruence is explicitly subtracted.

For the full quadratic norm-one observable, the accepted equivalence is

$$I_w\ne(0)\quad\Longleftrightarrow\quad
W_O=1\text{ on all but finitely many admissible native-visible cycles}.$$

One fixed $S$ handles all support and visible bad cycles simultaneously.
This is visible CP, not unfiltered ordinary CP. Combined with Section 2,
it gives a finite decision of this precise visible condition.

There are infinitely many permanently blind native cycles in both
characteristic-three controls. For $f=x^2$, primitive $5^t$th roots
have native period divisible by four and return multiplicities
$3^{v_3(2^n-1)}$. For $f=x^2-2=x^2+1$, write $\pi(u)=u+u^{-1}$
and take primitive $11^t$th roots. Their projected native periods
$r_t$ divide the odd number $5\cdot11^{t-1}$, their native returns
lift to inversion, and their $k$th return multiplicities are
$3^{v_3(2^{r_tk}-(-1)^k)}$, always divisible by three. Distinct root
orders yield disjoint cycles. The coordinator supplied the Chebyshev
control; the report and nonauthor review disclose that provenance.

Root and E5 read [Berger's complete Section 3 proof](https://perso.ens-lyon.fr/laurent.berger/articles/article33.pdf).
The [Sen journal page](https://annals.math.princeton.edu/1969/90-1/p04)
was read only as metadata, not as Sen's original proof. Worksheet
access failed on the separate reopen attempts. No missing source is
claimed accessed; the required formal argument is self-contained.

No rational weight satisfying all annihilation levels while violating
CP has been constructed. The controls defeat the finite-blind-cycle
shortcut, not the full rational-observable converse or MS6.

## 4. A3: complete ordinary finite-CP decision accepted as FCP10

A3's [frozen full proof](a3_inseparable_finite_cp/REPORT.md) concerns
all primes, all degree-$d\ge2$ polynomials with $f'=0$, and all rational
$g=A/B$ of height at most $m$, with every ordinary native cycle retained.
It asks for a coefficient-independent finite decision of cofinite CP,
not a weaker degree-restricted sample and not full MS6. Put

$$b=\left\lceil\frac{m}{d-1}\right\rceil+1,\qquad D=2b^2,\qquad
N=6b^2+1=3D+1,$$

$$F_n=f^{\circ n}-x,\qquad
H_n=\prod_{i=0}^{n-1}A\circ f^{\circ i}-\prod_{i=0}^{n-1}B\circ f^{\circ i},
\qquad S_* =\prod_{r=1}^{D}F_r.$$

The unchanged exact author theorem is

$$\mathrm{(CP)}\quad\Longleftrightarrow\quad
F_n\mid S_*H_n\text{ for every }1\le n\le N.$$

Root hand-checked its full proof at this scope: actual scaling conjugacy
handles nonmonic maps; $F_n'=-1$ gives the simple-root CP ideal equivalence;
the general-polynomial Laurent extractor and base-$d$ basis provide two
blocks; logarithmic contraction gives the fixed-$S$ cutoff $k_S+4b^2$;
split rank plus arbitrarily long nonzero returns bounds each visible
exceptional period by $D$; and the explicit $S_*$ then yields $N$.
Cycles meeting both a numerator and denominator zero are legitimate
finite support exceptions, invisible to all cleared products, and
their periods are not asserted bounded. One-sided support cycles are
visible and the persistence proof covers them.

All primes, $m=0$, unequal numerator/denominator degrees, whole-function
multiplicities, nonmonic coefficients and all native periods are retained.
No A1 theorem is used as an unproved black box. Root supplied the
high-level adaptation and constants before the author proof; one
provenance-only five-line addition now explicitly records this. The
mathematical body was unchanged and the addition actually read back.
Root read all 429 final lines of [E8's complete mathematical review](reviews/e8_inseparable_finite_cp/REVIEW.md).
The reviewer reconstructed the entire argument without importing A1
or its review, verified that removing the exact provenance insertion
recovers the original 708-line hash, and closed all mathematical and
textual obligations. This is nonauthor review of the actual proof,
not an independent-origination or blind-review claim.

Root also read all 293 final lines of [X2's separate source/substance
report](x2_finite_cp_sources/REPORT.md), which reads the complete final
A3 proof and explicitly charges the shared root/R9/A1 mechanism.
Its conditional one-contract recommendation is now supported by the
completed zero-must-fix mathematical gate. Root agrees and admits
one integrated FCP10 contract.

X2's source checks are limited to two actual targeted search batches.
Root directly read Kiefer et al.'s [primary text, Sections 3 and 4.1](https://arxiv.org/html/1302.2818v1).
Finite-word reachability over a field and Hankel rank factorization are
classical inputs. The Section 4.1 Gram-kernel proof uses the rational
sum-of-squares argument and is not imported into characteristic $p$.
These inputs do not by themselves bound an unknown finite set of
exceptional cycles. One such cycle contributes at arbitrarily many
return lengths, so a classical finite-support word-series theorem is
not a direct solution. The degree of the coefficient field is also
unbounded; finite matrix size alone does not bound an element's order.
The two-batch source search found no theorem owning this exact
question, but this is not certified worldwide novelty.

Root also directly read the complete Section 4 normal-form/residue
pairing and trace arguments in [Cattani--Dickenstein--Sturmfels](https://arxiv.org/html/alg-geom/9404011v1),
including Lemma 4.2, Theorems 4.3/4.9 and the trace algorithm, together
with the stated other-field limitation in Remark 1.6(iii). These are
classical infrastructure, not a cross-return unknown-exception bound.

The surviving independent output is an exact infinite-to-finite
ordinary multiplicative CP decision for the complete canonical class
$f'=0$, despite unknown finite exceptions and unbounded coefficient
fields. This class includes $(x^s+x)^p$ for $s\ge2$, $p\nmid s$,
which has multiple generic inverse branches and is not a pure
Frobenius base in disguise. The accepted additive unicritical theorem,
pure-Frobenius multiplicative existence and derivative-filtered
quadratic certificate do not already give this whole decision.
The construction, exceptional-period bound and finite criterion count
together as one question. They are not split into extra papers.

FCP10 is not a renamed partial completion of MS6. It proves no rational
or finite algebraic transfer existence or classification, even at its
own derivative-zero scope. No general separable-map CP theorem,
optimal bound, practical running time or public priority claim follows.
An actual exact prior implication would reopen substantive admission.

## 5. Final frozen bindings and integration boundary

The following final hashes were actually checked from disk:

| Relative path | Lines | SHA256 |
| --- | ---: | --- |
| `a1_annihilator_ideal/REPORT.md` | 455 | `3e53c02f8315cfd957be1c235609b3f2fd3292103b7bd8b31aa98b81f69b835e` |
| `reviews/e2_annihilator_ideal/REVIEW.md` | 590 | `89d878bc6104ba8a22ab178f602260502641fed55d1f86835c18a000ded097f1` |
| `a2_native_jacobian_visibility/REPORT.md` | 411 | `46a8d605900a3145134a0074371ea170c6ed8d2ba54aa8c046ed6e59c7c2dd0b` |
| `reviews/e5_native_jacobian_visibility/REVIEW.md` | 433 | `55af32ee9c5da5e996c4695ef96ee4766e22970bdbf8e27141b09cb7bf3b6df6` |
| `a3_inseparable_finite_cp/REPORT.md` | 713 | `34a773edfce1e02e3dbe39f967888d4e49ba50d1384040f07d350c1e79779f1c` |
| `reviews/e8_inseparable_finite_cp/REVIEW.md` | 429 | `6074afa280e6ac735074b1da70532b2d9adc38e0d6a56d16a209b920117c0951` |
| `x2_finite_cp_sources/REPORT.md` | 293 | `340c85b45f11c5a5fec8c18b4490a70c7c313f39cad2b8309a55414aa7628a85` |

Author/reviewer date headers may retain the environment-provided
2026-09-10; the actual coordinator clock is 2026-09-09 UTC. Those headers
are not execution timestamps, and frozen mathematical inputs are not
rewritten merely to change their date labels.

No R10 staging, integration audit, commit, push or release is claimed
here. The mathematical and source gates are now closed. Root will obtain
a separate exact-path audit and synchronize only the checkpoint paths.
The previous R9 research commit is
`af22f7184a4d2fe3f32228777cd1b5c6c59ba771`; its coordinator-only later
receipt is `8dc9bfba2ba5834a15804e9e608a5a16fffe68b4`. After a completed
fresh fetch, actual HEAD, origin/main and live remote main all agreed
with the latter at the start of this adjudication.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional. Ordinary cycle
products, residue matrices and finite decisions do not establish target
Euler factors, root numbers, automorphy or a Hilbert--Polya realization.
