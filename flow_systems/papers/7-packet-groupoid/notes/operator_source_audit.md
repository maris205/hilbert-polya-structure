# Paper 7 Phase-2 operator source audit

Status: **FROZEN — SOURCE GATE PASS WITH MANDATORY TERMINOLOGY RESTRICTIONS**  
Audit date: 2026-08-14  
Protocol SHA-256: `0029ea437f9318ff4962830ed4d197cdad0d355968364a52bbeefc63a9db96c4`  
Candidate-lock SHA-256: `0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa`  
Artifact manifest: `sources/operator_source_manifest.md`

This is a Phase-2 source/domain audit only.  It neither proves P7-1–P7-9 nor
changes the frozen candidate.  All theorem locators below were checked in full
text with `PASS` PDF preflights.

## 1. Executive verdict

1. **Selected algebra and positive-cone trace: source gate PASS.**  The bounded
   product algebra is the countable atomic direct-integral von Neumann algebra
   on the Hilbert direct sum.  Once each concrete fiber trace is verified,
   the weighted positive-cone sum is a faithful normal semifinite trace.

2. **Global `L1` boundary: PASS and non-negotiable.**  For a bounded block
   operator `A=(A_p)`,

   ```text
   A in L^1_tau(M)  iff  sum_p m_p tau_p(|A_p|) < infinity,
   ||A||_(1,tau) = sum_p m_p ||A_p||_(1,tau_p).
   ```

   Componentwise trace class does not imply global trace class.  Nothing in
   the sources licenses `tau_m(C_f)` when this sum diverges.

3. **Zero-mode branch: source gate PASS on `Re(s)>1` for unit masses, but the
   determinant name in the manuscript must be qualified.**  The complex
   function required by P7-5 is a **local principal trace-log determinant**
   (equivalently, a branch-fixed local scalar lift made before taking the
   relative de la Harpe–Skandalis quotient).  It is not the ordinary Fredholm
   determinant and not the Fuglede–Kadison determinant.

4. **Fuglede–Kadison applies only as a positive-valued companion.**  The
   semifinite Fuglede–Kadison determinant is defined for `I-K_s`, but for
   complex `s` it retains only the modulus of the principal trace-log
   determinant.  It cannot carry the complex Euler-product phase.

5. **Breuer–Fredholm gives no determinant credit.**  Since `I-K_s` is already
   invertible in the audited half-plane, it is trivially Breuer–Fredholm with
   index zero.  Calling the scalar function a “Breuer determinant” is false.

6. **Morishita can be repaired to a topological orbit bridge only.**  The v5
   full-character parametrization and printed prime-circle proof do not close:
   the trivial character is a counterexample to the asserted surjection, and
   vanishing only at the `p` coordinate was not established.  Restricting the
   construction to Deninger's invariant finite-kernel subsystem `E_f`, and
   using Deninger's equation (35) for every away-from-`p` coordinate, gives a
   genuine same-source continuous flow-anti-equivariant map that is
   packetwise onto the corresponding prime circle.  It is not globally onto,
   collapses the transverse packet labels, and supplies no measure,
   disintegration, operator-algebra, trace-ideal, or determinant transport.

## 2. Decomposable algebra, trace, and `L1`

### 2.1 What the sources support

- Hiai [OA-2], journal p. 118 and Lemma 2.1(1),(5), treats a semifinite von
  Neumann algebra as a direct integral of fibers with a measurable field of
  faithful normal semifinite traces.  Spectral-projection traces and `L^p`
  norms disintegrate fiberwise.  A countable product is the atomic/counting-
  measure specialization.

- Bagarello–Trapani–Triolo [OA-1], Theorem 2.1, constructs a faithful normal
  semifinite trace from a countable sufficient family of normal semifinite
  traces.  For the central summand traces

  ```text
  eta_p(A) = m_p tau_p(A_p),    supp(eta_p)=z_p,
  ```

  the supports `z_p` are mutually orthogonal, so their theorem specializes to
  `tau_m(A)=sum_p eta_p(A)` on `M_+`.

- Fack–Kosaki [OA-3], Proposition 2.7 and Corollary 2.8, supplies the
  noncommutative integral identity `tau(|T|)=integral mu_t(T) dt`.  Hochs–Kaad–
  Schemaitat [OA-5], §6.2, explicitly defines the bounded trace ideal

  ```text
  L^1_tau(M) := {x in M : tau(|x|)<infinity}
  ```

  and records that it is a Banach star-algebra for
  `||x||_(1,infinity)=||x||+tau(|x|)` and an ideal in `M`.

