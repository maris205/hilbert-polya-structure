# Derivation Package — SD-C27

**Invariant object:** the full cyclic supertrace, equivalently the connected
graded trace logarithm

\[
 -\log D_{\mathrm{gr}}(s,z)
 =\sum_{r\ge1}\frac{z^r}{r}\operatorname{Str}L_s^r.
\]

**Derivation goal:** determine whether a holomorphic or anisotropic
function-space lift of a logarithmic arithmetic code can produce the desired
all-repetition Euler factor without degenerating to atom loops or changing
the symbolic object.

## 1. Assumption ledger

### Structural assumptions

1. Elias gamma coding fixes a prefix-free binary history \(c(n)\) of length
   \(\ell(n)=2\lfloor\log_2n\rfloor+1\).
2. The digit maps are
   \(\psi_0(z)=z/2-1/4\) and \(\psi_1(z)=z/2+1/4\).
3. Their code composition is affine with derivative
   \(q_n=2^{-\ell(n)}\).
4. Zero- and one-form pullbacks act on frozen Bergman spaces.
5. Weights are \(w_n(s)=n^{-s}\), and \(\Re s>1\) is the initial nuclear
   domain.

### Ownership assumptions

- `shared` means every label can follow every label on one disk;
- `disjoint` means one recurrent disk per supplied label;
- \(z\) counts completed returns;
- \(u\) counts binary digit edges;
- a quotient of degreewise determinants is graded/relative, never ordinary
  ungraded.

### Explicit nonassumptions

No bounded differential between the two infinite Bergman spaces is assumed.
No prime table is built into a local weight.  No target-zero data, analytic
continuation, functional equation, or self-adjoint operator is assumed.

## 2. Local scalar branch

For \(\phi(z)=a+qz\), the \(r\)-fold zero-form pullback has fixed-point
trace

\[
 \operatorname{Tr}(wU_{\phi,0})^r=\frac{w^r}{1-q^r}.
\]

The denominator is a repetition-dependent stability factor.  Multiplying
the one-step operator by a scalar \(\alpha(q)\) changes the numerator to
\(\alpha(q)^r\).  The first trace demands \(\alpha=1-q\), while the second
demands

\[
 (1-q)^2=1-q^2.
\]

Thus \(q=0\) or \(q=1\).  The contracting solution \(q=0\) is rank-one
evaluation, so scalar repair returns to the atom loop.

## 3. Ordinary tensor-fiber test

If \(T=w(B\otimes U_{\phi,0})\) is to have
\(\operatorname{Tr}T^r=w^r\) for all \(r\), then

\[
 \operatorname{Tr}B^r=1-q^r.
\]

The full moment sequence forces

\[
\begin{aligned}
 \det(I-tB)
 &=\exp\!\left(-\sum_{r\ge1}\frac{t^r}{r}
     \operatorname{Tr}B^r\right)\\
 &=\exp\!\left(-\sum_{r\ge1}\frac{t^r}{r}
     +\sum_{r\ge1}\frac{(qt)^r}{r}\right)\\
 &=\frac{1-t}{1-qt}.
\end{aligned}
\]

An ordinary trace-class determinant is entire in \(t\); the final ratio has
a pole at \(q^{-1}\) for \(0<|q|<1\).  Ordinary tensor fibers therefore
cannot supply the missing numerator.  The negative multiplicity suggested
by the ratio points directly to a graded sector.

## 4. Canonical exterior numerator

The pullback on one-forms contributes the derivative:

\[
 U_{\phi,1}=qU_{\phi,0}.
\]

At the \(r\)-th repetition,

\[
 \operatorname{Tr}(wU_{\phi,1})^r
 =\frac{w^rq^r}{1-q^r}.
\]

Hence

\[
 \operatorname{Str}W^r
 =\frac{w^r}{1-q^r}-\frac{w^rq^r}{1-q^r}
 =w^r.
\]

This is the one-dimensional exterior identity

\[
 \operatorname{tr}\Lambda^0(q^r)-
 \operatorname{tr}\Lambda^1(q^r)=1-q^r.
\]

It is canonical tangent functoriality, not a hand-chosen alternating scalar.
Summing over all repetitions yields

\[
 \det(I-zW_0)=(1-zw)\det(I-zW_1).
\]

For a centered branch, the same calculation telescopes the two ordinary
products:

\[
 \frac{\prod_{m\ge0}(1-zwq^m)}
      {\prod_{m\ge0}(1-zwq^{m+1})}=1-zw.
\]

The successful object is the quotient, not the product associated with the
ordinary block sum.

## 5. Exact finite complex

For \(\phi(z)=a+qz\), the zero-form pullback matrix on the monomial basis of
\(P_N\) is

\[
 (M_0)_{j,k}=\binom{k}{j}a^{k-j}q^j,
 \qquad 0\le j\le k\le N,
\]

