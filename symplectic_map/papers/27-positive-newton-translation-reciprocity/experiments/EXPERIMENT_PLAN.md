# Paper 27 source-design experiment plan

## Status and governing boundary

This is a proof-first theory article, not an empirical or numerical study.
The source-design stage is authorized by
BATCH07_PAPER27_SOURCE_DESIGN_AUTHORIZED and is limited to a written audit
plan.  No code, data, numerical run, CAS certificate, build root, figure,
manuscript, or PDF is created here.  “Experiment” means a falsifiable
mathematical check that must be displayed as a proof; it is not computational
evidence.

The coefficient field is characteristic zero, the degree space is ordered
real, and the headline support class is
\[
 E_V,E_W\subset\mathbb Z_{\ge2}^{\,r},\qquad r\ge3,
\]
with finite, nonempty, collected supports and nonzero coefficients.  The map
is
\[
 S_V(q,p)=(q,p+\nabla V(q)),\quad
 T_W(q,p)=(q+\nabla W(p),p),\quad F=T_W\circ S_V .
\]

## Claim-driven proof checks

1. **Scope and realization.**  State the collected-support convention and
   keep coefficient-field symbols separate from real degree vectors.  For
   every invoked edge, exhibit a positive integer pair satisfying the score,
   carry, target, and reflected inequalities.  Disjoint variable blocks with
   algebraically independent leading tuples realize the pair.
2. **Leading-form survival.**  For each positive exposed face, group the
   Hessian determinant by row-labelled tuples and choose a generic secondary
   weight with a unique minimizer \(\alpha_0\).  The unique lowest group has
   coefficient
   \[
   c_{\alpha_0}^{\,r}(-1)^r(1-|\alpha_0|)\prod_i\alpha_{0i}\ne0 .
   \]
   Apply the Jacobian criterion and injective substitution; check fresh
   blocks, carried blocks, and inverse subtraction signs.  Record the
   boundary \(V=(q_1+q_2+q_3)^3,\ W=(p_1-p_2)^3\), where a half-step
   cancellation occurs outside the positive-support class.
3. **Phase map.**  For unique \(\alpha,\beta\), derive
   \[
   A_\alpha=\mathbf1\alpha^{\mathsf T}-I,\quad
   B_\beta=\mathbf1\beta^{\mathsf T}-I,\quad
   v=A_\alpha u,\quad u'=B_\beta v .
   \]
   Then derive
   \[
   v=h_V(u)\mathbf1-u,\qquad
   u'=u+\delta\mathbf1,\qquad
   \delta=h_W(v)-h_V(u).
   \]
   Strict carry is exactly \(\delta>0\); \(\delta\le0\) stops the branch.
4. **Global selector audit.**  Put \(u(t)=u_0+t\mathbf1\) and
   \(g(t)=h_V(u(t))-t\).  Since every support total exceeds one, \(g\) is
   strictly increasing.  Verify
   \[
   (\beta-\eta)\cdot v(t)
   =(|\beta|-|\eta|)g(t)-(\beta-\eta)\cdot u_0 .
   \]
   Unequal-total walls cross at most once; equal-total walls are invariant.
   Count at most \(d_V-1\) V and \(d_W-1\) W changes.
5. **Reflection.**  With coordinate reversal \(R\), verify
   \[
   B_{R\alpha}R=RA_\alpha,\qquad A_{R\beta}R=RB_\beta .
   \]
   Necessity is the \(n=1\) restriction on \(U_e,V_e\); sufficiency is
   edge-by-edge induction with reflected score/carry checks.
6. **Local perturbation.**  On one normalized compact strict pair core, verify
   selected-minus-new margins on \(\pi_u(C_e^+)\), \(A_\alpha u\), \(Ru\),
   and \(RA_\alpha u\), plus typed source-pair margins.  Conclude one forward
   and one reflected inverse leading step only.  Do not test or claim a
   target-core, multi-edge, C1-to-C2, or all-iterate stability result.
7. **Exact fixture.**  Print and rederive the \(r=3\) matrices, products,
   gaps, carries, reflected identities, and six canonical span seeds.  Show
   C1→C2→C2 and the reflected path; use the omitted \(\gamma\) to show local,
   not global, reflection closure.

## Acceptance and falsification gates

The proof package is accepted only if every item has a literal equation or
quantified lemma, all strict inequalities are typed, and each failure
boundary is stated beside the theorem.  A cancellation, sign/order mismatch,
missing carry, unsupported span upgrade, collision, or scope leak is a hard
FAIL and requires an append-only correction followed by a fresh review.  No
computational output can close such a finding.

## Proposed proof-only allocation

The frozen article is planned for 25.7 content pages (working range 24--28;
references, appendices, governance, and discovery history excluded):
abstract 0.4, introduction 1.8, related work 1.5, setup/theorem 2.8,
Hessian/Jacobian transport 4.2, translation and wall bound 3.8, reflected
reciprocity 3.5, local lower-ideal lemma 1.4, fixture and boundaries 3.8,
limitations/reproducibility 1.8, conclusion 0.7.  Every theorem-critical
argument remains in the main text.

## Reproducibility and authorization

The only reproducible objects at this stage are the displayed definitions,
inequalities, proofs, and exact integer arithmetic.  A later symbolic check,
if separately authorized, must be run at most once, recorded as a
falsification aid, and must not replace a proof.  There is no GPU, network,
upload, submission, hosting, identity disclosure, or external side effect.

BATCH07_PAPER27_SOURCE_DESIGN_EXPERIMENT_PLAN_FROZEN
