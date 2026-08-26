# Paper 11 candidate lock

Lock date: **2026-08-14 (Asia/Shanghai)**  
Status: **PHASE 1 PASS — PHASE 2 AUTHORIZED**

## 1. Primary candidate family

```text
Candidate family: DEN-EF-ACT-ORBIT-CONV-P-A
Actual unit: ACT-ORBIT-p-a with inherited indiscrete topology
Source action: additive logarithmic R-action, stabilizer (log p) Z
New object: actual-topology transformation groupoid and typed convolution conventions
Primary question: is Phi:C_c(R)->C_qc^glob(G_act) a *-isomorphism?
```

All fixed-orbit statements quantify over every rational prime `p` and every
normalized Paper-9 orbit label `a`.

## 2. Exact inherited evidence

The design depends on, but does not mutate:

- Paper 9 proof audit, SHA-256
  `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8`;
- Paper 9 source audit, SHA-256
  `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20`;
- Paper 9 release PDF, SHA-256
  `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02`;
- Paper 10 proof audit, SHA-256
  `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a`;
- Paper 10 release PDF, SHA-256
  `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4`.

Paper 9 owns orbit indiscreteness and the exact stabilizer. Paper 10 owns the
unit-space separated-observable collapse. Paper 11 must contribute arrow-level
groupoid/function/convolution/completion results rather than relabel either
input.

## 3. Typed owner records

```text
ACT-GRPD-p-a
  = X_{p,a} rtimes R with actual-indiscrete x usual-R arrow topology;

GLOB-QC-ACT-GRPD-p-a
  = globally continuous open-cover-quasi-compact-support function *-algebra
    under the frozen topological-support and fibre-family conventions;

GLOB-FIBRE-FAMILY-ACT-GRPD-p-a
  = author-defined range-fibre Radon/full-support/continuity/left-invariance
    record on the exact global function domain;

UNIT-REG-ACT-GRPD-p-a
  = author-defined source-fibre/inversion-measure regular representation;

HOPEN-PATCH-ACT-GRPD-p-a
  = diagnostic span generated from Hausdorff open arrow patches;

GLOB-FULL-COMP-ACT-GRPD-p-a
  = author-defined universal completion transported only after an algebraic
    *-isomorphism is proved;

GLOB-RED-COMP-ACT-GRPD-p-a
  = author-defined completion under the explicitly proved unit-regular norm;

STD-CIRCLE-GRPD-p-PROXY
  = ordinary-circle transformation groupoid and its standard crossed product.
```

No record may serialize a standard proxy theorem as an actual theorem. No
record may use an unqualified `groupoid C*` label until the exact literature
hypotheses and function convention pass.

## 4. Frozen groupoid and analytic conventions

- Right action notation: `x dot t`.
- Range/source: `r(x,t)=x`, `s(x,t)=x dot t`.
- Product: `(x,t)(x dot t,u)=(x,t+u)`.
- Inverse: `(x,t)^{-1}=(x dot t,-t)`.
- Arrow topology: actual indiscrete unit topology times usual `R`.
- `quasi-compact` means only the open-cover finite-subcover property.
- Global support is closure of the nonzero locus in the exact arrow topology;
  `GLOB-QC` requires this support to be open-cover quasi-compact.
- `C_c^HOp` is a raw-function span of zero-extensions from Hausdorff open
  patches; those extensions are not presumed globally continuous.
- Range-fibre measure: Lebesgue `dt` under `t -> (x,t)`.
- Convolution and involution are derived from the above convention, not chosen
  to match a desired group formula.
- `G_x=s^{-1}(x)`, `lambda_x=inv_*lambda^x`,
  `vartheta_x(t)=(x dot (-t),t)`, and the `Ind_x` formula in the amended
  protocol own the regular norm. The unitary coordinate map is frozen by
  `(U_x xi)(t)=xi(vartheta_x(t))` from `H_x` to `L^2(R,dt)`.
- Full norm is transported from the usual group `C^*(R)` norm; reduced norm is
  the supremum over the named `Ind_x`; neither is an abstract all-algebraic-
  representation norm or a standard actual-groupoid norm.
- Fourier convention is `integral g(t)exp(-it xi)dt`; full=reduced may use
  only amenability of the group `R` after source verification.
- Fixed orbit only: no packet, prime coproduct, or full suspension promotion.

## 5. Proxy lock

For each orbit choose `x_{p,a}^0` and freeze
`theta_{p,a}([r])=x_{p,a}^0 dot r`, so
`theta([r]) dot t=theta([r+t])`; put `beta=theta^{-1}`. The induced
set-groupoid isomorphism is
`J(x,t)=(beta(x),t):G_act->G_std`. Its candidate continuous inverse and the
contravariant function map `I(f)=f o J^{-1}` are named separately. The proxy
still equips the orbit with the ordinary circle topology. Its normalized Haar
probability is `mu_p`, and the frozen crossed-product convention is
`alpha_t(h)([r])=h([r+t])`. No completion map
is included without a boundedness/isometry theorem, and no proxy
Morita/isomorphism result receives actual-source topology credit.

## 6. Frozen theorem and decision IDs

Active targets are exactly `P11-1`--`P11-10` in `research_protocol.md`.
`T0`--`T7` remain reserved same-object certificate names.

Primary scoped verdicts:

```text
CONFIRM_CONVOLUTION_COLLAPSE
CONFIRM_CONVENTION_SPLIT
SPLIT
REFUTE
NOT_TESTABLE
```

`CONFIRM_CONVOLUTION_COLLAPSE` requires P11-1--P11-5. The stronger
`CONFIRM_CONVENTION_SPLIT` additionally requires P11-6--P11-8 and exact proxy
boundaries. Neither verdict grants a standard groupoid `C*` theorem.

Standalone-paper status additionally requires the Phase-2 bounded novelty
ledger and exact convention/proxy package gate. Failure preserves a correct
technical theorem but changes the release format to a technical note or merge.

## 7. Route ceiling

No owner is pre-certified. Design ceiling:

```text
ACT-GRPD-p-a: source host relation only; immutable earlier Route record not reissued
GLOB-QC concrete / abstract / transported completions: separately evaluated,
  with no analytic-arithmetic A0 inheritance and likely A1_FAIL if action,
  p, and log p disappear
HOPEN-PATCH: diagnostic only
STD proxy: MODELING_CHOICE
all new owners: A2/A3/A4_FAIL absent a new same-object result
Route B: false; no Route-B YAML
```

## 8. Frozen exclusions

- standard-circle topology on the actual unit;
- packet/global source completion;
- untyped non-Hausdorff `C_c` or groupoid `C*` notation;
- Radon measure on the whole arrow space without a definition;
- determinant, analytic continuation, functional equation, zero matching;
- Hilbert--Pólya, self-adjoint spectral host, or Route B;
- target-zero data, fitting, or random search.

## 9. Lock integrity

The initial bytes received three independent REVISE verdicts. Amendment v1 is
recorded in `notes/phase1_design_amendment.md`. It has no Phase-1 PASS status
until all three reviewers close on the exact amended tuple.
