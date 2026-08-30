# Theorem package

## Model and event coordinates

Let (N\ge2), (a>0), and (phi_i\in[0,1)) obey
(dotphi_i=1).  Set

\[
U_a(\phi)=\frac{1-e^{-a\phi}}{1-e^{-a}},\qquad
r=e^{-a},\qquad u_i=e^{-a\phi_i}.
\]

At (U_a=1) the oscillator resets to (U_a=0).  Every other oscillator
receives an excitatory increment (epsilon\in(0,1)), clipped at one; pulses
are applied repeatedly until the same-time avalanche is closed.

### Theorem 1 (exact event map)

For a post-avalanche state (u\in[r,1]^N), the next threshold is reached
after the common scaling
\[
u_i\longmapsto \widehat u_i=\frac{r}{\min_j u_j}u_i.
\]
The indices with (widehat u_i=r) fire.  A pulse from one firing index sends
\[
u_j\longmapsto \max\{r,u_j-(1-r)\epsilon\};
\]
newly clipped indices fire and emit their own pulse.  The queue closure is
finite and order-independent as a set; the recorded index order is a
deterministic serialization.

*Proof.*  Since (u_i=e^{-a\phi_i}), free flow multiplies every coordinate by
(e^{-at}).  The first threshold solves (e^{-at}\min u_i=r), giving the
displayed scale.  The identity
(U_a^{-1}(y)=\log(1-(1-r)y)/\log r) shows that adding (epsilon) in (y)
subtracts ((1-r)epsilon) in (u), with clipping exactly at (r).  Each
new firing adds one member to the finite set, so closure terminates. ∎

### Theorem 2 (rational certificate)

If (r,epsilon) and the initial event state are rational, every scaled,
pulsed, reset, and avalanche state is rational.  The producer therefore makes
all firing and tie decisions by exact comparisons in (mathbb Q).

### Theorem 3 (cluster partition cannot refine)

Let the equality partition of (u) group indices having equal coordinates.
Common scaling preserves every equality.  A nonfiring pulse is the same affine
subtraction for every member of a block, while a firing block reaches (r) at
once and is reset together.  Hence the post-event equality partition is a
coarsening (or equal) of the pre-event partition.

### Theorem 4 (synchronized primitive cycle)

The all-equal state (u=(1,\ldots,1)) scales to (u=(r,\ldots,r)), all (N)
indices fire simultaneously, and reset returns to ((1,\ldots,1)).  Its event
word is ([N]), which has primitive period one.  This is a source event cycle;
it is not an arithmetic primitive orbit.

### Finite receipt and literature boundary

The release evaluates (3\times3\times7\times7=441) rational probes for
(r\in\{1/2,2/3,3/4\}), (epsilon\in\{1/5,1/4,1/3\}), (N=2,\ldots,8), and seven
seeds, with twelve event steps.  It records 63 synchronized rows and 441
coarsening rows.  Mirollo--Strogatz prove almost-everywhere synchrony for a
strictly concave rise under their all-to-all hypotheses; Bottani studies
globally coupled synchronization beyond concavity/convexity restrictions.
Those results are cited, not recomputed, and no
complete continuous-state cell census is claimed here.

## Boundary and Route-A verdict

(epsilon=0) removes coupling; (r\to1^-) loses strict concavity and
(r\to0^+) is a fast-rise singular face.  Simultaneous ties are retained as
explicit event boundaries.  Directed or inhibitory coupling is outside scope.
There is no intrinsic arithmetic-prime carrier (A0_FAIL), no target match or
continuation (A2_FAIL/A3_FAIL), and only a formal lift hint (A4_FORMAL_HINT).
The strict tuple is
\[
(\mathtt{A0\_FAIL},\mathtt{A1\_PASS\_ANALYTIC},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT}),
\]
with `ROUTE_A_REJECTED`, `NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B disabled.
