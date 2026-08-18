# Research question brief

## Narrow question

For a primitive one-step shift of finite type sampled along the multiplicative
chains

$$
i,qi,q^2i,\ldots\qquad(q\nmid i),
$$

does the prefix complexity admit an exact, bounded, order-one correction to
its leading entropy term, and can every subsequential value of that correction
be described without replacing the integer cutoff by an asymptotic proxy?

The quantifiers are fixed:

```text
for every integer q >= 2
for every finite primitive zero-one adjacency matrix A
for every prefix cutoff N >= 1
derive an exact finite-N identity and its full N -> infinity accumulation set
```

The golden-mean control asks a second, narrower question: is the complete
binary boundary image a quantitatively separated Cantor set, and do the same
coefficients force dense radial singularities of its ordinary generating
function?

## Answer

Yes, under the frozen primitive hypothesis.

Adding the site $N$ extends exactly one $q$-adic chain. Therefore the
successive logarithmic increment is $c_{\nu_q(N)}$. After subtracting the
Perron limit and the valuation mean, exact summation by parts gives a uniformly
convergent series on $\mathbb Z_q$. Compactness and the density of every tail
of the positive integers in $\mathbb Z_q$ identify the complete accumulation
set with the image of that continuous function.

For the binary golden-mean adjacency, Binet's formula converts the boundary
function into

$$
E(x)=\sum_{k\ge0}\gamma_k\varepsilon_k,
\qquad x=\sum_{k\ge0}\varepsilon_k2^k,
$$

where the $\gamma_k$ alternate, dominate their full tails, and have ratio
$-\varphi^{-2}$. The image is therefore a Cantor set with dimension
$\log2/(2\log\varphi)$. The nonzero coefficient tails are exactly the radial
singularity coefficients at primitive dyadic roots, giving a natural
boundary.

## Why this question is useful

Prior work determines the multiplicative-SFT object, its chain product,
leading entropy, and leading fractal dimensions. Those results do not by
themselves identify the bounded finite-size correction or all of its
subsequential values. The present question isolates that subleading object
and gives it an intrinsic $q$-adic state space.

The theorem also separates three notions that must not be conflated:

1. the leading dimension of the original multiplicative shift;
2. the dimension of the real boundary image $E(\mathbb Z_2)$;
3. ordinary Minkowski content over all real covering scales.

Only the first is prior-owned and only the second is proved here. The third is
not claimed.

## Frozen theorem output

For the frozen $q,A$,

$$
\operatorname{Acc}_{N\to\infty}(\log Z(N)-hN)=E_{A,q}(\mathbb Z_q),
$$

and

$$
\operatorname{Acc}_{N\to\infty}(Z(N)e^{-hN})
=\exp(E_{A,q}(\mathbb Z_q)).
$$

In the golden control,

$$
\dim_H E_{A,2}(\mathbb Z_2)
=\dim_B E_{A,2}(\mathbb Z_2)
=\frac{\log2}{2\log\varphi}.
$$

The ordinary generating function $G(z)=\sum_{N\ge0}E(N)z^N$ has the unit
circle as a natural boundary through dense nonzero Abelian/radial
singularities.

## Explicit non-goals

- no novelty claim for the multiplicative shift, chain product, Fibonacci
  counts, entropy, or leading Hausdorff/Minkowski dimensions;
- no theorem for nonprimitive $A$ without a separately proved variant;
- no ordinary Minkowski-content claim;
- no claim that $G$ is an Artin--Mazur zeta, determinant, or transfer trace;
- no claim that dense boundary singularities are isolated meromorphic poles;
- no target fitting, stochastic experiment, or numerical evidence used as a
  substitute for proof;
- no priority claim from failure to locate an exact published collision.

## Decision

Proceed as a `/tmp` preauthority candidate for independent proof, source, and
integrity review. No authority action follows from this brief.

