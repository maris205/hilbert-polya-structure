# A1: ordinary periodic sums and polynomial coboundaries

2026-09-09 UTC. One unchanged original question, zero proposed admissions,
zero mathematical programs. The question and feasibility boundary were
written before the proof supplement or any mathematical computation.

## Original claim (unchanged)

For every odd prime $p$, $k=\overline{\mathbb F}_p$, and $c\in k$, put
$f(x)=x^2+c$ and $\Delta Q=Q\circ f-Q$. Determine whether

$$K_c=\{h\in k[x]:\sum_{a\in O}h(a)=0\text{ for every ordinary primitive }f\text{-orbit }O\}
=B_c=\Delta k[x],$$

or classify the full defect if equality fails. Each distinct point of a
primitive geometric orbit is counted once, including periods divisible by
$p$. The native clock is one iterate of $(x,y)\mapsto(f(x),y+h(x))$.

## Frozen route and cheap failure criterion

The imported normal form is $k[x]=B_c\oplus(k\oplus xk[x^2])$. A1 tests
direct polynomial-quotient and finite-field separation, independently
of A2's invariant Artin--Schreier-cover construction. The precise success
criterion is detection of every nonzero normal representative by at least
one ordinary primitive cycle, uniformly in the original parameters.

Before a substantial proof or any computation, the cheap tests are:

1. Track distinct periodic points versus scheme multiplicities in every
   proposed quotient. A trace killed by characteristic $p$ is not ordinary
   primitive-cycle information.
2. In the monomial specialization, check exponent collisions modulo the
   prime-to-$p$ part of $2^n-1$ before making a coefficient-separation claim.
3. For finite-field transfer polynomials, identify an actual degree bound
   independent of field size, or an equivalent proved compactness mechanism.
   Arbitrary interpolants are not algebraic transfers.

A surviving nonzero normal representative with zero sums on every cycle
would refute equality, but one example would not itself classify the full
defect. Failure to remove exponent collisions or unbounded interpolation
degrees is only failure of this route, not a no-go for the original claim.

## Imported inputs and subtraction

- R6 [algebraic descent](../../../research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md), full proof: for a polynomial base of degree prime to $p$, an already-existing compatible finite algebraic transfer is polynomial. Its construction from periodic sums is **not proved**.
- Initial [normal form and finite interpolation](../../../research_c424_c428/positive_characteristic/PROOF_PACKAGE.md), complete: telescoping, orbitwise functions, finite-field interpolation, uniform-degree equivalence, normal form and Frobenius saturation are old inputs.
- R2 [cyclic quotient and binary-support proof](../../../research_c424_c428/continuation_round2/positive_characteristic/PROOF_PACKAGE.md), Steps 1--3 and the Jacobian counterexample in Step 5: nonvanishing in the full periodic algebra is already proved; passage to its reduced quotient is not.
- R3 [prime-level multiplicity obstruction](../../../research_c424_c428/continuation_round3/positive_characteristic/PROOF_PACKAGE.md), complete: a hypothetical defect requires exponentially high contacts on genuinely new prime cycles. This is imported, not a new A1 theorem.
- The R6 [frozen question](../../../research_c424_c428/continuation_round6/positive_characteristic/FROZEN_QUESTION.md), [source audit](../../../research_c424_c428/continuation_round6/positive_characteristic/SOURCE_AUDIT.md), and [disposition](../../../research_c424_c428/continuation_round6/positive_characteristic/DISPOSITION.md) were read; their Mahler/algebraicity scope boundaries are retained.

## Result and original-claim status

**Original PC424-L: NOT CURRENTLY JUSTIFIED / UNCLOSED.** This lane neither
proves equality for all $(p,c)$ nor constructs a nonzero full defect. The
original all-parameter, all-degree, all-ordinary-period statement survives
unchanged. No weakened statement is proposed as a replacement paper.

The complete small auxiliary result is in
[PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md). Put $N_c=K_c\cap V$, identified
with $K_c/B_c$ by the imported normal form. Then:

1. $N_c$ is a free left $k[\mathcal F]$-module, with
   $\mathcal Fv=v^p$ and $\mathcal Fa=a^p\mathcal F$. Its degree-adapted
   basis is constructed by the first occupied leading degree on each
   $p$-power chain. No skew-ring structure theorem is invoked.
2. $\dim_kN_c$ is either zero or countably infinite. A degree-$D$ defect
   would give at least $1+\lfloor\log_p(M/D)\rfloor$ independent defects
   through degree $M\ge D$.
3. If $c\in\mathbb F_q$, every bounded-degree defect space has an
   $\mathbb F_q$-basis. Any defect would therefore descend to the field of
   definition of the base without increasing its degree.

These are elementary structural deductions from the imported normal form
and Frobenius identities. The unknown occupied chains and their unknown
generators are **not** a full classification. In particular, item 1 does
not decide whether any generator exists, and finite rank over
$k[\mathcal F]$ is not finite dimension over $k$. Source-level auxiliary
progress is not an independent substantial-question closure.

## What the direct route actually established or failed to establish

### A. The monomial control is already covered by the imported mechanism

