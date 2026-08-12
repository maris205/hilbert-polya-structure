# Devil's advocate audit

## Could irreducibility of \(F_{18}\) already prove rank nine?

No. It proves that one chosen quadratic extension has a transitive normal
closure, but hidden products among several conjugate square classes can
still shrink the Kummer kernel. The rank-nine conclusion comes from the
valuation relation module, not from the degree of \(F_{18}\).

## Could the repeated factor modulo \(19\) be a power-basis index artifact?

The proof does not apply Dedekind's factorization theorem to the order
\(\mathbb Z[A]\). It works directly in \(\overline{\mathbb Q}_{19}\) with
the exact Newton polygon of \(P_9(1802+T)\). The leading coefficient is a
\(19\)-adic unit, and the slope \(-5/2\) directly counts two roots of
valuation \(5/2\). Hence no maximal-order or index assumption enters.

## Could cancellation change the Hill valuation?

No. On the two-root cluster the linear term of the shifted Hill numerator
has valuation \(5/2\), while the constant term has valuation \(3\) and all
higher terms have valuation at least \(5\). The minimum is unique.

## Could another conjugate carry odd valuation at the same place?

No. The exact residue gcd is \(A+3\). The seven noncluster roots reduce
away from this factor, so their Hill values are units.

## Does an exact sequence automatically split?

No splitting is assumed. The quadratic Kummer theorem embeds the full
normal-closure group into \(C_2\wr S_9\). Rank nine gives kernel order
\(2^9\), restriction gives quotient order \(9!\), and therefore the
embedded group already has the full ambient order. Equality, and hence the
semidirect description, follows from the order comparison.

## Is this Hilbert--Pólya evidence?

Only weakly structural. A maximal finite arithmetic monodromy group is
interesting, but it supplies neither an all-period determinant nor a
self-adjoint spectrum. Route A stays rejected and Route B is not opened.
