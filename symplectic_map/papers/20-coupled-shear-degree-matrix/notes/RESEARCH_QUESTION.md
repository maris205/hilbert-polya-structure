# Paper20 — Research Question and Scope

**Working title:** *Coupled Hamiltonian Shear Degree Matrices in \(\mathbb A^4\): an asymmetric \(g\ge5\) family*

**State:** proof-first source design; no manuscript, experiment, build, or publication artifact is authorized.

## Research question

For an algebraically closed field \(K\) of characteristic zero and an integer \(g\ge5\), consider the canonical shears on \(\mathbb A^4_K\), with coordinates \((q_1,q_2,p_1,p_2)\),

\[
 V_g=q_1^2q_2^2+q_1^g,\qquad
 W_g=p_1^2p_2^2+p_2^g,
\]
\[
 S_g(q,p)=(q,p+\nabla V_g(q)),\qquad
 T_g(q,p)=(q+\nabla W_g(p),p),\qquad
 F_g=T_g\circ S_g.
\]

The principal question is:

> Can the algebraic degree of every iterate \(F_g^n\) be proved exactly, from a finite two-phase Newton-face/degree cone, by a coupled nonnegative matrix whose Perron root is not the product of the two individual shear degrees?

The proposed answer is yes for this explicit family and only for the stated hypotheses. The target identity is

\[
 \deg(F_g^n)=e_2^{\mathsf T}C_g^n\binom11\quad(n\ge1),
 \qquad
 C_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix},
\]
and hence

\[
 \lambda_1(F_g)=\rho(C_g)=g+1+2\sqrt g=(\sqrt g+1)^2.
\]

Each shear has algebraic degree \(g-1\), so the comparison quantity is \((g-1)^2\). For \(g\ge5\),
\[
 (\sqrt g+1)^2 < (g-1)^2,
\]
which records a coupled degree-matrix effect, not a claim about every symplectic map.

## Exact subquestions

1. Do the two shears preserve the standard symplectic form and remain polynomial automorphisms with explicit polynomial inverses?
2. On which literal cone of degree vectors do the selected Newton faces dominate every competing monomial, including the carried coordinate?
3. Does the full step (not a half-step) have the matrix \(C_g=B_gA_g\), and is the cone forward invariant for all \(g\ge5\)?
4. Do positivity and characteristic zero rule out coefficient cancellation in every iterate?
5. Is the Perron class both reachable from \((1,1)\) and visible to the total-degree functional?
6. Which parts are genuinely new relative to Papers 12–19 and to the established two-dimensional Hénon degree-product background?

## Definitions fixed before proof

For a polynomial \(h\), \(\deg h\) is total degree. For a polynomial map, \(\deg f\) is the maximum coordinate degree and
\[
 \lambda_1(f)=\lim_{n\to\infty}(\deg f^n)^{1/n}
\]
when the limit is established by the displayed recurrence. The degree vector \(u_n\) always refers to the two \(q\)-coordinates after the complete iterate \(F_g^n\). The intermediate vector \(v_{n+1}\) refers to the two \(p\)-coordinates after the first shear in the next complete step. This phase distinction is part of the theorem, not notation that can be silently changed.

The Newton rows are face exponents of the displayed monomials, not arbitrary Jacobian or gradient matrices:
\[
 A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\qquad
 B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix}.
\]
The first row of \(A_g\) comes from \(q_1^g\), the second from \(q_1^2q_2^2\); the first row of \(B_g\) comes from \(p_1^2p_2^2\), the second from \(p_2^g\). A proof must re-check the selector inequalities rather than treating these rows as free input.

## In scope

- The fixed word \(T_g\circ S_g\) and the fixed potentials above.
- All integers \(g\ge5\), over algebraically closed characteristic-zero fields.
- The positive-coefficient specialization displayed above, together with the explicitly stated positive-coefficient open set only when the same leading-face and no-cancellation proof is supplied.
- The two-dimensional degree cone, its exact ratio map, matrix products, Perron calculation, symplecticity, and polynomial automorphism inverses.
- A bounded literature comparison and a finite collision matrix.

## Out of scope and automatic STOP conditions

- Arbitrary sparse potentials, arbitrary shear words, arbitrary coefficients, or positive characteristic.
- Any headline for \(g<5\), a one-dimensional reduction, or a block/separable map.
- A generic finite-fan theorem, a theorem for all symplectic polynomial automorphisms, or a claim that every Newton selector closes finitely.
- Topological entropy, arithmetic degrees, periodic points, traces, invariant curves, centralizers, torus translates, or effective orbit counts.
- A claim that the map is not conjugate to a product in every possible coordinate system; the defensible claim is non-block coupling in the displayed support and a non-product comparison with \((g-1)^2\).

The design is **STOP** if any selector inequality becomes an equality, if a carried coordinate is not dominated, if a coefficient cancellation is possible, if the degree functional does not see the Perron class, or if a purported generalization is not reduced back to this literal family.

## Evidence and permission boundary

The theorem is intended to be self-contained. External sources are used only for bounded context and collision checking; they are not evidence for the displayed recurrence. No experiments, CAS search, numerical orbit computation, file build, source lock, transport, or publication action is authorized in this package.
