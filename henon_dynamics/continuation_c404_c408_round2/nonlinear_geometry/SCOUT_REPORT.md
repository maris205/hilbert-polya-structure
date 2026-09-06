# Nonlinear geometry scout: continuation C404–C408, round 2

Date: 2026-09-06. Baseline supplied by the parent: `ae2fdc72c865a61369ef74d03d5b266a94ace86d`.
Scope: this directory only; no C-number, manuscript, global ledger, Git operation,
or modification of the frozen first scout round.

**Admission result: 0 paper contracts.** Two candidates were examined. The first
is covered by established theory. The second has a genuine unresolved all-period
boundary problem; a tempting formula is false. The proved open-stratum formula
and a five-period counterexample are not being split into papers.

## 1. Elliptic-translation return divisors

Object: a characteristic-zero elliptic surface over a smooth base curve, with
zero section O and a non-torsion section P; the map is translation by P on smooth
fibres. Clock: multiplication index n. Observable: the divisor
`D_n = [n]P^*(O)` on the **base**, and its Möbius transform. This is not a finite
count of points in phase space: a torsion-specialization fibre has an entire
curve of periodic points. Lyness/QRT supplied the motivating concrete family.

The formal local-entry law, its primitive-divisor consequence, and the
intersection-theoretic periodic-fibre count already have direct owners.
Thus a proposal consisting of height growth plus Möbius inversion does not
provide a new lemma. An exact parameter-jump classification beyond those
inputs was not obtained. This candidate is `REJECT_CLASSICAL_OWNER`.

Primary-source checks actually performed:

