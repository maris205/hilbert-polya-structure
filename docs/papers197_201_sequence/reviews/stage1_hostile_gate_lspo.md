# Stage-1 hostile gate: least-source path orientations (`LSPO`)

**Audit date:** 2026-09-05 UTC  
**Reviewer role:** process-separated from the LSPO scout; no scout code was
imported into the independent control  
**Scope:** queue normal form, exact clock and depth polynomial, every-time
labelled fibres, one-step fibre histogram, and the P145/P90/P100 firewall  
**External status:** `HOLD_EXTERNAL`  
**Novelty or priority conclusion:** none

## Outcome first

The mathematical contract survives rederivation: equations (1)--(10) are
correct, including all boundary cases tested below.  That correctness does
not make LSPO eligible for a new paper number.  The exact literal candidate
was already recorded and rejected in the P147--P151 combinatorial scout:

> On a path orientation, repeatedly pushing the least source has a sharp
> quadratic tail and product basins, but it is the same vertex-push literal
> operation as P145 with a new scheduler.

That record says explicitly that the candidate was aborted before promotion.
It is not a vague proof-engine resemblance: it names the same carrier and the
same least-source repeated update.  The accompanying historical anchor also
forbids reviving a P1--P146 mechanism by a scheduler change.  A stronger
inverse atlas is valuable mathematical analysis of the old killed candidate,
but cannot silently make its literal map new.

```text
MATHEMATICAL_CORRECTNESS: PASS
BLOCKING_PORTFOLIO_FINDINGS: 1
VERDICT: KILL_EXACT_INTERNAL_HISTORY
OWNER_STATUS: OWNER_RED_AMBER
EXTERNAL_STATUS: HOLD_EXTERNAL
```

This is a selection kill, not a claim that the displayed theorems are false.

## Frozen audit surface

The following inputs were read without modification.  Paths and hashes are
workspace-root-relative.

```text
d9658d47d79cda762132c3efd5d0a46e6d7ad484a01a688ea69a52670fb8f7bc  docs/papers197_201_sequence/scouting/root_least_source_path/THEOREM_CONTRACT.md
834f00ee29f91b3fbd42acd18ce209a64d8e5ea1d83dab1cc9c14296b94b273f  docs/papers197_201_sequence/scouting/root_least_source_path/COLLISION_FIREWALL.md
b0f18c5d011020fa5df15fade57e7cbb9b83974d64e052a8a9441b853473ad8e  docs/papers197_201_sequence/scouting/root_least_source_path/verify_scout.py
d7050a3e25eaadbfba36a1a76ed65f75785431b1ce813a958c6ddc2a3be2315e  docs/papers197_201_sequence/scouting/root_least_source_path/CANONICAL.txt
e7f22c3e9dedbd0c569864a7d2098caad201ee9ed327eb2f48e050aac8f47ea2  docs/papers147_151_sequence/PROBLEM_ANCHOR.md
371c740e6c2ab99db9aa2f3c429b0b32a4a4af94bd5b11255eba892c379d2cd3  docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md
31817113f6c06621f4157a227f3af4dc046a3601292cb0a4e008a2786f859107  docs/papers142_146_sequence/phase1/FINAL_THEOREM_CONTRACTS.md
12186ef6c2625409111d527e114f8131c6bc04ead3a1a29530d8aea85f7202ce  docs/papers142_146_sequence/phase1/SYSTEM_COLLISION_FIREWALL.md
74adef800c0f6ff315746cc0bb8e74d975359653f488c998e822746933445f90  papers/90-rule184-particle-periodic-zeta/main.tex
b1bc16c0ff98e89b64f7d8517cdd76a77dfd99807acd6baf99a28c428a8e6b7d  papers/100-least-valuation-digit-erasure/main.tex
```

The P147--P151 scout hit is at lines 627--630 of its frozen file.  The
binding no-revival rule is at lines 43--47 of its problem anchor.  These
locators are given so that the collision can be checked without relying on
the present review's paraphrase.

## 1. Independent literal reduction and queue normal form

Use signs `epsilon_i in {-1,+1}` for the edge `i--(i+1)`, with `+1`
meaning `i -> i+1`.  Vertex `v` is a source precisely when its left incident
edge, if present, points left and its right incident edge, if present, points
right.  If `A={i:epsilon_i=+1}`, this gives three exhaustive cases.

1. If `A` is empty, the only source is the right endpoint, so its click
   changes `A` to `{m}`.
2. If `p=min A=1`, the left endpoint is the least source, so its click deletes
   site `1`.
3. If `p=min A>1`, all sites below `p` point left.  The least source is vertex
   `p`; clicking it replaces the occupied site `p` by `p-1`.

This independently recovers (1).  It also shows why the dynamics is a serial
queue, rather than a parallel traffic rule.

Let `A={a_1<...<a_k}`.  Until it disappears, the first particle moves

