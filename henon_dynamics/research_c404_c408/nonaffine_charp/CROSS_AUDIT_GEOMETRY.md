# Independent bounded cross-audit: nonlinear_geometry

Date: 2026-09-06. Reviewer lane: `nonaffine_charp`. Requested scope: the actual geometry scout report and its exact probe, with emphasis on the Hietarinta–Viallet 9-versus-18 distinction, the hypotheses of the Frobenius–surface corollary, and avoiding whole-family impossibility claims.

Verdict: **0 blocking findings; 0 required corrections** within that scope. Both zero-contract decisions are justified as stated. This is a second AI-agent read-only audit, not a blind human review, not a manuscript-acceptance verdict, and not a global novelty certification.

## 1. Frozen material actually read

All 242 report lines, all 137 code lines, and the complete saved JSON were read. The report was then reread in full after its author changed only “no Git operations” to the more precise “no Git writes/commits”; the table binds that final frozen text. No SymPy lane or author probe was rerun. No target files were edited. Only this audit file was written.

| Material under `../nonlinear_geometry/` | SHA-256 |
|---|---|
| `SCOUT_REPORT.md` | `04e7e476357e7b12f36ab70f1460bbc12d072c9765bccf2f2a4246db90ff3d3d` |
| `exact_probe.py` | `8d04b32150dcbd12e17d56f2ba0a7c006868f0202179c34a022cc4e366747d8e` |
| `EXACT_PROBE_OUTPUT.json` | `0c9802ced7e6f79e1ea8834b62c5d97cafb9f1fb836a14135f068ed510627799` |

## 2. HV three-period classification and multiplicity

The map is H_a(x,y)=(y,−x+y+a/y²), over C with a≠0, restricted to orbits whose intermediate coordinates are nonzero. The scaling S_t with t³=a conjugates it to H_1. Thus the degeneracy demonstrated at a=1 applies to every declared nonzero parameter; it cannot be removed by choosing a generic a in this family.

I independently checked the following algebraic chain, rather than accepting the saved result as its proof.

1. Fixed points are (t,t), t³=1. Their derivative is M=[[0,1],[−1,−1]], with det(I−M)=3 and M³=I. They are simple for H_1 but not transverse for H_1³.
2. Expanding the local map to degree two gives (u,v)↦(v,−u−v+3v²)+O(3). Composing three times gives the displacement (3u²+6uv,−6uv−3v²)+O(3), exactly as reported. The two homogeneous leading terms have no common projective zero. Their initial forms form a regular sequence, so the local intersection length is 2·2=4. The cube-root scaling symmetry transports this to each of the three fixed points.
3. The cyclic equations F_i=x_i³−(x_j+x_k)x_i²+1 force each coordinate to be nonzero. Consequently no denominator-zero solution was silently added, and one may locally eliminate x₂ using the original recurrence. The cyclic scheme is locally the fixed-point scheme of H_1³ in the pair (x₀,x₁); the local lengths being compared are the same objects.
4. If two coordinates are equal to t and the third is s, the equations give st²=1 and (t³−1)²=0. Set-theoretically this is precisely the three old fixed points. If all coordinates are distinct, dividing F_i−F_j by x_i−x_j gives x_i²+x_j²−x_k(x_i+x_j)=0. Subtracting two such identities gives (x_i−x_k)(x₀+x₁+x₂)=0, hence the sum is zero. Substitution then gives the pairwise-product sum zero and x_i³=−1/2. The only points are therefore the six permutations of the distinct roots of X³+1/2.
5. There is also a direct check of the six new points' simplicity that does not depend on the author's Gröbner computation. At such a point the cyclic Jacobian is diag(x₀²,x₁²,x₂²)(6I−J₃). Its determinant is (x₀x₁x₂)²·3·6·6=(1/4)·108=27≠0. Thus the scheme length is already forced to be 3·4+6·1=18, while its support has 3+6=9 points. The six nonfixed points form two exact three-cycles.

The saved multiplier characteristic polynomial is consistent with this independent classification. At old points, L=x₀+2x₁+4x₂ equals 7t, giving (z³−343)⁴. For the six new points choose r³=−1/2 and a primitive cube root ω. The two cyclic permutation orbits have L-values rωʲA and rωʲB, where A=1+2ω+4ω² and B=1+4ω+2ω². Since A+B=−4, AB=7 and A³+B³=20, their degree-six factor is z⁶+10z³+343/4. This verifies the reported factorization without recomputing an 18×18 matrix.

The code's Gröbner monomial traversal, multiplication-matrix construction and characteristic-polynomial assertions match the described exact rational calculation. The saved stdout is author-run provenance, not a new execution by this reviewer. In particular, the number 18 is not being certified solely because the code contains an assertion that it is 18: the preceding local/global classification supplies a second mathematical derivation.

## 3. Existing surface formulas and source ownership

I reopened the following primary passages independently of the scout's summary:

