# Paper 23 — Final Proof-First Proposal

## Title

**Four-Mode Hamiltonian Product Shears Beyond Cubic Collapse: Exact Degree
Growth and Quartic Perron Subfamilies**

## Lifecycle status

Source-design author proposal only.  Candidate review passed before this
package, but the ten source-design files still require a fresh independent
audit.  This proposal is not a source lock, paper plan, manuscript, build, or
release authorization.

## Headline theorem

Let $K$ be a characteristic-zero field and let $g\ge10$ be an integer.  Put

$$
V_g(q)=q_1^2q_2^2q_3^2q_4^2+q_1^g+q_2^{g-1},
$$

$$
W_g(p)=p_1^2p_2^2p_3^2p_4^2+p_3^{g-1}+p_4^g,
$$

and define

$$
S_g^+(q,p)=(q,p+\nabla V_g(q)),\qquad
T_g^+(q,p)=(q+\nabla W_g(p),p),\qquad
F_g=T_g^+\circ S_g^+.
$$

Then $F_g$ is a polynomial symplectic automorphism.  Four strict gradient
support selectors persist on the explicit sufficient ratio cone

$$
\mathcal K_g=left\{
u_1(1,x,y,z)^{\mathsf T}:
u_1>0,
1\le x\le\frac{g-1}{g-2},
1\le y\le z\le\frac{g-1}{g-2}y,
y+z<\frac{g-5}{2}
\right\}.
$$

They yield

$$
A_g=
\begin{pmatrix}
g-1&0&0&0\\
0&g-2&0&0\\
2&2&1&2\\
2&2&2&1
\end{pmatrix},
\qquad
B_g=
\begin{pmatrix}
1&2&2&2\\
2&1&2&2\\
0&0&g-2&0\\
0&0&0&g-1
\end{pmatrix},
$$

and

$$
C_g=B_gA_g=
\begin{pmatrix}
g+7&2g+4&6&6\\
2g+6&g+6&6&6\\
2g-4&2g-4&g-2&2g-4\\
2g-2&2g-2&2g-2&g-1
\end{pmatrix}.
$$

For the ordinary seed $\mathbf1$, the actual phase degrees satisfy

$$
v_{n+1}=A_gu_n,\qquad
u_{n+1}=C_gu_n,\qquad
u_n=C_g^n\mathbf1.
$$

Positive integer coefficients and characteristic zero prevent leading-form
cancellation.  For every $n\ge1$, the fourth $q$ coordinate is uniquely
maximal among all eight coordinate degrees, while $n=0$ is tied.  Therefore

$$
\deg(F_g^n)=e_4^{\mathsf T}C_g^n\mathbf1\quad(n\ge0),
\qquad
\lambda_1(F_g)=\rho(C_g).
$$

The characteristic polynomial is

$$
\begin{aligned}
R_g(t)={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
&+(12g^3-70g^2+126g-72)t
+9(g-1)^2(g-2)^2.
\end{aligned}
$$

For $g\equiv3\pmod5$, it reduces to the irreducible polynomial
$t^4-2t^3-t^2+1$ over $\mathbf F_5$.  Thus
$g=13,18,23,\ldots$ gives pairwise distinct quartic Perron first dynamical
degrees.

## Public contribution boundary

The contribution is the concrete conjunction of four staggered selectors,
removal of the Paper 22 common unit sector, an exact visible quartic matrix,
and an infinite irreducible quartic Perron subfamily.  Gradient shears,
weighted supports, matrix recurrences, Perron–Frobenius, Cayley–Hamilton,
modular irreducibility, and the abstract support-kernel lemma are reused
machinery.

## Proof architecture

1. Differentiate the potentials; write inverses and the symmetric-Hessian
   symplectic calculation.
2. List all eight support rows and read $A_g,B_g$ in phase order.
3. Derive four selector gaps, with the second phase evaluated at $A_gu$.
4. Place the ordinary seed in $\mathcal K_g$ and prove each selector strict.
5. Compute $C_gu$ in normalized coordinates and prove all six target faces.
6. Prove base carry, later first-phase carry, second-phase carry, and
   positive-leading-form survival.
7. Prove the fourth complete row beats the other three, use $C_g-A_g>0$ to
   beat all final $p$ rows, and obtain the exact scalar degree.
8. Derive the characteristic polynomial from its principal minors and apply
   Cayley–Hamilton and Perron–Frobenius.
9. Exclude every linear and quadratic factor modulo five; prove infinitude
   and pairwise distinctness.
10. State the common-kernel explanation, calculate $R_g(1)$, and isolate the
    $g=9$ failure and all anti-claims.

## Planned 24–28 content pages

| Section | Target pages |
|---|---:|
| introduction, theorem, and bounded related work | 3 |
| exact family, symplecticity, supports, and escape signature | 4 |
| four selector faces and the sufficient ratio cone | 5 |
| invariance, carry, and leading forms | 6 |
| visibility and exact degree | 3 |
| quartic spectrum and modulo-five subfamily | 4 |
| boundary, limitations, and comparison | 2 |
| **target** | **27** |

Every theorem-critical argument must appear locally.  Page count excludes
references and lifecycle/governance records.

## Citation and novelty boundary

The citation ledger may use only the R1-verified records and their recorded
access levels until a later citation stage is authorized.  Positioning must
credit Papers 20--22 as direct methodological predecessors and must cite the
general weak-Perron and dimension-four affine-triangular neighbors.  The only
safe novelty sentence is that no direct collision with the complete frozen
package was located within the bounded search.

## Hard exclusions

- $g\le9$ validity or globally optimal threshold;
- maximal/necessary cone or all-chamber classification;
- sign changes, arbitrary coefficients/supports, reversed order, or positive
  characteristic;
- quartic minimal polynomial for every $g$;
- every-full-rank-profile-implies-quartic;
- novelty of reused machinery;
- general realization, minimality, sparsity, non-conjugacy, entropy,
  integrability, genericity, periodicity, or unrelated arithmetic claims;
- computational proof or absolute priority.

## Permission boundary

This proposal completes no lifecycle gate by itself.  Only a fresh independent
reviewer may decide whether the exact ten-file source-design package passes.
Until then, no lock, plan, manuscript, bibliography, figure, code, build, PDF,
release, registry edit, submission, upload, transport, message, identity
disclosure, or other external effect is authorized.
