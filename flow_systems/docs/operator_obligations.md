# Operator Obligations

This registry records Route-B obligations by **one typed operator**.  Passing
coordinates from different operators or from a scalar identity with no
operator owner may not be combined.  Evidence labels follow
`skills/route-b-evaluator.md`.

## Active operator ledger

| Candidate / operator | B1 definition | B2 self-adjointness | B3 spectral type | B4 arithmetic trace / Weil form | B5 divisor | Current boundary |
|---|---|---|---|---|---|---|
| `DEN-EF-PACKET-ACTION-GRPD-P` / no packet operator frozen | packet Hausdorff/LCH and the standard completion are unavailable — `NOT_TESTABLE` | `NOT_TESTABLE` | `NOT_TESTABLE` | no packet trace or Weil form | no divisor | Packet primary question is `NOT_TESTABLE`; local orbit representations cannot be promoted without a same-map packet theorem. |
| `DEN-EF-ORBIT-ACTION-GRPD` / one-orbit groupoid representations | the C*-algebra and induced/regular representations are explicit, but no closed spectral generator with an HP domain is frozen | `NOT_TESTABLE` | `NOT_TESTABLE` | no same-object arithmetic trace or Weil form | no divisor | A representation-theoretic completion is not a natural quantization; Route-B invocation is false. |
| `DEN-EF-ORBIT-GRPD-REG-TRACE` / `M_L^reg, Tau_L` | the fixed bicommutant and FNS trace are exact, but a trace host is not a closed spectral generator | `NOT_TESTABLE` | no spectral target is posed; the exact trace is return-blind away from zero | `Tau_L(a_f)=L f(0)` only; no arithmetic repetition trace or Weil form | no divisor | Normality cannot be borrowed by the return-sensitive character trace; Route-B invocation is false. |
| `DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE` / `pi_theta, tau_theta` | the induced representation and full l.s.c. C*-trace domain are defined, but neither is a closed self-adjoint HP generator | `NOT_TESTABLE` | no HP spectral type is posed; normal extension to the fixed regular completion is refuted | exact local character comb only; no packet/global operator trace or Weil form | no divisor | The fixed-map obstruction is local, and singular corner states are not full trace extensions; Route-B invocation is false. |
| `DEN-EF-GRPD-TIME-RETURN-POS` / scalar `Theta_+`, no operator | no Hilbert space, closed operator, or operator trace is defined | `NOT_TESTABLE` | `NOT_TESTABLE` | exact coefficient-one scalar Radon ledger only; no operator owner or Weil form | no divisor | Scalar A1 credit cannot be transferred to a local trace, packet completion, determinant, or Route-B record. |
| `DEN-WITT-Z-FIN` / none frozen | required inputs absent — `NOT_TESTABLE` | `NOT_TESTABLE` | `NOT_TESTABLE` | `NOT_TESTABLE` | `NOT_TESTABLE` | Route-B entry unauthorized; first define a source-intrinsic trace-bearing operator. |
| `DEN-WITT-PACKET-DECOMP-MASS-FAM` / selected decomposable algebra, no HP operator | a faithful normal semifinite trace host is defined, but no closed spectral generator is frozen | `NOT_TESTABLE` | `NOT_TESTABLE` | no determinant owned by this record | no divisor | A rigorous operator-algebra proxy is not a natural quantization; Route-B invocation remains forbidden. |
| `DEN-WITT-PACKET-DECOMP-RETURN-DIST-M` / component translations | component circle unitary actions exist, but the positive-time Radon record is not a global trace of one frozen closed operator | `NOT_TESTABLE` | `NOT_TESTABLE` | exact typed return ledger only; no determinant | no divisor | Its Route-A A1 credit cannot be combined with the zero-mode record's A2 credit. |
| `DEN-WITT-PACKET-DECOMP-K0-M1` / holomorphic bounded zero-mode family `K_s` | `K_s` and its exact bounded/affiliated trace domains are defined, but it is not a densely defined self-adjoint Hamiltonian | `NOT_TESTABLE` | ordinary Hilbert multiplicity is infinite; no HP spectral problem is posed | branch-fixed scalar only on `Re(s)>1`; not a spectral trace of an HP operator | no continuation or completed divisor | Route-B entry unauthorized; the exact scalar is base-blind and arbitrary-clock compilable. |
| `MOD-GEO` / automorphic Laplacian | natural same-quotient host exists | standard self-adjoint realization exists | correct Selberg host, but wrong target counting/support | no rational-prime trace under frozen clock | no completed-$\xi$ identity | Retained only as exact calibration; Route A is rejected for the rational-prime target, so Route B cannot rescue it. |
| `FF-FROB-SUSP-P1-F2-KOOPMAN-P1` / $A_K=-i\,d/du$ | `B1_COMPLETE_OPERATOR_DEFINITION` — `PROVED` | `B2_SELF_ADJOINT` — `PROVED` | `B3_FAIL` — `PROVED` | not invoked in Paper 5 | not invoked in Paper 5 | Limited early audit stops at Gate C: $\sigma_{\rm p}=(2\pi/\log 2)\mathbb Q$, every point is infinitely degenerate, and $\sigma=\sigma_{\rm ess}=\mathbb R$. |
| `FF-FROB-OPERATOR-OWNERSHIP-P1-F2` / Koopman $A_K$ | `B1_COMPLETE_OPERATOR_DEFINITION` — `PROVED` | `B2_SELF_ADJOINT` — `PROVED` | `B3_FAIL` — `PROVED` | `B4_FAIL` — native Lefschetz trace belongs to $\Phi$, not $A_K$ | `B5_FAIL` — native factor is not completed $\xi$ | Full limited audit: `ROUTE_B_REJECTED`; see the Stage-6 YAML. |
| same parent / étale Frobenius $\Phi$ | finite-dimensional graded $\mathbb Q_\ell$-linear action, not a canonical complex Hilbert operator | no canonical positive complex inner product or self-adjoint HP realization supplied | finite eigenvalue ledger $\{1,2\}$, not a Riemann energy spectrum | exact native Lefschetz trace and graded determinant — `PROVED` | native $1/((1-t)(1-2t))$, not completed $\xi$ | Exact determinant owner and positive control; its credits cannot be transferred to $A_K$. |

