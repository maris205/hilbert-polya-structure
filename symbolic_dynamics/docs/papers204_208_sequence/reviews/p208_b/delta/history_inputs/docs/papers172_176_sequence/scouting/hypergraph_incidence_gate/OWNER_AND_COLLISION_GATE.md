# Owner and collision gate: odd pair-codegree feedback

**Gate date:** 2026-09-03 UTC  
**External state:** `HOLD_EXTERNAL`  
**Final disposition:** `KILL_DIRECT_OWNER_AND_INTERNAL_SILHOUETTE`  
**Allocation:** none

## 1. Literal object being gated

The carrier is the set of labelled $3$-uniform hypergraphs on $[n]$, written
as $C_2=\mathbb F_2^{\binom{[n]}3}$.  If $W=W_{2,3}$ is pair--triple
incidence, the update is

$$
L=W^{\mathsf T}W=I+A(J(n,3)).
$$

Thus the next bit on a triple is the parity of its three current
pair-codegrees.  The exact new calculation in this gate factors through the
Eulerian boundary graph $b=Wx$ and proves

$$
L^2=\begin{cases}L,&n\text{ odd},\\0,&n\text{ even},\end{cases}
\qquad
\operatorname{rank}L=
\begin{cases}\binom{n-1}{2},&n\text{ odd},\\
\binom{n-2}{2},&n\text{ even}.
\end{cases}
$$

It also decomposes a nonempty one-step fibre into compatible Eulerian
boundary graphs and fillings of each boundary.

## 2. Primary-source owner audit

