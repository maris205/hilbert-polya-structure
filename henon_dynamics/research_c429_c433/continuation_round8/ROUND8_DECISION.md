# R8: critical-atom proof and two source/scout controls

Status: `ROOT_PROOF_READ; TWO_MATHEMATICAL_REVIEWS_CLOSED;
FULL_SINGLE_QUADRATIC_ATOM_ACCEPTED_AUXILIARY;
FOUR_ADMITTED_CONTRACTS; ZERO_COMPLETED_PAPERS`.

This is a completed mathematical checkpoint, not a paper admission or release.
The user's continuous main/subagent authorization remains active. R7 is frozen:
research commit `4773182d6a4c7a08e8f2a8d0ebe8fdbf31d3fcbc` and subsequent
two-record receipt commit `8098054a33660422e7b17d22b13538e279a23f2a`.
At this checkpoint the actual local HEAD and origin/main still equal the
latter commit. No R8 commit, push, paper, or mathematical execution is claimed.

## 1. Actual work and current dispositions

| Work | Actual evidence read by coordinator | Current decision |
| --- | --- | --- |
| A2 critical atom | Entire final 526-line author report, E2's 448-line independent coefficient reconstruction and E5's 429-line complete proof review | Accept full residual theorem and its exact R7 atom-family corollary as auxiliary; zero open must-fixes |
| X2 bounded multiplier sources | Entire 204-line report and the primary passages specified below | Accept bounded source/quantifier audit; it supplies no applicable positive-characteristic classification |
| D1 fresh contract scout | Entire 141-line report, actual primary Example 2, and direct hand verification of every local and real step | Accept HP8 counterexample as an auxiliary control; no independent contract recommended |

The two R8 mathematical review tasks reuse E2 and E5. E2 reconstructs the
cyclic coefficient without first reading A2's new proof; E5 reads and checks
the complete final author proof without first reading E2's assessment. These
are internal current-team reviews, not human or external-model peer review.
Both final files are now fully read and accepted at their respective scopes,
877 review lines in total. E5 did not read E2 at any stage. No author repair
was requested after the final freeze; the original false shortcut remains
withdrawn. No review is counted as a new theorem or a complete paper.

## 2. Exact critical-atom claim and root verification

Keep all odd primes $p$, $k=\overline{\mathbf F}_p$,
$f(x)=x^2-1$, and $g(x)=(x-1)/(x+1)$. The original allocated question
asks for infinitely many ordinary primitive native cycles avoiding
$\{0,1,-1\}$ with product of $g$ different from one. A2 proves the
stronger pointwise prime-period assertion: every prime $n\ne p$ with

$$n\equiv1\pmod{p-1},\qquad n\not\equiv1\pmod p$$

has such a cycle of least period exactly $n$. Its Section 8 proves that
these primes are infinite. No restriction to a sampled finite field, no
fixed-scheme multiplicity in the observable, and no return-clock replacement
has been made.

Root read the complete final report and independently checked the following
interfaces. This records mathematical checking, not a program execution.

1. On an ordinary cycle, writing $A=\prod x$, $B=\prod(x+1)$ and
   $C=\prod(x-1)$ gives $BC=A$, $B=A^2$, hence the product is
   $A^{-3}$. Odd prime cycles cannot contain the excluded critical two-cycle
   or its strict preimage.
2. The algebra
   $\mathcal A_n=k[X_0,\ldots,X_{n-1}]/(X_i^2-X_{i+1}-1)$
   is $k[x]/(f^{\circ n}(x)-x)$. Squarefree monomials form a basis:
   reduction lowers total degree, and substitution yields monic polynomials
   of distinct binary degrees from $0$ to $2^n-1$.
