# Proof Package — SD-C27

**Candidate:** SD-C27  
**Proof status:** complete for the frozen affine holomorphic model  
**Primary family:** Symbolic Dynamics  
**External analytic inputs:** nuclear trace formula for compactly contained
holomorphic map-weight systems; standard trace-class Fredholm determinant
identities  
**Route verdict:** `ROUTE_A_REJECTED`; Route B locked

## 0. Notation and proof firewall

Let \(\phi(z)=a+qz\) map \(\mathbb D\) compactly into itself, with
\(0<|q|<1\), and set

\[
 U_{\phi,0}f=f\circ\phi,
 \qquad
 U_{\phi,1}(g\,dz)=q(g\circ\phi)\,dz.
\]

Write \(\operatorname{Str}T^r=\operatorname{Tr}(T^0)^r-
\operatorname{Tr}(T^1)^r\).  The finite complex

\[
 0\to\mathbb C\to P_N\xrightarrow dP_{N-1}dz\to0
\]

provides an exact algebraic proof.  The infinite Bergman identity is proved
independently by the nuclear fixed-word trace formula; no bounded infinite
differential is assumed.

## 1. Local ordinary trace

### Lemma 1.1 — affine fixed-point trace

For \(W_0=wU_{\phi,0}\) and every \(r\ge1\),

\[
 \operatorname{Tr}W_0^r=\frac{w^r}{1-q^r}.
\]

**Proof.**  The iterate \(\phi^r\) has derivative \(q^r\) and one fixed
point.  The holomorphic fixed-point trace formula gives the result.  After
centering the fixed point, monomials have eigenvalues
\(1,q,q^2,\ldots\), so the same trace is the geometric series
\(w^r\sum_{m\ge0}q^{rm}\).  On \(P_N\) it is the finite sum through
\(m=N\).  Translation changes only upper-triangular entries. \(\square\)

### Corollary 1.2 — local zero-form determinant

\[
 \det(I-zW_0)=\prod_{m\ge0}(1-zwq^m).
\]

Thus an ordinary holomorphic composition determinant is a
\(q\)-Pochhammer factor, not \(1-zw\).

## 2. Scalar and ordinary-tensor rigidity

### Proposition 2.1 — scalar all-power rigidity

No scalar \(\alpha(q)\) can satisfy

\[
 \operatorname{Tr}(\alpha(q)wU_{\phi,0})^r=w^r
 \quad\text{for every }r\ge1
\]

unless \(q=0\) (or the excluded noncontraction \(q=1\)).

**Proof.**  The first power forces \(\alpha=1-q\).  The second then requires

\[
 \frac{(1-q)^2}{1-q^2}=1,
\]

or \(2q(q-1)=0\).  Under \(|q|<1\), only \(q=0\) remains.
\(\square\)

The normalized second-power residual is

\[
 \frac{(1-q)^2}{1-q^2}-1=-\frac{2q}{1+q}.
\]

At \(q=0\), composition is evaluation at the fixed point followed by
inclusion of constants: the branch is rank one and determinant-equivalent to
an atom loop.

### Theorem 2.2 — ordinary trace-class tensor obstruction

Let \(B\) be a finite matrix or trace-class operator.  For
\(0<|q|<1\), the tensor operator

\[
 T=w(B\otimes U_{\phi,0})
\]

cannot satisfy \(\operatorname{Tr}T^r=w^r\) for every \(r\ge1\).

**Proof.**  Trace factorization would require
\(\operatorname{Tr}B^r=1-q^r\) for every \(r\).  Near the origin, the
trace-class determinant formula then forces

\[
 \det(I-tB)
 =\exp\!\left(-\sum_{r\ge1}\frac{1-q^r}{r}t^r\right)
 =\frac{1-t}{1-qt}.
\]

The Fredholm determinant of a trace-class operator is entire in \(t\), but
the final expression has a genuine pole at \(t=q^{-1}\).  This is a
contradiction. \(\square\)

The theorem is scoped to ordinary tensor fibers.  It does not exclude every
nontensor nuclear construction.

## 3. Canonical de Rham escape

### Theorem 3.1 — local all-order Lefschetz cancellation

Let

\[
 W_0=wU_{\phi,0},\qquad W_1=wU_{\phi,1}.
\]

Then for every \(r\ge1\),

\[
 \operatorname{Tr}W_0^r-\operatorname{Tr}W_1^r=w^r,
\]

and

\[
 \det(I-zW_0)=(1-zw)\det(I-zW_1).
\]

**Trace proof.**  Since \(U_{\phi,1}=qU_{\phi,0}\), Lemma 1.1 gives

\[
 \operatorname{Tr}W_1^r=\frac{w^rq^r}{1-q^r}.
\]

Subtracting gives \(w^r\); exponentiating the full trace logarithm yields
the determinant identity. \(\square\)

**Finite-complex proof.**  Affine pullback preserves
\(P_N\xrightarrow dP_{N-1}dz\), whose kernel is the constants and whose
positive-degree quotient is intertwined with the one-form action.  The
induced map on constants is multiplication by \(w\), so

\[
 \det(I-zwU_{\phi,0}|P_N)
 =(1-zw)\det(I-zwU_{\phi,1}|P_{N-1}dz)
\]

for every \(N\). \(\square\)

**Centered spectral proof.**  The two degreewise determinants are

\[
 D_0(z)=\prod_{m\ge0}(1-zwq^m),\qquad
 D_1(z)=\prod_{m\ge0}(1-zwq^{m+1}),
\]

and their ratio telescopes to \(1-zw\). \(\square\)

### Proposition 3.2 — determinant ownership

The conclusion of Theorem 3.1 is a graded ratio

\[
 \frac{\det(I-zW_0)}{\det(I-zW_1)}=1-zw
\]

