# Paper Plan

**Title:** *Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps*

**Article type:** Proof-first algebraic dynamics.

**Length:** 22--24 content pages, with a target of exactly 23.0 pages. The reference list follows the appendix as a separate, unnumbered final part and is not charged to the content-page budget.

**Display inventory:** Exactly 0 figures, 0 illustrations, and 1 manuscript table. The sole table is a non-numerical proof-dependency table placed after the main theorem; there are no data tables or numerical-result tables. The planning tables below are editorial scaffolding and are not manuscript displays.

**Evidence policy:** Every mathematical assertion is proved directly, imported from a precisely identified theorem with its hypotheses checked, or deduced formally from such assertions. The article contains no scientific experiment, computational experiment, code, computer algebra, numerical example, dataset, benchmark, plot, or empirical claim.

**One-sentence contribution:** For every \(d\ge 2\) and every positive period vector of length \(d-1\), the \(d-1\) traces of labelled, pairwise-disjoint, simple exact marked cycles, together with \(-b\), form a dominant generically étale map on the unique simple marked Hénon component issuing from the polynomial boundary, and its critical Fitting scheme restricts there exactly to the polynomial multiplier critical scheme.

## Narrative and terminology

The paper tells one story: arbitrary-period polynomial multiplier coordinates can be transferred through the degenerate boundary \(b=0\) to marked trace coordinates for the extended generalized Hénon family, and the transfer preserves the full scheme structure of ramification on the simple scalar locus. The coordinate theorem and the ramification theorem must remain coupled; either one alone understates the contribution.

The opening pages must answer:

- **What:** construct the exact cycle-marked component through the polynomial boundary and prove the five-part theorem below;
- **Why:** the boundary map is not an automorphism, the total marked incidence need not be irreducible, specialized fibers may be reducible, and ramification must be compared scheme-theoretically rather than set-theoretically;
- **So what:** an arbitrary labelled selection of exactly \(d-1\) simple exact cycles of arbitrary positive periods supplies generic trace coordinates on the selected Hénon component, while the boundary records the polynomial multiplier ramification with its scheme multiplicities.

Use the following terms consistently:

- **point-marked incidence** for a chosen point on each labelled orbit;
- **cycle-marked incidence** only after quotienting each exact point marking by its own cyclic shift;
- **trace** for \(\rho_i=\operatorname{tr}(DH_{b,p}^{n_i})\), never “chosen eigenvalue”;
- **scalar boundary** or **polynomial boundary** for \(b=0\), with the explicit reminder that \(H_{0,p}\) is not an automorphism;
- **simple exact disjoint locus** whenever a component, completion, or Fitting-scheme statement depends on those hypotheses;
- **general fixed \(b\)** only for \(b\) in the unspecified nonempty open subset \(U\subset\mathbf G_m\).

## Abstract blueprint

The abstract should be about 180--220 words and follow five moves.

1. State the achieved result immediately: the map \(\Psi=(-b,\rho_1,\ldots,\rho_{d-1})\) is dominant and generically étale on the unique simple marked component through the polynomial boundary, for every \(d\ge2\) and every positive period vector.
2. Explain the difficulty in one sentence: point-to-cycle quotients, component selection, reducible fixed-\(b\) fibers, and the singular degeneration \(b=0\) prevent an unqualified openness argument.
3. Give the mechanism: identify the scalar incidence with the polynomial marked incidence, use Gorbovickis's arbitrary-period full-rank theorem, read the total differential in block form, and apply exact base change for relative differentials and Fitting ideals.
4. State the boundary guarantee:
   \[
   \mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
   =\mathcal R_{\mathrm{poly}},
   \qquad
   J_H\bmod b=\pm J_{\mathrm{poly}}.
   \]
5. Close on scope, not priority: the result concerns selected marked traces on the normal-form cover and makes no global reconstruction, every-\(b\), reducedness, or transversality assertion.

The abstract should contain no citation-dependent background sentence, undefined acronym, experiment language, or global-priority wording.

## Formal setup and five-part main theorem

Work over \(\mathbf C\). For \(d\ge2\), set
\[
\mathcal P_d^{\mathrm{cm}}
=\left\{p(z)=z^d+\sum_{j=0}^{d-2}a_jz^j\right\}
\simeq\mathbf A^{d-1},
\qquad
\mathcal B_d=\mathbf A^1_b\times\mathcal P_d^{\mathrm{cm}},
\]
and consider
\[
H_{b,p}(x,y)=(p(x)+by,x).
\]
Put \(r=d-1\), and fix an arbitrary vector
\[
\mathbf n=(n_1,\ldots,n_r)\in\mathbf Z_{>0}^{r}.
\]
Repeated numerical periods are allowed. The \(r\) cycles remain labelled and must be pairwise disjoint.

