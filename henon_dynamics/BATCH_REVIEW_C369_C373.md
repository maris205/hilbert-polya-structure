# Batch review: HCS-C369--HCS-C373

## Outcome

This round delivers five independent theorem packages from frozen baseline
`c6553f02d928c6aa05400ded57746869a85f0238`.  Their dynamical owners are a
quartic arithmetic root scheme, a quasiregular contact flow, a rational-flux
magnetic Bloch family, an inviscid free-boundary vortex patch, and a curved
classical--quantum oscillator.  They have different phase spaces, clocks,
proof engines, and singular boundaries; they are not one paper divided into
five installments.

Each unbounded-parameter or all-class headline is closed analytically under
explicit hypotheses.  The finite evidence ledgers audit conventions,
formulas, boundary branches, and serialization; no paper uses sampling as a
proof of its all-prime, all-return-time, all-flux, all-mode, or full-spectrum
statement.  Every package has a producer, a code-independent checker, a
separate SymPy lane, two-directory byte replay, repaired-hash hostile
mutations, three substantive manuscript rounds, deterministic PDF builds,
and a self-excluding release manifest.

## Independent theorem increments

- **C369:** the polynomial-specific `S_4` Chebotarev--Frobenius root atlas for
  `x^4-x-1`.  Irreducibility, discriminant `-283`, and Galois group `S_4` are
  proved from explicit modular witnesses.  At every good prime, factor
  degrees equal the arithmetic-Frobenius orbit lengths; every iterate fixed
  count and primitive-cycle count follows, and the five conjugacy classes
  give the exact factor types and Chebotarev densities.  The finite
  permutation zeta/determinant identity is explicitly inherited from C12A
  and specialized here, not reclaimed as a universal result.  The repeated
  factor at `p=283` is retained as a non-etale source boundary, and no
  cross-prime determinant or target Euler object is formed.
- **C370:** the complete normalized Reeb atlas on each pairwise-coprime
  Brieskorn link `Sigma(2,p,q)` with odd `3 <= p < q`.  The result identifies
  the principal period `2pq`, all three exceptional simple circles, every
  real return-time fixed set, and the Morse--Bott kernel.  It derives the
  missing-coordinate rotations, return determinants, first degeneracy
  covers, and every pre-degeneracy Conley--Zehnder index.  In the named
  Milnor-fibre capping trivialization the two normal complex directions are
  accounted for separately, yielding the principal Robbin--Salamon formula
  and its unique positive case `(p,q)=(3,5)`.  Contact homology and a discrete
  primitive-orbit promotion remain outside the theorem.
- **C371:** the all-reduced-rational-flux anisotropic Harper--Chambers Bloch
  atlas.  A fixed Landau-gauge convention gives
  `det(EI-H)=P(E)-2 cos(q k_x)-2 lambda^q cos(q k_y)`, hence the full
  two-dimensional spectrum as one exact polynomial preimage.  The two edge
  factors are actual real-symmetric endpoint-fibre characteristic
  polynomials, giving an exact multiple-edge criterion without asserting
  that every other gap is open.  Aubry duality, flux reversal, parity, and
  the accumulated-neighbour `q=1,2` faces are closed.  For all even
  denominators, Lamoureux--Mingo's cyclic-continuant theorem is mapped by
  `lambda_LM=2 lambda` to prove the forced central contact; the finite
  `q<=10` lane is only regression evidence.
- **C372:** the complete Love-mode threshold ladder for Kirchhoff's uniform
  elliptic vortex.  The paper derives the rigid Euler relative equilibrium,
  rotation clock, interior field, invariants, and marked/unmarked periods.
  Starting from the explicitly sourced Love dispersion in the frame
  co-rotating with the instantaneous principal axes, it factors every modal
  square, proves one strictly ordered critical aspect for each `m>=3`, and
  obtains the sharp first wall `gamma_3=3`.  It also proves
  `m(1-delta_m) -> 1+W(e^-1)` and
  `gamma_m/m -> 2/(1+W(e^-1))`, so every fixed aspect has only a finite
  initial block of unstable modes.  Every square identity is written without
  division by possibly zero vorticity.  Only spectral linear stability is
  claimed.
