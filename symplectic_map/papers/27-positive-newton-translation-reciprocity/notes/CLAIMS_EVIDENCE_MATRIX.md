# Claims--evidence matrix (source-design freeze)

The matrix separates theorem claims, proof obligations, fixtures, and
governance.  An external citation supplies context only; each promoted
mathematical claim has a self-contained algebraic evidence location.  A
“kill condition” is the exact observation that would force the claim to be
removed or narrowed.

| ID | Exact claim | Evidence / proof obligation | Status | Kill condition | Planned section |
|---|---|---|---|---|---|
| C1 | \(F=T_W\circ S_V\), with finite nonempty collected \(E_V,E_W\subset\mathbb Z_{\ge2}^r\), \(r\ge3\), over char-0 \(K\). | Definitions and support/field lock in E0052. | ASSUMPTION LOCK | Empty/uncollected support, zero coefficient, coordinate 0/1, mixed \(W\), char \(p\), or \(r<3\). | §3 |
| C2 | Every invoked edge has positive integer pair seeds and declared observable spans \(U_e,V_e\); algebraically independent leading tuples realize the pair. | Seed construction and span definitions in E0033/E0039; explicit fixture seeds. | DEFINITION / CONSTRUCTION | No integer seed, failed carry, or span asserted without a seed set. | §3 |
| C3 | A positive exposed face has a nonzero grouped Hessian determinant. | Generic secondary minimizer and coefficient \(c_{\alpha_0}^{\,r}(-1)^r(1-|\alpha_0|)\prod_i\alpha_{0i}\). | PROVE | Zero/unit coordinates, zero coefficient, or positive characteristic makes the displayed witness unusable. | §4 |
| C4 | Face-gradient tuples are algebraically independent and remain visible after substitution. | Jacobian criterion, injective substitution, pure powers, nonzero scalars, and signs. | PROVE | A face coefficient cancels, substitution is not injective, or a carry is non-strict. | §4 |
| C5 | Forward and inverse leading forms survive in the stated phase order; inverse subtraction changes no degree vector. | Direct \(F=T_W\circ S_V\) calculation and simultaneous block-visibility induction. | PROVE | Wrong phase order, uncollected terms, or missing fresh/carry margin. | §4 |
| C6 | The phase maps are \(v=A_\alpha u\) and \(u'=B_\beta v\), with \(A_\alpha=\mathbf1\alpha^{\mathsf T}-I\), \(B_\beta=\mathbf1\beta^{\mathsf T}-I\). | Componentwise gradient degree calculation. | PROVE | Exposed row not unique or a declared selector/carry inequality fails. | §3–4 |
| C7 | Every strict two-phase step is \(u'=u+\delta\mathbf1\), with \(\delta=h_W(v)-h_V(u)>0\). | \(v=h_V(u)\mathbf1-u\), followed by \(u'=h_W(v)\mathbf1-v\). | PROVE | Support leaves the positive-coordinate class or \(\delta\le0\). | §5 |
| C8 | Along an infinite strict branch, selector changes are at most \(d_V+d_W-2\). | \(g(t)=h_V(u_0+t\mathbf1)-t\) is strictly increasing; unequal-total walls cross once and equal-total walls are invariant. | PROVE | A claimed change occurs at a tie, a nonmonotone phase, or an uncounted total-degree class. | §5 |
| C9 | After the last selector change, \(t_{n+1}=\lambda t_n+\mu\), with \(\lambda=(|\alpha|-1)(|\beta|-1)\) and global-origin \(\mu=((|\beta|-1)\alpha-\beta)\cdot u_0\). | Expand \(\delta\) on \(u_0+t\mathbf1\). | PROVE | Phase is not stationary or \(t_0=0\) is replaced by an inconsistent origin. | §5 |
| C10 | Reflected inverse actions obey \(B_{R\alpha}R=RA_\alpha\), \(A_{R\beta}R=RB_\beta\). | Permutation-matrix identities and \(R_{\rm state}(u,w)=(Rw,Ru)\). | PROVE | Coordinate reversal is not fixed, or phase order/sign is swapped. | §6 |
| C11 | Phase-resolved reciprocity is necessary and sufficient edgewise on \(U_e,V_e\), with reflected score/carry checks. | \(n=1\) linear restriction for necessity; edge-by-edge induction for sufficiency. | PROVE | Only scalar totals agree, same-seed pair is not \(R_{\rm state}\)-fixed, or a proper span is promoted to full rank. | §6 |
| C12 | The lower-ideal statement preserves one forward and one reflected inverse leading step on one strict pair core only. | Four normalized compact projections and typed source-pair margins \(\min(\ell-\rho)\cdot x\ge\Delta>0\). | PROVE (LOCAL) | Any claim of target-core invariance, C1→C2 perturbation, multi-edge, or all-iterate stability. | §7 |
| C13 | The \(r=3\) support fixture realizes an unperturbed C1→C2→C2 strict path and reflected path. | Exact matrices, products, gaps, carries, \(R\)-identities, and six independent \(u\)-seeds. | FIXTURE | Arithmetic mismatch, nonpositive gap, or missing span determinant. | §8 |
| C14 | Hessian cancellation and missing-reflection examples delimit the hypotheses. | \(V=(q_1+q_2+q_3)^3,\ W=(p_1-p_2)^3\); \(R\gamma\notin E_W\); \(n=1\) span mismatch. | COUNTEREXAMPLE | If the example lies inside the headline class or does not cancel/mismatch as stated. | §6, §8 |
| C15 | No direct claim collision with P12–P26 or reserved P28–P31 axes was found in the bounded screen. | Claim-level matrix and source ledger; E0043 portfolio lock. | SCREENED | A primary source is found with the exact conjunction, or a reserved axis is silently imported. | §2, §9 |
| C16 | The article is proof-only, anonymous, and has no external effect at this gate. | E0052/E0053; experiment tracker; later source/publication locks. | GOVERNANCE LOCK | Any empirical evidence, CAS dependency, identity/path/provenance leak, upload, submission, or unauthorized file. | §9 |

## Required cross-links

* C1–C2 are defined in RESEARCH_QUESTION.md and PROOF_PACKAGE.md.
* C3–C5 require the grouped determinant and Jacobian arguments, not a generic
  coefficient assumption.
* C7–C9 use the same global origin \(u_0\); changing origin changes the
  displayed intercept and must be stated explicitly.
* C10–C11 compare phase-resolved vectors, never only their maximum coordinate
  or total degree.
* C12 retains the selected-minus-new sign convention on all four projections
  and stops after one step.
* C13 is illustrative arithmetic and cannot close C3, C8, or C11.
* C15 uses citations only to position the claim; it is not a priority or
  exhaustiveness statement.

BATCH07_PAPER27_CLAIMS_EVIDENCE_MATRIX_FROZEN
