# A4 — native cyclic resolvent and Witt ramification data

2026-09-09 UTC. Bounded theorem-first investigation; the contract below was
frozen before developing the proof supplement. Only this lane is write-owned.

## Outcome

**PROVED AUXILIARY BRIDGE / GHOST-ONLY REFINEMENT REFUTED / ORIGINAL
PC424-D UNCLOSED / NO ADMISSION PROPOSED.**

The [proof supplement](PROOF_SUPPLEMENT.md) supplies a concrete
native-coordinate Artin–Schreier test, a precise full-Witt sufficient
datum, and an exact all-level obstruction to replacing that datum by
its characteristic-$p$ ghosts. The refinement does not extract lost
lengths from an already-zero trace and does not change ordinary counts.

- On a generic $C_{p^e}$ native torsor, the formula below constructs
  $a_0$ in the orbit-invariant algebra without assuming connectedness.
  At a normalized quotient place over $k((t))$, its reduced polar part
  is nonzero **if and only if** local inertia is the full $C_{p^e}$.
- Full compatible reduced Witt pole orders $m_0,\ldots,m_{e-1}$ give
  upper breaks $u_i=\max_{j<i}p^{i-1-j}m_j$, then lower breaks and
  normalized native fixed lengths. These classical formulas are
  subtracted; their hypotheses and exact observable are preserved.
- A hand test on the actual quadratic period-$3$ cycle in
  characteristic $3$ gives $y^3-y=t^{-1}$, where
  $c=-t^2-t+1$. This certifies full local inertia and validates the
  extraction. It is not an all-level proof or a new census.
- For every fixed $e\ge2$, the vectors
  $(t^{-(p-1)},0,\ldots,0,t^{-M})$, with $p\nmid M$ sufficiently
  large, have identical lower truncation, all characteristic-$p$
  ghosts, ordinary closed-point data, and zero multiplication/twisted
  trace packets, but unbounded top native local length. This is an
  exact obstruction for local cyclic covers, not a claimed quadratic
  counterexample.

The principal gain is a checkable **A3→A4 interface**, not another
ramification theorem. A3 constructs the canonical parabolic Hensel
cycle factor for every $p,e$; A4's explicit resolvent now reduces its
full-inertia gap to a particular Laurent-series Artin–Schreier class.
Its nonvanishing for $e>1$ is not proved. Global transitivity on all
native cycles is a separate unresolved obligation.

## Exact question and decisive boundary

For $k=\overline{\mathbb F}_p$, odd $p$, $n=p^e$, and the reduced quadratic
dynatomic curve $X: \overline\Phi_n(x,c)=0$, retain the native action
$\sigma(x,c)=(x^2+c,c)$, one application per tick. Can one construct from
the generic native orbit a rational Artin–Schreier resolvent whose local
pole detects **full** $C_n$ inertia, and state exactly how full Witt data
recovers native local fixed-scheme lengths without identifying them with
ordinary orbit counts or fixed-parameter fibre lengths?

The proposed datum is not a Witt lift of an already-reduced trace. On the
generic $C_n$ torsor over the orbit quotient, form

