# R401-VAL-L1-V2: contiguous validated fast-orbit branch

Status: **frozen protocol candidate; no result is licensed until both
precisions and the independent checker pass**.

This protocol extends the corrected R401-VAL-V2 local certificate from one
endpoint slab to a connected chain covering

\[
  0\leq \epsilon\leq 0.101.
\]

It is deliberately a local-branch result.  It neither excludes periodic
orbits outside the listed boxes nor completes the root-complement and global
phase-space covers required by `PASS_ENDPOINT` or `PASS_FULL`.

## 1. Frozen reduced return system

Let

\[
 W_\epsilon(q_1,q_2)
 =(-c q_1-q_2-a\epsilon q_1^2,q_1),
 \qquad a=\frac{51}{50},\qquad
 c=2\left(\sqrt{1+a}-1\right),
\]

and use the analytic extension

\[
 K_\epsilon(q,p)
 =\frac{|p|^2}{2}
  +2\pi^2|W_\epsilon(q)|^2
    \operatorname{exprel}\!\left(\pi\epsilon^2|W_\epsilon(q)|^2\right),
 \qquad \operatorname{exprel}(s)=\frac{e^s-1}{s}.
\]

The orthonormal matrix `O` is reconstructed by outward interval arithmetic
from the ordered eigenvectors of the quadratic metric, with the signs fixed
in the source.  In normal coordinates, write the unknown as

\[
 x=(Q_-,Q_+,P_-,T),\qquad
 z_0(x)=(Q_-,Q_+,P_-,0).
\]

The CAPD flow integrates the scaled autonomous system over `tau in [0,1]`,
so its terminal state is exactly the time-`T` Hamiltonian flow.  The frozen
four-equation residual is

\[
 F(x,\epsilon)=
 \begin{pmatrix}
 K_\epsilon(z_0)-1\\
 Q_-(T)-Q_-\\
 P_-(T)-P_-\\
 P_+(T)
 \end{pmatrix}.
\]

## 2. Primary slabs

`R401_VAL_L1_FINAL_PLAN_V2.json` contains 51 closed parameter slabs `E_i` and
root boxes `X_i`.  Their union is exactly `[0,0.101]`; every adjacent pair
has a nonempty interval overlap.  Floating-point continuation was used only
to propose decimal centers.  A center has no evidentiary force unless the
corresponding interval job passes every gate below.

For each `E_i x X_i`, the producer must compute with CAPD's MPFR-backed C1
Taylor/Lohner flow:

\[
 [F(\bar x_i,E_i)],\qquad [D_xF(X_i,E_i)].
\]

The energy row of the derivative enclosure must be evaluated on the complete
box `X_i`, not at its midpoint.  This explicitly retains
`dK/dP_- = P_-` as an interval.

With the fixed point-interval preconditioner
`C_i = mid(inverse(mid([D_xF])))`, define

\[
 \mathcal K_i
 =\bar x_i-C_i[F(\bar x_i,E_i)]
  +\left(I-C_i[D_xF(X_i,E_i)]\right)(X_i-\bar x_i).
\]

The primary job passes only if all of the following are strict interval
statements:

1. `K_i subset interior(X_i)` componentwise;
2. the interval infinity-norm bound
   `||I-C_i[D_xF(X_i,E_i)]||_infinity < 1`;
3. every entry of `C_i` is internally a degenerate MPFR interval (the two
   printed decimal endpoints may differ in their last digit because CAPD
   formats lower and upper bounds with opposite directed rounding);
4. `Q_+(0)` and the entire CAPD enclosure of `Q_+(T)` lie in `[0.10,0.18]`;
5. `dK_epsilon/dQ_+ > 0` uniformly for
   `Q_- in X_i[0]`, `Q_+ in [0.10,0.18]`, and `epsilon in E_i`.

The first two gates give, for every fixed epsilon in `E_i`, one and only one
zero of `F(.,epsilon)` inside `X_i`.  The last two recover the omitted
`Q_+(T)=Q_+(0)` equation: the exact Hamiltonian flow conserves energy, all
other coordinates agree at a zero of `F`, and energy is strictly increasing
in `Q_+` on the common connected interval.  Thus every certified reduced
zero is a genuine full-state periodic orbit.

The certified periods lie above `0.60`.  Together with the already frozen
analytic exclusion of all nonconstant energy-one returns below `0.60`, a
proper repetition is impossible (a repeated orbit would have primitive
period at most `T/2 < 0.60`).  Hence these are primitive fast orbits.

