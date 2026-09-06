# Twelfth bounded finite-system slate — intake before code

Date: 2026-09-06 UTC. Author: `batch197_fifth_scout`. This folder is the
entire write scope. P207 B is sealed; OFS, triangulations and flip-family
proofs are excluded and have not been read for this task. No paper number,
admission, central-index edit, Git operation or external release is authorized.

This file was created before any new pilot source or pilot execution. There
are six literal desk candidates across simple graphs, matrices, matrix
subspaces and affine subsets. Only three receive pilots. A desk rejection
is not an executed system and is not a paper candidate retained by default.

## Literal definitions and immutable full boxes

| Code | Autonomous map on a fixed finite carrier | Full pilot boxes |
|---|---|---|
| STC | On labelled simple graphs on `[n]`, let `P_e(G)` be the parity of the number of spanning trees of G containing edge e (zero for absent edges). Output `K_n` minus the edges with `P_e(G)=1`. | All graphs, n=1,2,3,4,5,6; 33,867 states total. |
| PCG | On `M_r(F_p)`, output entry `(i,j)` equal to the permanent of the matrix obtained by deleting row i and column j. There is **no transpose**, no threshold and no division. | `(r,p)=(2,3),(2,5),(2,7),(3,3)`; all 22,790 matrices. |
| UMP | On all subsets S of `F_p^d`, output each m for which exactly one unordered pair of **distinct** a,b in S satisfies `a+b=2m`. Counts are integers, not residues. | `(p,d)=(3,0),(3,1),(3,2),(5,1),(7,1),(11,1)`; all 2,730 subsets. |
| SRS | On the subspaces of `M_2(F_q)`, q odd, send U to the linear span of all A with `A^2 in U`. | None: generic two-step erasure deduced below. |
| NCS | On the subspaces of `M_2(F_q)`, q odd, send U to the span of all N with `N^2=0` and `Nu=uN` for every u in U. | None: centralizer classification deduced below. |
| QSZ | On all subsets S of `F_p`, p odd, output the roots x of `sum_(a in S)(x-a)^2=0` in `F_p`. | None: degree-two moment collapse deduced below. |

PCG state sum is `3^4+5^4+7^4+3^9 = 22,790`; combined executed intake is
59,387 states in 16 boxes. These boxes will not be enlarged, narrowed or
replaced after seeing a result. No random sampling, GPU, learned surrogate,
parameter tuning or excluded rank/word/contrast/visibility family is used.
Expected CPU cost is below one minute per complete run. Two actual isolated
executions will be recorded with raw stdout, exit status, before/after input
pins, runtime flags and exact-byte comparison. Any failed run is preserved.

## Historical collision deductions made before pilots

The initial ideas UCN (unique common-neighbor graph), quartic Hessian,
derived subspace `[U,U]`, hypergraph pair-parity completion, and unique
orthogonal point feedback were discarded **before this slate**: exact or
stronger historical rules exist. They are not counted among these six.
Historical unique-perfect-matching adjugation uses Boolean output, exact
integer value one and transposed cofactors; it is not PCG over an odd field.
Nevertheless every determinant/adjugate, characteristic-two and 2x2-linear
PCG component is zero-credit background. Exact scan paths and sources are
recorded in `SOURCE_AND_COLLISION.md`; no claim of exhaustive novelty is made.

The standard generic mechanisms are charged in advance:

* STC: matrix-tree, deletion/contraction and binary cut/bicycle linear
  algebra. With reduced incidence vectors b_e and reduced Laplacian L,
  `P_e=A_e b_e^T adj(L)b_e`. Symmetry in characteristic two cancels all
  cross terms. Writing d for the diagonal of adj(L), with the deleted vertex
  assigned zero, gives `P_uv=A_uv(d_u+d_v)`. Thus the removed edges form a
  cut of G; the first output is co-bipartite. If corank L>=2 it is K_n.
  This factorization and any one-step fibre restatement carry no novelty.
  The complement prevents direct monotone-erasure deduction; a global
  temporal theorem and independently evaluated inverse/extremal theorem
  are both still missing at intake.
