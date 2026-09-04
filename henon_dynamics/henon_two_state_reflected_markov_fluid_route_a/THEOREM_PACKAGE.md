# Theorem package: two-state reflected Markov fluid

## Core model

Let `J` be the continuous-time chain on `{0,1}` with `q01=a` and `q10=b`.  Let `r0=-d`, `r1=c`, and let
\[
Y_t=X_0+\int_0^t r_{J_s}\,ds,\quad
L_t=\sup_{0\le s\le t}(-Y_s)^+,\quad X_t=Y_t+L_t.
\]
On the core domain `a,b,c,d>0`, write
\[
\bar r={ac-bd\over a+b}.
\]

## Main theorem

1. The Skorokhod formula gives the unique global reflected PDMP.  The environmental stationary law is `(b/(a+b),a/(a+b))`, and the additive input obeys `t^{-1}(Y_t-X_0) -> bar r` almost surely.
2. If `ac<bd`, the process is positive recurrent and has one invariant probability.  If `ac=bd`, it is null recurrent and has no invariant probability.  If `ac>bd`, it is transient and `X_t/t -> bar r` almost surely.
3. In the stable chamber define
   \[
   \kappa={bd-ac\over cd},\qquad
   p_*={bd-ac\over(a+b)d}.
   \]
   The only atom is `p_*` at `(0,0)`.  For `x>0`,
   \[
   f_0(x)={ac\kappa\over(a+b)d}e^{-\kappa x},\qquad
   f_1(x)={a\kappa\over a+b}e^{-\kappa x}.
   \]
   These obey zero interior flux `c f1=d f0`, boundary balance `a p_*=d f0(0)`, total mass one, and the correct environmental marginals.
4. If
   \[
   p_+=\Pr\{X>0\}={a(c+d)\over(a+b)d},
   \]
   then `X | {X>0}` is exponential with rate `kappa`; hence for every integer `n>=1`,
   \[
   \mathbb E X^n=p_+{n!\over\kappa^n}.
   \]
   In stationarity `L_t/t -> (bd-ac)/(a+b)=d p_*` almost surely and in mean.

## Proof engine

Observe the workload at successive starts of state `1`.  With independent on-times `I_n~Exp(b)` and off-times `O_n~Exp(a)`,
\[
 W_{n+1}=\max\{0,W_n+cI_n-dO_n\}.
\]
Its increment mean is `c/b-d/a=(ac-bd)/(ab)`.  The negative-, zero-, and positive-mean Lindley alternatives give respectively positive recurrence, null recurrence, and linear escape.  At zero mean, the increments are continuous, nondegenerate, and have finite variance, so the reflected walk is recurrent but has no finite invariant measure.  Cycle-time normalization gives the continuous-time speed `bar r`.

For the stable law, the stationary forward equations on `x>0` are
\[
0=d f_0'-a f_0+b f_1,\qquad
0=-c f_1'+a f_0-b f_1.
\]
Their sum gives zero integrable flux.  Solving the remaining scalar equation, imposing boundary flux, and normalizing yields the displayed law.  Integration gives all moments.  The path identity divided by time gives the regulator rate.

## Complete zero-rate atlas

Classification is by closed environmental classes.

- `a,b>0`: the core theorem applies when `c,d>0`; if `c=0<d`, the unique law is `delta_0 tensor pi`; if `d=0<c`, workload escapes at speed `ac/(a+b)`; if `c=d=0`, workload is frozen and all `nu tensor pi` are invariant.
- `a=0<b`: state `0` is the unique closed class.  If `d>0`, every trajectory eventually drains and the unique invariant law is `delta_(0,0)`.  If `d=0`, the terminal workload is frozen and every `nu tensor delta_0` is invariant.  The value of `c` affects only the transient pre-absorption excursion.
- `b=0<a`: state `1` is the unique closed class.  If `c>0`, every trajectory in that class escapes at speed `c` and there is no invariant probability.  If `c=0`, every `nu tensor delta_1` is invariant.  The value of `d` affects only the transient pre-absorption excursion.
- `a=b=0`: both singleton environmental classes are closed.  On class `0`, `d>0` leaves only `delta_(0,0)` invariant, while `d=0` permits arbitrary workload laws.  On class `1`, `c>0` has no invariant law and `c=0` permits arbitrary workload laws.  Global invariant probabilities are precisely convex mixtures of the available class-supported laws; uniqueness is not asserted.

## Claim boundary

The nearest workspace neighbors are C351's discrete open Jackson network, C346's deterministic two-dimensional oblique Skorokhod map, and C332's deterministic scalar Moreau play operator.  In particular, C346 is an all-input deterministic path-map theorem, not a Markov-additive reflected-fluid theorem.

This package does not claim a Brownian component, a many-state matrix-analytic theorem, finite-buffer asymptotics, queueing-network product form, literature priority, target arithmetic, Euler data, a target zero match, or a Hilbert--Polya operator.
