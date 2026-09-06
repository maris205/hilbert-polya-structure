# Independent bounded check: height-series residues

2026-09-07. Reviewer: the positive-characteristic scout, not the author of
the height-series proof. The arithmetic reviewer requested this auxiliary
read-only check while independently reviewing the full argument. This is
current-team internal review, not human peer review.

## Material and exact scope

Actually read [HEIGHT_PROOF_PACKAGE.md](../spectral/HEIGHT_PROOF_PACKAGE.md),
including its definitions and Steps 4–6. This check concerns only the
factorization (7)–(8), coefficient aggregation from the cone/turn sectors,
and the $k=1$ root-of-unity degeneration. It does **not** certify the full
orbit classification, convergence proof, natural boundary or counting
asymptotic. No source browsing or external API was used for this check.

**Finding: no defect found within that scope.**

## Algebraic verification

The relation $v^d=q$ gives

$$
\sum_{r=1}^{d-1}v^{-r}=\frac{q-v}{q(v-1)}.
$$

The three rational terms in (7) combine to

$$
\frac1{A-1}+\frac{A}{q/v-A}+1
=\frac{A(q-v)}{(A-1)(q-vA)}.
$$

After extracting $(q-1)(q-v)$, the remaining numerator is

$$
(q-1)A(v-1)+(A-1)(q-vA)=(q-A)(vA-1).
$$

This yields (8) with precisely its stated signs and factors. An independent
symbolic check was actually executed from the repository root:

```text
python -B -c 'import sympy as s; q,v,A=s.symbols("q v A"); R=(q-1)**2*(1/(A-1)+A/(q/v-A)+1)+(q-1)*(q-v)/(v-1); F=(q-1)*(q-v)*(q-A)*(v*A-1)/((v-1)*(A-1)*(q-v*A)); print("factorization_difference =",s.factor(R-F)); d=s.symbols("d",integer=True,positive=True); print("combined_numerator_difference =",s.expand((q-1)*A*(v-1)+(A-1)*(q-v*A)-(q-A)*(v*A-1)))'
```

Actual stdout, exit status 0:

```text
factorization_difference = 0
combined_numerator_difference = 0
```

The finite geometric-sum reduction was checked algebraically above, not
delegated to a symbolic assumption that $v^d=q$.

## Aggregation and degeneration at k=1

Put $t=B_0(s_0)=q^{1-s_0}$. If $t\ne1$, the two cone terms of $C_0$
each contribute $(q-1)^2/(t-1)$ to their shared denominator. Although
$C_0$ has weight one in (5), its aggregate contribution is therefore
$2(q-1)^2/(t-1)$. Both $C_1$ and $E_1$ have weight two. This gives the
same total factor $2R$ as claimed; there is no missing factor of two.

At $k=1$ the definitions give $vA=q^{s_0}$ and $t=q/(vA)$. Hence
$q-vA=0$ exactly when $t=1$, which at the displayed pole lattice is
exactly $(d+1)\mid\ell$. Away from that condition, the other numerator
and denominator factors do not vanish: in particular
$|A|=q^{1-1/d}>1$, $|A|<q$ and $|vA|=q>1$.

At $t=1$, equation (6) gives
$b_j=((d-1)/(d+1))j+O_d(1)$. Thus the double-pole coefficient of $C_0$
is

$$
\frac{(q-1)^2(d-1)}{(d+1)(\log q)^2}>0.
$$

The remaining contributing sectors have at most simple poles there and
cannot cancel this coefficient. Consequently the claimed distinction
between double poles for $(d+1)\mid\ell$ and simple poles otherwise is
correct within the reviewed algebraic and sector-aggregation framework.
