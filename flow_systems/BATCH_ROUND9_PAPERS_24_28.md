# Round 9 — Papers 24–28 complete-manuscript report

Date: 2026-08-28
Pipeline position: **ARS Stage 2 (`WRITE`) complete; Stage 2.5 (`INTEGRITY`) not started**
Roadmap position: **Route A only; Route B remains unauthorized**

## 1. Landed outcome

Round 9 converts the frozen Round-8 theorem and certificate spines into five
independently readable research manuscripts. Each package now contains a
LaTeX source, closed BibTeX bibliography, compiled PDF, manuscript audit,
reproduction path, limitations, Route-A interpretation, and the confirmed
publication declarations.

| Paper | Complete manuscript | Audited body | PDF | Cited sources | Final PDF SHA-256 |
|---|---|---:|---:|---:|---|
| P24 | [Congruence Trace Universality and the Limits of First-Jet Separation in Bianchi Holonomy](papers/24-bianchi-holonomy-flow/paper/paper.pdf) | 4,029 words | 12 pages | 7/7 | `e8dcfa74b967054a956521daa138a4cb397292c13674c19e1c03e218438759f1` |
| P25 | [Why a Unit-Roof Symbolic Determinant Does Not Transfer to the Physical Three-Disk Flow](papers/25-three-disk-scattering-flow/paper/paper.pdf) | 4,055 words | 12 pages | 8/8 | `608b669835f55c02bf5e43c570878728865e8659a58dbd23dae02dbf16dd101f` |
| P26 | [Exact Newform-Period Taxonomy for a Level-11 Time Change of the Modular Geodesic Flow](papers/26-level11-newform-time-change/paper/paper.pdf) | 4,210 words | 12 pages | 5/5 | `b2911495fff88a1e351c4b7cc65989f998df47822b3a2bae0db60b543c34d5aa` |
| P27 | [Renormalization Obstructions in Congruence and Homology Towers of Geodesic Flows](papers/27-congruence-inverse-limit-no-go/paper/paper.pdf) | 4,099 words | 12 pages | 5/5 | `540403e2cfb3c893822f3bcb80fb56e33bff00970f340df3dc9e6e8d2810d65a` |
| P28 | [An Exact Systole and Finite Enumeration Certificate for a Nonarithmetic Genus-Two Octagon](papers/28-bolza-magnetic-flow/paper/paper.pdf) | 5,127 words | 14 pages | 6/6 | `6bbda36564994ac8dcc16c962655867f6c427b6aeb19d7071922c6e07678e688` |

Aggregate manuscript output: **21,520 audited body words, 62 PDF pages, 31
closed bibliography entries, and five complete PDFs**. Citation style remains
`natbib` with `plainnat` numeric output, as previously confirmed.

## 2. Paper-level scientific progress

### P24 — universal theorem plus a scoped refinement

For a commutative ring, a non-zero-divisor `m`, and
`gamma=I+mA` in `SL_2(R)`, the paper proves

```text
(tr(gamma)^2-4)/m^2 = m^2 det(A)^2 - 4 det(A).
```

It also proves the level-conjugacy, inversion, and power laws of the first
congruence jet. The 11,481-matrix exact panel shows that the joint descriptor
refines 145 scalar values to 517 descriptors, but leaves 10,964 collision rows
and no singleton bucket. The result stops `D9` as a Gaussian-specific owner
mechanism. The mandatory canonical-control gate remains **2/3 INCOMPLETE**.

### P25 — an exact clock-ownership no-go theorem

In the equilateral no-eclipse regime `d>4a/sqrt(3)`, the physical period means
are proved to be

```text
T2/2 = d-2a,    T3/3 = d-sqrt(3)a.
```

Their gap proves that the physical roof is not cohomologous to a constant and
rules out every owner- and repetition-preserving scalar substitution
`z=exp(-cs)`. The replay has 2,241 rows across three geometries, 747 per
geometry. This theorem does not reject a genuine nonconstant-roof transfer
operator and does not equate a symbolic determinant with the exact quantum
multiple-scattering determinant.

### P26 — a complete finite exact taxonomy

The exact Schreier-homology model yields the real involution
`tau(x,y,z)=(-x,y+z,-z)` and period coordinate `k=2y+z`. Every one of the 138
frozen Hecke cycle-owner instances is classified: two full complex kernels,
two real-projection-only kernels, 134 true nonkernels, and zero unresolved
instances. The three predeclared group laws fail respectively 51/55, 51/55,
and 55/55 groups. This is a complete theorem for the frozen multiset, not a
full primitive census or global determinant.

### P27 — exact support/multiplicity renormalization costs

