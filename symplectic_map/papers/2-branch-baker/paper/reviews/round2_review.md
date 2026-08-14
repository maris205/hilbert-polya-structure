# Round-2 Technical Review

Manuscript: *Finite-Rank Obstructions for Locally Constant Multiplier Clocks:
An Audited PCF Markov--Baker Note*

Artifact reviewed: `paper_round1.pdf` (16 pages; SHA-256
`0afa8833b65aaa09ad286205d34f483f10af32364d1128f46f327b263fae2ec9`)

Overall score: **6/10**

Recommendation: **Major revision, but the remaining mathematical repair is
localized. Potentially publishable as a specialist note after that repair.**

Confidence: **4/5**

## Review scope

I read the complete round-1 manuscript and rendered PDF, the round-1 review,
the improvement log, proof package, citation-verification record, source lock,
exact preflight, parent audit, experiment and validation reports, bibliography,
compile log, and final result manifest. I also checked the branch formulas,
cycle counts, determinant identities, relevant implementation logic for the
inverse-branch parent audit, PDF metadata/font embedding, and the rendered
layout of all 16 pages.

The frozen result hashes printed in the final manifest agree with the current
`source_lock.json`, `exact_preflight.json`, `ledger.json`, `parent_audit.json`,
and three floating-stress JSON files. The round-1 PDF is byte-identical to the
current `manuscript.pdf`. The compile log contains no undefined citations or
references and no overfull/underfull box warnings; all fonts are embedded.

## Executive assessment

The revision is materially better. It now calls itself a specialist note,
states that the finite-span observation is elementary and makes no priority
claim for it, cites standard symbolic/weighted-orbit sources, restricts
symplecticity to branch interiors in the abstract, compresses the main audit
section, and moves control details to the appendix. The main finite-rank
theorem, branchwise exact-symplectic proposition, graph-cycle calculations,
signed determinant conventions, and rank-one multiplier corollary remain
correct as stated.

The new boundary lemma correctly identifies the only *periodic endpoint* and
correctly shows that its allowed symbolic names form one primitive two-cycle.
It does not, however, yet establish the preceding assertion that every
admissible periodic word determines exactly one parent periodic point away
from the endpoints. A monotonicity partition and its adjacency matrix do not
give this injectivity by themselves: one must prove that the partition is
generating, equivalently that the relevant nested itinerary cylinders shrink
to points (or at least that no nontrivial periodic itinerary fibre exists).
This is precisely the possibility allowed by the standard piecewise-monotone
coding theory cited in the proof. Consequently the intended all-period result
is very plausible and appears repairable, but the claimed direct proof is not
yet complete.

## Disposition of the round-1 requests

| Round-1 request | Round-2 status | Assessment |
|---|---|---|
| Direct all-period boundary proof | **Partially addressed** | Endpoint part is correct; generating/injectivity step is still missing. |
| Reposition as a note/certificate | **Addressed** | Title, abstract, introduction, prior-work section, and conclusion are now appropriately restrained. |
| Theorem-focused literature context | **Addressed** | Lind--Marcus, Parry--Pollicott, and Marcus--Tuncel are relevant and the manuscript makes no priority claim. |
| Abstract: branch interiors | **Addressed** | The abstract now matches the proposition's regularity boundary. |
| Compress Section 6 | **Addressed** | Main text is now three concise audit paragraphs; evidence/control detail is in Appendix D. |
| Subordinate project labels | **Substantially addressed** | Ordinary mathematical conclusions lead; internal tags are retained only for traceability. |

## CRITICAL findings

**None.** I found no counterexample or algebraic error in the finite-rank
theorem, the affine carrier proposition, or the rank-one multiplier product.

## MAJOR findings

### 1. Lemma 3 still assumes, rather than proves, the generating property needed for the all-period quotient

The decisive sentence is at `manuscript.tex` lines 551--554:

> an admissible periodic word determines its parent periodic point; the
> exceptional multiplicities and period changes can occur only when an
> iterate lies on a monotonicity-partition endpoint.

The remainder of the proof (lines 558--569) correctly proves the following
conditional statement: **if** the only coding multiplicities come from
partition endpoints, then $d$ is the sole periodic endpoint, and its closed
boundary names are forced to alternate $1,2,1,2,\ldots$. Thus there is one
primitive symbolic period-two orbit over the fixed point $d$, and no other
endpoint correction.