```text
a_1, a_1-1, ..., 1
```

one site per step, while every later particle remains unchanged.  Its final
click occurs after exactly `a_1` steps.  Induction after deleting that
particle proves that particle `a_j` is active on the half-open time interval

```text
[S_(j-1),S_j),       S_j=a_1+...+a_j,
```

and is then at `a_j-(t-S_(j-1))`.  This is exactly (6).  Only the original
rightmost particle is left at time

```text
tau(A)=a_1+...+a_(k-1).
```

No earlier state is recurrent because it still has at least two particles;
each subsequent step continues to reduce this nonnegative clock by one.
Once at a singleton, the literal rule gives

```text
empty -> {m} -> {m-1} -> ... -> {1} -> empty,
```

so the `n` displayed states are one cycle and are the complete recurrent
set.  This proves the exact entrance claim, not merely an upper bound.

The largest possible clock is obtained by taking rightmost site `m` and all
sites below it:

```text
1+2+...+(m-1)=m(m-1)/2=binom(n-1,2).
```

For `m>=2` every omission makes the sum smaller, so `[m]` is the unique
maximizer.  For `m=0,1`, every state is already on the core and the maximum is
zero.

## 2. Exact depth polynomial

Partition all nonempty states by their rightmost site `r`.  The remaining
particles form an arbitrary subset `R subseteq [r-1]`, and the queue proof
gives depth `sum R`.  Hence their depth enumerator is

```text
product_(i=1)^(r-1) (1+u^i).
```

The empty core state contributes the additional `1`.  Summing over
`1<=r<=m` proves

```text
H_m(u)=1+sum_(r=1)^m product_(i=1)^(r-1)(1+u^i).
```

Its constant coefficient is `m+1=n`, exactly the recurrent population, and
its degree and leading coefficient are respectively `binom(m,2)` and one.
Thus (7), the core census, and the sharp unique tail witness agree at both
ends.

## 3. Every-time labelled fibres

### 3.1 Transient targets

Fix a target `B={b_1<b_2<...<b_l}` with `l>=2`.  Any source reaching `B`
at time `t` is still transient.  At that time its active particle must have
started at

```text
b_1+r,       0<=r<b_2-b_1,
```

and moved `r` steps.  All already consumed particles form a unique strict
subset

```text
R subseteq [b_1+r-1]
```

whose labels contribute the remaining time `sum R=t-r`.  Particles
`b_2,...,b_l` have not moved.  Conversely every such `(r,R)` reconstructs a
unique source and its whole queue history.  Therefore

```text
|Phi^(-t)(B)|
  = sum_(r=0)^(b_2-b_1-1) [u^(t-r)] product_(i=1)^(b_1+r-1)(1+u^i),
```

which is (8), including `t=0` and all zero-fibre cases.

### 3.2 Core targets

Write `c_0=empty` and `c_s={s}`.  There is exactly one core ancestor of
`c_s` at every time.  A transient source with rightmost particle `r` has a
nonempty consumed subset `R subseteq [r-1]`, entrance time `e=sum R>=1`,
and enters at `c_r`.  After the remaining `t-e` core steps it is at

```text
c_(r-(t-e) mod n).
```

Consequently it reaches `c_s` if and only if

```text
s == r+e-t (mod n).
```

There are `q_(r-1)(e)` choices for `R`.  Requiring `e<=t`, adding the unique
core ancestor, and summing over `r` proves (9).  This derivation also explains
why no transient term with `e=0` should be present and why the leading `1`
must remain for arbitrarily large `t`.

## 4. One-step fibre histogram

The predecessor classification can be made target-local.  For a target
`B`:

- if `1 notin B`, then `B union {1}` is always a predecessor via boundary
  deletion;
- if `q=min B<m` and `q+1 notin B`, then replacing `q` by `q+1` supplies
  the unique move-left predecessor;
- for `B={m}`, the empty state replaces that second predecessor;
- there are no other possibilities.

It follows immediately that a target is a nonimage exactly when it contains
both sites `1` and `2`.  There are `2^(m-2)` such targets.  The two-preimage
targets consist of `{m}` and, for each `2<=q<m`, the targets with minimum
`q` and missing `q+1`; their number is

```text
1+sum_(q=2)^(m-1) 2^(m-q-1)=2^(m-2).
```

All remaining `2^(m-1)` targets have one predecessor.  This proves (10),
the image size `3*2^(m-2)`, and maximum indegree two.  At `m=1` the two
states form a two-cycle, so both fibres have size one.

## 5. Independent computational pressure

The scout verifier itself was launched in two fresh processes.  Both runs
were byte-identical, reported `1,363,910` assertions, and had stdout SHA-256

```text
d7050a3e25eaadbfba36a1a76ed65f75785431b1ce813a958c6ddc2a3be2315e
```

