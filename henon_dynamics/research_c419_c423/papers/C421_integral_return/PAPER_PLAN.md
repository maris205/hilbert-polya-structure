# C421 paper plan

Date: 2026-09-08 UTC. Manuscript title: **Integral periodic orbits of a
cubic three-term recurrence**. Type: exact computer-assisted arithmetic-dynamics
classification. Format: English, anonymous, standalone `article`, 11pt.
No target ML conference, hard page limit, minimum page count, empirical
section or fabricated experiment is imposed.

**One-sentence contribution.** For every integer additive forcing, we
classify all ordinary integral periodic orbits of one fixed trace-map
automorphism by a parameter-free difference reduction and a completely
terminated finite certificate, and derive every primitive period and
invariant-level return count.

The overall batch outline has been approved by the coordinator after an
actual nonauthor outline review with no mandatory correction. This
per-paper plan records its complete evidence/production interpretation;
it does not claim a separate outline review that never occurred. The
coordinator has subsequently authorized full LaTeX drafting and one
baseline PDF, followed by two actual nonauthor manuscript-review rounds.

Production checkpoint: the complete 18-page baseline has now been
compiled, text-checked and visually inspected on every page. See
[BASELINE_REPORT.md](BASELINE_REPORT.md) for the actual build attempts,
frozen PDF/source identifiers and pending nonauthor manuscript-review
gates. The signed case proof is entirely in §4, the full certificate
algorithms in §5, least periods in §6, level counts in §7, and the full
primary source listing in Appendix A. These actual placements supersede
the provisional appendix/section numbering below without dropping any
claim.

## 1. Frozen mathematical scope and story

For every $a,k\in\mathbb Z$, keep
$$
T_a(x,y,z)=(y,z,yz+a-x),\qquad
K_a=x^2+y^2+z^2-xyz-a(x+y+z).
$$
The map is a polynomial automorphism of $\mathbb Z^3$, with inverse
$(xy+a-z,x,y)$. No ordinary integer point is omitted on singular levels.
One map application is the native clock. A scalar word denotes its
consecutive triples; only cyclic rotation identifies one directed
orbit. Reversal is a symmetry of the recurrence, not a universal orbit
identification.

What: the complete all-forcing integer cycle list and exact per-level
counts. Why: bounded experiments do not exhaust unbounded forcing or
coordinates, and whole-group orbit theorems have different quantifiers.
So what: a parameter-free difference mechanism reduces an all-parameter
integer problem to explicit infinite channels and one genuinely complete
finite computation, with no chosen period cutoff.

The contribution is this one exhaustive classification, not the sum of
several separately claimed papers on a period bound, sporadic words,
four-cycle family and zeta product. Classical trace geometry and the
entire prior unforced classification are expressly deducted.

## 2. Claims–evidence matrix

| Claim | Complete supporting evidence | Status and planned location |
| --- | --- | --- |
| Every integer periodic orbit is one of ten disjoint rows below | Accepted analytic proof §§1–4, independently reconstructed full finite core, classification and final coordinator review | Accepted computer-assisted theorem; §2 statement, §§3–5 proof |
| The reduction is uniform in forcing, level and period | Exact identity $d_{i-1}+d_{i+1}=(x_{i+1}+1)d_i$, high-coordinate channel, all five extremal centers with both signs | Analytic proof and independent analytic review passed; §§3–4 and typeset Appendix A |
| Every row has its exact native least period and only the stated representative identifications | Complete word/degeneracy proof, reversal closure and all-parameter symbolic identities | Accepted exact proof; §6, not inferred from observed traversal lengths |
| Every fixed level has explicit finite ordinary counts and rational dynamical zeta | Invariant substitutions and all nine square/parity rules; separate symbolic receipt and coordinator check | Accepted consequence; §6 |

The exact source paths, complete read scopes, historical identifiers and
both algorithms are in [EVIDENCE_PREPARATION.md](EVIDENCE_PREPARATION.md).
That document is an assembly aid; it will not replace typeset arguments
inside the article.