What is missing is the condition before that argument. For a general
piecewise-monotone map, an itinerary fibre can be a nontrivial interval. In
fact, Hofbauer (1985), Lemma 1, explicitly separates singleton fibres from
interval fibres and explains that an interval fibre can contain periodic
points. Therefore the Hofbauer citation supports the framework and the
boundary-period phenomenon, but it does **not** by itself justify the stronger
claim made at lines 551--554. Lind--Marcus is likewise standard symbolic
background, not a proof that this particular nonlinear interval partition is
generating.

The statement is likely true here because this quadratic is a strictly
preperiodic (Misiurewicz/subhyperbolic) map. The fixed endpoint has

\[
 |f'_u(d)|=2u(u-1)>1;
\]

the frozen lower bound $u>3859/2500$ already gives
$2u(u-1)>1.678$. The critical point and both core endpoints eventually land
on that repelling fixed point. These facts should rule out a nontrivial
homterval and make the postcritical Markov partition generating, but that
argument or an exact applicable theorem must appear in the manuscript.

**Minimum actionable repair:**

1. Define the coding map explicitly by nested cylinders
   \[
   K_n(\omega)=I_{\omega_0}\cap f^{-1}I_{\omega_1}\cap\cdots
   \cap f^{-n}I_{\omega_n}.
   \]
2. Prove or cite an applicable result showing
   `diam(K_n(omega)) -> 0` away from the declared closed-endpoint naming
   ambiguity. A concise route is the homterval/no-wandering-interval lemma for
   a nonflat negative-Schwarzian unimodal map, together with the exact fact
   that the critical orbit lands on the repelling $d$. A complex-dynamical
   route via the Misiurewicz/subhyperbolic conjugate $z\mapsto z^2-u$ is also
   acceptable if the cited theorem directly gives shrinking real cylinders.
3. State why injectivity of the off-boundary coding also preserves *least*
   period: if a primitive word mapped to a point of smaller period, the point
   and its shorter iterate would have the same unique itinerary.
4. Then retain the existing endpoint calculation unchanged; it correctly
   completes the proof.

An equivalent repair is to identify this three-state graph explicitly with
the applicable finite Hofbauer/Markov diagram and quote the precise theorem
that supplies the one-to-one periodic correspondence, while checking all its
hypotheses. Merely saying “standard monotone Markov coding” is not enough.

If the authors do not want to add this generating argument, the all-period
claims in the abstract, Lemma 3, equations (17)--(18), and Table 4 must be
weakened to the independently audited cutoff $n\leq20$.

### 2. The contribution still has a specialist-note venue ceiling

The revision now handles this honestly, so this is a venue-fit limitation
rather than an overclaim. The finite-rank theorem is an immediate finite-span
argument once the clock class is specified, and the PCF carrier is a carefully
audited negative control rather than a result about the nonlinear parent
derivative. The current positioning is defensible for a specialist note,
methods/certification note, or archival companion. It is still unlikely to
clear the significance bar of a broad nonlinear-dynamics or arithmetic-
dynamics full-paper venue without an additional theorem of materially greater
scope.

The main Section 6 is now sufficiently compressed. If a short-note venue has
a strict length limit, the reproducibility passport and Figure 3 can be made a
supplement without changing the mathematical narrative.

## MINOR findings

### 1. Two manual line breaks create visible dangling-hyphen spacing

The source has `period-` followed by a newline before `\(2k\)` at lines
69--70, and `length-` followed by a newline before `\(m\)` at lines 264--265.
The rendered PDF visibly says “period- 2k” and “length- m.” Use “period
$2k$” and “length-$m$” (or keep each construction unbroken).

### 2. Figure 3 floats into Section 7

Figure 3 belongs to Section 6 but appears at the top of PDF page 11 after the
Discussion section has already begun on page 10, splitting the discussion
across the audit figure. Insert a float barrier before Section 7, use an
appropriate nonfloating placement, or move the figure to the appendix with
the detailed audit table.

### 3. The Bowen--Lanford bibliography name is parsed incorrectly

The rendered reference reads “R. Bowen and III O. E. Lanford.” The BibTeX
name at `references.bib` line 132 should use BibTeX's suffix form, e.g.
`Lanford, III, O. E.`, so that it renders as “O. E. Lanford III.” The DOI and
other metadata are otherwise correct.

