# AF5-C auxiliary torsion-kernel contract

Date: 2026-09-08 UTC. This is an auxiliary input to the existing AF5-C
full cyclotomic periodic-point algorithm, not a new candidate or admission.
Write ownership is only this `torsion_kernel/` directory.

## Exact question

For a finite list of Laurent polynomials in $d\ge0$ variables, with all
coefficients given exactly in a specified finite cyclotomic field
$K=\mathbb Q(\zeta_N)$, prove or refute an explicit terminating algorithm
for the Zariski closure of their common torsion zeros in
$(\mathbb G_m)^d$. The output must be a finite union of connected torsion
cosets, including an explicit representation of their translating roots
of unity and saturated character lattices. A finite exact subfield of
$\mathbb Q^{\mathrm{cyc}}$ is accepted after an explicit embedding into
such a cyclotomic field is supplied or effectively recovered.

Required operations are exact intersection, equality, and coordinate
projection of finite unions of torsion cosets. The projected torsion
image must equal all torsion points on the projected cosets, not merely
be Zariski dense there. Empty sets, the zero-dimensional torus, zero and
one-term polynomials, repeated exponents, coefficient cancellation,
nonprimitive character lattices, and disconnected equation kernels
must be covered.

## Proposed route, unproved at this freeze

1. Expand each coefficient in a finite rational linear combination of
   powers of $\zeta_N$ and retain nonzero rational-weighted terms.
2. Partition any torsion vanishing sum into minimal vanishing blocks.
   Verify the exact rational-coefficient Mann theorem against a primary
   source before treating it as an input.
3. Enumerate partitions and the finitely many possible blockwise root
   ratios; keep exact weighted zero sums and impose the resulting
   binomial equations in the original variables.
4. Use integer Smith normal form to test consistency and split every
   equation system into connected torsion cosets. Prove soundness,
   torsion coverage, and torsion density.
5. Give explicit lattice/ideal tests for the three required operations,
   with an actual torsion-lifting argument for coordinate projection.

## Success and failure boundary

Success is a complete proof under the stated finite exact input model,
plus an accessed-source record for the Mann dependency. If the claimed
algorithm adds false torsion solutions, misses a torsion point, needs an
ineffective choice, or loses torsion lifting, record the precise gap or
counterexample instead of calling the kernel closed.

No general novelty or paper-level increment claim is made. Classical
torsion-coset algorithms and integer normal forms remain classical inputs.
The main Hénon algorithm, its initial root-length bound, and its final
finiteness argument belong to other owners and are not proved here.

## Execution boundary

Default evidence is a hand proof plus bounded primary-source browsing.
No mathematical program, census, symbolic import, GPU work, old rerun,
external model/API call, Git operation, or global-state write is authorized
by this contract. Any useful mathematical execution would first need an
explicit analytic purpose frozen separately. Source browsing and ordinary
file reads are not represented as mathematical execution. New Markdown
files use `apply_patch` only.

The repository batch workflow, `proof-writer`, `research-lit`, and bounded
ARS source-verification guidance govern this work. Current-team output is
AI-assisted internal research, not external peer review. The source-only
boundary `NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.