- **C373:** the exact classical, Friedrichs-quantum, and revival closure of
  the hemispherical Higgs oscillator.  Turning points give the radial action
  `I_r=(sqrt(2R^2E+omega^2R^4)-|L|-omega R^2)/2`, its inverse action
  Hamiltonian, the global `2:1` frequency lock, and the exact regular period.
  Separation gives the complete Jacobi basis, energy levels, and a directly
  proved multiplicity `N+1`, together with the flat and zero-coupling
  Dirichlet-hemisphere limits.  Consecutive spectral gaps then prove that the
  full propagator, not merely a scalar multiple, revives exactly when
  `2 nu` is rational and determine the least revival multiplier.

The strict tuples, in order, are
`(A0_STRUCTURAL_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, and
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.  C369 is
`ROUTE_A_ARITHMETIC_CANDIDATE`, C370 is `ROUTE_A_EXPLORATORY`, and
C371--C373 are `ROUTE_A_REJECTED`.  Route B is false for all five.

## Exact release accounting and hashes

| ID | finite evidence | independent checker / symbolic lane | hostile rejections | evidence bytes | final pages / fonts |
|---|---|---:|---:|---:|---:|
| C369 | 1,228 good primes and 14,736 prime--iterate cells | 16,044 / 187 | 51/51 | 1,121,861 | 3 / 17 |
| C370 | 1,003 pairs, 5,469,178 fixed cells, 4,012 orbit types, 3,009 rotations, and 103,749 CZ cells | full independent reconstruction / 11,041 | 61/61 | 3,787,774 | 3 / 19 |
| C371 | 390 panels, 74,880 fibres, 825,600 eigenvalues, and 224,640 determinant probes | 1,139,690 / 1,557 | 107/107 | 644,534 | 4 / 18 |
| C372 | 561 aspects, 35,904 modal cells, 62 thresholds, and 390 rigid rows | 37,030 / 2,470 | 64/64 | 2,649,874 | 4 / 18 |
| C373 | 2,048 classical cells, 8,385 state labels, 129 levels, and 512 revival controls | full independent reconstruction / 1,404 | 75/75 | 7,013,177 | 4 / 21 |
| **total** | **five independent exact ledgers** | **at least 1,192,764 numbered checker assertions plus two full-ledger reconstructions / 16,659** | **358/358** | **15,217,220** | **18 / 93** |

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C369 | `804902a4f9cc74e5f71be5e9aa72f8fd6d32873e48073c6925a64e901a8e3e94` | `d998c948f340a5f68882de5d867fbe3d63f60359efbf7bf3c5af699bd95c7abc` | `a59681855601ca9efceb8fbec311a7c23c716d50e66ea36fadba386ad949096f` | `671743c9ca09fc814fe3b8027ee9f6b4783d732eaeb33e2e3af22a18012ed399` | `41763f0c4bef491a99c928e0e267d2dcc32a613dfe07d45b11c590a1fcb31fd5` |
| C370 | `3d000cca57cbc26bcb262b75e87fc7cafa6826b79a5e61d287cd9d62b71b5f84` | `28d36fa94cbd994ca9571dab034949e89e61cd7e3f702181b006fd5442177aa5` | `716a7e04cc125bd871e54deb25aafb3f9f00909c86655639b822b98dbe931149` | `fa189eb25322876c2114408e738ddcae400e3286258c1bf914eb385e985ff44c` | `677bf3bf2377e07d28db5b01697f6b47d727f8123a8367e43d7c59b7fe421261` |
| C371 | `ae3131b99840763ad6309c6ec702dd01a35145b57323eb66a170b3244e07e11c` | `6260291e78ebcb451efdf69d929d379cfa0571fc4f32ea2dab338134719fdbe4` | `c1a1ffbc5b00a6f7017aed9b7f16465b8aeee21709d0c6e45e179219254a5c39` | `9a4a91d0906527785458ba8d5092b2f98309710823242ff8f1e5b68daa15d72f` | `b79962f7d384a6752b5e8d116b13e069ea072ffdd97825c07228222733475c1f` |
| C372 | `6b72bdbfcd9a9c16c54e26235c274e9c056dfbba6fdc114ba0be21d28da76b50` | `30148b32552733cff662cfc79ea404f39134ff0ae5650401fcc1e96eecd4046a` | `034bf0b28bd113961cc6564fedb07b923eeb7d5a152a081315d3e96e168cc2fd` | `f83c5b580d3e6893c5b9d0fb931e6a06c7f246b9825b8ca323f4178761dfb2d5` | `79acac0a530b6d8af9893dee18afa25ed56fdfad0d861b6ec087700855fdacb9` |
| C373 | `bddd07106ff003318555efe931b12ba10e3938669df23e97770a7f2327c342b5` | `2d8a17ebec4a597baa419ae2078f8a2ecba2524c90d89593793b23554d774439` | `820dcd69392bc88e9880ae7d6f019837961f5feed12c9ff5de96a308fb089058` | `814d3b8a1cfdddc7d9b3c682cf73d5e6f4f8c3429d93c91b65da89e874df2e29` | `94dd8d1e74513f31ed416b12e8362da32178e85ae0757d85f8722b8475320379` |

All five manifests contain exactly 35 payloads and exclude only themselves,
giving 175 content-addressed payloads and 180 physical package files.  Every
paper retains three distinct round hashes and `main.pdf` is byte-identical to
Round 2.  The 18 final pages were visually inspected; all 93 font rows are
embedded and subset.  Settled builds have no layout, citation, reference,
destination, rerun, missing-character, or missing-glyph warning.  Every page
rasterizes and every extracted-text sentinel passes.

## Author-swapped corrections and integrity

C369's first collision pass added the degree-27 C56 Fano-line scheme as the
closest finite-etale arithmetic neighbour.  A later hostile ownership review
found the more important universal collision: C12A already owns the fact that
reduced zero-dimensional Frobenius is a finite permutation and therefore has
a rational finite zeta/permutation determinant.  Every package layer now
inherits that mechanism explicitly and restricts C369's owner to the fixed
quartic's `S_4` proof, five-class all-good-prime specialization, densities,
ramified boundary, and executable convention lock.  Evidence schema v2 and
four new ownership mutations prevent the broader claim from returning.

C370's first principal-index proof subtracted a normal contribution without
exhibiting both normal complex directions.  The repaired capping calculation
uses Kwon--van Koert Section 5.3, formula (14), and Proposition 5.9: the
defining-polynomial line winds `d=2pq` times and contributes `2d`, while the
radial/Reeb complex line is stationary and contributes zero.  This turns the
ambient contribution into
`2d(1/2+1/p+1/q-1)` under a named Milnor-fibre trivialization.  Independent
re-review verified the contact-form rescaling, all exceptional rotations,
the Morse--Bott kernels, and the sign wall.

C371's initial manuscript correctly computed every tested denominator but
did not prove that mixed cyclic matching terms cancel for every even `q`.
The repair maps Lamoureux--Mingo's operator parameter by `L=2 lambda`,
identifies their monic discriminant with this package's `P`, and invokes their
Theorem 2.5 and Corollary 2.6 for the all-denominator constant term.  Parity
alone then gives `P'(0)=0`.  The two endpoint identities
`P-C=D(E;0,0)` and `P+C=D(E;pi/q,pi/q)` were added so realness of every
algebraic edge label follows from actual real-symmetric fibres.  Eight new
source, edge, and priority attacks lock the repair.