## 3. Main theorem table to typeset completely

Each row is one directed native orbit for every allowed parameter.
In the manuscript long words may be aligned separately from the guard
and level table so that no formula is shrunk or clipped.

| Least period | Scalar word and complete guard | Level $k$ |
| --- | --- | --- |
| 1 | $(r)$, $r\in\mathbb Z$, $a=2r-r^2$ | $r^2(2r-3)$ |
| 2 | $(u,v)$, $u<v$, $a=u+v-uv$ | $uv(u+v-3)$ |
| 3 | $(-2,-2,t)$, $a=2t-4$, $t\ne-2$ | $8-(t-4)^2$ |
| 4 | $(-1,t,-1,a+1-t)$, $2t<a+1$ | $t^2-(a+1)t+2a+2$ |
| 5 | $(-1,t,0,0,-1-t)$, $a=-1$, $t\in\mathbb Z\setminus\{-1\}$ | $t(t+1)$ |
| 5 | $(-4,-2,-3,-3,-2)$, $a=-13$ | $-64$ |
| 6 | $(0,0,t,0,0,-t)$, $a=0$, $t\ge1$ | $t^2$ |
| 8 | $(-1,t,1,t,-1,-t-2,1,-t-2)$, $a=-1$, $t\ge0$ | $(t+1)^2+1$ |
| 9 | $(-2,-1,0,0,-1,-2,0,-1,0)$, $a=-2$ | $-1$ |
| 12 | $(1,m,1,m-1,-1,-m,1,1-m,1,-m,-1,m-1)$, $a=0$, $m\ge1$ | $m^2-m+2$ |

The global possible-period set is exactly $\{1,2,3,4,5,6,8,9,12\}$.
Thus $T_a^{360}$ fixes its integer periodic locus, not its whole phase
space. The full theorem must be labelled computer-assisted at its first
statement rather than hiding that dependency in the back matter.

## 4. Section-by-section structure

Seven numbered main sections, abstract and three typeset appendices are
planned. Length follows the complete argument; no allocation sums to an
invented venue limit.

### Abstract

Use approximately 150–200 words, subject to clarity rather than quota.
Open with the all-$a$ classification and the actual map. State the
uniform difference reduction, explicit channels and finite certificate.
Preview the complete period set, the two sporadic cycles and exact
level counts. Call the proof computer-assisted. Avoid undefined
abbreviations, “first” priority claims, target arithmetic or citations
needed to understand the abstract.

### §1. Introduction and relation to trace-map dynamics

Define the single-map integer problem immediately and explain why
unbounded forcing and oriented returns are the exact obstacles. Give
three concrete contribution bullets: uniform reduction, exhaustive
classification with complete certificate, and exact level arithmetic.
State the possible periods before the technical proof.

Synthesize prior work in three short thematic paragraphs: classical
trace-map families/reversibility, cubic-surface group actions versus a
fixed map, and prior unforced integer exhaustion. Include the exact sign
change to the classical cubic family. Do not force a full-page standalone
Related Work section or extend the bibliography without a specific claim.
The main result is visible by the end of this section.

### §2. Complete integral orbit classification

Set the native scalar-word convention, invariant levels, ordinary points
and oriented equivalence. Print all ten rows above with guards and
levels, state the exact possible-period set and the scope of the
$360$-iterate corollary. Give a short road map of the mathematical versus
finite-computational dependencies. No proof is delegated to an old MD
link. State all-level infinitude versus fixed-level finiteness clearly.

### §3. The parameter-free difference mechanism

Derive the scalar recurrence and the exact difference identity by
subtraction. Prove propagation of adjacent zero differences; resolve
$D=0$ completely. Prove the height-versus-difference lemma: if some
$|x_i+1|>3D$, the four-step word is forced. Include both neighbors equal
to $m+e$, the corrected sign from the accepted proof. Present the
contrapositive at every phase, with the universal residual interval.

### §4. All large-amplitude channels

