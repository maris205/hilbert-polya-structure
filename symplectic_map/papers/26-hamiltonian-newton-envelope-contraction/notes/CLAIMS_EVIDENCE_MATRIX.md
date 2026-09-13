# Claims–evidence matrix

## Reading rule

Each claim below has a single strongest conclusion, a proof dependency, a local evidence location, and a kill condition. “Proved” means a complete symbolic argument is supplied in notes/PROOF_PACKAGE.md; it does not mean the claim has undergone external peer review. No numerical output is evidence for a theorem claim.

## Structural and cancellation claims

| ID | Claim | Dependencies | Evidence | Status | Kill condition |
|---|---|---|---|---|---|
| C01 | \(S\), \(T\), and \(F=T\circ S\) are polynomial symplectomorphisms. | Symmetric Hessians; nonzero coefficients not needed. | Proof Package, Symplectic structure and inverses. | Proved | A Jacobian block product is not \(J\). |
| C02 | \(F^{-1}=S^{-1}\circ T^{-1}\) with subtraction shears. | C01 | Proof Package, Symplectic structure and inverses. | Proved | A sign or phase order differs. |
| C03 | Every positive exposed face of \(V\) has \(\det\operatorname{Hess}P\ne0\). | Characteristic zero; support in \(\mathbf Z_{\ge2}^2\); collected nonzero coefficients. | Minimal-\(x\) coefficient lemma. | Proved | A distinct pair contributes to the witness exponent or its coefficient vanishes. |
| C04 | The two face-gradient coordinates are algebraically independent. | C03; characteristic-zero Jacobian criterion. | Algebraic-independence corollary. | Proved | Jacobian determinant vanishes or characteristic-zero is removed. |
| C05 | Substitution into an algebraically independent leading pair is injective. | Algebraic independence of the pair. | Substitution lemma. | Proved | A nonzero polynomial relation exists. |
| C06 | Pure powers, nonzero scalars, and signs preserve leading-pair algebraic independence. | C05; \(e,f\ge1\). | Pure-power lemma. | Proved | A nonzero polynomial relation survives pullback. |
| C07 | All forward top forms survive, including on Newton walls. | C03–C06. | Forward half-step induction. | Proved | A wall face is reduced to one tied monomial or a top pair becomes dependent. |
| C08 | All inverse top forms survive, including on Newton walls. | C03–C06; C02. | Inverse half-step induction. | Proved | Subtraction is treated as cancellation without tracking its nonzero top form. |

## Exact degree and bidirectional claims

| ID | Claim | Dependencies | Evidence | Status | Kill condition |
|---|---|---|---|---|---|
| C09 | The Newton transform is \(\mathcal A(u)=(H(u)-u_1,H(u)-u_2)^\top\). | Definition of \(H\); C07–C08 for exactness. | Degree-transform derivation. | Proved | A derivative face loses its expected top degree. |
| C10 | For every positive \(u\), both components of \(\mathcal A(u)\) strictly exceed \(\|u\|_\infty\). | Every support coordinate at least two. | Carry lemma. | Proved | Axis or exponent-one support is admitted. |
| C11 | Forward degrees obey \(u^+_{n+1}=B\mathcal A(u^+_n)\) and \(\deg(F^n)=\|u^+_n\|_\infty\). | C07, C09, C10; separated pure powers. | Forward block-visibility induction. | Proved | The final position block does not dominate both carried blocks. |
| C12 | Inverse degrees obey \(v^-_{n+1}=\mathcal A(Bv^-_n)\) and \(\deg(F^{-n})=\|v^-_n\|_\infty\). | C08–C10; reversed phases. | Inverse block-visibility induction. | Proved | The final momentum block is not visible. |
| C13 | \(u^+_{n+1}=c_\star Bv^-_n\) for \(c_\star=H(\mathbf1)-1\). | C11–C12; positive homogeneity; ordinary seed. | Bridge proposition and fixture F1. | Proved | Base case, shift, seed, or phase order fails. |
| C14 | Forward and inverse first dynamical degrees are equal. | C13; fixed positive constants in the norm comparison. | Bridge corollary. | Proved | Only one-sided asymptotic bounds remain. |

## Projective dynamics and arithmetic claims

