# R401-VAL-L1-MG-V2 — local-branch monodromy-gap protocol

Status: prospectively re-frozen before the V2 derived rerun after an audit of
the report's decimal rendering.  The numerical threshold is inherited
verbatim from hard gate 3 of the earlier frozen R401-VAL protocol, not
selected from the exploratory trace readout.  The exact-rational computation
is unchanged; V2 makes every human-readable decimal bound directionally
rigorous and independently replayable.

## Purpose

The accepted L1-V2 archive certifies one primitive periodic orbit in every
local primary box and identifies those orbits as one branch.  Every CAPD
transcript also contains a validated enclosure of the full state derivative

\[
 M_\epsilon=D_z\Phi_\epsilon^{T(\epsilon)}(z_\epsilon)
 \in\operatorname{Sp}(4,\mathbb R).
\]

This derived protocol asks only whether those already frozen enclosures prove
the pre-registered local nondegeneracy gate

\[
 D_M=4-\operatorname{tr}M_\epsilon>3
\]

uniformly on the certified branch.  It does not attempt the independent
event-projected Poincare construction or the narrow Taylor-model identity
residual required by the final R401-VAL protocol.

## Structural identity

Use the invariant quotient rather than assuming diagonalizability at the unit
multiplier.  At a certified periodic point $z$, set

\[
 V=T_z\mathbb R^4,
 \qquad
 \alpha=dK_\epsilon(z),
 \qquad
 v=X_{K_\epsilon}(z),
 \qquad
 L=\operatorname{span}\{v\}.
\]

Energy conservation and flow covariance give

\[
 \alpha\circ M_\epsilon=\alpha,
 \qquad
 M_\epsilon v=v,
 \qquad
 L\subset\ker\alpha.
\]

Thus

\[
 0\subset L\subset\ker\alpha\subset V
\]

is an invariant flag.  The induced maps on $L$ and on
$V/\ker\alpha$ are both the identity.  The induced map on the symplectic
quotient $\ker\alpha/L$ is precisely the derivative $D\Pi_\epsilon$ of the
two-dimensional energy-section Poincare return.  Therefore, without any
semisimplicity assumption and also when the unit multiplier has algebraic
multiplicity four,

\[
 \chi_{M_\epsilon}(t)
 =(t-1)^2\chi_{D\Pi_\epsilon}(t),
 \qquad
 \operatorname{tr}M_\epsilon
 =2+\operatorname{tr}D\Pi_\epsilon.
\]

The quotient map is symplectic, hence
$\det D\Pi_\epsilon=1$.  Consequently

\[
 \det(I-D\Pi_\epsilon)
 =2-\operatorname{tr}D\Pi_\epsilon
 =4-\operatorname{tr}M_\epsilon.
\]

The L1-V2 certificate supplies a stronger event-section statement than
non-equilibrium alone.  Its frozen `phase_gradient_qplus` gate proves

\[
 \partial_{Q_+}K_\epsilon>0
\]

at both endpoints of every certified return and uniformly on the connecting
phase interval, while the event section is $P_+=0$.  Consequently

\[
 dK_\epsilon\ne0,
 \qquad
 \dot P_+=-\partial_{Q_+}K_\epsilon\ne0.
\]

Thus $K_\epsilon=1$ is a regular energy surface at the orbit and the
$P_+=0$ event section is transverse to the Hamiltonian flow.  This is the
regularity/transversality input needed to identify the two nontrivial
multipliers of $M_\epsilon$ with the derivative of the local energy-section
Poincare map.  The analyzer and checker must reparse the phase-slope interval
from every frozen transcript and require its lower endpoint to be positive;
they may not infer this gate merely from $Q_+>0.1$.

## Frozen arithmetic

For every one of the 202 accepted transcripts:

1. parse the 36 intervals of `monodromy_box` as exact rational decimal
   endpoints;
2. take indices $0,7,14,21$, the diagonal of the physical state
   four-by-four block; the $\epsilon$ and period coordinates are augmented
   constants and are not part of $M_\epsilon$;
3. form outward-exactly
   \[
   [D_M]=
   \left[4-\sum_{j=0}^3 M_{jj}^{+},
         4-\sum_{j=0}^3 M_{jj}^{-}\right];
   \]
4. require the lower endpoint to be strictly greater than 3;
5. require the 128-bit and 256-bit intervals for each job ID to intersect;
6. verify every accepted transcript hash through the L1-V2 manifest and
   verify the accepted independent checker and postcheck statuses.

## Directed decimal rendering

Exact numerator/denominator pairs are authoritative.  Every structured
fraction payload must retain them.  Human-readable decimal enclosures use
exactly 18 places after the decimal point and must be formed without a
binary floating-point conversion.  For an exact fraction $x=n/d$, let
$s=10^{18}$.  The stored decimal endpoints are

\[
 x_{\rm floor}=\frac{\lfloor sn/d\rfloor}{s},
 \qquad
 x_{\rm ceil}=\frac{\lceil sn/d\rceil}{s}.
\]

Any displayed lower bound must use `decimal_floor`; any displayed upper
bound, including an upper bound on an interval width, must use
`decimal_ceil`.  The no-analyzer-import checker must independently reconstruct
both fixed-point strings from the exact fraction, verify

\[
 x_{\rm floor}\le x\le x_{\rm ceil},
\]

verify that the two endpoints differ by at most one $10^{-18}$ grid unit,
and check that the Markdown report uses the correct directed member together
with the exact numerator and denominator.

The analyzer and a second no-analyzer-import checker must independently
perform this exact-rational calculation.  A successful derived archive uses

`protocol_id: R401-VAL-L1-MG-V2`

`milestone_status: PASS_LOCAL_MONODROMY_GAP`

and retains `final_status: null`.

## Claim boundary

Success proves the transverse determinant bound $D>3$ only on the already
certified local fast branch.  It does not:

- exclude other roots or other periodic orbits;
- provide the independent $D_\Pi$ event-projection computation;
- meet the $2^{-30}$ Taylor-remainder or $2^{-28}$ residual gates;
- close the root-complement, phase, or global cover trees;
- promote $\delta_{\rm tr}$, P0, Hilbert--Polya, zeta zeros, or RH.
