# Hostile Review — P88

Audit date: 2026-08-28 UTC.

Reviewer posture: two independent hostile passes, with every theorem read
against its exact quantifiers, every ownership sentence checked against a
primary source, the control program rerun from a clean Python invocation,
and every rendered page inspected after repair.

Disposition: **GO for internal short-paper freeze; EXTERNAL HOLD**.

## Executive finding

The mathematical core survives both rounds. The terminal-level bijection,
three complexity normalizations, compatible uniform law, joint-offspring
factorization, iid-ray law, and exact complete-level coordinate-deletion
threshold all have short proofs independent of the control output.

The original freeze was not release-ready in two respects. First, two
finite-height formulas silently included `h=0` where their notation was
undefined. Second, the phrase “all-or-nothing” did not sufficiently subtract
classical threshold secret sharing, and the stochastic owner ledger omitted
Guyon's earlier joint sibling kernel and the classical tree-reconstruction
line. Those issues are repaired. A non-prime-field `F_4` regression lane and
two assumption-failure controls were also added.

## Round 1 — mathematics, quantifiers, and controls

### Findings and repairs

1. **Double-log formula at `h=0` — MAJOR, FIXED.**  The expression
   `log(C_h)/h` is undefined at `h=0`. Theorem 3.1 now states that the first
   two identities hold for `h >= 0` and the double-log identity for
   `h >= 1`; Table 1 carries the same qualifier.
2. **Block factorization at `h=0` — MAJOR, FIXED.**  Equation (16) used
   `V_(h-1)`, which is undefined at height zero. It is now quantified for
   `h >= 1`, with the root-only `q^(-1)` factor stated separately for
   `h=0`.
3. **Prime-power theorem versus prime-only code — MODERATE, FIXED.**  The
   universal theorem remains proof-based, but the control suite now has an
   independent exhaustive `F_4 = F_2[a]/(a^2+a+1)` lane. It checks the field
   tables and all 256 height-two binary terminal assignments.
4. **Necessity claims only described, not guarded — MODERATE, FIXED.**  The
   script now explicitly detects the `d=1` ray degeneracy and the
   zero-coefficient proper-subset reconstruction leak.
5. **No floating-point dependency — PASS.**  Enumeration, finite-field
   arithmetic, counters, and modular Gaussian elimination are exact.

### Claim–dependency–proof ledger

| Claim | Status | Minimal dependencies | Independent proof check |
|---|---|---|---|
| Terminal restriction is a bijection | PASS | finite field; one nonzero coefficient is enough for downward extension | triangular constraint matrix has full internal-row rank and nullity `d^h` |
| Root coefficient is the path product | PASS | local linear rule | recursive substitution and extension-matrix root row agree |
| Every root fiber has `q^(d^h-1)` blocks | PASS | at least one nonzero root coefficient | a nonzero linear functional has a codimension-one kernel |
| SNRE collapses to `A_(h+1)=q^(d-1)A_h^d` | PASS | all coefficients nonzero; root fibers uniform | one affine child hyperplane times independent rooted subblocks |
| Three complexity rates | PASS after quantifier repair | exact block count and tree volume | direct substitution; double-log lane restricted to `h >= 1` |
| Uniform block laws are compatible | PASS | one local equation of rank one | every restriction fiber has size `q^((d-1)d^h)` |
| Projective law is shift-invariant | PASS | complete global levels are iid uniform | a rooted descendant boundary is an iid subcollection of one global level |
| Joint-offspring factorization | PASS after quantifier repair | uniform root and affine-hyperplane kernel | exponent is `1+(d-1)|V_(h-1)|=d^h` for `h >= 1` |
| Every deterministic ray is iid | PASS | `d >= 2`; all coefficients nonzero | both conditional-kernel proof and independent full-rank ray-form proof |
| Every proper level subset is independent of the root | PASS | every path coefficient nonzero | adjoining the root row raises every proper coordinate-observation rank by one |
| Complete level reconstructs the root | PASS | iterated local equation | pointwise path-product formula |

### Independent stress derivations

**Constraint rank.** Order variables by depth. Each local row has coefficient
one on its parent, and no row at the same or deeper level uses that parent as
a child. Backward depth elimination gives full row rank
`|V_(h-1)|`, hence nullity `|V_h|-|V_(h-1)|=d^h`.

**Ray rank.** For each ray depth `r<h`, choose a terminal vertex that follows
the ray through depth `r` and then takes a different child. Its coordinate
appears in ray forms through depth `r` and in none of the later forms.
Successive elimination gives rank `h+1`; a full-rank linear image of uniform
leaf data is uniform on `F_q^(h+1)`.

**Proper-subset threshold.** The root row has a nonzero entry in every leaf
coordinate. If a coordinate is omitted, the root row is outside the span of
the observed coordinate rows. The joint observation `(Z_A,R)` therefore has
rank `|A|+1`, proving the uniform joint table and zero mutual information.

### Reproduced control result

The final run reports:

```text
enumerated_blocks=8315
exhaustive_proper_subsets=811
rank_constraint_rows=78
rank_subset_certificates=567
assertions=19764
ALL EXACT CONTROLS PASSED
```

