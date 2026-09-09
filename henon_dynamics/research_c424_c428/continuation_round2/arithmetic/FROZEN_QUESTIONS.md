# Second-round arithmetic questions

2026-09-08 UTC. AI-generated bounded questions under the same C424--C428
batch, not admitted contracts. At most two questions may be opened here.
Currently one question is frozen, before any mathematical program.
AM1 remains the single admitted contract; the complete first-round Adler
theorem remains auxiliary only. No old proof program will be rerun.

## AR2-1: all Laurent-parameter quadratic Hénon rational cycles

For every field $k$ with $\operatorname{char}k\ne2$, every $a\in k^*$,
and every nonconstant Laurent polynomial $c\in k[t,t^{-1}]\setminus k$,
where $t$ is transcendental, use

$$
H_{a,c}(x,y)=(y,y^2+c-a x)
$$

on all of $k(t)^2$. One ordinary application of this polynomial
automorphism is one tick; the parameter functions and $a$ stay fixed.
The observable is every ordinary $k(t)$-rational periodic point, its
exact least period, and the coexistence of cycles for the same map.
There is no sign quotient, field extension, local completion, arbitrary
period cutoff, or replacement by a geometric fixed-scheme count.

The full question is an exhaustive all-field, all-parameter atlas, with
a rationality criterion and exact reconstruction. One-pole parameters
are included as an already-owned boundary, not a new result. In the
genuine two-pole case the arithmetic carrier is the pair of valuations
at $0$ and $\infty$, together with the unit group of $k[t,t^{-1}]$.

### Source and local subtraction before computation

- C418 already solves every nonconstant polynomial parameter, all nonzero
  constant determinants and all allowed fields; inversion of $t$ also
  solves the negative-power-only boundary. Its pole argument, two-sign
  offset encoding, finite graph and seven cycle templates are deducted.
- AM1/C412's real annulus arguments and C417's integer cubic secant
  classification are not new questions here. This is not their next
  coefficient value or another integer-height census.
- Ingram owns function-field height/finiteness/bad-place bounds in his
  stated determinant normalization. Gauthier--Vigny provide a broader
  characteristic-zero geometric Northcott result. Their exact primary
  theorem scopes are being checked; bare finiteness or boundedness will
  not be counted as a residual contribution.
- Allen--DeMark--Petsche's completed-field horseshoe is source-owned.
  A local binary shift does not by itself classify global rational
  functions, but that distinction alone is also not a theorem.

### Proposed route and cheap decisive tests

1. Prove that periodic coordinates have no poles outside $0,\infty$,
   and identify their positive and negative principal parts separately.
2. Test whether the two pole signs can genuinely vary independently
   within one ordinary cycle or among coexisting cycles. If all points
   reduce to one common $\pm P+\text{constant}$ family, this may be only
   a short extension of C418 and should not become a paper.
3. For independent-sign behaviour, prove or refute a Laurent-unit
   factorization constraint forcing a special monomial-pair parameter
   form. This is a proposed claim, not a presumed exhaustive reduction.
4. Only after that reduction, use a finite exact sign/offset diagnostic
   if it answers a specified structural question. A general period graph
   with a source-sized upper bound but no new global classification is
   not enough for admission.

Success requires full coverage of the entire frozen Laurent class and a
substantial residual after C418 and the external theorems are subtracted.
An independent-sign counterexample refutes any single-square-only
shortcut but does not itself complete the contract. A known-source
collision, or reduction to a short inherited corollary, triggers an
auxiliary/reject disposition. A missing exhaustive mixed-sign theorem
must remain explicit; it cannot be replaced by a larger parameter scan.

## Process boundary

The second question has not been selected or counted. No mathematical
program, symbolic engine, parameter census, GPU job, manuscript, formal
evaluation or Git mutation has run in this lane. Local PDF structure
preflights are source-access diagnostics, not mathematical experiments;
their actual UNAVAILABLE results are preserved separately.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional. No source classification
is promoted to target Euler factors, root numbers, automorphy, divisor
matching or a Hilbert--Pólya realization.

## One bounded structural diagnostic, frozen before execution

The first diagnostic will test the precise proposed shortcut:
“every single periodic orbit has constant product of its two pole signs.”
It is a falsification check, **not** an exhaustive period theorem.
After the hand reduction to a monomial pair, enumerate pairs of binary
sign words of lengths 2 through 6, up to rotation and independent global
sign flips. Retain only words with nonconstant sign product and genuine
pair-word period. Solve the resulting *linear* compatibility equations
for constant determinant `a` and normalized coefficients `alpha,beta`;
then inspect the constant-term equations for `r=uv != 0` and `C`.
The equation system is

```
2 e_i b_i + alpha = e_(i+1) + a e_(i-1)
2 d_i b_i + beta  = d_(i+1) + a d_(i-1)
b_i^2 + 2 e_i d_i r + C = b_(i+1) + a b_(i-1).
```

The diagnostic may use exact rational polynomial arithmetic only. It may
not launch an expanding parameter/prime/period census. It will stop on a
reconstructible characteristic-zero mixed-sign counterexample, or after
the fixed sign-word cutoff. A negative outcome proves nothing beyond
that cutoff and must not be used to assert the shortcut. If the shortcut
fails, the actual rational-function orbit will be checked by direct
substitution; a full global atlas or an explicit remaining proof gap is
still mandatory. Source and local subtraction have already been performed
before this diagnostic. No C418 program is reused or rerun.
