# HCS-C59 proof package

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

## 1. Premise discipline

This written proof runs from C59-EXACT-0 through C59-EXACT-7. The official
producer and independently implemented checker bind those exact finite
premises at `PREFREEZE_CODE_RESULTS_PASS`; all eight gates pass, and the
independent post-refresh machine hostile audit is `POSTREFRESH_PASS`. No
staged pilot or design review is used as theorem authority. Although this
formal-root handoff changes prose after the machine tuple was frozen, its
independent formal-document audit has `FORMAL_DOCS_PASS`; paper and release
are not authorized.

## 2. Integrality of the scaled roots and orbit sums

Write the released eliminant as

\[
g(x)=Lx^{27}+b_{26}x^{26}+\cdots+b_0\in\mathbf Z[x].
\]

For a root (d_i), set (alpha_i=Ld_i). Substituting (x=y/L) and
multiplying by (L^{26}) yields

\[
y^{27}+b_{26}y^{26}+Lb_{25}y^{25}+\cdots+L^{26}b_0=0.
\]

Thus each (alpha_i) is an algebraic integer. The canonical sums

\[
\eta_\pm=\sum_{\{i,j\}\in\mathcal S_\pm}\alpha_i\alpha_j
\]

are algebraic integers. The unscaled sums, if mentioned, are
$\widetilde\eta_\pm$, with
$\eta_\pm=L^2\widetilde\eta_\pm$. Therefore the $G$-invariant
coefficients of the orbit products $R_\pm(T)$ are rational algebraic
integers and hence lie in $\mathbf Z$.

## 3. Stabilizer and primitive-element lemma

By construction, $H_\pm$ preserves $\mathcal S_\pm$, hence fixes
$\eta_\pm$. C59-EXACT-1 states that the setwise stabilizer of each support
is exactly the corresponding $H_\pm$, and that the 320 formal conjugate
values have pairwise distinct reductions at (p=692717).

If two characteristic-zero conjugate values were equal, their reductions at
every common integral prime would be equal. The distinct reductions therefore
prove 320 distinct characteristic-zero conjugates. Hence

\[
[G:\operatorname{Stab}_G(\eta_\pm)]=320.
\]

Since $H_\pm\leq\operatorname{Stab}_G(\eta_\pm)$ and
$[G:H_\pm]=320$, equality follows. Galois correspondence gives

\[
[\mathbf Q(\eta_\pm):\mathbf Q]=320,
\qquad
\mathbf Q(\eta_\pm)=K^{H_\pm}.
\tag{3.1}
\]

The orbit product is therefore the monic integral irreducible separable
minimal polynomial. This proves product-form exactness, not an expanded
characteristic-zero coefficient list.

## 4. Graph-labelling lemma

C59-EXACT-1 reconstructs all 27 modular lines from the exact lex shapes,
checks every line in all four chart equations, and recovers the Schlaefli
incidence graph. It also proves, inside the released labelled action,

\[
\operatorname{Aut}(\Gamma)=W(E_6)
\]

as equality of 51,840-element permutation sets.

Any two graph identifications differ by an element $w\in W(E_6)$. Replacing
the labelling by $w$ sends the support to $w\mathcal S_\pm$ and merely
permutes the full 320-member support orbit. Therefore it leaves the orbit
polynomial and the noncollision statement unchanged. Literal equality with a
particular embedded $K^{H_\pm}$ uses the one frozen labelling or transports
$H_\pm$ with the relabelling.

Eight sampled graph isomorphisms cannot replace this structural proof. The
historical bounded design enumeration remains feasibility evidence only; the
official G1 producer/checker replay supplies the project-local structural
proof.

## 5. Complete Gassmann and minimum-index lemma

C59-EXACT-2 computes the full induced trivial character for every one of the
350 subgroup conjugacy classes. Equality for (H_+) and (H_-) is therefore
full character equality, not equality on sampled Frobenius or cyclic rows.
The complete collision list shows that ToM 301/303 is the unique collision of
minimum index 320 in this table.

The unequal abelianizations `[2,3]` and `[2]` prove that (H_+) and (H_-)
are nonisomorphic, hence nonconjugate. James's prior eleven-collision result is
the source boundary; the finite replay identifies and durably binds the pair.

## 6. Common normal closure and field nonisomorphism

For $F=K^H$, the normal closure of $F/\mathbf Q$ inside $K$ is fixed by
the core of (H) in (G). C59-EXACT-2 gives trivial cores, so both normal
closures are (K).

If $F_+\cong F_-$ over $\mathbf Q$, extend such an isomorphism to an
automorphism of an algebraic closure. It preserves the common normal closure
(K) and conjugates the two point stabilizers inside (G), contradicting
nonconjugacy. Thus $F_+\not\cong F_-$.

## 7. Equality of Dedekind zeta functions

For (F=K^H), Artin formalism identifies

\[
\zeta_F(s)=L\!\left(s,\operatorname{Ind}_H^G\mathbf 1\right).
\]

The full rational permutation characters for (H_+) and (H_-) agree by
C59-EXACT-2, so

