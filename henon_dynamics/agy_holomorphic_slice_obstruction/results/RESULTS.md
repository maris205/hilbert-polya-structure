# HCS-C26 results: an exact AGY point-evaluation slice witness

## Result status

```text
exact C25 gamma_star application witness:                 VERIFIED
point-evaluation hypothesis chain:                        COMPLETE, CONDITIONAL
C24 discrete-metaplectic-atom theorem:                    EXTERNAL, NOT REPROVED
C25 all-length projected-matrix decoder theorem:          EXTERNAL, NOT REPROVED
bounded vector Bergman AGY transfer space:                 PROVED
positive-prefix common complex-domain geometry:            GO BY EXACT LEMMA INPUTS
scalar Perron/characteristic trace reduction:              PROVED IDENTITY + 3 CHECKS
countable scalar trace-norm summability:                   PROVED
finite decoder sentinel as proof/completeness evidence:   FORBIDDEN
ordinary scalar Bergman Fredholm determinant:             PROVED
ordinary holomorphic metaplectic Fredholm determinant:    REFUTED FOR TARGET
```

The meaningful advance is a sharp conditional obstruction, not a positive
Fredholm construction.  A tensor-type holomorphic realization cannot evade
the unsmoothed oscillator fibre merely by losing branch-supported bump
functions if it still contains constants continuously and has continuous
point evaluation.

## Exact source-locked witness

The producer and independent checker both reconstruct:

- seven labeled Rauzy states and fourteen directed edges;
- the AGY base permutation `1342/4321`, sorted state id 4;
- `eta=tbttbtbb`;
- `gamma_star=t^64 eta^8`, of elementary length 128;
- later-on-the-left chronological multiplication;
- a strictly positive determinant-one matrix `B_gamma_star` and
  `R_gamma_star=B_gamma_star^T`.

With

\[
x_0=\frac{R_{\gamma_*}{\bf 1}}
          {{\bf 1}^{T}R_{\gamma_*}{\bf 1}},
\qquad
S=S_{\gamma_*}(x_0)={\bf 1}^{T}R_{\gamma_*}x_0,
\]

the exact normalizer is

\[
\boxed{
S=\frac{15076979616018}{8999921}
}\approx1.6752346621729236\times10^6.
\]

Direct differentiation of

\[
h_{\gamma_*}(x)=\frac{R_{\gamma_*}x}
{{\bf 1}^{T}R_{\gamma_*}x}
\]

in three affine simplex coordinates gives

\[
\boxed{
J_{\gamma_*}(x_0)=S^{-4}
}
\]

exactly.  This rejects the common mutation that substitutes the affine
dimension three for the projective-Jacobian exponent; the exponent is the
number of interval labels, namely four.

## Common complex-domain gate: exact positive prefix

Every source branch has a fixed positive length-matrix prefix

\[
P=B_{\gamma_*}^{T}=R_{\gamma_*};
\]

the nontrivial return branches have the pattern \(PQP\), with \(Q\)
nonnegative.  Normalizing the four columns of \(P\), the producer and
checker obtain the exact coordinate margin

\[
\boxed{
\delta
=\min_{i,j}\frac{P_{ij}}{\sum_kP_{kj}}
=\frac{14783}{1642663}>0.
}
\]

The exact maximum Birkhoff cross ratio is

\[
\boxed{
\theta(P)
=\max_{i,k,j,l}
\frac{P_{ij}P_{kl}}{P_{il}P_{kj}}
=\frac{12206150825}{12121793906}.
}
\]

Therefore

\[
\Delta(P)=\log\theta(P)
\approx0.0069350089391777932,
\qquad
q(P)=\tanh\!\left(\frac{\Delta(P)}4\right)
\approx0.0017337504976364321<1.
\]

These exact quantities independently validate the fixed positive prefix and
the convention locks.  The self-contained complex-cone theorem, rather than
complex-point sampling or the numerical Birkhoff bound, supplies a bounded
branch-independent domain with strict containment.  On that domain

\[
\operatorname{Re}\ell_\gamma(z)>0,
\qquad
\ell_\gamma(z)={\bf1}^{T}R_\gamma z,
\]

