# HCS-C50 exact experiment plan

## E1. Automorphism and representation certificate

Reduce the four rational identities

\[
f(\rho^2/x)=-f(x),\quad T^2=1,\quad
f(T(x))f(x)=h^3,\quad T(\rho^2/x)=\rho^2/T(x)
\]

modulo \(\rho^2+\rho+1\). Reconstruct the group relations and verify the
idempotents \(q_\pm\). The representation dimension ledger must show one
positive and one negative standard \(S_3\)-block.

## E2. Curve-factor controls

On the 21 registered split-prime rows, count \(C(\mathbf F_p)\) and the
fixed \(E_+\)-model trace exactly; under the independently proved
squared-factor theorem, validate the complementary factor trace. On a
separate four-prime subset, count \(C(\mathbf F_{p^k})\) for
\(1\le k\le4\) and use Newton identities to reconstruct the complete
genus-four local numerator independently. These are validations of the
theorem, not its proof and not an identification of canonical Weierstrass
models for \(E_\pm\).

## E3. Second-logarithm replay

Starting from \(c_{p,2}=-(28+4a_p)/(p-1)\), verify the leading coefficient
\(14+2a_p\) after setting \(u=2s+1\). Independently replay the two split
degree-one primes, inert degree-two primes, higher Euler powers, and
denominator correction.

## E4. Fourth chronological zero fibre

Count \(Z_{p,4}\) by a source-ordered dynamic program whose state retains the
initial endpoint, current endpoint, and phase residue. Add the closing term
\(\rho x_7x_0\) only at the terminal step. Never replace the chronology by
a power of an averaged transition matrix.

Independently count \(S,Q,X\) on disjoint projective charts and verify

\[
Z_{p,4}=1+\#\mathbf P^7-\#S-\#Q+p\#X.
\]

## E5. Smoothness replay

Run the exact coefficient-one recurrence ideal over
\(\mathbf Q[r]/(r^2+r+1)\). The reduced basis must be

\[
x_7,x_6,\ldots,x_0,r^2+r+1.
\]

At \(p=181,r=48\), verify every recurrence and both defining equations at
the frozen nonzero witness.

## E6. Mutation tests

The checker must reject at least:

- a changed cubic coefficient or a permuted time ordering;
- deletion or conjugation of the closing coefficient \(\rho\);
- \(d_p=p-1\) in place of \((p-1)/2\);
- a sign or power change in \(\zeta_K^7L(C/K)\);
- a claim that the continued factor is zero-free;
- \(+pB_p\) in place of \(-pB_p\);
- primitive ranks \(85,87,167,\) or \(169\);
- promotion of all-split smoothness;
- \(\operatorname{Det}_8\) or \(\operatorname{Det}_9\) on
  \(\Re s>1/5\); and
- identification of normalized-semifinite and classical Schatten traces.

## E7. Analytic replay

Replay \(n=1,3,4\), and \(n\ge5\) separately. Verify that the extracted
\(F_2\) is holomorphic, but not certified zero-free, on \(\Re s>0\).
Confirm that \(L^{10}(\mathcal M,\tau)\) and classical \(S^{15}\) are the
least fixed integer orders on \(\Re s>1/5\).