### 2.2 Exact permission for Paper 7

Paper 7 may state, after its concrete fiber verification, that

```text
M = product_p M_p
```

is the selected countable decomposable/W-star product on `direct-sum_p H_p`,
and that

```text
tau_m(A) = sum_p m_p integral_Bp Tr_Kappa_p(A_p(b)) dmu_p(b),  A>=0,
```

is an extended faithful normal semifinite trace.  Faithfulness uses `m_p>0`;
normality and semifiniteness must be checked on the positive cone, independently
of any Dirichlet-series convergence.

For every bounded `A=(A_p)`, functional calculus is componentwise, hence
`|A|=(|A_p|)`.  Hiai's disintegration plus the defining positive-cone sum then
permits precisely

```text
A in L^1_tau(M)  iff  sum_p m_p ||A_p||_(1,tau_p)<infinity.
```

This is the required global boundary for both `C_f` and `K_s`.

### 2.3 Required notation discipline

- When the object is required to be bounded, write `L^1_tau(M)` or
  `M intersect L^1(M,tau)` and define it as above.  The full noncommutative
  `L^1(M,tau)` is also commonly used for a completion/affiliated-operator
  space; the manuscript must not silently alternate between the two meanings.
- `tau_m` is a normal semifinite trace on the positive cone, but a complex
  value `tau_m(x)` is available only on its linear trace domain.  An arbitrary
  bounded block outside `L^1_tau` does not acquire a finite complex trace.
- `Theta_m` remains a componentwise positive-time distribution.  It is not a
  continuation of `tau_m(C_f)` supplied by any source audited here.

## 3. Determinant taxonomy and the `K_s` decision

| Construction | Verified domain and codomain | Multiplicativity | Status for `I-K_s` |
|---|---|---|---|
| Ordinary Hilbert Fredholm determinant [OA-7] | `I+A`, `A` trace class on the represented Hilbert space; scalar complex, with an entire `det(I+zA)` | Global on `I+S_1`; Plemelj trace-log series is initially local | **Not available** in the intended representation: `1_Bp tensor P_0,p` has infinite ordinary Hilbert multiplicity when `dim L2(B_p)=infinity`.  P7's ordinary-trace control must record this fact. |
| de la Harpe–Skandalis [OA-4] | Stable identity component of a Banach algebra with a bounded tracial map; values in `E/r(K0(A))` | Homomorphism into the quotient | The absolute theorem does not apply to unbounded `tau_m` on all of `M`.  The relative trace-ideal version [OA-5] applies, but is still quotient-valued before taking real part. |
| Semifinite Fuglede–Kadison [OA-5, OA-6] | Invertible `g` with `g-I in L^1_tau(M)`; `(0,infinity)`, `Delta_tau(g)=exp tau(log|g|)` | Global positive multiplicative invariant | **Applies**, but yields only `|D_pr(s)|` for this diagonal normal family; it equals the complex determinant only on the real half-line `s>1`. |
| Breuer–Fredholm [OA-9] | Invertibility modulo the `tau`-compact ideal / finite kernel and cokernel; index-valued | Index is additive, not a determinant law | `I-K_s` is invertible when `||K_s||<1`, hence Breuer–Fredholm of index zero.  No complex determinant follows. |
| Guido–Isola–Lapidus analytic determinant [OA-8] | A C-star algebra with a **trace state**, on `0 notin conv sigma(A)`; scalar analytic | Product law can fail even when all three factors lie in the domain | Its theorem cannot be applied verbatim because `tau_m(1)=infinity`.  It is a useful warning and finite-trace analogue only. |

### 3.1 Why the relative theorem, not the absolute theorem, is relevant

Hochs–Kaad–Schemaitat [OA-5] verifies that `(L^1_tau(M),M)` is a relative
Banach-algebra pair and that `tau` is a continuous hypertrace in the trace-ideal
norm.  Their complex pre-determinant is quotient-valued; Definition 7.4 takes a
real part and exponentiates to obtain the positive semifinite Fuglede–Kadison
determinant.  Therefore:

- the sources do **not** provide a canonical global complex scalar determinant
  on all of `I+L^1_tau(M)`;
- choosing the logarithmic path near the identity gives a legitimate local
  scalar lift, but that branch/path must remain in the notation and statement;
- no unrestricted noncommutative product law may be imported for this scalar
  lift.

### 3.2 Exact permitted theorem statement for `K_s`

