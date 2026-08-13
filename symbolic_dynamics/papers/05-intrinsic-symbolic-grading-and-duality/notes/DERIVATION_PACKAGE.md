# Derivation Package

## Target

Derive or refute the same-source chain

\[
\text{tensor factorization}
\longrightarrow
\text{intrinsic grading}
\longrightarrow
\text{graded determinant}
\longrightarrow
\text{new A3 structure}.
\]

## Status

**COHERENT AS SCOPED / SCOPED THEOREM STOP.**

The first three arrows are exact in the Euler half-plane. The final arrow
fails for every preregistered intrinsic duality. The stage therefore gives

~~~text
GO_A2_GRADED_ORIENTATION / STOP_A3_COMPLETION
~~~

and retains SD-C07 without assigning SD-C08.

## Invariant object

The source is the symmetric monoidal skeleton of finite full shifts:

\[
F_m\boxtimes F_n\cong F_{mn},
\qquad
h(F_n)=\log n.
\]

Its tensor atoms are \(F_p\), and the Paper-04 transfer is

\[
L_s e_p=p^{-s}e_p
\]

on \(\ell^2(\operatorname{At})\). Every construction in this package is a
functorial operation on that same symbolic source.

## Frozen assumptions

- Tensor atoms are extracted from the full-shift product law, not from a
  prime table.
- All weights use topological entropy.
- A supertrace is claimed only on a trace-class graded object.
- Scalar continuation of \(\zeta\) does not count as operator continuation.
- A target-selected \(1/2\)-shift, Gamma factor, or counterterm receives no
  source credit.

## Derivation map

1. The open tensor-divisor order complex \(\Delta_n\) has reduced homology
   \(S^{\omega(n)-2}\) for squarefree \(n\) and is contractible otherwise.
2. Its homology supertrace equals \(\mu(n)\), including the prime degree
   \(-1\) convention.
3. The zero-differential exterior transfer module has
   \(\operatorname{Str}\Gamma_-(L_s)=1/\zeta(s)\).
4. The purely odd one-particle Berezinian has
   \(\operatorname{Ber}(I-L_s)=\zeta(s)\).
5. The honest equivariant Koszul resolution instead has supertrace \(1\):
   its bosonic and fermionic Euler factors cancel.
6. Natural symbolic reversal preserves entropy and produces \(s\mapsto s\).
7. Tensor-group inversion produces \(s\mapsto-s\) and is parity-even.
8. Even after granting an external \(s\leftrightarrow1-s\) pairing, the
   first shared Schatten regularization is \(\det_3\); it is zero-free and
   deletes repetitions \(r=1,2\).

## Exact formulas

### Factorization homology

\[
\widetilde H_j(\Delta_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,& n\text{ squarefree},\ j=\omega(n)-2,\\
0,& n\text{ not squarefree},
\end{cases}
\qquad
\widetilde\chi(\Delta_n)=\mu(n).
\]

Hence, for \(\Re s>1\),

\[
\operatorname{Str}W_s
=\sum_{n\ge1}\mu(n)n^{-s}
=\frac1{\zeta(s)}.
\]

### Exterior module versus honest Koszul resolution

\[
\operatorname{Str}_{\Lambda^\bullet V}\Gamma_-(L_s)
=\det(I-L_s)
=\frac1{\zeta(s)},
\]

\[
\operatorname{Ber}_{V_{\bar1}}(I-L_s)=\zeta(s).
\]

For \(K=\mathbb C[M]\otimes\Lambda^\bullet V\) with the standard equivariant
Koszul differential and total-mass transfer \(T_s\),

\[
\operatorname{Tr}T_s
=\frac{\zeta(s)^2}{\zeta(2s)},
\qquad
\operatorname{Str}T_s=1,
\qquad
\operatorname{sdet}(I-zT_s)=1-z.
\]

Thus the exterior module, factorization homology, and Koszul resolution are
not interchangeable.

### Duality obstruction

\[
L_s\in\mathcal S_q
\iff q\Re s>1,
\qquad
L_{1-s}\in\mathcal S_q
\iff q(1-\Re s)>1.
\]

There is no common trace-class or Hilbert--Schmidt domain. The first integer
order with overlap is \(q=3\):

\[
\frac13<\Re s<\frac23.
\]

After granting the missing half-density pairing,

\[
D_3(s)=\det\nolimits_3(I-L_s)\det\nolimits_3(I-L_{1-s})
\]

is \(s\leftrightarrow1-s\) symmetric but zero-free, with

\[
\log D_3(s)
=-\sum_{r\ge3}\frac1r
\sum_p\left(p^{-rs}+p^{-r(1-s)}\right).
\]

The regularization removes the prime and prime-square traces that a Riemann
divisor mechanism must retain.

## Evidence status

| Statement | Status | Evidence |
|---|---|---|
| Tensor-divisor homology theorem | PROVED | Crosscut theorem; exact \(N\le512\) chain audit |
| Exterior/Berezinian Euler identities | PROVED | Trace-class product in \(\Re s>1\); exact coefficient audit |
| Equivariant Koszul cancellation | PROVED | Factorwise boson/fermion cancellation |
| Reversal gives \(s\mapsto s\) | PROVED | Entropy invariance and chain intertwining |
| Group inversion gives \(s\mapsto-s\) | PROVED | Character calculation |
| First shared Schatten order is \(3\) | PROVED | Exact \(\mathcal S_q\) criterion |
| Intrinsic half-density / Gamma sector | OPEN | No same-source construction found |
| A3 promotion | FAIL | G4 condition unmet |

## Boundaries and non-claims

- Selecting the exterior/Koszul functor is a modeling choice; its internal
  degree is canonical after selection.
- Simplex orientation is only a chain-basis gauge.
- The finite dual ratio has exact reflection symmetry but no infinite
  determinant credit.
- The adversarial paired \(\det_3\) is an obstruction, not a promoted
  candidate.
- No Riemann zeros are read or fitted.
- No Gamma factor, functional equation, completed-\(\xi\) determinant,
  self-adjoint operator, or Route-B object is claimed.

The complete statements and proofs are in
[PROOF_PACKAGE.md](../PROOF_PACKAGE.md); exact computational evidence is in
[EXPERIMENT_REPORT.md](../EXPERIMENT_REPORT.md).
