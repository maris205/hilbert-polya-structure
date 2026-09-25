# Independent MAIN J2 — actual scalar kernel and flat-determinant function

**Audit:** `ANG-AUDIT-20260921-RCZ01`  
**Unchanged flow:** `ANG-20260921-RCF01`  
**Result:** Positive-time scalar flat trace and D_0 are owned; ordinary trace class and identification with the unit-weight orbit objects fail.  
**Limits:** MAIN J2 only; controls and a full J1/J3 review are not performed.  
**Standing:** Internal, inherited model/shared history; `NOT_CALIBRATED`.

## 1. Actual inputs, sequence and exposure

The sole scientific file reread was the original349 card, complete lines1–192
through EOF, measured SHA-256
`7549da0db82ad6b260ce91dbebde484ce8d6045f92b7672f467900a5fdc9366e`.
Previously read ARS router/workflow/DA/runtime guidance remains applicable.
This assignment follows the separate frozen scope review, which is unchanged.

The restated source, quotient coordinates, volume and physical flow agree
at the formula level with this reviewer's retained348 Gate1 derivation.
The348 card/paper dependency locks quoted in the349 card were not remeasured
or reopened. This report does not claim a new complete read of those sources.
The positive-time fixed locus needed below is derived from the actual frozen
Phi formula, not from a borrowed trace formula or a selected-center operator.

All main derivations below were obtained before sending the parent a summary
of the kernel weights, operator class, initial domain, product and mismatch.
After that summary, the parent reported agreement with its independent work
and said it had checked standard zeta continuation in official DLMF25.2.
That later exposure supplies no independently read external evidence here.
The continuation statement in section7 is explicitly conditional on that
classical property; only the product-tail implication is proved here.

No root manuscript, outcome, peer result, other scientific file, web page,
auxiliary agent, numerical experiment, model change, external upload or Git
operation was used. Only this assigned scalar-independent file was written.
Inherited history and the card's disclosed transverse-weight expectation
prevent any claim of blind discovery, external peer review or independent
model errors. No alternative bundle, weight, function space or flow is added.

## 2. Full scalar action and its Hilbert-space status

Write L_r=log r for each intrinsic cover atom r. The FULL quotient has
the terminal R^3 component and the components

```text
Q_r=(R/L_r Z) x R^2_(v,z),
Phi^t(u,v,z)=(u+t,exp(t)v,exp(-t)z),
dnu=du dv dz.
```

In the terminal component u is real rather than circular. All these
components and all v,z values remain in the operator domain.
The real-coordinate Jacobian of Phi is one. Since Phi is a complete
diffeomorphism with inverse Phi^(-t), its pullback U_t on C_c^infinity(Q)
preserves the L2 norm. It extends uniquely to a unitary operator on the
entire H=L2(Q,nu), with inverse U_(-t), for every real t.
Compactly supported smooth functions are dense: truncate to finitely many
components and compact coordinate boxes, then smooth in those charts.
Thus this is the full-H extension, not a closed-orbit subspace construction.

H is infinite dimensional, already on its terminal component. Disjoint
translates of a unit-norm bump there give an infinite orthonormal sequence;
U_t carries it to another such sequence. Consequently U_t is not compact
and hence is not trace class for ANY real t, including t=0. Equivalently
its absolute value is the identity on an infinite-dimensional H. No ordinary
Tr(U_t) is supplied by the flat distribution constructed next.

## 3. Derivation from the joint kernel, not an orbit-formula definition

Let delta_L be the periodic Dirac distribution with one unit atom per
period L. Relative to the volume du dv dz on Q_r, the frozen kernel is

```text
K(t;x,y)=delta_L(y_u-u+t)
          delta(y_v-exp(-t)v) delta(y_z-exp(t)z),
x=(u,v,z).
```

Integrating this kernel against f(y) gives precisely f(Phi^(-t)x), fixing
the sign and normalization. On local circular lifts the longitudinal
factor is the sum of delta(y_u-u+t-kL), k integer.

Restricting y=x is NOT an evaluation of a fixed-time delta at zero.
For the joint time/space diagonal, the relevant three defining functions are

```text
F_k(t,u,v,z)=(t-kL,(1-exp(-t))v,(1-exp(t))z).
```

For t>0 their common zero set has t=kL with k>=1 and v=z=0; u is free.
At every such point the derivative in (t,v,z) has determinant
(1-exp(-t))(1-exp(t)), which is nonzero. The joint diagonal is therefore
transverse to the kernel's delta constraints. More concretely, near that
time one can use F_k as the three coordinates transverse to u; the inverse
is obtained by dividing its last two entries by the two nonzero factors.
Ordinary change of variables for a three-variable delta proves the pullback
exists and determines its absolute density uniquely. No general trace
formula is assumed in this step.