### 4. The exact audit language in Table 4 is contingent on the Lemma 3 repair

The Table 4 boundary row currently says the evidence supports the all-period
parent quotient. That is appropriate after the generating argument is added;
until then, the computational evidence only supports periods through 20. No
numerical result is wrong, but the inference label must track the final proof
status.

## Mathematical and numerical checks

### Finite-rank theorem

The higher-block recoding, containment
$V_{\mathrm{cyc}}\subseteq V$, rational independence of distinct prime
logarithms, cardinality bound, and finite-rank sharpness example are correct.
The theorem's exclusions of variable roofs, countable-state models, growing
model families, and nonmultiplicative matrix spectral radii are appropriately
stated.

### Carrier proposition

The Perron--Frobenius vectors and areas are correct. On every allowed branch,

\[
 DB_{ij}=\operatorname{diag}(\sigma_{ij}\sqrt2,
 \sigma_{ij}/\sqrt2)
\]

has determinant $+1$. The simultaneous reversal on decreasing branches is
necessary and correctly implemented. For the affine form
$\bigl(ax+b,a^{-1}y+c\bigr)$, the calculation
$B^*(x\,dy)-x\,dy=(b/a)dy=d((b/a)y)$ correctly proves branchwise exactness.
The half-open and closed-relation conventions are stated without claiming a
global $C^1$ symplectomorphism.

### Cycle and determinant ledger

The eigenvalues $0,\sqrt2,-\sqrt2$, fixed-point counts, Möbius inversion,
primitive vector, total 226, and

\[
 \det(I-zA)=1-2z^2
\]

all agree. The endpoint replacement algebra
$(1-z^2)/(1-z)=1+z$ is correct once the sole-identification lemma is fully
proved. The calculations $W^3=0$,
$\det(I-zW)=1$, the separate parent factor-orientation object $1-z$, and
the Lefschetz convention $1/(1-z)$ are mutually consistent.

### Multiplier corollary

Bipartiteness forces period $2k$; the constant edge multiplier gives
$|\Lambda_u|=2^k$ and $L=k\log2$. Hence the only rational prime hit is
$p=2$. The weighted Euler product

\[
 Z_u(s)=\det(I-2^{-s/2}A)^{-1}
       =(1-2^{1-s})^{-1}
\]

and its absolute-convergence half-plane $\operatorname{Re}s>1$ is correct.
The manuscript consistently excludes the nonlinear parent derivative from
this corollary.

### Frozen computation

The reported 89 tests, six exact gates, three counts of 16,777,216 per-step
checks, maximum roundtrip error $1.388\times10^{-16}$, zero mismatches and
boundary failures, 100-digit audit, and maximum residual
$9.706\times10^{-98}$ agree across the manuscript and frozen artifacts. The
paper correctly calls the parent computation a high-precision consistency
audit rather than interval certification and correctly avoids treating the
three deterministic splits as independent samples.

## Citation assessment

The three theorem-focused additions are appropriate within the claims made:

- **Lind--Marcus (2021)** appropriately supports higher-block presentation,
  finite-state coding, and standard periodic-orbit bookkeeping.
- **Parry--Pollicott (1990)** appropriately supports the established
  suspension/weighted-periodic-orbit and dynamical-zeta framework.
- **Marcus--Tuncel (1991)** is acceptable context for mature finite-state
  weight-per-symbol invariants built from periodic Markov data.

The manuscript correctly does not claim that any of these sources states the
prime-log corollary in its present form. The only citation caveat is that
Lind--Marcus and Hofbauer do not eliminate the candidate-specific itinerary-
fibre issue without an additional generating/homterval argument. The sixteen
audited bibliography entries otherwise match their restrained uses; the
Lanford suffix is a formatting correction only.

## Submission verdict

**Current version: not yet submission-ready because the all-period parent
quotient is still missing one necessary generating/injectivity step.** This is
a localized gap, not evidence that the endpoint conclusion is false. Add a
precise nested-cylinder/homterval argument (or an exact theorem with checked
hypotheses), make the three production fixes, update the contingent Table 4
inference label, and recompile.

After that repair, I would regard the manuscript as **technically ready for a
specialist-note venue**, with an expected score around **7/10** under that
venue framing. I would not recommend marketing it as a broad full research
article: its value is the explicit, convention-safe arithmetic design
certificate and audited negative example, not a deep new theorem about smooth
or arithmetic dynamics.
