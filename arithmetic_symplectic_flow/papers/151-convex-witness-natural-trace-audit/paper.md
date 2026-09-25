# Three natural trace obstructions for the convex witness map

**Paper ID:** 151-convex-witness-natural-trace-audit  
**Candidate ID:** ASFS-20260915-CWT01  
**Date:** 2026-09-15  
**Status:** STOP — AREA KOOPMAN NONCOMPACT; LOCAL INDEX ZERO; GAUSSIAN DIAGONAL DIVERGENT.  
**Route:** Bounded owner-level A2 audit; formal coordinates UNASSIGNED;
Route B NOT INVOKED.

## Abstract

This analytic-owner contract uses the full all-integer convex-witness
symplectic map and unit roof, with a newly specified full-area Koopman
operator and two local trace proposals. Its intrinsic periodic set is
rechecked, not transferred as an operator theorem: there is one primitive
rounded-binary-length packet for each prime and none for composites.
Nevertheless, the full-area Koopman operator is a nonzero multiple of a
unitary operator on an infinite-dimensional space and is not compact.
Every isolated prime periodic point has local fixed-point index zero,
including all repetitions. An explicit normalized Gaussian regularization
of the graph/diagonal integral already diverges at the integer-2 fixed
point, with rate epsilon to the power minus one half. These are three
distinct, exactly scoped obstructions. Finite fixed-point counts and the
ordinary orbit zeta remain meaningful but are not Hilbert traces or a
Fredholm determinant of the proposed Koopman operator. No universal
no-go theorem for other analytic spaces or regularizations is asserted.

## 1. Candidate identity and same-object ledger

The [version-1 analytic-owner card](candidate-card.md) was frozen before
this audit. For every integer n>=2 set

\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad
b(n,k)=\sum_{\substack{2^k\le d<2^{k+1}\\d<n}}1_{\{d\mid n\}},
\quad 1\le k\le K_n.
\tag{1}
\]

With cyclic successor k^+, the entire carrier and map are

\[
M=\coprod_{\substack{n\ge2\\1\le k\le K_n}}\mathbb R^2_{n,k},
\qquad \omega|_{M_{n,k}}=dq\wedge dp,
\]
\[
F(n,k,q,p)
=(n,k^+,p,2p-q+(p-1)^2+b(n,k)).
\tag{2}
\]

Let mu be full componentwise Lebesgue area. The newly frozen main analytic
proposal is

\[
\mathcal H=L^2(M,\mu),\qquad
U_s f=e^{-s}f\circ F,\qquad s\in\mathbb C.
\tag{3}
\]

The proposed central object is the ordinary Fredholm determinant
det(I-U_s), only if its required operator-ideal hypotheses hold.

| Item | Exact owner | Boundary |
| --- | --- | --- |
| Geometry | Full (2), including all real states and all integer components | No selected prime carrier or periodic support |
| Arithmetic source | Local divisor witnesses in (1), executed in the continuous recurrence | No prime table, zero data, or fitted prime weight |
| Symbolic lineage | Prime/composite divisor-exclusion constraints -> autonomous dyadic phases -> nonlinear Hénon-form force | Constraint deformation, not a conjugacy to the original causal sieve |
| Roof and flow | tau=1 and the mapping torus of (2) | Complete unit macrotime; not exact log p |
| Measure and operator | Full mu and (3), without smoothing | No finite invariant probability is asserted |
| Periodic data | Every full-state periodic point, cyclic packet identification and all repetitions | Rechecked below |
| Alternative local proposals | Fixed-point index and explicit graph/diagonal Gaussian integral | Neither is silently equated with counting |
| Ordinary zeta | Re-derived from the complete packet ledger | Not the determinant in (3) |
| Later owner | No Hamiltonian, contact, quantum or spectral-target construction | Route B NOT INVOKED |

The displayed geometry and roof equal those of [145](../145-convex-witness-henon-sieve/paper.md).
The new ID records the newly fixed analytic contract; it does not retroactively
equip 145 with an operator theorem. The base is two-dimensional and
symplectic; its three-dimensional mapping torus is not thereby symplectic
or Hamiltonian.

## 2. Question and claim boundary

Do any of the three natural analytic proposals in this card directly
realize the ordinary unweighted prime-packet zeta?

The strongest supported answer is a scoped negative: the area Koopman
proposal is noncompact; the ordinary local indices are zero; the stated
positive Gaussian diagonal regularization diverges. The complete
arithmetic periodic ledger is not refuted by these analytic failures.
No claim concerns all transfer operators, all distributional extensions,
all anisotropic spaces, all regularizations, or every possible future
geometric deformation.

## 3. Inputs, provenance and proof conventions

