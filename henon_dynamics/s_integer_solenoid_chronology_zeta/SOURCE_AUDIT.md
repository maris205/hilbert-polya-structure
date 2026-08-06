# Primary-source and novelty audit

Date: 2026-08-06

## Foundational local source

The requested starting point was the original project manuscript
`docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`:

```text
SHA-256 23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9
```

It motivates the conservative-map requirement and the insistence on a genuine
chronological clock.  Its fitted Hénon parameter, formal continuous limit,
quartic confinement, numerical zero comparisons, and quantum/dissipative
solvers are not assumptions of HCS-C14.  The solenoid skew product is a
breadth-first change of dynamical category, not a derivation or quantization
of that manuscript's map.

## Source-locked results

### \(S\)-integer periodic-point formula

Chothi--Everest--Ward construct dynamical systems by dualizing
\(S\)-integer modules and express periodic counts through local absolute
values. This project uses that product-formula mechanism, not its scalar
examples as a novelty claim.

- V. Chothi, G. Everest, and T. Ward, *S-integer dynamical systems:
  periodic points*, J. Reine Angew. Math. 489 (1997), 99--132.
  [Repository record and manuscript](https://ueaeprints.uea.ac.uk/id/eprint/18601/),
  [DOI](https://doi.org/10.1515/crll.1997.489.99).

For \(R=\mathbb Z[1/2]\) and a matrix \(M\in GL_2(R)\), the exact formula

\[
\#\operatorname{Fix}(\widehat{M^{\mathsf T}})
=|\det(I-M)|_\infty|\det(I-M)|_2
\]

also follows directly by dualizing the cokernel and applying Smith normal form
over the localized PID \(R\).

### General finite-dimensional solenoids

Miles gives periodic-point formulas for endomorphisms of finite-dimensional
solenoids and related compact groups. Bell--Miles--Ward explicitly use this
result as their higher-dimensional starting point.

- R. Miles, *Periodic points of endomorphisms on solenoids and related
  groups*, Bull. Lond. Math. Soc. 40 (2008), 696--704.
  [DOI](https://doi.org/10.1112/blms/bdn052).

A more recent rank-two treatment gives explicit subgroup-index and periodic
point formulas for rational matrix endomorphisms.  It confirms that the
cokernel/odd-part step is prior theory rather than the novelty claim here.

- K. Y. Ha and J. B. Lee, *Rank-two solenoidal endomorphisms*, Topol. Methods
  Nonlinear Anal. 61 (2023), 291--329.
  [DOI](https://doi.org/10.12775/TMNA.2022.063).

### Entropy and local places

The archimedean/\(p\)-adic decomposition of entropy for solenoidal
automorphisms is established background.

- D. Lind and T. Ward, *Automorphisms of solenoids and \(p\)-adic entropy*,
  Ergodic Theory Dynam. Systems 8 (1988), 411--419.
  [DOI](https://doi.org/10.1017/S0143385700004545).

### Natural-boundary theorem

The only external analytic theorem used in the main result is applied to a
**single** return automorphism \(\alpha_{M_w}\), never directly to the full
switching skew product.

- J. Bell, R. Miles, and T. Ward, *Towards a Pólya--Carlson dichotomy for
  algebraic dynamics*, Indag. Math. 25 (2014), 652--668.
  [arXiv manuscript](https://arxiv.org/abs/1307.2369),
  [DOI](https://doi.org/10.1016/j.indag.2014.04.005).

Theorem 15 says, under the finite-place and no-archimedean-unit-circle
hypotheses, that the dynamical zeta of a finite-dimensional connected compact
group automorphism is rational unless a finite-place eigenvalue has absolute
value \(1\); in the latter case the convergence circle is a natural boundary.
Example 18 treats the two-dimensional cat-map setting explicitly.

Byszewski--Cornelissen--Houben place \(S\)-integer and other compact-group
fixed-point sequences in the broader finite-adelically-distorted framework
and prove zeta dichotomies and orbit-counting results.  This is a close
framework prior, but it does not supply the switching chronology theorem or
the local-factor/full-zeta contrast proved here.

- J. Byszewski, G. Cornelissen, and M. Houben, *Dynamics of endomorphisms of
  algebraic groups and related systems*, arXiv:2209.00085 (2022).
  [arXiv](https://arxiv.org/abs/2209.00085).

For the period-five return \(M_{\texttt{ababb}}\), the characteristic
polynomial reduces modulo \(2\) to \(x(x+1)\), so Hensel lifting supplies one
\(2\)-adic unit root and one nonunit root. Both real eigenvalues have modulus
greater than \(1\), and the determinant is \(8^5\). Thus the theorem applies
with return-variable radius \(8^{-5}\), or base-orbit radius \(1/8\) after
\(u=z^5\).

## Skew-product prior-art boundary

For Ruelle-expanding generators, ordered semigroup actions, their skew
products, thermodynamic formalism, and associated zeta functions are
established structures.

- M. Carvalho, F. B. Rodrigues, and P. Varandas, *Semigroup actions of
  expanding maps*, J. Stat. Phys. 166 (2017), 114--136.
  [arXiv](https://arxiv.org/abs/1601.04275),
  [DOI](https://doi.org/10.1007/s10955-016-1697-3).

Accordingly, neither “use a full-shift skew product” nor “ordered matrix
products matter” is claimed as new. Likewise, golden-mean/Lucas counting is
standard and already appears as an internal control in HCS-C13B.

## Internal collision audit

- HCS-C01 concerns a two-letter **Hénon-parameter** cocycle and common
  hyperbolicity. HCS-C14 instead uses compact \(S\)-solenoid automorphisms and
  intrinsic local fixed-point indices.
- HCS-C03 and C12A warn that finite local rationality can be universal and
  that arithmetic and chronological clocks must remain separate. HCS-C14
  uses one physical shift clock and an infinite valuation tower, not a
  Frobenius-degree surrogate.
- HCS-C13B contains a golden-mean/Fibonacci symbolic series. The new scoped
  claim is the iff link between the cyclic no-\(aa\) language and the parity of
  a solenoidal fixed-point determinant, together with its analytic-type split.
- HCS-C13P/G do not apply: HCS-C14 uses physical symbolic time and an indirect
  fixed-point divisor, not a short-clock polynomial energy coefficient.

No implemented solenoid cocycle was found in the repository.

## Novelty ruling

YELLOW, not GREEN.

The exact combination below was not located in the directed source audit:

1. a noncommuting \(S\)-integer two-generator cocycle;
2. an exact cyclic-language classification of active local valuations;
3. same-Parikh primitive returns with rational versus natural-boundary zeta;
4. a full switching zeta whose first circle is nevertheless meromorphically
   crossed with a zero-free annulus.

This is a scoped novelty assessment, not an exhaustive literature theorem.
The manuscript must foreground the established Bell--Miles--Ward theorem and
must not imply that individual natural-boundary factors force a natural
boundary for their infinite product.
