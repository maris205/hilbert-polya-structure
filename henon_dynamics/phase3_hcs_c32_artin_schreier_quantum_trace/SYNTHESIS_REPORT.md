# HCS-C32 Phase 3 synthesis report

Date: 2026-08-12 UTC

Decision: `STOP_MORSE_LOCAL_HILL_GATE; GO_DISCRIMINANT_FAMILY_GATE`

Manuscript status: `HOLD_PENDING_CHECKPOINT_2`

## 1. Material passport

| Field | Value |
|---|---|
| Candidate | `HCS-C32-MORSE-LOCAL-HILL-GATE` |
| Base dynamics | (H_6(q,p)=(1-6q^2-p,q)) |
| Deformation class | area-preserving quadratic Hénon maps |
| Clock | genuine chronological period (n) |
| Arithmetic setting | (mathbb F_p), registered (p\le61), (p>3) |
| Analytic object | local Artin--Schreier vanishing cycles and local Fourier transform |
| Exact evidence | primitive (p=61,n=5) collision plus (operatorname{GL}_5) congruence |
| Theorem evidence | henselian Morse normal form and quadratic local Fourier classification |
| Discovery status | post-pilot witness, not preregistered prediction |
| AI assistance | disclosed; source and code checks retained |

## 2. Claim-intent manifest

The Phase-3 question was deliberately narrower than the Phase-2 construction:

> Does the standard good-prime Morse-local factor retain the actual Hénon
> Hill determinant, rather than only its quadratic square class?

The intended outcomes were symmetric:

- `GO`: exhibit a source-certified local invariant that separates equal-value,
  equal-square-class Hénon critical points;
- `STOP`: prove the local object is quadratic-classified and find an exact
  Hénon collision with unequal Hill values.

The second outcome occurred.

## 3. Evidence convergence map

| Evidence stream | Independent content | Result |
|---|---|---|
| Hénon dynamics | critical equations reproduce the chronological recurrence | PASS |
| Discrete variational theory | Hessian determinant equals signed Hill determinant | PASS; generic theorem, exact specialization |
| Henselian singularity theory | nondegenerate germ reduces to critical value plus quadratic form | PASS |
| Local Fourier theory | quadratic local factor is Kummer/Gauss data | PASS |
| Exact finite-field scan | two primitive period-five classes share local invariants | PASS |
| Explicit form isometry | (C^{\mathsf T}B_AC=B_B), (det C\ne0) | PASS |
| Independent replay | permutation-cycle scan, independent determinant code | PASS |
| Global Artin--Schreier cohomology | equality or collapse of full global object | NOT TESTED |
| Hilbert--Pólya structure | canonical self-adjoint operator or Riemann factor | NOT ESTABLISHED |

The theorem and experiment meet at exactly one interface: the matrix
congruence turns the finite-field collision into an isomorphism of local
function germs, so the local sheaf conclusion does not rely on a heuristic
stationary-phase decomposition.

## 4. The decisive obstruction

At (p=61,n=5), two distinct primitive Hénon orbit classes have

\[
\Phi_5=45,
\qquad
\chi_{61}(\det D^2\Phi_5)=-1,
\]

but their Hill values are (44) and (7).  Their Hessians are explicitly
congruent over (mathbb F_{61}).  The henselian Morse lemma therefore makes
the complete unframed local function germs isomorphic.

The obstruction is conceptual, not merely numerical:

\[
\det(C^{\mathsf T}BC)=\det(C)^2\det(B).
\]

An intrinsic quadratic germ cannot remember which determinant representative
was written in a chosen coordinate volume; it remembers the discriminant
class.  The Hénon coordinates do provide a preferred external framing, but
the standard local vanishing-cycle representation forgets that framing.

## 5. Tension inventory and resolution

### Tension A: the Hill identity seems to inject stability into cohomology

Phase 2 correctly observed

\[
\det D^2\Phi_n=(-1)^{n+1}\det(I-DH_6^n).
\]

That identity does inject the Hill value into the coordinate Hessian.  It does
not follow that an unframed local sheaf retains the entire coordinate
determinant.  Phase 3 resolves the tension by separating coordinate data from
quadratic-form isometry data.

### Tension B: purity produces unit-circle spectra

The global Artin--Schreier group is pure, and the finite kernel is unitary.
Neither statement makes individual local Morse factors multiplier-complete.
Purity remains valid, but it is generic and does not reverse the local loss of
information.

