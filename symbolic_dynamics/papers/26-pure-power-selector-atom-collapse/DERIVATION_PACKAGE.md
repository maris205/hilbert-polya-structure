# Derivation Package — SD-C28

## 1. The target cyclic coefficient

For `w=a_{i_1}...a_{i_r}` define

\[
 \chi_m(w)=\prod_{t=2}^r\delta_{i_1,i_t}.
\]

This equals one precisely for a nonempty pure power.  It is unchanged by
cyclic rotation and by replacing `w` with `w^q`.

## 2. Exterior incidence derivation

If `S=supp(w)` and `Q_S=ker(C^S -> C)`, then `dim Q_S=|S|-1`.  Total exterior
parity gives

\[
 \operatorname{Str}_{\Lambda^\bullet Q_S}I
 =\sum_{j=0}^{|S|-1}(-1)^j\dim\Lambda^jQ_S
 =\sum_j(-1)^j\binom{|S|-1}{j}
 =(1-1)^{|S|-1}.
\]

The derivation is exact but post hoc: `Q_S` is not known until the word is
complete.

## 3. Stationary projector derivation

For coordinate projectors `P_i`,

\[
 P_{i_1}\cdots P_{i_r}
 =\left(\prod_{t=2}^r\delta_{i_1,i_t}\right)P_{i_1}.
\]

Taking the trace gives `chi_m(w)`.  This formula already exposes the memory
cost: the `m` mutually orthogonal nonzero idempotents are indexed by the
supplied colors.

## 4. Hankel residual derivation

The Hankel matrix is `H(u,v)=chi_m(uv)`.  Its letter block is

\[
 (H(a_i,a_j))_{i,j}=I_m,
\]

so the rank is at least `m`.  For every nonempty prefix, the residual is a
color residual or zero.  Thus the residual span has dimension at most `m`
after the empty residual is included under `chi(1)=m`.  Under `chi(1)=0`, the
empty residual adds exactly one dimension.  Hence

\[
 \operatorname{rank}H=
 \begin{cases}m,&\chi(1)=m,\\m+1,&\chi(1)=0.\end{cases}
\]

## 5. Syntactic pairing derivation

In `C^m`, write coordinatewise multiplication and
`tau(v)=sum_i v_i`.  The contexts see

\[
 \tau(vw)=\sum_i v_iw_i.
\]

This pairing is nondegenerate, so no nonzero vector can be removed from the
observable quotient.  For the language convention, the extra coordinate has
weight `-m`, giving diagonal form `diag(-m,1,...,1)` and the extra dormant
simple.

## 6. Character-comparison derivation

On positive words,

\[
 \operatorname{Str}_V(w)-\operatorname{Tr}_{\Lambda_m}(w)=0.
\]

At the identity the difference is

\[
 d=\dim V_+-\dim V_--m.
\]

The dormant character is one at the identity and zero on every positive
word.  Therefore the full character identity is

\[
 \chi_{V_+}-\chi_{V_-}
 =\chi_{\Lambda_m}+d\chi_{L_0}.
\]

Passing to a finite combined image algebra and its semisimple quotient turns
character equality into the Grothendieck-group identity

\[
 [V_+^{ss}]-[V_-^{ss}]
 =\sum_i[L_i]+d[L_0].
\]

The radical is absent from the right-hand side because every representation
matrix is block upper triangular along a composition series and traces depend
only on diagonal blocks.

## 7. Trace-log derivation

Let `T=sum_i x_iA_i`.  Expanding before abelianization gives

\[
 \operatorname{Str}T^r
 =\sum_{i_1,\ldots,i_r}x_{i_1}\cdots x_{i_r}
   \operatorname{Str}(A_{i_1}\cdots A_{i_r})
 =\sum_i x_i^r.
\]

Consequently

\[
 \begin{aligned}
 \log D_{gr}(z)
 &=-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Str}T^r\\
 &=-\sum_i\sum_{r\ge1}\frac{(zx_i)^r}{r}
 =\sum_i\log(1-zx_i),
 \end{aligned}
\]

and

\[
 D_{gr}(z)=\prod_i(1-zx_i).
\]

## 8. Why aggregate coefficients lose information

With `R_0=E_12`, `R_1=E_23`, `R_2=E_31`,

\[
 \operatorname{Tr}(R_0R_1R_2)=1,
 \qquad
 \operatorname{Tr}(R_2R_1R_0)=0.
\]

The transpose sector reverses these roles.  Hence the two oriented words have
supertraces `+1` and `-1`.  After commuting variables are imposed, they carry
the same monomial `x_0x_1x_2` and cancel.  A determinant in commuting weights
can therefore pass while the frozen cyclic word selector fails.

## 9. Separable bar derivation

For `B_m=C^m`, the element

\[
 e=\sum_i e_i\otimes e_i
\]

satisfies `mu(e)=1` and centralizes the left and right actions.  It splits the
multiplication map as a `B_m`-bimodule morphism, so `B_m` is projective over
`B_m^e`.  Therefore

\[
 HH_q(B_m)=\operatorname{Tor}^{B_m^e}_q(B_m,B_m)=0\quad(q>0),
\]

and commutativity gives `HH_0(B_m)=B_m`.  The homology is exactly the span of
the primitive color idempotents.

## 10. Total holomorphic grading

For branch word `alpha`, total parity yields multiplicativity of supertrace:

\[
 \operatorname{Str}_{color\widehat\otimes dR}
 (A_\alpha\otimes U_\alpha)
 =\operatorname{Str}_{color}(A_\alpha)
  \operatorname{Str}_{dR}(U_\alpha).
\]

The inherited de Rham factor is one.  The remaining coefficient is
`chi_m(alpha)`.

## 11. Countable trace norm and determinant

For `b_n=u^{ell(n)}n^{-s}` and coordinate projectors,

\[
 \mathcal T^k=\bigoplus_n b_nU_{n,k},
 \qquad
 \|\mathcal T^k\|_1=\sum_n|b_n|\,\|U_{n,k}\|_1.
\]

Uniform compact containment supplies `||U_{n,k}||_1<=C`, hence

\[
 \|\mathcal T^k\|_1\le C\sum_n|u|^{\ell(n)}n^{-\Re s}.
\]

For `|u|<=1`, convergence holds on `Re(s)>1`.  Orthogonal projector products
delete mixed labels before trace, so

\[
 \operatorname{Str}(\mathcal T)^r
 =\sum_nu^{r\ell(n)}n^{-rs}
\]

and

\[
 D_{gr}(s,u,z)=\prod_n(1-zu^{\ell(n)}n^{-s}).
\]

Setting `u=1` changes from digit-resolved weights to completed-return weights;
the selector itself does not erase `ell(n)`.

## 12. Route derivation

- A0 is structural: the arithmetic source semiring and logarithmic returns are
  retained without target-zero data.
- A1 fails: all successful stationary realizations retain one observable
  simple or orthogonal block per supplied label.
- A2 passes: degreewise trace-class operators and their graded ratio exist on
  `Re(s)>1`.
- A3 fails: no continuation of the same trace-class family is constructed.
- A4 fails: no self-adjoint/unitary spectral mechanism is constructed.

Thus the frozen record is

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