3. For $F=f^{\circ n}-x$, a polynomial $H$ vanishing at every ordinary
   root satisfies $F\mid F'H$. A root of multiplicity $e$ contributes
   order at least $e-1$ to $F'$, even when $p\mid e$. For prime $n$,
   fixed points are killed by $K=X_1-X_0$ and good $n$-cycles by
   $P^3-1$, where $P=\prod_iX_i$. Thus all good $n$-cycles would force

   $$D_n=K(2^nP-1)(P^3-1)=0\quad\text{in }\mathcal A_n.$$

4. With $M=\prod_{i=1}^{n-1}X_i$, root verified the coefficients
   $[M]K=0$, $[M]KP=-1$, $[M]KP^2=-1$, $[M]KP^3=n-3$ and
   $[M]KP^4=2^{n-1}-3$. The cubic parity argument uses the sole
   higher-degree basis element $P$, which is odd, and division by the
   even polynomial $f^{\circ n}$. The quartic argument uses the correct
   $(X_i+1)^2$ product, not its false earlier simplification.
5. Root checked the finite coefficient functional in Section 6 directly:
   finiteness follows from total degree, cancellation annihilates each
   defining relation, and its values on the squarefree basis identify it.
   The index inequalities bound the cyclic traces to the displayed $2$-
   and $3$-state matrices. Their entries, powers, and final traces give
   $14\cdot2^{n-2}-2$ and $6\cdot2^{n-1}+1$, respectively.
6. Hence

   $$[M]D_n=\frac{(2^n-2)^2}{2}+1-n,$$

   which is $1-n\ne0$ for the displayed prime periods. Division by two
   is legitimate throughout the original domain. The separate $p=3$
   argument uses $K(1-P^2)$ and coefficient one for every odd prime $n$,
   including $n=p$; it does not divide by three.
7. For the prime lemma, set $m=p-1$. Since
   $2\varphi(m)\le p-1$, some $t\in\mathbf F_p$ has
   $\Phi_m(t)\notin\{0,1\}$. Choose $A$ in that residue class
   divisible by $m$ and any finite set of putative desired primes. Every
   prime factor $q$ of $\Phi_m(A)$ avoids these divisors and $p$.
   Squarefreeness of $T^m-1$ modulo $q$ proves
   $\operatorname{ord}_q(A)=m$, hence $q\equiv1\pmod m$.
   At least one such factor is not one modulo $p$, since their product
   with multiplicity is not one modulo $p$. This supplies a new desired
   prime. All CRT and cyclotomic conditions include $p=3$.

The coordinator also independently developed a cyclic-carry coefficient
calculation before reading the final author body and shared it with A2/E2.
That author-side interaction is disclosed; it does not stand in for E5's
whole-proof review. E2 had independently reported the corrected quartic
formula before receiving the coordinator's detailed carry classification.
The final E2 report preserves its actual information-exposure sequence.

### Correction retained, not erased

A2's preliminary claim used the false identity
$P^4=\prod_i(X_i+2)$, omitting the $2X_i$ term in squaring
$X_i+1$. A2 self-retracted that claim before the final report, root had
not adopted it, and E2 was immediately notified. The revised proof uses

$$P^4=\prod_i(X_i+1)^2=\prod_i(X_{i+1}+2X_i+2).$$

The author report's Section 10 retains the withdrawn claim explicitly.
It is not described as a passing intermediate theorem. Root read E2's
entire final 448-line reconstruction and verified its actual hash. Its integer
basis proof, degree-budget exhaustion of all carry paths, the otherwise
possible but zero adjacent-square term, and the $n=3$ boundary all check.
The corrected coefficients are accepted; the original false coefficient
remains rejected. E2 did not review CP or the prime lemma and is not credited
with doing so. No open coefficient repair remains. Root subsequently read
all 429 lines of E5's final whole-proof review and checked the unchanged
author and actual review hashes. Every interface listed above, including the
prime lemma and critical $p=3,n=3$ boundary, is independently covered.
The full residual theorem is accepted with zero open must-fixes.

### Integration boundary