so the principal logarithm on the right half-plane defines the common
holomorphic weight

\[
\ell_\gamma(z)^{-(s+4)}
=\exp(-(s+4)\operatorname{Log}\ell_\gamma(z)).
\]

The complex projective dimension is three while the homogeneous Jacobian
exponent is four.  The common-domain/log theorem, combined with C25 real
branch summability and the Bandtlow--Jenkinson Bergman restriction theorem,
does prove locally uniform countable trace-norm summability and the scalar
Fredholm determinant.  The finite cone calculation above verifies inputs
and conventions; it is not the proof of those functional-analytic results.

## Conditional point-evaluation theorem

Let `X` be a proposed space of functions with values in the oscillator
Hilbert space \(\mathscr F=L^2(\mathbb R^2)\), and suppose:

1. the literal chronological AGY transfer \(\mathcal L_s:X\to X\) is
   bounded;
2. the constant embedding
   \(\iota_{\rm const}:\mathscr F\to X\) is bounded;
3. evaluation \(\operatorname{ev}_{x_0}:X\to\mathscr F\) is bounded;
4. the C25 source-half-plane pointwise branch sum is absolutely summable;
5. C25 all-length decoding is used to retain distinct projected branch
   matrices and actual central signs;
6. the C24 discrete-metaplectic-atom theorem is invoked.

Then

\[
\operatorname{ev}_{x_0}\mathcal L_s\iota_{\rm const}
=\sum_\gamma w_{s,\gamma}(x_0)U_\gamma.
\]

C24 gives the signed-aggregate \(\ell^2\) essential-norm bound.  C25
injectivity makes each projected aggregate a singleton, so retaining only
the exact `gamma_star` term yields

\[
\left\|
\operatorname{ev}_{x_0}\mathcal L_s\iota_{\rm const}
\right\|_{\rm ess}
\ge
|w_{s,\gamma_*}(x_0)|.
\]

For \(s=\sigma+it\), the magnitude is independent of \(t\):

\[
\boxed{
|w_{s,\gamma_*}(x_0)|=S^{-(\sigma+4)}.
}
\]

Consequently,

\[
\boxed{
\|\mathcal L_s\|_{\rm ess}
\ge
\frac{S^{-(\sigma+4)}}
{\|\operatorname{ev}_{x_0}\|\,
 \|\iota_{\rm const}\|}.
}
\]

The machine-registered exact floors are

\[
\begin{aligned}
\sigma=0:\quad
S^{-4}
&=
\frac{6560769639033108250634950081}
{51672252134321473356696529937672668896230786946152976}
\\
&\approx1.2696891209576963\times10^{-25},
\\[3mm]
\sigma=1:\quad
S^{-5}
&=
\frac{59046408450496490640162750567943601}
{779061492142907448328418465488645116967666902058919462934767969568}
\\
&\approx7.5791717400999829\times10^{-32}.
\end{aligned}
\]

Small numerical size is irrelevant to the qualitative conclusion: every
strictly positive lower bound excludes compactness.

## Scalar periodic trace: Perron/characteristic simplification

For a positive determinant-one chronological length matrix \(A\), let

\[
p_A(x)=\frac{Ax}{{\bf1}^{T}Ax},
\qquad
\chi_A(t)=\det(tI-A),
\]

and let \(\lambda\) be the simple Perron root.  The branch normalizers
telescope around the periodic word, so the scalar weight is

\[
\lambda^{-(4+s)}.
\]

On the three-dimensional projective tangent, the non-Perron eigenvalues
appear divided by \(\lambda\).  Hence