- Ingram, Mahé, Silverman, Stange and Streng, *Algebraic divisibility sequences
  over function fields*, 2012: the published PDF's Theorem 1.7 and Lemma 5.6
  were read, including the formal-group argument. In characteristic zero,
  the valuation at a place is constant at multiples of its first appearance
  and vanishes at other indices. Under the paper's nonconstant/non-torsion
  hypotheses, sufficiently late terms have primitive valuations.
  [Published original](https://doi.org/10.1017/S1446788712000092).
- Duistermaat, *Discrete integrable systems: QRT maps and elliptic surfaces*,
  2010: author-institution metadata, the library table of contents, and indexed
  original-book introductory passages were inspected. They explicitly identify
  section-intersection numbers as periodic-fibre counts; Chapters 7 and 11.4
  cover those counts, reducible-fibre contributions and Lyness. The publisher
  chapter could not be opened, so **no full-chapter/proof reading is claimed**.
  [Author institution](https://research-portal.uu.nl/en/publications/discrete-integrable-systems-qrt-maps-and-elliptic-surfaces/),
  [library contents](https://toc.library.ethz.ch/objects/pdf/e01_978-1-4419-7116-6_01.pdf).
- Naskręcki's 2016 paper and Naskręcki–Streng's 2020 constant-j paper were
  discovered through primary metadata/abstracts; they further rule out treating
  old uniform-Zsigmondy questions as automatically open. Their proofs were not
  used or represented as read.
  [2016 primary metadata](https://research-information.bris.ac.uk/en/publications/bb2a5d08-0ec2-4193-abf2-ac44f7a08585/),
  [2020 article](https://doi.org/10.1016/j.jnt.2019.12.002).

## 2. Rank-two cluster-type return schemes

Full proposed family:

`F_{k,c}(x,y) = (y,(c+y^k)/x)`, with integer `k >= 3` and `c in C`.

Clock: every integer `n >= 1`. Domain: periodic trajectories for which **every**
coordinate in the cycle is nonzero. Observable: the scheme length, not the
number of distinct points, of

`A_{k,c,n}[(x_0 ... x_{n-1})^{-1}]`,

where

`A_{k,c,n} = C[x_0,...,x_{n-1}] /
 (x_i^k+c-x_{i-1}x_{i+1}: i mod n)`.

The repeated-neighbour conventions for n=1 and n=2 are literal. This localized
scheme is identified with the fixed scheme on the stated rational-map domain
by recursively eliminating coordinates; invertibility makes each elimination
valid. A compactification's fixed scheme is a different object.

### Proved elementary stratum, not sufficient for paper admission

Each equation has leading monomial `x_i^k` in a degree order. These leading
monomials are pairwise coprime, so the equations form a Gröbner basis and the
whole cyclic algebra has length `k^n` for every c. This also precludes
positive-dimensional cyclic components.

If `c != 0` and a cyclic solution has `x_i=0`, its neighbours satisfy

`x_{i-1}^k = x_{i+1}^k = -c`, and `x_{i-1}x_{i+1}=c`.

Consequently `c^k=c^2`. Thus, for the complete open parameter stratum

`c != 0` and `c^(k-2) != 1`,

the localized scheme has length **exactly `k^n` for every n**. The exceptional
condition is genuine: if `c^(k-2)=1`, then `(0,t,c/t)`, `t^k=-c`, is a
three-period cyclic solution outside the domain. At c=0 the map is monomial
and belongs to an already-owned type. The short open-stratum argument does
not settle the full proposed family and is not admitted separately.

### Closest primary owner and the missing increment

Grigorev, Kalidindi, Quintero Santander and Roeder,
*Complex dynamics perspective for birational maps of the plane arising from
cluster algebra mutations*, arXiv:2607.08125v2, revised 6 August 2026, studies
the rank-two mutation composition; on the diagonal it equals `F_{k,1}^2`.
The introduction, Sections 5.3–5.4 and the relevant Section 6 statements were
actually read. The stable surface construction, Picard action, dynamical
degrees and entropy are direct prior inputs. Remark 5.13 explicitly warns
that these stable maps are not surface automorphisms made regular by finitely
many blowups. None of those results supplies the needed localization length
without further boundary work. No exact all-period torus-count theorem was
found in the inspected portions; this is a bounded search conclusion, not
a global novelty certificate.
[Primary original, v2](https://arxiv.org/html/2607.08125v2).

The required new lemma would classify all zero-pattern local multiplicities
on the confinement locus `c^(k-2)=1`, for all k and n, and prove the resulting
localized count. That lemma has **not** been established. Using only the
Picard trace, or extrapolating the following small values, would be invalid.

### Decisive checks and counterexample

Characteristic-zero saturation with Singular produced:

| k | n | whole cyclic length | localized torus length |
|---:|---:|---:|---:|
| 3 | 1 | 3 | 3 |
| 3 | 2 | 9 | 5 |
| 3 | 3 | 27 | 18 |
| 3 | 4 | 81 | 45 |
| 3 | 5 | 243 | 123 |
| 4 | 1 | 4 | 4 |
| 4 | 2 | 16 | 16 |
| 4 | 3 | 64 | 52 |
| 4 | 4 | 256 | 192 |

These values fit a trace recurrence with parity/period-four corrections.
That tempting extrapolation fails at **k=6,n=5**. The exact argument in
[PARTIAL_RESULTS.md](PARTIAL_RESULTS.md) gives

`N_{6,1,5} = 6666`, while that fit predicts `6726`.

The difference consists of sixty boundary double points arising from
`(0,i,u,-u,-i)`, `u^6+i*u+1=0`, their sign-conjugates and cyclic shifts.
[cluster_boundary_resonance.py](cluster_boundary_resonance.py) checks the
equations, invertible implicit-function minor, zero first derivative and
nonzero second derivative exactly. This is local algebra plus the written
finite decomposition, **not** an independent exhaustive 7776-dimensional
Gröbner census.

One supplementary computation over characteristic 32003 returned length 320
for k=3,n=6; it is not used as a characteristic-zero proof. The attempted
QQ computation k=4,n=5 was stopped after approximately five minutes without
an answer. No value is asserted for that unfinished computation. No further
census or all-period extrapolation is planned in this scout.

Candidate status: `HOLD_UNPROVED_ALL_PERIOD_BOUNDARY_CLASSIFICATION`.
There is no admitted contract and no proposed low-period replacement paper.

## Reproduction and process boundaries

- `Singular -q cluster_periodic_saturation.sing`: the nine QQ rows above.
- `python cluster_boundary_resonance.py`: exact local double-point certificate
  and the arithmetic of the separately proved boundary decomposition.
- `timeout 60s Singular -q cluster_modular_probe.sing`: finite-characteristic
  supplementary check only.

The initial modular probe had a library-name collision (`product`); it was
fixed to `cycleProduct` before the successful run. The discarded QQ k=4,n=5
call is no longer in the bounded reproducible scout script.

Skills used within the authorized scope: research-lit, novelty-check,
idea-creator, proof-writer and the ARS source-verification/retrieval guidance.
The batch's current-team instructions override old external-model/ML quotas;
no external review API, GPU job, source upload or claim of human reading was
made. Local Zotero/Obsidian and a relevant local paper corpus were unavailable,
so primary-web retrieval was used. These constraints influenced the outcome:
owner-heavy and unfinished claims were not promoted to papers.