For a compactly supported smooth test function a(t,u,v,z), the diagonal
distribution on this component is consequently

```text
sum_(k>=1) [1/((1-exp(-kL))(exp(kL)-1))]
            integral_(R/LZ) a(kL,u,0,0) du.
```

This includes the full longitudinal phase circle exactly once. Its integral
has length L, not kL; the same orbit's kth traversal does not create k
distinct phase circles. The transverse factors have an absolute determinant;
there is no degree sign or cancellation inserted by hand.

On the terminal R^3 component the longitudinal diagonal constraint is t=0.
Its restriction to the open positive-time domain has empty support, so that
component contributes zero. This conclusion is derived from its actual
kernel; the terminal component was not removed from Q or from H.

## 4. Noncompact pushforward and the exact positive measure

Let h have compact support in (0,infinity), contained in [a,b] with a>0.
Only r with log r<=b can contribute, hence only finitely many positive
integer atoms r<=exp(b). Also k<=b/log2. Thus only finitely many (r,k)
pairs occur in this time window. Each contributing spatial support is the
compact circle at v=z=0. The diagonal-support projection to positive time
is therefore proper over every compact time window.

This supplies the missing noncompact/countable-union justification. The
full spatial integral can be defined with a compact cutoff equal to one
on those finitely many circles, and is independent of that cutoff. It is
not an unjustified integration of a distribution against a noncompact
constant test function. The resulting object is a positive locally finite
Radon measure, not just a formal list of closed orbits:

```text
Theta_0 = sum_(r atoms) sum_(k>=1)
          L_r * r^(-k)/(1-r^(-k))^2 * delta_(k L_r).
```

It is also a distribution on C_c^infinity((0,infinity)), exactly the class
frozen in the card. Time zero is outside the construction; no regularization
there, fixed-time ordinary trace or distributional value at t=0 is asserted.
The delta support at v=z=0 is a consequence of the full kernel equations,
not a restriction of the function space or an a priori orbit selection.

## 5. D_0: sharp initial domain and normalization

Because the actual Theta_0 is now a positive measure, the frozen integral
has an unambiguous absolute-convergence meaning. It gives

```text
log D_0(s) = -sum_(r atoms) sum_(k>=1)
              r^(-k(s+1)) / [k(1-r^(-k))^2].                 (1)
```

This logarithm is the defining integral, with no logarithmic branch chosen
after evaluating D_0. For sigma=Re s>0, use (1-r^(-k))^(-2)<=4 and
sum over positive integer r>=2 to dominate the series by a constant times
sum_(r>=2) r^(-1-sigma). The bound is locally uniform on sigma>=epsilon>0.
Extra logarithmic factors from s differentiation are summable with a smaller
positive margin. Hence (1) is holomorphic in Re s>0, D_0 is holomorphic
and nonzero there, and differentiation is legitimate. In particular

```text
D_0'(s)/D_0(s) = integral_(0,infinity) exp(-s t) Theta_0(dt), Re s>0.
```

The initial integral diverges absolutely for sigma<=0. Its k=1 terms are
at least 1/r in magnitude, and the sum of reciprocals of cover atoms
diverges. An elementary justification is as follows. If that sum converged,
the logarithms of the finite products product_(r<=X)(1-1/r)^(-1) would
be bounded, since -log(1-1/r)<=2/r. Yet factorization shows each such
product contains every term 1/n with n<=X and therefore exceeds the
diverging harmonic partial sum. This is a contradiction.

Thus Re s>0 is the EXACT absolute-convergence half-plane for the original
integral. This is not claimed to be a boundary of analytic continuation.
The measure is supported at t>=log2, so dominated convergence at any fixed
positive abscissa proves log D_0(s)->0, uniformly in Im s, as Re s->infinity.
The frozen normalization is therefore D_0(s)->1.

## 6. Product on the owned initial domain

For |a|<1, a/(1-a)^2=sum_(m>=1) m a^m. Absolute convergence established
above permits the corresponding triple rearrangement in Re s>0:

```text
log D_0(s)=-sum_(m>=1) m sum_(r atoms,k>=1) r^(-k(s+m))/k;
D_0(s)=product_(r atoms,m>=1) (1-r^(-(s+m)))^m
      =product_(m>=1) zeta(s+m)^(-m).                       (2)
```

