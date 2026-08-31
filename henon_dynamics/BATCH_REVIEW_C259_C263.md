# Batch review — HCS-C259 through HCS-C263

## Release decision

All five independent Route-A papers are release-complete from the common
baseline `98782afe1e754c311ad0736f72ce09dcc7c85c77`.  Each package has 27
content-addressed payload files plus a self-excluded release manifest, three
substantively different paper rounds, two fresh deterministic builds per
round at `SOURCE_DATE_EPOCH=1788048000`, embedded/subsetted fonts, clean
settled logs, and a page-by-page visual audit.

The common evaluator is `flow_systems/skills/route-a-evaluator.md` v0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
All forbidden scope flags are false and the common firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Five theorem-scale advances

### HCS-C259 — heterogeneous Kuramoto locking on weighted trees

The unique tree cut flow gives the exact existence criterion
`|F_e|<=K_e`.  In the strict chamber there are exactly `2^(N-1)` rotation-
quotient equilibria; with `s` saturated edges there are `2^(N-1-s)` merged
branches and reduced nullity `s`.  The reduced Hessian is congruent to the
diagonal edge-cosine form, so its Morse index is the number of negative
cosines and the all-positive branch is the unique stable branch.

- exhaustive receipt: all 18,248 labeled Prüfer trees for `N=2,...,7`;
- regimes: 6,082 strict, 6,083 saturated, 6,083 violated;
- independent checker: 477,330 assertions; SymPy: 261;
- hostile mutations: 34/34; PDF: 2 pages, 27 font records;
- evidence SHA-256: `8022cf052355bac0952f0274f1daa68aa474f9defae27eed82af87726bf28f3e`;
- PDF SHA-256: `15e020b8c67721fbd22a1a85943eedee4b60c0c9c4a1c1423abefffb47c43946`;
- manifest SHA-256: `9514185483ee6f3b359e87d33e039751a95dcc814cc6fc96f51d12f3fce784bc`;
- tuple: `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
  `ROUTE_A_REJECTED`.

### HCS-C260 — finite projective Möbius dynamics

For every prime power `q`, the identity, nontrivial-unipotent, split-
semisimple, and nonsplit-semisimple types exhaust `PGL_2(F_q)` on
`P^1(F_q)`.  The theorem gives exact cycle types, every fixed and primitive
count, source zeta, Koopman determinant/spectrum, reversors, order
distribution, and the characteristic-two absolute-trace boundary.

- exhaustive receipt: 155,346 elements over 18 representative fields and
  4,367,094 direct state images;
- producer assertion units: 6,314,520; independent checker: 6,159,318;
- SymPy: 193; hostile mutations: 40/40; PDF: 2 pages, 31 font records;
- evidence SHA-256: `c5983dfc3253376d9ae5c225608b5dcb6e95248f72853c5c1391abdf388cdfde`;
- PDF SHA-256: `b121a1e71b244b1447b53014105ae4378345b52b4f3d1df2199c16aee94c2dfe`;
- manifest SHA-256: `8c687a0bdda8f45988cc2ace85dbdbfd1b797c142d8eca6f16b240d70cd447b6`;
- tuple: `(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
  `ROUTE_A_EXPLORATORY`.

### HCS-C261 — periodic Airy cubic-Talbot flow

The all-time `L^2(T)` unitary group has least global period `2*pi`.  Every
reduced rational strobe has an exact cubic-DFT translation formula and exact
order `q`; its fixed space is classified by
`product ell^ceil(v_ell(q)/3)`.  The theorem also closes every finite-support
state period, the irrational fixed-space boundary, and noncompactness.

- receipt: 2,806 reduced strobes through `q=96`, 101 full DFTs through
  `q=18`, and ten support-period rows;
- independent checker: 50,765 assertions; symbolic/modular checks: 301,200;
- hostile mutations: 41/41; PDF: 2 pages, 23 font records;
- evidence SHA-256: `6eac95acc424c97743ac772e8c44ed667cc12651f7b1fc5a41a19522c8915e2a`;
- PDF SHA-256: `67090f077d783a12ba504dc43c91e144d88a214319121b462a0b895872e0ffbd`;
- manifest SHA-256: `012c3c1d5773a49a62d89fe9f7ece355a95786905b2d2dffab924358600f6e10`;
- tuple: `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
  `ROUTE_A_REJECTED`.

### HCS-C262 — two-step Hill Floquet--Jordan atlas

Entire segment functions cover positive, zero, and negative coefficients in
one `SL(2,R)` transfer.  The exact discriminant closes elliptic and
hyperbolic regions; the theorem separately resolves `M=+/-I` and nontrivial
Jordan linear growth, fixes `U_{-1}=0,U_0=1` in the Chebyshev iterate, and
includes zero-duration, constant-coefficient, and order-swap faces.

- receipt: 900 all-sign transfers and six exact boundary witnesses;
- independent checker: 19,849 assertions; SymPy: 289;
- hostile mutations: 41/41; PDF: 2 pages, 21 font records;
- evidence SHA-256: `34f8e1ba2567dfb9821cd84c5a3d3cfb04219df1df360fd4106a8bdc7c696f4b`;
- PDF SHA-256: `d3b6743904caea88860c38635602a3395fabfdd795b326d12cdb1b82cd604cb9`;
- manifest SHA-256: `2ed20af8071af9f317e1f7c3bd2813e9b9cb55e04c871d070f0cbd753cebba52`;
- tuple: `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
  `ROUTE_A_REJECTED`.

### HCS-C263 — multicolor Pólya reinforcement

For arbitrary color count, nonnegative initial masses with positive total,
and nonnegative reinforcement, the theorem closes ordered-word
exchangeability, Dirichlet--multinomial counts, beta--binomial marginals,
arbitrary multi-index factorial moments, exact covariance, the normalized-
mass martingale, Dirichlet de Finetti representation and almost-sure/all-
finite-`L^p` limit.  The iid, zero-color-mass, and one-color faces are
separate and exact.

- receipt: 12 cases, 10,860 words, 1,000 compositions, 1,021 marginals,
  1,567 factorial rows, 2,042 martingale rows, and 253 mixture rows;
- independent checker: 62,233 assertions; SymPy: 156;
- hostile mutations: 23/23; PDF: 3 pages, 20 font records;
- evidence SHA-256: `520f838b31ec414bd9fab8d0ef797c687a045c85e30180563bed0f0da4214db3`;
- PDF SHA-256: `964abebbfeeb64af5f2d3038a790a537476faa88d0485cacfc4e055b4f946c88`;
- manifest SHA-256: `32beb6b20585409166ffe1c23e2111dc79f308f675f3b46e88271a8ff622ec71`;
- tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
  `ROUTE_A_REJECTED`.

## Aggregate audit

| gate | aggregate result |
|---|---:|
| independent-checker assertions | 6,769,495 |
| symbolic checks | 302,099 |
| repaired-hash hostile rejections | 179/179 |
| manifest payloads | 135 |
| physical files including manifests | 140 |
| final-paper pages | 11 |
| embedded/subsetted font records | 122 |

Every producer, independent checker, SymPy reconstruction, clean-process
byte replay, hostile-mutation suite, and release-manifest script passes.
Independent second-agent audits repeated the C261 and C262 mathematics,
fresh PDF builds, manifest generation, and all 27 ledger hashes.  All five
manifests report `RELEASE_COMPLETE`; each final PDF equals its round-2 PDF,
and all three round hashes differ within every package.

## Final integrity gate

The registered reference population contains ten items.  All ten existence,
bibliographic-metadata, DOI/record, and manuscript-context checks were rerun
against publisher or authoritative repository records on 2026-08-31.  The
gate found one correctable mismatch: C261 had abbreviated its second source
from the middle author rather than preserving the published author order.
The final source audit, evidence producer, independent checker, hostile
mutation, evaluator key, manuscript, PDF, and release manifest now use
L. Boulton, G. Farmakis, and B. Pelloni, with the complete article metadata.
The context audit also found bibliography-only entries in C260--C263; each is
now anchored explicitly in the relevant model or boundary paragraph.  All
four affected final PDFs were deterministically rebuilt and visually
rechecked.  The corrected packages were regenerated and re-audited from
scratch; no registered-reference or citation-context issue remains.

| candidate | standardized verification query | authoritative record | result |
|---|---|---|---|
| C259 | `Kuramoto "Self-entrainment" 1975 420 422` | [Springer DOI record](https://doi.org/10.1007/BFb0013365) | verified |
| C260 | `Sakzad Sadeghi Panario cycle structure 2012 347 361` | [AIMS article record](https://doi.org/10.3934/amc.2012.6.347) | verified |
| C260 | `Forsyth Gurev Shrima metacommutation 2016 4583 4590` | [AMS DOI record](https://doi.org/10.1090/proc/13126) | verified |
| C260 | `Wall conjugacy projective special linear 1980 339 364` | [Cambridge DOI record](https://doi.org/10.1017/S0004972700006675) | verified |
| C261 | `Pelloni Smith Airy Talbot 2024 e12699` | [Wiley article record](https://doi.org/10.1111/sapm.12699) | verified |
| C261 | `Boulton Farmakis Pelloni beyond periodic revivals 2021 20210241` | [Royal Society article record](https://doi.org/10.1098/rspa.2021.0241) | verified after correction |
| C262 | `Hill lunar perigee 1886 1 36` | [Springer DOI record](https://doi.org/10.1007/BF02417081) | verified |
| C262 | `Golubev piecewise constant coefficients preprint 43 1997` | [MathNet record](https://www.mathnet.ru/eng/ipmp1431) | verified |
| C263 | `Eggenberger Polya Statistik verketteter Vorgaenge 1923 279 289` | [Wiley DOI record](https://doi.org/10.1002/zamm.19230030407) | verified |
| C263 | `Blackwell MacQueen Ferguson distributions 1973 353 355` | [Project Euclid DOI record](https://doi.org/10.1214/aos/1176342372) | verified |

The seven-mode research-integrity screen is clear within its declared
population: deterministic outputs have saved producers and logs; independent
checkers, symbolic reconstructions, clean-process replay, and repaired-hash
mutations address implementation/narrative drift; no unrun empirical metric,
seed count, learned shortcut, or fabricated experimental method is claimed;
and the collision report records early-frame alternatives and exclusions.
This is a coverage-bounded integrity result, not a claim that automated checks
establish global mathematical truth, literature priority, or plagiarism-tool
coverage.

## Claim and route boundary

C260 alone reaches `ROUTE_A_EXPLORATORY` because finite-field prime-power
structure is intrinsic.  It still has no one-rational-prime/one-primitive-
orbit dictionary, logarithmic prime clock, target local factor, or target
global analytic object.  C259 and C261--C263 are `ROUTE_A_REJECTED`.

No package claims target arithmetic local data, Euler factors, root numbers,
automorphy, a target divisor/counting law/functional equation, a target zero
match, a Hilbert--Pólya operator, or Route-B readiness.  Route B is false for
all five.  The next five-paper round therefore requires a new user
confirmation.
