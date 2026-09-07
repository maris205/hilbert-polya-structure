# Full-image threshold test and triangular renewal enumeration

## Claim

For the map $F$ that replaces each maximal weakly increasing run of a
positive integer composition by its sum, the following statements hold.

1. For a target composition $s=(s_1,\ldots,s_m)$, start with $r_m=1$.
   For $i=m-1,\ldots,1$, reject if $s_i\le r_{i+1}$; otherwise set

   $$r_i=\begin{cases}
   s_i,&s_i=r_{i+1}+1,\\
   1,&s_i\ge r_{i+1}+2.
   \end{cases}$$

   The target is in the image of $F$ exactly when this scan never rejects.
2. Let $i_n$ be the number of distinct image compositions of total $n$.
   With $\Theta(z)=\sum_{k\ge1}z^{k(k+1)/2}$, the formal generating
   function is

   $$\sum_{n\ge1}i_nz^n=\frac{\Theta(z)}{1-\Theta(z)}.$$

## Status

PROVABLE AS STATED. The statements concern the full image, not the
number of preimages of an individual target and not the maximum fibre.
This proof note does not assert source novelty or candidate admission.

## Assumptions

- The carrier at total $n\ge1$ is all ordered compositions into positive
  integer parts.
- Runs are maximal weakly increasing runs under simultaneous old-state
  comparisons. A strict descent separates two output parts.
- No cyclic boundary or external schedule is present.

## Notation

A refinement of a positive integer $s$ is a nonempty sequence of positive
parts summing to $s$. A run refinement is weakly increasing. For a
realizable target suffix, its minimum-first value is the smallest first
part among all source refinements realizing that suffix. Every such set
is finite and nonempty, so this minimum is attained.

All generating functions below are formal power series. The symbol
$Q_r(z)$ counts target prefixes that may be prepended to a realizable
suffix whose minimum-first value is $r$; it includes the empty prefix.
It counts target part lists, not their possible source refinements.

## Proof strategy

First minimize the initial part of a run refinement subject to a strict
descent into the next run. The exact minimum is a sufficient state for
all further prepends. Then count accepted target lists through the
deterministic state transitions, decomposing each path at its first reset.

## Dependency map

1. The run-refinement characterization of a preimage gives the boundary
   inequality between consecutive runs.
2. A constrained run-minimum lemma gives the exact scan.
3. The scan gives a deterministic weighted transition system.
4. First-reset decomposition gives a renewal identity and the series.

## Proof

### Step 1. Exact run refinements

Every source for $s$ has one weakly increasing run refinement $u_i$ of
each $s_i$, with

$$\operatorname{last}(u_i)>\operatorname{first}(u_{i+1})
\quad(1\le i<m).$$

Conversely concatenating such refinements produces exactly those maximal
runs, because the internal comparisons are weak increases and the listed
external comparisons are strict descents. Its image is therefore $s$.
This characterization neither counts an arbitrary cut as a valid run
boundary nor permits a run to cross two target parts.

### Step 2. Constrained minimum

Fix a positive threshold $r$. A weakly increasing refinement of mass
$s$ whose last part exceeds $r$ exists exactly when $s\ge r+1$.
Necessity follows because its last part is at most $s$. If $s=r+1$,
its last part is at least $r+1=s$, so positivity forces the singleton
refinement $(s)$; the minimum first part is $s$.
If $s\ge r+2$, the refinement $(1,s-1)$ is weakly increasing and
has last part $s-1>r$. Its first part is the smallest positive integer.
Thus the minimum first part is $1$.

### Step 3. The greedy image criterion

For a one-part target $(s_m)$, the all-ones source refinement shows
that its minimum-first value is $1$. Assume a suffix beginning at
$i+1$ is realizable and has minimum-first value $r$.
Every realization of that suffix starts with a part at least $r$;
therefore any run prepended before it must have last part exceeding
$r$. Conversely a suffix realization attaining $r$ can be chosen,
and any run with last part exceeding $r$ can be joined to it.
Consequently Step 2 applies exactly, not just as a necessary condition.
It either rejects the extended suffix or computes its attained
minimum-first value. Induction proves the scan and both directions of
the first claim. The one-part and mass-one targets are included.

