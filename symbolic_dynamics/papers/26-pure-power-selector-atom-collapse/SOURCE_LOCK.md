# Source Lock — SD-C28

**Freeze date:** 2026-08-14  
**Primary family:** Symbolic Dynamics  
**Authority object:** a cyclic pure-power selector on logarithmic-code return
words, followed by its finite recognizable, graded-character, and
holomorphic-tensor classifications  
**Target-zero data:** forbidden and unused  
**Route-B invocation:** forbidden  
**Review loop:** excluded by instruction

## 1. Arithmetic source boundary

Retain the inherited full-shift semiring skeleton

\[
 F_m\boxtimes F_n\cong F_{mn},\qquad
 F_m\boxplus F_n\cong F_{m+n},\qquad
 S(F_n)\cong F_{n+1},\qquad h(F_n)=\log n.
\]

Rational primes are multiplicative atoms of this skeleton.  Every selector
theorem is first stated for an arbitrary finite color inventory.  Restricting
labels to primes is a specialization, never evidence that the construction
discovered primality.  Prime tables in weights, fitted Euler coefficients,
cutoff-dependent alphabets, and target-zero data are inadmissible.

## 2. Frozen cyclic coefficient

Fix `m>=1` and the alphabet

\[
 A_m=\{a_1,\ldots,a_m\}.
\]

For every nonempty word `w`, define

\[
 \chi_m(w)=
 \begin{cases}
 1,&|\operatorname{supp}(w)|=1,\\
 0,&|\operatorname{supp}(w)|\ge2.
 \end{cases}
\]

The coefficient is invariant under cyclic rotation and repetition because
`supp(w^r)=supp(w)`.  It is frozen word by word, before commutative variables
are substituted.  Equality only after abelianization, only after summing all
words of a given length, or only for a scalar pencil is insufficient.

## 3. Empty-word firewall

Two extensions to the free monoid are kept distinct.

1. **Determinant/character convention:** `chi_m(1)=m`, the identity trace on
   the canonical `m`-color fiber.  The empty word does not occur in a trace
   logarithm.  The Hankel rank and observable syntactic algebra are `m` and
   `C^m`.
2. **Language convention:** `chi_m(1)=0`, the characteristic series of
   nonempty pure powers.  Its Hankel rank and observable syntactic algebra are
   `m+1` and `C^(m+1)`; the extra character is dormant because every letter
   acts on it by zero.

No determinant conclusion depends on the dormant empty-word correction.

## 4. Realization classes

A recognizable series may have a bilinear presentation

\[
 f(w)=\alpha\mu(w)\beta.
\]

The Hankel and syntactic-algebra conclusions apply to this general class.  The
semisimplification theorem is narrower: the letters act by even,
grading-preserving maps on a finite-dimensional complex `Z/2`-graded space
and

\[
 f(w)=\operatorname{Str}\rho(w)
 =\operatorname{Tr}\rho_+(w)-\operatorname{Tr}\rho_-(w)
\]

for every positive word.  Odd letters or supercyclic sign conventions define
a different object and are outside the freeze.

## 5. Frozen exact constructions

For a completed nonempty word with support `S`, the word-indexed exterior
coefficient is

\[
 E(w)=\Lambda^\bullet\ker\!\left(\mathbb C^S\xrightarrow{\sum}\mathbb C\right),
 \qquad
 \operatorname{Str}(I\mid E(w))=(1-1)^{|S|-1}=\chi_m(w).
\]

This is exact, cyclic, repetition-stable, and nonstationary because its fiber
is chosen after the word support is known.

The stationary finite construction is `V_m=C^m` with color projectors

\[
 P_i=e_ie_i^*,\qquad P_iP_j=\delta_{ij}P_i,
 \qquad
 \operatorname{Tr}(P_{i_1}\cdots P_{i_r})=\chi_m(w).
\]

It is positive and exact, but visibly provides one recurrent line per supplied
color.

## 6. Frozen collapse theorem

If a finite-dimensional ordinary or `Z/2`-graded stationary multiplicative
trace realization agrees with `chi_m` on every nonempty word, then its
semisimplified virtual character is

\[
 [V_+^{\mathrm{ss}}]-[V_-^{\mathrm{ss}}]
   =\sum_{i=1}^m[L_i]+d[L_0].
\]

