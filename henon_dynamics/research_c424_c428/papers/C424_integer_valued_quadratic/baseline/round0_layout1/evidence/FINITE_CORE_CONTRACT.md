# AM1 finite-core contract, frozen before its first mathematical execution

2026-09-08 UTC. The coordinator requested a single exact CPU certificate
after checking the new analytic reduction. This remains the same AM1
question, with zero manuscript or paper admission. The reduction is in
[PROOF_PACKAGE.md, Step 8](PROOF_PACKAGE.md): every $a\le-146$ is classified,
every $a\ge2$ has no periodic points, and $a=1$ is an analytic control.

## Exact finite scope

Run exactly the 147 integer parameters $a=-145,-144,\ldots,1$ once.
This is the full proved residual parameter range plus the upper-boundary
control, not a conjectural cutoff or enlarged sample. No period cutoff,
floating point, random search or old mathematical program is allowed.

For each parameter use odd doubled-centered coordinates $z=2x+1$.
The cyclic recurrence and one-step map are
$$z_i^2+8a+7=4(z_{i-1}+z_{i+1}),\qquad
G_a(z,w)=\left(w,\frac{w^2+8a+7}{4}-z\right).$$
For odd $w$ the numerator is divisible by eight. Thus $G_a$ and its
inverse preserve the odd lattice and the division is exact.

Set
$$B_a=4+\lfloor\sqrt{9-8a}\rfloor,\qquad
S_a=\{z\in\mathbb Z:z\text{ odd},\ |z|\le B_a,
                         \ |z^2+8a+7|\le8B_a\}.$$
The maximum estimate for $v=x+1/2$ gives
$|z|\le4+\sqrt{9-8a}$, hence $|z|\le B_a$ by integrality.
The recurrence then gives the second alphabet restriction. Therefore
every periodic point is in the proved finite set $V_0=S_a\times S_a$.
These are integer-square-root and integer-comparison operations only.

Iterate exact pruning
$$V_{j+1}=\{P\in V_j:G_a(P)\in V_j\}$$
until equality. It terminates since the set decreases and is finite.
Every periodic point stays in every set; the final restriction is an
injective self-map of a finite set, so every remaining point is periodic.
This proves that the final set is exactly the full periodic locus.
This finite-partial-permutation lemma is deducted C412 ownership.

## Expected output, not predeclared results

The stdlib-only script will record every parameter, its alphabet and initial
size, every strictly decreasing pruning cardinality, stable cardinality,
all canonical oriented cycle words in original $x$ coordinates, and the
least-period histogram. Canonicalization is by cyclic rotation only.
No cyclic word is identified with its reversal unless already a rotation.
The script must assert each reported word's exact recurrence and primitive
period and that its expanded state set is the complete stable set.

It will compare the full stable set against the four symbolic families
from Step 8, for every nonnegative $k$ capable of producing the present
parameter. The output must list every unmatched cycle explicitly rather
than force-fitting it into the expected families. No numerical total,
exception count or universal maximal period is predicted in advance.

Record the script and output hashes after its one execution. Do not rerun
on unchanged inputs just to reconfirm a successful output. If a code error
appears, preserve it and explain the exact changed input before a retry.
The output is an author certificate, not an independent review; a nonauthor
must later check the proof, certificate organization and substantive
increment before any coordinator admission.
