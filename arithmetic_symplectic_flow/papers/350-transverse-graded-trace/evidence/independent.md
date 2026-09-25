# Independent MAIN and full-cotangent derivation

**Audit:** `ANG-AUDIT-20260921-TGT01`; physical owner `ANG-20260921-RCF01`.
**Finding:** The prescribed transverse supertrace is minus the orbit measure;
its flat function is the orbit zeta, not the reciprocal orbit determinant.
**Scope:** MAIN and full-cotangent control only; internal `NOT_CALIBRATED`.

## 1. Inputs and actual sequence

I personally read original card lines1–100 through EOF and measured SHA-256
`a4fb462ee562dbcda150a6ac2f408fc9cc152e78e15fc8a0308297e9d1c414f0`.
I reread the complete ARS router and retained the previously read
workflow/DA/runtime instructions. The same348/349 owner and my own earlier
derivations were retained context, not newly inspected scientific files.
The card's quoted348/349 manuscript hashes were not independently remeasured.

After that input read I explicitly acknowledged that no scientific derivation
had begun. The parent then issued `CP1released`, reporting the separate scope
review PASS and no required card change. Only then did I derive the claims
below. I sent the completed main/control conclusions before writing this file.
After the initial report write, the parent reported agreement on the sign and
requested that classical continuation remain a retained standard input rather
than a fresh proof campaign. This final report follows that narrower scope.
No root draft, peer answer, outcome, other scientific file, web source,
numerical experiment or auxiliary agent was read or used. This is the sole
file written; the scope review and all earlier packages remain untouched.

Shared history, one inherited model and the card's disclosed cancellation/sign
expectation preclude blind or error-independent review claims. This is a
bounded independent derivation with an adverse check, not external peer review
or a completed review of the parent's eventual full manuscript and controls.

## 2. Whole bundle, action and full Hilbert spaces

Use the entire terminal component R^3 and every circular component
Q_p=(R/L_p Z) x R^2, L_p=log p. No transverse state is removed.
The frozen beta satisfies beta(R)=1. Thus TQ=span(R) direct-sum ker beta
everywhere, including vz=-1. Restriction identifies ann(R) with (ker beta)*:
its inverse extends a covector to vanish on R using that direct sum.

The forms alpha=dv-v du and eta=dz+z du annihilate R, are independent,
and are global even when u is circular. In this frame

```text
beta=du+(v eta-z alpha)/2;
(Phi^(-t))* beta=beta,
(Phi^(-t))* alpha=e^(-t) alpha,
(Phi^(-t))* eta=e^t eta.                                  (1)
```

These identities follow by substituting the actual backward flow; hence both
the splitting and its transverse bundle are invariant on the full owner.
The scalar coefficient pullback is unitary for nu=du dv dz. With the FROZEN
orthonormal alpha,eta metric, the degree matrices are
M_0=M_2=1 and M_1=diag(e^(-t),e^t). Consequently the operators on compactly
supported smooth sections extend uniquely to bounded invertible operators
on the full H_q, with norms 1,e^|t|,1 respectively. Density follows by finite
component/compact truncation and smoothing. Degrees0,2 are unitary; degree1
is not unitary for t!=0 in this metric.

Every H_q is infinite dimensional, already over the terminal component.
A bounded invertible operator on such a space cannot be compact, since its
inverse would then make the identity compact. Thus NONE of these U_t^(q)
is trace class, for any real t, including zero. No ordinary degree trace or
ordinary trace-class supertrace follows from the distributional calculation.

## 3. Actual kernels and justified spatial pushforward

Relative to the global form frames and nu, the degree-q joint kernel on Q_p is

```text
K_q(t;x,y)=M_q(t) delta_(L_p)(y_u-u+t)
                 delta(y_v-e^(-t)v) delta(y_z-e^t z).       (2)
```

Integrating against a section reproduces exactly its induced pullback.
On the joint diagonal y=x, the local defining functions at the kth lift are
(t-kL_p,(1-e^(-t))v,(1-e^t)z). For t>0 they vanish only at
t=kL_p, k>=1, v=z=0; their derivative in (t,v,z) has nonzero determinant.
Changing to these three transverse coordinates directly defines the delta
pullback. Its absolute denominator is

```text
Delta(t)=(1-e^(-t))(e^t-1)=e^t+e^(-t)-2 > 0.              (3)
```

The longitudinal integration is over ONE phase circle of length L_p, not
kL_p. The terminal component's diagonal requires t=0 and contributes nothing
on positive time; it nevertheless remains part of every operator space.
For any compact time window [a,b] inside (0,infinity), only finitely many
p<=e^b and k<=b/log2 occur. Their diagonal supports are compact circles at
v=z=0. Thus projection of the diagonal support is proper on that window;
a compact spatial cutoff equal to one there defines its pushforward
independently of the cutoff. This handles both noncompactness and the full
countable union, rather than integrating a distribution against 1 formally.

