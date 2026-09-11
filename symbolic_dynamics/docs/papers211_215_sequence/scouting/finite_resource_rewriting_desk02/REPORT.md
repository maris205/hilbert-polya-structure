# Finite resource rewriting desk 02 — one closed literal

2026-09-09 UTC. Author/proof contributor: /root/round211_rational_scout.
**One literal, zero scientific modules/imports/runs/pilots, zero reserves.**
Disposition: **NO_PROMOTION_PRIMITIVE_AND_UNCLOSED_SHARP_CLOCK**.
This is author scouting, not independent review, admission or a paper.

Parent scope is this directory only, against the accepted 41 closed
attempts plus the separately sealed TTRS boundary. TTRS and the earlier
zero-literal desks are not reopened or amended. Central indexes and
reception belong to root. No Git, external upload or specialist contact.
The project research, idea-creator, research-lit and proof-writer skills
supply source-first subtraction and explicit proof limits. Generic
external-model brainstorming and pilot templates are not run; the current
task specifically permits only bounded deductions and documentary checks.

## 1. Exact literal PFF: parallel Fibonacci fission

Let $F_1=1,F_2=2,F_{i+1}=F_i+F_{i-1}$ for $i\ge2$.
For each fixed integer $N\ge0$, the carrier is
$$X_N=\left\{c=(c_1,c_2,\ldots):
 c_i\in\mathbb Z_{\ge0},\quad\sum_{i\ge1}F_i c_i=N\right\}.$$
Coordinates are denomination multiplicities, not labelled individual coins.
This is finite: if $F_i>N$ then $c_i=0$, and otherwise
$c_i\le\lfloor N/F_i\rfloor$. $X_0$ contains only the zero sequence.

At every denomination, group its **old** $c_i$ copies into
$q_i=\lfloor c_i/2\rfloor$ pairs and retain
$r_i=c_i-2q_i\in\{0,1\}$. Simultaneously replace all these pairs by
$$2F_1\longrightarrow F_2,\qquad
2F_2\longrightarrow F_1+F_3,\qquad
2F_i\longrightarrow F_{i-2}+F_{i+1}\quad(i\ge3). \tag{1}$$
Add the outputs to the retained old singletons. There are no consecutive-
denomination fusion moves, no external scheduler and no choice of pair
labels. This is maximal old-pair firing at each site, not one firing per
site. New arrivals cannot fire until the next time step.

For a finitely supported vector $q$, define the output-incidence operator
$A$ by
$$(Aq)_1=q_2+q_3,\quad (Aq)_2=q_1+q_4,\quad
(Aq)_i=q_{i-1}+q_{i+2}\quad(i\ge3). \tag{2}$$
Then the literal update is
$$T(c)=r+Aq=c-(2I-A)q. \tag{3}$$
Every replacement in (1) preserves Fibonacci value. For $i\ge3$,
$F_{i-2}+F_{i+1}=F_{i-2}+F_i+F_{i-1}=2F_i$.
The two boundary identities are $2=2$ and $4=1+3$.
Nonnegative multiplicities and total value $N$ are therefore preserved,
including the upper-support boundary, without any truncation or cap repair.

One map was instantiated, not three: (1) lists its denomination boundary
cases. Old carry, averaging, cancellation and composition entries seen
during discovery were exclusions, not additional current proposals.

## 2. Claim, status and proof dependencies

**PROVABLE AS STATED:** finite carrier closure; all recurrent states are
fixed, exactly $c_i\in\{0,1\}$; a nonsharp entrance bound $\tau(c)\le4N$;
and the complete, but coupled, predecessor parameterization in (6).

**NOT CURRENTLY JUSTIFIED:** a sharp all-$N$ parallel clock, evaluated
all-target fibre counts or extrema, or a materially independent two-axis
admission contract. The proved results below do not imply any of these.

Assumptions are exactly Section 1, with no restriction to the usual
initial state of $N$ copies of $F_1$, and no claim that the terminal state
must be the Zeckendorf representation. Depth $\tau(c)$ is the first time
at a recurrent state. All sums in this report are finite on each $X_N$.

Dependency map: denomination identities give closure; an explicit positive
linear potential gives termination and the recurrent class; quotient and
remainder reconstruction gives every predecessor. The standard chip-firing
identification then deducts these mechanisms. No census or imported
scientific implementation is a premise.

### 2.1 Full-carrier termination, including all boundary moves

Set
$$w_1=4,\quad w_2=7,\quad w_i=2i+2\ (i\ge3),\qquad
\Phi(c)=\sum_{i\ge1}w_i c_i.$$
The decrease caused by one individual firing at denomination $i$ is
$$\delta_i=
\begin{cases}
2w_1-w_2=1,&i=1,\\
2w_2-w_1-w_3=2,&i=2,\\
2w_3-w_1-w_4=2,&i=3,\\
2w_4-w_2-w_5=1,&i=4,\\
2w_i-w_{i-2}-w_{i+1}=2,&i\ge5.
\end{cases}$$
Linearity and simultaneous old-state evaluation imply exactly
$$\Phi(c)-\Phi(T(c))=\sum_{i\ge1}\delta_i
 \left\lfloor c_i/2\right\rfloor. \tag{4}$$