Assume $D>100$, choose the extremal triple, and derive all five possible
centers. Prove centers $1,-3$ impossible. At center $-1$, resolve
$E=0$ and $E=-\kappa$; show $\kappa\in\{1,2\}$ after excluding
$3,4$. Print the bounded forcing arguments and the exact surviving
$a=-1$ five/eight channels and $a=0$ twelve channel.

For centers $0,-2$, state the second reversal's sign change explicitly:
$(d_0,p,q)\mapsto(-d_0,-q,-p)$. Keep $\varepsilon=\pm1$ thereafter.
Give the complete outcome table in the main text and typeset every
signed branch and strict inequality in Appendix A. Close the symbolic
list under reversal, especially the five-cycle parameter involution
$t\mapsto-1-t$. Conclude $1\le D\le100$ outside the listed channels.
The technical appendix is part of the PDF, not an external reference.

### §5. A complete and terminating finite certificate

Print the complete seed formulas and the exit-or-first-return algorithm.
Prove coverage, exact integer parameter recovery, finite-state
termination and injectivity-based first-repeat property. Explain both
the author forward/positive-extremum implementation and the independent
inverse/two-sign interval implementation. Explicitly retain zero
coefficients in the interval bounds.

Print the complete seed partitions, symbolic-family counts and the two
sporadic terminal words. Explain full directed-state-set comparison,
not just matching hashes or totals. Observed step lengths and forcing
range are outputs, never search limits. Include native reconstruction
and reversal-pair checks. Place the full primary source listing and
complete independent pseudocode in Appendix B; archive identifiers
and data schema go in Appendix C. No “Experiments” heading or artificial
timing benchmark is needed.

### §6. Primitive clocks and arithmetic of invariant levels

Prove that least scalar word length equals least triple-map period.
Give every degeneracy/identification: alternating equality; $t=-2$ for
the three-cycle; $2t=a+1$ for the four-cycle; sole five-cycle duplication
$t=0,-1$; the six/eight parameter rotations; all proper divisors of
twelve including $m=1$; and the two self-reversing sporadic words.

Derive the invariant levels and all nine exact cycle-count rules below.
Conclude fixed-level finiteness, ordinary fixed counts and the finite
Artin–Mazur product. This consequence is elementary cycle combinatorics,
not an additional classification or arithmetic Euler product.

### §7. Scope and conclusion

Restate the all-forcing exhaustion and evidence boundary concisely.
Distinguish integer from rational points, one map from a whole group,
fixed-level counts from all-level infinitude, and dynamical cycle factors
from target Euler factors or root numbers. Do not append new unproved
classification conjectures or claim a formal Route-A grade. Note that
the finite proof uses exact integer implementations, not proof-assistant
kernel verification.

### Typeset appendices

- Appendix A: every signed $s=0,-2$ branch, explicit scalar iterates and
  numerical inequalities for all integers $D>100$; no omitted case ledger.
- Appendix B: full 139-line primary certifier, complete independent
  mathematical pseudocode, zero-coefficient handling, matching rules and
  the original assertions/no-`-O` convention.
- Appendix C: exact historical input/output identifiers, JSON schema,
  full-data availability and separate symbolic-check scope. The raw
  25,851 records remain machine-readable witnesses, not thousands of
  typeset pages or a replacement for the printed finite algorithm.

## 5. Exact count formulas to carry into §6

Let $c_\ell(a,k)$ denote directed cycles of least native length $\ell$.
All other lengths have zero count.

1. $c_1$ counts distinct $r=1\pm\sqrt{1-a}\in\mathbb Z$ satisfying
   $k=r^2(2r-3)$; deduplicate a double root.
2. For each distinct integer root $P$ of
   $P^2+(a-3)P-k=0$, put $S=P+a$. Count one precisely if
   $S^2-4P=h^2>0$ for an integer $h\equiv S\pmod2$.
3. $c_3=1$ precisely for even $a$, $t=(a+4)/2\ne-2$ and
   $k=8-(t-4)^2$.