Let \(\widetilde{\mathcal X}_{\mathbf n}^{\circ}\) be the point-marked incidence on which every marked point has exact period \(n_i\), the underlying cycles are pairwise disjoint, and
\[
\det(DH_{b,p}^{n_i}-I)\ne0.
\]
The product
\[
G_{\mathbf n}=\prod_{i=1}^{r}\mathbf Z/n_i\mathbf Z
\]
acts freely by shifting each point around its own exact cycle. Define the cycle-marked incidence
\[
\mathcal X_{\mathbf n}^{\circ}
=\widetilde{\mathcal X}_{\mathbf n}^{\circ}/G_{\mathbf n},
\]
its scalar locus
\[
\mathcal S_{\mathbf n}=(\mathcal X_{\mathbf n}^{\circ})_{b=0},
\]
and the marked traces
\[
\rho_i=\operatorname{tr}(D H_{b,p}^{n_i}).
\]
Let \(\lambda_i\) denote the corresponding one-variable multiplier on \(\mathcal S_{\mathbf n}\), and let \(\mathcal C_{\mathbf n}\) be the unique irreducible component specified in part 1 below. With
\[
T=\mathbf A^1_t\times\mathbf A^r,
\qquad
\Psi=(-b,\rho_1,\ldots,\rho_r):\mathcal C_{\mathbf n}\longrightarrow T,
\]
the manuscript will state the following theorem in full near the beginning of Section 4 and preview all five parts in the Introduction.

### Main Theorem

For every \(d\ge2\) and every \(\mathbf n\in\mathbf Z_{>0}^{d-1}\), the following assertions hold.

1. **Marked scalar component.** The scalar cycle-marked locus \(\mathcal S_{\mathbf n}\) is nonempty and irreducible. It is contained in a unique irreducible component \(\mathcal C_{\mathbf n}\) of \(\mathcal X_{\mathbf n}^{\circ}\). The natural map
   \[
   \pi:\mathcal C_{\mathbf n}\longrightarrow\mathcal B_d
   \]
   is étale and dominant, and
   \[
   (\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}
   \]
   scheme-theoretically inside the simple exact disjoint incidence. Thus the component contains the full simple scalar fiber, not merely one scalar test point.

2. **Coordinate map.** The morphism
   \[
   \Psi=(-b,\rho_1,\ldots,\rho_r):
   \mathcal C_{\mathbf n}\longrightarrow
   \mathbf A^1\times\mathbf A^r
   \]
   is étale at a scalar point and hence is dominant and generically étale. Consequently,
   \[
   \rho_1,\ldots,\rho_r
   \]
   are algebraically independent over \(\mathbf C(b)\) in
   \(\mathbf C(\mathcal C_{\mathbf n})\).

3. **Safe fixed-\(b\) specialization.** There is an unspecified nonempty Zariski-open subset
   \[
   U\subset\mathbf G_m
   \]
   such that, for every \(b_0\in U\), the whole-fiber trace map
   \[
   \rho_{b_0}:(\mathcal C_{\mathbf n})_{b_0}
   \longrightarrow\mathbf A^r
   \]
   is dominant. For each such \(b_0\), at least one irreducible component of the reduced fiber
   \[
   (\mathcal C_{\mathbf n})_{b_0,\mathrm{red}}
   \]
   maps dominantly and generically étale to \(\mathbf A^r\). No irreducibility of the specialized fiber, no all-component assertion, and no conclusion for a prescribed nonzero \(b_0\) is included.

4. **Completed local form.** At every scalar point \(s\in\mathcal S_{\mathbf n}\), with centered coefficient coordinates \(u=(u_0,\ldots,u_{d-2})\) based at \(\pi(s)\), there are compatible isomorphisms
   \[
   \widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
   \simeq\mathbf C[[b,u_0,\ldots,u_{d-2}]],
   \qquad
   \widehat{\mathcal O}_{\mathcal S_{\mathbf n},s}
   \simeq\mathbf C[[u_0,\ldots,u_{d-2}]],
   \]
   under which
   \[
   \rho_i(b,u)=\lambda_i(u)+bG_i(b,u)
   \]
   for a unique \(G_i\in\mathbf C[[b,u]]\).

5. **Fitting-scheme restriction.** Define
   \[
   \mathcal R_H
   =V\!\left(\operatorname{Fitt}_0
   \Omega_{\mathcal C_{\mathbf n}/T}\right),
   \qquad
   \mathcal R_{\mathrm{poly}}
   =V\!\left(\operatorname{Fitt}_0
   \Omega_{\mathcal S_{\mathbf n}/\mathbf A^r}\right).
   \]
   Then, on the simple scalar locus,
   \[
   \mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
   =\mathcal R_{\mathrm{poly}}
   \]
   as closed subschemes. In completed local coordinates,
   \[
   J_H\bmod b=\pm J_{\mathrm{poly}}.
   \]
   The two determinant sections are nonzero sections. Their zero schemes are effective Cartier divisors when nonempty and may be empty. If \(\mathcal R_{\mathrm{poly}}\) is empty, the component-multiplicity assertion is vacuous; otherwise, the equality preserves the generic multiplicity along each actual irreducible boundary component. For \(d>2\), it gives no numerical intersection multiplicity at an arbitrary closed point without a separately justified proper transverse slice.

Immediately after the theorem, record
\[
\det(DH_{b,p}^{n_i})=(-b)^{n_i}.
\]
Thus a trace, together with the known determinant, determines only the unordered eigenvalue pair and never a regular choice of an individual eigenvalue branch.

## Proof architecture