For $c=0$, the full iterate polynomial is $F_n=x^{2^n}-x$. If
$p\nmid2^n-1$, it is squarefree: its derivative is $-1$ at zero and
$2^n-1$ at every nonzero root. Let $t=\operatorname{ord}_{\mathbb F_p^*}(2)$.
Since $p$ is odd, $t>1$. For every sufficiently large prime $n$, $t$ does
not divide $n$, so $p\nmid2^n-1$. Choose such $n$ also larger than
$2\lfloor\log_2D\rfloor$ for a proposed nonzero normal degree $D$.
The R2 binary-support lemma gives a nonzero trace class in $k[x]/(F_n)$;
squarefreeness makes it nonzero at an ordinary point. Hence $K_0=B_0$.

This is a short consequence of the imported R2 theorem, not a new all-$c$
result. A direct exponent-necklace proof would duplicate the same control.
At excluded monomial levels, the ordinary nonzero points are roots of
$x^{(2^n-1)/p^{v_p(2^n-1)}}-1$, not $2^n-1$ distinct roots. Pretending
otherwise incorrectly deletes precisely the characteristic-$p$ issue.

### B. General $c$ retains the nilradical gap

Write $H_n(h)=\sum_{i=0}^{n-1}h\circ f^{\circ i}$ and
$F_n=f^{\circ n}-x$. The ordinary hypothesis is exactly

$$\operatorname{rad}(F_n)\mid H_n(h)\quad\text{for every }n.$$

Taking $n$ equal to each primitive length proves the converse without
dividing by that length. The R2 result already establishes
$[H_n(v)]\ne0$ in $k[x]/(F_n)$ for every sufficiently large $n$ and every
nonzero positive-degree normal $v$. A hypothetical defect therefore has
nonzero nilpotent trace classes; the argument does not exclude them.

Multiplying the trace by $F_n'$ is not an equivalent replacement for
ordinary vanishing. The imported R2 Step 5 hand example
$p=3,c=0,n=6,h=x$ satisfies $F_6\mid F_6'H_6$ while $H_6$ is nonzero on
an ordinary primitive three-cycle. No rerun was made. Thus Jacobian
annihilation alone cannot supply the missing implication.

### C. Finite-field linear algebra is still not a global transfer

Choose $q$ with $c,h\in\mathbb F_q[x]$. For every $r\ge1$, the finite
functional-graph argument gives a solution of

$$\Delta Q_r\equiv h\pmod{x^{q^r}-x},\qquad \deg Q_r<q^r.$$

One can choose $Q_r\in\mathbb F_q[x]$: after reducing modulo the monic
polynomial $x^{q^r}-x$, this is a finite linear system with coefficients
in $\mathbb F_q$. Its solvability over $\mathbb F_{q^r}$ implies its
solvability over $\mathbb F_q$, by Gaussian elimination over the latter.
The coefficient-field reduction does **not** bound $\deg Q_r$.

The imported degree criterion is still exact: if transfers have a single
degree bound $M$ for arbitrarily large $r$, then choosing
$q^r>\max(2M,\deg h)$ turns the congruence into a polynomial identity.
Neither finite-field coefficient descent nor compactness of a sequence of
coefficient vectors supplies that bound. No field-size-independent
algebraic relation or compatible finite extension has been obtained.

### D. The precise new finiteness interface

The supplement gives the sufficient target

$$\dim_k(K_c/B_c)<\infty\quad\Longrightarrow\quad K_c=B_c.$$

The hypothesis on the left is unproved. It is useful because it asks only
for a finite-dimensionality theorem, not an explicit transfer degree
bound. It is not implied by the finite dimension of **each** degree slice,
by finite $k[\mathcal F]$-generation, or by finite-field interpolation.
The free-module proof explicitly prevents these quantifier substitutions.

Equivalently, a dual route would have to prove density of ordinary cycle
functionals among invariant algebraic linear functionals. In detail, let
$P=k[x]$, $I=B_c^\perp\subseteq P^*=\operatorname{Hom}_k(P,k)$, and
$E$ be the span of $h\mapsto S_h(O)$ over all ordinary cycles. In the
topology of agreement on finitely many polynomials,

$$K_c=B_c\quad\Longleftrightarrow\quad\overline E=I.$$

Here $E^\perp=K_c$, $I=B_c^\perp$, and the equivalence is algebraic
double-annihilator duality: a functional outside a closure can be
separated on a finite-dimensional polynomial test space by one polynomial.
This is an exact reformulation, not a proved density theorem. Pointwise
density of periodic points alone says nothing about invariant-functional
density with polynomial coboundary regularity.

## Reusable handoff interfaces

