# Claims–Evidence Matrix

## Frozen status

- Candidate: henon_primitive_cycle_cover_v1
- Primary claims: PC1 and PC2
- Atomic claims: C1–C20
- Source-proof authority: notes/PROOF_PACKAGE.md
- Literature authority: notes/CITATION_VERIFICATION.md
- Current lifecycle verdict: `SOURCE_LOCKED_V2 / PENDING_INDEPENDENT_R2 /
  NO_CODE / NO_RESULTS`
- Machine evidence: none
- Code/results/figures/manuscript: unauthorized

“Proved” below means proved in the author source package. It does not mean
that an independent Round-2 `SOURCE_LOCK_PASS` has been issued.

## Primary-claim map

| Claim | Exact statement | Atomic dependencies | Status |
|---|---|---|---|
| **PC1** | \(B_n\) is \(A\)-free rank \(d^n\); the generic actual block \(E_n\) is one degree-\(\nu\) field; its relative normalization \(S\) is geometrically integral and finite locally free rank \(\nu\), with \(S/aS=D_n\); \(S_0=S^{C_n}\) is finite locally free rank \(r\), has scalar fiber \(D_n^{C_n}\), and has geometric cycle monodromy \(S_r\) on a finite-étale open. | C1–C14 | PROVED_SOURCE_PENDING_REVIEW |
| **PC2** | \(\tau,\rho\in S_0\), \(K(\tau)=F=K(\rho)\), and their basis-free multiplication characteristic polynomials are irreducible of degree \(r\); \((2,2)\) is the explicit linear boundary. | C15–C20 plus C14 | PROVED_SOURCE_PENDING_REVIEW |

## Atomic claim matrix

| ID | Atomic claim | Evidence and location | Evidence class | Mandatory check |
|---|---|---|---|---|
| **C1** | The cyclic equations \(g_i=z_i^d+a z_{i-1}+c-z_{i+1}\) are exactly the orbit-coordinate equations for \(\operatorname{Fix}(H^n)\). | PROOF_PACKAGE Step 1; direct substitution \(H(z_i,z_{i-1})=(z_{i+1},z_i)\). | exact derivation | index convention modulo \(n\) |
| **C2** | The \(g_i\) form a monic Gröbner basis and \(B_n\) is \(A\)-free rank \(d^n\). | PROOF_PACKAGE Step 1; pairwise-coprime leading monomials \(z_i^d\). | exact derivation | monic division over \(A\), not a field-only argument |
| **C3** | \(B_n\otimes_AK\) is finite étale. | PROOF_PACKAGE Step 2; separable scalar generic fiber plus finite-free discriminant. | derivation with imported scalar separability | formal/actual distinction retained |
| **C4** | Actual exact-\(n\) points define a generic idempotent block \(E_n\) of dimension \(\nu=\sum_{e\mid n}\mu(n/e)d^e\). | PROOF_PACKAGE Step 2; Galois-stable clopen subset and Möbius inversion. | exact derivation | idempotent only on generic étale algebra |
| **C5** | \(E_n\) is one field. | PROOF_PACKAGE Step 3; scalar exact field, henselian finite-étale lifting, persistence of product idempotents. | derivation with Gao–Ou input | lifted idempotent equals actual block |
| **C6** | The integral closure \(S\) is finite over \(A\). | PROOF_PACKAGE Step 4; Stacks 07QW, 07QV, 035S. | standard commutative algebra | excellence/Nagata chain stated |
| **C7** | \(S\) is finite locally free of rank \(\nu\). | PROOF_PACKAGE Steps 4–5; normal surface is CM, miracle flatness. | exact derivation with standard CA | local dimensions and zero-dimensional fiber |
| **C8** | There is a unique height-one \(P\) over \((a)\), with \(e=1\), residue degree \(\nu\), and \(\operatorname{div}_S(a)=P\). | PROOF_PACKAGE Step 6; henselian exact block and valuation descent. | exact valuation derivation | no omitted prime or multiplicity |
| **C9** | \(S/aS\) is reduced and is exactly \(D_n\). | PROOF_PACKAGE Steps 6–7; \(R_0+S_1\), unique minimal prime, finite birational map, Gao–Ou normality. | exact derivation with imported normality | excludes closed-point nilpotents; no automatic base-change claim |
| **C10** | \(\operatorname{Spec}S\) is geometrically integral over \(\mathbb Q\). | PROOF_PACKAGE Step 8; constants inject into \(\operatorname{Frac}D_n\); Stacks 037P, 0322, 0FWF. | exact derivation | both geometric irreducibility and reducedness |
| **C11** | The time shift acts on \(S\) and \([E_n:E_n^{C_n}]=n\). | PROOF_PACKAGE Step 9; functorial normalization and Artin fixed-field theorem. | exact derivation | generic actual-period action only |
| **C12** | \(S_0=S^{C_n}\) is finite locally free rank \(r\), and invariants commute with arbitrary base change. | PROOF_PACKAGE Step 9; Reynolds idempotent and determinant-free projectivity. | exact derivation | use \(1/n\in A\) and image-of-idempotent argument |
| **C13** | \(S_0/aS_0=D_n^{C_n}\), the affine scalar orbit curve. | PROOF_PACKAGE Step 9, using C9 and C12. | exact derivation | affine notation; no projective claim |
| **C14** | On a dense finite-étale open, geometric monodromy on cycles is \(S_r\). | PROOF_PACKAGE Step 10; imported scalar \(C_n\wr S_r\) (Morton 1998, Theorem D/Theorem 10; Fakhruddin 2014, Theorem 3.2); \(G_{\rm special}\subseteq G_{\rm global}\); centralizer bound. | derivation with imported monodromy | verify exact-period factor, geometric constant field, and subgroup direction |
| **C15** | \(\tau,\rho\in S_0\), with \(\rho=\operatorname{tr}(M_{n-1}\cdots M_0)\). | PROOF_PACKAGE Step 11; integral coordinates and cyclic invariance of matrix trace. | exact derivation | \(\rho\) is not field trace or determinant |
| **C16** | For \(r>1\), \(\tau\notin K\). | PROOF_PACKAGE Steps 12–13; word-sum leading terms. Morton 1996, Corollary 3 (p. 335) and p. 336 independently give scalar fixed-field generation when \(d=2\). | exact formal-branch derivation with direct scalar prior-art overlap | \(d\ge3\) and binary cases both covered; no novelty credit for scalar \(d=2\) |
| **C17** | For \(r>1\), \(\rho\notin K\). | PROOF_PACKAGE Steps 12–13; leading inverse word products. Morton 1996, Corollary 1 and pp. 335--336 directly give scalar fixed-field generation for every \(d,n\). | exact formal-branch derivation with direct scalar prior-art overlap | independent of C16; derivative exponent/sign checked; no novelty credit for the scalar generator |
| **C18** | \(K(\tau)=F=K(\rho)\). | PROOF_PACKAGE Step 14; C14, C16, C17, and maximality of \(S_{r-1}<S_r\); Morton 1996 is an alternate scalar input for \(\rho\) in all degrees and \(\tau\) in degree two. | exact group/field derivation with disclosed alternate theorem input | non-base alone is insufficient; residual delta is the two-parameter lift and uniform \(\tau\) treatment |
| **C19** | Each \(\chi_s(T)=\det(T-m_s)\) is basis-free, belongs to \(A[T]\), and is irreducible degree \(r\). | PROOF_PACKAGE Step 15; determinant line, nonzero \(1\wedge s\wedge\cdots\), C18. | exact algebra derivation | generic irreducibility only; no fiberwise promotion |
| **C20** | For \((d,n)=(2,2)\), \(\nu=2,r=1,\tau=a-1,z_0z_1=(a-1)^2+c,\rho=4a^2-6a+4+4c\). | PROOF_PACKAGE Step 16; direct two-equation calculation. | exact derivation | not monodromy evidence |

