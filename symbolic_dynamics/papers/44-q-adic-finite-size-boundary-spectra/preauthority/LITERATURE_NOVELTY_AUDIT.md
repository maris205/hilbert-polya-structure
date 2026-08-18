# Literature and novelty audit

## Audit date, question, and evidence ceiling

Search date: `2026-08-18 UTC`.

The audit asked whether a primary source already owns any of the following
same-object statements:

1. the exact increment
   $\log Z(N)-\log Z(N-1)=c_{\nu_q(N)}$;
2. a continuous real-valued extension of $\log Z(N)-hN$ to $\mathbb Z_q$;
3. equality between its complete accumulation set and the image of that
   extension;
4. the golden boundary image's strong separation and dimension
   $\log2/(2\log\varphi)$;
5. dense nonzero radial singularities of the corresponding remainder
   generating function.

Queries combined `multiplicative golden mean`, `multiplicative shift`,
`finite prefix`, `finite-size correction`, `q-adic remainder`, `accumulation
set`, `boundary complexity`, `Fibonacci product`, `Lambert series`, `radial
singularity`, and `natural boundary`. Primary publisher, DOI, arXiv, author,
and institutional records were preferred.

Negative search evidence is assigned grade `B-` at best. It is not proof of
novelty or priority.

## Primary-source chronology and ownership

### 2012: multiplicative golden-mean object and leading counts