$$
M(T)=\prod_{i=0}^{n-1}(T-\sigma^i x),\qquad
z=\frac{x^{n-1}}{M'(x)},\qquad
y=-\sum_{i=0}^{n-1}(i\bmod p)\sigma^i z,\qquad
a_0=y^p-y.
$$

Frozen target: prove that $a_0$ belongs to the orbit-invariant algebra and
represents the degree-$p$ quotient of the native $C_n$ torsor; a surviving
prime-to-$p$ pole in a locally Artin–Schreier-reduced representative must
force full inertia. A full compatible reduced Witt vector should then
give all lower breaks and local lengths for powers of the **same** native
generator. These are proposed auxiliary bridge statements, not an
all-$(p,e)$ component theorem.

Success is a complete exact extraction-and-implication theorem, including
the normalization/fibre-length compatibility condition. Failure is an
explicit violated implication or an unavoidable missing datum. Merely
renaming local fixed-point indices, Dold congruences, Lefschetz traces, or
the unknown multiplicities is excluded. No finite census is a theorem.

## Original data versus added data

Original ordinary data are distinct geometric native periodic points,
cycles, and any ordinary orbit sums or characteristic-$p$ multiplication
traces already allowed in R4. The added datum is the generic separable
native cyclic cover with its marked coordinate $x$, a normalized
orbit-quotient place, and the local class of the displayed rational
resolvent; full local-length recovery also needs a compatible reduced
Witt vector. These geometric/jet data are **not** consequences of the
ordinary numerical trace packet.

The original PC424-D question is classification of geometric irreducible
components for every odd $p$ and $e\ge1$, not merely local lengths. It
remains unchanged. PC424-L is likewise not replaced by scheme-weighted
orbit sums.

The precise length boundary is important. Witt ramification gives
lengths of $k[[u]]/(\sigma^j u-u)$ on a normalized native cover. For a
possibly singular dynatomic curve, its fixed-parameter local fibre
length is instead the sum of $v_q(c-c_0)$ over normalized branches
above the point. A branch contributes its quotient-parameter order
times its ramification index. The supplement proves this identity;
the quotient-parameter order and branch list are not supplied by
ordinary traces or silently inferred from a break sequence.

## Exact reusable interface and cross-line use

**Input from A3:** [REPORT.md](../a3_wild_tower/REPORT.md), “Proved
auxiliary interface” and “Exact A4 handoff”. With
$c=1/4-s^2/4$ and $z=x-(1+s)/2$, the canonical Hensel factor $M_e$
has degree $p^e$, distinct generic roots forming one native cycle,
and invariant algebra $k((s))$. This receiver read the full A3 proof
and checked those hypotheses against the extraction theorem.

**Output to A3/root:** substitute $M_e,z$ in the displayed resolvent.
The exact remaining local assertion is

$$
\operatorname{red}_{\rm AS}\!left[
\left(-\sum_{i=0}^{p^e-1}(i\bmod p)
\sigma^i\frac{z^{p^e-1}}{M_e'(z)}\right)^p
-\left(-\sum_{i=0}^{p^e-1}(i\bmod p)
\sigma^i\frac{z^{p^e-1}}{M_e'(z)}\right)
\right]\ne0.
$$

If proved at a level, it supplies full inertia for that cluster and
irreducibility of its local factor. Combined with **separately proved**
global orbit-quotient transitivity, it would give the marked-point
irreducibility required by R5. The root and A3 received this interface
when derived, before report completion; A3 incorporated and checked
its cluster compatibility. No formula for the displayed reduced
series at arbitrary $e$ is claimed.

**Input from B4, actually applied:** [PROOF_SUPPLEMENT.md,
Lemma 4](../b4_wild_jet_detection/PROOF_SUPPLEMENT.md) computes the
spectrum of every fixed ambient jet action from derivative eigenvalues
in any characteristic. Its proof was read and checked. Every native
germ in our counterfamily has multiplier $1$, so its ambient depth-$N$
characteristic polynomial is $(T-1)^N$ for every $N$, independently of
$M$. This strengthens the ghost-blind control: even all ambient jet
spectra fail there. Retaining the dynamical fixed ideal is different
and remains outside B4's no-go. No broader impossibility is inferred.

## Read inputs and initial subtraction

Read root/Hénon/batch AGENTS, SCOUT_PLAN, current-state entry, batch skill
and workflow, proof-writer, research-lit and idea-creator. Read R4
positive-characteristic contracts/proof/source/disposition and R5
positive-characteristic contracts/proof/source/disposition in full.
Inherited R4 trace blindness and R5 regular $c=0$ fibre / cyclic-stabilizer
formula are subtracted. R6 cocycle descent is not a dependency of this
cover-theoretic question and was not pulled into it.

Targeted local searches found classical iterative-residue/minimal-germ
ownership and the earlier Carlitz ramification tower; neither is this
native quadratic cyclic cover. Artin–Schreier–Witt classification and
ramification-break formulas are classical source inputs, not new claims.
The proposed increment is the exact native resolvent interface and its
compatibility boundary. Admission is reserved to the coordinator.

## Primary-source check and subtraction

Local collision checks preceded browsing. Searches targeted the active
R4/R5 proofs, Hénon obstruction records, iterative-residue ownership,
the earlier Carlitz ramification tower, and the C23 local-algebra
boundary. No old theorem was reopened as a missing proof. The ARS
router was inspected but no additional ARS pipeline was executed.

Actual primary sources used, with read scope:

| Source | Actual check and role |
| --- | --- |
| Elder–Keating, *Artin-Schreier-Witt extensions and ramification breaks*, [arXiv v1, 2025-03-21](https://arxiv.org/html/2503.16830v1) | §§1–2, including Theorem 2.3 and proof, were read. Its arbitrary-perfect-residue-field hypothesis covers $\overline{\mathbb F}_p$. This is source-owned ramification, not a quadratic application theorem. |
| Obus–Pries, *Wild tame-by-cyclic extensions*, [author-hosted 2009 preprint](https://www.math.colostate.edu/~pries/Preprints/10pries_obus409_JPPA.pdf) | Introduction, §2 local setting, and §§3.2–3.3/Lemmas 3.3–3.5 read as browser text; generator compatibility and prior ownership. No local PDF was downloaded or page-audited. |
| Elkies, [Higher Algebra 2001–02](https://people.math.harvard.edu/~elkies/M250.01/index.html) | Theorems 4.30–4.33 and displayed additive transfer construction; subtracts Hilbert-90/Artin–Schreier resolvent mechanism. |
| Doyle et al., [*Reduction of dynatomic curves*, Proposition 6.14](https://arxiv.org/html/1703.04172v2#S6.SS1) | Statement and full short proof rechecked: its tame lifting hypothesis excludes $p\mid n$. Our conditional local pole test does not claim that theorem already covers the wild case. |
| Lindahl–Rivera-Letelier, [arXiv:1311.4478v3](https://arxiv.org/html/1311.4478v3) | Introduction through Theorem C and Proposition 4.4's odd-prime proof checked for A3 compatibility. One native cycle is not one Galois orbit. |

Actual new search strings: `Artin Schreier Witt upper ramification
breaks reduced form max p pole degree Witt vectors cyclic extension`;
`Artin Schreier Witt dynamical dynatomic curves characteristic p cyclic
quotient ramification`; `Schmid Witt ramification jumps cyclic p n
extensions standard form upper jumps theorem`; `"Artin-Schreier"
"resolvent" "trace" cyclic extension`; `"dynatomic" "Witt"`;
`"dynatomic" "Artin-Schreier" quotient`; `"Lagrange interpolation"
"trace" "derivative" separable polynomial`. No recency filter,
private manuscript upload, external model or mathematical program was
used. Leads not listed above were not promoted to theorem evidence.
No global literature-completeness or priority claim follows from this
bounded search.

## Execution boundary

Mathematical program count: **0**. None was requested. The diagnostic
was an exact hand derivation. Any later computation requires its own
written bounded discriminating question and coordinator allocation.
No old-run/build, PDF, external-model upload, evaluator, shared index,
Git or configuration write is authorized here.

The proof-writer skill kept the original question and added-data
assumptions separate; the batch and literature skills required the
classical source subtraction and actionable handoff. These are
author-produced auxiliary results, not independent internal review,
human review, a formal evaluation or a paper admission.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
