# R4 X1 — Fricke parabolic-divisor primary-source check

2026-09-09 UTC. Bounded source verification for C4; no mathematical
execution or new author proof. Exclusive source-lane report.

## Frozen use and result

The family and native clock are
$$
x^2+y^2+z^2-xyz-Ax-By-Cz=D,
\qquad T=s_zs_ys_x.
$$
The prescribed divisor $\mathscr F$ is the smooth marked two-cycle fold
through $(A,B,C,D)=(0,0,0,-9/4)$, not the surface-singularity divisor.
The unchanged target is unramified normalization of every higher native
period splitting field at $\eta_{\mathscr F}$.

The [C4 R4 frozen question](../c4_remote_parabolic_divisors/REPORT.md)
and [accepted R3 reduction](../../continuation_round3/c4_smooth_fold_separation/PROOF_PACKAGE.md)
own the finite-flat fixed loci and isolation of the period-two part.
This scout does not reprove those inputs. It checks sources for a
relative nonresonance statement on the remaining genuine higher-period
points, or distinct-period multiplier-one divisor noncontainment.

**Result:** a direct-family, all-saddle **ambient genericity** theorem was
verified, but no applicable relative theorem on $\mathscr F$ or
single-parabolic/all-other-nonresonant parameter theorem was located in
this bounded pass. Source absence is not a no-go theorem.

## Closest exact theorem: Rebelo–Roeder, Lemma 10.8

Julio Rebelo and Roland Roeder, *Dynamics of groups of automorphisms of
character varieties and Fatou/Julia decomposition for Painlevé 6*,
[arXiv:2104.09256v4](https://arxiv.org/abs/2104.09256v4), 2024.
The inspected metadata describes it as forthcoming in *Indiana
University Mathematics Journal*; final publisher metadata was not checked.

Lemma 10.8, printed pp. 42–44, states that outside a countable union of
real-algebraic hypersurfaces in $\mathbb C^4$, the surface is smooth and
every fixed point of every hyperbolic word in the even subgroup $G$ is a
hyperbolic saddle. Here word hyperbolicity means exponential degree
growth; the conclusion is actual derivative hyperbolicity.

Its proof combines Picard-parameter ambient eigenvalues (Corollary 6.8),
uniform exclusion of periodic points near infinity (Proposition 9.6),
semialgebraic projection of the trace-in-$[-2,2]$ obstruction, elimination of
the multiplier-one incidence, and holomorphic continuation of simple
fixed points. See the
[primary theorem and proof](https://arxiv.org/pdf/2104.09256v4).

**Fit:** this proves ambient bad loci are proper, not that different
native-period bad loci have distinct components. The continuation avoids
the whole multiplier-one locus; it supplies no continuation inside the
marked fold after removing its period-two part.

## Exact translation and missing relative bridge

The source uses the plus-$xyz$ convention. The elementary coordinate
translation
$$
(x_{\rm src},y_{\rm src},z_{\rm src})=(-x,y,z),\qquad
(A_{\rm src},B_{\rm src},C_{\rm src},D_{\rm src})=(-A,B,C,D)
$$
identifies that equation and its named involutions with the frozen family,
without reordering the word. This is a coordinate check, not a new
dynamical theorem.

The source's even-subgroup statement can be tested on $T^{2n}$; it is not
a license to rename $T^2$ as the native clock. The period-two fold is
already a multiplier-one obstruction for the full fixed locus of those
even powers. Thus applying an ambient theorem after discarding all bad
parameters also discards the very divisor of interest. This is an
inference from the frozen fold property, not a claim made by the source.

The missing bridge is precisely an **on-$\mathscr F$, all-residual-sheet**
statement. For each higher layer one needs either a witness on that same
divisor controlling every genuine higher-period point, or a theorem that
its residual multiplier-one incidence does not dominate $\mathscr F$.
An ambient open set near the Picard parameter, unrestricted genericity,
or expected codimension does not supply such a statement. No assertion
that the stronger multiplier condition is necessary for normalized
unramifiedness is made here.

## Other primary passages checked and excluded

### Iwasaki–Uehara: asymptotic saddle counts are not all-sheet control

Katsunori Iwasaki and Takato Uehara, *Singular cubic surfaces and the
dynamics of Painlevé VI*,
[arXiv:0909.5269](https://arxiv.org/abs/0909.5269), 2009 preprint.
Theorem 1.6 gives finite isolated periodic sets, counts with local
multiplicity, and asymptotic equivalence of saddle counts and total
isolated counts for non-elementary monodromy. The displayed route is the
Lefschetz/local-index counting theorem plus saddle equidistribution;
see Theorems 2.5–2.8 and Corollary 2.6 in the
[primary PDF](https://arxiv.org/pdf/0909.5269).
It does not state that every periodic point is a saddle or separate two
multiplier-one parameter divisors. Its asymptotic conclusion leaves room
for exceptional non-saddle points and cannot discharge the residual
all-sheet obligation.

### Rebelo–Roeder's questions paper: group dynamics, not the missing theorem

Rebelo–Roeder, *Questions about the dynamics on a natural family of
affine cubic surfaces*,
[arXiv:2307.10962v2](https://arxiv.org/abs/2307.10962v2), 2024 version.
The inspected [primary passages](https://arxiv.org/pdf/2307.10962v2),
§5.1 Questions 3–4 and §6.5 Question 10, concern Julia membership,
density of points with hyperbolic stabilizers, and actions of subgroups
whose nonidentity words have exponential growth. These are not asserted
single-parabolic parameter or relative divisor-separation theorems.
The questions are not used as evidence that C4's specific target is open
in all literature or false.

The already-checked real connected-locus theorem in Cantat's
`0711.1727` is excluded by instruction and is not counted as a new
finding. Generic polynomial-automorphism transversality sources are
being checked separately by C4; no hypothesis transfer from those
families is presumed in this report.

## Access, coordination, and stopping boundary

The research-lit skill was read and used local-first. Available tools
showed no configured Zotero/Obsidian source. The local paper listing was
unrelated to Fricke dynamics; no local PDF was opened. The fetch script
was absent from the scoped tool/skill search, so arXiv-targeted web
retrieval was used. No PDF was downloaded. An institutional mirror and
an author-PDF attempt failed during detailed retrieval; the arXiv
versions supplied the inspected primary text. Search snippets were
discovery material only.

Actual detailed reading includes the complete displayed proof of
Lemma 10.8, its Picard eigenvalue input, and the selected statements and
mechanisms identified above; no full audit of all three papers is
claimed. No separate child was created for this task. C4 and the
coordinator received the strongest theorem's locator and its precise
relative-domain limitation.

This bounded source task is complete. Only this report was written; no
mathematical programs, finite census, private-proof upload, external
model call, Git operation, shared/source-package edit, configuration
change, or manuscript build was performed. The source result does not
admit SF2 or change the accepted R3 scope.