Combining the accepted R8 proof with the accepted R7 all-parameter
atom reduction now settles that entire single balanced-atom question for every
odd prime, all $c$, and all $a\ne0$. For $a=-1$ at $c=-1$, the atom
is the reciprocal of the displayed one, so the same bad cycles suffice.
Only the residual family has the stronger prime-length assertion; that is
not attributed to all R7 parameters. This is still not the general norm-one
theorem for arbitrary powers or products of atoms:
cofinite product-one for a product of rational functions does not imply that
each factor has cofinite product-one. Even infinitely many products different
from one do not exclude their all belonging to a fixed finite root-of-unity
group. General MS6 and the fifth independent contract remain open.

## 3. Bounded multiplier sources: what was actually established

Root accepts X2's logical controls. Cofinitely many nonzero multipliers lying
in one finite set, having one uniform prime-to-$p$ order bound, and lying in
one finite field are equivalent. Mere membership in
$\overline{\mathbf F}_p$ is automatic; fixed-period multiplier polynomials
with coefficients in $\mathbf F_p$ do not imply a uniform field for all
individual roots. For $x^2$, all nonzero cycle multipliers equal $2^n$ and
lie in $\mathbf F_p^\times$, providing the stated positive control.

The necessary constraint $\lambda_O^{3(p-1)}=1$ is weaker than the
actual product condition $A_O^3=1$. Proving its failure on infinitely many
cycles would suffice, but failure to prove that stronger target would not
establish cofinite product-one.

Root's actual source reading, in addition to the entire X2 report:

- [Huguin, arXiv:2210.17521v1](https://arxiv.org/html/2210.17521v1):
  Theorem 7, the full proof of Lemma 11 and the complete proof of Theorem 7
  through its final Lyapunov contradiction were read. They require complex
  inverse branches/metrics and number-field Galois equidistribution, not a
  positive-characteristic substitute for them.
- [Ji–Xie–Zhang, arXiv:2308.00289v3](https://arxiv.org/pdf/2308.00289v3):
  exact Theorem 1.5, Remark 1.6 and the complete Section 4 proof were read.
  Finite exceptions are allowed; the complex/number-field hypotheses are the
  unavailable interface. The proof does not transfer solely by lifting roots
  of unity.
- [Benedetto–Ingram–Jones–Levy, arXiv:1201.1605v4](https://arxiv.org/pdf/1201.1605v4):
  exact Theorem 1.5 and Corollary 1.7, and all of Section 6's relevant
  Lemma 6.1, proofs, Remark 6.2 and Corollary 6.3 were read. Constant
  multipliers/isotriviality do not classify the target, which is already
  PCF over $\mathbf F_p$.

X2 used exactly two batches/eight queries. Root's later opening of the full
identified Huguin proof completes its own passage check, not a new discovery
or an additional search batch. No global literature-completeness or novelty
claim is made. This source route did not solve the atom theorem; A2's separate
direct coefficient proof supplies the now-reviewed mathematical evidence.

## 4. HP8: complete counterexample, auxiliary only

For

$$G(t)=(t^3-19)(t^2+t+1),\quad
H(x,y)=(y,2y+G(y)-x),$$

every $\mathbf Q_v$ has a genuine fixed point. Root checked all primes:
for $\ell\equiv1\pmod3$ use the simple nontrivial cubic root of
unity in the quadratic factor, including $\ell=19$; for
$\ell\equiv2\pmod3$ use the bijective cube map and simple root of
$t^3-19$, including $2$; at $3$ substitute $t=1+3z$ and lift a simple
root of $z+3z^2+3z^3-2$. The real fixed point has
$\alpha=\sqrt[3]{19}$.

Since $t^2+t+1>0$ on $\mathbf R$, the sign of $G(t)$ is that of
$t-\alpha$. A real periodic sequence satisfies
$x_{i-1}+x_{i+1}=2x_i+G(x_i)$. Its maximum $M$ has $G(M)\le0$,
and its minimum $m$ has $G(m)\ge0$, forcing $m=M=\alpha$.
Thus the unique real periodic point is $(\alpha,\alpha)$, so there
is no rational periodic point of any period.

Root read the actual Introduction, Theorem 1, Example 2, Remark 2 and
Example 3 in the [author-uploaded Berend–Bilu primary text](https://www.researchgate.net/publication/254468616_Polynomials_with_roots_modulo_every_integer).
Example 2 already owns this precise polynomial and its local arithmetic.
Root also checked [Towsley Theorem 1 and Corollary 1](https://arxiv.org/pdf/1209.2399v4),
including the latter's proof: their single globally chosen point is not HP8's
place-dependent point. HP8 does not contradict that theorem.

The counterexample is accepted as a short Hénon realization/control, not a
substantial fifth contract or a priority claim. No minimum degree is proved
for the problem allowing different local periodic points and periods. D1
froze only one full question, used three batches/twelve queries, and recommends
none; no extra parameter family or manuscript is opened to preserve a slot.

## 5. Actual frozen mathematical inputs

| Path relative to this directory | Lines | SHA-256 |
| --- | ---: | --- |
| `a2_critical_atom/REPORT.md` | 526 | `e3fcd6eef80df88ed1d0b5b4633e6d6e1003582bf0b4022c86303df166f278c3` |
| `x2_bounded_multiplier_sources/REPORT.md` | 204 | `ec116d3ffdc18ed7f896ff43cb4aedb4156e6dbb9d4363da580969e00273c90e` |
| `d1_fresh_contract_scout/REPORT.md` | 141 | `66e6e08b910bc6cb148bd2e53ae18c638a3d900f5d56ff5685000cd0a08609e4` |
| `reviews/e2_critical_atom_coefficient/REVIEW.md` | 448 | `ea470518379cd1ed8e66f5b7f46150d7e520f4b4d3c2cd303dab91b93d70563d` |
| `reviews/e5_critical_atom_full/REVIEW.md` | 429 | `5175b39734069cada021febb86d30d8733938d9104f2921e8fd3564c4d1a41b2` |

All five were actually hashed and fully read. Both mathematical reviews are
closed. Hashes establish byte identity, not mathematical truth.

## 6. Continued work and unchanged gates

An actual new R9 follow-up now reuses A1 in
`../continuation_round9/a1_general_quadratic_normone/REPORT.md`.
It freezes all odd $p$, all $c\in\overline{\mathbf F}_p$ and arbitrary
rational norm-one $w$, asking whether cofinite ordinary native products imply
$w=1$. Its sole new mechanism must address simultaneous balanced-atom
cancellation, not reuse the false factorwise implication. At most two targeted
source batches, no mathematical execution or automatic parameter census, and
only the assigned new path are allocated. It began while the R8 reviews ran.

A second actual R9 follow-up reuses A2 in
`../continuation_round9/a2_frobenius_twisted_bridge/REPORT.md`.
It keeps the full MS6 family and tests a distinct actual-incidence bridge:
$f(x)=x^q$ makes the native map equal to Frobenius on those points,
so finite-field Hilbert 90 applies to the orbit products there. The missing
step must produce one rational or finite algebraic transfer, with a fixed
$p$-power allowed as in the original conclusion. Uniformly bounded rational
interpolants for $g$ itself would be a stronger claim and are not assumed.
This has the same two-source-batch/no-mathematics-execution allocation and
disjoint ownership; the cyclic-coefficient attempt remains A1's task.

This continues the unchanged full MS6 family; the quadratic portion is a
named intermediate obligation, not a silent weakening of all $d\ge2$.
PC424-L, UL4, OM4 and RLG5 remain the four admitted contracts. No complete
fifth batch plan, new manuscript, PDF, formal evaluation, external-model call,
GPU job, new agent, old-proof edit, target arithmetic promotion, or Route-B
entry occurred. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
