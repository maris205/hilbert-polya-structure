# C278 theorem package

## Status

**PROVABLE AS STATED**, with the state space restricted to the ordered
two-peakon manifold before collision and to the post-collision extension
defined below.  No claim about arbitrary weak-data uniqueness is needed.

## Frozen model

Let

```text
m_t+u m_x+2u_x m=0,  m=u-u_xx,
u(x,t)=p_1(t)e^{-|x-q_1(t)|}+p_2(t)e^{-|x-q_2(t)|},  q_1<q_2.
```

Set `q=q_2-q_1`, `y=e^q`, `p=p_2-p_1`,

```text
P=p_1+p_2,
E=p_1^2+p_2^2+2p_1p_2 e^{-q},
D^2=2E-P^2.
```

## Theorem

1. Distributional substitution is equivalent, until collision, to

   ```text
   qdot_i=sum_j p_j e^{-|q_i-q_j|},
   pdot_i=p_i sum_j p_j sgn(q_i-q_j)e^{-|q_i-q_j|}.
   ```

   Both `P` and `E` are constant, and

   ```text
   ydot=p(y-1),
   pdot=(P^2-p^2)/(2y),
   ydot^2=D^2(y-1)(y-P^2/D^2).
   ```

   In the ordered chart,

   ```text
   P^2-D^2=4p_1p_2(1-e^{-q}).
   ```

   Thus every state with `p_1p_2!=0` lies in exactly one of the two strict
   chambers below.  The equality face `p_1p_2=0` is the degenerate
   single-peak boundary (including the zero field), not a strict two-body
   chamber.

2. If `P^2>D^2`, then for a unique time shift `t_*`,

   ```text
   y=1+(P^2/D^2-1)cosh^2(D(t-t_*)/2),
   p=D tanh(D(t-t_*)/2).
   ```

   The gap is globally positive.  For `P!=0`, after choosing an additive
   centre constant,

   ```text
   q_1+q_2=P t+2 sgn(P) artanh[(D/|P|)tanh(D(t-t_*)/2)].
   ```

   The two asymptotic momenta are `(P-D)/2` and `(P+D)/2`; the labeled
   amplitudes exchange them through the interaction.

3. If `D^2>P^2`, choose the collision time `t_c`.  On the incoming branch,

   ```text
   y=1+(1-P^2/D^2)sinh^2(D(t_c-t)/2),
   p=-D coth(D(t_c-t)/2).
   ```

   Hence collision occurs at finite `t_c` and

   ```text
   q=(D^2-P^2)(t_c-t)^2/4+O((t_c-t)^4),
   p=-2/(t_c-t)+O(t_c-t).
   ```

   With `c=(q_1+q_2)/2`, `h=q/2`, and `K_a(x)=e^{-|x-a|}`,

   ```text
   cdot=P(1+e^{-q})/2,
   u=P(K_{c-h}+K_{c+h})/2+p(K_{c+h}-K_{c-h})/2,
   ||u-PK_c||_infinity <= (|P|+|p|)h.
   ```

   Finite collision time gives `c->q_c`; the displayed asymptotics give
   `h=O((t_c-t)^2)` and `p=O((t_c-t)^-1)`.  Hence the profile converges
   uniformly to the single peak `P e^{-|x-q_c|}`.  Its ordinary energy is
   `P^2`; the difference
   `E-P^2=(D^2-P^2)/2` is the concentrated collision-energy ledger.

4. For a declared `alpha in [0,1]`, conserve `P` and set

   ```text
   E_+=(1-alpha)E_-+alpha P^2,
   D_+^2=(1-alpha)D_-^2+alpha P^2.
   ```

   `alpha=0` gives the conservative reflected signed branch; `alpha=1`
   gives the sticky single peak; intermediate values restart the outgoing
   signed branch with `D_+^2>P^2`.  This is the package's continuation
   definition, not a uniqueness assertion for all weak solutions.

## Proof

The kernel identity `(1-partial_x^2)e^{-|x-q|}=2 delta_q` makes
`m=2 sum p_i delta_{q_i}`.  Testing the momentum equation and matching the
delta-prime and delta coefficients gives the displayed ODE.  In the ordered
chart, `pdot_1=-p_1p_2e^{-q}`, `pdot_2=+p_1p_2e^{-q}`.  Direct
differentiation therefore proves `Pdot=Edot=0`.

Writing `p_1=(P-p)/2`, `p_2=(P+p)/2` gives

```text
E=[P^2+p^2+(P^2-p^2)/y]/2,
```

which rearranges to `p^2(y-1)=D^2y-P^2`.  Combining this with
`ydot=p(y-1)` proves the scalar quadratic.  Separation yields the cosh branch
when its second root exceeds one and the sinh branch when it lies below one.
Differentiation verifies both solutions.  Taylor expansion of `sinh` and
`coth` gives the collision laws.  The centre equation and the global
one-Lipschitz dependence of `K_a` on `a` give the displayed uniform profile
bound and its limit.  Substitution of the energy prescription gives the
`alpha` formula and its endpoint classifications.

The one-peak boundary is `u=p e^{-|x-q_0-pt|}`.  `P=0<E` is retained in the
signed chamber; `P=E=0` is the zero field.  `q=0` is not an ordered chart
point and is used only as the explicitly defined extended collision state.

## Dependency and evidence boundary

The distribution identity implies the ODE; the ODE implies invariants; the
invariants imply scalar reduction; the root order implies chamber; explicit
branches imply global or collision behavior; only then is the continuation
ledger applied.  The 42 finite rows, 551 independent assertions, 10 symbolic
identities, byte replay, and 41 repaired-hash attacks audit this chain but do
not replace the analytic implications.

## Route-A result

Strict tuple:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`.  Continuous source parameters, scattering and collision
provide no rational-prime owner, isolated primitive-cycle product, target
divisor, functional equation, target zero match, or Hilbert–Pólya operator.
Route B is false.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