The following is the maximal operator-theoretic statement authorized for the
unit-mass candidate, subject to proof in P7-4/P7-5:

> For `Re(s)>1`, `K_s=direct-sum_p p^(-s)P_(0,p)` belongs to the bounded trace
> ideal `L^1_tau(M)`, satisfies `||K_s||=2^(-Re(s))<1`, and depends
> holomorphically on `s` in the trace-ideal Banach norm.  With `Log_0` denoting
> the logarithm branch fixed at the identity by its norm-convergent power
> series, define the **principal trace-log determinant**
>
> ```text
> D^pr_tau(s) := exp(tau(Log_0(I-K_s))),
> Log_0(I-K_s) := -sum_(r>=1) K_s^r/r.
> ```
>
> The series converges in `L^1_tau`, its traced series converges absolutely and
> locally uniformly on `Re(s)>1`, and consequently `D^pr_tau` is holomorphic
> and nonzero there.  In the same branch,
>
> ```text
> D^pr_tau(s)
>   = exp(-sum_(r>=1) tau(K_s^r)/r)
>   = exp(-sum_p sum_(r>=1) p^(-rs)/r)
>   = product_p (1-p^(-s)).
> ```

The relevant source conditions are exactly those verified in [OA-5]: `K_s` is
in the bounded trace ideal, `tau` is continuous in the relative Banach norm,
and `I-K_s` is invertible.  The additional `||K_s||<1` fixes the logarithm
without a global branch choice.  Trace-ideal convergence is the needed gate;
operator-norm convergence alone is insufficient.

The Euler product here is obtained from the absolutely convergent trace-log
sum over central blocks.  It does not require, and must not be advertised as,
an unrestricted multiplicativity theorem for a complex semifinite determinant.

### 3.3 Relation to the positive determinant

For the same `s`, [OA-5] permits

```text
Delta_tau(I-K_s) = exp(tau(log|I-K_s|)) in (0,infinity).
```

Because the audited family is normal and diagonal,

```text
Delta_tau(I-K_s)=|D^pr_tau(s)|.
```

For real `s>1`, the principal logarithm is real and the two values coincide.
For nonreal `s`, the Fuglede–Kadison determinant discards phase.  Thus it cannot
be the complex analytic function required by P7-5.

### 3.4 Multiplicativity boundary

- Ordinary Fredholm multiplicativity [OA-7] is unavailable because the
  ordinary Hilbert trace-class hypothesis fails.
- Positive Fuglede–Kadison multiplicativity [OA-5, Proposition 7.5] is valid,
  but only for the positive-valued invariant.
- The de la Harpe–Skandalis construction is multiplicative in its quotient
  codomain, not as an automatically chosen scalar complex representative.
- A scalar trace-log product law is safe only under an explicitly compatible
  logarithm/path (in particular in a commuting local functional-calculus
  domain).  Paper 7 does not need such a general theorem for its blockwise
  Euler-product calculation.
- [OA-8, Remark 4.5] is an explicit warning that even a well-defined analytic
  trace-log determinant need not satisfy a general product property.

## 4. Fourier/Poisson convention authorized for P7-1

Laugesen [OA-10], Definition 14.1, uses

```text
fhat(xi) = integral_R f(t) exp(-i xi t) dt,
f(t) = (1/2pi) integral_R fhat(xi) exp(i xi t) dxi.
```

Scaling Theorem 23.5 from period `2pi` to period `L>0` gives

```text
sum_(n in Z) fhat(2pi n/L) = L sum_(r in Z) f(rL).
```

Every `C_c^infinity` test function satisfies the stated decay hypotheses.
Changing the sign convention for the translation eigenvalue merely replaces
`n` by `-n` in the full lattice sum, but the manuscript must freeze one
convention before stating the component trace.

This source supports only the component Poisson calculation.  It does not
license exchanging the prime sum with a global semifinite trace outside the
`L^1_tau` criterion.

## 5. Morishita v5: exact bridge credit and hard boundary

Morishita [OA-11], Lemmas 3.4--3.5 (PDF pp. 23--24), supplies continuity,
Galois equivariance, and `R_+` anti-equivariance for the displayed map.
However, equation (2.2.7) is not surjective onto the printed full character
space: its image has finite kernel, whereas the trivial character does not.
The printed proof of Theorem 3.6(2) (PDF p. 25) also checks only that the
`p`-coordinate vanishes, which does not exclude additional zero coordinates
and therefore does not prove membership in the standard prime circle `C_p`.

