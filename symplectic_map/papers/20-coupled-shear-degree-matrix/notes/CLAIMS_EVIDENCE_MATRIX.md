# Paper20 — Claims and Evidence Matrix

This matrix is a source-design ledger, not a publication certificate. A claim
is admissible only if its stated proof object exists and every assumption is
literal. `FORMAL` means proved in `PROOF_PACKAGE.md`; `SOURCE` means bounded
context only; `GATE` means a proof obligation that must be checked before the
claim is promoted.

| ID | Claim | Required assumptions | Evidence / proof object | Class | Failure or STOP |
|---|---|---|---|---|---|
| C01 | The family is defined on \(\mathbb A^4_K\) by the displayed \(V_g,W_g,S,T,F\). | \(g\in\mathbb Z, g\ge5\); \(\operatorname{char}K=0\). | RQ definitions; literal coordinate formulas. | FORMAL | Any hidden extra coordinate or changed shear word invalidates the package. |
| C02 | \(S\) and \(T\) are polynomial automorphisms. | Triangular shear form. | Lemma 1, explicit inverse. | FORMAL | A non-triangular or rational replacement is out of scope. |
| C03 | \(S\) and \(T\) preserve \(\omega\). | Hessians symmetric; characteristic is irrelevant here but fixed as zero. | Lemma 1 pullback calculation. | FORMAL | Missing Hessian cancellation is a proof gap. |
| C04 | The support is coupled/non-block in the displayed split. | Mixed monomials \(q_1^2q_2^2,p_1^2p_2^2\) retained. | Support graph with one connected edge; theorem wording limits claim to this split. | FORMAL/GATE | Removing either mixed monomial triggers STOP; no universal non-conjugacy claim. |
| C05 | The \(S\)-phase selects \(q_1^g\) in \(\partial_{q_1}V\). | \(1\le r=u_2/u_1<(g-2)/2\). | Lemma 2 inequality \(u_1+2u_2<(g-1)u_1\). | FORMAL | Equality or reversed inequality: STOP. |
| C06 | The \(T\)-phase selects \(p_2^g\) in \(\partial_{p_2}W\). | \(g\ge5\), \(v=Au\), and the cone. | Lemma 3 inequality \(v_2/v_1>2/(g-2)\). | FORMAL | A selector tie requires a new phase proof; do not average faces. |
| C07 | The exact face matrices are \(A=[[g-1,0],[2,1]]\), \(B=[[1,2],[0,g-1]]\). | Rows must come from the actual gradient monomials. | Monomial-to-row map in RQ and Lemmas 2–3. | FORMAL | Treating arbitrary Jacobian rows as \(A,B\) is prohibited. |
| C08 | The ratio cone is forward invariant. | \(g>4\); strict upper boundary. | Lemma 4 and explicit \(f_g\). | FORMAL | A single strict two-shear cone is not used; equality at phase return is expected. |
| C09 | Carried coordinates are strictly dominated. | Initial degree-one vectors and Lemma 4 induction. | Lemmas 2–3 and the componentwise inequalities in Lemma 6. | GATE | Any unverified carried term can change the recurrence. |
| C10 | No leading coefficient cancels. | Positive displayed coefficients; characteristic zero. | Lemma 5 coefficient induction and strict degree gaps. | FORMAL | Arbitrary signs, specializations, or positive characteristic are STOP. |
| C11 | The full-step matrix is \(C=BA=[[g+3,2],[2(g-1),g-1]]\). | Correct phase order \(S\) then \(T\). | Lemma 6 matrix multiplication. | FORMAL | The off-diagonal half-step matrix cannot replace \(C\). |
| C12 | \(\deg F_g^n=e_2^TC^n(1,1)^T\) for \(n\ge1\). | Exact selectors, no cancellation, total-degree visibility. | Lemma 6. | GATE | If another coordinate exceeds \(q_2\), the observable must be revised. |
| C13 | \(\rho(C)=(\sqrt g+1)^2\). | No extra phase product. | Lemma 7 characteristic polynomial. | FORMAL | A phase-lift extension must take the appropriate period root. |
| C14 | \(\lambda_1(F_g)=\rho(C)\). | C12 and Perron reachability/visibility. | Theorem proof; positive matrix. | FORMAL/GATE | No claim of whole-matrix spectral control without visibility. |
| C15 | Each elementary shear has degree \(g-1\). | \(g\ge5\), displayed potentials. | Maximum degree of displayed gradients. | FORMAL | Calling \(g\) the shear degree is an indexing error. |
| C16 | The Perron root is strictly below \((g-1)^2\). | \(g\ge5\). | Factored difference in theorem proof. | FORMAL | “Non-product” means this comparison, not a broad conjugacy theorem. |
| C17 | The family is asymmetric. | Pure high-degree term occurs in \(q_1\) for \(V\) and \(p_2\) for \(W\); cross terms are shared. | Support and row matrices have different triangular orientation. | FORMAL | Symmetrizing or permuting away the witness requires a separate proof. |
| C18 | The result is uniform in all integer \(g\ge5\). | Same inequalities and coefficients for every such \(g\). | Lemmas 2–7 with symbolic \(g\). | FORMAL | No interpolation from finitely many numerical values. |
| C19 | The result is not a generic theorem for arbitrary sparse shears. | Scope remains fixed. | Anti-claim ledger and collision matrix. | GATE | Any generic wording is a publication STOP. |
| C20 | Literature novelty is provisional and bounded. | Sources checked only for specified neighboring claims. | `CITATION_VERIFICATION.md`, `NOVELTY_ASSESSMENT.md`. | SOURCE/GATE | No priority or exhaustive-search claim. |

## Proof dependency graph

\[
 C01\to(C02,C03,C04)\to(C05,C06,C07)\to C08\to(C09,C10)\to
 C11\to C12\to(C13,C14,C15,C16)\to(C17,C18),
\]
with C19–C20 as scope and evidence gates. The graph is intentionally acyclic:
literature cannot substitute for a failed algebraic lemma, and a numerical
example cannot substitute for a symbolic selector proof.

## Evidence policy

The external citations listed in `CITATION_VERIFICATION.md` support only
background statements about degree growth, generalized Hénon maps, or coupled
four-dimensional symplectic dynamics. They do not prove any C05–C18 claim.
Every formal claim must be reproducible from the displayed definitions and
lemmas without an external database or experiment.