- [Bedford–Kim, arXiv:0804.2078v2](https://arxiv.org/pdf/0804.2078v2), theorem 8.1 with the preceding displayed differential computations: the stated boundary union consists of points fixed by f^{2N}, tangent to the identity. The report preserves the theorem-1 family condition; it does not apply the assertion to arbitrary birational maps or arbitrary c.
- [Iwasaki–Uehara, arXiv:0710.0706v1](https://arxiv.org/pdf/0710.0706v1), §7 equations (33)–(37) and theorem 7.2; theorem 2.6 and remark 6.2. The source explicitly distinguishes multiplicity-weighted cardinality from ordinary cardinality. Algebraic stability, absence of type-I periodic curves, and the meromorphic-form pole-order condition were not erased in the report.
- [Esnault–Srinivas, arXiv:1105.2426v2](https://arxiv.org/pdf/1105.2426v2), theorem 1.1 and its cup-product/polarization setup. The finite-order statement applies to the maximal automorphism-stable subspace inside the polarization's orthogonal complement, exactly the subspace used by the scout after its identification with W-perp.

These were focused theorem-body checks, not complete readings of those papers. Takenawa's 14-blowup/Picard construction and all publication metadata were not independently re-audited in this bounded cross-check. No claim that the whole cited bibliography was reverified is intended.

## 4. Frobenius–surface corollary

The report assumes a smooth, projective, geometrically connected surface X/F_q, an F_q-automorphism g, an F_q-polarization h, ℓ not dividing q, and b₁=0. It takes the actual q-power Frobenius morphism Φ, n≥1 and r≥1. These hypotheses are sufficient for each stated step:

| Step | Independent check |
|---|---|
| Ordinary finite fixed-point count | d(gⁿΦʳ)=0 on the smooth surface, so the graph and diagonal meet transversely. The fixed scheme is zero-dimensional and reduced; properness makes it finite. |
| Φ* on W | Every (g*)ʲh is a divisor class defined over F_q. Untwisted pullback therefore equals q times that class. This proves Φ*\|_W=qI, not a scalar assertion on all H². |
| H²=W⊕V | W is a rational Néron–Severi subspace containing an ample class. Hodge index makes the restriction nondegenerate: the orthogonal part to h is negative definite over R, and scalar extension preserves nondegeneracy. |
| Identification of V | g* preserves the intersection form. Orthogonality to all (g*)ʲh is equivalent to remaining in h-perp under every g*-iterate. Hence V is precisely the maximal stable subspace in Esnault–Srinivas theorem 1.1. Tate twisting does not change g*'s order. |
| Φ-stability of V | g and Φ commute. More directly, Φ* scales the intersection form by q² and W by q, so Φ*(W-perp) lies in W-perp. Thus the restricted traces used in the report are defined. |
| Remaining cohomology | Geometric connectedness gives H⁰ trace 1; the automorphism preserves H⁴ and Φʳ contributes q^{2r}. Poincaré duality gives b₃=b₁=0, so no omitted odd-degree term remains. |
| Removal of finite-order phase | If M is an exponent of g* on V, the cancellation with the untwisted point count requires M dividing n. The report imposes this explicitly. |
| Integrality | W is defined over Q in NS⊗Q. Its intersection with NS modulo torsion is a g*-stable full lattice, so Tr(Aⁿ)−dim W is an integer. |

Accordingly the general trace decomposition and the difference

\[
\#\mathrm{Fix}(g^n\Phi^r)-\#X(\mathbb F_{q^r})
=q^r\bigl(\mathrm{Tr}(A^n)-\dim W\bigr),\qquad M\mid n,
\]

are correct consequences of the cited theorem and the classical proper fixed-point formula. The report's fixed-n series over r is explicitly a **formal generating series**. It is not claimed to be the dynamical zeta of gⁿΦ: indeed (gⁿΦ)ʳ would contain g^{nr}, not gⁿ. That potential clock mismatch is avoided in the actual prose and displayed definition.

No new Salem/centralizer statement is proved by this chain, and the report correctly treats it as an insufficiently novel direct corollary. The finite-order theorem does real mathematical work; its attribution is not hidden behind the elementary final subtraction.

## 5. Scope and final disposition

The report repeatedly states `REJECT_NO_CLOSED_NEW_LEMMA` for the HV proposal, rather than claiming that all ordinary-point formulas or the entire birational-surface family are impossible. The counterexample specifically invalidates the silent identification of scheme length/local index with ordinary cardinality; it does not invalidate every possible corrected formula. Likewise the Frobenius decision rejects its particular separation proposal, not every arithmetic observable on positive-entropy surfaces.

No repair request is needed. A reopened HV project would still need the full local-index/periodic-curve and affine-boundary analysis described by the scout; this audit does not provide that missing all-period theorem. The frozen report remains suitable as a **zero-contract scout record** under the present selection standard.
