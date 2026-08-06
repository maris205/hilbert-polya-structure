# R401-VAL Protocol Amendment V2 — Parameter-Aware Monodromy Gate

## 1. Scope and reason for the amendment

This document is a narrow amendment to the frozen
`R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md`.  The composite protocol called
**R401-VAL-V2** consists of

1. the original protocol with SHA-256
   `d00d95f32ddfe4420da2cdac46ef1a3bb39bb3ea2277a21a9776652794a20d82`;
2. this amendment;
3. the unchanged analytic proofs A4.11a and A4.11b.

All original claim boundaries, coverage obligations, strict endpoint margin,
status logic, Krawczyk inclusion requirements, phase-cover tree, global-cover
tree, and independent-checker obligations remain in force.  This amendment
replaces only the literal *raw interval-width* interpretation of hard gate 4
in Section 8 and makes its independent Poincare construction explicit.

The correction is necessary because the stability determinant is not
constant in the parameter.  Existing high-accuracy diagnostics give

\[
 D(0)\approx3.8627220,
 \qquad
 D(0.1)\approx3.8632714.
\]

Consequently, a nontrivial parameter slab has a genuine determinant range.
Requiring the raw range enclosure on every useful slab to have width at most
\(2^{-30}\) confuses physical parameter variation with numerical remainder.
It would force extremely small slabs without strengthening the mathematical
identity being checked.

This amendment does **not** relax the determinant lower bound, the identity
residual, or any orbit-coverage gate.  It requires a more informative proof
object: a shared-parameter Taylor model whose polynomial records the genuine
variation and whose interval remainder records numerical uncertainty.

## 2. Shared parameter coordinate

For every closed parameter slab

\[
 E_j=[\epsilon_j^-,\epsilon_j^+]
\]

define the exact affine coordinate

\[
 \epsilon=\epsilon_j^0+r_j\eta,
 \qquad
 \epsilon_j^0=\frac{\epsilon_j^-+\epsilon_j^+}{2},
 \qquad
 r_j=\frac{\epsilon_j^+-\epsilon_j^-}{2},
 \qquad
 \eta\in[-1,1].
\]

The endpoints, midpoint, and radius must be stored as exact dyadic or rational
numbers.  A repeated ordinary interval occurrence of \(\epsilon\) is not a
Taylor model and does not preserve the dependency required by this gate.

## 3. Replacement for hard gate 4

On every certified slab, independently construct, along the same validated
implicit periodic branch \(z_{0,j}(\eta),T_j(\eta)\),

\[
 \begin{aligned}
 D_{\Pi,j}(\eta)&\in \bar p_{\Pi,j}(\eta)+\bar R_{\Pi,j},\\
 D_{M,j}(\eta)&\in \bar p_{M,j}(\eta)+\bar R_{M,j},
 \end{aligned}
\]

where \(\bar p_{\Pi,j},\bar p_{M,j}\in\mathbb Q[\eta]\) have exact rational
coefficients, \(0\in\bar R_{\Pi,j},\bar R_{M,j}\), and the barred remainders
contain every truncation, flow, rounding, and coefficient-enclosure error.
If a producer first obtains interval coefficients \(C_k\), it must select
exact rational centers \(\bar c_k\) and absorb

\[
 \sum_k(C_k-\bar c_k)[-1,1]^k
\]

into the corresponding barred remainder before applying any width gate.
Coefficient uncertainty may not be hidden outside the remainder budget.  The
models must be validated on the implicit branch for every \(\eta\), not fitted
to sample values or formed from only the explicit occurrence of \(\epsilon\).

This section completely replaces the raw-width, range-intersection, and raw
residual numerical clauses of the original Section 8 hard gate 4.  Its
nonzero flow-tangent, symplecticity, and even unit-multiplier obligations
remain unchanged.  The replacement conditions are:

1. **remainder width**
   \[
   \operatorname{diam}\bar R_{\Pi,j}\le2^{-30},
   \qquad
   \operatorname{diam}\bar R_{M,j}\le2^{-30};
   \]
2. **identity residual as a shared-parameter model:** define the unique
   residual proof object by subtracting the two polynomials *before* taking
   their common-parameter range,
   \[
   \mathcal E_j=
   \operatorname{range}_{\eta\in[-1,1]}
   \bigl(\bar p_{\Pi,j}-\bar p_{M,j}\bigr)(\eta)
   +\bar R_{\Pi,j}-\bar R_{M,j},
   \]
   and require
   \[
   \boxed{0\in\mathcal E_j\subset[-2^{-28},2^{-28}].}
   \]
   Separately ranging the two polynomials and then subtracting those ranges
   is forbidden because it discards the shared \(\eta\) dependency.  This
   single condition is the V2 replacement for both the original intersection
   and residual clauses;
3. **strict stability on the complete slab**
   \[
   \inf\bigl(\bar p_{\Pi,j}([-1,1])+\bar R_{\Pi,j}\bigr)>3,
   \qquad
   \inf\bigl(\bar p_{M,j}([-1,1])+\bar R_{M,j}\bigr)>3;
   \]
4. **coefficient and remainder replay:** the independent checker reconstructs
   both polynomial ranges and both remainders from the archived flow and
   variational proof objects; it does not trust printed coefficients or
   Boolean pass flags.