A separate in-memory verifier used edge-sign tuples, located the least source
directly from incoming arrows, and enumerated strict subsets directly; it did
not import or call any function from `verify_scout.py`.  It checked:

- literal orientation clicks against the queue update for every state through
  `n=13`;
- the whole pointwise queue normal form and no-early-entry condition;
- the recurrent cycle, exact depth polynomial, maximum and equality count;
- the complete one-step indegree histogram and nonimage classification;
- (8) and (9) against direct powers for every target and every
  `0<=t<=binom(n-1,2)+3n` through `n=10`;
- total fibre mass at every checked time.

It completed `484,681` independent checks.  Its terminal row summary was

```text
n=9   states=256   image=192   max_tail=28  max_fibre=2
n=10  states=512   image=384   max_tail=36  max_fibre=2
n=11  states=1024  image=768   max_tail=45  max_fibre=2
n=12  states=2048  image=1536  max_tail=55  max_fibre=2
n=13  states=4096  image=3072  max_tail=66  max_fibre=2
```

The SHA-256 of the complete row serialization for `n=1,...,13` was
`fa6a7e3476bf19580451f392f587c7ff26346a3d2cdaf8c620e45d4d3f402721`.
These finite checks are falsification pressure only; the deductions in
Sections 1--4 supply the all-parameter proofs.

## 6. Collision audit

### P145: close mechanism, and the route to the fatal history hit

For a connected tree, vertex pushes span the full cut space, whose dimension
is `n-1`; hence the P145 push orbit on `P_n` is all `2^(n-1)` path
orientations.  Both systems reverse every edge incident with the selected
vertex.  P145 samples a labelled vertex uniformly, whether or not it is a
source; LSPO deterministically selects the least current source.  Thus LSPO
is not the same transition kernel as P145, and P145's folded-hypercube
spectrum does not prove (2) or (8)--(9).

That distinction is mathematically real but insufficient for portfolio
admission.  The historical P147--P151 scout already applied the scheduler
rule to this exact proposed specialization and explicitly aborted it.  The
current firewall's comparison only to the numbered P145 paper misses this
more specific internal record.

### P90: terminology/proof-surface adjacency only

P90 Rule 184 is a simultaneous radius-one update on a cyclic binary word and
preserves particle number.  LSPO is an open serial queue: one globally
selected particle moves, particles disappear at the left boundary, and an
injection occurs only at the empty state.  Their recurrent sets also differ
structurally: P90 has density-dependent translating subshifts, whereas LSPO
has one `n`-cycle.  There is no literal equality or simple conjugacy in the
audited material.  Exclusion/traffic language and generic particle tracking
must nevertheless receive zero credit.

### P100: an additive-clock analogy, not a transfer

P100 repeatedly subtracts one unit from the least nonzero base-`p` digit,
has a fixed absorber, and uses digit sum as its clock.  LSPO instead decrements
the location of the active least particle, deletes it at the boundary, and
retains the rightmost particle as a rotating core phase.  Strict-subset
positions, rather than independent digit multiplicities, produce (7)--(9).
Thus P100 supplies a warning that a least-object additive clock is not itself
new, but it does not transfer the LSPO inverse atlas.

### Binding exact-history finding

The decisive record is not any loose analogy above.  It is this exact entry:

```text
docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md:627-630
```

It identifies the same path-orientation carrier, repeated least-source push,
quadratic tail, and product basins, and records `aborted before promotion`.
The associated anchor states:

```text
Do not revive any P1--P146 mechanism by ... scheduler change ...
```

The present candidate therefore fails the current literal-map/history gate
even though the every-time atlas goes beyond the older one-line diagnosis.

## 7. Findings and disposition

| ID | severity | finding | consequence |
|---|---|---|---|
| `LSPO-B-01` | blocking portfolio collision | The firewall omits the exact P147--P151 historical LSPO entry and treats P145 merely as a neighbouring random system. | A previously killed literal candidate would be counted again; **kill before numbering**. |
| `LSPO-B-02` | minor documentation | The literal-system paragraph begins with `n>=2`, while the clock and verifier also state an `n=1` convention. | If retained in the kill ledger, say explicitly that `n=1` is the edgeless identity extension. |

No critical or major mathematical error was found in (1)--(10).  In
particular, there is no orientation error in (1), no missing `e=0` term in
(9), and no exceptional failure of the one-step histogram at `m=2`.

Final disposition:

```text
KILL_EXACT_INTERNAL_HISTORY
math_critical=0
math_major=0
math_minor=1
portfolio_blocking=1
paper_number_authorized=NO
novelty_claim_authorized=NO
external_release=HOLD_EXTERNAL
```

The useful outcome is a strengthened theorem dossier for an already killed
system.  It may be preserved as negative/scouting evidence, but it must not
be promoted as one of P197--P201 without an explicit central override of the
literal-repeat rule; no such override is present in the audited inputs.