## Reusable obligations

| ID | Obligation | Why it is mandatory | Smallest acceptable evidence |
|---|---|---|---|
| `OP-OWN-1` | Name the operator that owns every asserted trace and determinant. | Equal scalar functions can arise from orbit, fixed-point, cohomological, or spectral ledgers with different owners. | One space, action, domain/test class, trace theorem, and determinant convention in a common source lock. |
| `OP-MAP-1` | Prove the exact same-map transport before promoting a local trace or obstruction to a packet or global owner. | A common source clock does not transport topology, completion, disintegration, trace domains, normality, or multiplicity. | Named maps at both completions, proved restriction/disintegration/compression identities, preserved domains, and an explicit ownership theorem. |
| `OP-NORM-1` | Distinguish a lower-semicontinuous C*-trace from a normal weight on a represented von Neumann completion. | Point-character traces can retain returns while being singular relative to diffuse dual Haar. | A fixed representation and bicommutant, an explicit extension map, and a finite-corner/decreasing-net argument or an equivalent normal-extension theorem. |
| `OP-DOM-1` | Specify the full dense domain and boundary conditions before spectral claims. | A formal differential expression is not a closed operator. | Graph domain, boundary traces, closedness/closability, and a core or equivalent theorem. |
| `OP-SA-1` | Prove self-adjointness, not just symmetry or unitarity of a finite approximation. | Real eigenvalues do not imply a self-adjoint infinite operator. | Deficiency/extension theorem, quadratic form, Stone generator, or explicit unitary equivalence. |
| `OP-SPEC-1` | Prove the actual spectral type and multiplicities. | Self-adjointness alone permits dense point spectrum and essential spectrum. | Compact resolvent or another precise target mechanism; spectral projections and essential spectrum audited. |
| `OP-HEAT-1` | Audit compactness and trace ideals before writing a spectral determinant. | Ordinary Fredholm and heat-zeta determinants require trace/compactness hypotheses. | Trace-class/nuclear theorem or an explicitly different regularization with a proved domain. |
| `OP-TRACE-1` | Derive prime-power weights from the same operator. | A native cohomological trace cannot be pasted onto a Koopman generator. | Distributional trace equality with test class, convergence, non-orbit terms, clock, phase, and multiplicity. |
| `OP-WEIL-1` | Tie any Weil-form compression to the same arithmetic/operator ledger. | A post-hoc Hermitian form proves too much and does not certify Hilbert–Pólya. | Intrinsic form/compression whose trace, second moment, and inertia are read from the same prime-power data. |
| `OP-DIV-1` | Prove a global completed-ξ determinant equality. | Finite divisor agreement or a native finite-field determinant is a different target. | Defined determinant, multiplicities, growth, continuation, and zero-free prefactor, globally. |

