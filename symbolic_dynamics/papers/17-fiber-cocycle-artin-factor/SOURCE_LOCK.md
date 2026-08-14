# SOURCE LOCK — SD-C19

**Title:** *Genuine Fiber Symmetry after Relabeling Failure: Artin Character
Factors of the Tensor-Atom Shift*
**Freeze date:** 2026-08-14
**Primary family:** Symbolic Dynamics
**Status:** frozen construction-plus-obstruction candidate

## 1. Arithmetic source and symbolic grammar

Let

\[
\mathcal M=\{F_n:n\ge 1\},\qquad
F_m\otimes F_n=F_{mn},\qquad h(F_n)=\log n.
\]

The tensor-indecomposable objects are \(F_p\).  For a finite atom set \(P\),
let

\[
E_P=\{S:\varnothing\ne S\subseteq P\},\qquad X_P=E_P^{\mathbb Z},
\]

with the full shift \(\sigma\).  Attach commuting variables \(x_p\) and put

\[
x_S=\prod_{p\in S}x_p,\qquad
\varepsilon(S)=(-1)^{|S|+1},\qquad w(S)=\varepsilon(S)x_S.
\]

Arithmetic specialization means \(x_p=p^{-s}\), with symbolic roof
\(T(S)=\sum_{p\in S}\log p\).  The exact construction is first defined over
the free commutative polynomial ring.  No target zeros, prime-indexed cocycle
values, von Mangoldt table, or fitted parameter enters the definition.

## 2. Genuine commuting fiber

Write \(C_2=\{0,1\}\) additively and freeze

\[
\alpha_P(S)=|S|\pmod 2,
\qquad
\sigma_\alpha(x,g)=(\sigma x,g+\alpha_P(x_0)).
\]

Deck translations \(R_h(x,g)=(x,g+h)\) commute with \(\sigma_\alpha\) for every
roof assignment.  They do not relabel atoms, variables, or arithmetic roofs.
The cocycle is intrinsic subset degree modulo two.

For every nonempty finite \(P\), singleton symbols switch the fiber and hence
the extension is topologically transitive.  If \(|P|\ge2\), even-cardinality
symbols also give fiber-preserving loops, so the extension is mixing.  The
one-atom system is transitive of period two.

## 3. Transfer and determinant convention

Let \(a\) be the nonidentity element and \(L_a\) left translation on
\(\mathbb C[C_2]\).  Define

\[
B_{\rm reg,P}(x)=
\sum_{\varnothing\ne S\subseteq P}\varepsilon(S)x_S L_a^{|S|},
\qquad
D_{\rm reg,P}(x)=\det(I-B_{\rm reg,P}(x)).
\]

For \(\chi_+(a)=1\) and \(\chi_-(a)=-1\), the isotypic blocks are

\[
B_{\chi,P}(x)=\sum_S\varepsilon(S)x_S\chi(a)^{|S|},
\qquad D_{\chi,P}(x)=1-B_{\chi,P}(x).
\]

The frozen normalization is \(z=1\) in \(\det(I-zB)\).  Off shell,

\[
D_\chi(z)=1-z+z\prod_{p\in P}(1-\chi(a)x_p),
\]

which is not generally an atomwise Euler product.  No off-shell factorization
is claimed.

The determinant convention is always \(D=\det(I-B)\).  Literature using a
dynamical Artin \(L\)-function may instead write \(L_\chi=D_\chi^{-1}\).
These are dynamical character factors, not number-field Artin \(L\)-functions.

## 4. Whole-object boundary

The exact identities are

\[
D_+=\prod_{p\in P}(1-x_p),\qquad
D_-=\prod_{p\in P}(1+x_p),\qquad
D_{\rm reg}=D_+D_-=\prod_{p\in P}(1-x_p^2).
\]

Only \(D_{\rm reg}\) is the determinant of the whole regular extension.
The factors \(D_+\) and \(D_-\) are isotypic block determinants of the same
operator.  A divisor visible in one meromorphically continued block need not
survive multiplication by the other block.

For \(\Re s>1\),

\[
D_+(s)=\zeta(s)^{-1},\qquad
D_-(s)=\frac{\zeta(s)}{\zeta(2s)},\qquad
D_{\rm reg}(s)=\zeta(2s)^{-1}.
\]

## 5. Countable convergence boundary

For \(\sigma=\Re s>1\),

\[
\sum_{\varnothing\ne S\subset_{\rm fin}\mathbb P}|x_S|
=\prod_p(1+p^{-\sigma})-1<\infty.
\]

Thus the finite-fiber adjacency series converges in operator norm, locally
uniformly on \(\Re s>1\), and defines a holomorphic matrix family.  This paper
does not claim nuclearity for an independently defined Ruelle operator on a
larger countable-shift Banach space.  Meromorphic identities inherited from
the Euler products are not promoted to a new Fredholm continuation theorem.

## 6. Primitive and mixed-factor terminology

For a primitive base necklace \(\gamma=[S_0\ldots S_{r-1}]\), set

\[
c(\gamma)=\sum_{i=0}^{r-1}|S_i|.
\]

In the \(C_m\) degree extension, the lift closes after

\[
q(\gamma)=\frac{m}{\gcd(m,c(\gamma))}
\]

base traversals and splits into \(\gcd(m,c(\gamma))\) primitive lifted cycles.
Base necklaces, immediate closures, and lifted cycles are distinct counts.

“No mixed local Euler factor” means that the determinant is a product of
atom-indexed factors.  It does **not** mean that expanded coefficients lack
composite monomials or that mixed base/lifted primitive cycles disappear.

## 7. Theorem scope and firewalls

The rigidity theorem assumes all of the following:

1. a one-letter cocycle \(\alpha_P:E_P\to G\);
2. naturality under all atom bijections with no action on the fixed group;
3. compatibility under inclusions/restrictions;
4. an operator-coherent atom-local matrix identity in a faithful
   representation.

Under these hypotheses \(\alpha_P(S)=a^{|S|}\), so the image is cyclic; a
transitive full \(G\)-extension forces \(G\) to be cyclic.  The theorem does
not cover transition-dependent cocycles \(\alpha(S,T)\), higher-memory rules,
or determinant-only coincidences in one selected higher-dimensional block.

## 8. Data and scope firewall

```yaml
candidate_id: SD-C19
frozen_group: C2
frozen_cocycle: alpha(S)=cardinality(S) mod 2
frozen_normalization: z=1
frozen_clock: sum of tensor-atom entropies
free_fitted_parameters: none
training_data: none
target_zero_data: forbidden_and_unused
primary_system_family: Symbolic Dynamics
route_b_invocation_allowed: false
```

Geometric covers, quantum graphs, Hamiltonians, scattering systems, and
self-adjoint carriers are outside Session 4.  They may appear only as
`ROUND2_CLUE` items.

## 9. Frozen route decision

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FAIL)

ROUTE_A_REJECTED
STOP_SCOPED / PROVES_TOO_MUCH
ROUTE_B_LOCKED
```

The A3 credit is limited to the exact same-object Artin block structure and
the holomorphic determinant in its honest domain.  It does not borrow credit
from an external continuation theorem, functional equation, or completed
divisor.