## Imported theorem matrix

| Import | Exact role | Allowed consequence | Forbidden promotion |
|---|---|---|---|
| Gao–Ou scalar smoothness/irreducibility | \(D_n\) is geometrically integral and normal; scalar exact generic algebra is one field | C3, C5, C9, C10 | no Hénon normalization or monodromy attributed to Gao–Ou |
| Scalar full-centralizer monodromy for \(z^d+c\) | point group \(C_n\wr S_r\), cycle quotient \(S_r\) | scalar lower bound in C14 | distinguish Morton 1998 from the unrelated Morton 1996 Theorem D; use Fakhruddin for the geometric constant field; no direct global equality without restriction/centralizer proof |
| Morton 1996 scalar fixed-field generators | Corollary 1 and pp. 335--336 give \(\operatorname{Frac}(D_n)^{C_n}=\mathbb Q(c,\rho|_{a=0})\) for all \(d,n\); Corollary 3 and p. 336 give \(\mathbb Q(c,\tau|_{a=0})\) for \(d=2\) | alternate scalar input to C16--C18 and mandatory direct collision | no claim that PC2 invents either scalar generator; no automatic replacement for the two-parameter lift or the \(d\ge3\) \(\tau\) proof |
| Hutz formal dynatomic theory | warns that formal period may specialize to lower actual period | construction boundary in C4 | no actual-period family inferred on every fiber |
| Standard commutative algebra sources | excellence, finite normalization, CM, miracle flatness, henselian lifting, geometric integrality criteria | C5–C10 | no “method novelty” |

Cantat--Dujardin (2026), Section 3.2 and Theorems A/3.7, is an adjacent
observable boundary rather than an imported proof input. Its data are
formal-period trace multisets over finitely many periods, used to reconstruct
map parameters up to uniformly finite ambiguity. C15--C19 instead concern one
fixed actual-period cycle field and the value at one generic cycle. These
statements must not be conflated in either direction.

## Proof-versus-audit boundary

The theorem authority is the source proof plus a future independent review.
A future authorized symbolic audit may only challenge bounded identities and
known counterexamples. It may not:

- infer PC1 or PC2 from a finite \((d,n)\) table;
- scan neighboring degrees or periods;
- replace the all-\(d\) monodromy citation check;
- issue a proof verdict;
- use one implementation route to validate the other;
- treat the \((2,2)\) fixture as evidence beyond the boundary case.

