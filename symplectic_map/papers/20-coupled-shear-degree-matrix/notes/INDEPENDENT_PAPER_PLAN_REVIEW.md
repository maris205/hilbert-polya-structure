# Paper20 — Independent Paper-Plan Review

Date: 2026-08-22 UTC

Project: `papers/20-coupled-shear-degree-matrix`

Role: post-author independent paper-plan auditor

## Verdict and scope

**PAPER_PLAN PASS — proof-first planning scope only.**

This report binds only the repaired, author-stopped plan at
`paper/PAPER_PLAN.md`. I did not modify the plan, source lock, source-design
files, or prior review receipts. This review authorizes no manuscript, TeX,
bibliography, code, experiment, figure, build, transport, upload, publication,
release, or priority claim.

## Exact plan identity

Two independent reads give:

- bytes: **22,064**;
- LF: **397**;
- SHA-256:
  `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3`;
- regular mode 0644, UTF-8, terminal LF, no CR, NUL, or BOM.

The earlier 22,006-byte snapshot is obsolete and is not reviewed here.

## Source-lock and artifact bindings

The plan records and independently matches:

- source lock `experiments/source_lock.json`:
  `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`,
  11,847 bytes, LF1;
- ten-author aggregate:
  `3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`,
  45,416 bytes and 873 LF;
- design-review receipt:
  `c4f456c8d9aee5ac9364abf91dc140e9a0261b09cf1922491a773e8c7d87f2c5`,
  9,484 bytes;
- source-lock review receipt:
  `b6ba83186b7e8c5db548376c5478260bb6d1b3e3d84d8ff0944f641c185a513a`,
  with terminal verdict `SOURCE_LOCK_PASS`.

The source lock remains byte-identical. `PAPER_PLAN.md` and this reviewer note
are downstream/out-of-band artifacts and do not enter the locked ten-file
aggregate.

## Theorem and formula replay

The plan preserves the literal family over an algebraically closed
characteristic-zero field, for every integer (g\ge5):

\[
V=q_1^2q_2^2+q_1^g,\qquad W=p_1^2p_2^2+p_2^g,
\]

\[
S(q,p)=(q,p+\nabla V(q)),\qquad
T(q,p)=(q+\nabla W(p),p),\qquad F_g=T\circ S.
\]

The four displayed coordinates are the correct gradients. The selected degree
rows and complete-step product are

\[
A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\qquad
B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},
\]

\[
C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]

For (r=u_2/u_1\in[1,(g-2)/2)), the first selector gap is
((g-1)u_1-(u_1+2u_2)>0). With (v=A_gu),
(v_2/v_1=(2+r)/(g-1)>2/(g-2)), so the second selected face is strict.
The ratio return map

\[
f_g(r)=\frac{(g-1)(2+r)}{g+3+2r}
\]

is increasing; (f_g(1)>1), and at (R=(g-2)/2) the cleared positive gap
is (g(g-4)). Thus the half-open cone is invariant for every allowed (g).

The old-term inequalities in L5 correctly distinguish the carried
(p)-degrees from the new intermediate vector. Positivity of all generated
coefficients plus characteristic zero and strict degree gaps is sufficient for
no cancellation; the plan correctly avoids claiming uniqueness of a leading
monomial. Since

\[
C_g-A_g=\begin{pmatrix}4&2\\2g-4&g-2\end{pmatrix}>0,
\]

the final (q)-degrees dominate the final (p)-degrees, and (q_2) is the
total-degree observable. Therefore

\[
\deg(F_g^n)=e_2^{\mathsf T}C_g^n(1,1)^{\mathsf T}\quad(n\ge1).
\]

The trace, determinant, and discriminant are (2g+2), ((g-1)^2), and
(16g), so

\[
\lambda_1(F_g)=\rho(C_g)=(\sqrt g+1)^2<(g-1)^2.
\]

The explicit (g=5) check is also correct:
(C_5=\left(\begin{smallmatrix}8&2\\8&4\end{smallmatrix}\right)) and
(\rho(C_5)=6+2\sqrt5<16).

## L1–L7 dependency audit

The seven proof obligations are complete and acyclic in the stated order:

1. L1 establishes the triangular inverses and symmetric-Hessian symplecticity.
2. L2 fixes the first selector and the carried-(p) base/induction gaps.
3. L3 uses (v=A_gu) for the second selector and carried-(q) gaps.
4. L4 closes the two-stage cone and componentwise growth.
5. L5 uses L2–L4 for old-term dominance and coefficientwise no-cancellation.
6. L6 uses L2–L5 for the exact recurrence and visible total degree.
7. L7 uses L6 and Perron–Frobenius for the dynamical-degree limit.

The plan keeps the mandatory phase equality (v_{n+1}=A_gu_n), excludes the
false single strict two-shear cone, and prevents the off-diagonal half-step
matrix from replacing (B_gA_g).

## Page arithmetic and drafting structure

The 13 substantive allocations are

`0.5+2.0+1.5+2.5+1.5+2.5+2.5+2.5+2.0+2.0+1.5+2.0+1.0`,

which sums exactly to **24.0 pages**, within the authorized 22–26 range. The
introduction now promises four falsifiable contributions and lists exactly
four. Proof obligations remain in the main body; references, acknowledgements,
and any optional appendix are outside the substantive count. No experiment or
computational appendix is introduced.

## Citation and collision boundaries

The citation scaffold now agrees with the locked source ledger:

- S01: planar degree-product/normal-form background;
- S02 and S03: higher-dimensional degree-growth context;
- S03 and S05: dynamical-degree and spectral terminology;
- S04: plane valuation/compactification history only;
- S06: nearest four-dimensional coupled-Hénon hyperbolicity neighbor;
- S07: optional, explicitly labeled survey context only.

C12 likewise uses only S03/S05 as context. No citation is proof authority for
the new recurrence, cone, symplecticity, Perron root, or priority.

All eight P12–P19 rows reproduce the locked `EMPTY` object-boundary result and
the plan explicitly states that this is bounded collision control, not an
exhaustive priority search. P1–P11 are not silently reclassified.

## Non-blocking editorial notes

Two local clarifications would improve a later manuscript without changing the
plan verdict. Section 3 can define the initial carried degree vector
(v_0=(1,1)^{\mathsf T}) before L2 uses that symbol; L2 already supplies the
value, so the induction is not ambiguous. Also, the reader-promise phrase
“exceptional set” is not attached to any theorem in this package and should not
be propagated into a draft unless a separately scoped definition is added.

## Anti-claims and permission gates

The plan carries forward the source-lock anti-claims: no arbitrary supports,
coefficients, or words; no positive characteristic; no generic finite-fan/all
symplectic-map theorem; no entropy equality, periodic/trace/torus theorem,
universal product non-conjugacy, numerical/CAS proof certificate, or absolute
novelty claim. The eight drafting STOP conditions preserve selector, phase,
coefficient, visibility, coupling, citation, and lifecycle failures.

The plan is the only author-side write in its stage. It does not modify the
source lock or enable `main.tex`, `references.bib`, code, data, figures,
results, build, transport, upload, publication, or release. No experiment or
symbolic/CAS run was performed. This independent note is the expected
post-author review artifact and does not broaden those permissions.

PAPER_PLAN_PASS