| ID | Claim | Dependencies | Evidence | Status | Kill condition |
|---|---|---|---|---|---|
| C15 | The forward ratio map is \(\phi(r)=\kappa(\Phi(r)-r)/(\Phi(r)-1)\). | C11; positivity. | Projectivization derivation. | Proved | The momentum scaling is not diagonal. |
| C16 | Every chamber branch is strictly decreasing and has logarithmic slope below one in absolute value. | \(x,y\ge2\). | Log-derivative and positive-gap identity. | Proved | A branch gap is nonpositive. |
| C17 | One \(q<1\) contracts all positive rays, including across Newton walls. | C16; finite support; continuity of \(\Phi\). | Uniform-contraction theorem. | Proved | The supremum reaches one or wall patching is discontinuous. |
| C18 | There is one fixed ray and no nontrivial projective periodic orbit. | C17; Banach contraction. | Fixed-ray corollary. | Proved | Global log contraction fails. |
| C19 | The selector tail is stationary in an interior chamber or fixed/alternating at a wall. | C17–C18; decreasing injectivity; finite walls. | Selector-classification proposition. | Proved | An orbit crosses more than the adjacent wall chambers infinitely often. |
| C20 | The inverse ratio map is conjugate to the forward map by \(L(s)=\kappa s\). | C12, definitions of \(\phi,\psi\). | Conjugacy identity. | Proved | Either side of \(L\psi=\phi L\) differs. |
| C21 | An interior dynamical degree is algebraic of degree at most two. | C19; positive \(2\times2\) integer matrix. | Interior spectrum proposition. | Proved | The stationary selector matrix is not two-dimensional integral. |
| C22 | A wall dynamical degree is a positive integer. | C19; rational primitive wall ray; integrality of selector matrices. | Wall spectrum proposition. | Proved | Adjacent matrices lack the same ray or multiplier. |
| C23 | Uniformly, \([\mathbf Q(\lambda_1(F)):\mathbf Q]\le2\). | C21–C22. | Main theorem conclusion. | Proved | An unclassified selector tail exists. |
| C24 | Forward and inverse interior scalar degree tails have order at most two; forward and inverse strict-wall scalar degree tails have order at most four. | C11–C12, C19–C20; Cayley–Hamilton; separate forward \(C_\xi\) and inverse \(D_\xi=B^{-1}C_\xi B\) visibility; both parity products. | Proof Package Section 16, including inverse fixed-seed and parity-product subsections. | Proved | Either visible coordinate fails to stabilize, or the bridge is substituted for the inverse scalar proof. |

## Fixture and boundary claims

| ID | Claim | Evidence | Status | Kill condition |
|---|---|---|---|---|
| F01 | \(E=\{(2,2)\}\), \(B=\operatorname{diag}(3,2)\) gives \((5+\sqrt{97})/2\). | Exact matrix and characteristic polynomial in Proof Package. | Cross-checked | Any displayed product or bridge vector differs. |
| F02 | \(E=\{(2,8),(4,5),(5,3)\}\), \(B=\operatorname{diag}(24,11)\) has the prefix low–high–middle–high and then alternates. | Exact ratios and interval maps in Proof Package. | Cross-checked | A ratio lies outside its declared chamber. |
| F03 | The F02 wall multiplier is \(132\); monodromy eigenvalues are \(17424\) and \(224\). | Exact common-ray and matrix arithmetic. | Cross-checked | Trace or determinant does not factor as displayed. |
| B01 | Axis support can invalidate face-gradient independence and strict carry. | Counterexample discussion \(V=q_1^3+q_1q_2^3\). | Boundary frozen | Do not extend theorem across this boundary. |
| B02 | Mixed \(W\) can yield an increasing projective map. | Counterexample map \((5r+4)/(4r+5)\). | Boundary frozen | Do not infer selector rigidity for mixed momentum support. |
| B03 | Positive characteristic can kill the coefficient certificate. | Derivative/Hessian coefficient discussion. | Boundary frozen | Retain characteristic zero. |
| B04 | The exact bridge is phase- and seed-sensitive. | Base-case audit. | Boundary frozen | Restate before changing either datum. |

## Anti-claim register

The package explicitly does not support the following:

| Anti-claim | Reason unsupported |
|---|---|
| The support hypothesis is optimal. | Only sufficiency is proved. |
| Every planar Hamiltonian product shear has quadratic Perron degree. | Mixed \(W\), axes, and exponent-one support are excluded. |
| Selector alternation is a nontrivial projective two-cycle. | The numerical ratios converge to one fixed ray. |
| Wall recurrence order four is minimal. | Cayley–Hamilton gives only an upper bound. |
| Degree equality holds term by term forward and inverse, or the bridge alone transfers scalar recurrences. | The bridge includes a shift, scalar, and diagonal rescaling; inverse scalar recurrences use \(D_\xi\) and their own visibility proof. |
| The first dynamical degree computes entropy or all dynamical degrees. | No compactification or higher-degree action is analyzed. |
| The theorem classifies polynomial symplectomorphisms. | It concerns one explicit product-shear family. |
| The result has global priority. | The current novelty check is local-only. |

## Evidence completeness

The theorem is ready for manuscript planning because each promoted conclusion C01–C24 has a symbolic proof path and a named kill condition. Bibliographic sources provide context only and are not used as proof evidence. External novelty verification remains mandatory before global comparative language is introduced.