The polynomial ranges are allowed to be wider than \(2^{-30}\), because they
represent verified physical variation.  A producer that does not implement
Taylor models may still satisfy the gate by subdividing until its raw interval
enclosures obey the original width bounds; that is a valid but potentially
expensive special case.

## 4. Independent construction of \(D_\Pi\)

The two determinant routes may share the same validated orbit and monodromy
enclosure, but they may not use the same final algebraic formula.

In the normal-coordinate ordering

\[
 z=(Q_-,Q_+,P_-,P_+),
\]

the positive turning section is \(P_+=0\).  Eliminate \(Q_+\) on the energy
surface and embed section coordinates \((Q_-,P_-)\) by

\[
 D\iota=
 \begin{pmatrix}
 1&0\\
 -K_{Q_-}/K_{Q_+}&-K_{P_-}/K_{Q_+}\\
 0&1\\
 0&0
 \end{pmatrix}.
\]

For \(h(z)=P_+\), the event-time projection at the return is

\[
 \mathcal P
 =I-\frac{X_K(z_T)e_{P_+}^{T}}
 {e_{P_+}^{T}X_K(z_T)}.
\]

Let

\[
 L=\begin{pmatrix}1&0&0&0\\0&0&1&0\end{pmatrix}
\]

select the \((Q_-,P_-)\) coordinates.  The derivatives in \(D\iota\) are
evaluated at the initial point \(z_0\), while \(\mathcal P\) is evaluated at
the return point \(z_T\).  Define

\[
 M=D_z\Phi_\epsilon^{\,T_\gamma(\epsilon)}(z_0)
\]

as the derivative with the integration time held fixed.  The event-time
derivative enters only through \(\mathcal P\) and must not be included a
second time in \(M\).  The independently formed
section derivative and determinant are

\[
 D\Pi=L\mathcal P M D\iota,
 \qquad
 D_\Pi=\det(I_2-D\Pi).
\]

The denominator signs in \(D\iota\) and \(\mathcal P\) must be certified by
the original connected energy-derivative and oriented-section gates.  The
second route remains

\[
 D_M=4-\operatorname{tr}M.
\]

The checker must replay the event projection, energy elimination, two-by-two
determinant, and full-monodromy trace separately before comparing their Taylor
models.

## 5. Validated-flow producer and precision replication

The preferred production engine is a validated Taylor/Lohner implementation
with a C1 variational flow, such as a pinned CAPD build.  A successful archive
must record:

- the exact CAPD commit and build configuration;
- compiler, MPFR, GMP, and interval-backend versions;
- Taylor order and step-control policy;
- all rational root boxes and Krawczyk preconditioners;
- sufficient Taylor/Lohner data to replay inclusion and remainder bounds.

The original requirement for separate runs at at least 128-bit and 256-bit
precision remains.  A double/FILIB computation is useful as a non-claiming
implementation smoke but cannot by itself satisfy the production precision
gate.  Arb may serve as an independent arithmetic/replay implementation, but
a custom Arb integrator must separately justify its Picard enclosure and
Taylor remainder theorem.

## 6. Status boundary for local milestones

A strict parameterized Krawczyk inclusion on only one slab is recorded in the
manifest's `milestone_status` field as `PASS_LOCAL_SLAB_SMOKE`.  A pointwise
inclusion at one exact \(\epsilon\) is similarly recorded as
`PASS_LOCAL_POINT`.  Neither milestone is a `final_status`, and neither
licenses a lower bound on
\(\delta_{\rm tr}\), because neither closes the contiguous parameter branch,
the root-box complement, the phase-cover tree, or the global shell cover.

Only the original `PASS_FULL` or `PASS_ENDPOINT` statuses, evaluated under
this composite V2 protocol and namespaced as, for example,
`R401-VAL-V2/PASS_FULL`, can place the R401 cell strictly inside the proved
theorem domain.

The V2 production namespace is
`results/r401_validated_theorem_domain_v2/`.  Its manifest must bind the base
protocol, this amendment, and both analytic proofs separately:

```json
{
  "protocol_id": "R401-VAL-V2",
  "protocol_components": {
    "base_protocol_sha256": "d00d95f32ddfe4420da2cdac46ef1a3bb39bb3ea2277a21a9776652794a20d82",
    "amendment_sha256": "FROZEN_AFTER_REVIEW",
    "radial_proof_sha256": "b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb",
    "warped_proof_sha256": "71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8"
  },
  "milestone_status": null,
  "final_status": "R401-VAL-V2/PASS_FULL"
}
```

The placeholder amendment hash is replaced only in a separate freeze record;
the frozen amendment itself is not self-edited to contain its own hash.

Failure to close a Taylor remainder or identity residual because of wrapping
is `R401-VAL-V2/INCONCLUSIVE`.  A hash, rounding, replay, or certificate
integrity failure is `R401-VAL-V2/INVALID`.  A rigorously demonstrated failure
of the deliberately strong \(D>3\) auxiliary bound retains
`R401-VAL-V2/PROTOCOL_BOUND_FAILED`.  No local milestone status produces a
\(\delta_{\rm tr}\) lower bound.
