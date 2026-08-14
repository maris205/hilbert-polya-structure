# PROOF PACKAGE — SD-C19

## Status

**PROVABLE AS STATED**, with the one-letter, naturality, inclusion-compatibility,
and operator-coherence assumptions written explicitly below.  No proof is
claimed for transition-dependent cocycles or determinant-only coincidences in
a selected higher-dimensional representation.

## Assumptions and notation

- \(P\) is a finite set of tensor atoms and
  \(E_P=\{S:\varnothing\ne S\subseteq P\}\).
- \(x_p\) are commuting indeterminates,
  \(x_S=\prod_{p\in S}x_p\), and
  \(\varepsilon(S)=(-1)^{|S|+1}\).
- \(G\) is finite unless an infinite-group boundary is explicitly stated.
- \(L_g\) denotes left translation on \(\mathbb C[G]\).
- The determinant convention is \(D=\det(I-B)\) at the fixed temporal
  normalization \(z=1\).
- A family \(\alpha_P:E_P\to G\) is *relabeling-natural* when atom bijections
  leave the group labels invariant, and *inclusion-compatible* when restriction
  from a larger finite atom set preserves every existing label.

## Dependency map

1. Regular Artin factorization uses the decomposition of the finite left
   regular representation and finite inclusion–exclusion.
2. Degree-power factorization uses the expansion of a commuting matrix product.
3. One-letter rigidity compares squarefree coefficients in that matrix identity.
4. Genuine motion uses the periodic obstruction to a cocycle coboundary.
5. Primitive lifting uses the order and orbit count of a cyclic translation.
6. The Route-A obstruction combines primitive lifting with the arbitrary-variable
   nature of the factorization.

## Theorem 1 — finite-group same-object Artin decomposition

Let \(\alpha:E_P\to G\) be any one-letter cocycle and define

\[
B_{\rm reg}(x)=\sum_{S\in E_P}\varepsilon(S)x_S L_{\alpha(S)}.
\]

For each irreducible complex representation \(\rho\in\widehat G\), let

\[
B_\rho(x)=\sum_{S\in E_P}\varepsilon(S)x_S\rho(\alpha(S)),
\qquad D_\rho(x)=\det(I-B_\rho(x)).
\]

Then

\[
D_{\rm reg}(x)=\det(I-B_{\rm reg}(x))
=\prod_{\rho\in\widehat G}D_\rho(x)^{d_\rho},
\qquad d_\rho=\dim\rho.
\]

The trivial block is

\[
D_{\mathbf1}(x)=\prod_{p\in P}(1-x_p).
\]

### Proof

For \(h,g\in G\), left and right translations commute.  Hence every linear
combination of the \(L_g\), including \(B_{\rm reg}\), preserves the right
regular isotypic decomposition.  The finite regular representation decomposes
as a direct sum of \(d_\rho\) copies of each irreducible \(\rho\).  Restricting
\(I-B_{\rm reg}\) to these summands and multiplying determinants gives the
displayed product.

For the trivial representation, every group label maps to one, so

\[
D_{\mathbf1}=1-\sum_{\varnothing\ne S\subseteq P}
(-1)^{|S|+1}x_S.
\]

Expanding \(\prod_{p\in P}(1-x_p)\) shows that its nonconstant coefficient on
\(x_S\) is \((-1)^{|S|}\), exactly the coefficient above after subtraction.
This proves the second identity. \(\square\)

## Theorem 2 — degree-power character factorization

Fix \(a\in G\) and let \(\alpha(S)=a^{|S|}\).  For a representation \(\rho\),
write \(A=\rho(a)\).  Then

\[
I-B_\rho(x)=\prod_{p\in P}(I-x_pA),
\qquad
D_\rho(x)=\prod_{p\in P}\det(I-x_pA).
\]

### Proof

All factors \(I-x_pA\) commute because they are polynomials in the same
matrix \(A\).  Expanding the product yields

\[
\prod_{p\in P}(I-x_pA)
=I+\sum_{k\ge1}(-1)^k e_k(x)A^k,
\]

where \(e_k(x)=\sum_{|S|=k}x_S\).  On the other hand,

\[
B_\rho(x)=\sum_{k\ge1}(-1)^{k+1}e_k(x)A^k.
\]

Subtracting from \(I\) proves the matrix identity.  Determinants are
multiplicative for finite matrices, proving the factorization. \(\square\)

## Corollary 3 — the primary \(C_2\) identities

For \(C_2=\langle a\rangle\), with characters
\(\chi_+(a)=1\) and \(\chi_-(a)=-1\),

\[
D_+(x)=\prod_p(1-x_p),\qquad
D_-(x)=\prod_p(1+x_p),\qquad
D_{\rm reg}(x)=\prod_p(1-x_p^2).
\]

At \(x_p=p^{-s}\), \(\Re s>1\),

\[
D_+(s)=\zeta(s)^{-1},\qquad
D_-(s)=\frac{\zeta(s)}{\zeta(2s)},\qquad
D_{\rm reg}(s)=\zeta(2s)^{-1}.
\]

### Proof

The first two identities are Theorem 2 with \(A=1\) and \(A=-1\).  The
regular representation is their direct sum, so Theorem 1 gives the product.
The local equality \((1-x)(1+x)=1-x^2\) gives the last polynomial formula.
For \(\Re s>1\), absolute convergence permits termwise Euler multiplication,
and \(1+p^{-s}=(1-p^{-2s})/(1-p^{-s})\). \(\square\)

## Corollary 4 — \(C_m\) character and regular factors

Let \(C_m=\langle a\rangle\), \(\omega=e^{2\pi i/m}\), and
\(\chi_j(a)=\omega^j\).  Then