C372's initial factorized display divided by `omega_0^2` even though the
boundary atlas allowed `omega_0=0`.  All public identities now use
cross-multiplied physical squares, including the `m=3` and circular faces, so
the zero-vorticity theorem is defined rather than interpreted through `0/0`.
The source convention now also states that Fourier labels are measured
relative to the instantaneous principal axes and `lambda_m` is a co-rotating
frequency.  Evidence schema v2 replaces the quotient field by the physical
Love-square coefficient, and a dedicated frame/source mutation locks it.

C373's source audit corrected two bibliographic identities and refused to
copy a prose degeneracy sentence that conflicts with the admissible-label
count; multiplicity `N+1` is proved directly.  The first PDF audit removed
control bytes created by scalable braces.  A later independent visual review
then caught two missing backslashes that printed the literal token `qquad`
inside the revival theorem even though the old automated gate passed.  The
formula was repaired, and the release program now rejects unescaped
`quad`/`qquad` in source and literal leakage in extracted PDF text while
accepting legal commands and ordinary words.  Two new hostile attacks and
four positive controls close that blind spot.

Every checker imports no producer code.  JSON parsing rejects duplicate keys
and nonfinite constants.  Evaluation parsing locks exact identity, date,
epoch, evaluator authority, raw and semantic YAML digests, strict tuple,
Route-B lock, false scope flags, nested key sets, coordinate inventories, and
leaf types.  Repaired semantic mutations recompute outer payload hashes
before demanding rejection.  Every executable refuses optimized Python.

