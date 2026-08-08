# HCS-C20 results

## Exact geometric output

\[
\operatorname{Gal}(\mathbb Q(E)/\mathbb Q(\sigma))=D_7,
\qquad
(g(E),g(B),g(C))=(8,2,3).
\]

The quotient maps are

\[
E\longrightarrow B=E/\langle\tau\rangle
\quad\text{(unramified cyclic degree \(7\))},
\]

and

\[
E\longrightarrow C=E/\langle J\rangle
\quad\text{(quadratic, six branch points)}.
\]

The exact quotient and endomorphism identities are

\[
B:w^2=Q_6(\sigma),\qquad
\mathbb Q(E)=\mathbb Q(C)(\sqrt{Q_6(\sigma)}),
\]

\[
\operatorname{Jac}(E)\sim_{\mathbb Q}
\operatorname{Jac}(B)\times\operatorname{Jac}(C)^2,
\]

and

\[
\mu_{q_*\tau^*q^*}(T)=T^3+T^2-2T-1.
\]

## Selected-prime count ledger

The producer and the non-importing checker independently enumerate the
affine plane septic over \(\mathbb F_{p^r}\), \(r=1,2,3\), and apply the
proved normalization correction.

| \(p\) | affine counts | node split by \(r\) | normalized \(C\)-counts | Frobenius power sums |
|---:|---|---|---|---|
| 5 | \(3,31,141\) | no, yes, no | \(9,39,147\) | \(-3,-13,-21\) |
| 11 | \(11,159,1163\) | yes, yes, yes | \(19,167,1171\) | \(-7,-45,161\) |
| 13 | \(10,234,2125\) | no, yes, no | \(16,242,2131\) | \(-2,-72,67\) |

For each row,

\[
N_C(r)=N_{\mathrm{aff}}(r)+7+
\begin{cases}
+1,&\text{the ordinary node splits},\\
-1,&\text{the node is nonsplit}.
\end{cases}
\]

## Certified local factors

The genus-three numerators are

\[
\begin{aligned}
L_{C,5}&=1+3T+11T^2+31T^3+55T^4+75T^5+125T^6,\\
L_{C,11}&=1+7T+47T^2+161T^3+517T^4+847T^5+1331T^6,\\
L_{C,13}&=1+2T+38T^2+51T^3+494T^4+338T^5+2197T^6.
\end{aligned}
\]

They are simultaneously reconstructed from the counts and from
\[
\operatorname{Norm}_{\mathbb Q(\theta)/\mathbb Q}
(1-a_pT+pT^2),
\qquad \theta^3+\theta^2-2\theta-1=0.
\]

At these primes the genus-eight factors are certified by
\[
L_{E,p}=L_{B,p}L_{C,p}^2.
\]

## Verification state

- Producer schema: `HCS-C20-producer-1`.
- Independent checker schema: `HCS-C20-independent-check-1`.
- Independent exact checks: 136 passed.
- Regression tests include certificate-byte binding, complete recomputation,
  naming consistency, selected-prime ledgers, and deliberate tamper failure.
- Scope: no good-reduction or local-factor claim outside \(p=5,11,13\).

The authoritative machine-readable values and SHA-256 binding are in
[c20_certificate.json](c20_certificate.json) and
[c20_independent_check.json](c20_independent_check.json).