A.-H. Fan, L. Liao, and J.-H. Ma, *Level sets of multiple ergodic averages*,
*Monatshefte für Mathematik* 168 (2012), 17--26,
[DOI 10.1007/s00605-011-0358-5](https://doi.org/10.1007/s00605-011-0358-5).

Assigned ownership: the multiplicative golden-mean setting, Fibonacci chain
counts, and leading dimension calculations. These receive zero novelty
credit.

### 2012: general multiplicative-shift dimension framework

R. Kenyon, Y. Peres, and B. Solomyak, *Hausdorff dimension for fractals
invariant under the multiplicative integers*, *Ergodic Theory and Dynamical
Systems* 32 (2012), 1567--1584,
[DOI 10.1017/S0143385711000538](https://doi.org/10.1017/S0143385711000538).

Assigned ownership: general multiplicative subshift/SFT chain framework and
leading Hausdorff/Minkowski theory. The source object and leading entropy or
dimension are not candidate contributions.

### 2012 and earlier: digital-summatory neighbors

M. G. Madritsch, *The summatory function of q-additive functions on
pseudo-polynomial sequences*, *Journal de théorie des nombres de Bordeaux*
24 (2012), 153--171,
[DOI 10.5802/jtnb.791](https://doi.org/10.5802/jtnb.791), surveys and extends
the Delange/digital-sum tradition.

Assigned ownership: general digit-summatory fluctuation methodology. Its
periodic real fluctuations are a method neighbor, not an exact collision
with the valuation-increment sequence, bounded inverse-limit remainder, or
multiplicative-SFT boundary image studied here.

### 2013/2019: direct multiplicative pattern-count framework

J.-C. Ban, W.-G. Hu, and S.-S. Lin, *Pattern generation problems arising in
multiplicative integer systems*, arXiv:1207.7154v3; *Ergodic Theory and
Dynamical Systems* 39 (2019), 1234--1260,
[DOI 10.1017/etds.2017.74](https://doi.org/10.1017/etds.2017.74).

Assigned ownership: admissible-chain decomposition, densities of chains of
each length, direct pattern products, entropy, and leading dimension/error
control for multiplicative integer systems. These ingredients receive zero
novelty credit here.

### 2023: boundary complexity and surface entropy

J.-C. Ban, W.-G. Hu, and G.-Y. Lai, *Boundary complexity and surface entropy
of 2-multiplicative integer systems on $\mathbb N^d$*, *Journal of
Mathematical Physics* 64 (2023), 062704,
[DOI 10.1063/5.0118652](https://doi.org/10.1063/5.0118652),
[arXiv:2210.09115](https://arxiv.org/abs/2210.09115).

Assigned ownership: boundary-complexity and surface-entropy concepts,
speed-dependent boundary limits, and their leading formulas.

The journal metadata were verified at DOI 10.1063/5.0118652. The theorem text
used below was checked only in the author manuscript arXiv:2210.09115v1:
Theorem 3.3(2) and Remark 3.4 state, for the same one-dimensional
multiplicative SFT at $N=p^{kn}$,

$$
\log |\mathcal P([1,p^{kn}],X^p_{\Sigma_A})|-p^{kn}h
=-(1-p^{-1})\log(\lambda_A)kn+o(kn).
$$

That displayed specialization cannot hold under the stated quantifiers. For
the full $d$-shift $A=J_d$, the exact chain product is $Z(N)=d^N$, so the
left side is identically zero, whereas the displayed main term is nonzero
for $d>1$. More generally, the exact increment and summation-by-parts proof
in this package gives a bounded order-one remainder and gives zero at every
cutoff for that full-shift control. Paper 44 therefore treats the author
manuscript's one-dimensional subleading formula as a same-object statement
requiring correction, not as novelty ownership and not as an exact duplicate.
The version-of-record theorem text and any publisher erratum or correction
notice have not been checked line by line; no claim here transfers that
displayed formula to the version of record. The eligible claim is the
corrected exact remainder, its $q$-adic completion, and the golden closure
after all of Ban--Hu--Lai's valid leading/boundary ownership is subtracted.

### 2025: affine multiplicative-shift dimensions

J.-C. Ban, W.-G. Hu, G.-Y. Lai, and L. Liao, *Hausdorff dimensions of affine
multiplicative shifts*, *Advances in Mathematics* 471 (2025), 110266,
[DOI 10.1016/j.aim.2025.110266](https://doi.org/10.1016/j.aim.2025.110266).

Assigned ownership: recent leading Hausdorff/Minkowski dimension theory for
a broader affine family. It further prevents leading fractal dimension from
being used as candidate novelty.

## Known, derived, and eligible components

| Component | Status | Candidate novelty credit |
|---|---|---:|
| multiplicative-SFT definition | primary-owned | 0 |
| $q$-adic chain partition | primary-owned/elementary | 0 |
| exact product of $W_\ell$ over chains | primary-owned | 0 |
| golden Fibonacci word counts | primary-owned | 0 |
| leading entropy and leading shift dimensions | primary-owned | 0 |
| boundary-complexity terminology | primary-owned | 0 |
| direct admissible-chain pattern product and leading error control | Ban--Hu--Lin, primary-owned | 0 |
| Ban--Hu--Lai author-manuscript $d=1$, $N=p^{kn}$ linear subleading formula | contradicted by the full-shift exact control; corrected here; version-of-record/erratum text not line-checked | 0 as prior ownership |
| exact valuation increment | locally proved finite-size sharpening | eligible only in package |
| continuous $\mathbb Z_q$ order-one remainder | no exact hit found | eligible |
| complete accumulation image | no exact hit found | eligible |
| golden strong-separated boundary image and dimension | no exact hit found | eligible |
| dense radial-singularity corollary | no exact hit found; elementary once coefficients are known | minor |
| ordinary Minkowski-content nonexistence | not proved | excluded |

## Exact collision result

The bounded search did not locate a primary source stating the same theorem
package with the frozen quantifiers. This is a reproducible absence result,
not a priority proof.

`STOP_DUPLICATE` applies if a primary source is found that already gives the
exact $\mathbb Z_q$ extension and complete accumulation image for these
multiplicative-SFT prefix counts, or gives the golden strong-separation and
dimension as a direct same-object theorem. Discovery of only the chain
product, entropy, or a generic $q$-adic/digital lemma does not create an exact
collision, but must still be cited as method ownership.

## Internal Papers 1--43 collision audit

| Internal cluster | Shared surface | Exact collision result |
|---|---|---|
| P14--P16 | tensors, markers, cycle indices | different primitives and no prefix-boundary map |
| P19--P25 | traces, determinants, recurrence ledgers | no same source or finite-size theorem |
| P26 | pure-power selector syntax | no multiplicative-SFT boundary result |
| P27--P30 | incidence/Gram/free-UFD operators | different object and observable |
| P31 | additive semiring verification | no valuation-chain remainder |
| P38 | Bass--Serre tree collapse | no same finite prefix census |
| P43 | squarefree factor periodic rigidity | non-SFT source and periodic-factor ledger, not prefix complexity |

No same-object/result collision was found. Generic finite-size, tensor, or
natural-boundary vocabulary receives no internal inheritance credit.

## Anti-salami boundary with proposed Papers 45--48

- P45 studies nonnormal prime-exponent retraction fibers, Weyl laws, and
  similarity; P44 has no operator or prime-fiber geometry.
- P46 studies additive edges $m+n=2^a$, a $v_2$ direct sum, and cycle
  equations; P44 studies prefix-count valuation increments.
- P47 studies Egyptian homogeneous edges and a Mordell--Tornheim trace;
  P44 has neither arithmetic adjacency nor a trace ideal.
- P48 studies positional no-carry adjacency and all-radix Schatten
  thresholds; P44's base expansion records cutoff residues, not digitwise
  edge compatibility.

After deleting shared summability, digit, and finite-size vocabulary, the
exact $\mathbb Z_q$ accumulation theorem remains unique to P44.

## Novelty scorecard

| Axis | Conservative score out of 10 | Reason |
|---|---:|---|
| source/object novelty | 0 | primary-owned multiplicative SFT |
| leading asymptotic novelty | 0 | entropy/dimensions primary-owned |
| exact subleading theorem | 6 | coherent same-object delta; no exact hit found |
| golden geometric closure | 6 | all-level separation and exact dimension |
| natural-boundary corollary | 2 | short consequence, not anchor |
| standalone package after subtraction | 6 | survives delete-shared-method test |

## Decision

`PROCEED_TO_INDEPENDENT_PREAUTHORITY_DA_WITH_FIREWALL`.

Do not advertise first discovery. If an exact primary collision is found,
retain the package as an internal derivation/evaluator note and apply
`STOP_DUPLICATE` to the standalone position.

## Chronology statement

Every cited source, the Phase-2 source subtraction, and the local theorem
outline were known before this package freeze. The freeze confers no
prospective, outcome-independent, novelty, priority, ranking, or
authorization credit.