| Consumer | Assumptions and output | Missing compatibility |
| --- | --- | --- |
| A2 / global algebraic route | Supplement §§1--3: all odd $p$, all $c$; any finite-dimensional defect quotient is zero | Prove actual global finite-dimensionality; finite module rank is insufficient |
| A2 / a future approved exact diagnostic | Supplement §4: $c\in\mathbb F_q$; a defect has a representative over $\mathbb F_q$ of the same degree bound | No degree or period cutoff is supplied; a bounded search cannot certify the full statement |
| A3/A4 | Imported R3: a degree-$D$ defect requires initial contacts $e_\ell>2^{(\ell+1)/2}/(pD)$ on new exact prime-$\ell$ multiplier-one cycles | A bound for initial contacts on new cycles is needed; $p$-power growth at one old germ is a different quantifier |
| B1/B2 | Veech §2, Corollary 2.11, surfaced a classical multiplicative-coset local/global result | Full body was not verified here; nonlinear Hénon time must first reduce to one multiplicative coset, which is unproved |

These messages were sent to the coordinator while work was in progress,
not withheld until this report. The coordinator owns cross-lane forwarding
and review allocation. No child agent was launched by this lane.

## Bounded primary-source verification

Theoretical correctness here rests on the displayed proofs and the cited
local inputs. External sources are comparisons, not missing-lemma surrogates.

| Source | Actual access and verified claim | Role and limitation |
| --- | --- | --- |
| William A. Veech, *Periodic points and invariant pseudomeasures for toral endomorphisms*, ETDS 6 (1986), 449--473, DOI 10.1017/S0143385700003606 | [Publisher HTML](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/periodic-points-and-invariant-pseudomeasures-for-toral-endomorphisms/5AF4A715A07BF8E0AC967645A282DA24): title, author, venue, print year, pages and full abstract read. It states smooth coboundary regularity for ergodic toral endomorphisms with zero periodic sums. | Classical periodic-functional analogy only. Smooth functions on a real torus are not polynomials over $k$. The indexed PDF exposed Theorem 1.1 and Corollary 2.11 excerpts, but direct PDF retrieval timed out; no full body/proof review is claimed. |
| Michelle Manes and Bianca Thompson, *Periodic points in towers of finite fields for polynomials associated to algebraic groups* (2013) | [arXiv:1301.6158](https://arxiv.org/abs/1301.6158): metadata, submission record and full abstract read; concerns periodic proportions for power and Chebyshev maps. | Source subtraction for group-based specializations. No body theorem or polynomial-coboundary criterion was read or used. Journal publication was not verified. |
| Derek Garton, *Periodic points of polynomials over finite fields*, arXiv v3 (2021) | [arXiv:2103.16533](https://arxiv.org/abs/2103.16533): metadata, history and full abstract read. It gives an average periodic-proportion bound over quadratic families; metadata records Trans. AMS 375 (2022), 4849--4871. | Average finite-field proportions do not give all-$c$ polynomial regularity. No body theorem was inspected; journal metadata was not independently checked at the publisher. |

For mathematical claim fitness, Veech is verified primary publication
metadata/abstract evidence for the stated classical comparison; the two
arXiv records are primary abstract-only evidence for their stated scopes.
None is evidence for the missing all-$c$ bridge. Empirical-study levels
I--VII are not a proof-strength scale. No source was graded as proving an
unseen theorem, and no global novelty, COI, retraction or predatory-venue
clearance is claimed. The direct DOI request for Veech also returned an
internal retrieval error; the later direct publisher HTML succeeded.

Sixteen browser search formulations were submitted, covering polynomial
cohomological equations/periodic sums over finite fields; algebraic Livšic
and invariant pseudomeasures; finite-field coboundaries; and parabolic
multiplier-one/initial-multiplicity bounds in positive characteristic.
The exact-title Veech lookup is included in sixteen. Broad irrelevant
matches and uninspected smooth/ultrametric sources were not proof inputs.
This is a bounded search, not a systematic review or proof that no relevant
theorem exists.

Available-tool discovery showed no Zotero/Obsidian tools. A targeted
`arxiv_fetch.py` filename search in the repository skill and selected local
skill locations found no script, so browser metadata was used. The root
`papers/` tree belongs to another stream and was not scanned; relevant
local Markdown proofs supplied the local-first source context. No local
PDF was opened, downloaded or page-anchored.

## Disposition, skills and execution receipt

Stop this pass with the original gap visible. A low-degree census would not
test the missing all-degree finiteness/algebraicity implication, so none was
requested or run. A next proof attempt should supply one of: actual global
finite-dimensionality; a finite algebraic transfer from the cycle data; or
a sufficiently strong all-parameter initial-contact bound. Merely repeating
the imported descent theorem or the monomial control is not that progress.

The repository batch workflow prevented auxiliary lemmas from being counted
as a paper; proof-writer required the original claim and the proved
auxiliary scope to remain separate; research-lit enforced local-first
comparison. The ARS router, source-verification role and source-quality
guidance were used only for the bounded source audit, not an entire
six-phase research/report pipeline. No external review or human-read
attestation is claimed. This is AI-assisted author research.

Written files: exactly this report and its proof supplement, both in the
assigned lane. Mathematical programs and old certification reruns: **0**.
No GPU, external LLM/API upload, manuscript/PDF, formal evaluation,
shared-state/index, earlier-batch, Git or release mutation was performed.
Read/search/edit calls were not counted as mathematical experiments.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force: no target Euler factors,
root numbers, automorphy or Hilbert--Pólya realization is established.
