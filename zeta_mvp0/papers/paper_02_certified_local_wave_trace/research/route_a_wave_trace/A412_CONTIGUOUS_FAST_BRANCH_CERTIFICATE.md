# A4.12 — Validated contiguous fast Lyapunov branch

## Theorem (local-box computer-assisted form)

Fix

\[
 a=\frac{51}{50},
 \qquad
 0\leq\epsilon\leq0.101,
 \qquad
 \delta=\epsilon^2,
\]

and let $K_\epsilon$ be the normalized Hamiltonian in the frozen
R401-VAL protocol.  There is a real-analytic family

\[
 \epsilon\longmapsto
 \gamma_\epsilon=(Q_-(\epsilon),Q_+(\epsilon),
 P_-(\epsilon),0;T(\epsilon))
\]

of nonconstant primitive periodic orbits on $K_\epsilon=1$, satisfying

\[
 0.66<T(\epsilon)<0.67.
\]

For every primary slab $E_i$ and every $\epsilon\in E_i$, this return is
the unique zero in its frozen root box $X_i$ from
`R401_VAL_L1_FINAL_PLAN_V2.json`.  On every adjacent parameter overlap,
the two primary representatives are the same zero inside the corresponding
guarded bridge hull.  At $\epsilon=0$ the family is anchored to the exact
fast harmonic orbit

\[
 \gamma_0=
 \left(0,\frac{\sqrt2}{\omega_+},0,0;
             \frac1{\sqrt{\lambda_+}}\right),
 \qquad \omega_+=2\pi\sqrt{\lambda_+}.
\]

The uniqueness asserted here is local to the displayed boxes.  This theorem
does not exclude a second return elsewhere on the energy shell.

## Frozen return equations

For

\[
 x=(Q_-,Q_+,P_-,T),
 \qquad z_0(x)=(Q_-,Q_+,P_-,0),
\]

the validated system is

\[
 F(x,\epsilon)=
 \begin{pmatrix}
 K_\epsilon(z_0)-1\\
 Q_-(T)-Q_-\\
 P_-(T)-P_-\\
 P_+(T)
 \end{pmatrix}=0.
\]

Every primary and bridge job constructs a parameterized Krawczyk operator

\[
 \mathcal K(X,E)=
 \bar x-CF(\bar x,E)
 +\bigl(I-C[D_xF(X,E)]\bigr)(X-\bar x).
\]

The corrected energy row is evaluated on the full box $X$.  In particular,

\[
 [D_xF(X,E)]_{0,2}=X_{P_-},
\]

not the zero derivative obtained by evaluating only at the midpoint
$P_-=0$.

For each of the 202 production jobs, CAPD proves both

\[
 \mathcal K(X,E)\Subset X,
 \qquad
 \left\|I-C[D_xF(X,E)]\right\|_\infty<1.
\]

Thus, for each fixed $\epsilon$ in the parameter slab, the Krawczyk map is a
strict self-map and contraction.  It has exactly one zero in $X$, and the
root derivative is nonsingular.

## Recovery of the full return

The fourth return equation $Q_+(T)=Q_+(0)$ is not imposed directly.  Every
certificate instead proves

\[
 Q_+(0),Q_+(T)\in[0.10,0.18]
\]

and, uniformly on the connecting interval,

\[
 \partial_{Q_+}K_\epsilon>0.
\]

At a zero of $F$, the other position, both momenta, and the energy agree at
the two endpoints.  Exact Hamiltonian energy conservation and strict
monotonicity in $Q_+$ therefore force

\[
 Q_+(T)=Q_+(0).
\]

Consequently the certified zero is a full-state periodic return, not merely
a zero of a reduced projection.  The smallest validated phase-slope lower
bound in the complete production archive is

\[
 8.955040964476345\ldots>0.
\]

## One branch, not 51 unrelated solutions

The final plan has 51 primary parameter slabs whose union is exactly
$[0,0.101]$.  For adjacent primary jobs, let

