# Narrative report — C122

The map augments a quadratic Hénon recurrence by allowing its additive
parameter to evolve.  The update is neither a passive constant nor a delayed
coordinate: it contracts by one half and receives present-state feedback.
Despite that coupling, the full three-dimensional map has a polynomial inverse
and constant volume contraction.

The exact two-cycle was chosen as a falsifiable witness.  Its two Hénon states
force the adaptive coordinate to jump from `-3` to `1` and back.  Solving the
two feedback equations fixes gain `3` and offset `-1/2`; removing or perturbing
the gain breaks closure.  The direct three-dimensional monodromy is recorded
without rebranding it as a transfer operator.

This yields a new adaptive-feedback dynamics subtype and exact intrinsic
low-period evidence, but only `A1_WEAK`: no prime-like target correspondence
is present.  The local monodromy has neither a target-divisor match nor an
analytic bridge, so A2 and A3 fail.  The negative boundary is part of the
result.
