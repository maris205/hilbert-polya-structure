# C63 research question

Let `G=W(E_6)` and let `Y_i=G/S_i` for the 16 subgroup-conjugacy types
`S1,...,S16` in the C62 fixed-field dictionary.  What is the exact rank and
kernel of
\[
  \operatorname{lin}_{16}:\mathbb Q\{Y_1,\ldots,Y_{16}\}
       \longrightarrow \operatorname{Class}_{\mathbb Q}(G),
\]
where the map sends a transitive set to its permutation character?

The target theorem is that the 25-class character matrix has rank 13 and
kernel dimension 3, with basis (using the C62 type labels)
\[
 z_1=Y_{10}-Y_9,\qquad
 z_2=Y_2+Y_3+Y_5+Y_6-Y_{11}-Y_{12}-Y_{13}-Y_{14},qquad
 z_3=Y_{16}-Y_{15}.
\]
The C62 exterior-square difference is `-z_2` under the plus-minus convention
used in its evidence, while the symmetric-square difference is `-z_2-z_3`.
The central new support-restricted relation is therefore
\[
 R_4=Y_2+Y_3+Y_5+Y_6-Y_{11}-Y_{12}-Y_{13}-Y_{14}=0.
\]
Its eight terms occur in four plus/minus pairs of equal degree but
nonconjugate stabilizers; no proper subrelation is in the restricted kernel.

The `z_1=Y_{10}-Y_9` relation is an inherited C60 collision and is explicitly
not claimed as new.

No assertion is made about the kernel of the full Burnside ring: C63 is
explicitly the 16-type submodule determined by the complete C62 atlas.
