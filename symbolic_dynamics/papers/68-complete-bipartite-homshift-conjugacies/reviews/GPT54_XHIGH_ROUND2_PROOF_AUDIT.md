# GPT-5.4 xhigh Round 2 Proof Audit for P68

## Provenance

- Reviewer role: official second-round hostile mathematical reviewer for **Paper P68 only**
- Model: **GPT-5.4**
- Reasoning level: **xhigh**
- Review date: **Tuesday, August 25, 2026**
- Review posture: hostile, theorem-first, source-boundary-aware, no manuscript edits performed
- Frozen package actually read locally before verdict: `main.tex`; all files in `sections/`; `math_commands.tex`; `references.bib`; `PROOF_PACKAGE.md`; `CONTROL_RESULTS.md`; `CLAIMS_EVIDENCE.md`; `ARGUMENT_BLUEPRINT.md`; `FINAL_QA.md`; `DECLARATIONS.md`; `BUILD.md`; `FIGURE_DECISION.md`; `NARRATIVE_REPORT.md`; `PAPER_PLAN.md`; `PAPER_CONFIGURATION.md`; `PAPER_IMPROVEMENT_LOG.md`; `PAPER_IMPROVEMENT_STATE.json`; `CITATION_AUDIT.md`; `SHA256SUMS`; `code/verify_complete_bipartite.py`; `code/verify_complete_bipartite.out`; all existing files in `reviews/`; all existing files in `rounds/`; frozen PDF hashes; and a text preview of `main.pdf`.

## Executive verdict

**Internal mathematical verdict:** **PASS.**

**Round 1 no-change disposition:** **CONFIRMED.**

I do **not** find a hidden proof gap, overclaim, stale mathematical artifact, or contradictory source boundary that forces a manuscript, proof, control, citation, or claims-ledger change in the frozen package. The theorem package remains mathematically closed.

**Release posture:** **EXTERNAL RELEASE HOLD.**

That hold remains source/priority-boundary-driven, not proof-driven.

## Severity-ranked findings

### CRITICAL

None.

### MAJOR

None.

### MINOR requiring manuscript, proof, control, citation, or ledger change

None.

### INFORMATIONAL / artifact-level note

- The package still contains the earlier provisional non-GPT-5.4 Round 2 provenance artifacts (`reviews/ROUND2_PROOF_AUDIT.md`, `rounds/ROUND2_RESOLUTION.md`, `PAPER_IMPROVEMENT_LOG.md`, and `PAPER_IMPROVEMENT_STATE.json`) from the thread-cap-limited cross-agent pass. That is a historical provenance artifact, not a theorem defect and not a source-boundary contradiction. This file is the official GPT-5.4/xhigh Round 2 mathematical record.

## Independent re-tests actually performed

### Packaged control

I reran:

```sh
python3 papers/68-complete-bipartite-homshift-conjugacies/code/verify_complete_bipartite.py
```

Result: `ALL CHECKS PASS`.

### Separate scratch verification, independent of the manuscript prose

I also ran an independent scratch audit that did **not** import the manuscript proof text and directly targeted the failure modes named in the prompt.

1. Exhaustive finite-shape sweep on all `64` subsets of a `3 x 2` window for parameter pairs `(1,1)`, `(1,3)`, `(2,3)`, and `(3,4)`: PASS.
2. Explicit disconnected-shape separation between global extendibility and mere local admissibility:
   - two remote even sites at `(m,n)=(2,3)`: `13` extendible versus `25` locally admissible;
   - remote even/odd pair at `(m,n)=(2,3)`: `12` extendible versus `25` locally admissible.
3. Independent `2D` dimer encode/decode and odd/even translation-equivariance check for `X_{2,6}^{(2)} -> X_{3,4}^{(2)}` on the full `2 x 2` torus family: PASS.
4. Independent `d=1` dimer encode/decode check including the degenerate edge case `X_{1,6}^{(1)} -> X_{2,3}^{(1)}`: PASS.
5. Independent `d=1` fixed-point checks for periods `1,2,3,4,6` and parameter pairs `(1,3)` and `(2,3)`: PASS.
6. Weighted disconnected-shape partition identity on a mixed-parity disconnected shape: PASS.
7. Concrete one-dimer Gibbs optimizer factorization check for a nontrivial one-site potential: PASS.

These computations are regression checks only, not proof premises.

## Theorem-by-theorem rederivation

