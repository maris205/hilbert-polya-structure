# HCS-C59 narrative report

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

## 1. From one line field to two new fields

C56 proved that the 27 lines on the fixed cubic surface generate a normal
field (K) with Galois group (W(E_6)). C58 then determined exactly how that
normal field ramifies, including the complete lower inertia filtrations. At 3
it deliberately leaves two decomposition groups, ToM 140 and ToM 206.

C59 does not try to settle that remaining group choice. Instead, it builds two
new subfields of (K) for which the same zeta function conceals different
ramified local algebras in either branch.

## 2. Why an abstract subgroup pair is not enough

James already found all eleven Gassmann collisions among the 350 subgroup
classes of (W(E_6)). Merely writing (K^{H_+}) and (K^{H_-}) would be
formal Galois correspondence, not a sufficient successor paper.

The new bridge comes from the labelled line coordinates. Scale each eliminant
root by the leading coefficient, (alpha_i=Ld_i), and form two quadratic
pair-support sums. The (H_+) support is a disjoint union of two 27-pair
orbits; the (H_-) support is one 81-pair orbit. The scaled integral sums are
called (eta_+) and (eta_-) throughout C59.

## 3. Primitive realization

The exact G1 gate proves that the supports have stabilizers (H_+) and
(H_-), and that at the fully split prime 692717 each sum has 320 distinct
conjugate reductions. Equality of two characteristic-zero conjugates would
survive reduction, so the modular noncollision proves that the sums generate
the full fixed fields.

The exact resolvents are finite products over $G/H_\pm$. They are monic
integral minimal polynomials in product form. Printing an enormous expanded
characteristic-zero coefficient table would add bulk but is not a premise.

The official producer and independently implemented checker reconstruct all
27 lines, all four chart equations, the Schlaefli graph, and the equality of
its full 51,840-element automorphism set with the released (W(E_6)) action.
The split-prime primitivity witness and graph-labelling bridge are therefore
project-local G1 facts at the frozen machine tier, not merely feasibility
evidence.

## 4. Equal zeta, different fields

The two subgroup actions have the same full rational permutation character,
so Artin formalism gives equal Dedekind zeta functions. Their cores are
trivial, so both fields have normal closure (K). Their subgroup invariants
differ, so they are not conjugate and the fields are not isomorphic.

The minimum-index description is restricted to the complete (W(E_6))
subgroup table and is explicitly placed after James's prior collision count.
It is not a minimum-degree theorem for arithmetically equivalent fields in
general.

## 5. Exact global arithmetic

The C58 filtration acts on each 320-point coset carrier with the same orbit
counts. The conductor-discriminant calculation gives

\[
\operatorname{Disc}(F_\pm)
=+3^{624}5^{496}A^{192}B^{160}
\]

and signature ((16,152)). The sign is positive because (r_2=152) is even.
The support is exactly the eight primes already ramified in (K): no new
prime can appear in a subfield, and every displayed exponent is positive.

## 6. The branch-independent separator

In the ToM-140 branch, $F_+$ has eight $\mathbf Q_3$ factors and $F_-$
has no degree-one factor. In the ToM-206 branch, (F_+) has four unramified
quadratic factors and (F_-) has no degree-two factor. Thus the products of
completions are nonisomorphic whatever the unresolved decomposition group is.

The complete row tables also reconcile the equal zeta functions: their
residue-degree counts agree even though the ramification-index/local-degree
splits differ. The row tuple is not promoted into a classification of each
high-degree local field.

## 7. Prior-art and salami boundary

Gassmann/Perlis theory, classical locally inequivalent arithmetic-equivalence
examples, and relative resolvents are prior art. The standalone weight comes
only from the exact primitive cubic-surface realization joined to the complete
global arithmetic and both local branches. These parts remain one paper.

## 8. Machine evidence and current state

The official prefreeze tuple contains 13 source files and 8 result files: 21
live code/result leaves, of which the self-excluding manifest binds 20. All
eight gates G0--G7 pass. The 15-key payload contains 10,412 scalar leaves;
the independent checker rejects 20,894 certificate rebound mutations and 8
evidence-carrier mutations; and all 48 tests pass. The independent
post-refresh machine hostile audit is `POSTREFRESH_PASS`.

The principal SHA-256 bindings are payload
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

This handoff changes formal-root prose after the machine tuple was frozen;
the refreshed aggregate now has an independent `FORMAL_DOCS_PASS`. No paper,
paper audit, release archive, promotion, or release is asserted.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains the operative analytic firewall.