Here zeta(w) initially denotes the classical Dirichlet series
sum_(n>=1)n^(-w) on Re w>1. Its Euler product on that domain follows
from integer factorization and absolute convergence, not from a trace
theorem or a new prime weight. Every argument s+m in (2) lies in that
domain when Re s>0. The integer multiplicity m in this product was derived
from the actual transverse Jacobian expansion; it was not inserted into
the scalar operator or the primitive-orbit normalization.

The double product is absolutely locally convergent there, and the logarithms
are the convergent series tending to zero at positive infinity. No branch
ambiguity or unfrozen normalization is needed for (2).

## 7. Conditional global continuation; independently proved product tail

The additional classical input in this section is explicitly conditional:
assume zeta has its standard meromorphic continuation to C. This report
does not claim a new external verification of that property. The parent's
later DLMF-check message is disclosed in section1, not treated as a source
personally read by this reviewer.

Given that classical input, (2) yields a meromorphic continuation of D_0
to the whole plane. Here is the independent product-tail proof. On any
compact K in C, choose M sufficiently large that Re(s+m)>=3 for s in K
and m>=M. The original Dirichlet series then bounds

```text
|zeta(s+m)-1| <= sum_(n>=2) n^(-Re(s+m)) <= C_K 2^(-m).
```

For larger M this is uniformly less than1/2, giving the unique logarithm
near1 with |log zeta(s+m)|<=2 C_K 2^(-m). Hence the tail logarithm
-sum_(m>=M) m log zeta(s+m) converges locally uniformly. Its exponential
is holomorphic and nowhere zero. The remaining finitely many reciprocal
integer powers of meromorphic zeta are meromorphic, proving the claimed
conditional extension. The constructions agree on overlaps and with (1).

Possible zeros/poles of different finite factors must be combined with
their multiplicities; no independent zero-location or spectral claim follows.
Analytic continuation never retroactively makes the original integral
absolutely convergent outside Re s>0. An ordinary/nuclear Fredholm
representation is neither proved nor inferred from this product.

## 8. Comparison and the precise scalar stop

The frozen unit-weight orbit distribution assigns coefficient log2 at
t=log2. The actual scalar kernel assigns 2log2 there, because
2^(-1)/(1-2^(-1))^2=2. Thus Theta_0 is not Theta_orb.
This is a full-owner coefficient difference, not a missing phase factor.

The normalized determinant functions differ as well. On the common
absolutely convergent half-plane Re s>1, use the frozen definition of
D_orb and set w(r,k)=r^(-k)/(1-r^(-k))^2. For real sigma tending to infinity,

```text
log D_0(sigma)-log D_orb(sigma)
 = -sum_(r,k) (w(r,k)-1) r^(-k sigma)/k
 = -2^(-sigma) + O(3^(-sigma)).
```

Indeed 0<w(r,k)<=2, each integer prime power has a unique (r,k), and
the remaining absolute tail is at most sum_(n>=3)n^(-sigma), which is
O(3^(-sigma)) for sigma>=2. The leading term cannot vanish. This comparison
uses only the stated orbit normalization on its convergent domain, not
a claim to have completed the separate ordinary-zeta J1 audit.

The justified stop is therefore the asserted identification of this scalar
flat trace/function with the unit-weight orbit objects, together with any
ordinary trace-class interpretation of U_t. The genuine positive-time flat
measure, its holomorphic initial-domain function and product are retained.
No compensating amplitude, graded bundle, selected subspace or time change
has been introduced. Failure here does not rule out every different transfer
or trace construction under a separately frozen owner.

## 9. Adverse checks and final limits

The strongest positive case survives: the full classical scalar pullback
owns a well-defined positive-time flat trace despite its lack of an ordinary
operator trace. Noncompactness and countably many components do not obstruct
this particular pushforward because the actual diagonal support is compact
over compact positive-time windows. Those facts were proved, not assumed.

The strongest false inference would turn that distributional construction
into a trace-class/Fredholm or spectral realization, or cancel its transverse
weights to force the orbit zeta. The explicit infinite-dimensional unitary
test, the coefficient at log2 and the normalized-function asymptotic disprove
those inferences for the frozen scalar object.

This completes ONLY the independent MAIN J2 assignment. The controls,
full ordinary-zeta J1 synthesis, final J3 audit, stronger naturalness and
any new function space remain outside this report. It issues no formal
Route coordinate, quantization, self-adjoint generator, Riemann-zero claim
or universal transfer-operator no-go. The original card and scope-review
were not changed. The global continuation assertion retains its explicit
classical-input condition rather than an invented personal source receipt.

EOF — completed bounded MAIN scalar derivation; freeze after full readback/hash.