### 1. Intrinsic checkerboard phase, empty/nonempty finite-shape counts, and entropy

`Z^d` is bipartite by parity
`chi(v)=v_1+...+v_d mod 2`, and `K_{m,n}` is bipartite with parts `A,B`.
Every nearest-neighbour step in the source changes target part, so once the
target part at one site is fixed, the target part at every site is forced by
path parity. Hence every configuration has exactly one of two global phases:

- `E -> A`, `O -> B`;
- `E -> B`, `O -> A`.

This immediately gives the translation rule
`omega(sigma^u x)=(-1)^{chi(u)} omega(x)`.

For a finite shape `F`:

- if `F=empty`, there is exactly one restriction;
- if `F` is nonempty, the two global phases induce two disjoint restriction classes, because at any chosen site they demand membership in opposite target parts.

Therefore the globally extendible count is

```text
N(F)=m^|F cap E| n^|F cap O| + n^|F cap E| m^|F cap O|
```

for every nonempty finite `F`.

I explicitly rechecked the cases the prompt singled out:

- disconnected shapes;
- shapes contained entirely in one parity class;
- arbitrary parity imbalance;
- the empty shape versus the nonempty formula.

No component-wise phase freedom survives. The current manuscript is using the
correct global restriction formula, not the false old induced-subgraph count.

Entropy then follows on rectangular Følner boxes because the parity-class size
difference is `O(1)`, so the normalized logarithm tends to
`(1/2) log(mn)`.

### 2. Full-shift model of one phase

Inside `X^+`, the map

```text
Theta_+(x)_v = (x_v, x_{v+e_1}),   v in E
```

is correct because the dimers `(v,v+e_1)` with `v in E` are pairwise disjoint
and cover the entire lattice. Conversely, any labelling of `E` by `A x B`
unpacks independently on those dimers and yields a valid point because every
lattice edge joins opposite parities and every `A-B` pair is an edge in the
complete bipartite target. This is the exact structural reduction used in the
pressure proof.

### 3. Product classification and the radius-one dimer code

Assume `mn=rs` and fix a bijection `f:A x B -> A' x B'`.

The current rule is the correct two-sided, translation-equivariant one:

- if `x_v in A`, anchor the dimer `(v,v+e_1)`, apply `f(x_v,x_{v+e_1})`, and
  place its `A'` coordinate at `v`;
- if `x_v in B`, use the same anchored dimer at `v-e_1` and place the
  corresponding `B'` coordinate at `v`.

This does **not** freeze an absolute checkerboard origin. The neighbour
selection is made from visible symbol membership in `A` versus `B`, so odd
translations carry anchors to anchors.

I independently rechecked the exact stress points:

- both global phases;
- odd translations;
- the inverse on the same dimers via `f^{-1}`;
- `d=1`;
- degenerate part-size edges `m=1` or `n=1`.

The map is genuinely radius one: at site `v` it uses `v` together with one of
`v-e_1` or `v+e_1`, so its memory set is contained in `{-e_1,0,e_1}`. The
inverse has the same locality. No hidden one-sided dependence appears.

Necessity is also exact: entropy is a conjugacy invariant, and the corrected
finite-shape formula gives `h_top=(1/2)log(mn)`, forcing `mn=rs`.

So the manuscript’s stated criterion

```text
X_{m,n}^{(d)} ~= X_{r,s}^{(d)}  iff  mn=rs
```

is correct for every `d>=1`, including the `m=1` or `n=1` edge cases.

### 4. Finite-dependence subgroup dichotomy

Let `mu` be a finitely dependent probability carried by `X_{m,n}^{(d)}` and
set `I_v = 1_{x_v in A}`.

For every even vector `u`, the phase lemma gives `I_u=I_0` pointwise on the
support. Choosing an even `u` beyond the dependence range makes `I_0` and
`I_u` independent, hence

```text
p = P(I_0=1) = P(I_0=1, I_u=1) = p^2.
```

Therefore `p in {0,1}` and the phase is deterministic.

From that:

- the support lies in one clopen phase component, so no finitely dependent law
  has topological support equal to all of `X`;
- if `L` contains an odd vector, `L`-invariance is impossible because odd
  translations swap the two phase components;
- if `L<=E`, parity-wise iid colours on one chosen phase give a `0`-dependent
  `L`-invariant law with full support on that component.

I find the subgroup theorem exact as stated.