All proof bridges remain visible in the numbered main sections. Appendix A expands only the cyclic-index algebra at \(n=1,2\) and a short monic-reduction detail; it does not carry a theorem-critical step.

The exact bridge sequence is:

1. prove the finite-free cyclic-loop lemma by a monic Gröbner basis, including the \(n=1,2\) relations;
2. apply the relative Jacobian criterion to the simple point-marked orbit equations;
3. prove the product cyclic-shift action is free on the exact locus and descend étaleness to cycle markings;
4. identify the scalar fiber scheme-theoretically and reduce trace and simplicity to polynomial multiplier and simplicity;
5. use Gorbovickis for scalar irreducibility and a \(d\ge2\) arbitrary-period full-rank point on distinct simple cycles;
6. use regular-component disjointness to obtain the unique component through the full scalar locus and the exact scalar fiber;
7. compute the block-triangular differential of \(\Psi\);
8. use the open image of the total étale locus to obtain the reducible-fiber-safe fixed-\(b\) result;
9. apply formal étaleness and divisibility by \(b\) to obtain the completed local expansion;
10. use the Cartesian boundary square, base change for relative Kähler differentials, and base change for zeroth Fitting ideals;
11. prove the Cartier-or-empty alternative and the generic component-length statement;
12. identify the residual \(\mu_{d-1}\) action and its obstruction to global injectivity.

The manuscript contains exactly one table, **Table 1: Dependency of the five theorem parts on the twelve proof bridges**. Its rows are the five theorem parts and the auxiliary finite-free lemma; its columns identify the relevant bridge numbers and distinguish direct, imported, and formal-corollary evidence. It contains no numerical data.

## Page budget

| Manuscript part | Pages | Running total |
|---|---:|---:|
| Abstract | 0.3 | 0.3 |
| 1. Introduction | 3.2 | 3.5 |
| 2. Marked incidences and exact-cycle quotients | 3.0 | 6.5 |
| 3. Universal cyclic-loop algebra and simple incidence | 2.0 | 8.5 |
| 4. Scalar component and marked trace coordinates | 4.0 | 12.5 |
| 5. Completed local geometry at the polynomial boundary | 3.0 | 15.5 |
| 6. Scheme-theoretic ramification and multiplicities | 3.5 | 19.0 |
| 7. General nonzero fibers and residual normal-form symmetry | 1.5 | 20.5 |
| 8. Comparison, limitations, and conclusion | 1.5 | 22.0 |
| Appendix A. Cyclic-loop algebra edge details | 1.0 | **23.0** |

The eight numbered sections and Appendix A total exactly 23.0 content pages including the abstract allocation. References appear last, after Appendix A, as a separate unnumbered list. There are no further appendices.

## 1. Introduction — 3.2 pages

### Purpose

Front-load the exact object, theorem, and distinction from full-spectrum rigidity. The first paragraph should begin with the selected marked-coordinate problem for
\[
H_{b,p}(x,y)=(p(x)+by,x),
\]
not with generic background about polynomial dynamics.

### Paragraph plan

1. Introduce the monic-centered family, the automorphism locus \(b\ne0\), and the polynomial proof boundary \(b=0\).
2. Pose the finite selected-data question: whether \(d-1\) labelled, disjoint, simple exact cycles of arbitrary prescribed positive periods, together with \(-b\), give local algebraic coordinates.
3. Explain the four structural obstacles: point markings versus cycle markings; selection of a single component through the full scalar locus; reducibility of closed fixed-\(b\) fibers; and scheme-theoretic rather than set-theoretic ramification.
4. State the one-sentence contribution and preview all five theorem parts with their quantifiers intact.
5. Give four concrete contribution bullets:
   - construction and uniqueness of the simple marked component through the full scalar boundary;
   - dominant generically étale arbitrary-period trace coordinates and algebraic independence over \(\mathbf C(b)\);
   - exact completed-local and Fitting-scheme restriction at every simple scalar tuple;
   - safe general fixed-\(b\) specialization and the residual finite-symmetry obstruction.
6. Credit the sole deep polynomial input explicitly and position the Hénon transfer against the nearest full-spectrum and regular-endomorphism results.
7. End with a short roadmap organized by proof dependency, not by discovery history.

### Front-loading checks

- The reader encounters \(d\ge2\), \(r=d-1\), arbitrary positive periods, repeated-period labels, exactness, disjointness, simplicity, and the selected component by the end of page 1.
- The boundary Fitting identity appears before the roadmap.
- The words “dominant and generically étale” are not replaced by “reconstructs.”
- No figure is promised or needed; Table 1 is the sole visual compression device.

## 2. Marked incidences and exact-cycle quotients — 3.0 pages

### Definitions

- Define \(\mathcal P_d^{\mathrm{cm}}\), \(\mathcal B_d\), \(H_{b,p}\), \(r=d-1\), and the arbitrary period vector \(\mathbf n\).
- Build the full point-marked incidence from
  \[
  H^{n_i}(z_i)-z_i=0,\qquad 1\le i\le r.
  \]
- Define the open conditions:
  - exact period by deleting all proper-divisor fixed loci;
  - pairwise cycle disjointness by deleting all finitely many iterate-collision loci;
  - simplicity by \(\det(DH^{n_i}-I)\ne0\).
