# C169 theorem package

## Assumptions and conventions

Let \(\alpha\in\mathbb R/\mathbb Z\) be irrational and
\[
T_\alpha(x,y)=(x+\alpha,y+x)\pmod1
\]
on \(\mathbb T^2\). Haar measure is normalized. On \(L^2(\mathbb T^2)\), set \(Uf=f\circ T_\alpha\) and \(e_{m,k}=e^{2\pi i(mx+ky)}\).

## Theorem

For every irrational \(\alpha\) and every \(n\ge1\):

1. \(T_\alpha^n(x,y)=(x+n\alpha,\ y+nx+\binom n2\alpha)\pmod1\).
2. \(\operatorname{Fix}(T_\alpha^n)=\varnothing\), hence \(\zeta_{AM}(z)=1\).
3. Haar measure is invariant and \(Ue_{m,k}=e^{2\pi i m\alpha}e_{m+k,k}\).
4. The \(k=0\) sector is pure point. For each \(k\ne0\), the sector decomposes by \(m\bmod |k|\) into \(|k|\) weighted bilateral shifts, each unitarily equivalent to the bilateral shift. The sum of all nonzero sectors has Lebesgue spectrum of countably infinite multiplicity.
5. \(R(x,y)=(\alpha-x,y)\) is an involution with \(RT_\alpha R=T_\alpha^{-1}\). Thus \(\Theta f=\overline{f\circ R}\) is antiunitary, \(\Theta^2=I\), and \(\Theta U\Theta=U^{-1}\).
6. \(U\) is noncompact and belongs to no finite Schatten class. For \(z\ne0\), \(zU\) is not trace class, so the ordinary Fredholm determinant \(\det(I-zU)\) is not defined.

## Proof

The iterate formula follows by induction. If it holds at \(n\), one more application adds \(\alpha\) to the first coordinate and adds the old first coordinate \(x+n\alpha\) to the second; this changes \(\binom n2\) to \(\binom{n+1}2\). A fixed point of the \(n\)-th iterate would require \(n\alpha=0\pmod1\), contradicting irrationality. Every fixed count is therefore zero, and the defining exponential series of the Artin--Mazur zeta vanishes.

The linear part of \(T_\alpha\) has determinant one and the map is invertible, so Haar measure is preserved. Direct substitution in \(e_{m,k}\) gives
\[
e_{m,k}\circ T_\alpha=e^{2\pi i m\alpha}e_{m+k,k}.
\]
For \(k=0\), each Fourier vector is an eigenvector. For \(k\ne0\), fix a residue class of \(m\) modulo \(|k|\); its Fourier vectors form a bilateral chain. The unimodular weights can be removed recursively by a diagonal unitary on that chain. There are \(|k|\) residue classes, and summing over all nonzero \(k\) gives countably many copies of the bilateral shift.

The identities \(R^2=I\) and \(RT_\alpha R(x,y)=(x-\alpha,y-x+\alpha)=T_\alpha^{-1}(x,y)\) are direct. Complex conjugation commutes with composition by a real measurable map, yielding the antiunitary relation.

Finally, a compact operator sends every orthonormal sequence to a sequence with a norm-convergent subsequence. The unitary \(U\) sends the Fourier orthonormal basis to another orthonormal basis, so it is not compact. All singular values of a unitary are one; their \(p\)-sum diverges for every finite \(p\). Hence \(zU\) is not trace class for nonzero \(z\), which blocks the ordinary Fredholm determinant.

## Edge cases and evidence status

Irrationality is essential. Rational \(\alpha\) can admit fixed points of positive iterates and is outside the frozen family. Every numbered statement above is `PROVED`. The finite JSON ledger is only a deterministic regression sentinel.

## Route-A decision

The v0.2 tuple is `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`, overall `ROUTE_A_REJECTED`, with Route B false. A4 records a genuine same-clock Haar--Koopman unitary and antiunitary reversor. It cannot rescue A1: empty periodic data provide no intrinsic arithmetic or primitive-orbit carrier.
