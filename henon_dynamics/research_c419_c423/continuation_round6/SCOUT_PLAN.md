# Sixth continuation: two original full questions, new closure mechanisms

Date: 2026-09-08 UTC. The user explicitly said **继续** after the fifth
checkpoint. Resume C419–C423 at M1/AS2/IR1 **3/5 admitted contracts,
zero manuscripts/PDFs/formal evaluations**. No accepted proof is rerun.

This pass focuses on two existing full questions, not a fresh list of
renamed candidates. Their original success thresholds remain unchanged.

## LY4: analytic exhaustion beyond the classified six-channel

Every integer parameter of $L_a(x,y,z)=(y,z,(a+y+z)/x)$, every ordinary
two-sided nonzero integer periodic orbit, modulo cyclic rotation, remains
in scope. The fifth-pass complete low-period/$a=1$ strata and the rational
$N\le48$ bound avoiding $0,-1$ are inherited, not recomputed.

Try a genuinely new uniform descent on six-step coordinate differences,
or another arithmetic argument that either establishes exhaustion E
($a\ne1$ implies least period at most six) or classifies all remaining
higher-period channels. A possible intermediate route is to prove that
every non-six-periodic residual orbit must visit $1$ or $-2$, then derive
a parameter-independent residual core after removing the complete
unbounded six-channel. Neither intermediate statement is assumed true.
Do not enlarge or rerun the old height-eight alphabet. Freeze any new
mathematical computation's exact analytic role before executing it.

Owner: `lyness_exhaustion/`. Full proof or exact failed implication;
no helper-only admission, C-number or manuscript.

## AF5-C: an exact Noetherian torsion-correspondence algorithm

The original family remains $F_c(x,y)=(y,y^2+c-x)$ for every integer
$c$, on all $\mathbb A^2(\mathbb Q^{\rm cyc})$, including zero coordinates.
Success is an explicit terminating procedure outputting **all** ordinary
cyclotomic periodic points and their least native periods. A finite
algebraic alternative to explicit period/conductor bounds is permitted
by the original freeze, but requires an actual exhaustion proof.

The proposed new strategy is unproved at this freeze:

1. Obtain a computable root-of-unity length bound for every cyclotomic
   integer of house at most $1+\sqrt{1+|c|}$. Choosing a fixed padded
   length $M$ realizes every such coordinate by a sum of $M$ roots of
   unity. Padding by vanishing sums of lengths two and three must be
   justified, not a fictitious zero torus coordinate.
2. On $T=(\mathbb G_m)^{2M}$ let $\phi$ sum the two coordinate blocks.
   Starting with $V_0=T$, compute the torsion-point Zariski closure of
   the relation $u,v\in V_j$, $F_c(\phi(u))=\phi(v)$, then project to
   $u$ to define $V_{j+1}$ as a finite union of torsion cosets.
3. Prove that this closure/projection operation preserves the **exact
   torsion-point set**, not merely its Zariski closure, and that the
   descending closed chain stabilizes with an effective equality test.
4. On stabilization, show that every torsion representative has an
   infinite bounded-house forward orbit. Its original coordinates stay
   in a single finite number field; integrality and a bounded house
   then force finiteness, and invertibility forces periodicity.
5. Conversely every cyclotomic periodic point must survive every step.
   Use the already source-dependent finiteness result to prove that
   $\phi$ is constant on each surviving connected torsion coset, so
   an explicit finite point list and least periods can be extracted.

Potential fatal failures: an ineffective initial Loxton bound; torsion
closure adding false torsion solutions; failure of torsion lifting under
projection; confusing a descending constructible chain with a closed
Noetherian chain; an undecidable stabilization test; or extracting an
infinite image while calling it a finite atlas. Each requires a proof or
an explicit unclosed status. No large conductor/period census is planned.

Disjoint work:

- Coordinator owns `cyclotomic_algorithm/`, the main algorithm and shared
  state. The classical fifth-pass finiteness helper is reused with its
  stated Ji–Xie–Zhang v2 dependency, not counted as a new proof.
- `cyclotomic_sources/` owns the exact effective Loxton/root-length
  dependency and bounded closest-source/algorithm-ownership audit.
- `torsion_kernel/` owns an explicit exact torsion-closure/projection
  algorithm over cyclotomic coefficients, its Mann-type dependency and
  adversarial checks of the proposed algebraic step. It is an auxiliary
  input to the same AF5-C question, not another candidate.

## Gates and execution limits

Proof-writer governs original-claim versus helper boundaries. Research-lit
and bounded ARS source verification govern actual theorem hypotheses,
effective constants, access and ownership. This is not a full/Socratic ARS
pipeline or a manuscript phase. Current-team delegation follows the
repository/runtime instructions; no old-model, paid API or GPU default
is activated. Named Zotero/Obsidian tools and relevant local PDF/helper
sources were unavailable; official primary browsing is the fallback.

No mathematical program has run in this pass before this freeze. No
new census is planned; any useful implementation needs a separately
frozen exact purpose. Authors write only their assigned new directories
with apply_patch, preserve historical proofs and other streams, and do
not change admissions or Git. A substantial full survivor requires a
non-author full proof/source/increment review before admission.

If neither original question closes, report that scientific boundary;
do not split Loxton, torsion kernels, period strata or Noetherian helpers
into the two remaining papers. No target arithmetic or A2 claim follows
from source-side effectiveness. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