Put w_p,k=p^(-k)/(1-p^(-k))^2=1/Delta(kL_p). Each degree therefore owns a
positive locally finite measure, with respective coefficients

```text
Theta_0: L_p w_p,k;
Theta_1: L_p (p^k+p^(-k)) w_p,k;
Theta_2: L_p w_p,k,                                      (4)
```

at kL_p. No fixed-time delta(0), time-zero regularization, degree sign, or
selected-orbit function space entered this derivation.

## 4. Fixed parity, exact function and initial domains

Since (p^k+p^(-k))w_p,k=1+2w_p,k, the independently defined degree measures
satisfy Theta_1=Theta_orb+2Theta_0 and Theta_2=Theta_0. Standard parity gives

```text
Theta_perp=Theta_0-Theta_1+Theta_2=-Theta_orb;
log D_perp(s)=sum_(p,k>=1) p^(-ks)/k,
D_perp(s)=product_p (1-p^(-s))^(-1)=zeta(s), Re s>1.        (5)
```

The minus sign comes from the actual transverse determinant divided by its
absolute value: 2-e^t-e^(-t)=-Delta(t). Flipping it after the calculation
would change the frozen grading. Thus D_perp=Z_orb=D_orb^(-1), not D_orb.
Already the coefficient at log2 is -log2 instead of +log2.

For precision, the defining Laplace integrals with /t for degrees0,2 converge
absolutely exactly when Re s>0; their terms are
p^(-k(s+1))/[k(1-p^(-k))^2]. The degree1 integral converges exactly when
Re s>1, by its positive decomposition above. The signed supertrace integral
also has exact absolute domain Re s>1, since its total variation is Theta_orb.
Upper bounds follow from geometric sums and integer Dirichlet series;
lower bounds use the k=1 prime harmonic series. That series diverges:
if sum_p 1/p were finite, the finite Euler products product_(p<=X)(1-1/p)^(-1)
would be bounded, yet contain the harmonic partial sum through X.

Absolute local convergence permits rearrangement into the Euler product,
whose expansion is the integer Dirichlet series by unique factorization.
This proves (5) without a borrowed dynamical trace formula. It also gives
D_perp->1 uniformly in Im s as Re s->infinity, no branch ambiguity, and
D_perp'/D_perp=integral e^(-st) Theta_perp(dt) on Re s>1.

## 5. Continuation with the classical input explicitly separated

Assume the standard meromorphic continuation of zeta to C, with its simple
pole at1. Then (5) immediately gives that same meromorphic continuation of
D_perp, by equality on the initial half-plane. This implication is exact;
the classical property is retained349 context, not a new source verification
or new continuation theorem by this reviewer. The parent previously reported
its official DLMF verification; I did not independently open that source.
Continuation does not enlarge the original integral's absolute domain,
change its normalization or provide an ordinary/Fredholm determinant.

## 6. Full-cotangent control, with its own authorized scope

The global cotangent frame is (beta,alpha,eta). Its backward multipliers are
(1,e^(-t),e^t), so the degree0–3 characters are respectively
1, 1+e^(-t)+e^t, 1+e^(-t)+e^t, 1. Each actual kernel has the same scalar
factor (2) and its induced exterior matrix. The same joint transversality
and compact-support argument establishes every individual flat trace before
forming the prescribed sum. Their measures are

```text
Theta_cot,0=Theta_0; Theta_cot,1=Theta_orb+3Theta_0;
Theta_cot,2=Theta_orb+3Theta_0; Theta_cot,3=Theta_0.
```

The standard alternating sum is ZERO because the invariant beta factor
contributes 1-1. Its flat function is1, entire, with its zero defining
integral convergent for every s. Individual degrees0,3 have initial domain
Re s>0 and degrees1,2 Re s>1. This is cancellation of already defined
distributions, not cancellation of an undefined diagonal restriction.
No full-cotangent Hilbert metric was frozen: this control makes no operator
norm, unitarity or full-H claim based on an invented metric.

## 7. Adverse check and bounded disposition

The strongest positive result is genuine transverse cancellation derived
from the actual form pullback on the entire frozen flow. It supplies the
ordinary orbit zeta as a signed flat function, not a scalar-operator repair.
The fixed parity obstructs identifying its measure with +Theta_orb or its
function with D_orb. Full cotangent does not remove that issue: it cancels
everything through the invariant longitudinal covector. Ordinary trace-class
interpretations fail independently on the stated MAIN Hilbert spaces.
No differential, cohomology, anisotropic/nuclear space, quantum object,
Riemann-zero realization or formal Route coordinate is proved. FACTOR-OFF,
UNIT-HOLONOMY and DRIFT-ONLY are not audited in this report. Their conclusions
cannot be inferred from the two owners treated here. Strong naturalness
remains OPEN; no change of source, physical clock, metric or parity was made.

EOF — independent MAIN/full-cotangent derivation and adverse check complete.
