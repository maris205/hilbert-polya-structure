# Paper20 — Final Proof-First Proposal

**Status:** `CONDITIONAL DESIGN GO`; internal source-design only. No manuscript,
experiment, build, transport, or publication action is authorized.

## Headline theorem (literal scope)

Let \(K\) be algebraically closed of characteristic zero and let \(g\ge5\) be
an integer. On \(\mathbb A^4_K\) with coordinates \((q_1,q_2,p_1,p_2)\), set
\[
 V_g=q_1^2q_2^2+q_1^g,
 \qquad W_g=p_1^2p_2^2+p_2^g,
\]
\[
 S_g(q,p)=(q,p+\nabla V_g(q)),\qquad
 T_g(q,p)=(q+\nabla W_g(p),p),\qquad F_g=T_g\circ S_g.
\]
Then \(F_g\) is symplectic and polynomially invertible, and
\[
 \deg(F_g^n)=e_2^{\mathsf T}
 \begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}^{n}
 \binom11 \quad(n\ge1),
\]
so
\[
 \lambda_1(F_g)=(\sqrt g+1)^2.
\]
The elementary shears each have degree \(g-1\), and the strict comparison
\((\sqrt g+1)^2<(g-1)^2\) holds for \(g\ge5\). “Non-product” is used only in
this degree comparison and in the connected mixed support in the displayed
coordinates.

## Proof architecture

1. **Canonicality:** symmetric Hessians prove preservation of
   \(dq_1\wedge dp_1+dq_2\wedge dp_2\); triangular formulas give inverses.
2. **Actual Newton rows:** the selected rows are
   \(A_g=((g-1,0),(2,1))\) and \(B_g=((1,2),(0,g-1))\), tied to the four
   displayed gradient monomials.
3. **Two-phase selector:** for \(r=u_2/u_1\in[1,(g-2)/2)\), the \(S\)-phase
   selects \(q_1^g\) and the mixed \(q_1^2q_2^2\); the resulting ratio
   \(v_2/v_1=(2+r)/(g-1)\) makes the \(T\)-phase select \(p_1^2p_2^2\) and
   \(p_2^g\).
4. **Cone induction:**
   \[
   r\longmapsto f_g(r)=\frac{(g-1)(2+r)}{g+3+2r}
   \]
   maps the cone into itself for \(g\ge5\). The carried coordinates are
   strictly lower degree.
5. **No cancellation:** all displayed coefficients are positive integers and
   every selected face has a strict degree gap; characteristic zero keeps the
   leading coefficients nonzero.
6. **Complete-step matrix:** \(C_g=B_gA_g\), not the off-diagonal matrix of
   two half-steps. The total degree is observed by \(e_2\), and the positive
   Perron class is reachable from \((1,1)\).
7. **Perron calculation:** trace \(2g+2\), determinant \((g-1)^2\), and
   discriminant \(16g\) give \(\rho(C_g)=(\sqrt g+1)^2\).

The complete proof and all inequalities are in `notes/PROOF_PACKAGE.md`.

## Required formal artifacts

Before any manuscript drafting, the following artifacts must be written and
checked by an independent reviewer:

- a monomial-to-row table for all four selected gradient coordinates;
- the two endpoint inequalities and the carried-coordinate inequalities;
- the ratio-map endpoint calculation for every symbolic \(g\ge5\);
- the coefficient/no-cancellation induction over characteristic zero;
- the total-degree visibility inequalities for \(q_2\) against all other
  coordinates;
- the exact collision table and bounded citation ledger;
- a line-by-line anti-claim/STOP audit.

No numerical orbit or CAS output can replace any artifact.

## Literature and collision boundary

The package acknowledges the plane degree-product baseline, richer
higher-dimensional degree-growth examples, spectral-radius definitions of
dynamical degree, and a nearby four-dimensional coupled-Hénon hyperbolicity
literature. Those sources are background only; see
`notes/CITATION_VERIFICATION.md` and `notes/NOVELTY_ASSESSMENT.md`.

## Explicit anti-claims

This proposal does not cover arbitrary supports, arbitrary coefficients,
positive characteristic, arbitrary shear words, all symplectic polynomial
automorphisms, finite-fan closure in general, topological/arithmetic entropy,
periodic points, traces, torus geometry, centralizers, invariant curves, or
non-conjugacy to products in arbitrary coordinates.

## Permission boundary

Authorized now: write exactly the ten source-design markdown files in this
directory and perform read-only consistency checks on them. Not authorized:
`main.tex`, `PAPER_PLAN.md`, source locks, transport bytes, build directories,
experiments, web uploads, citation APIs, or independent review. The package
must stop after the author self-audit and wait for the parent to commission
review.