where the denominator is nonzero.  The ordinary block determinant instead
equals

\[
 \det(I-z(W_0\oplus W_1))
 =\det(I-zW_0)\det(I-zW_1).
\]

The two objects are unequal except in degenerate cases.

## 4. Shared renewal

Let \(\{(w_j,\phi_j)\}_{j\in J}\) be finite, or countable with absolute
weight summability and common compact containment, and define

\[
 L_k=\sum_{j\in J}w_jU_{\phi_j,k},\qquad
 S_w=\sum_{j\in J}w_j.
\]

### Theorem 4.1 — shared cohomology collapse

For every \(r\ge1\),

\[
 \operatorname{Str}L^r=S_w^r,
\]

and

\[
 \det(I-zL_0)=(1-zS_w)\det(I-zL_1).
\]

**Proof.**  Expand each power over ordered words
\(\alpha=(j_1,\ldots,j_r)\).  The composite affine branch has derivative
\(q_\alpha=\prod_mq_{j_m}\).  The degree-zero word trace is its weight
divided by \(1-q_\alpha\); the degree-one word trace has the additional
factor \(q_\alpha\).  Their difference is exactly
\(\prod_mw_{j_m}\).  Absolute convergence permits summation, giving

\[
 \sum_{\alpha\in J^r}\prod_mw_{j_m}=S_w^r.
\]

The trace logarithm gives the determinant identity near zero, hence
everywhere by the identity theorem for the entire degreewise determinants.
\(\square\)

On the finite polynomial complex, the same result follows because constants
carry multiplication by \(S_w\) and the nonconstant quotient is similar to
the one-form action.

### Corollary 4.2 — mixed necklaces survive

For two weights \(x,y\),

\[
 \operatorname{Str}L^2=x^2+2xy+y^2.
\]

The desired disjoint ledger has \(x^2+y^2\).  Equivalently,

\[
 -\log(1-z(x+y))+\log((1-zx)(1-zy))
 =z^2xy+z^3(x^2y+xy^2)+O(z^4).
\]

The coefficients are the mixed primitive necklaces \([xy]\), \([xxy]\),
and \([xyy]\).  Exterior grading cancels local tangent stability for every
word; it supplies no test for whether a word uses one label or several.

For a constrained branch graph, the same fixed-word proof leaves precisely
the legal graph cycles on degree-zero cohomology.

## 5. Disjoint assembly

For an inventory \(S\), set

\[
 \mathcal E^k_{S,s}=\bigoplus_{n\in S}n^{-s}U_{\phi_n,k}.
\]

### Theorem 5.1 — disjoint atom-loop collapse

For \(\Re s>1\),

\[
 \det(I-z\mathcal E^0_{S,s})
 =\prod_{n\in S}(1-zn^{-s})
   \det(I-z\mathcal E^1_{S,s}),
\]

and therefore

\[
 D_{\mathrm{gr}}(s,z)=\prod_{n\in S}(1-zn^{-s}).
\]

**Proof.**  The uniform trace-norm bound on the compactly contained branch
operators and \(\sum_n|n^{-s}|<\infty\) make the degreewise direct sums
trace class.  Apply Theorem 3.1 componentwise and multiply the absolutely
convergent factors. \(\square\)

### Corollary 5.2 — cohomological equivalence to atom loops

Each disk complex has one surviving constant class.  The direct-sum
cohomology is

\[
 \bigoplus_{n\in S}\mathbb C,
\]

and its induced operator is \(\operatorname{diag}(n^{-s})\).  All
nonconstant analytic modes cancel.  Hence the graded determinant is exactly
the ordinary Fredholm determinant of one diagonal atom loop per supplied
label.  The same statement holds for primes, squares, Fibonacci numbers,
seeded random sets, hashes, and arbitrary decidable inventories.

## 6. Analytic and marker ceilings

### Corollary 6.1 — no trace-class half-plane gain

For \(S=\mathbb P\), the surviving cohomology operator has eigenvalues
\(p^{-s}\).  It is trace class exactly where
\(\sum_pp^{-\Re s}<\infty\), namely \(\Re s>1\).  Removing the constant
modes makes the graded determinant one; retaining them prevents a
trace-class extension through \(\Re s=1\).  Equivalent renorming cannot
change these eigenvalues.

### Corollary 6.2 — digit marker persistence

If \(u\) marks the binary digit steps, replace \(n^{-s}\) by
\(u^{\ell(n)}n^{-s}\) in every preceding identity.  The shared and disjoint
graded determinants become

\[
 1-\sum_{n\in S}u^{\ell(n)}n^{-s},
 \qquad
 \prod_{n\in S}(1-u^{\ell(n)}n^{-s}).
\]

The variable \(z\) assigns one mark per completed code only after inducing
or taking whole codewords as countable return symbols.  Exterior
cancellation does not cancel symbolic duration.

## 7. Route theorem

### Theorem 7.1 — exact escape-and-collapse classification

For the frozen logarithmic-code affine family:

1. scalar normalization and ordinary trace-class tensor fibers fail to
   remove the stability denominator at all repetitions unless the branch is
   rank one;
2. the canonical de Rham grading removes it exactly at all repetitions;
3. a shared recurrent assembly retains all mixed primitive necklaces;
4. a disjoint assembly is determinant-equivalent to a supplied inventory of
   atom loops;
5. the original digit marker and the \(\Re s>1\) cohomology boundary remain.

Consequently the frozen tuple is

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)
```

The candidate is `ROUTE_A_REJECTED`; Route B remains locked.

**Proof.**  Combine Propositions 2.1 and 3.2, Theorems 2.2, 3.1, 4.1, and
5.1, and Corollaries 4.2, 5.2, 6.1, and 6.2. \(\square\)