\[
\zeta_{F_+}(s)=\zeta_{F_-}(s).
\tag{7.1}
\]

This is an equality of Dedekind zeta functions. It supplies no new bad Artin
Euler factor, Frobenius, epsilon factor, or root number.

## 8. Signature

Let $c$ be complex conjugation. C59-EXACT-4 gives 168 $\langle c\rangle$-
orbits on each 320-point coset carrier. If (r_1) points are fixed and the
remaining points form (r_2) transpositions, then

\[
r_1+2r_2=320,\qquad r_1+r_2=168.
\]

Therefore

\[
r_1=16,\qquad r_2=152.
\tag{8.1}
\]

The sign of the discriminant is ((-1)^{r_2}=+1).

## 9. Conductor-discriminant calculation

On both coset carriers, the C58 filtration subgroups have orbit counts

```text
I3,P3,Q3,I5,P5,tame-C3,reflection-C2 =
36,56,112,16,64,128,160.
```

The permutation conductor exponents are

\[
v_3=(320-36)+\frac{320-56}{2}+(320-112)=624,
\tag{9.1}
\]
\[
v_5=(320-16)+\frac34(320-64)=496,
\tag{9.2}
\]
\[
v_A=320-128=192,\qquad v_B=320-160=160.
\tag{9.3}
\]

C58 proves that (K) is unramified outside the eight listed primes, so each
subfield is unramified there. The positive exponents prove that every listed
prime ramifies. Together with (8.1), this gives the exact signed identity

\[
\operatorname{Disc}(F_\pm)
=+3^{624}5^{496}A^{192}B^{160}.
\tag{9.4}
\]

No maximal order or degree-(320) expanded polynomial is needed for this
field-discriminant proof.

## 10. Double-coset/local-completion lemma

Fix a prime (w) of (K) over 3, with decomposition group (D) and inertia
(I). For (F=K^H), primes of (F) over 3, equivalently factors of
$F\otimes\mathbf Q_3$, are indexed by

\[
D\backslash G/H.
\]

For representative $g$, put $J=D\cap gHg^{-1}$. The corresponding
completion has

\[
n=[D:J],\qquad
e=[I:I\cap J],\qquad
f=[D:IJ],\qquad n=ef.
\tag{10.1}
\]

The right-coset computational convention is equivalent by inversion. A
(D)-orbit is one double coset and hence one completion factor, not a second
presentation layer.

For the C58 lower filtration at 3, the point-stabilizer orbit deficits give
the contribution (fd) of the completion to the global discriminant
exponent. C59-EXACT-5 and C59-EXACT-6 enumerate all double cosets and verify
the complete row tables.

## 11. Branch-independent local separation

In the ToM-140 branch, the (F_+) table contains eight factors of degree one
and the (F_-) table contains none. In the ToM-206 branch, the (F_+) table
contains four rows `(2,1,2,0)`, hence four copies of the unique unramified
quadratic extension, while (F_-) has no degree-two factor.

An isomorphism of finite etale $\mathbf Q_3$-algebras permutes field factors
and preserves their degrees. The distinct degree multisets prove
nonisomorphism in both branches. Thus no branch selection is needed.

Conversely, `(n,e,f,d)` does not determine a high-degree local field up to
isomorphism. The proof uses only the one-way degree obstruction.

The equal zeta functions are compatible with this: in the ToM-140 branch
both tables have 36 residue-degree-one factors, and in the ToM-206 branch both
have 18 residue-degree-two factors.

## 12. Scope locks

`NO_BAD_EULER_OR_ROOT_NUMBER`.

The argument proves no integral permutation equivalence, ring-of-integers
isomorphism, class-number equality, local equivalence, adelic equivalence,
selected decomposition branch, individual local-field classification,
expanded coefficient vector, integral basis, maximal order, monogenicity,
bad Euler/Frobenius/epsilon/root-number statement, Artin holomorphy,
automorphy, rational point, Brauer--Manin obstruction, motive, RH, or
Hilbert--Polya operator.

## 13. Machine evidence boundary

One unchanged official tuple certifies the exact premises. It contains 13
source files, 8 result files, 21 live code/result entries, and 20
self-excluding scoped entries. The 15-key payload has 10,412 scalar leaves;
the checker rejects 20,894 certificate rebound mutations and 8 evidence
mutations; and all 48 tests pass.

The official SHA-256 values are payload
`a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b`,
certificate
`3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a`,
check report
`271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3`,
schema file
`07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4`,
group/resolvent evidence
`0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958`
and
`667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6`,
scoped manifest
`c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda`,
payload shape
`788aa5e58d51f0d4edfa7a4e58de5748bd5a1ad1d28445d91045d5dd72c850d2`,
and G0 subpayload
`ac445822702b5e376eed6fbfa86a4df81c7f8177ca35c8211282dca830123d5d`.

The machine layer, its hostile audit, and the separate `FORMAL_DOCS_PASS` do
not imply paper proof review, compilation, promotion, or release. Those later
gates remain `PAPER_PENDING / NOT_RELEASED`.