\[
D_j(x)=\prod_p(1-\omega^j x_p),
\qquad
D_{\rm reg}(x)=\prod_p(1-x_p^m).
\]

### Proof

The character formula is Theorem 2.  Multiplying over all characters and using
\(\prod_{j=0}^{m-1}(1-\omega^j x)=1-x^m\) proves the regular formula. \(\square\)

## Theorem 5 — natural one-letter no-leak rigidity

Suppose \(\alpha_P:E_P\to G\) is relabeling-natural and
inclusion-compatible.  Then there are elements \(g_k\in G\), independent of
the ambient atom set, such that

\[
\alpha_P(S)=g_{|S|}.
\]

Let \(\rho\) be a representation, set \(A=\rho(g_1)\), and assume the
operator-coherent identity

\[
I-\sum_{S\in E_P}\varepsilon(S)x_S\rho(g_{|S|})
=\prod_{p\in P}(I-x_pA)
\tag{*}
\]

for every finite \(P\).  Then \(\rho(g_k)=A^k\) for every \(k\).  If \(\rho\)
is faithful, then \(g_k=g_1^k\).  Consequently the cocycle image lies in
\(\langle g_1\rangle\); if the skew extension is transitive on the entire fiber
\(G\), then \(G=\langle g_1\rangle\) and \(G\) is cyclic.

### Proof

The symmetric group of a finite atom set acts transitively on its \(k\)-element
subsets.  Naturality therefore assigns the same group element to all such
subsets.  Inclusion compatibility identifies this element in every larger
ambient set, producing \(g_k\).

Fix \(k\) and take \(|P|\ge k\).  The coefficient of any squarefree monomial
\(x_S\) with \(|S|=k\) on the left of (*) is
\((-1)^k\rho(g_k)\).  The coefficient on the right is \((-1)^kA^k\).
Polynomial equality gives \(\rho(g_k)=A^k\).  If \(\rho\) is faithful, this
matrix equality implies \(g_k=g_1^k\).

Every periodic fiber displacement is then a power of \(g_1\), so the state
graph of the skew extension decomposes into right cosets of
\(\langle g_1\rangle\).  Strong connectivity on all of \(G\) is possible only
when there is one coset, which means \(G=\langle g_1\rangle\). \(\square\)

### Boundary of Theorem 5

The premise is a matrix-polynomial identity, not equality of one determinant
in a selected higher-dimensional representation.  Such determinant equality
can hide spectral coincidences.  For a one-dimensional character the matrix is
scalar, and the first failed degree \(k\) has discrepancy

\[
(-1)^k\bigl(\chi(g_k)-\chi(g_1)^k\bigr)e_k(x).
\]

The theorem also says nothing about \(\alpha(S,T)\) or higher-memory cocycles.

## Proposition 6 — genuine motion and the coboundary firewall

If \(a\ne e\), the degree-power cocycle is not cohomologous to the identity
cocycle on the full subset shift.

### Proof

The bi-infinite word that repeats a singleton symbol is a period-one point.
Its cocycle product is \(a\).  For a multiplicative coboundary
\(\alpha(x)=b(\sigma x)b(x)^{-1}\), the product around every periodic orbit
telescopes to the identity.  Since \(a\ne e\), the cocycle is not a
coboundary. \(\square\)

## Theorem 7 — primitive lift formula and mismatch

Let \(\gamma=[S_0\ldots S_{r-1}]\) be primitive in the base shift and let
\(c=\sum_i|S_i|\).  In the \(C_m\) degree extension, the preimage of \(\gamma\)
contains

\[
\gcd(m,c)
\]

primitive lifted cycles.  Each has period

\[
r\,\frac{m}{\gcd(m,c)}.
\]

### Proof

After one traversal of \(\gamma\), the fiber return map is translation by
\(c\) in \(\mathbb Z/m\mathbb Z\).  Its order is
\(q=m/\gcd(m,c)\).  Therefore each fiber point returns after exactly \(q\)
base traversals, and the translation partitions the \(m\) fiber points into
\(m/q=\gcd(m,c)\) orbits.

If a lifted orbit had smaller period, its projection would return to the same
point of the primitive base orbit in fewer than a multiple of \(r\), or the
fiber translation would close in fewer than \(q\) traversals.  Both alternatives
contradict minimality.  Hence every counted lift is primitive and has period
\(rq\). \(\square\)

For a singleton, \(c=1\), so its period is multiplied by \(m\).  A mixed
subset of cardinality divisible by \(m\) closes after one traversal.  Thus the
regular extension has no prime-singleton primitive ledger at the original
clock, even though its character determinants are atom-local.

## Proposition 8 — universality and zero selectivity

The factorizations in Theorem 2 are identities in a commutative polynomial
ring and therefore survive every substitution of the variables for which the
expressions are defined.  Composite, shuffled, and random inventories cannot
separate from the prime inventory on the binary metric “does the identity
hold?”  The identity pass-rate margin is exactly zero.

### Proof

A ring identity is preserved by every ring homomorphism.  Substituting any
finite rational or complex inventory is such a homomorphism. \(\square\)

## Corrections or missing assumptions

- Theorem 5 requires operator-coherent equality.  Replacing it by a determinant
  identity in one selected higher-dimensional block would make the original
  conclusion unjustified.
- Countable specialization is asserted only where the finite-fiber series is
  absolutely norm-convergent, namely \(\Re s>1\).
- No orbitwise interpretation is inferred from the cancellation of a completed
  trace-log series.

## Open risks

- Transition-dependent incidence cocycles remain outside the theorem and form
  the next symbolic loophole.
- The finite-fiber determinant has no supplied self-adjoint or scattering
  carrier.
- Meromorphic continuation through the zeta identities is not an intrinsic
  transfer-operator continuation theorem.
