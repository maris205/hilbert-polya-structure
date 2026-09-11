# Algebra lane: scout-and-kill ledger

Freeze date: 2026-09-03.  The ledger contains **15 conservative, genuinely
different literal systems**.  Changing a parameter, basis, or conjugating a
map was not counted as another system.  The final coordinator decision is
A01 `SELECTED_P182`, A02 `RESERVE`, and every other entry `KILL`.

## Decision table

| ID | Literal carrier and map/kernel | Exact small-box signal | All-parameter theorem axes | Decision |
|---|---|---|---|---|
| **A01 / CLC** | `L_d(q)^3`, where `L_d(q)` is the subspace lattice of `F_q^d`; `T(A,B,C)=(C,A cap B,A+B)` | Exact pilot: `(q,d)=(2,4)` has 300,763 states, image 34,371, 513 fixed points, 4,376 strict 2-cycles, and depth census `9265,157272,134226`; every fibre is checked target by target | arbitrary prime power `q`, all `d>=1`: full temporal census plus image and every-target fibres | **SELECTED — P182**. Short tower and a nontrivial 2-clock coexist; complement-pair fibres give a second independent spine |
| **A02 / LDS** | all subspaces of `L_{z,q}=F_q^z direct-sum sl_2(F_q)` for odd `q`; `D(U)=span{[x,y]:x,y in U}` | Exact pilot: `(q,z)=(3,2)` has 2,664 states, image 15, two fixed points, depths `2,1128,1534`, and positive fibre sizes `118,292,838`; `(5,1)` independently passes | every odd prime power `q`, all central dimensions `z>=0`: image, cycles, depths, and every-target fibres | **RESERVE #1**. The bracket isomorphism `Lambda^2 sl_2 ~= sl_2` and a closed central-lift count close the two axes |
| A03 / TCC | `M_2(F_q)`, odd `q`; `A -> AA^t-A^tA` | At `q=7`: 2,401 states, image 49, unique fixed point, depths `1,384,2016`; zero fibre 385 and every nonzero image fibre 42; `T^2=0` | all odd `q`: factorization and full fibres | **KILL**: exact but the square-zero diagonal/transpose commutator mechanism transfers too directly from P175 |
| A04 / BHD | `{0} union P(Sym^4 F_q^2)`; `0->0`, `[f]->[det Hess(f)]` when nonzero and to `0` otherwise | Ordinary formal derivatives give an identically zero Hessian in characteristic 3 (122 states, one-point image).  At `q=5`: 782 states, image 452, cycles `1:26,2:60,3:40,4:30`, height 2 | `q` versus characteristic/residue class; invariant-theoretic fibre strata | **KILL**: striking clocks, but no closed uniform fibre/temporal theorem emerged and the Hessian covariant has an obvious classical owner field |
| A05 / CHS | `M_2(F_q)`; `A -> A^2-tr(A)A=-det(A)I` | At `q=3`: 81 states, image 3, fixed scalars `0,2I`, height 2; determinant fibres are 33 over zero and 24 over each nonzero value | all `q`, determinant class and scalar power dynamics | **KILL**: Cayley--Hamilton scalarization hands the problem to scalar power/radial dynamics (P103/P180) |
| A06 / SLP | subspaces of `V=X direct-sum K`, `dim X=2`; `U -> (pr_X U)^perp`, embedded in `X` | Over `F_3` with the anisotropic dot form: 28 states, image 6, three 2-cycles, height 1; fibre sizes are `2,4,4,4,4,10` | `q`, form type, and dimensions of `X,K` | **KILL**: a Galois/polarity retraction; P143 and earlier OFP polarity arguments own the mechanism |
| A07 / SYZ | module isomorphism types over `R=F_q[t]/(t^e)` with at most `r` cyclic summands; syzygy sends a part `a<e` to `e-a` and deletes a free part `e` | `(e,r)=(4,3)`: 35 partitions, 20 recurrent, 6 fixed, 7 strict 2-cycles, height 1; a reachable target of length `l` has `r-l+1` type-preimages | all `e,r`; partition involution and deletion fibres | **KILL**: this is the textbook hypersurface-syzygy involution on module types, so ownership is immediate |
| A08 / ART | `{0}` plus intervals `[i,j]` of the linearly oriented `A_m` quiver; `[i,j]->[i+1,j+1]` if `j<m`, otherwise `0` | `m=3`: 7 states, unique fixed state 0, height 3; zero fibre 4 and every other reachable fibre 1 | all `m`; exact level/fibre census | **KILL**: it is the Auslander--Reiten translation on indecomposables with the boundary totalized |
| A09 / RQC | isomorphism types of finite abelian `p`-groups; from `G`, choose uniform `x in G` and move to `G/<x>` | From `Z/4 x Z/2`: probabilities to types `(2,1),(1),(2),(1,1)` are respectively `1,4,2,1` divided by 8 | prime `p`, partition type; Hall-polynomial transition kernel | **KILL**: direct random-quotient erosion, colliding with the P173 motif and classical finite-abelian-group enumeration |
| A10 / RGC | conjugacy classes of `S_n`; fix `g` in the class, choose uniform `h`, move to the class of `[g,h]` | For `S_3`: identity goes to identity; a transposition gives identity/3-cycle with counts `2/6,4/6`; a 3-cycle gives `3/6,3/6` | all `n`; character/centralizer formula for the class kernel | **KILL**: no uniform temporal closure signal beyond direct commutator and commuting-pair ownership |
| A11 / MLG | `GL_2(F_4)`; Lang map `A -> A^{-1} bar(A)`, with Frobenius `bar(a)=a^2` | Exact exploratory enumeration: 180 states, image 30, 21 fixed points, depths `21,105,54`, and 30 nonempty fibres all of size 6 | `GL_n(F_{q^r})`, Frobenius order, norm-one strata | **KILL**: Lang--Steinberg/Hilbert 90 owns the image/fibre engine; inverse/power motifs also meet P102/P168 |
| A12 / SRA | additive group `Sym_2(F_q)`; Markov step `A -> A+vv^t` for uniform `v in F_q^2` | At `q=3`, 27 states; increment multiset is zero once and four rank-one points twice.  The 27 Fourier characters have phase-count signatures `(9,0,0):1,(5,2,2):12,(1,4,4):6,(3,6,0):4,(3,0,6):4` | odd `q`, rank and discriminant; quadratic Gauss sums | **KILL**: a translation-invariant Cayley walk whose Fourier solution transfers from P177 |
| A13 / SGE | disjoint union of ordered symmetric matrices of sizes `0..n`; take the Schur complement at the first nonzero diagonal pivot, otherwise the first nonzero hyperbolic `2x2` pivot, and delete one coordinate from a zero matrix | `n=2,q=3`: 31 states, unique sink, depth census `1,5,25`, sharp height 2 | all `n,q`; pivot-type and congruence-rank descent | **KILL**: canonical symmetric Gaussian elimination/LDL is the whole mechanism; the descent clock is owner-obvious |
| A14 / JDS | all subspaces `U <= M_2(F_q)`; `J(U)=span{XY+YX:X,Y in U}` | At `q=3`: 212 states, image 72, cycles `1:49,2:4`, depths `57,125,30`; fibre histogram includes sizes `1,2,5,7,9,24,27` | `q` and ambient matrix size; Jordan-product ranks | **KILL**: no stable all-`q` atlas appeared, and subspace-product/closure pressure from P97 is severe |
| A15 / LAS | pairs of subspaces `(U,V)` of `M_2(F_2)`; `T(U,V)=(Ann_l(V),Ann_r(U))` | 4,489 states, image/recurrent core 25, 5 fixed and 10 strict 2-cycles, height 1; nonzero fibre sizes `1,4,16,54,216,2916` | `M_n(F_q)`, annihilator-closed subspaces | **KILL**: triple-annihilator/Galois-polarity transfer, squarely inside P143/OFP territory |

## Why only two survive

A01 and A02 each close **two independent unbounded axes** and each offers two
claims that do not reduce to a size-only orbit table: a temporal theorem and an
every-target fibre theorem.  A03 is mathematically cleaner than many rejected
ideas, but cleanliness does not overcome its internal collision.  A04 has the
best unexplained exploratory clock after the finalists, yet its characteristic
dependence and absent uniform fibre law make it an intentionally early kill.

The exact verifier freezes A01, A02, and the A03 kill-control.  Small results
for the other twelve are screening observations only and are not used as proof
or novelty evidence.
