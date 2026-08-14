# HCS-C53 proof package

## P1. Status ledger

| Claim | Status | Proof mechanism |
|---|---|---|
| all-\(n\) equation descent | proved | monomial substitution and explicit fixed basis |
| smoothness | inherited only for \(n=2,3,4\) | base change plus certified source computation |
| rational packets | proved for \(n=2,3,4\) | rational equations and hyperplane projectors |
| order-24 Reynolds descent | proved over \(\mathbf Q\) | Galois-stable graph sum plus restriction/corestriction |
| rank-10/158 projectors | proved subject to the frozen C52 projector certificate | pullback injectivity on rational Chow groups |
| strict local compatibility | proved outside a finite bad set | correspondence traces and Katz--Messing |
| split exponent clearing at \(n=4\) | proved locally | quadratic base change and Euler logarithms |
| inert/global square root | not claimed | inert polynomial identity is generally nonsquare |
| semisimplicity, automorphy, functional equation | not claimed | outside current inputs |

## P2. Equation-level descent

The three identities

\[
C_n(M_nx)=C_n(x),\qquad
Q_{n,\rho}(M_nx)=\rho Q_{n,\rho^2}(x),\qquad
M_n\tau(M_n)=I
\]

follow term-by-term from the reversal \(i\mapsto-i\), the alternating even
phases, and \(\rho^3=1\). The fixed columns in `THEOREM_PACKAGE.md` satisfy
\(M_n\tau(B_n)=B_n\). Their closed determinant is nonzero, so substitution
is invertible. Direct expansion produces forms in \(\mathbf Q[u]\), proving
\(X_{n,0,K}\simeq X_n\) for every \(n\ge2\).

This proof bypasses any false assertion that arbitrary projective descent
data are automatically effective. Smoothness descends along the field
extension, but smoothness of a source row must first be known; in this
project it is certified only for \(n=2,3,4\).

## P3. Chow-cycle descent

The Galois transport

\[
r^k\mapsto r^{-k},\qquad r^ks\mapsto r^{1-k}s
\]

permutes all 24 C52 graph cycles. Hence
\(e_G=24^{-1}\sum_g\Gamma_g\) is invariant. For the degree-two base-change
map \(q\), set \(e_{\mathscr G}=2^{-1}q_*e_G\). Then

\[
q^*e_{\mathscr G}=e_G,\qquad q_*q^*=2.
\]

The second equality proves injectivity of \(q^*\) with rational
coefficients. Every polynomial correspondence identity for the descended
cycles follows from the corresponding C52 identity after pullback. This
proves idempotence, self-transpose, mutual orthogonality, and the rank-
\(10+158\) splitting. Rational coefficients are essential.

The denominator \(1/24\) is the Reynolds average; \(1/2\) is the quadratic
transfer. They must never be conflated.

## P4. Compatible Frobenius polynomials

Spread the smooth projective variety and each rational projector outside a
finite set \(S\). At a good prime, the specialized projector commutes with
Frobenius and splits the realization into image and kernel. After clearing
the cycle denominator, Katz--Messing's correspondence-trace comparison,
applied to powers of Frobenius, makes the projected traces independent of
\(\ell\). Newton identities then put the projected characteristic
polynomial \(\chi_{p,\mathrm{core}}(U)=\det(U-F_p)\) in
\(\mathbf Q[U]\), independently of \(\ell\). Here and below Frobenius is
geometric, acting as \(p\) on \(\mathbf Q_\ell(-1)\).

Integrality is a separate second step. The full untwisted smooth-projective
polynomial \(\det(U-F_p)\) is monic in \(\mathbf Z[U]\) and factors into
the two monic projected polynomials in \(\mathbf Q[U]\). Their roots are
algebraic integers, hence their rational coefficients are rational
algebraic integers. Therefore both factors lie in \(\mathbf Z[U]\). For
the rank-10 core,

\[
P_p(T)=\det(1-F_pT)=T^{10}\chi_{p,\mathrm{core}}(T^{-1})
\in\mathbf Z[T].
\]

The polynomial \(P_p(T)\) is not described as monic. After a Tate twist,
strict compatibility persists in \(\mathbf Q[U]\), but powers of \(p\)
can occur in denominators.

This argument establishes compatibility, not semisimplicity or motivic
irreducibility.

For reciprocity, use four separate facts. First, the middle pairing is
\[
H^5\times H^5\longrightarrow\mathbf Q_\ell(-5),
\qquad
\langle F_px,F_py\rangle=p^5\langle x,y\rangle
\]
for geometric Frobenius. Second, self-transposition and idempotence give
\[
\ker\pi_{\mathrm{core},0}
=(\operatorname{im}\pi_{\mathrm{core},0})^\perp,
\]
so the restricted pairing is nondegenerate. Third, the specialized
projector is defined over \(\mathbf F_p\) and commutes with \(F_p\).
Fourth, the ten core eigenvalues therefore pair as
\(\alpha,p^5/\alpha\). It follows that
\[
P_p(T)=p^{25}T^{10}P_p(1/(p^5T)),\qquad
a_{10-k}=p^{25-5k}a_k.
\]
The idempotent supplies the invariant direct sum; semisimplicity is not
used.

## P5. Artin formalism and the split/inert firewall

For quadratic \(K/\mathbf Q\), induction of the restricted realization is
the direct sum with its quadratic twist. Away from the common bad set,

\[
L_K(\mathsf W_{n,K})=L_{\mathbf Q}(\mathsf W_n)
L_{\mathbf Q}(\mathsf W_n\otimes\chi_K).
\]

At split \(p\), the twist has the same local factor, giving the square and
therefore the exact \(4/n\) exponent. At inert \(p\), Frobenius is squared,
giving

\[
P_{K,v}(U^2)=P_p(U)P_p(-U).
\]

No manipulation of the split identity supplies an inert or global
half-root. Bad-place or global identities would additionally require a
defined compatible Weil--Deligne formalism; they are not used here.

## P6. Irreducibility scope

If one good-prime polynomial of the rank-10 summand is irreducible over
\(\mathbf Q\), then no rational projector defined over \(\mathbf Q\) can
have a realization with nonzero proper image: after good reduction it
commutes with Frobenius, and the image/kernel decomposition would force a
nontrivial factorization of the characteristic polynomial. This statement
does not require semisimplicity.

It does not, without additional comparison and faithfulness hypotheses,
exclude a Chow projector with zero or full cohomological realization (a
possible phantom complement), prove absolute Chow indecomposability, exclude
projectors after coefficient extension, or prove semisimplicity of the
compatible system. Since C53 does not yet certify a full rank-10 Frobenius
polynomial at one prime, even the scoped criterion remains a future Route-A
gate rather than a theorem used in the paper.
