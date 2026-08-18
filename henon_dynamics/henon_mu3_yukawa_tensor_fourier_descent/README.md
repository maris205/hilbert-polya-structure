# HCS-C61: zeta-equivalent tensor algebras and Fourier descent

Status: **`TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING /
NOT_RELEASED`.**

Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This directory is a target-lock formal package.  It contains no C61 code,
machine evidence, paper, release archive, or promotion authorization.  Every
G0--G7 gate is pending.  Values imported from the adaptive scan, arithmetic
design, source audit, and `/tmp` pilots are expected targets only; they are not
theorem authority.

The final target-report digest is bound exactly as supplied by its owner:

```text
target_report_sha256: eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026
```

The bound report has 59,956 bytes and 1,096 lines.  No earlier target-report
digest or self-atlas aggregate hash may be inferred from filenames, messages,
or partial artifacts.

## 1. Locked successor

The recommended paper title is:

> **Zeta-Equivalent Tensor Algebras of the Hénon Gassmann Twins and an
> Explicit Fourier Descent.**

The project basename is `henon_mu3_yukawa_tensor_fourier_descent`.

The sole released authority is P60
`fe1217810b72840619efdf40a2af31b8b80d96f6`.  C61 starts from C60's
released `W(E6)` normal closure `K/Q`, the nonconjugate order-162 Gassmann
subgroups `H_+,H_-`, their degree-320 fixed fields `F_+,F_-`, and C60's
biquadratic envelope `M subset F_+,F_0,F_3 subset L`.

C61 does not add another arm to that envelope.  Its new object is the ordered
triple of dimension-102400 finite étale algebras

\[
 \mathscr T_{++}=F_+\otimes_{\mathbf Q}F_+,
 \quad
 \mathscr T_{+-}=F_+\otimes_{\mathbf Q}F_-,
 \quad
 \mathscr T_{--}=F_-\otimes_{\mathbf Q}F_-.
\]

The target is integrated: the complete tensor/Burnside comparison and the
exact Fourier-to-mixed-factor bridge must both pass.  An atlas alone, a
Fourier note alone, local arithmetic alone, or a one-self-product result is a
KILL outcome rather than a smaller C61 paper.

## 2. Conditional theorem spine

Put `G=W(E6)`, `X=G/H_+`, `Y=G/H_-`, and
`x=[X], y=[Y]` in the Burnside ring.  Conditional on G0--G7, the headline is

\[
 x^2,xy,y^2\text{ are pairwise distinct in }B(G),
 \qquad
 \operatorname{lin}(x^2)=\operatorname{lin}(xy)
 =\operatorname{lin}(y^2).
\]

Thus the three finite étale algebras are pairwise nonisomorphic although their
rational permutation characters, Artin formal products, and products of
Dedekind zeta functions agree.  This is not an isomorphism of finite G-sets,
fields, rings of integers, or integral permutation modules.

The locked factor-degree targets are

```text
T++ = [320x2,960x2,1920,5760x2,8640x2,17280,25920x2]
T+- = [640,960x2,1920,2880x4,8640x2,17280,51840]
T-- = [320x2,960x2,1920,5760x2,8640x2,17280,25920x2]
```

Each has 12 factors and total dimension 102400.  The mixed product is
separated from either self product by degrees.  The equal self spectra do not
separate the two self products; G1 must use the two diagonal degree-320
`H_+`/`H_-` types and the core-free common-normal-closure extension argument.

The mixed product must retain three distinct inventories:

```text
160 conjugate relative positions
12 double cosets / simple factors
8 Q-isomorphism types
```

Its unique degree-640 minimum rebounds to C60's `L/M`, and its unique
degree-51840 maximum is `K`.  Both uniqueness statements are confined to the
twelve mixed factors.

## 3. Fourier-selected mixed base

Fourier decomposition of C60's released integral carrier `lambda` under
`N/J isomorphic to V4` must projectively reconstruct

\[
 R_0=0,\qquad r_+=R_+/2,\qquad r_3=R_3/4,
 \qquad r_0=r_+r_3,
\]

with coefficientwise exact division and

\[
 4\lambda=\operatorname{Tr}_{L/M}(\lambda)+2r_++4r_3,
 \qquad \delta_0=\delta_+\delta_3,
 \quad \delta_i=r_i^2.
\]