If every $c_i\le1$, then every $q_i=0$ and $T(c)=c$.
If any $c_i\ge2$, the right side of (4) is positive, so $c$ is not
fixed and cannot lie on any periodic orbit. Since $\Phi$ is a nonnegative
integer, every orbit terminates at a fixed state.

For the bound, $F_i\ge i$: it holds at $i=1,2$, and the recurrence gives
$F_{i+1}\ge i+(i-1)\ge i+1$ for $i\ge2$.
Thus $w_1=4F_1$, $w_2\le4F_2$, and for $i\ge3$,
$w_i=2i+2\le4i\le4F_i$. Hence
$$\Phi(c)\le4N,\qquad \tau(c)\le\Phi(c)\le4N. \tag{5}$$
This is deliberately **not** called sharp. At $N=0$ the only state is
fixed; at $N=1$ the only state is one $F_1$, also fixed.
Every remaining boundary case is already included in (1) and (4).

Fixed states are precisely sums of distinct Fibonacci denominations.
They need not have nonconsecutive indices: at $N=3$, both $c_3=1$
and $c_1=c_2=1$ are fixed and distinct. Thus integer value alone does not
specify a common endpoint, and the full Zeckendorf-game terminal theorem
cannot be substituted for a proof about this fission-only map.

For completeness the number of fixed states is the elementary static
coefficient $[z^N]\prod_{i\ge1}(1+z^{F_i})$. Only factors with $F_i\le N$
affect it. This records distinct-denomination counting, not an additional
dynamical contribution or an evaluated fibre theorem.

### 2.2 Exact all-target inverse parameterization and its limitation

For any target $b\in X_N$, range over nonnegative integer vectors $q$
with
$$0\le q_i\le\left\lfloor\frac{N}{2F_i}\right\rfloor
\quad\text{for all }i,$$
so only finitely many coordinates can be nonzero. Keep precisely those
vectors for which every coordinate of $r=b-Aq$ lies in $\{0,1\}$.
Then
$$T^{-1}(b)=
\left\{2q+b-Aq:
 q\text{ satisfies these bounds and }
 b-Aq\in\{0,1\}^{(\mathbb N)}\right\}. \tag{6}$$

Necessity: take $q_i=\lfloor c_i/2\rfloor$ for an actual predecessor.
Equation (3) gives $r=b-Aq$, and $2F_iq_i\le N$ gives the bounds.

Sufficiency: for a retained $q$, let $r=b-Aq$ and $c=2q+r$.
All entries are nonnegative, and the quotient/remainder of $c_i$ on
division by two are exactly $q_i,r_i$. The identities in (1) yield
$\sum_iF_i(Aq)_i=2\sum_iF_iq_i$, so
$$\sum_iF_ic_i=2\sum_iF_iq_i+\sum_iF_i(b-Aq)_i=N.$$
Thus $c\in X_N$ and (3) returns $b$. If two retained vectors gave the
same $c$, taking its coordinatewise quotients by two would make those
vectors equal. Hence (6) is a bijective parameterization with no
overcount. It also covers $N=0,1$.

However, the admissibility inequalities in (6) still couple the unknown
firing vector through (2). This is the generic quotient/remainder inverse
of a threshold-two redistribution $c\mapsto(c\bmod2)+A\lfloor c/2\rfloor$.
No closed target-local product, sharp extremum or independent evaluated
enumeration is claimed. Calling (6) “complete” refers to its exact set
equality, not to a solved separate research axis. ∎

## 3. Direct primary sources and exact subtraction