## Current hard stops

1. A positive component reweighting of the Koopman circle sum is a unitary
   diagonal change and cannot remove its essential spectrum or multiplicity.
2. Deleting the infinite zero eigenspace does not help: every nonzero rational
   frequency also has infinite multiplicity.
3. Adding a finite-dimensional Frobenius block to $A_K$ leaves
   $\sigma_{\mathrm{ess}}(A_K)=\mathbb R$ and the noncompact resolvent intact.
4. The substitution $t=2^{-s}$ creates vertical preimage lattices; it does
   not create additional physical eigenvalues of Frobenius or Koopman time.
5. A genuinely new cohomological flow, anisotropic transfer space, coupling,
   or boundary condition is a new candidate and must restart T0--T7 and
   B1--B5 rather than inherit coordinatewise credits.
6. A componentwise Radon return record and a zero-mode trace-log determinant
   on two typed proxy records cannot be spliced into one operator ledger.
7. A principal semifinite trace-log scalar is not, by itself, an ordinary
   Hilbert Fredholm determinant, a primitive-orbit Ruelle determinant, or a
   self-adjoint spectral determinant.
8. On the fixed one-orbit regular completion, dual-Haar normality comes with
   exact erasure of every nonzero return: `Tau_L(a_f)=L f(0)`.
9. The return-sensitive character trace has no normal extended-positive
   extension along that fixed map; singular corner-state extensions do not
   constitute an extension of the full unbounded trace.
10. The fixed-map obstruction cannot refute the packet primary question until
    packet Hausdorff/LCH and a same-map restriction/disintegration/compression
    theorem are proved.
11. The coefficient-one positive-time object `Theta_+` is a scalar Radon
    measure whose count comes from rational closed points; it is not a packet
    multiplicity, global trace, or spectral operator.

## Canonical next theorem

Construct a source-derived Hilbert or trace-space realization in which a
**single** closed operator carries the arithmetic return ledger and its exact
trace/determinant.  Prove its spectral type first; only then test rational-prime
weights, a Weil-form bridge, and a completed-ξ divisor.  Paper 7 narrows the
first step further: the transport must select the transverse measure and
cross-prime masses and must remain sensitive to packet geometry rather than
only to total probability mass and a prescribed clock list.

Paper 8 makes the immediate gate more precise: first prove or refute that the
restricted diagonal equivalence relation defining each inherited `Gamma_p` is
closed. Only a positive result may reopen the standard packet LCH completion
and a same-map restriction/disintegration/compression theorem selecting the
transverse measure and cross-prime masses. The fixed regular map is now a
negative calibration: its normal trace is return-blind, while its
return-sensitive point-character trace has no normal extension. The scalar
measure `Theta_+` does not discharge any of these operator obligations.