### Step 4. Weighted deterministic transitions

In scan state $r$, a prepended target part of size $r+1$ changes the
state to $r+1$; any size $s\ge r+2$ resets it to $1$. No smaller
size is permitted. Hence

$$Q_r(z)=1+z^{r+1}Q_{r+1}(z)
+\frac{z^{r+2}}{1-z}Q_1(z).$$

This counts each accepted target prefix once: reading its sizes from
right to left determines a unique transition path. The alternative
source refinements used in Step 3 are not counted. Every transition has
positive weight degree, so each fixed-degree coefficient depends on
only finitely many path lengths; the decomposition is valid for formal
series without any convergence assumption.

### Step 5. First-reset decomposition

Starting at state $1$, exactly $j\ge0$ consecutive nonreset transitions
have sizes $2,3,\ldots,j+1$ and total weight degree
$j(j+3)/2$. A path can terminate at that point. Alternatively its first
reset uses any size at least $j+3$, after which any path counted by
$Q_1$ can follow. Therefore

$$Q_1=A+BQ_1,$$

where

$$A=\sum_{j\ge0}z^{j(j+3)/2}=\frac{\Theta(z)}z,
\qquad
B=\frac1{1-z}\sum_{j\ge0}z^{(j+2)(j+3)/2}
=\frac{\Theta(z)-z}{1-z}.$$

The notation $\Theta/z$ is a formal power series because $\Theta$
has no constant term and starts with $z$. Since $B(0)=0$, the series
$1-B$ is invertible, and

$$Q_1=\frac{(1-z)\Theta(z)}{z(1-\Theta(z))}.$$

The rightmost target part is any positive integer, contributing
$z/(1-z)$, and its state is always $1$. Appending its independently
chosen admissible prefix gives

$$\sum_{n\ge1}i_nz^n=\frac z{1-z}Q_1(z)
=\frac{\Theta(z)}{1-\Theta(z)}.$$

This proves the second claim. In particular, with the auxiliary empty
count $i_0=1$, coefficient extraction yields

$$i_n=\sum_{\substack{k\ge1\\k(k+1)/2\le n}}
i_{n-k(k+1)/2}\quad(n\ge1).\qquad\square$$

## Corrections or missing assumptions

The rightmost target part has no outgoing descent condition; imposing
one would give an incorrect initial state or extra weight. The auxiliary
coefficient $i_0=1$ is only the empty-series convention, not an additional
positive-mass state. This note proves equinumerosity with compositions
into positive triangular parts through formal series, not an explicit
bijection to that known counting class.

## Authorship and evidence boundary

The lane40 scout first supplied the exact minimum-first image recursion.
Root derived and first shared the closed triangular renewal series from
that recursion on 2026-09-07 UTC and wrote this proof. The scout reports
having independently begun a threshold-reset derivation before that
message; that chronology is retained without treating the two processes
as independent candidate reviewers. Both are mathematical contributors.

No scientific code was run for this note. The scout subsequently reported
one already completed, precontracted total-mass $1$ through $12$ pilot;
its reported image counts agree with the series. Root has not yet
inspected that pilot's full original package here, so those reported
finite values are not used as proof or certified root replay evidence.

## Open risks

Triangular-part compositions and the renewal-series identity are a known
generic enumeration class, not themselves a claimed new object. The
substantive proposed connection is the exact full image of this literal
run-sum map. Its direct-source and historical-adapter checks, residual
value gate and any later manuscript review remain open. No maximum-fibre
claim, paper number or global novelty clearance is granted.
OWNER_AMBER / HOLD_EXTERNAL.