\[
\boxed{
\det_{\mathbb C}(I-Dp_A)
=\frac{\chi_A'(\lambda)}{\lambda^3}
}
\]

and the scalar trace atom simplifies to

\[
\boxed{
\frac{\lambda^{-(4+s)}}
     {\det_{\mathbb C}(I-Dp_A)}
=\frac{\lambda^{-(s+1)}}{\chi_A'(\lambda)}.
}
\]

The general identity follows from Perron eigenline splitting, not from a
finite-word fit.  Two independent specializations were nevertheless made.

For `gamma_star`,

\[
\chi_{\gamma_*}(t)
=t^4-1675423t^3+463448097t^2-1675423t+1,
\]

with

\[
\lambda_{\gamma_*}
\approx1675146.33874045398181070157337977279365519.
\]

For a genuine ordered two-return word, the second branch is

```text
gamma_star · bttbtbb · gamma_star,
```

In **forward Rauzy-path order** the two returns are composed as

```text
gamma_star, then second_branch,
B_two = B_second_branch * B_gamma_star.
```

The inverse projective map reverses that forward path composition:

```text
A_two = B_two^T = A_gamma_star * A_second_branch,
h_two = h_gamma_star o h_second_branch.
```

Thus, in the operator-factor convention of
`T_gamma1 ... T_gamman`, the same example has factor order
`(second_branch, gamma_star)`.  Recording both orders prevents the forward
Rauzy clock from being confused with the contravariant inverse-branch
action.

The full elementary word has length 391.  Its matrix differs from the
reversed-order matrix, and

\[
\begin{aligned}
\chi_{2}(t)
={}&t^4-16015896888538880980t^3\\
&+540332039590143109406685478t^2\\
&-16015896888538880980t+1,
\end{aligned}
\]

with

\[
\lambda_2
\approx16015896888505143747.3397455655949642813.
\]

However, the reversed two-return product has the same characteristic
polynomial: `AB` and `BA` are cyclically equivalent at this spectral level.
Thus this example validates contravariant matrix bookkeeping but is not a
spectral chronology test.

The spectral chronology sentinel uses three forward returns

```text
gamma_star,
gamma_star · bttbtbb · gamma_star,
gamma_star · bbb · gamma_star.
```

Its total elementary length is 650.  The forward and noncyclically reversed
orders have reciprocal characteristic-polynomial coefficients

```text
forward:
[1,
 -78462677068799478932275282109777,
  193788302599840312521254027654987461135596759,
 -78462677068799478932275282109777,
  1]

reverse:
[1,
 -78462676839072961074051275858065,
  193788302599985746036399604537872487742569559,
 -78462676839072961074051275858065,
  1]
```

so genuine noncyclic time reversal is visible in the scalar Perron trace
data.  The independent checker recomputes all three characteristic
polynomials and uses a high-precision centered finite difference for
\(Dp_A\).  The relative denominator discrepancies for the one-, two-, and
three-return examples are approximately \(5.4\times10^{-95}\),
\(6.9\times10^{-103}\), and \(1.0\times10^{-110}\), respectively.  These
examples validate chronology and exponent bookkeeping; they are not the
proof of the general identity.

## What was and was not proved

The exact certificate verifies the selected coefficient and every algebraic
input attached to it.  The general point-evaluative theorem remains
conditional on its explicitly declared function-space maps and on the
already proved C24/C25 theorems.  For the concrete space
`A^2(Omega;L^2(R^2))`, however, C26 proves boundedness, bounded constants and
evaluation, and hence noncompactness.  It also proves that the scalar
operator on `A^2(Omega)` is trace class, that every fixed power has the
absolutely convergent chronological trace sum, and that the scalar Fredholm
determinant is jointly holomorphic in its stated parameter domain.

C26 does not claim:

- a new proof of C25 real absolute branch summability;
- a new proof of C24 atomic noncompactness;
- a new proof of C25 all-length decoding;
- an ordinary trace of an isolated infinite-dimensional metaplectic
  unitary;
- an ordinary Fredholm determinant for the infinite oscillator twist;
- convergence of the orbit logarithm at determinant variable `u=1` without
  an additional spectral argument;
- a Riemann divisor, functional equation, or prime law.

The result is nevertheless a large filter: standard vector-valued Hardy,
Bergman, `H^infinity`, or RKHS candidates that meet the bounded constants,
evaluation, and literal-transfer assumptions inherit the obstruction
without needing a holomorphic branch localizer.

## Finite sentinel

The optional state-2 first-return replay through elementary length 20 gives

```text
first returns:       13,528
distinct B matrices: 13,528
collisions:          0
```

Every word is recovered by finite row subtraction.  This is only a mutation
sentinel.  It is not an AGY branch enumeration, does not prove completeness,
and does not replace the external C25 all-length theorem.
