# Claims–Evidence Matrix — Paper 48

## Evidence types

- **Formal proof** means a self-contained argument from the frozen positive-vertex
  operator and standard trace-ideal facts.
- **Independent certificate** means a record emitted by proof auditor `P`; it is
  an audit of the formal argument, not a substitute for that argument.
- **Finite control** means a cutoff, digit tensor, shell computation, or mutation
  test.  It can falsify a formula or detect an implementation defect, but it
  cannot prove an infinite ideal-membership statement.
- **Bounded search** means only that the directed source search found no exact
  match.  It is not evidence of priority.

## Matrix

| ID | Manuscript claim | Formal support | Machine support | Status and prose ceiling |
|---|---|---|---|---|
| C1 | The one-digit matrix \(C_b=(\mathbf 1_{a+c<b})\) has singular values \([2\sin((2j-1)\pi/(4b+2))]^{-1}\). | Row reversal turns \(C_bC_b^*\) into \((\min(i,j))\); the inverse tridiagonal recurrence gives the sine spectrum. | Both finite lanes enclose the same 8,010 one-digit singular values with zero center discrepancy. | **Proved finite lemma.** No novelty claim; finite matrix results are background controls. |
| C2 | Every unweighted radix-shell block has the exact nonzero-singular-value factorization stated in the paper, including \(A_{kk}\simeq C_{b-2}\otimes C_b^{\otimes k}\). | Direct digit-coordinate permutation, deletion of zero rows/columns, and tensor multiplicativity. | 420 direct weighted shell norms lie inside independently constructed endpoint envelopes; exact ranks and supports agree. | **Proved shell lemma; independently checked.** The finite agreement is validation only. |
| C3 | For all integers \(b\ge2\), all \(1\le q<\infty\), and \(\sigma=\Re s\), \(B_{b,s}\in S_q\) iff \(\sigma>\max\{1,\log_b\kappa_{b,q}\}\). | Uniform weighted comparison plus summation gives sufficiency; a positive-density column gives the universal wall; orthogonal pinching gives the digit wall. | Auditor `P` accepts `INF-SIGMA-WALL` and `INF-DIGIT-WALL`; endpoint mutations M001–M007 are killed by their exact consumers. | **Main theorem.** Strict inequalities are mandatory. Never cite finite cutoff behavior as its proof. |
| C4 | The full binary nonmembership range \(\kappa_{2,q}2^{-\sigma}\ge1\) is rejected by adjacent paired shells because all binary same-shell blocks vanish; equality is the exceptional endpoint that this construction repairs. | \(C_0=0\), exact adjacent-shell norm \(\|A_{2j+1,2j}\|_{S_q}=\kappa_{2,q}^{2j}\), and block compression \(\left(\begin{smallmatrix}0&X_j\\X_j^*&0\end{smallmatrix}\right)\).  The same paired-shell lower bound is nondecaying at equality and grows when \(\kappa_{2,q}2^{-\sigma}>1\). | The finite census contains 180 binary adjacent rows and zero binary same-shell output rows; mutation M004 is killed. | **Proved exceptional binary necessity mechanism.** Do not reuse the \(b\ge3\) same-shell proof at \(b=2\), and do not describe paired shells as treating equality only. |
| C5 | Boundedness, compactness, and Hilbert–Schmidt membership are equivalent to \(\sigma>1\); trace class is equivalent to \(\sigma>\alpha_b=\log_b\|C_b\|_{S_1}>1\). | \(\kappa_{b,2}^2=b(b+1)/2<b^2\); column wall; \(|\det C_b|=1\) and strict AM–GM give \(\tau_b>b\). | Auditor `P` certifies the strict domains. The tabulated \(b=2,3,4,5\) values are deterministic evaluations of the exact formula. | **Corollary of C1–C3.** Decimal values illustrate exact expressions and do not define the theorem. |
| C6 | In \(\sigma>1\), \(\det_2(I-zB_{b,s})\) is entire in \(z\) and has the local trace-power logarithm for \(r\ge2\); ordinary trace/determinant require \(\sigma>\alpha_b\). | Hilbert–Schmidt membership, trace-class powers, finite-shell convergence, and absolute majorization by \(B_{b,\sigma}\). | Auditor `P` accepts `INF-DET2-DOMAIN`; determinant-domain mutation M014 is killed. | **Proved domain statement.** No completed \(s\)-plane function, functional equation, or target divisor is claimed. |
| C7 | The trace is the positive-vertex digit-restricted Dirichlet series; it vanishes structurally only for \(b=2\).  Least periods are \(\{2,3,\ldots\}\) for \(b=2\) and all positive integers for \(b>2\). | Delete the zero word; characterize loops by \(2d<b\); use distinct powers \(b^j\) as pairwise carry-free support witnesses. | Auditor `P` accepts `INF-TRACE-LPS`; direct and automaton lanes agree on finite trace supports and witnesses. | **Proved support/domain ledger.** Positivity is asserted only on the real trace-class half-line; no complex zero-free or Artin–Mazur-zeta claim. |
| C8 | The implementation realizes the preregistered finite controls without detected inconsistency. | Not a theorem claim. | Two disjoint lanes each emit 1,965 rows; 39 atomic mutations and 76 physical/adversarial instances have zero survivors; normal/hostile independent replays pass for States A and B. | **Finite validation only.** Report exact census and limitations; never use “machine-certified proof” wording. |
| C9 | The paper’s eligible delta is the infinite, weighted, all-radix classification and its endpoint/trace/period bookkeeping after subtracting finite carry, Pascal, Boolean, and disjointness ownership. | Explicit source and ownership firewall. | Source/type mutations M008, M021–M027 are killed; bounded search found no exact same-quantifier hit. | **Conditional positioning.** Say “the bounded search did not find”; never say “first,” “novel,” or “exhaustive.” |

## Forbidden inference shortcuts

1. A PASS status, a proof-auditor record, or a zero-survivor mutation suite is
   not the mathematical proof; the manuscript must contain the proof.
2. Finite-prefix singular values do not imply membership of the infinite
   operator in any Schatten ideal.
3. Kummer’s theorem is a prime-radix comparator only; the all-radix source is
   defined directly by carry-free addition.
4. The zero-completed matrix \(C_b^{\otimes L}\) is a control, not a finite
   restriction of an infinite source containing vertex zero.
5. A nonzero complex trace value cannot be inferred from positive
   coefficients, and least-period support cannot be inferred from a possibly
   cancelling complex trace.