The exact repair is source-compatible but strictly narrower.  Deninger's
equation (35) parametrizes the finite-kernel class `E_f`; on a closed
`p`-fibre it makes every away-from-`p` coordinate nonzero and normalizable.
Deninger's admissibility and restricted-topology results make `E_f` an
invariant subsystem with the full prime packet.  Morishita's map restricts and
descends there, and the repaired coordinate calculation plus
anti-equivariance proves that each source circle maps onto `C_p`.  The global
map is not onto the whole adelic target (its image has at most one finite zero
coordinate), and distinct transverse circles over `p` have the same target
circle.  This is genuine same-object topological/flow credit, but it is a
many-to-one packet-label collapse, not a measured equivalence or a global
factor onto the target.  The detailed proof and locators are frozen in
`source_audit.md`, Sections 7.2--7.3.

The full-text operator audit located no definition or theorem transporting:

- a Borel or Haar probability measure on the packet base;
- a disintegration or Radon–Nikodym relation;
- a Hilbert-space representation or decomposable von Neumann algebra;
- a normal faithful semifinite trace or its `L^1` ideal;
- the zero-mode projection, the family `K_s`, or any determinant.

The paper mentions that certain noncommutative quotients correspond to crossed-
product noncommutative algebras (PDF p. 4), but neither the printed statement
nor the repaired restriction is an operator-algebra homomorphism or
trace-preserving equivalence.  A continuous map that collapses fibers does not
determine a canonical transverse measure; even a chosen pushforward measure
would not automatically induce a normal trace, disintegration, trace-ideal
isometry, or determinant identity.

**Permitted credit:** after explicitly naming the `E_f` repair, same-source
topological continuity, flow anti-equivariance, and packetwise prime-orbit
surjectivity onto `C_p`; the map may be called a factor only onto its invariant
image.  **Forbidden credit:** the uncorrected full-character theorem, global
surjectivity onto the adelic target, or “Morishita transports `mu_p`, `M_p`,
`tau_p`, `K_s`, or the determinant.”

## 6. Mandatory permitted and forbidden terminology

### Permitted

- “selected decomposable type-I von Neumann algebra”;
- “extended faithful normal semifinite trace on the positive cone”;
- “bounded `tau_m`-trace ideal” with its definition;
- “componentwise return distribution” for `Theta_m`;
- “principal trace-log determinant on `Re(s)>1`” or
  “branch-fixed local analytic `tau` trace-log determinant”;
- “local scalar lift of the relative de la Harpe–Skandalis class,” provided the
  path/branch and the non-global nature are stated;
- `Delta_tau` / “semifinite Fuglede–Kadison determinant” only for the positive
  quantity `exp tau(log|g|)`;
- “Breuer–Fredholm, index zero” only as the trivial consequence of invertibility.

### Forbidden without a new theorem

- `tau_m(C_f)` when `C_f` is outside the global trace domain;
- “global flat trace,” “groupoid trace,” or “distributional extension of
  `tau_m`” for `Theta_m`;
- “ordinary Fredholm determinant of `I-K_s`”;
- “Fuglede–Kadison determinant equals the complex Euler product” for nonreal
  `s`;
- “the de la Harpe–Skandalis determinant” as a canonical global complex scalar;
- “Breuer determinant” or “Breuer/Fuglede–Kadison determinant” as a conflated
  construction;
- applying [OA-8]'s finite-trace-state analytic determinant theorem directly to
  `tau_m`;
- “Ruelle determinant,” “primitive-orbit determinant,” or dynamical determinant
  for the zero-mode ledger;
- any claim that Morishita's topological map transports measure, trace,
  representation, `L^1`, zero modes, or determinant;
- “canonical/source-owned determinant” while unit masses and the source-to-
  proxy operator transport remain unproved.

## 7. Residual obligations after the source gate

The operator-source gate is complete.  Phase 3 must still establish, rather
than cite away:

1. the concrete fiber trace's faithfulness, normality, and semifiniteness;
2. the exact block `L^1` calculation for `C_f` and its unit-mass divergence;
3. the trace-ideal holomorphy and locally uniform trace-log convergence for
   `K_s`;
4. infinite transverse Hilbert multiplicity in the ordinary-trace control;
5. the unit-mass provenance and the full source/proxy transport certificate.

Items 4–5 are not repaired by determinant exactness.  In particular, the
zero-mode construction remains base-blind and arbitrary-clock compilable even
when its right-half-plane trace-log identity is exact.