[David Eppstein, *Carrying as chip-firing for the Zeckendorf representation*,
12 June 2021](https://11011110.github.io/blog/2021/06/12/carrying-chip-firing.html):
the author body explicitly gives the fission identity, both low-value
exceptions, and a separate fission-without-fusion discussion. It identifies
fission alone with chip-firing. This is a direct author exposition, not a
refereed-paper claim. Only that mechanism identification is used; its
displayed asymptotic observations and later priority algorithm are not
imported as bounds for PFF.

[Cusenza et al., *Bounds on Zeckendorf Games*,
arXiv:2009.09510v1](https://arxiv.org/html/2009.09510v1), Definition 1.1,
lists exactly the three local duplicate-denomination moves in (1), within
a game that also permits consecutive-denomination fusion. The source
starts with $N$ ones and counts individual legal moves, not maximal
parallel steps on every $X_N$. Its Theorems 1.2–1.4 are not transferred.
The HTML header identifies v1, 20 September 2020; the rendered body also
shows “Date: August 24, 2026”. That latter rendering date is not silently
used as a publication/version date.

[Li et al., *Deterministic Zeckendorf Games*, author-hosted manuscript](https://web.williams.edu/Mathematics/sjmiller/public_html/math/papers/zeckgamedeterministic31.pdf):
Definition 1.1 and §1.2 give the same primitive and four serial priorities;
§2 computes summand-count and index-sum potentials. This supports the
subtraction of priority choices and basic potential proofs. It is not the
PFF parallel operator. The retrieved copy has placeholder “MONTH YEAR” /
“VOLUME, NUMBER” footers; no publication date or final venue is inferred
from them. Selected extracted text was read, not a visual PDF review.

The exact adapter for PFF is a directed chip-firing graph: denomination 1
sends one chip to denomination 2 and one to an unrecorded zero-value sink;
denomination 2 sends to 1 and 3; denomination $i\ge3$ sends to $i-2,i+1$.
Every active vertex has threshold two. A PFF step executes precisely the
old $q_i$ firings at each vertex. Such a batch is legal to serialize:
before its $j$th scheduled firing at $i$, at least
$c_i-2(j-1)\ge2$ old chips remain there, and incoming chips cannot hurt
legality. This identifies the local mechanism and batched scheduler;
it does **not** assert an exact published owner of this whole parallel map.

The temporal evidence here is only a bounded integer potential on that
already identified toppling mechanism. The inverse in (6) is its standard
firing-vector reconstruction. Neither supplies the missing sharp/independent
residual. The source-first value/proof gate closes this literal without
a pilot, a larger cutoff or another choice of scheduling designed to save it.

## 4. Actual historical comparison, not a false same-map claim

The ZR section of
docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md
defines synchronous cyclic binary $001\to110$; complementation and spatial
reversal turn it into cyclic $011\to100$. The companion
SOURCE_AND_COLLISION_NOTES.md, ZR section, distinguishes that cyclic map
from linear normalization. These actual old sections were read.

PFF uses arbitrary nonnegative denomination multiplicities at fixed
integer value and performs **duplicate** splitting, not consecutive-bit
fusion on a cyclic word. No equality or conjugacy with ZR is asserted.
The old local-carry owner warning and nonsharp-potential gate remain
relevant, while the directly read fission source is decisive here.

Broader bounded discovery saw existing averaging/gap-sharing, Euclidean,
gcd-current, composition and cancellation controls. They were not reopened,
repaired or counted as fresh candidates. No result from their old pilots
is evidence of a new execution. The prior sealed TTRS result is an explicit
closed boundary supplied by parent, not material re-read for this task.

## 5. Scope, provenance and preserved limitations

The selected local native returns are recorded as documentary evidence,
with their actual commands, exits and tool chunk identities. They contain
combined decoded output; no separate raw stdout/stderr is fabricated.
Browser records preserve actual requests, URLs, selected body ranges and
version limitations without copying whole external works into this packet.

While locating ZR, the author unnecessarily selected mixed old files:
native c0294f returned PROOF_NOTES.md lines 1–160, and native 7be328 returned
SOURCE_AND_COLLISION_NOTES.md lines 1–140. Their opening PR sections also
describe an old pointer rule. This mixed-content exposure was disclosed to
root immediately after recognition; both actual returns are preserved.
No PR theorem is a premise of Sections 1–3 and no PR/pointer work was
advanced. The task's forbidden P211 manuscript/review, finite_pointer and
related root-reception paths were not searched or opened.

This report does not claim that the current author never saw pointer
summaries or that old contributions/failures restore independent-review
eligibility. Unsolicited status/results from the existing root-assigned B
worker were not checked or used here; that worker was asked to send its
future results directly to root. No linked B material was opened.

The first attempt to construct these documents failed during JavaScript
template parsing with "SyntaxError: Unexpected identifier 'docs'", before
any tool in that cell could run. It created or modified no file. The
corrected construction removes the accidental template delimiter; this
documentary authoring failure is not hidden or called a scientific result.

No strict runtime prelock, scientific source, scientific parameter box,
canonical output, replay, manuscript or admission gate exists for PFF.
Documentary hashes and comparisons do not prove the mathematics or novelty.
The remaining sharp-clock and independent-inverse gaps are why this one
attempt is closed, not a claim that every future Fibonacci system is
unresearchable. Root owns reception and any resulting count/index update.

## 6. Documentary key and reading scope

INPUT_PINS.sha256 contains two workspace-relative whole-original hashes,
first established after the reads and draft, not a scientific prelock.
The post-disclosure hash command displayed no body text. Subsequent body
reads were confined to the ZR proof lines 24–81 and source lines 20–33;
no PR section was displayed again. These two returned excerpts are compared
byte-for-byte with the corresponding parts of the original archived tool
returns. A whole-file hash does not mean its entire body was studied.

LOCAL_NATIVE_RECORDS.json has 12 selected original discovery/read/pin
returns, including both mixed-read exposures; it separately preserves the
document-construction parse failure. PRIMARY_SOURCE_RECORDS.json has three
actual browser requests and exact source-use boundaries. The documentary
check result is not a mathematical verifier. MANIFEST.sha256 is directory-
relative and covers every other regular file; no central index is changed.
