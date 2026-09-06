# What is proved, and what is not

These are author-side adapter deductions used only to avoid counting an old
mechanism twice. They are not independently accepted paper theorems, and no
finite experiment was performed in this desk.

## 1. Transposing the old permanent gradient

Fix a prime $p$ and $r\geq2$. On $M_r(\mathbb F_p)$ define

$$
G(A)_{ij}=\operatorname{per}(A_{\widehat i,\widehat j}),
\qquad S(A)=A^{\mathsf T},\qquad T=S\circ G.
$$

Here $G$ is exactly the untransposed PCG literal in sources H2–H3.
Permanent is invariant under transpose: transposing a permutation summand
reindexes it by the inverse permutation. Hence, for each $i,j$,

$$
G(A^{\mathsf T})_{ij}
=\operatorname{per}\bigl((A_{\widehat j,\widehat i})^{\mathsf T}\bigr)
=G(A)_{ji}.
$$

Thus $GS=SG$. Since $S^2$ is the identity, composition gives

$$
T^2=SGSG=S^2G^2=G^2,
\qquad T^{2k}=G^{2k}\quad(k\geq0).
$$

For every target $B$ there is also an equality of actual source sets,

$$
\{A:T(A)=B\}=\{A:G(A)=B^{\mathsf T}\}.
$$

This last identity merely relabels the target of the old inverse problem;
it does **not** evaluate that problem. Odd-time orbits can differ, so neither
one-step equality nor conjugacy of $T$ and $G$ is asserted. No complete
all-parameter odd-time classification or newly evaluated inverse is supplied.
The conjunction required for a fresh paper is therefore not established.

## 2. Affine Hessian and its old projective factor

Let $V=\operatorname{Sym}^4(\mathbb F_q^2)$, represented as homogeneous binary
quartic coefficient vectors. Set $H(f)=\det\operatorname{Hess}(f)$, with
ordinary formal derivatives. Each second derivative is a binary quadratic,
so $H(f)$ is again a binary quartic. Each Hessian entry scales by $c$ under
$f\mapsto cf$; its two-by-two determinant therefore satisfies

$$
H(cf)=c^2H(f),\qquad H(0)=0.
$$

Let $Q=\{0\}\sqcup\mathbb P(V)$ and set $\pi(0)=0$, $\pi(f)=[f]$ for
$f\ne0$. Define $\overline H([f])=[H(f)]$ when $H(f)\ne0$, and $0$
otherwise, with $\overline H(0)=0$. The scaling identity makes this
well-defined in every characteristic and gives

$$
\pi\circ H=\overline H\circ\pi.
$$

This is a factor statement, not a bijection between affine and projective
carriers. H10 already records $\overline H$; H9 explicitly considered the
affine lift $H$, and H4 excludes it at intake. The scalar lift can in principle
alter orbit data, but no new uniform scalar-lift classification or evaluated
affine fibres were supplied in this desk. A factor alone is neither a full
temporal theorem nor a proof that such a theorem is impossible.

## 3. Remaining comparison boundaries

D1 and D5 have exact prior definitions; their old unfinished temporal axes
are not repaired here. D2 changes the cubic/carrier and D6 changes the parse
output, so their resemblance to an old primitive does not prove equality,
conjugacy, temporal transfer or an inverse formula. They were not fixed as
new total maps and remain undeclared probes.

For every comparison group the admission predicate

$$
\text{new residual all-parameter temporal theorem}
\quad\land\quad
\text{materially separate evaluated inverse/fibre/extremum theorem}
$$

is **NOT_CURRENTLY_JUSTIFIED**. This is an evidence boundary, not a universal
mathematical impossibility result. No bounded orbit table, observed period,
or historical kill label has been promoted to an all-parameter proof.
