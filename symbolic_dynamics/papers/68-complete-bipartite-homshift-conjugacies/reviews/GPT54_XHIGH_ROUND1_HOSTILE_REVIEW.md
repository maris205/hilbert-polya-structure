# GPT-5.4 xhigh Round 1 Hostile Mathematical Review for P68

## Provenance

- Reviewer role: official first-round hostile mathematical reviewer for **Paper P68 only**
- Model: **GPT-5.4**
- Reasoning level: **xhigh**
- Review date: **Tuesday, August 25, 2026**
- Package actually read locally before verdict:
  `main.tex`, all files in `sections/`, `math_commands.tex`,
  `ARGUMENT_BLUEPRINT.md`, `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`,
  `PROOF_PACKAGE.md`, `FINAL_QA.md`, `NARRATIVE_REPORT.md`,
  `PAPER_PLAN.md`, `PAPER_CONFIGURATION.md`, `DECLARATIONS.md`,
  `BUILD.md`, `CITATION_AUDIT.md`, `FIGURE_DECISION.md`,
  `PAPER_IMPROVEMENT_LOG.md`, `BILINGUAL_ABSTRACT.md`, `SHA256SUMS`,
  `code/verify_complete_bipartite.py`, `code/verify_complete_bipartite.out`,
  `references.bib`, all prior files in `reviews/`, and all prior files in
  `rounds/`.
- Review posture: hostile, theorem-first, no manuscript edits performed.

## Scope of this audit

I independently rederived the central contracts the prompt singled out:

1. the intrinsic phase lemma and the exact extendible finite-pattern formula
   for every finite `F`, including the empty shape, disconnected shapes, and
   same-parity shapes;
2. the radius-one dimer code and inverse, and the classification
   `X_{m,n}^{(d)} \cong X_{r,s}^{(d)}` iff `mn=rs`;
3. the finite-dependence phase-rigidity and subgroup dichotomy;
4. the one-site pressure formula and uniqueness of the full-action equilibrium
   state;
5. the finite-index periodic-point counts.

I explicitly stress-tested the failure modes requested in the prompt:
phase double-counting, memory-set/radius wording, empty/nonempty pattern
semantics, `d`-range, and unjustified conditional-independence or
entropy-equality steps.

## Overall verdict

**Verdict:** **INTERNAL MATHEMATICAL PASS.**

I do **not** find a surviving mathematical defect in the frozen package.
The previously repaired disconnected-pattern issue is in fact repaired; the
current manuscript states the correct global-extendibility formula and the
current control script enforces the correct semantics.

**Release status:** **EXTERNAL RELEASE HOLD.**

That hold is now source/priority-boundary driven, not proof-driven.

## Severity-ranked defects

### CRITICAL

None.

### MAJOR

None.

### MINOR requiring manuscript change

None.

### Residual non-proof gate

- The package still makes only a bounded source audit and expressly does not
  claim priority. That is a valid release hold, but it is **not** a
  mathematical defect.

## Theorem-by-theorem rederivation

### 1. Intrinsic phase and exact finite-pattern counts

`K_{m,n}` is bipartite with parts `A,B`, and `Z^d` is bipartite by parity
`chi(v)=sum_i v_i mod 2`. Along every nearest-neighbour step the target part
must flip. Therefore the target part at `v` is forced by the target part at
`0` together with `chi(v)`. Since all lattice paths from `0` to `v` have the
same parity, there are exactly two global possibilities:

- even sites in `A`, odd sites in `B`;
- even sites in `B`, odd sites in `A`.

That proves the phase lemma for every `d>=1`.

For a finite shape `F`:

- if `F=empty`, there is exactly one restriction, namely the empty pattern;
- if `F` is nonempty, the two global phases give two disjoint restriction
  classes, because at any chosen site the two phases require membership in
  opposite target parts and `A,B` are disjoint.

Hence for nonempty `F`,

`N_{m,n}(F)=m^{|F cap E|} n^{|F cap O|} + n^{|F cap E|} m^{|F cap O|}`.

This formula is correct for:

- connected shapes;
- disconnected shapes;
- shapes contained entirely in one parity class;
- shapes with arbitrary parity imbalance.