### Tension C: finite stationary phase versus infinity

The finite Morse ranks may saturate the global rank under additional
cohomological-tameness and stationary-phase hypotheses.  Those hypotheses are
not proved in this phase.  The release therefore retains infinity as an open
global contribution rather than silently setting it to zero.

### Tension D: the witness was found before the protocol

The collision cannot be advertised as a preregistered prediction.  Its use is
theorem construction, not significance testing: every equality is exact, and
the frozen scan is independently replayed.  The 80-cell uniqueness statement
remains descriptive and is never assigned a (p)-value.

## 6. Literature synthesis and novelty boundary

| Component | Literature status | Phase-3 use |
|---|---|---|
| Henselian Morse lemma | established, SGA 7 II | theorem bridge |
| Quadratic vanishing cycles | established, SGA 7 II and Fu | theorem bridge |
| Local Fourier/Kummer transform | established, Laumon | convention and representation bridge |
| Hasse--Davenport | established, SGA 4 1/2 | extension convention; not needed for the explicit congruence |
| Discrete Hill formula | established, Bolotin--Treschev | Hénon specialization |
| Hénon finite-field collision | no direct duplicate found within the bounded search | exact new specialization |
| Local no-recovery corollary for the two Hénon cycles | derived here | scoped obstruction |

The general mathematics is not new.  The defensible delta is the explicit
Hénon collision and the precise no-recovery consequence for the proposed
Morse-local Hill bridge.  This is a meaningful project result, but not by
itself a broad new stationary-phase theorem.

## 7. Route-A evaluation

The exact orbit clock is genuine and the obstruction is intrinsic.  However,
the Phase-3 output is not a positive Route-A candidate:

- A1: at most `A1_WEAK`; real chronological periodic orbits exist, but there
  is no prime correspondence or global coefficient law;
- A2: `A2_FAIL`; no canonical global Fredholm/dynamical determinant is built;
- A3: `A3_FAIL`; purity is finite-field and generic, not a Riemann critical-line
  theorem;
- A4: `A4_FORMAL_HINT`; finite unitary kernels exist, but there is no single
  canonical Hilbert--Pólya operator.

The machine certificate conservatively records `NOT_TESTABLE` because no
formal Route-A candidate package is being submitted.  Route B remains
unauthorized.

## 8. What died and what survived

### Route stopped

Recovering the full value (det(I-DH_6^n)) from each standard good-prime
Morse-local vanishing-cycle factor is impossible.

### Route retained

The fixed global Artin--Schreier kernel, the two-axis trace identity, and the
global critical-value geometry remain mathematically valid.  Their generic
rank and purity are not evidence of arithmetic specificity, but they can host
new global monodromy.

### Highest-value escape

The strongest next object is not another isolated Morse point.  It is the
one-parameter discriminant family

\[
H_a(q,p)=(1-aq^2-p,q),
\qquad
S_a(q,Q)=qQ-q+\frac a3q^3,
\]

with the cyclic critical equations and the degeneracy equation

\[
\det D^2\Phi_{n,a}=0.
\]

By Hill's formula this is the parabolic periodic-orbit locus
(det(I-DH_a^n)=0).  Its discriminant polynomial, braid/Galois monodromy,
and vanishing cycles around collisions are genuinely global-in-parameter and
are not classified by the separate Morse germs.

## 9. Recommended next gate

`HCS-C33-HENON-DISCRIMINANT-MONODROMY-GATE`

The first large experiment should:

1. eliminate the period-(n) critical equations together with the Hessian
   determinant for (2\le n\le6), preserving chronological cyclic structure;
2. factor the resulting discriminant in ((a,c)) or a carefully chosen
   one-parameter slice;
3. compute exact local ramification and permutation monodromy of critical
   values;
4. test whether this monodromy distinguishes orbit stability data erased by
   the Morse-local quotient;
5. stop immediately if the discriminant reduces to a generic degree-only
   invariant or repeats an existing Hénon resultant project.

This is a larger door than extending the prime scan: it changes the invariant,
not just the sample size.

## 10. Manuscript recommendation

Do not yet promote this phase alone into a full Hilbert--Pólya paper.  Preserve
it as a theorem-grade negative section and exact certificate.  A manuscript
becomes more compelling if the next discriminant-family gate either produces
a nontrivial global monodromy theorem or proves a second, genuinely global
obstruction.