The residual-tower candidate has no periodic point and every fixed owner
escapes under the common physical clock. A separately registered genus-two
pure-homology cover is then proved to have degree `N^4`, deck order `N`,
`N^3` primitive lift components, and physical period `N ell(g)` for a
content-one owner. Of the four clock/multiplicity quadrants, only simultaneous
`1/N` time rescaling and `1/N^3` logarithmic normalization recovers the base
finite-panel factor. The positive identity is generic and nonresidual, hence
a proves-too-much calibrator rather than Route-A A2 evidence.

### P28 — a global systole theorem backed by a finite exact certificate

For the `alpha=pi/4` slice of Nazarenko's two-parameter octagon family at
`u=exp(-1/10)`, the paper proves

```text
sys(S) = 2 acosh(1/(2 exp(-1/5)-1)).
```

The primitive witness is `g0*g3`. A tile-chain theorem converts the frozen
geometric cutoff `Lambda=21/10` into a finite centre guard, and exact
polynomial `PSU(1,1)` states exhaust the resulting 18,533-element component
with 108,616 rejected boundary states. The 144 equality states are group
elements, not 144 conjugacy classes, owners, or geometric systoles. No Bolza
census, magnetic comparison, A2 evaluation, or Route-B audit was run.

## 3. Dynamics-system boundary retained

This manuscript round does not manufacture five new models. It consolidates
the five previously frozen continuous-time subtypes and their declared
initial restrictions:

1. a level-(3) Bianchi hyperbolic geodesic flow and an incomplete word-ball
   proxy;
2. an equilateral no-eclipse three-disk billiard at three frozen separations,
   plus a separately typed unit-roof symbolic suspension;
3. a positive newform time change of the geodesic flow on `Y_0(11)`;
4. a normal residual geodesic-flow tower and a distinct nonresidual homology
   cover calibrator;
5. a nonarithmetic genus-two hyperbolic control surface, without a magnetic
   comparison in this round.

The coverage count therefore remains five main dynamical subtypes, 12 frozen
geometric/physical parameter instances, and seven `q`-symbol analytic
calibrators. These 19 frozen model instances are not treated as 19 independent
statistical samples.

## 4. Independent review and repair

Every paper received a read-only reviewer who had not authored that paper.
Initial findings were:

| Paper | Blocker | Major | Minor | Disposition |
|---|---:|---:|---:|---|
| P24 | 0 | 0 | 1 | non-zero-divisor scope restored in the jet definition and theorem |
| P25 | 0 | 0 | 2 | replay denominator wording and no-eclipse/full-shift scope corrected |
| P26 | 0 | 0 | 0 | CLEAN |
| P27 | 0 | 0 | 1 | cosmetic bibliography underfull line removed |
| P28 | 0 | 0 | 4 | family slice, source locator, author metadata, and display-only dependency corrected |

All eight Minors are closed. No theorem value, research artifact, frozen
candidate, or Route-A verdict changed. Post-repair compilation logs contain
zero LaTeX/BibTeX warnings, undefined citations/references, missing glyphs,
overfull boxes, or underfull boxes.

## 5. Reproducibility dashboard

- historical unit tests: **372/372 PASS** (`71+65+74+58+104`);
- Round-8 theorem/certificate replays: **80/80 PASS**
  (`14+12+18+12+24`);
- default reproduction mode: verify-only for all five packages;
- deterministic isolated rebuilds: **5/5 PASS**;
- P28 exact state-tree replay:
  `c30beebdd2e832d9375f55f1eab700868b7b967dfb5ee43fcecc0ba5f60919ac`
  in both builds;
- Round-9 structural/citation/PDF audit: **5/5 PASS**, zero warnings;
- citation closure: **31/31 unique cited records**, zero missing and zero
  orphan entries;
- target-data firewall: no prime table, Riemann-zero table, or resonance table
  enters a candidate definition, parameter choice, proof, or cutoff.

## 6. Route-A correspondence and checkpoint

Round 9 is a writing/completion round, so it does not alter the scientific
Route-A tuples established in Round 8:

| Paper | Route-A record after Round 9 | Reason no promotion occurs |
|---|---|---|
| P24 | `ROUTE_A_EXPLORATORY` | A0 controls remain 2/3; no complete owner or ideal map |
| P25 | symbolic control `ROUTE_A_REJECTED`; physical flow `UNASSIGNED` | scalar transfer refuted; genuine physical determinant absent |
| P26 | `ROUTE_A_EXPLORATORY` | exact finite taxonomy, no complete primitive product or A2 determinant |
| P27 | `ROUTE_A_REJECTED` | residual owner fails A1; positive calibrator fails arithmetic specificity |
| P28 | `ROUTE_A_EXPLORATORY` control theorem | systole/cutoff certified, matched census and A2 not run |

Typed records remain 5/5, positive arithmetic candidates reaching A2 remain
0/5, and Route-B invocations remain 0/5. The five manuscripts close **ARS
Stage 2 only**. Entry to Stage 2.5 requires explicit user confirmation after
this dashboard; Stage 2.5 has not been started or passed.
