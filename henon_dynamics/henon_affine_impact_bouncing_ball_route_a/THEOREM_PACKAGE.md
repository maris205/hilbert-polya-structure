# Theorem package

Freeze `g>0`, `0<=r<=1`, and `J>=0`. In the interior `q>0`,
`q'=v`, `v'=-g`. The guard is `q=0,v^-<0`, with reset
`v^+=r(-v^-)+J`. Adjoin a separate absorbing rest state `R` at
`(q,v)=(0,0)`; the guard excludes zero incoming velocity.

## Main theorem

1. From an interior state `(q_0,v_0)`, the next impact time and incoming
   speed magnitude are `tau_0=(v_0+sqrt(v_0^2+2gq_0))/g` and
   `w_0=sqrt(v_0^2+2gq_0)`. The outgoing speed is `u_0=r w_0+J`.
2. A positive outgoing speed `u` generates one physical flight of duration
   `tau(u)=2u/g`, followed by the event map `P(u)=r u+J`.
3. For `r!=1`, with `u_*=J/(1-r)`,
   `u_n=u_*+r^n(u_0-u_*)` and
   `t_n=(2/g)[n u_*+(u_0-u_*)(1-r^n)/(1-r)]`, where `t_n` is the
   time after `n` flights. For `r=1`, `u_n=u_0+nJ` and
   `t_n=(2/g)[n u_0+J n(n-1)/2]`.
4. If `J=0,0<r<1`, positive initial speeds form a Zeno sequence with
   accumulation time `2u_0/[g(1-r)]`; continuation requires the explicitly
   adjoined rest state. The edge `r=0,J=0` has at most one positive-duration
   flight and then sticks at rest, so it is not an infinite Zeno sequence. If
   `J>0,0<=r<1`, there is one positive forced cycle
   at `u_*=J/(1-r)`, of physical period `T_*=2u_*/g), and multiplier
   `r`; all positive speeds converge to it and event times diverge.
5. If `r=1,J=0`, every `u>0` is an elastic periodic flight of period
   `2u/g`; `u=0` is rest, not a periodic orbit. If `r=1,J>0`,
   speeds grow as `u_0+nJ`, event times grow quadratically, and no physical
   flight is periodic. The `r=0` edges are included: one-step forcing for
   `J>0`, and first-impact sticking for `J=0`.
6. On the outgoing section, the transverse event multiplier is exactly
   `P'(u)=r`. No full two-dimensional saltation matrix is asserted.
7. Define the regular positive-flight section as `S_+=(0,infinity)`. On
   `S_+`, the physical event-map series is `zeta_phys=1/(1-z)` when
   `J>0,r<1`, and is the empty series `1` when `J=0,r<1` (including the
   one-step sticking edge `r=0`). If one instead closes the section to
   `[0,infinity)`, the affine map has the formal boundary series
   `zeta_aff=1/(1-z)` for `J=0,r<1`, because its sole fixed point is `u=0`;
   this point is rest and not a physical flight. For `r=1,J=0` the fixed set
   is a continuum and both cardinality series are undefined. For `r=1,J>0`
   there are no fixed points and the empty finite-count series is `1`. These
   are event-map statements, not physical-flow zeta statements.

## Proof ledger

The quadratic flight equation gives the first-impact formulas. Symmetry of
constant acceleration gives flight duration `2u/g`, and the reset law gives
the affine map. Iterating an affine map yields the displayed geometric or
arithmetic sequences; summing them gives the cumulative times. The Zeno sum is
geometric precisely when `J=0,0<r<1`; at `r=0` the sequence reaches zero after
one flight and the rest convention stops it. Solving `u=r u+J` gives the unique
positive fixed speed when `J>0,r<1`; contraction gives convergence and
`P'(u)=r`. Identity and translation boundaries follow directly. The
zero-speed point is assigned to the rest state, which prevents a formal
zero-time event loop from being counted as a physical cycle.