| source | source-owned surface | consequence here |
|---|---|---|
| René Peeters, [*On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs*](https://www.maths.tcd.ie/EMIS/journals/JACO/Volume15_2/v121065651493101.fulltext.pdf), *J. Algebraic Combin.* 15 (2002), 127--149, DOI [10.1023/A:1013842904024](https://doi.org/10.1023/A:1013842904024), Section 4.1 | For the Johnson adjacency matrix $A$, records the binary minimal-polynomial split $(x+k)^2$ for even $n$ and $x(x+1)$ for odd $n$, and the exact rank of $A+kI$: $\binom{n-2}{k-1}$ for even $n$ and $\binom{n-1}{k-1}$ for odd $n$. | At $k=3$, $A+kI=A+I=L$.  Hence both the square law and both rank formulas are directly owned, apart from degenerate small carriers that are immediate checks.  This is the decisive external hit. |
| R. M. Wilson, [*A diagonal form for the incidence matrices of t-subsets vs. k-subsets*](https://doi.org/10.1016/S0195-6698(13)80046-7), *European J. Combin.* 11 (1990), 609--615 | Diagonal form and modular ranks of inclusion matrices.  Peeters explicitly invokes this theorem for $W_{k-1,k}$ and the Gram matrix $W^{\mathsf T}W$. | Owns the general inclusion-matrix rank infrastructure; it is background rather than the only kill because Peeters already reaches this exact Johnson Gram. |
| E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori, and M. Mohammad-Noori, [*Inclusion Matrices and Chains*](https://arxiv.org/abs/0709.3144) | Reobtains Wilson's diagonal form and exact solution criteria for inclusion-matrix equations. | Confirms that treating $W_{2,3}$ and its lift equations as an unexplored linear object would be untenable. |
| A. M. Duval, C. J. Klivans, and J. L. Martin, [*Simplicial Matrix-Tree Theorems*](https://arxiv.org/abs/0802.2576), *Trans. AMS* 361 (2009), 6073--6114 | General simplicial boundary and up/down Laplacian framework. | Background owner for the Laplacian viewpoint only; it does not by itself state this finite iteration or the labelled fibres. |

The Peeters hit is literal after the one-line identity
$W_{2,3}^{\mathsf T}W_{2,3}=I+A(J(n,3))$.  The finite-map consequences of an
idempotent or square-zero linear map (depths, zeta factors, and uniform
fibres) are then mechanical.  They cannot be counted as an independent
temporal theorem package.

## 3. What remains after owner subtraction

The boundary factorization gives a clean refinement.  Write $Z$ for the
Eulerian graph space and $\mathcal B=Z\cap Z^\perp$ for its bicycle space.
For $y\in\operatorname{im}L$, the compatible $b\in Z$ with
$W^{\mathsf T}b=y$ form an affine coset of $\mathcal B$:

$$
\#\{b\in Z:W^{\mathsf T}b=y\}=
\begin{cases}1,&n\text{ odd},\\2^{n-2},&n\text{ even}.
\end{cases}
$$

Every such $b$ has $2^{\binom{n-1}{3}}$ hypergraph fillings.  This explains
the kernel size rather than merely restating it.  It is nevertheless a
uniform unmarked factorization of a linear fibre.  It has no target-sensitive
enumerator, nonuniform inverse geometry, or residual clock beyond the square
law already owned by Peeters.  The residual is therefore below a standalone
paper threshold.

Bounded queries combining `odd pair-codegree feedback`, `parity of three
pair-codegrees`, `W_2,3^T W_2,3 dynamics`, and `I+A(J(n,3)) functional graph`
did not locate a paper phrased as this literal iteration.  That non-hit is
recorded only as a search result; it is **not** a novelty or ownership claim.

## 4. Internal P1--P171 firewall

| comparison | literal/mechanism distinction | gate result |
|---|---|---|
| P125, conditional quadratic-state shear | P125 is nonlinear on pairs in a nonsingular binary quadratic space, uses a polar-bit quotient and Witt-sensitive counting, has $0/1/2$ fibres, and supports periods up to four.  It is not an incidence Gram projection. | `NO_LITERAL_COLLISION`; generic finite-quotient and fibre language receives zero separation credit. |
| P127, odd-outdegree transpose dynamics | P127 is transpose plus a recomputed rank-at-most-one parity-margin correction on looped digraph matrices.  Its recurrent even-parity hyperplane, periods $1,2,4$, and $0/1/(2^{n-1}+1)$ fibres do not follow from the H03 cycle space. | `NO_LITERAL_COLLISION`; both use binary margins, but neither theorem transfers directly. |
| P171, Boolean Gram feedback | P171 uses Boolean-semiring $AA^{\mathsf T}$, then graph Boolean powers and distance closure; its inverse axis is ordered clique covers with inclusion--exclusion.  H03 uses field addition and cancellation. | `NO_LITERAL_COLLISION`; Gram vocabulary alone is superficial, but P171 removes any credit for merely presenting another Gram map. |
| Current odd-degree Seidel-switch feedback | On graph edge space, $\Psi=I+B^{\mathsf T}B$ with $B$ vertex--edge incidence.  Its proof also pushes to a boundary parity vector, evaluates an incidence product, and obtains an odd/even projection/involution law with uniform unmarked fibres. | `SAME_PROOF_SILHOUETTE / PORTFOLIO_COLLISION`.  The maps are not conjugate (the even dynamics differ), but the chain-level incidence--Gram engine transfers. |

The current Seidel-switch candidate has the stronger residual: its switching
set is selected autonomously from the current degree signature, and for every
odd-order Eulerian target it has a target-sensitive edge-count polynomial
over predecessor cuts.  H03 has only a uniform boundary-lift multiplicity,
while its central time and rank laws have a direct Johnson owner.

## 5. At-most-one decision

Between the two same-silhouette candidates, retain the odd-degree
Seidel-switch feedback for further hostile review and kill H03/OCF now:

```text
H03/OCF = KILL_DIRECT_OWNER_AND_INTERNAL_SILHOUETTE
root parity switch = GREEN_OWNER_THIN (unchanged; not an ownership clearance)
```

This decision does not assert novelty for the retained candidate.  A direct
owner for its degree-selected feedback plus marked every-target inverse law
still kills it.