The first primary box is additionally anchored at the exactly solvable
harmonic endpoint.  At `epsilon=0`, let

\[
 x_0=\left(0,\frac{\sqrt2}{\omega_+},0,
                 \frac1{\sqrt{\lambda_+}}\right),
 \qquad \omega_+=2\pi\sqrt{\lambda_+}.
\]

The quadratic Hamiltonian gives `F(x_0,0)=0` analytically.  The runner and
checker must reconstruct `lambda_+` independently and verify
`x_0 in interior(X_000)`.  This identifies the certified connected family as
the continuation of the fast harmonic Lyapunov orbit, rather than merely an
unnamed local branch.

## 3. Bridge slabs and branch identity

For each adjacent pair `(E_i,X_i)`, `(E_{i+1},X_{i+1})`, the plan contains

\[
 B_i=E_i\cap E_{i+1},\qquad
 Y_i=\operatorname{hull}(X_i\cup X_{i+1})
      +[-10^{-18},10^{-18}]^4.
\]

The rational padding is frozen before the V2 production run.  It is
negligible relative to the `2e-5`--`8e-5` root radii but dominates the final
MPFR decimal-formatting ULP created when primary and bridge boxes are parsed
and constructed separately.  There are 50 such bridge jobs.  Each bridge is
run through the identical
Krawczyk, contraction, and phase-recovery gates on `B_i x Y_i`.

The independent checker must verify from the actual printed MPFR boxes, not
only from the JSON construction rule, that

\[
 X_i^{\rm MP}\cup X_{i+1}^{\rm MP}\subset Y_i^{\rm MP}.
\]

For any epsilon in `B_i`, the two primary zeros then lie in `Y_i`.  The bridge
certificate proves that `Y_i` contains only one zero, so the two primary
zeros coincide.  Induction across all 50 overlaps identifies the 51 primary
families as one connected local branch.  Analyticity of the vector field and
the uniformly nonsingular root derivative give the corresponding local
analytic continuation in epsilon.

This argument proves uniqueness only in the displayed primary boxes and
bridge hulls.  It says nothing about roots in their complement.

## 4. Arithmetic and reproducibility gates

- CAPD commit: `731079217a9254ea2948d742df2b170895effe7f`.
- CAPD must be built with multiprecision enabled and compiler flags must
  include MPFR, GMP, and directed-rounding support.
- Taylor order: 24.
- Required precisions: 128 and 256 MPFR bits.
- Tolerances: `1e-30` at 128 bits and `1e-60` at 256 bits.
- Required jobs per precision: 51 primary plus 50 bridge jobs.
- Every one of the 202 jobs must exit successfully and print all strict gates
  as true.
- Every primary and bridge period box must satisfy
  `0.66 < T < 0.67`, `T < 0.68`, and `2T > 0.75`.
- The two precision runs must overlap componentwise for every certified root
  box and Krawczyk image; disagreement is a hard failure.
- The independent checker must verify frozen hashes, plan coverage, guarded
  bridge-hull construction, and actual MPFR box containment; parse every
  transcript; recompute the Krawczyk
  arithmetic from printed `X`, `x_bar`, `F`, `J`, and `C` using exact rational
  decimal endpoints, and replay all strict inequalities.

## 5. Status namespace

If and only if every production and independent-check gate passes, the
milestone may be recorded as

`PASS_CONTIGUOUS_LOCAL_BRANCH`.

The result manifest must retain `final_status: null`.  The following are not
authorized by this protocol:

- `PASS_ENDPOINT`;
- `PASS_FULL`;
- a promoted value of `delta_tr`;
- global uniqueness on the energy shell;
- any Hilbert--Polya, Riemann-hypothesis, prime-power, or zeta-zero claim.

## 6. Invalid predecessor handling

The original L0 archive used a midpoint energy gradient in the first
Krawczyk Jacobian row.  Its source hash was
`663287f629457d81f716a1a56a032c660bd91a79a1ae7aa77bc980483819c929`.
That archive must be preserved under an explicit `attempt0-invalid-*` name
and must not appear as a passing proof milestone.  Only a rerun against the
corrected frozen source may replace it.

The first L1 production attempt used exact unpadded decimal hulls.  Although
all 202 validated jobs and all 202 independent Krawczyk replays passed, 89
printed coordinate comparisons missed containment by roughly one final
formatting ULP after separate outward constructions.  That attempt is
preserved as `r401_val_l1_branch.attempt1-invalid-bridge-rounding` and is not
licensed.  V2 changes the plan before rerunning; it does not introduce a
post-hoc comparison tolerance.