Only the all-integer witness formula (1), the fixed square force in (2),
the unit roof and full area are inputs. All coefficients are fixed before
the audit. There are no zero comparisons, parameter searches, prime-data
fits, finite orbit experiments or numerical regularization runs.

The functional-analytic principles used are the elementary change-of-
variables formula, the sequential criterion for compactness, and the
standard inclusion of trace-class operators in compact operators.
The topological principle used is homotopy invariance of Brouwer degree
on a bounded open set whose boundary avoids zero. The local fixed-point
index convention is degree(I-G,U,0). The Gaussian limit uses the
dominated convergence theorem. These named standard principles are not
new research results or claims supported by model review.

## 4. Exact proofs

### Proposition 1 — Full geometry and the relevant periodic ledger

The map F is a global smooth symplectomorphism, preserves mu, and has the
complete periodic set

\[
\{(\ell,k,1,1):\ell\text{ prime},\ 1\le k\le K_\ell\}.
\tag{4}
\]

Each prime label ell contributes one oriented primitive packet of length
K_ell to the unit-roof suspension and repetition lengths r K_ell.

**Proof.** Given (n,k',Q,P), take the preceding phase k. The inverse
geometric coordinates are
(2Q+(Q-1)^2+b(n,k)-P,Q). Also
dq' wedge dp'=dp wedge ((2+2(p-1))dp-dq)=dq wedge dp.
The countable disjoint union is a smooth Hausdorff second-countable surface,
and the map permutes its components preserving area.

For a full m-cycle, the phase condition requires K_n to divide m. Write
q_t=x_t and p_t=x_{t+1}. Summing

\[
x_{t+2}-2x_{t+1}+x_t
=(x_{t+1}-1)^2+b(n,k_t)
\tag{5}
\]

around the cycle gives a sum of nonnegative terms equal to zero. Hence
all x_t=1 and every visited witness count vanishes. Each phase is visited,
so no integer d with 2<=d<n divides n, which is equivalent to n prime.
Conversely a prime makes every witness zero and (1,1) follows the cyclic
phases. The least full period is exactly K_n because the phases themselves
have that least period. This exhausts all real states and all periods.
The globally invertible unit-roof mapping torus is complete: any finite
flow time makes only finitely many crossings. Cyclic identification yields
one primitive oriented packet, and each repetition adds the same roof
K_n again. QED.

Along (4), the geometric derivative is

\[
A=\begin{pmatrix}0&1\\-1&2\end{pmatrix}=I+N,\qquad N^2=0.
\tag{6}
\]

Thus every returning iterate has det(I-A^m)=0. Isolation in (4) is a
nonlinear result and is compatible with this degenerate linearization.

### Proposition 2 — Full-area Koopman noncompactness

For every complex s, U_s is bounded on all of H, with
norm exp(-Re(s)), but is not compact and therefore not trace-class.

**Proof.** Area preservation gives

\[
\|f\circ F\|_2^2=\int_M|f(Fx)|^2\,d\mu(x)
=\int_M|f(y)|^2\,d\mu(y)=\|f\|_2^2.
\tag{7}
\]

Composition with F^{-1} is its inverse, so U_0 is unitary. The space is
infinite-dimensional; for example normalized indicators of pairwise
disjoint unit squares within one component form an orthonormal sequence
(e_j). The sequence (U_0 e_j) is again orthonormal. For distinct i,j,

\[
\|U_s e_i-U_s e_j\|_2=e^{-\operatorname{Re}s}\sqrt2>0.
\tag{8}
\]

It has no convergent subsequence although (e_j) is bounded, contradicting
the sequential criterion for compactness. A trace-class operator is
compact, so U_s is not trace-class. QED.

Every power U_s^m is similarly a nonzero scalar multiple of a unitary
operator. Consequently making Re(s) large does not provide a trace-class
half-plane. In fact |U_s|=exp(-Re(s))I has infinite positive trace on H.
The proposed ordinary Fredholm determinant is therefore not supplied by
this construction. No regularized determinant is introduced as a repair.

### Proposition 3 — All local return indices are zero

For every prime label ell, each of its phase points, and every m=rK_ell,
the isolated local fixed-point index of F^m on that phase plane is zero.

**Proof.** On a prime fibre all witness counts vanish. The geometric
return is H_0^m, where the following family is used only as a proof
homotopy:

\[
H_\eta(q,p)=(p,2p-q+(p-1)^2+\eta),\qquad \eta\ge0.
\tag{9}
\]

The point z=(1,1) is the only fixed point of H_0^m, by the same cycle sum.
Take a bounded open ball U around z. Its compact boundary avoids fixed
points, so min_{x in boundary U}|x-H_0^m(x)| is positive. Continuity in
eta, uniformly on this compact boundary, gives an eta_0>0 for which
I-H_eta^m never vanishes there when 0<=eta<=eta_0.

If eta>0 and H_eta had an m-periodic point, summing its recurrence would
give

\[
0=\sum_{t=0}^{m-1}(x_{t+1}-1)^2+m\eta>0,
\tag{10}
\]

a contradiction. Homotopy invariance of Brouwer degree now gives

\[
\operatorname{ind}(H_0^m,z)
=\deg(I-H_0^m,U,0)
=\deg(I-H_{\eta_0}^m,U,0)=0.
\tag{11}
\]

The boundary choice and eta_0 are made for each fixed m; no uniform
all-period perturbation estimate is required. This applies to each phase
and each repetition separately. QED.

Thus an ordinary local-index sum cannot assign the weight +1 to these
fixed points. This is not a global Lefschetz theorem on the noncompact
surface: no such global theorem or cohomological trace has been assumed.
The auxiliary homotopy neither changes the candidate nor transfers a
result from a different action.

### Proposition 4 — An explicit Gaussian diagonal divergence

Work in the n=2 component, which has one phase and b=0. Fix once and for
all a nonnegative smooth compactly supported cutoff psi(q,p) that equals
1 near (1,1). For epsilon>0 define the two-dimensional Gaussian with
standard deviation epsilon in each coordinate by

\[
\delta_\varepsilon(y)
=\frac1{2\pi\varepsilon^2}
 \exp\left(-\frac{|y|^2}{2\varepsilon^2}\right),\qquad
I_\varepsilon=\int_{\mathbb R^2}
\psi(q,p)\delta_\varepsilon(F(q,p)-(q,p))\,dq\,dp.
\tag{12}
\]

Then

\[
I_\varepsilon\sim C\varepsilon^{-1/2},\qquad
C=\frac1{2\pi}\int_{\mathbb R^2}
 \exp\left(-\frac{a^2+(a+b^2)^2}{2}\right)\,da\,db
\in(0,\infty).
\tag{13}
\]

**Proof.** Set u=p-q and v=p-1; the absolute coordinate Jacobian is one,
and the two components of F(q,p)-(q,p) are exactly (u,u+v^2).
With u=epsilon a and v=sqrt(epsilon)b, (12) becomes

\[
\varepsilon^{1/2}I_\varepsilon
=\frac1{2\pi}\int_{\mathbb R^2}
\psi(1+\sqrt\varepsilon b-\varepsilon a,\,
     1+\sqrt\varepsilon b)
\exp\left(-\frac{a^2+(a+b^2)^2}{2}\right)\,da\,db.
\tag{14}
\]

The cutoff tends pointwise to 1 and is uniformly bounded. Completing
the square gives

\[
\frac{a^2+(a+b^2)^2}{2}
=(a+b^2/2)^2+b^4/4.
\tag{15}
\]

Integration in a therefore leaves sqrt(pi) exp(-b^4/4), integrable over
the real line. This provides a dominating integrable function after
the a integration, or directly an integrable majorant on the plane.
Dominated convergence yields (13); the integral is strictly positive.
QED.

The failure already occurs locally at one intrinsic fixed point. For
the weighted kernel of U_s this local expression acquires the nonzero
scalar e^{-s}, which does not remove divergence. The claim concerns
exactly the Gaussian family, normalization and cutoff in (12). It does
not establish that every renormalization, finite-part prescription,
distributional framework or alternative analytic space is impossible.

### Proposition 5 — Counting survives but is a different operation

The full fixed-point count is finite at every positive integer m and is

\[
N_m=\#\operatorname{Fix}(F^m)
=\sum_{\substack{\ell\ \mathrm{prime}\\K_\ell\mid m}}K_\ell.
\tag{16}
\]

It yields the ordinary full-packet product

\[
Z(s)=\exp\left(\sum_{m\ge1}\frac{N_m}{m}e^{-sm}\right)
=\prod_{\ell\ \mathrm{prime}}(1-e^{-sK_\ell})^{-1}
\quad\text{for }\operatorname{Re}s>\log2.
\tag{17}
\]

**Proof.** Equation (4) gives (16). K_ell<=m limits ell to finitely many
integer labels, including the separately guarded label 2. Regrouping
the term of a primitive K_ell-cycle at m=rK_ell gives
K_ell/(rK_ell)=1/r, proving the formal series identity in (17).
For Re(s)=sigma>log2 the all-integer bound

\[
\sum_{\ell\ \mathrm{prime}}e^{-\sigma K_\ell}
\le e^{-\sigma}+\sum_{j\ge1}2^j e^{-\sigma j}<\infty
\tag{18}
\]

and the repetition factor 1/(1-e^{-sigma}) justify absolute local
uniform convergence and regrouping. QED.

This proof uses no periodic-support restriction in (3). If one instead
introduces the algebraic full-set comparator
V=C^{(M)}, T e_x=e_{F x}, its finite diagonal count for T^m is (16).
That operation is a combinatorial count in the point basis, not a
trace-class Hilbert trace. Its counting-measure Hilbert completion would
again make T unitary on an infinite-dimensional space. It cannot repair
Proposition 2.

## 5. Results and comparison of the five operations

| Operation | Result for this exact contract | What is not licensed |
| --- | --- | --- |
| Full fixed-point cardinality | Finite N_m in (16) | Hilbert or flat trace identity |
| Ordinary orbit product | Equation (17), owned by the unit roof | det(I-U_s) |
| Full-area operator trace | U_s and its powers are not trace-class | Taking their ordinary Fredholm determinant |
| Local fixed-point index | Zero at every surviving point and repetition | Replacing the unweighted count by local index |
| Explicit Gaussian diagonal integral | Divergence C epsilon^(-1/2) at n=2 | Unspecified finite part or a universal regularization no-go |

In particular the finite positive count N_1=2, from integer labels 2 and
3, does not become either an index sum of 2 or a finite Gaussian graph
trace. The five operations are mathematically different even when they
are motivated by the same frozen map.

## 6. Controls and adverse findings

- **Arithmetic control:** the zero-witness comparator has one K_n packet
  in every integer fibre by (5). The same full-area noncompactness and
  convex local-index obstruction remain. These analytic failures are not
  evidence that the prime selector itself was externally supplied.
- **Geometry control:** a positive eta in (9) removes periodic points by
  (10), while the boundary-safe degree homotopy verifies their zero index.
  It is used only to compute the original local invariant.
- **Ownership control:** no prime-only Hilbert subspace, orbit-representative
  basis, modified roof, smoothing operator or analytic weight is supplied.
- **Robustness control:** the Gaussian leading constant is the same for
  every fixed compact smooth cutoff equal to 1 near the point. The proof
  is an exact limit, not a fitted divergence rate. Other regularization
  families are not covered.
- **Simpler-parent / PROVES_TOO_MUCH control:** every invertible
  area-preserving map on an infinite-dimensional L2 space has the same
  noncompact Koopman obstruction. This does not prohibit transfer
  operators on other spaces and supplies no arithmetic explanatory power.
- **Enumeration control:** (5) covers all real states, all n and all
  periods. Finite experimental cutoffs are not used to establish (16).

## 7. Gate assessment

| Gate or proposal | Scoped evidence | Status / boundary |
| --- | --- | --- |
| Same geometric and roof owner | Explicit inverse, symplecticity and completeness rechecked | ESTABLISHED for this contract |
| Operational arithmetic mechanism | Complete prime-only cycle-sum classification | ESTABLISHED; stronger natural target clock remains outside this audit |
| Owner A1 | Full packets, phases, repetitions and degeneracy rechecked | ESTABLISHED; not a formal Route coordinate |
| Ordinary scalar A2 | Equation (17) in its stated half-plane | ESTABLISHED; not the proposed operator determinant |
| Full-area Koopman determinant | Noncompactness for every finite complex s | SCOPED FAIL |
| Ordinary local-index replacement | All local return indices equal zero | SCOPED FAIL as unweighted counting replacement |
| Frozen Gaussian diagonal proposal | Explicit local divergence | SCOPED FAIL for this regularization |
| Other analytic spaces or prescriptions | Not supplied or tested | OPEN; no universal negative claim |
| Formal Route A / Route B | No target-divisor or B protocol undertaken | UNASSIGNED / NOT INVOKED |

## 8. Conclusion and portfolio decision

**Stop** these specific natural trace and determinant proposals. Their
decisive obstructions are exact, so there is no reason to iterate cutoffs
or tune the Gaussian width numerically. **Retain** the complete arithmetic
packets and ordinary product as positive results. **Fork** any changed
space, smoothing prescription, force, roof or analytic weight with an
explicit new owner; this paper does not authorize such a substitution.

The same-object ledger remained intact. An honest negative A2 operator
audit leaves the earlier geometric and scalar results true and leaves
all formal Route coordinates unassigned.

## Reproducibility and research disclosure

All mathematical inputs and proof steps are in this paper and the
[candidate card](candidate-card.md). There were no numerical experiments,
datasets, fitted parameters, external uploads or publication artifacts.
The [claim ledger](claim-ledger.md) separates each positive and negative
statement; the [evidence index](evidence/README.md) records verification.
The research note was generated and checked with model assistance under
the authorized repository workflow. Model review is not independent
human peer review. No human-subject study, financial disclosure, funding
or human authorship contribution is inferred by this note.