No machine audit has been executed. The immutable independent Round-1 source
review returned `REPAIR_REQUIRED`; Round 2 must independently verify (i)
Morton 1996, Corollaries 1/3 and pp. 335--336, (ii) the direct scalar
generator collision for \(\rho\) in all degrees and \(\tau\) in degree two,
(iii) Cantat--Dujardin's formal-period multiset and finite-period
parameter-reconstruction scope, and (iv) the corrected v2 hashes and
lifecycle. None of those gates may be self-signed by the source author.

## Mandatory falsifier matrix

| ID | Falsifier | False inference rejected | Claim protected |
|---|---|---|---|
| **N1** | \(f_t(z)=z^2+t\), \(t=-3/4,z=-1/2\): formal period two but actual period one | FORMAL_IMPLIES_ACTUAL | C4 |
| **N2** | \(\mathbb Q[a,t]/(t^2-a)\) at \(a=0\) | GENERIC_ETALE_IMPLIES_REDUCED_FIBERS | C9 |
| **N3** | \(\mathbb Q[t^2,t^3]\subsetneq\mathbb Q[t]\) | SAME_FRACTION_FIELD_IMPLIES_EQUALITY_WITHOUT_NORMALITY | C9 |
| **N4** | \((d,n)=(2,2)\) | NONBASE_OR_NONTRIVIAL_MONODROMY_WHEN_R1 | C20 |
| **N5** | assert \(\tau\in K\) for all \(r>1\) | TAU_BASE_FUNCTION | C16 |
| **N6** | assert \(\rho\in K\) for all \(r>1\) | RHO_BASE_FUNCTION | C17 |
| **N7** | use \(G_{\rm global}\subseteq G_{\rm special}\) for the lower bound | REVERSED_SPECIALIZATION | C14 |
| **N8** | replace \(\rho\) with \(\operatorname{Tr}_{F/K}(\rho)\) or \((-a)^n\) | TRACE_CATEGORY_COLLAPSE | C15–C19 |

## Exact formula lock

\[
\nu_d(n)=\sum_{e\mid n}\mu(n/e)d^e,\qquad r_d(n)=\nu_d(n)/n.
\]

\[
M_i=
\begin{pmatrix}
d z_i^{d-1}&a\\
1&0
\end{pmatrix},
\qquad
\rho=\operatorname{tr}(M_{n-1}\cdots M_0).
\]

At \(a=0\), \(c=-q^{-d}\), \(z_i=q^{-1}v_i\), and
\(\epsilon=q^{d-1}\):

\[
v_i^d=1+\epsilon v_{i+1},
\]

\[
\tau=q^{-1}\left(\sum_i\omega_i+O(\epsilon)\right),
\]

\[
\rho=d^nq^{-n(d-1)}
\left(\prod_i\omega_i^{-1}+O(\epsilon)\right).
\]

For \(n=2\):

\[
\operatorname{tr}(M_1M_0)=u_0u_1+2a.
\]

For \((d,n)=(2,2)\):

\[
\tau=a-1,\qquad z_0z_1=(a-1)^2+c,\qquad
\rho=4a^2-6a+4+4c.
\]

## Novelty and lifecycle matrix

| Item | Locked disposition |
|---|---|
| Adjudicator | GO, novelty 6.8/10, size 7.4/10, proof confidence 0.74 |
| Dissent | STOP, novelty 4.5/10, size 3.9/10 |
| Corrected conservative novelty range | 4.8--5.5/10 after the low-period Hénon, Morton fixed-field, and Cantat--Dujardin comparisons; author-side/R1-informed risk estimate, not a replacement verdict |
| Corrected conservative standalone-size range | 4.5--5.5/10; PC1 carries most of the residual package and PC2 is narrower than first assessed |
| Conservative synthesis | five-layer package justifies source review; dissent unresolved |
| Cross-model novelty phase | unavailable; not simulated |
| Venue criteria | criteria_binding_unavailable |
| Independent source review | Round 1 `REPAIR_REQUIRED` preserved immutably; Round 2 required and pending |
| Implementation | not authorized |
| Registered execution | not authorized |
| Result/figure/manuscript | not authorized |

## Terminal wording lock

Safe:

> For the fixed normalized family \(H_{a,c}\), the relative normalization of
> the generic actual-period field has the exact affine scalar dynatomic fiber;
> its cycle quotient has full symmetric geometric monodromy, and each of two
> named observables separately generates the generic cycle field.

Unsafe:

- “the actual-period subscheme exists over every parameter”;
- “the cyclic action is free on every fiber”;
- “all fibers are smooth or reduced”;
- “this is the first dynatomic/trace/monodromy method”;
- “this invents the Hénon orbit-sum carrier or cyclic-polynomial method”;
- “this invents the scalar multiplier/orbit-sum primitive generators”;
- “this proves Hénon parameter reconstruction from a trace spectrum”;
- “the theorem holds for arbitrary Hénon maps”;
- “the novelty dissent has been resolved”;
- “the characteristic polynomial stays irreducible in every fiber.”