4. $c_4=1$ precisely when $(a+1)(a-7)+4k=h^2>0$ with
   integer $h\equiv a+1\pmod2$.
5. For $a=-1$, $c_5=1$ at $k=0$, and $c_5=2$ at positive $k$
   with $4k+1$ square; otherwise that family contributes zero. Add one
   at $(a,k)=(-13,-64)$.
6. $c_6=1$ precisely when $a=0$ and $k$ is a positive integer square.
7. $c_8=1$ precisely when $a=-1$ and $k-1$ is a positive integer square.
8. $c_9=1$ precisely at $(a,k)=(-2,-1)$.
9. $c_{12}=1$ precisely when $a=0$ and $4k-7$ is a positive integer
   square. Its root is odd and $m=(1+\sqrt{4k-7})/2\ge1$.

Every omitted case in items 3–9 has count zero. The formulas imply
$$
\#\operatorname{Fix}(T_a^n\mid K_a=k,\mathbb Z^3)
=\sum_{\ell\mid n}\ell c_\ell(a,k),\qquad
\zeta_{a,k}(\tau)=\prod_\ell(1-\tau^\ell)^{-c_\ell(a,k)}.
$$
Use $k$ only for the invariant level, $\kappa$ for the positive
auxiliary integer at center $-1$, and $\tau$ for the formal zeta
variable. This removes the source proof's local symbol overload.

## 6. Figures and tables

The full classification and count rules are the primary visuals. A
compact monochrome proof-flow schematic may serve as Figure 1 if it
improves the first-page reading; it is not mandatory decoration.

| Item | Exact content and purpose | Evidence source |
| --- | --- | --- |
| Classification table/word panel | All ten rows, guards, levels and native periods; long words split across aligned lines | Accepted classification, not newly sampled values |
| Large-amplitude branch table | Five centers, signed subcases, terminal family or precise contradiction | Full analytic proof and Appendix A |
| Finite-certificate table | Forward one-sign and inverse two-sign seed/return/exit partitions | Both preserved summaries |
| Finite family-partition table | Counts $(200,25350,99,100,50,50,2)$, expressly finite-core only | Both preserved summaries and complete independent comparison |
| Optional Figure 1 | All integer cycles split into $D=0$, explicit large-amplitude channels, or the proved finite core; all converge to the complete native table | Exact dependency chain, drawn as vector lines/text |

Optional figure caption: “The difference identity removes the additive
forcing from the exhaustion argument. Explicit channels account for
unbounded coordinates or differences; all remaining cycles enter a
proved finite core. Its exact completed certificate leaves only two
sporadic words. The finite core is uniform in forcing, level and period.”
No prior method is depicted as though it used the same quantified
problem. Tables are preferred to empirical-looking scatter plots.

## 7. Citations, review and next gates

[CITATION_PREPARATION.md](CITATION_PREPARATION.md) gives verified fields,
actual body scopes and bounded access failures. Cite Roberts–Baake for
classical unforced families and symmetry, Roberts for unforced escape,
Cantat–Loray for the ambient cubic/group action, Hone for the distinct
product-coefficient recurrence, Humphries for the whole-group quantifier,
and the prior anonymous C413 manuscript for the already-owned unforced
classification. Do not invent a venue or author for C413; its release
location remains an explicit bibliographic transport item.

Current-team fallback replaces the legacy GPT-5.4 MCP reviewer default;
the user/coordinator's standalone format replaces ML venue/page defaults.
The narrative principles shape one technical story, front-loaded claims,
consistent notation and self-contained proof exposition. They do not
authorize an artificial experiment, figure, minimum length or extra claim.

Next authorized steps: read the complete paper-write and paper-compile
skills and their required references; draft the full anonymous source;
build and inspect the first actual PDF while preserving the true baseline
logs/environment. Do not rerun the old accepted mathematical certificate.
Two actual nonauthor full-manuscript reviews and their real revisions
remain future gates; no review verdict or formal evaluation is prefilled.
Git/global integration and final release remain coordinator-owned.