Extendibility is also correct: once a phase is fixed, all outside sites may be
filled arbitrarily from the phase-prescribed part, and completeness of
`K_{m,n}` makes every adjacent pair valid.

**Double-counting check:** the two phase counts are disjoint for every
nonempty `F`; the empty shape is correctly separated as a special case.

**Entropy check:** on rectangular boxes the two parity counts differ by `O(1)`,
so the normalized logarithm tends to `(1/2) log(mn)`. No hidden dependence on
connected components remains.

### 2. Full-shift model of one phase

Inside `X^+`, the map
`Theta_+(x)_v=(x_v,x_{v+e_1})` for `v in E`
is correct because the dimers `(v,v+e_1)` with `v in E` are disjoint and cover
`Z^d`. Arbitrary labels in `(A x B)^E` unpack to a valid point of `X^+`
because all edges of the source lattice join opposite parities and every
`A-B` pair is an edge in the complete bipartite target.

This gives the exact even-subgroup full-shift model used later in the
pressure proof. I find no hidden compatibility constraint between dimers.

### 3. Product conjugacy classification and the radius-one dimer code

Assume `mn=rs` and fix a bijection `f:A x B -> A' x B'`.

The forward code is:

- if `x_v in A`, the site `v` anchors the dimer `(v,v+e_1)`, apply `f` to
  `(x_v,x_{v+e_1})`, and output the `A'` coordinate at `v`;
- if `x_v in B`, then `v` belongs to the unique anchor at `v-e_1`, and the
  output at `v` is the corresponding `B'` coordinate from the same application
  of `f`.

This is the correct translation-equivariant formulation. It does **not**
freeze an absolute checkerboard origin; the anchor is detected from the symbol
membership in `A` versus `B`.

The dimers partition the lattice because the `A`-sites form exactly one parity
class, in either global phase. The map preserves target-part membership
sitewise, so every nearest-neighbour edge in the output still joins `A'` to
`B'`. Therefore the image lies in `X_{r,s}^{(d)}`.

**Memory/radius check:** the local rule at `v` uses `v` together with exactly
one of `v-e_1` or `v+e_1`, chosen by visible target-part membership. So the
memory set is contained in `{-e_1,0,e_1}` and the radius is genuinely one.

The inverse is the same construction with `f^{-1}`. On each anchored dimer,
the pair of output symbols comes from one application of `f`, and the inverse
reconstructs both coordinates from the same dimer. There is no one-sided leak
or mismatched pairing.

For necessity, topological entropy is a conjugacy invariant and the phase-count
derivation gives `h_top=(1/2)log(mn)`. Thus a conjugacy forces `mn=rs`.

I rechecked the edge cases:

- `d=1`: the construction still works;
- `m=1` or `n=1`: no failure, since the proof needs only nonempty parts and a
  bijection of dimer alphabets when products agree;
- odd translations: equivariance remains valid because the rule is
  symbol-anchored, not parity-origin anchored.

### 4. Finite dependence and subgroup dichotomy

Let `mu` be `k`-dependent and carried by `X_{m,n}^{(d)}`.
Define `I_v = 1_{x_v in A}`.

For every even displacement `u`, the phase lemma gives `I_u = I_0`
pointwise on the support. Choose even `u` beyond the dependence range. Then
`I_0` and `I_u` are independent but equal almost surely, so if
`p = P(I_0=1)` then

`p = P(I_0=1, I_u=1) = p^2`,

hence `p in {0,1}`. So the phase is deterministic.

This part of the argument is sound and does not assume stationarity under the
full action. It uses only:

- the pointwise copied phase bit on even sites;
- finite dependence at sufficiently large separation.

Once the phase is deterministic, the support lies in one clopen phase
component, so no finitely dependent law can have support equal to all of `X`.

For subgroup invariance:

- if `L` contains an odd vector, that vector exchanges the two phase
  components, contradicting deterministic phase for any `L`-invariant law;
- if `L<=E`, parity-wise iid sampling on one fixed phase component gives a
  `0`-dependent `L`-invariant law with full support on that component.

I find the dichotomy exact.

