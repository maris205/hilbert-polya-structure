# HCS-C64 theorem package

Status: **PREFREEZE_IMPLEMENTED / PAPER_COMPILED / NOT_RELEASED**.

Let (G=W(E_6)), (|G|=51840), and let (S_1,ldots,S_{16}) be the
core-free subgroup representatives from the C62 dictionary.  Put
(X_j=G/S_j) and define the restricted Burnside mark map
[
m:\mathbb Z\{X_1,ldots,X_{16}}\longrightarrow\mathbb Z^{16},
\qquad m(X_j)_i=|X_j^{S_i}|.
]

The exact source-replayed matrix (M=(m(X_j)_i)) has
[
\operatorname{rank}_{\mathbb Q}M=16,
\qquad \det M=226492416=2^{23}3^3.
]
Consequently the restricted 16-type Burnside map is injective over
(mathbb Q) (and over (mathbb Z) after tensoring), even though C63's
permutation-character linearization has a three-dimensional rational kernel.

For the C63 relation
[
R_4=X_2+X_3+X_5+X_6-X_{11}-X_{12}-X_{13}-X_{14},
]
[
m(R_4)=(0,4,2,0,0,-2,0,20,0,0,-2,-4,2,0,0,0)^T.
]
In particular its (S_2)-mark is 4 and it is nonzero in the restricted
Burnside module; the mark vector has content 2.

The theorem is finite-group and support-restricted.  It does not assert
injectivity for the full Burnside ring or any arithmetic/local consequence.

## Gates

- G0: C61/C62/C63 byte rebind and scope checks.
- G1: exact group, subgroup order, core-free, and mark-integrality checks.
- G2: full 16-by-16 matrix, determinant, rank, and relation image.
- G3: independent checker, clean replay, hostile mutations, and paper audit.
