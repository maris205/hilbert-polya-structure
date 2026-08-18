# Derivation Package — Paper 47

## Dependency chain

1. gcd reduction proves the unique \((t,a,b)\) edge coordinates;
2. harmonic quotient elimination gives the independent divisor-row
   coordinates;
3. the divisor row estimate proves boundedness and compactness;
4. even loops and squarefree high-degree rows prove the bounded endpoint;
5. the scale sum and the coprime double sum prove the \(S_2\) wall;
6. entrywise summability and the even diagonal prove the \(S_1\) wall;
7. the diagonal gives the zeta first trace;
8. gcd extraction in the double series gives the primitive
   Mordell–Tornheim second trace;
9. the mixed triangle prevents a rank-one-fiber misclassification.

## Two independent edge coordinates

### Coprime-scale coordinate

$$
(t,a,b)\longmapsto
\bigl(t a(a+b),t b(a+b)\bigr),\qquad (a,b)=1.
$$

### Divisor-row coordinate

For fixed \(m\),

$$
d\mid m^2,\quad d<m
\longmapsto n=m^2/d-m.
$$

Their exact agreement is the central implementation cross-check.

## Endpoint table

| Property | Exact domain | Decisive boundary |
|---|---|---|
| bounded/compact | \(\sigma>0\) | even diagonal for \(\sigma<0\), unbounded degree at \(0\) |
| Hilbert–Schmidt | \(\sigma>1/2\) | loop scale \(\sum_t t^{-2\sigma}\) |
| trace class | \(\sigma>1\) | absolute even diagonal \(\sum_t t^{-\sigma}\) |
| \(\operatorname{Tr}E_s\) | \(\sigma>1\) | trace-class wall |
| \(\operatorname{Tr}E_s^2\), \(\det_2\) | \(\sigma>1/2\) | Hilbert–Schmidt wall |

## Primitive MT identity

Let

$$
P(s)=
\sum_{\substack{a,b\ge1\\(a,b)=1}}
a^{-s}b^{-s}(a+b)^{-2s}.
$$

Writing arbitrary \(a=du\), \(b=dv\), with \((u,v)=1\), gives

$$
\zeta_{\rm MT}(s,s;2s)=\zeta(4s)P(s).
$$

The edge-scale variable contributes \(\zeta(2s)\), hence

$$
\operatorname{Tr}(E_s^2)
=\zeta(2s)P(s)
=\frac{\zeta(2s)}{\zeta(4s)}
 \cdot\zeta_{\rm MT}(s,s;2s).
$$

The word “primitive” here means gcd one in the edge coordinates. It does not
mean least temporal period.

## Anti-salami remainder

After deleting the shared Schur, summability, Schatten, and determinant
lemmas, Paper 47 retains:

- two exact arithmetic parameterizations of one edge set;
- the zeta first trace from a frozen loop convention;
- the primitive MT second-trace realization;
- a genuinely mixed triangle not explained by scale blocks.

The package is invalid as a standalone paper if the MT realization is
removed from the principal theorem.
