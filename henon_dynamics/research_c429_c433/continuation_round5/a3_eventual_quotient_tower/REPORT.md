# A3/R5: eventual finite-quotient stabilization

2026-09-09 UTC. New bounded theorem bridge in the same local research contract. All previous author and review files remain unchanged.

## Exact question and outcome

Fix any odd prime $p$, $K_0=\overline{\mathbb F}_p((s))$, and $P_s(z)=(1+s)z+z^2$. Let $L_e/K_0$ be the canonical cyclic small-cycle field of degree $p^e$. Does its unique subfield of degree $p^j$ stabilize, inside one fixed separable closure, for every fixed $j$ and all sufficiently large $e$? Must the corresponding native-oriented characters stabilize as well?

**Author outcome: PROVABLE AS STATED relative to the two named R4 contact/compact-limit theorems; those dependencies and the new bridge require their respective coordinator acceptance.** The complete [proof](PROOF_PACKAGE.md) establishes a canonical continuous surjection

$$
\chi_\infty:G_{K_0}\longrightarrow\mathbb Z_p
$$

with the exact quantifier order

$$
\forall j\ge1\ \exists E_j\ge j\ \forall e\ge E_j\ \forall g\in G_{K_0}:
\quad \rho_e(g)\bmod p^j=\chi_\infty(g)\bmod p^j.
$$

Here $\rho_e$ records **one original native step as $+1$**, not an unspecified cyclic generator. Consequently the degree-$p^j$ subfield of $L_e$ is eventually the same field $K_j$, and

$$
K_1\subset K_2\subset\cdots,\qquad
\operatorname{Gal}\left(\bigcup_jK_j/K_0\right)\simeq\mathbb Z_p.
$$

The result does not assert $E_j=j$, $K_j=L_j$, or nesting of the full fields $L_e$.

## Mechanism and dependency boundary

The actual R4 A1 proof supplies all-anchor contact convergence, and the actual R4 D1 proof supplies a compact classical limit $\Omega$ conjugate to the $p$-adic adding machine. Their full proofs were read, at hashes `038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e` and `e2daa9770024c62e7b7fb09855d4c23eaa0c4cd0aa5416ad268288dbe569aedd`; D1's complete E1 review was also read. This bridge does not substitute those results with an unwritten compactness assumption.

Finite nets chosen among separable algebraic cycle roots prove uniform continuity of the Galois action on the entire compact closure. The limit is Galois-stable, and each Galois action commutes with the native adding machine. An explicit centralizer argument makes it a translation. Every mod-$p^j$ clopen quotient of the limit then matches every sufficiently nearby finite cycle, simultaneously for native dynamics and Galois. This includes quotient sizes skipped by a chosen sequence of metric-radius partitions.

The translation amount is independent of the limit's chosen origin; no unit twist survives preservation of the native $+1$ action. Nontriviality of the already accepted first quotient makes the compact image all of $\mathbb Z_p$. Classical finite/infinite Galois correspondence converts the kernels to actual stabilized subfields.

Classical compact-group, odometer-centralizer and Galois-correspondence mechanisms are subtracted. The centralizer and continuity arguments are proved directly; the field correspondence was checked in [Stacks, Section 9.22](https://stacks.math.columbia.edu/tag/0BMI). This is not a separate paper or broad priority claim.

## Limits and execution record

Limit points are classical points of a completed algebraic closure; they are not assumed algebraic over $K_0$. The tower is defined from open character kernels in $G_{K_0}$, not by declaring a limit coordinate to be an algebraic generator. No identification with a fixed subfield of the completion is used.

No quantitative stabilization threshold, full Witt coefficient vector, complete higher ramification sequence, global cycle-quotient transitivity, or new paper admission is asserted. Mathematical executions: **zero**. Only this allocated report and proof were written; no agents, old-file changes, shared-state, Git, manuscript or PDF action occurred.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
