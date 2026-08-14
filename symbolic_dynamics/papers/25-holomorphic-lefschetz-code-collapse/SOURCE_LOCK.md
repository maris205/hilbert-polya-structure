# Source Lock — SD-C27

**Freeze date:** 2026-08-14  
**Primary family:** Symbolic Dynamics  
**Authority object:** a self-delimiting binary integer code lifted to affine
holomorphic inverse branches, tested in shared-renewal and disjoint-component
assemblies  
**Target-zero data:** forbidden and unused  
**Route-B invocation:** forbidden  
**Review loop:** excluded by instruction

## 1. Arithmetic source boundary

Retain the full-shift semiring skeleton

\[
 F_m\boxtimes F_n\cong F_{mn},\qquad
 F_m\boxplus F_n\cong F_{m+n},\qquad
 S(F_n)\cong F_{n+1},\qquad h(F_n)=\log n.
\]

Rational primes are multiplicative atoms of this skeleton.  No Riemann-zero
data, prime table in a transfer weight, cutoff-dependent alphabet, or fitted
Euler coefficient is admissible.  Restricting a branch inventory to primes
must be displayed as a restriction and rerun on arbitrary inventories.

## 2. Frozen logarithmic code

For every integer \(n\ge1\), let \(c(n)\) be its Elias gamma code.  If

\[
 L(n)=\lfloor\log_2n\rfloor+1,
\]

then \(c(n)\) is \(L(n)-1\) zeros followed by the \(L(n)\)-digit binary
expansion of \(n\), and

\[
 \ell(n)=|c(n)|=2L(n)-1=O(\log n).
\]

The code is prefix-free and fixed before an inventory is selected.  Its role
is to test the logarithmic-code loophole from SD-C26, not to claim that gamma
coding itself selects primes.

## 3. Frozen holomorphic branches

On the unit disk \(\mathbb D\), define

\[
 \psi_0(z)=\frac z2-\frac14,
 \qquad
 \psi_1(z)=\frac z2+\frac14.
\]

For a word \(c=c_1\cdots c_\ell\), let \(\phi_c\) be its ordered affine
composition and put

\[
 \phi_n=\phi_{c(n)},\qquad
 q_n=\phi_n'=2^{-\ell(n)}.
\]

Every digit branch maps the closed unit disk into \(|z|\le3/4\); every
code branch therefore satisfies a common compact-containment condition.
Translations retain the word order, while \(q_n\) records its length.

## 4. Frozen function spaces and grading

Use the Bergman spaces

\[
 \mathcal H^0=A^2(\mathbb D),\qquad
 \mathcal H^1=A^2(\mathbb D)\,dz.
\]

For \(\phi(z)=a+qz\), the canonical pullbacks are

\[
 U_{\phi,0}f=f\circ\phi,
 \qquad
 U_{\phi,1}(g\,dz)=q(g\circ\phi)\,dz.
\]

They obey \(dU_{\phi,0}=U_{\phi,1}d\) on the natural dense domain.  Exact
finite algebra is tested on

\[
 0\longrightarrow\mathbb C\longrightarrow P_N
 \xrightarrow{d}P_{N-1}dz\longrightarrow0.
\]

The finite exact complex and the infinite Bergman pair are distinct proof
devices: the differential is not asserted bounded between the two infinite
Bergman spaces.

## 5. Two assemblies

Let \(S\subseteq\{2,3,\ldots\}\) be an inventory and
\(w_n(s)=n^{-s}\).

### Shared renewal

All completed code returns act on one disk:

\[
 \mathcal L^k_{S,s}=\sum_{n\in S}w_n(s)U_{\phi_n,k},
 \qquad k=0,1.
\]

After any return every other return is legal.  This is the countable full
shift on return labels, so mixed primitive necklaces are part of the frozen
object.

### Disjoint components

Each completed code return acts on a private disk:

\[
 \mathcal E^k_{S,s}=\bigoplus_{n\in S}
 w_n(s)U_{\phi_n,k}.
\]

The disjoint architecture forbids mixed words by separating recurrent
components.  The component index is the supplied inventory and is subject to
the arbitrary-inventory control.

## 6. Determinant ownership firewall

Whenever the ordinary Fredholm determinants exist, define

\[
 D_{\mathrm{gr}}(z)
 =\frac{\det(I-zL^0)}{\det(I-zL^1)}
 =\exp\!\left[-\sum_{r\ge1}\frac{z^r}{r}
 \bigl(\operatorname{Tr}(L^0)^r-\operatorname{Tr}(L^1)^r\bigr)\right].
\]

This is a graded or relative determinant: a ratio of two separately honest
ordinary Fredholm determinants.  It is not the ordinary determinant of the
ungraded block sum, which is

\[
 \det(I-z(L^0\oplus L^1))
 =\det(I-zL^0)\det(I-zL^1).
\]

No statement may call the graded ratio an ordinary block determinant.

## 7. Marker ownership firewall

The variable \(z\) counts completed code returns.  It does not count the
binary digit edges in \(c(n)\).  If \(u\) counts original digit steps, then
the branch coefficient is

\[
 \widetilde w_n(s,u)=u^{\ell(n)}n^{-s}.
\]

Thus the digit-time shared and disjoint graded determinants are

\[
 1-\sum_{n\in S}u^{\ell(n)}n^{-s},
 \qquad
 \prod_{n\in S}\bigl(1-u^{\ell(n)}n^{-s}\bigr).
\]

Replacing these by one \(z\) per codeword is first-return induction, or a
declaration that whole codewords form a countable return alphabet.  It is a
change of marker/object, not an identity at the original digit scale.

## 8. Analytic domain

For \(\Re s>1\),

\[
 \sum_{n\in S}|n^{-s}|<\infty.
\]

Common compact containment and the holomorphic map-weight theorem give
trace-class shared operators; the same uniform trace-norm estimate gives
trace-class disjoint sums.  For \(S=\mathbb P\), the degree-zero cohomology
modes have eigenvalues \(p^{-s}\), whose absolute sum diverges for
\(\Re s\le1\).  Analytic continuation of \(1/\zeta(s)\) is not continuation
of this trace-class family.

## 9. Allowed conclusions and excluded universality

The frozen theorem class permits:

- scalar normalizations of one holomorphic composition branch;
- ordinary finite-dimensional or trace-class tensor fibers;
- the canonical holomorphic de Rham \(0|1\) grading;
- shared and disjoint assemblies of the frozen affine code branches;
- exact finite polynomial tests and full cyclic trace identities.

It does not prove a no-go for every nontensor nuclear operator, every signed
complex, every anisotropic space, or every nonlocal completed-orbit weight.
The canonical grading is a genuine escape from scalar rigidity; the paper
classifies its arithmetic ceiling.

## 10. Frozen route record

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

The A2 credit belongs only to the honest degreewise trace-class operators
and their graded/relative determinant on \(\Re s>1\).  Shared recurrence
fails A1 by mixed-word flooding; disjoint recurrence is determinant-equivalent
to an inventory of atom loops.  No same-object A3 continuation and no A4
spectral mechanism are constructed.