and the one-form matrix on \(P_{N-1}dz\) is

\[
 (M_1)_{j,k}=q\binom{k}{j}a^{k-j}q^j,
 \qquad 0\le j\le k\le N-1.
\]

With \(D_{k-1,k}=k\), exact differentiation gives

\[
 DM_0=M_1D.
\]

The sequence

\[
 0\to\mathbb C\to P_N\xrightarrow dP_{N-1}dz\to0
\]

shows that all nonconstant modes pair and the constant mode survives.  Thus
for a single weighted branch

\[
 \det(I-zwM_0)=(1-zw)\det(I-zwM_1)
\]

as an exact polynomial identity for every \(N\).

## 6. Shared return algebra

Let

\[
 L_k=\sum_jw_jU_{\phi_j,k}.
\]

Expanding \(L_k^r\) gives one term for every ordered return word
\(\alpha=(j_1,\ldots,j_r)\).  If
\(q_\alpha=\prod_mq_{j_m}\) and
\(w_\alpha=\prod_mw_{j_m}\), then

\[
 \operatorname{Tr}U_{\alpha,0}=\frac1{1-q_\alpha},
 \qquad
 \operatorname{Tr}U_{\alpha,1}=\frac{q_\alpha}{1-q_\alpha}.
\]

The word supertrace is \(w_\alpha\), so

\[
 \operatorname{Str}L^r
 =\sum_{\alpha\in J^r}w_\alpha
 =\left(\sum_jw_j\right)^r.
\]

Consequently

\[
 D_{\mathrm{gr}}^{\mathrm{shared}}(z)
 =1-z\sum_jw_j.
\]

This factor is the symbolic determinant of a shared full renewal alphabet.
For two weights it contains the mixed contributions

\[
 z^2xy+z^3(x^2y+xy^2)+\cdots
\]

in the difference of connected logarithms from the disjoint comparator.
The grading cancels stability for every legal word, so it preserves rather
than selects the mixed branch combinatorics.

## 7. Disjoint return algebra

For

\[
 \mathcal E_k=\bigoplus_jw_jU_{\phi_j,k},
\]

componentwise cancellation gives

\[
 D_{\mathrm{gr}}^{\mathrm{disjoint}}(z)
 =\prod_j(1-zw_j).
\]

The surviving cohomology is one constant state per disk, and its operator is
\(\operatorname{diag}(w_j)\).  Therefore the analytic contraction, code
translation, and nonconstant modes are determinant-invisible after grading.
The result is identical to one atom loop per supplied label.

For \(w_j=n^{-s}\), choosing primes gives \(1/\zeta(s)\) in
\(\Re s>1\), but choosing any other inventory produces its corresponding
product by the same mechanism.  The construction proves analytic
factorization, not arithmetic selection.

## 8. Marker derivation

A completed codeword of length \(\ell(n)\) has digit-time monomial

\[
 u^{\ell(n)}n^{-s}.
\]

Replacing that monomial by \(zn^{-s}\) declares one completed return to be
one step.  Thus

\[
\begin{array}{c|c|c}
 & \text{shared} & \text{disjoint}\\
\hline
\text{digit time}
 & 1-\sum_nu^{\ell(n)}n^{-s}
 & \prod_n(1-u^{\ell(n)}n^{-s})\\
\text{return time}
 & 1-z\sum_nn^{-s}
 & \prod_n(1-zn^{-s})
\end{array}
\]

The exterior numerator acts on tangent stability and does not change either
symbolic exponent.

## 9. Nuclearity derivation

Common compact containment gives a uniform trace-norm bound for the
degreewise branch pullbacks.  Therefore

\[
 \sum_n|n^{-s}|<\infty
\]

is a sufficient trace-class majorant for both assemblies.  On prime-indexed
disjoint cohomology it is also necessary: the eigenvalues are \(p^{-s}\),
so trace class requires \(\sum_pp^{-\Re s}<\infty\), exactly
\(\Re s>1\).  The scalar meromorphic continuation of the quotient cannot
upgrade the degreewise operator family.

## 10. Logical output

### Exact identities

- affine fixed-point traces;
- scalar two-power rigidity;
- ordinary tensor entire-versus-pole obstruction;
- local de Rham supertrace and determinant quotient;
- shared power supertraces and mixed-word ledger;
- disjoint direct-product factorization;
- digit/return marker formulas;
- prime cohomology trace-class boundary.

### Interpretations supported by those identities

- holomorphic nuclearity is a real escape from SD-C26's scalar whole-operator
  obstruction;
- the escape is cohomological and not prime-selective;
- shared recurrence fails by mixed-word flooding;
- disjoint recurrence collapses to the supplied atom inventory.

### Conclusions not derived

- a universal no-go for all signed or anisotropic spaces;
- an intrinsic prime selector;
- critical-strip continuation of the same operators;
- a functional equation, Riemann divisor, or Hilbert–Pólya generator.
