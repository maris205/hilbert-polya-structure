# Proof package

## 1. Reversor-line closure

Let `f(q)=1-6q^2` and

\[
H(q,p)=(f(q)-p,q),\qquad R(q,p)=(p,q),\qquad J=RH.
\]

Both `R` and `J` are involutions and `RHR=H^{-1}`. The line `Fix(J)` is
parameterized by

\[
q_0=X,\qquad q_{-1}=q_1=\frac{f(X)}2.
\]

For odd `n=2m+1`, reaching `Fix(R)` after `m+1` iterates is exactly

\[
F_n(X)=q_{m+1}(X)-q_m(X)=0.
\]

The two reversor identities then imply `H^n(q_0,q_{-1})=(q_0,q_{-1})`.

## 2. Degree theorem

For `j>=1`, induction in the recurrence gives `deg q_j=2^j`; its leading
coefficient is nonzero because it is `-6` times the square of the previous
one. Hence

\[
\deg F_n=\deg q_{m+1}=2^{m+1}=2^{(n+1)/2}.
\]

## 3. Divisibility theorem

Let `d=2r+1` divide odd `n`. In `Q[X]/(F_d)` one has both

\[
q_{-1}=q_1,\qquad q_r=q_{r+1}.
\]

The reversible second-order recurrence therefore gives
`q_(j+d)=q_j` for every integer `j`. Since `n/d=2s+1` is odd,

\[
\frac{n-1}{2}=sd+r.
\]

Thus `q_((n+1)/2)=q_(r+1)=q_r=q_((n-1)/2)` modulo `F_d`. Euclidean division
in the univariate ring proves

\[
F_d\mid F_n.
\]

## 4. Formal primitive degree

Define the virtual symmetry-line dynatomic divisor

\[
\mathfrak D_n^{\rm form}=\sum_{d\mid n}\mu(n/d)[F_d=0].
\]

Its degree is

\[
D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}.
\]

Every proper divisor of odd `n` is at most `n/3`, so

\[
D_n=2^{(n+1)/2}+O(n2^{n/6+1/2}).
\]

The finitely many small periods are positive by direct evaluation; for
`n>=11`, `n2^{-n/3}<1` makes positivity immediate. Therefore

\[
\lim_{n\to\infty\atop n\text{ odd}}\frac1n\log D_n=\frac12\log2.
\]

## 5. Exact finite quotient chain

For every odd `n<=15`, exact division gives a polynomial

\[
\Psi_n=F_n\big/\prod_{d\mid n,\ d<n}\Psi_d.
\]

The quotient degrees are `2,2,6,14,28,62,126,246`; each quotient is
irreducible over `Q`, each `F_n` is squarefree, and the product of all
divisor quotients reconstructs `F_n`. The `n=9` coefficient digest is
`b0e55d...ef9dd`, exactly the P58 degree-28 mixed-axis factor.

## 6. Claim boundary

The virtual divisor is defined and its degree theorem is unconditional. Its
all-period effectivity as a reduced primitive-root divisor is not proved.
General dynatomic effectivity theorems for morphisms of projective varieties
do not attach automatically to this symmetry-line intersection of a birational
projective extension. A transversality or local-intersection-multiplicity
theorem is still required.
