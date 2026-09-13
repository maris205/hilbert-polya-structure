# Paper21 Publication-Stage Scope

Date: 2026-08-22 UTC  
Project root: `papers/21-three-mode-hamiltonian-cubic-degree`  
Role: separately invoked publication-governance author  
Status: author-stop scope; no manuscript authority yet

## Authority boundary

The proof-first plan and source lock have already passed. In this invocation I
may create exactly one file, this file, and no other project path may change.

I do not edit `paper/main.tex`, `paper/math_commands.tex`,
`paper/references.bib`, any source-lock file, any review note, or any build
artifact. I do not compile, run BibTeX, run CAS or numerical code, access a
dataset, use the network, transport, submit, upload, or communicate
externally. After this file is written and read back, I stop.

The only possible subsequent project write in this gate is one fresh,
independent reviewer note at `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`.
The reviewer may write that file only after every frozen check passes; a
blocker means WRITE NOTHING. The review note must be the reviewer’s sole
project write and its final non-empty line must be exactly
`PUBLICATION_STAGE_PASS`. That token records eligibility for a separately
authorized later manuscript stage; it does not itself authorize source edits,
a rebuild, release, submission, upload, or any external effect.

## Exact anonymous public identity

The locked title string is exactly:

`Three-Mode Hamiltonian Shears in A6: Exact Degree Growth and Cubic Perron Subfamilies`

The typeset manuscript may render the `A6` as `\mathbb A^6`, but the source
title string remains fixed in the A6 wording already used throughout the frozen
paper records. The public author is exactly `Anonymous Authors` and the source
date is empty. No real name, affiliation, email, ORCID, acknowledgment,
funding, reviewer identity, local path, digest, dashboard, agent/model name,
lifecycle token, submission venue, or private provenance may appear in public
manuscript text or PDF metadata.

## Frozen theorem and proof contract

The manuscript must preserve the locked theorem from the source package:
`K` is algebraically closed of characteristic zero, `g` is an integer with
`g >= 8`, and the fixed family is

\[
V=q_1^2q_2^2q_3^2+q_1^g,\qquad
W=p_1^2p_2^2p_3^2+p_3^g,
\qquad F_g=T\circ S.
\]

The selected matrices are

\[
A_g=\begin{pmatrix}g-1&0&0\\2&1&2\\2&2&1\end{pmatrix},\quad
B_g=\begin{pmatrix}1&2&2\\2&1&2\\0&0&g-1\end{pmatrix},\quad
C_g=B_gA_g.
\]

The exact proof ledger remains frozen as:

- inverse automorphism and symplecticity;
- six-row support ledger and `A_g`;
- exactly two selector gaps, with corrected `M_T`;
- cone invariance with the `g = 8,\dots,11` versus `g >= 12` split;
- phase/carry induction and characteristic-zero no-cancellation;
- `q_3` visibility and exact degree identity;
- Perron-Frobenius, row-sum bound, and cubic mod-5 subfamilies;
- `g = 7` as a strict-cone boundary, not a selector tie.

The manuscript must remain proof-first, with every theorem-critical step in the
main body.

## Citation boundary

Exactly two bibliography entries are authorized, both for terminology and
bounded context only:

| Key | Record to verify | Use permitted |
|---|---|---|
| BlancVanSanten2019 | Jérémy Blanc and Immanuel van Santen, “Dynamical degrees of affine-triangular automorphisms of affine spaces,” arXiv:1912.01324v1, submitted 2019-12-03, https://arxiv.org/abs/1912.01324 | one sentence defining the larger affine-triangular comparison class; no theorem transfer |
| ShaoSun2025 | Enbo Shao and Xiaosong Sun, “Dynamical degrees of affine-triangular automorphisms in dimension four,” arXiv:2509.14584v1, submitted 2025-09-18, https://arxiv.org/abs/2509.14584 | one sentence noting dimension-four algebraic-degree context; no theorem transfer |

The bibliography must contain only these two citations. No other source is
authorized in the manuscript plan.

## Anti-claim boundary

The manuscript must not claim genericity, arbitrary dimensions, arbitrary or
sign-changing coefficients, positive characteristic, all symplectic or
affine-triangular automorphisms, universal non-conjugacy or classification,
topological/measure-theoretic/arithmetic entropy, periodic/trace/multiplier/
torus/arithmetic statements, CAS or numerical proof certificates, or absolute
novelty/priority/firstness/optimality.

## Deterministic next stage

If the publication-stage review passes, the separately authorized manuscript
stage may write only `paper/main.tex`, `paper/math_commands.tex`, and
`paper/references.bib`, with the same anonymous identity and the same proof
contract. No other path is to be opened by this scope.