### 5. Pressure and unique full-action equilibrium state

For nonempty finite `F`, the weighted partition sum over globally extendible
patterns is exactly

`Z_A^{|F cap E|} Z_B^{|F cap O|} + Z_B^{|F cap E|} Z_A^{|F cap O|}`.

This is the weighted analogue of the corrected finite-pattern formula, so the
same nonempty/empty and no-double-counting logic applies. On Følner boxes,
parity densities tend to `1/2`, giving

`P = (1/2)(log Z_A + log Z_B)`.

The uniqueness argument also closes correctly.

Condition on one phase, recode by dimers, and obtain the full shift on
alphabet `A x B` under the even subgroup. The dimer potential is
`psi(a,b)=varphi(a)+varphi(b)`. For any one-dimer marginal `p` on `A x B`,

`H(p) + E_p psi <= H(p_A)+H(p_B) + E_{p_A} varphi + E_{p_B} varphi
                  <= log Z_A + log Z_B`.

Equality conditions are correctly separated:

- first inequality: equality iff the dimer coordinates are independent,
  `p = p_A x p_B`;
- second inequality: equality iff `p_A = q_A` and `p_B = q_B`.

Then for an invariant process on the dimer full shift, entropy rate is at most
the entropy of its one-dimer marginal, with equality iff the process is iid
across dimer sites. Therefore the unique equilibrium on one phase component is
the dimer Bernoulli law with marginal `q_A x q_B`.

Finally, a full `Z^d`-invariant law must assign mass `1/2` to each phase
because any odd translation swaps `X^+` and `X^-`. The finite phase mixture
adds zero entropy density, and the odd translate of the component equilibrium
has the same free-energy value. Hence the equal mixture displayed in the
manuscript is the unique full-action equilibrium state.

I do not see an unjustified entropy leap left in this section.

### 6. Finite-index periodic-point counts

Let `L<=Z^d` have finite index.

- If `L` contains an odd vector, then a fixed point would identify a site with
  one in the opposite target part, impossible by the phase rule. So
  `Fix_L(X)=empty`.
- If `L<=E`, then `E/L` has cardinality `q=[E:L]`, and `Z^d/L` splits into
  `q` even cosets and `q` odd cosets. In one phase, each even coset has `m`
  choices and each odd coset has `n` choices, independently; the opposite
  phase contributes another disjoint copy.

Therefore

`|Fix_L(X_{m,n}^{(d)})| = 2 (mn)^q`.

This is correct for every `d>=1`. I explicitly checked the `d=1` case
separately by brute force on small periods; it matches the formula exactly.

## Explicit stress tests performed during this audit

### Packaged deterministic control

I reran:

```sh
python3 papers/68-complete-bipartite-homshift-conjugacies/code/verify_complete_bipartite.py
```

Result: `ALL CHECKS PASS`.

### Additional brute-force checks I ran independently

1. Exhaustive finite-shape count checks on all subsets of a six-point 2D
   window of sizes up to `4`, for parameter pairs `(1,1)`, `(1,3)`, `(2,3)`,
   and `(3,4)`: PASS.
2. Additional weighted disconnected-shape check on a shape containing two even
   sites and one odd site: PASS.
3. Additional `d=1` periodic-count checks for periods `1,2,4,6` and parameter
   pairs `(1,3)` and `(2,3)`: PASS.

These checks are not proof premises, but they do directly target the prompt's
requested failure modes.

## Exact required fixes

None for mathematics.

No manuscript theorem, proof, control semantic, or claims-ledger repair is
required by this review round.

## Remaining source / priority gates

1. The package correctly keeps the public checkerboard phase/MME picture,
   the Chandgotia-Thorat four-cycle-free finite-dependence obstruction, and
   the one-sided category outside its own ownership claim.
2. The source search is explicitly bounded and does not certify worldwide
   novelty or priority.
3. Because of that boundary, the package should remain on hold for external
   circulation until a specialist source/priority refresh is completed.

## Final decision

**Internal mathematical verdict:** PASS.

**Manuscript change demanded by this review:** none.

**EXTERNAL RELEASE HOLD:** maintain.