Here `L_i` is the one-dimensional character on which `a_i` acts as one and
all other letters act as zero, `L_0` is dormant, and `d` depends only on the
empty-word convention.  Common even/odd semisimple summands cancel, while
radical extensions are invisible to all word traces.  Thus the theorem does
not assert simultaneous diagonalizability of the original matrices.

In the ordinary case the observable dimension is at least `m`, and the
semisimplification contains `L_1+...+L_m`, plus only dormant simples.  The
Berezinian/Fredholm trace logarithm therefore collapses to

\[
 \operatorname{Ber}\!\left(I-z\sum_i x_iA_i\right)
   =\prod_{i=1}^m(1-zx_i).
\]

## 7. Aggregate-trace adversary

The wordwise hypothesis cannot be replaced by equality of commutative power
traces.  In dimension three set

\[
 R_0=E_{12},\qquad R_1=E_{23},\qquad R_2=E_{31}.
\]

Adding `R_i` to an even projector sector and `R_i^T` to an odd sector cancels
the aggregate commuting-pencil power traces, while

\[
 \operatorname{Str}(A_0A_1A_2)=1,\qquad
 \operatorname{Str}(A_2A_1A_0)=-1.
\]

Independent noncommuting word coefficients, or necklace-resolved traces, are
therefore mandatory.

## 8. Bar/Hochschild boundary

A free or polynomial shared algebra has mixed cyclic classes and does not
supply the frozen selector.  Passing to the separable color algebra
`C^m` works, but

\[
 HH_0(\mathbb C^m)\cong\mathbb C^m,\qquad
 HH_k(\mathbb C^m)=0\quad(k>0),
\]

so the canonical homological object is already the atom/color inventory.  A
support-dependent exterior fiber and a stationary bar/Hochschild complex are
not interchangeable.

## 9. Holomorphic tensor and trace-class domain

Retain Paper25's Elias gamma code

\[
 \ell(n)=2\lfloor\log_2n\rfloor+1,
\]

affine disk return `phi_n`, ratio `q_n=2^{-ell(n)}`, and canonical Bergman
zero-/one-form pullbacks `U_{n,0}`, `U_{n,1}`.  The Paper25 local supertrace
cancellation equals one for every completed branch word after scalar weights
are removed.

Tensor the color selector with this de Rham sector.  For a countable inventory
on `ell^2(I)` use coordinate projectors `P_n` and weights

\[
 b_n(s,u)=u^{\ell(n)}n^{-s}.
\]

The degreewise operator family is trace class whenever
`sum_n |b_n(s,u)|<infinity`; in particular at `u=1` for `Re(s)>1`.  The
resulting graded determinant is

\[
 \prod_{n\in I}\bigl(1-zb_n(s,u)\bigr).
\]

This is unitarily a direct sum of supplied color blocks.  It is an honest A2
construction, not a finite-memory shared-renewal escape.

## 10. Determinant and marker ownership

Every “graded determinant” is a ratio of separately honest ordinary
degreewise determinants,

\[
 D_{\mathrm{gr}}(z)=
 \frac{\det(I-zL^0)}{\det(I-zL^1)}.
\]

It is not the ordinary determinant of `L^0 direct-sum L^1`, which is the
product of those degreewise determinants.  For finite color fibers the same
distinction is the ordinary determinant versus the Berezinian/virtual
character.

The variable `z` counts completed returns.  The variable `u` counts original
binary digits and retains `u^ell(n)`.  Setting `u=1` is a return-scale
specialization, not an equality of digit and induced dynamics.

## 11. Allowed conclusions and explicit nonclaims

The source lock proves selector rigidity only for finite-dimensional
stationary even trace representations, and syntactic rigidity for finite
recognizable series.  It does not classify arbitrary infinite-dimensional
nuclear representations, unbounded complexes, odd-letter supercategories,
or nonlocal orbit-dependent weights.  Literal matrices may contain
trace-invisible radicals.  Aggregate commutative traces do not imply the
wordwise theorem.  Analytic continuation of the scalar color product is not
continuation of the trace-class operator family.

## 12. Frozen route record

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

A1 fails because the stationary selector stores one net simple character per
supplied label.  A2 passes only for the honest degreewise trace-class family
and its graded ratio on `Re(s)>1`.  No same-object A3 continuation or A4
spectral mechanism is constructed.