Round 1 verdict: **PASS after four bounded repairs**.

## Round 2 — ownership, overstatement, internal collision, and layout

### Primary-source owner subtraction

The nearest frameworks are now positively assigned as follows.

- Aubrun–Béal: finite-type and sofic tree shifts,
  `10.1016/j.tcs.2012.07.020`.
- Ban–Chang: nonlinear recurrence systems and the double-log tree-shift
  entropy convention, `10.1088/1361-6544/aa72c0`.
- Petersen–Salama: site-normalized tree-shift entropy,
  `10.1016/j.tcs.2018.05.034`.
- Benjamini–Peres: classical tree-indexed Markov-chain framework,
  `10.1214/aop/1176988857`.
- Guyon: binary parent-to-pair kernels with conditionally dependent
  daughters, `10.1214/105051607000000195`.
- Souissi: block Markov chains on trees,
  `10.1007/978-3-031-06170-7_8`.
- Evans–Kenyon–Peres–Schulman: noisy broadcasting and root reconstruction
  on trees, `10.1214/aoap/1019487349`.
- Blakley and Shamir: independently introduced perfect threshold secret
  sharing, `10.1109/AFIPS.1979.98` and `10.1145/359168.359176`.

All nine cited entries resolve to primary publications or their official
DOI records. The manuscript no longer presents the perfect `(n,n)` access
condition, the additive finite-field mechanism, joint sibling kernels, or
tree reconstruction as new. Its residual claim is only the simultaneous
finite-field tree-shift formula package.

### Overstatement repairs

1. The title and section heading now say **coordinate-deletion
   reconstruction**, not the overloaded “all-or-nothing” phrase.
2. The theorem is explicitly about **coordinate subsets of a complete
   noiseless level**. It makes no claim about arbitrary functions,
   compressed observations, noisy observations, or partial linear probes.
3. The secret-sharing paragraph states that the access structure and
   additive mechanism are prior; only their realization at every depth by
   one shift-invariant law is retained.
4. The broadcasting paragraph distinguishes this sibling-coupled,
   finite-depth calculation from independent-edge noisy reconstruction.
5. The bounded search sentence remains a search boundary, not a worldwide
   novelty assertion; public release remains on hold.

### Internal collision audit

A text scan of the `.tex` and `.md` sources in P01–P87 found no prior
finite-field parity-tree, iid-ray/complete-level, or proper-subset/root
theorem package. The two nearest internal objects remain explicitly
firewalled:

- **P49** uses parent–child hom constraints, transient cyclic phase
  allocation, and Hausdorff dimension. P88 uses one star-linear sibling
  equation, finite-block rank, and a probability law.
- **P77** is a one-dimensional countable automatic orbit closure with
  Cantor–Bendixson and endomorphism structure. P88 is an uncountable
  free-semigroup tree SFT with no automatic support.

### Page-by-page hostile layout audit

The first Round 2 render exposed two presentation defects: Table 2 floated
between the two halves of Theorem 5.1, and the wide two-row information
display displaced equation (21). The owner table is now fixed at its source
position and the redundant inline quantifier was removed from the display.
The bibliography is set one size smaller, returning the expanded nine-source
paper to seven balanced pages.

- **Page 1:** three-line title, anonymous author, abstract, keywords, and
  opening ownership paragraphs are clear; no footer collision.
- **Page 2:** residual theorem list, extension-field scope, internal
  firewall, and setup are continuous.
- **Page 3:** boundary theorem, proof, scalar recurrence, and start of the
  normalization ledger are unclipped.
- **Page 4:** Table 1, quantified complexity theorem, compatibility theorem,
  and proof are legible with no table overflow.
- **Page 5:** kernel, local lemma, iid-ray theorem, secret-sharing scope, and
  start of Theorem 5.1 remain in reading order.
- **Page 6:** Theorem 5.1 continues immediately; equations (19)–(21) align
  correctly; owner Table 2 begins only after the theorem and Remark 5.2.
- **Page 7:** owner-scope paragraph, controls, conclusion, and all nine
  references fit without clipping or an orphaned bibliography page.

Round 2 verdict: **PASS after owner and layout repairs**.

## Residual risks

1. The algebra is elementary once the model is stated; venue value depends
   on the synthesis of exact tree-shift complexity, iid rays, and a
   simultaneous complete-level threshold.
2. A bounded literature audit cannot certify absolute priority. Specialist
   review is still required before any public novelty language.
3. Souissi and Guyon supply neighboring stochastic frameworks; the paper
   therefore relies on its displayed factorization rather than on a claim
   that a generic framework theorem is new.
4. No noisy, matrix-valued, nonlinear, inhomogeneous, or arbitrary-observer
   extension is proved.
5. The `F_4` lane strengthens regression coverage but does not replace the
   all-prime-power proof.

## Final decision

**GO for internal freeze. EXTERNAL HOLD remains mandatory.** The theorem
contract is correct after explicit quantifier repair, the code reproduces
exactly, the ownership subtraction is materially stronger, and all seven
pages pass visual inspection.
