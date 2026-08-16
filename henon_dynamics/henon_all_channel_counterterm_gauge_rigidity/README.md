# HCS-P74: All-channel counterterm gauge rigidity

HCS-P72 makes the later relative packet/Lind channels exact:

    log C_rel(t)=H_rel(1-sqrt(2)t)-sum_(m>=2)c_m Phi(t^m),
    Phi(x)=2x/(1-2x^2),
    c_m=(1/m) product_(p|m,p odd)(1-p).

P74 classifies exponential multipliers

    W_(d,G)(t)=exp(sum_(m>=2)d_m Phi(t^m)+G(t)).

If `G` is holomorphic on the unit disk and the channel series is normally
convergent on the P72 punctured disk, removability of every channel
singularity forces `d_m=c_m` for every `m>=2`.  The coefficient vector is
rigid, but the result is not absolutely unique: after cancellation the
remaining freedom is exactly multiplication by a nowhere-zero holomorphic
function `exp(G)`.

At the source negative boundary `w=1+sqrt(2)t=0`, a multiplier
`w^beta exp(-a/w)` gives a nonzero holomorphic extension only for
`(a,beta)=(3/4,1/2)`.  For a general holomorphic gauge
`A(t)=exp(G(t))`, the exact remaining residual is
`exp(-3/2)exp(G(t))=exp(-3/2)A(t)`.  In the distinguished `G=0` gauge this
reduces to the constant `exp(-3/2)`.

Two order-independent primary-factor conventions expose the gauge issue.
Genus `m-1` has `G=0` and cancels the complete channel sector.  After the
forced source factor and scalar normalization `exp(3/2)`, the full relative
object is identically one.  Genus `m` preserves the first source monomial
and leaves

    exp(-2 sum_(m>=2)c_m t^m),

a nonconstant nowhere-zero holomorphic residual.  A finite Taylor jet never
chooses between such gauges.

**Status:** channel coefficient rigidity, source-pair rigidity, gauge-torsor
classification, the two primary regularizations, and finite-jet
nonuniqueness are PROVED.  An absolute canonical normalization, operator
ownership, rational-prime semantics, and Route B remain OPEN/UNAUTHORIZED.

Reproduce with `bash code/run_c74.sh`; the substantive manuscript is
`paper/paper.pdf`.