- Say explicitly that repeated values among the \(n_i\) are allowed, but the cycles retain their labels and must be disjoint. No symmetric-group quotient permutes equal-period labels.

### Point-to-cycle bridge

The orbit-variable Jacobian is block diagonal, with blocks
\[
DH_{b,p}^{n_i}-I.
\]
Invertibility on the simple locus proves that the point-marked incidence is étale over \(\mathcal B_d\). On an exact cycle a nontrivial cyclic shift cannot fix the point marking, so
\[
G_{\mathbf n}=\prod_i\mathbf Z/n_i\mathbf Z
\]
acts freely. Over \(\mathbf C\), the quotient is finite étale, and the cycle-marked incidence remains étale over \(\mathcal B_d\). The traces are invariant under cyclic shift and descend.

### Scope statements to make here

- The free action exists only on the exact locus; it is not asserted on the lower-period closure.
- Point markings contain cyclic-shift copies. Cycle marking removes exactly those copies and does not remove the residual \(\mu_{d-1}\) normal-form ambiguity.
- The simple incidence is smooth and regular of pure dimension \(d\), but this does not make the full incidence irreducible.

## 3. Universal cyclic-loop algebra and simple incidence — 2.0 pages

### Auxiliary finite-free lemma

For
\[
R_d=\mathbf C[b,a_0,\ldots,a_{d-2}]
\]
and \(n\ge1\), define
\[
A_n=
R_d[x_0,\ldots,x_{n-1}]
\Big/
\left(p(x_j)+b x_{j-1}-x_{j+1}:j\in\mathbf Z/n\mathbf Z\right).
\]
State and prove in the main text that \(A_n\) is finite free over \(R_d\) of rank \(d^n\), with basis
\[
\left\{x_0^{e_0}\cdots x_{n-1}^{e_{n-1}}:
0\le e_j<d\right\}.
\]
For several independent point markings, the tensor-product algebra is finite free of rank
\[
d^{n_1+\cdots+n_r}.
\]

### Main-text proof

- Treat parameters as coefficients and choose a monomial order refining total degree in the loop variables.
- The normalized relations are monic with pairwise-coprime leading monomials \(x_j^d\).
- The monic Buchberger criterion over \(R_d\) gives a Gröbner basis.
- Standard monomials span; the leading-monomial argument proves independence.
- The recurrence
  \[
  H(x_j,x_{j-1})=(x_{j+1},x_j)
  \]
  gives mutually inverse functorial maps between cyclic loops and the full scheme of points fixed by \(H^n\).

### Edge cases and strict limitations

The main text states the edge relations and sends only their expanded algebra to Appendix A:

- \(n=1\): \(p(x_0)+(b-1)x_0\), with leading monomial \(x_0^d\);
- \(n=2\): \(p(x_0)+(b-1)x_1\) and \(p(x_1)+(b-1)x_0\), with leading monomials \(x_0^d,x_1^d\).

Close the section by stating all limitations together. The algebra describes the full ordered fixed-point incidence, including lower periods, collisions, nonsimple points, multiplicities, and possibly nonreduced fibers. Its rank is not an exact-cycle count. Finite freeness does not imply irreducibility. After deleting the nonexact, collision, and nonsimple loci, the resulting open morphism is étale and quasi-finite but need not remain finite or proper over all of \(\mathcal B_d\).

## 4. Scalar component and marked trace coordinates — 4.0 pages

### Scalar identification

Prove by induction that
\[
H_{0,p}^{n}(x,y)=\bigl(p^n(x),p^{n-1}(x)\bigr).
\]
The fixed equations become
\[
p^n(x)=x,\qquad y=p^{n-1}(x),
\]
giving a scheme-level identification with the one-variable polynomial marked incidence. Prove that minimal periods and orbit disjointness agree under the lift.