\[
 B_i=E_i\cap E_{i+1},
 \qquad
 Y_i=\operatorname{hull}(X_i\cup X_{i+1})
       +[-10^{-18},10^{-18}]^4.
\]

There are 50 bridge certificates.  For $\epsilon\in B_i$, the two primary
zeros lie in $Y_i$, while the bridge Krawczyk certificate proves that
$Y_i$ has only one zero.  They therefore coincide.  Induction through the
50 overlaps identifies all primary pieces.

The padding is a pre-frozen rational construction guard, not a numerical
acceptance tolerance.  The independent checker verifies exact containment
of the actual printed MPFR primary boxes in the actual printed bridge boxes.

Since $F$ is analytic through $\epsilon=0$ (using the analytic `exprel`
extension) and $D_xF$ is nonsingular along the chain, the analytic implicit
function theorem upgrades the glued pointwise solutions to one real-analytic
branch.  The exact epsilon-zero solution identifies it as the fast Lyapunov
continuation.

## Primitivity

The exact blow-up $q=\epsilon Q$, $p=\epsilon P$ used to define
$K_\epsilon$ preserves physical time in Hamilton's equations.  Period bounds
proved for the original energy shell therefore apply to the normalized
return without an additional time-rescaling factor.

The root boxes give $T<0.67$.  If a certified return for $\epsilon>0$
were a repetition, its primitive period would be at most

\[
 \frac{T}{2}<0.335.
\]

A4.11b proves that every nonconstant warped orbit throughout
$0<\delta\le0.010201$ has period greater than $0.60$, a contradiction.
At $\epsilon=0$, primitivity follows directly from the exact fast harmonic
period.  Hence the complete branch is primitive.

## Certificate accounting

The accepted archive is `results/r401_val_l1_branch/` and reports
`PASS_CONTIGUOUS_LOCAL_BRANCH` with `final_status: null`.

- 51 primary jobs and 50 bridge jobs at 128 MPFR bits;
- the same 101 jobs at 256 MPFR bits;
- 202/202 validated-flow/Krawczyk jobs pass;
- 202/202 independent exact-rational Krawczyk replays pass;
- 3973 aggregate independent checks pass;
- every 128/256 root box and printed Krawczyk image overlaps its replica;
- all 100 actual bridge-containment checks pass.

The minimum strict Krawczyk margins are

\[
 9.323437289176983\times10^{-6}\quad(128\text{ bit}),
 \qquad
 9.328825112522987\times10^{-6}\quad(256\text{ bit}).
\]

The maximum certified contraction bounds are

\[
 0.033989409766443\quad(128\text{ bit}),
 \qquad
 0.029013314518191\quad(256\text{ bit}).
\]

The checker independently reconstructs $C$, $I-CJ$, and the Krawczyk image
from exact rational interpretations of the printed decimal endpoints.  It
does not perform a second ODE integration; the validated flow enclosures
remain supplied by the pinned CAPD computation.

## Audit history and exact boundary

Two failed predecessors are retained rather than overwritten.

1. `r401_val_local_slab_smoke.attempt0-invalid-energy-jacobian` used the
   midpoint energy gradient and therefore did not enclose $D_xF(X,E)$.
2. `r401_val_l1_branch.attempt1-invalid-bridge-rounding` passed all local
   Krawczyk jobs, but exact unpadded decimal hulls did not contain every
   separately rounded printed primary box.  V2 froze the rational bridge
   padding and reran all jobs; it did not apply a post-hoc tolerance.

What A4.12 now supplies is a validated, primitive, full-return fast branch
through the complete target energy parameter band.  What remains open is:

- exclusion of roots outside the local boxes;
- the complete local root-complement tree;
- the global shell return cover on $0.60<T<0.75$;
- the transverse determinant/nondegeneracy cover;
- promotion of $\delta_{\rm tr}$ beyond $0.01$;
- every endogenous prime-power, Hilbert--Polya, zeta-zero, or RH claim.

Thus A4.12 is a substantial theorem-domain component, but not the final
R401-VAL theorem-domain certificate and not the arithmetic $P_0$ bridge.