## Collision, citation, and scope integrity

The collision scan is mechanism-level.  C369 inherits C12A's universal
finite-fibre identity and stays separate from C56's Fano-line scheme, C41's
CM elliptic cohomology, and C172's chosen finite-field multiplier.  C370 is
different from C242's irrational ellipsoid Reeb flow, C313's round-sphere
clean geodesics, and C339's Katok--Zermelo family.  C371 is different from
C15's sparse `1/3^m` critical Harper edge tower.  C372 is distinct from
C284's point vortices, C299's viscous Lamb--Oseen diffusion, and C368's
Laplacian-growth boundary.  C373 is distinct from C349's full-sphere Neumann
oscillator, C244's spherical pendulum, C313's free sphere, and C221's
nonlinear Schrodinger dynamics.  These comparisons establish workspace
ownership only and never literature priority.

Primary lineage and exact locators remain explicit:

- C369 uses Serre, Neukirch, and Lidl--Niederreiter for the standard Galois,
  Chebotarev, Dedekind, and finite-field framework, while the displayed
  polynomial calculations are reproduced.
- C370 uses Kwon--van Koert, DOI `10.1112/blms/bdv088`, Section 5.3,
  formula (14), Proposition 5.9, and van Koert,
  DOI `10.1515/FORUM.2008.016`, for the capping/index framework.
- C371 treats Harper, Chambers, Hofstadter, and rational almost-Mathieu
  spectral theory as established, and uses Lamoureux--Mingo,
  DOI `10.1090/S0002-9939-07-08830-2`, Theorem 2.5 and Corollary 2.6, for
  the cyclic-continuant step.
- C372 sources the Love dispersion to Love's 1893 paper,
  DOI `10.1112/plms/s1-25.1.18`, and locks the modern convention against
  Mitchell--Rossi, DOI `10.1063/1.2912991`, Equation (17).
- C373 uses Higgs, DOI `10.1088/0305-4470/12/3/006`, and Leemon for the
  curved oscillator lineage; Bellucci--Nersessian--Saghatelian--Yeghikyan,
  arXiv `1008.3865`, for the action comparison; and
  Hakobyan--Pogosyan, arXiv `quant-ph/9803085`, for the separated hemisphere
  problem.

All formulas, proof closures, and executable receipts are source-local
reconstructions.  No package claims literature priority.

All five evaluations use evaluator v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
and literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local
datum, target Euler factor, target bad-prime datum, root number, automorphy object,
target divisor/counting law or functional equation, target-zero match,
Hilbert--Polya operator, or Route-B input is asserted.