The three nonzero character components must prove that the four `V4`
conjugates of `lambda` span exactly dimension three over `M`: `lambda` is
primitive but not a normal-basis generator.  No normal integral basis claim
is made.  At `p=692717`, the 243-term Trace carrier, normalized `r_+`, and
normalized `r_3` have identity values `581739`, `643771`, and `119649`.
The Trace carrier SHA-256 is
`a7398d36cea0c83ace64466a579e21666731d1e3c8e8641df4ce036c79de2bd7`.
These three nonzero witnesses, together with the distinct character
eigenspaces, are the exact rank-three bridge.

Define

\[
 S_+=\operatorname{Stab}_G(r_+),\qquad
 T_+=\operatorname{Stab}_G(\{r_+,-r_+\}),
\]

\[
 A=\mathbf Q(\delta_+)=K^{T_+},\qquad
 B=\mathbf Q(r_+)=K^{S_+}.
\]

The exact mixed bridge is equality of embedded element sets

\[
 T_+=\langle H_+,g_{149}H_-g_{149}^{-1}\rangle,
\]

not agreement of orders, hashes, ToM locators, isomorphism types, or merely
conjugacy.  The plus-self `263f...` and embedded minus-self `a426...`
degree-1920 joins form one G-conjugacy class; an exact conjugator must be
checked.  That self P3 class is nonconjugate to the mixed Fourier
`T_+` class `55d7...`.  No “three nonconjugate joins” statement is allowed.

The fixed-field target is

\[
 [A:Q],[B:Q],[M:Q],[F_+:Q]=40,80,160,320,
 \qquad B\cap M=A,\qquad BM=F_+.
\]

In particular, `Q(r_+)` is degree 80 rather than `F_+`, and
`Q(delta_+)` is degree 40 rather than `M`.

## 4. Canonical pending gates

| gate | required completion | state |
|---|---|---|
| G0 | released authority, conventions, Batch/Route/guard, 30 false leaves | PENDING |
| G1 | all 36 tensor rows, three products, Burnside separation | PENDING |
| G2 | mixed 160/12/8 atlas and fixed-field dictionary | PENDING |
| G3 | exact product-form resolvents and evaluated primitivity | PENDING |
| G4 | Fourier/Kummer identities, type-3 equality, fixed-field diamond | PENDING |
| G5 | complete global arithmetic for all advertised fields | PENDING |
| G6 | complete local arithmetic in both retained D3 branches | PENDING |
| G7 | independent checkers, hostile tests, sources, formal/paper/release gates | PENDING |

No target-selection pilot discharges any cell of this table.

## 5. Released-input pins

G0 must fail closed unless it independently rebinds at least:

- P60 commit `fe1217810b72840619efdf40a2af31b8b80d96f6`, parent
  `f3b3726c40519cdd8ac7832f9f22df16d451b890`, and released tree
  `22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a`;
- C60 full manifest
  `37c1f227aee6c0bfff233ffc1a7f1f8d2a8a27657faad353af711f2e503ed0a4`;
- C60 live/archive Route
  `8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872`;
- C60 certificate/payload
  `d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518` /
  `dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead`;
- C60 group/resolvent evidence
  `dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2` /
  `f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da`;
- C60 frozen permutation arrays
  `0fc281590b635eed046cc4a8d38036895e2b1bc56284a0948b1576303de1c2f5`;
- C59 resolvent evidence
  `667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6`;
- released Batch
  `d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5`;
- the protected guard as an external G0 input, never a C61-owned file.

## 6. Exact formal inventory

The target-lock project root contains exactly these 13 Markdown files:

```text
README.md
RESEARCH_QUESTION.md
METHODOLOGY_BLUEPRINT.md
THEOREM_PACKAGE.md
DERIVATION.md
PROOF_PACKAGE.md
EXPERIMENT_PLAN.md
EXPERIMENT_TRACKER.md
IMPLEMENTATION_CHECKLIST.md
NARRATIVE_REPORT.md
SOURCE_AUDIT.md
INTEGRITY_REPORT.md
PAPER_PLAN.md
```

Together with the candidate `route_a_evaluation.yaml` and staged Batch, they
form 15 target-lock inputs.  They are future machine inputs, not current
machine evidence and not theorem premises.

## 7. Hard boundary

Both `D_3=ToM140` and `D_3=ToM206` remain live.  No local field is classified
from `(n,e,f,d)`.  No expanded characteristic-zero resolvent, maximal order,
integral basis, monogenicity, class number, regulator, trace form, rational
point, Brauer--Manin, motive, automorphy, functional equation, analytic
continuation, decomposition Frobenius, bad Euler factor, epsilon factor, root
number, RH, or Hilbert--Pólya conclusion is licensed.

Current boundary: **`TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING /
NOT_RELEASED`**.  Promotion authorization is false.
