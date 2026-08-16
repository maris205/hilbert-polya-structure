# Paper 38 preregistration — SD-C40

## 1. Frozen question and verdict rule

On the full oriented-edge geodesic shift of the original Bass--Serre tree of

```text
BS(1,r)=<u,v | vuv^{-1}=u^r>,  r>=1,
```

test whether the canonical modular cocycle alone can simultaneously provide:

1. a nonempty source-selective primitive ledger;
2. an ordinary same-object Fredholm determinant;
3. a new but internally consistent unit tree-edge marker;
4. primitive/repetition ownership; and
5. failure on balanced, prime/composite, matched GBS, and generic
   presentation controls.

Failure through an empty or generic ledger, a non-trace-class operator, an
inapplicable determinant hypothesis, divergence, or marker incompatibility is
terminal.  It closes the entire affine branch.

## 2. New-object and source lock

This is a new object.  It inherits neither the full Cayley path space nor one
old generator step per marker from Papers 35--37.  The only allowed split is
the presentation-canonical original ascending HNN split over
`<u> = Z`.  The only allowed coefficient is the canonical signed HNN
height/modular cocycle.  Reversing its sign convention is harmless; changing
its content is forbidden.

## 3. Frozen invariant and ownership

The accepted primary object is the literal full-tree primitive geodesic
ledger and an ordinary determinant

```text
det(I-zB)
```

on `ell^2(E^or T_r)`.  Quotient-graph, graph-of-groups, group-conjugacy,
hyperbolic-end, von Neumann, groupoid, or finite-total-weight determinants are
separately typed controls.  None earns same-object Fredholm credit.

Formal diagonal sums are not traces until trace-class ownership is proved.
A positive-height restriction is not a graded cancellation.  Primitive
classes and their repetitions must be separated before forming an Euler
product.

## 4. Frozen theorem checks

1. Prove that a tree has no positive reduced closed path, so the full-tree
   geodesic shift has no periodic point.
2. Prove that the full-tree Hashimoto operator maps an infinite orthonormal
   edge family to pairwise orthogonal vectors of norm `sqrt(r)`, hence is
   noncompact and not trace class.
3. Prove that the nonzero canonical modular weight retains a constant-norm
   orthogonal family.
4. Prove the action boundary with its two cases: for `r>=2` the action is
   faithful and its image in `Aut(T_r)` is non-discrete; for `r=1`,
   `G_1=Z^2` has kernel `<u>` and discrete translation image `Z`, while the
   original action is non-proper and fails the finite-stabilizer
   tree-lattice hypotheses.
5. For `r>=2`, check the common-end signed-translation kernel `Z[1/r]`
   against the end-weight hypothesis; for `r=1`, keep the infinite action
   kernel `<u>` separate from the discrete translation image.
6. Separately classify positive-height group conjugacy classes as
   multiplication-by-`r` orbits in `Z/(r^k-1)Z`.
7. Derive total counts by Burnside, primitive counts by Möbius inversion, and
   the Euler product `(1-z)/(1-rz)`.
8. Show that the modular cocycle only substitutes `z -> r^{-s}z`.
9. Prove Bass--Serre translation length `|h(g)|` and exhibit collisions with
   the old generator-step marker.

## 5. Parameters and controls

- balanced `r=1`;
- prime controls `r=2,3,5,7`;
- composite baseline `r=4` and controls `r=6,8,9,10,12`;
- 18 deliberate `BS(p,q)` presentations spanning ascending,
  reversed-ascending, balanced, and non-ascending cases;
- 64 seeded cyclically reduced two-generator one-relator controls, seed
  `380038`, with independent cyclic-GBS eligibility parsing;
- finite-tree no-cycle controls;
- orthogonal-column/noncompactness controls;
- divergent group-conjugacy and empty full-tree controls;
- reciprocal-infinite-stabilizer-as-zero `PROVES_TOO_MUCH` control;
- tree-clock versus generator-clock marker witnesses;
- two fresh source/evaluator-separated subprocess runs.

## 6. Source/evaluator firewall

The source creates presentations, parameter rows, marker words, deterministic
controls, and bounds only.  It contains no evaluator import, orbit formula,
determinant formula, target coefficient, accepted-support table, or decision
oracle.  The evaluator independently parses the source JSON and implements
the exact combinatorics.  Scientific arithmetic is integer or
`fractions.Fraction`; no floating tolerance, network call, or unbounded word
enumeration is used.

Finite checks audit formulas and implementation.  They do not prove the
infinite no-cycle, noncompactness, action/properness, stabilizer, or
determinant statements.

## 7. Versioned exact results

The original external prototype seed produced:

- assertions: `277/277`;
- parameter rows: `11`;
- deliberate GBS controls: `18`;
- seeded random one-relator controls: `64`, with ineligible rows explicitly
  excluded rather than counted as failures;
- residue orbits agree with Burnside counts in the frozen direct range;
- primitive repetition identities and Euler products agree through degree
  twelve;
- two fresh scientific outputs are byte-identical;
- legacy external science SHA-256:
  `3485a1d925924459ce92ff3aeddb31302277589d61bd9d961ecb823b1e5bb089`.

That legacy digest is retained only as seed provenance: its action-boundary
assertion encoded the known overbroad claim that the `r=1` image is
non-discrete.  The corrected authority evaluator uses the two-case boundary
in Section 4, still passes `277/277`, and has scientific SHA-256
`a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24`.
Only the corrected authority digest is eligible for the final integration
and repository Route card.

## 8. Forbidden repairs

Forbidden: another representation, local system, character, fiber rank,
nilpotent automaton, quotient, induced flow, fundamental domain, alternative
divisor splitting, basepoint/radial damping, finite-total-weight retrofit,
von Neumann/groupoid determinant conflation, `1/|Z|=0`, first return,
acceleration, old marker inheritance, target-zero or prime table, and Route B.

## 9. Frozen decision

```text
STOP_BASS_SERRE_TREE_BRANCH
CLOSE_ENTIRE_AFFINE_BRANCH
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

## 10. Provenance and successor

- research package SHA-256:
  `208e839b8379d0e30a2f3647fe7a52f543ead2c9d1dcf57d1c0271dbe525f0c3`;
- original external source-lock seed `/tmp/paper38_source_lock.md` SHA-256:
  `34acddf6573a11adbd80adafa97e58cb1ac30be7a75a2c555443cbc7ee8762e0`;
- normalized authority `SOURCE_LOCK.md` SHA-256 after the explicit `r=1`
  action-boundary correction and whitespace normalization:
  `febaeb0b1db1a0713bbb68cf99110d7ecf2df8b39caf3ee9f311598f45fa6a7a`;
- external legacy draft Route seed `/tmp/paper38_route_v0_2.yaml` SHA-256:
  `34529b3fdd42d07311ff1995c81b04cb3ca8559b61fcecc3c841dd3583505983`;
- research hash ledger SHA-256:
  `7fe92afcccbc646064079203225d84df907520e09dab4a5c57d055b17fc0bf0d`.

The final repository Route hash is intentionally not recorded here; it is
created only after the corrected authority integration is complete.

Paper 39 may only build an affine-branch closure obstruction DAG and return
control to the pre-existing global Symbolic Dynamics registry.  It may not
try another affine mechanism.
