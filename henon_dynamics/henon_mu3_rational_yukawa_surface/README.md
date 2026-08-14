# HCS-C55: the Yukawa cubic surface over Q of the fourth Hénon dihedral core

Status: **DOCS_FINAL_NO_MORE_EDITS; exact code/results, paper source, official
PDF, compilation report, Route-A record, and the verified 47-entry
full-project inventory are frozen against RELEASE_CANDIDATE evidence; the
implementation commit is deferred to the later provenance stage**.

Let $K=\mathbf Q(\rho)$, where $\rho^2+\rho+1=0$, and let

\[
X=V(C,Q)\subset\mathbf P^7_K,
\qquad
C=\sum_{i=0}^7x_i^3,
\qquad
Q=\sum_{i=0}^6x_ix_{i+1}+\rho x_7x_0.
\]

HCS-C53 gives an explicit equation model $X_0/\mathbf Q$ and a descended
rank-$10$ Reynolds Chow core. HCS-C54 identifies the full projective
monomial ideal stabilizer as

\[
G=\operatorname{Dih}(C_{12}),\qquad |G|=24,
\]

and descends its ambient action to a nonconstant finite etale
$\mathbf Q$-group scheme $\mathscr G$. Only two geometric elements are
rational points; all $24$ elements participate in the Reynolds average.

## Theorem in one paragraph

The project constructs a smooth four-dimensional rational algebraic germ
$B_{\rm core}$ inside the $\mathscr G$-fixed Hilbert locus, transverse to
the kernel of the embedded Kodaira--Spencer map. The restricted universal
family carries the relative Reynolds graph correspondence. Its image on
$R^5f_*\mathbf Q(1)$ is a polarizable rank-$10$ variation of Hodge
structure of Calabi--Yau-threefold type

\[
(h^{3,0},h^{2,1},h^{1,2},h^{0,3})=(1,4,4,1),
\]

and its period map is locally immersive. At the central point, exact Cayley
ring multiplication produces a rational projective Yukawa cubic
$Y_H\in\mathbf Z[u_0,u_1,u_2,u_3]$. The homogeneous gradient quotient
has length $16$, proving that $V(Y_H)\subset\mathbf P^3$ is
a smooth geometrically irreducible cubic surface. Failure of projective
$\operatorname{GL}_4(\mathbf C)$-equivalence with an honest CY3-family
Yukawa tensor is then a rigorous necessary local-VHS obstruction. A match is
only permission to run stronger tests; it is not a motive.

“Rational” here means that the cubic and its surface are defined over
$\mathbf Q$; it does not assert that the cubic surface is a rational variety
over $\mathbf Q$.

## Algebraization firewall

The entire fixed Hilbert germ is **not** asserted to have dimension four.
Its tangent space is $H^0(N_{X/\mathbf P^7})^G$ and includes ambient/gauge
directions. The fourfold is a chosen smooth rational slice whose tangent is a
complement to the kernel of

\[
H^0(N_{X/\mathbf P^7})^G\twoheadrightarrow H^1(T_X)^G.
\]

The family is obtained from the Hilbert universal family. Tangent classes
represented by cubic polynomials are not silently promoted to a literal
linear family $C+\sum t_ip_i$.

## Cayley and motive firewalls

With $F=yC+zQ$, the four roles

\[
yp\in R_{1,0},\quad
y^2p\in R_{2,-3},\quad
y^4p_ip_jp_k\in R_{4,-3},\quad
y^5p_ip_jp_k\in R_{5,-6}
\]

are respectively a tangent operator, its first Hodge variation, its third
variation, and the result after pairing with the $H^{4,1}$ generator. They
must never be collapsed. In particular, contracted classes in
$R_{2,-3}$ are not multiplied directly to model the IVHS.

The relative theorem uses only the Reynolds graph correspondence acting on
$R^5$. It does not claim a relative Chow--Künneth projector. The central
fiber agrees on $H^5$ with the already released C53 projector
$\pi_5e_{\mathscr G}$.

One Tate twist is exact: $\mathbf Q(1)$, not $\mathbf Q(2)$. Equal Hodge
numbers or projectively equivalent Yukawa cubics do not identify a rational
Hodge structure, a VHS, or a Chow motive.

## Comparator status

The generic four-parameter Braun--Candelas--Davies
$\operatorname{Dic}_3$ and $\mathbf Z_{12}$ quotient families are admitted
as honest $(h^{1,1},h^{2,1})=(1,4)$ comparators. Their published
mirror-side one-parameter special geometry is not the required
four-variable B-model tensor of the original quotients, and the
enhanced-dihedral $c_0=c_1=0$ locus is generically nodal.
Until a full tensor and an exact $\operatorname{GL}_4$ incidence calculation
exist, the release label is NOT-COMPARABLE-WITH-CURRENT-DATA.

## Current provenance

- chronology-only theorem-design note SHA-256
  24a7d07fd15399346f4d5efeea10d3ae3b92a31239b523552fc4c51599519161
  (unpackaged history; not a theorem input or release dependency);
- payload:
  `6afc529d2ab9e849592d9eba7b76324cc7a840670f50c669f90fdd079c0b4323`;
- certificate:
  `aa6a57bc496d78afd5728640083179bb0dd24963deb44e31459c59edc71c381f`;
- independent check:
  `e24c90fac1b222ed161eec677c06209c901f0decc335e769dc7df4ce53c68469`;
- schema:
  `2961eb6b5b4aefa0e12ffcb59c9e1095b14f0309e2045fd6d8a7f636dc6dca53`;
- persistent scoped manifest:
  `7f1fa8bc6f22dd89b6b9a41ae2353129853f39430ba932f048ff295e56ba30e6`;
- stable 18-file paper-source aggregate:
  `93495af19048605bd814af264bcf3b2d745a5fdd4f94af31c9422d3bc3782221`;
- paper PDF:
  `ea75d7e0134531bd02b9ed32ae96aa8cd4416214d3913e19816922af6c30ccae`;
- final LaTeX log:
  `690ea4a3fd8af63384f02cf05eebadab5c2a4b9746bc7da999e54c18c59135a2`;
- extracted paper text:
  `6eb5fb4b9bb4a23b68cadbce75c9cf16a61637031a3dba7dc3106a4cf5d32b19`;
- compilation report:
  `b38790520104f13bf8c4348bf7c9453c86ed1f3d09bfda98e024172556ec812b`;
- Route-A record:
  `8fe1db8504b71b83e2669371a8ecf485c6755700050bb6ae7527782d83c6ef11`;
- full-project manifest: 47 verified entries; its SHA-256 is reported only
  outside manifest-covered artifacts to avoid a self-hash cycle;
- implementation commit: null by design at this provenance stage.

An independent read-only source/paper/hostile audit passed. No unpackaged
temporary-file hash is used as release authority.