Differentiate to obtain
\[
DH_{0,p}^{n}
=
\begin{pmatrix}
(p^n)'(x)&0\\
(p^{n-1})'(x)&0
\end{pmatrix}.
\]
Writing \(\lambda=(p^n)'(x)\), conclude
\[
\operatorname{tr}(DH_{0,p}^n)=\lambda,
\qquad
\det(DH_{0,p}^n-I)=1-\lambda.
\]
Thus scalar Hénon simplicity is exactly polynomial simplicity and the Hénon trace restricts exactly to the polynomial multiplier.

### Gorbovickis input and the \(d=2\) guard

State the imported result with its full role:

- Definition 1.3, Remark 1.4, and Lemma 1.5 of Gorbovickis give the irreducible marked polynomial space and independence from the starting marking;
- Theorem 1.6 applies for every \(d\ge2\), every \(k\le d-1\), and every positive period vector;
- Lemma 2.1 supplies, for \(p_0(z)=z^d\), a tuple on distinct exact cycles at which the selected multiplier Jacobian is nonzero.

At those nonzero exact periodic points, the multipliers are \(d^{n_i}\ne1\), so the cycles are simple. The quadratic case is included with \(k=1=d-1\): cite Theorem 1.6 and Lemma 2.1, not the \(d\ge3\) headline Corollary 1.7. Repeated period values remain allowed because the cycles, not the integers \(n_i\), are required to be distinct.

### Unique component through the full scalar locus

Use the imported scalar irreducibility and the free finite cyclic quotient to prove that \(\mathcal S_{\mathbf n}\) is irreducible. Since the total simple incidence is regular, distinct irreducible components are disjoint open-and-closed subsets. Therefore the entire scalar locus lies in one unique component \(\mathcal C_{\mathbf n}\). No other regular component meets \(b=0\). Étaleness makes the scalar fiber reduced, yielding
\[
(\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}
\]
scheme-theoretically. The restricted map \(\mathcal C_{\mathbf n}\to\mathcal B_d\) is étale; its nonempty open image is dense in the irreducible base, so it is dominant, not necessarily surjective.

### Block differential and coordinate theorem

At the Gorbovickis scalar point, use local coordinates \((b,u_0,\ldots,u_{d-2})\). With target coordinate \(t=-b\),
\[
D\Psi=
\begin{pmatrix}
-1&0&\cdots&0\\
\partial_b\rho_1&&&\\
\vdots&&(\partial_{u_j}\rho_i)&\\
\partial_b\rho_r&&&
\end{pmatrix},
\]
and at \(b=0\),
\[
\det D\Psi
=\pm\det\left(\frac{\partial\lambda_i}{\partial u_j}\right)\ne0.
\]
This proves étaleness at a scalar point. Equal source and target dimensions then give dominance and generic étaleness. The induced injection of function fields, followed by clearing denominators, proves algebraic independence of \(\rho_1,\ldots,\rho_r\) over \(\mathbf C(b)\).

## 5. Completed local geometry at the polynomial boundary — 3.0 pages

Fix an arbitrary simple scalar tuple \(s\), not only the full-rank test point. Étaleness of
\[
\pi:\mathcal C_{\mathbf n}\to\mathcal B_d
\]
and equality of residue fields give
\[
\widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
\simeq
\widehat{\mathcal O}_{\mathcal B_d,\pi(s)}
\simeq
\mathbf C[[b,u_0,\ldots,u_{d-2}]].
\]
Because the scalar fiber is scheme-theoretically cut out by \(b\),
\[
\widehat{\mathcal O}_{\mathcal S_{\mathbf n},s}
\simeq\mathbf C[[u_0,\ldots,u_{d-2}]].
\]

Continue each simple polynomial cycle formally over \(\mathbf C[[u]]\), and denote its multiplier germ by \(\lambda_i(u)\). The scalar identity gives
\[
\rho_i(0,u)=\lambda_i(u).
\]
Therefore \(\rho_i-\lambda_i\in(b)\), and the non-zero-divisor property of \(b\) yields the unique expansion
\[
\rho_i=\lambda_i+bG_i,
\qquad
G_i\in\mathbf C[[b,u]].
\]

The proof cites Stacks Tags 02GH and 0257 only for the formal/completed-local behavior of étale morphisms. It does not infer irreducibility from those tags and does not transfer the completion to a naive coarse \(\mu_{d-1}\)-quotient at a stabilizer. End the section by writing the Cartesian boundary square used in Section 6 and explaining why its top row is the full simple scalar fiber.

## 6. Scheme-theoretic ramification and multiplicities — 3.5 pages

### Exact relative-differential base change

Let
\[
T_0=\{t=0\}\times\mathbf A^r\subset
T=\mathbf A^1_t\times\mathbf A^r.
\]
Since \(t\circ\Psi=-b\) and the scalar fiber is exactly \(\mathcal S_{\mathbf n}\), display the Cartesian square
\[
\begin{array}{ccc}
\mathcal S_{\mathbf n}&\longrightarrow&\mathcal C_{\mathbf n}\\
\downarrow\Lambda&&\downarrow\Psi\\
T_0&\longrightarrow&T.
\end{array}
\]
Then prove the exact base-change isomorphism
\[
\Omega_{\mathcal C_{\mathbf n}/T}
\otimes_{\mathcal O_{\mathcal C_{\mathbf n}}}
\mathcal O_{\mathcal S_{\mathbf n}}
\simeq
\Omega_{\mathcal S_{\mathbf n}/T_0}.
\]
Because these relative differential modules are finitely presented, zeroth Fitting ideals commute with this base change:
\[
\operatorname{Fitt}_0\Omega_{\mathcal C_{\mathbf n}/T}
\cdot\mathcal O_{\mathcal S_{\mathbf n}}
=
\operatorname{Fitt}_0\Omega_{\mathcal S_{\mathbf n}/T_0}.
\]
After identifying \(T_0\simeq\mathbf A^r\), conclude the equality of closed subschemes
\[
\mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
=\mathcal R_{\mathrm{poly}}.
\]
Use Stacks Tag 07Z6, Lemma 15.8.4, for Fitting ideals under base change and Tag 0C3I for the corresponding scheme-level construction. Apply them only to this proved Cartesian simple-boundary square.

### Local determinant and Cartier-or-empty guard

From \(\rho_i=\lambda_i+bG_i\), reduce the lower-right differential block modulo \(b\) to obtain
\[
J_H\bmod b=\pm J_{\mathrm{poly}},
\]
where the sign depends only on coordinate ordering and is a unit. Generic étaleness of \(\Psi\) shows that \(J_H\) is not identically zero; the scalar full-rank point shows that \(J_{\mathrm{poly}}\) is not identically zero. On the smooth irreducible source spaces, the resulting zero schemes are effective Cartier divisors if nonempty and may be empty. Do not import nonemptiness of the polynomial critical scheme from the full-rank theorem.

If \(\mathcal R_{\mathrm{poly}}\) is empty, say explicitly that every multiplicity statement is vacuous. Otherwise, for each actual irreducible component \(Z\) with generic point \(\eta_Z\), write
\[
\operatorname{length}_{\mathcal O_{\mathcal C_{\mathbf n},\eta_Z}}
\frac{\mathcal O_{\mathcal C_{\mathbf n},\eta_Z}}{(b,J_H)}
=
\operatorname{length}_{\mathcal O_{\mathcal S_{\mathbf n},\eta_Z}}
\frac{\mathcal O_{\mathcal S_{\mathbf n},\eta_Z}}{(J_{\mathrm{poly}})}.
\]
Explain that this is the generic component multiplicity encoded by the scheme restriction. For \(d>2\), the component is generally positive-dimensional, so the local quotient at an arbitrary closed point need not be Artinian. A transverse slice could define a number, but no slicing theorem belongs to the article.

Close with the precise negative scope: no radicality, reducedness, smoothness, normal-crossings, transversality, nonsimple extension, or compactified equality follows.

## 7. General nonzero fibers and residual normal-form symmetry — 1.5 pages

### Reducible-fiber-safe specialization

Let \(E\subset\mathcal C_{\mathbf n}\) be the nonempty étale locus of \(\Psi\). Since
\[
\Psi|_E:E\to T
\]
is étale, its image \(V=\Psi(E)\) is a nonempty open subset of \(T\). Project \(V\) to the \(t\)-line, change \(t=-b\), and remove \(b=0\) to obtain a nonempty open
\[
U\subset\mathbf G_m.
\]
For every \(b_0\in U\), the slice \(V_{-b_0}\) is nonempty open dense in \(\mathbf A^r\), so the trace map on the whole fiber is dominant.

The reduced finite-type fiber has finitely many irreducible components. Their image closures cover the irreducible target, hence at least one component dominates. Choose a dominating component meeting the base-changed étale locus; its trace map is generically étale. State again that the proof gives neither fiber irreducibility nor goodness of every component, and does not identify the exceptional finite set or cover a prescribed value such as \(b=-1\).

### Determinant and residual symmetry

Compute
\[
\det(DH_{b,p}^{n_i})=(-b)^{n_i}
\]
and explain why trace plus determinant gives only an unordered eigenvalue pair.

For \(\beta\in\mu_{d-1}\), define
\[
L_\beta(x,y)=(\beta x,\beta y),
\qquad
p_\beta(z)=\beta^{-1}p(\beta z).
\]
Then
\[
L_\beta^{-1}\circ H_{b,p}\circ L_\beta=H_{b,p_\beta}.
\]
This diagonal conjugacy preserves \(b\), transports every labelled cycle, and preserves every trace. The action preserves the selected component by its uniqueness. For \(d>2\) it is generically free and obstructs generic injectivity or birationality on the monic-centered normal-form cover. For \(d=2\), \(\mu_1\) is trivial. At nontrivial stabilizers, a coarse quotient may have quotient singularities, so no coarse-quotient completed-local statement is made.

## 8. Comparison, limitations, and conclusion — 1.5 pages

### Primary-source comparison and date boundary

The literature comparison is bounded through **2026-08-17**. The manuscript makes no global or absolute-priority claim. Each source has one exact role:

- **Igors Gorbovickis, arXiv:1305.0867v1 (2013), later ETDS 36 (2016):** the sole indispensable dynamics input. Definition 1.3, Remark 1.4, and Lemma 1.5 support the irreducible marked polynomial space; Theorem 1.6 and Lemma 2.1 support the \(d\ge2\), \(k\le d-1\), arbitrary-positive-period full-rank point on distinct cycles. This source proves no Hénon, fixed-\(b\), completion, or Fitting assertion.
- **Gorbovickis--Taflin, arXiv:2411.12856v2 (2025 source version):** comparison with multiplier independence for regular polynomial endomorphisms, principally under period-at-least-\(4\) hypotheses. Generalized Hénon maps and the \(b=0\) boundary lie outside that theorem.
- **Valentin Huguin, arXiv:2412.19335v1 (2024):** comparison with complete unmarked period-\(1\) and period-\(2\) polynomial spectra and finite birational recovery. It gives no arbitrary selected marked Hénon-coordinate or boundary-ramification result.
- **Serge Cantat and Romain Dujardin, arXiv:2603.09445v1, submitted 2026-03-10:** the closest Hénon-spectrum comparison, covering full-spectrum rigidity and finite low-period determination. It does not prove that any arbitrary selected \(d-1\) marked traces are coordinates or that the scalar critical scheme base-changes exactly.
- **Fabrizio Bianchi and Yan Mary He, arXiv:2606.29363v1, submitted 2026-06-28:** comparison with analytic and thermodynamic use of the full marked unstable spectrum on hyperbolic components. It supplies no finite algebraic-independence or scalar-degeneration theorem.
- **Shmuel Friedland and John Milnor, ETDS 9 (1989), 67--99:** foundational generalized Hénon normal forms and the low-degree period-\(1\) overlap. It does not cover arbitrary periods or scheme-theoretic boundary ramification.
- **The Stacks Project, Tags 02GH, 0257, 07Z6, and 0C3I:** foundational support only for the stated formal-étale/completed-local and Fitting-base-change steps.

Organize the related-work discussion by question—marked local coordinates, complete spectra and global rigidity, and boundary scheme structure—rather than as a paper-by-paper catalogue. Reference metadata must be taken from these primary records; no citation is to be inferred from a secondary description.

### Exact A1--A20 scope ledger

The manuscript will preserve the following statements exactly.

- **A1.** No irreducibility claim for the full marked Hénon incidence.
- **A2.** No irreducibility claim for any or every specialized fixed-$b$ fiber.
- **A3.** No local-coordinate claim for every nonzero $b$.
- **A4.** No conclusion at any prescribed nonzero fiber, including $b=-1$.
- **A5.** No global injectivity, birationality, or reconstruction claim on the monic-centered normal-form cover.
- **A6.** No claim that every irreducible component of a general fixed-$b$ fiber dominates or is generically étale.
- **A7.** No reducedness or smoothness claim for either critical/Fitting scheme.
- **A8.** No transversality or normal-crossings claim for the boundary intersection.
- **A9.** No global, nonsimple, or compactified Fitting-scheme equality beyond the simple scalar locus.
- **A10.** No closed-point numerical intersection multiplicity without a separately justified proper transverse slice; the theorem preserves generic multiplicities along boundary components.
- **A11.** No individual eigenvalue branch is a coordinate: $\det(DH_{b,p}^{n_i})=(-b)^{n_i}$, so trace records only the unordered eigenvalue pair once the determinant is known.
- **A12.** No interpretation of finite-free rank $d^n$ as an exact-cycle count.
- **A13.** The fiber $b=0$ is only the polynomial/proof boundary; $H_{0,p}$ is not a Hénon automorphism.
- **A14.** No positive-characteristic extension.
- **A15.** No extension to multi-factor or composed generalized Hénon maps.
- **A16.** Point-marked fibers contain cyclic-shift copies; passage to cycle markings removes only those shifts, not residual $\mu_{d-1}$ ambiguity.
- **A17.** No naive coarse $\mu_{d-1}$-quotient completed-local claim near stabilizers; stack or quotient-singularity analysis is required.
- **A18.** No claim that the simple exact open is finite or proper over all of $\mathcal B_d$, no uniform all-fiber degree, and no all-fiber reconstruction.
- **A19.** No absolute-priority or “first ever” claim.
- **A20.** No computational, CAS, numerical, empirical, or experimental evidence or result.

### Conclusion plan

Restate the coupled conclusion without copying the Introduction: the marked component and block differential transfer polynomial multiplier independence to Hénon traces, while exact relative-differential and Fitting base change retain the boundary ramification scheme. End with two clearly non-theorem directions: determining exceptional nonzero \(b\)-values and analyzing stack or stabilizer-free quotients. Do not present either direction as completed work.

## Appendix A. Cyclic-loop algebra edge details — 1.0 page

Appendix A is the only appendix. It contains:

1. the expanded \(n=1\) calculation showing that the single cyclic equation is
   \[
   p(x_0)+(b-1)x_0
   \]
   and remains monic of degree \(d\);
2. the expanded \(n=2\) calculation showing that the two cyclic equations are
   \[
   p(x_0)+(b-1)x_1,\qquad
   p(x_1)+(b-1)x_0
   \]
   with relatively prime leading monomials;
3. the short coefficient-ring version of the monic Buchberger reduction and the standard-monomial independence argument;
4. a final reminder that the lemma concerns full ordered loops and proves no irreducibility, exact-cycle count, or all-base finiteness for the deleted simple open.

The appendix adds no new theorem, example, computation, or scope extension. The references follow it and are the final part of the manuscript.

## Claims-to-sections and evidence matrix

| Claim | Exact evidence | Main location | Supporting location | Scope check |
|---|---|---|---|---|
| Auxiliary finite-free ordered-loop lemma, rank \(d^n\), and product rank \(d^{\sum n_i}\) | Direct monic Gröbner-basis proof and functorial loop/fixed-point identification | Section 3 | Appendix A | Full ordered loops only; no irreducibility or exact-cycle count |
| Point-marked simple incidence is étale; exactness/disjointness are open; cyclic quotient is finite étale | Direct relative-Jacobian and free-action proof | Section 2 | Section 3 | Repeated periods allowed; labels not permuted |
| Main Theorem 1: nonempty irreducible scalar locus, unique component through the full scalar fiber, étale/dominant projection, exact scalar fiber | Direct scalar identification and regular-component argument; Gorbovickis irreducibility input | Section 4 | Sections 2--3 | No full-incidence irreducibility; dominant does not mean surjective |
| Main Theorem 2: \(\Psi\) étale at a scalar point, dominant, generically étale; traces independent over \(\mathbf C(b)\) | Gorbovickis Theorem 1.6 and Lemma 2.1 plus direct block differential and function-field argument | Section 4 | Section 1, Table 1 | \(d=2\) uses Theorem 1.6/Lemma 2.1, not Corollary 1.7 |
| Main Theorem 3: whole fixed-\(b\) fiber dominant and one reduced component dominant/generically étale for \(b\in U\) | Direct open-image argument for the total étale locus and finite component-image argument | Section 7 | Section 1 | \(U\subset\mathbf G_m\) nonempty and unspecified; no prescribed fiber or all-component claim |
| Main Theorem 4: completed rings and \(\rho_i=\lambda_i+bG_i\) | Formal étaleness, exact scalar fiber, and divisibility by the non-zero-divisor \(b\); Stacks 02GH/0257 | Section 5 | Section 4 | Every simple scalar tuple; normal-form cover only |
| Main Theorem 5: exact relative-\(\Omega\)/\(\operatorname{Fitt}_0\) base change and \(J_H\bmod b=\pm J_{\mathrm{poly}}\) | Direct Cartesian square and determinant calculation; Stacks 07Z6/0C3I | Section 6 | Section 5 | Simple scalar locus only; no nonsimple or compactified equality |
| Cartier-or-empty and component multiplicity statement | Nonzero determinant sections, smooth irreducible sources, and generic local-length equality | Section 6 | Section 4 | Empty case is vacuous; no arbitrary closed-point number for \(d>2\) |
| Trace records only the unordered eigenvalue pair | Direct determinant computation \(\det(DH^{n_i})=(-b)^{n_i}\) | Section 7 | Sections 2 and 4 | No eigenvalue-branch coordinate |
| Residual \(\mu_{d-1}\) obstruction | Direct diagonal-conjugacy calculation | Section 7 | Section 8 | No injectivity/birationality; coarse stabilizers require separate analysis |
| Positioning against neighboring results | Verified primary records, with comparison bounded through 2026-08-17 | Sections 1 and 8 | References | Comparison only except Gorbovickis and exact Stacks roles; no absolute priority |
| A1--A20 limitations and zero-science envelope | Exact scope ledger and proof-only evidence policy | Section 8 | Abstract and conclusion | 0 figures, 0 illustrations, 0 experiments, 0 computations |

## Drafting checkpoints

- [ ] Use the exact title given at the top of this plan.
- [ ] Keep exactly eight numbered main sections, one Appendix A, and a separate reference list last.
- [ ] Keep the content-page budget within 22--24 pages and target the explicit 23.0-page sum above.
- [ ] Keep the manuscript display inventory at exactly 0 figures, 0 illustrations, and 1 non-numerical proof-dependency table.
- [ ] Make the abstract follow the five-part blueprint and state both the coordinate and Fitting-scheme conclusions.
- [ ] State all five parts of the Main Theorem in full in the main text, with \(d\ge2\), \(r=d-1\), arbitrary positive periods, repeated-period labels, exactness, disjointness, and simplicity explicit.
- [ ] Distinguish point markings from cycle markings and say that equal-period labels are not permuted.
- [ ] Include all twelve proof bridges in the main text; use Appendix A only for the one-page cyclic-loop edge details.
- [ ] State the \(n=1\) and \(n=2\) loop relations and all finite-free limitations.
- [ ] Attribute scalar irreducibility and full rank precisely to Gorbovickis, and retain the \(d=2\) Theorem 1.6/Lemma 2.1 guard.
- [ ] Prove uniqueness of the component through the full simple scalar fiber by regular-component disjointness.
- [ ] Show the first differential row \((-1,0,\ldots,0)\) and the polynomial multiplier Jacobian as the lower-right block.
- [ ] State fixed-\(b\) results only for an unspecified nonempty \(U\subset\mathbf G_m\), and guarantee only at least one dominant generically étale component of the reduced fiber.
- [ ] Give both completed local rings and the unique expansion \(\rho_i=\lambda_i+bG_i\) at every simple scalar tuple.
- [ ] Display the Cartesian boundary square, the exact relative-\(\Omega\) base change, the \(\operatorname{Fitt}_0\) equality, and \(J_H\bmod b=\pm J_{\mathrm{poly}}\).
- [ ] State that both determinant sections are nonzero, their zero schemes are effective Cartier or empty, and multiplicity claims are vacuous when the polynomial scheme is empty.
- [ ] Restrict multiplicity to generic component lengths and exclude arbitrary closed-point numbers for \(d>2\) without a proper transverse slice.
- [ ] Record \(\det(DH^{n_i})=(-b)^{n_i}\) and the residual \(\mu_{d-1}\) action, including the trivial \(d=2\) case and the coarse-stabilizer warning.
- [ ] Preserve A1--A20 exactly and ensure no positive statement elsewhere contradicts them.
- [ ] Keep the comparison boundary at 2026-08-17, use the exact source roles and public version/submission dates above, and make no global-priority claim.
- [ ] Use only verified primary-source metadata in the reference list.
- [ ] Include no code, CAS, numerical example, experiment, dataset, empirical result, or computational evidence.