* PCG: permanence is a classical homogeneous polynomial and this is its
  gradient. For r=2, `(a,b;c,d)` maps to `(d,c;b,a)`, an involution with
  singleton fibres, entirely deducted. For p=2 it is the determinant
  gradient and classical double adjugation applies; p=2 is excluded before
  pilot. Static homogeneous scalar restrictions and rank-one restrictions
  do not supply a second paper axis. General odd-field r>=3 dynamics and
  evaluated all-target fibres are missing.
* UMP: restricted sumset representation counts and affine equivariance are
  classical/static. Empty and singleton inputs go to empty; two-point
  inputs go to their midpoint singleton, then empty. This does not prove
  the full system transient. No generic triangular/Fitting/normalizer or
  greedy-basis reduction has been established. A complete core/clock and
  independently evaluated inverse theorem remain missing.

## Analytic desk exclusions, before any computation

Write Z=F_q I and S=sl_2(F_q), q odd.

**SRS.** Square-zero matrices span S: E=E12, F=E21, and
`N=(1,1;-1,-1)` are square-zero, and `diag(1,-1)=N-E+F`.
Conversely square-zero matrices have zero trace. Thus every output contains
S. The matrix `X=(0,-1/2;1,1)` has trace one and determinant 1/2, so
`tr(X^2)=tr(X)^2-2 det(X)=0`. Hence SRS(S) contains S and X and is all
M_2. Monotonicity now gives SRS^2(U)=M_2 for every U. The constant core and
two-step clock are a generic span-erasure wrapper. No pilot is warranted;
status `DESK_KILL_GENERIC_ERASURE`.

**NCS.** Central U (exactly 0 or Z) has output S. If U is not central and
a nonzero square-zero N commutes with U, the centralizer of N is Z+F_q N:
in a Jordan basis direct multiplication proves this. Thus U is contained
in that plane but not in Z; conversely every such U has output F_q N.
Indeed any noncentral A=aI+bN with b nonzero has the same centralizer,
whose only square-zero matrices are multiples of N (trace forces its
scalar coefficient zero). All other U have output 0. Consequently
0 and S form a two-cycle and each nilpotent line is fixed; every output
already lies in this core. There are q+1 nilpotent lines, since each is
uniquely specified by its common image/kernel line in F_q^2.
The fibre over S has size 2; each nilpotent-line fibre has q+1 members
(q noncentral lines and their common plane); the zero fibre has
`G_4(q)-2-(q+1)^2` members, where `G_4(q)` is the total subspace count.
`G_4(q)=q^4+3q^3+4q^2+3q+5` follows by summing Gaussian binomials.
The remaining target fibres are empty. These are a complete elementary
centralizer/projection adapter, not a retained temporal contribution.
Status `DESK_KILL_GENERIC_CENTRALIZER`.

**QSZ.** The defining polynomial is `m0 x^2-2m1 x+m2` with the three
ordinary subset moments reduced modulo p. Its root set has size 0,1,2 or p.
Singletons are fixed; empty maps to the full field. For p>=5 the full field
is fixed because its first three power sums are zero. For p=3 it maps to
empty. A pair `{c-d,c+d}` (d nonzero) maps to the roots of
`(x-c)^2=-d^2`: to empty if -1 is nonsquare; otherwise to `{c-id,c+id}`,
where i^2=-1, and a second application returns the pair. No such pair is
fixed for odd p. Therefore every trajectory enters a fixed point or a
two-cycle in at most three steps. This entire time axis is a degree-two
moment/root-collapse wrapper. Counting source subsets with prescribed
moments is a static inverse constraint, not an evaluated independent
extremal theorem here. Status `DESK_KILL_GENERIC_MOMENT_COLLAPSE`.

These desk proofs are author deductions, not independent reviews. They are
included so that a true but automatic clock cannot later be promoted by a
large finite inverse census. No all-parameter proof is inferred from a pilot.