### 5. One-site pressure and uniqueness of the full-action equilibrium state

Replacing the alphabet sizes `m,n` in the corrected finite-shape count by the
weighted sums

```text
Z_A = sum_{a in A} e^{phi(a)},   Z_B = sum_{b in B} e^{phi(b)}
```

gives the finite-volume weighted count

```text
Z_A^|F cap E| Z_B^|F cap O| + Z_B^|F cap E| Z_A^|F cap O|
```

for every nonempty finite `F`. On rectangular Følner boxes this yields

```text
P = (1/2)(log Z_A + log Z_B).
```

For uniqueness, conditioning on one phase and using the dimer model turns the
problem into the full shift on alphabet `A x B` under the even subgroup, with
dimer potential `psi(a,b)=phi(a)+phi(b)`. The correct equality chain is:

1. for a one-dimer marginal `p` on `A x B`,
   `H(p) + E_p psi <= H(p_A)+H(p_B)+E_{p_A} phi + E_{p_B} phi`;
2. equality in that first step forces independence within a dimer;
3. the two finite-alphabet Gibbs equalities force `p_A=q_A` and `p_B=q_B`;
4. entropy rate for an invariant process on the dimer full shift is at most
   the entropy of its one-dimer marginal, with equality only for iid dimers.

Hence the unique equilibrium on one phase component is the dimer Bernoulli law
with one-dimer marginal `q_A x q_B`.

For the full `Z^d` action, odd translations exchange the two phases, so any
full-action invariant law must place weight `1/2` on each phase. The finite
phase mixture contributes zero entropy density, and entropy/potential scale
correctly under the index-two even subgroup. Therefore the displayed equal
mixture of the two parity-wise Gibbs products is the **unique** full-action
equilibrium state.

I find no missing equality case and no hidden dependence on an unproved
component-wise phase choice.

### 6. Finite-index subgroup fixed points

If a finite-index subgroup `L` contains an odd vector, a putative `L`-fixed
point would identify a site with a site in the opposite target part, which is
impossible. Thus `Fix_L(X)=empty`.

If `L<=E` and `q=[E:L]`, then `Z^d/L` has exactly `q` even cosets and `q` odd
cosets. In one phase, each even coset has `m` choices and each odd coset has
`n` choices independently, yielding `(mn)^q` fixed points; the opposite phase
contributes another disjoint copy. Therefore

```text
|Fix_L(X_{m,n}^{(d)})| = 2 (mn)^q.
```

I rechecked the `d=1` case directly on small periods, including odd periods
and the `m=1` edge case. The formula remains correct.

## Source boundary and overclaim recheck

I do **not** find a contradictory source boundary or an ownership overclaim.

1. The public checkerboard-phase / elementary MME picture is consistently
   treated as background and assigned to Chandgotia’s Lecture 4 notes.
2. The Chandgotia-Thorat finite-dependence obstruction is consistently scoped
   to the four-cycle-free setting; the manuscript correctly notes that
   `K_{m,n}` with `m,n>=2` lies outside that hypothesis.
3. The one-sided category is consistently firewalled off and is not used to
   claim a one-sided classification.
4. The package consistently states that the source search is bounded and is
   not a worldwide novelty or priority certificate.

So the present external hold is coherent: it is a bounded-source / specialist
refresh hold, not a disguised proof deficiency.

## Explicit Round 1 disposition recheck

I independently reconstructed the theorem package rather than inheriting the
Round 1 verdict. After doing so, I agree with the official first-round
GPT-5.4/xhigh record and its no-change resolution:

- no manuscript change should have been made between official Round 1 and this
  official Round 2 review;
- no manuscript change is demanded now;
- no hidden theorem defect was missed by the official Round 1 no-change call.

So the Round 1 official **no-source-change disposition is confirmed**.

## Remaining gates

1. Specialist source / priority refresh remains required before any external
   circulation. The current citation audit is explicitly bounded through
   **2026-08-25** and does not certify worldwide novelty or ownership.
2. If the archive wants a single authoritative Round 2 provenance chain, this
   file should be treated as the official GPT-5.4/xhigh Round 2 record; the
   earlier cross-agent Round 2 artifacts remain historical placeholders only.

## Final decision

**Internal mathematical verdict:** PASS.

**Manuscript change demanded by this review:** none.

**Pass/fail status:** PASS.

**EXTERNAL RELEASE HOLD:** maintain.
