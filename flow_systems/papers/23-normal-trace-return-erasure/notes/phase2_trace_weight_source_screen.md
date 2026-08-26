# Paper 23 Phase-2 trace-weight and novelty screen

Date: **2026-08-24**

Status: **TECHNICAL NOTE CANDIDATE / PREFER MERGE INTO PAPER 8**

This report is a bounded source, owner, and theorem-shape audit.  It does not
authorize a manuscript, transfer a result to the non-Hausdorff packet, or
advance Route A or B.

## 1. Search protocol

Search date: **2026-08-24**.

Search surfaces included Acta Mathematica/DOI, Springer, publisher and author
book records, arXiv, journal full text, and the complete local Paper-8 proof
package.  Query families included:

```text
Pedersen Takesaki Radon Nikodym normal semifinite weight central derivative
normal semifinite tracial weight type I direct integral central density
decomposable operators Takesaki IV.7.10
translation invariant density Haar uniqueness circle
translation invariant Fourier coefficients uniqueness
Plancherel weight crossed product coefficient zero trace
```

Only primary papers, authoritative monographs, official lecture notes, and
publisher records with exact theorem/page locators were used.  Results about
finite tracial states only, lower-semicontinuous `C*` traces, type-III/KMS
weights, or an owner other than the fixed Paper-8 regular algebra were
excluded from the load-bearing chain.

## 2. Source matrix

| Source | Exact use | Verification |
|---|---|---|
| G. K. Pedersen, M. Takesaki, *The Radon--Nikodym theorem for von Neumann algebras*, Acta Math. 130 (1973), 53--87, DOI `10.1007/BF02392262` | pp. 62--63, 71--72, and 82--83 classify normal semifinite weights through affiliated derivatives; Theorem 7.4 is the semifinite-trace form | **VERIFIED** |
| M. Takesaki, *Theory of Operator Algebras I*, Theorem IV.7.10, p. 259, DOI `10.1007/978-1-4612-6188-9` | direct-integral/decomposable realization and hence the center of `L^infinity(T) bar-tensor B(H)` | **VERIFIED** |
| G. Folland, *A Course in Abstract Harmonic Analysis*, Theorem 2.20, p. 44 | uniqueness of Haar measure up to positive scale | **VERIFIED** |
| R. Laugesen, *Harmonic Analysis Lecture Notes*, arXiv `0903.3845v2`, pp. 10 and 22 | circle Fourier coefficients and uniqueness | **VERIFIED** |
| J. Renault, *Continuity of the dual Haar measure*, C. R. Math. 359 (2021), 415--419, DOI `10.5802/crmath.183` | dual-Haar normalization and Plancherel-weight comparator | **VERIFIED AS NEAR NEIGHBOR** |
| V. Jones, *Von Neumann Algebras* lecture notes (2009), pp. 15--16 and 43--44 | `vN(Z) ~= L^infinity(T)` and normality; supports the diffuse-versus-point-evaluation boundary | **VERIFIED AS AUTHORITATIVE NOTES** |
| C. Bourne, A. Rennie, *Chern numbers, localisation and the bulk-edge correspondence...*, MPAG 21 (2018), article 16, DOI `10.1007/s11040-018-9274-4` | invariant-measure construction of coefficient-at-zero semifinite traces | **VERIFIED AS APPLICATION COMPARATOR** |

Primary links:

- <https://doi.org/10.1007/BF02392262>
- <https://link.springer.com/book/10.1007/978-1-4612-6188-9>
- <https://www.routledge.com/A-Course-in-Abstract-Harmonic-Analysis/Folland/p/book/9781032922218>
- <https://arxiv.org/abs/0903.3845>
- <https://doi.org/10.5802/crmath.183>
- <https://math.berkeley.edu/~vfr/VonNeumann2009.pdf>
- <https://doi.org/10.1007/s11040-018-9274-4>

## 3. Surviving theorem package

Freeze only the Paper-8 proxy owner

```text
M = L^infinity(T,m) bar-tensor B(H),
tau_0(x) = integral_T Tr(x(theta)) dm(theta).
```

Every normal semifinite tracial weight on `M` has a unique representation

```text
psi_h(x) = integral_T h(theta) Tr(x(theta)) dm(theta),
```

where `h` is a nonnegative measurable central density, finite almost
everywhere.  It is faithful exactly when `h>0` almost everywhere.  This is a
direct consequence of Pedersen--Takesaki plus tracial invariance under inner
automorphisms, which forces the affiliated derivative into `Z(M)`.

Freeze the center-moving action

```text
(alpha_s x)(theta) = x(theta-s),          s in T.
```

Then the following are equivalent:

1. `psi_h o alpha_s = psi_h` for every `s in T`;
2. `h` is translation invariant almost everywhere;
3. `h` is almost everywhere constant;
4. `psi_h=c tau_0` for a finite constant `c>=0`.

For a possibly unbounded but a.e.-finite `h`, translation invariance may be
tested on the bounded injective transform `h/(1+h)`; Fourier uniqueness then
forces constancy.  The faithful normal semifinite case is `c>0`.

On the exact Paper-8 trace domain, its established fibre formula

```text
Tr(lambda_L(a_f)(theta))
  = L sum_(r in Z) f(rL) exp(i r theta)
```

therefore yields

```text
(c tau_0)(lambda_L(a_f)) = c L f(0).
```

Thus full circle-translation invariance erases every nonzero return mode.
Nonconstant center densities are normal semifinite tracial weights and may
retain selected Fourier returns, but they necessarily break this full
translation invariance.  The converse “return erasure implies translation
invariance” is not asserted for the whole semifinite class: it requires a
common finite-weight/`L^1` domain on which all Fourier coefficients exist and
a separate uniqueness argument.

## 4. Load-bearing boundaries

- “Translation invariant” must mean every circle translation, or at least an
  explicitly frozen dense irrational generator.  Invariance under a finite
  rational rotation permits nonconstant periodic densities.
- The action must actually move the center.  An action trivial on the center
  leaves every density invariant and gives no uniqueness.
- The return formula remains restricted to Paper 8's trace-class/`L^1`
  domains; it is not an identity for arbitrary unbounded kernels.
- Point characters on `C(T)` do not become normal weights on diffuse
  `L^infinity(T,m)`.
- Nothing here transfers a weight, Haar system, or completion to the actual
  non-Hausdorff packet.

## 5. Maximum-prior and disposition

The classification is classical.  The local increment is the exact
implication from center-moving translation invariance to Paper 8's
return-erasing trace formula.  That is mathematically clean but too short and
too dependent on Paper 8 to justify a full standalone paper without an
additional nonroutine owner.

```text
NORMAL_SEMIFINITE_TRACIAL_WEIGHT_CLASSIFICATION=PASS
FULL_TRANSLATION_INVARIANCE_IFF_SCALAR_HAAR_WEIGHT=PASS
POSITIVE_SCALAR_IFF_FNS_WITHIN_THIS_FAMILY=PASS
NONZERO_RETURN_ERASURE_ON_FROZEN_DOMAIN=PASS
RETURN_ERASURE_CONVERSE=NOT_PROVED_WITHOUT_ADDITIONAL_DOMAIN_HYPOTHESES
NORMALITY_ALONE_FORCES_ERASURE=REFUTED
STANDALONE_FULL_PAPER_NOVELTY=FAIL
DISPOSITION=TECHNICAL_NOTE_OR_MERGE_INTO_PAPER_8
MANUSCRIPT=NOT_AUTHORIZED
ROUTE_ADVANCEMENT=NONE
```

The bounded search was sufficient to classify the contribution, but it is
not a global claim that no other paper has ever stated this exact corollary.
