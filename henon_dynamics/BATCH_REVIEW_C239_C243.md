# Route-A batch review: C239--C243

Status: **RELEASE_COMPLETE**

Evaluation date: 2026-08-30

Source/code baseline: `489506cf92bfed721f94f22dd0444a60427f90a5`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md`, v0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

This round changes the dynamical owner in every slot and gives each owner one
complete theorem-scale advance.  The finite receipts are regression slices;
the all-parameter statements are the source-local theorems in the individual
packages.  `NEW` is workspace bookkeeping and is not a literature-priority
claim.

## Theorem advances

| ID | dynamical owner | closed advance | finite receipt |
|---|---|---|---:|
| C239 | multiway perfect-shuffle permutation `rho(i)=k i mod (kn+1)` | All-parameter fixed counts `gcd(k^r-1,kn+1)-1`, pointwise orders, least periods, Möbius cycle counts, finite source zeta/Koopman factors, and an independent literal packet-interleave realization. | 50 atlas + 74 position + 6 spectral rows; 1,100 packet checks |
| C240 | one-discontinuity contracted rotation `x -> {lambda x+delta}` | Exact binary carry-word affine compositions, unique periodic point per admissible itinerary, half-open parameter intervals, primitive/repetition separation, endpoint controls, and direct-iteration replay for three rational slopes. | 2,241 word + 138 admissible/plateau + 295 direct rows |
| C241 | classical countable-branch Lüroth map | Unique coded periodic point and multiplier for every finite digit word, primitive necklaces, countably infinite points at every positive period, finite weighted identity, full convergence half-plane, and the exact `s=1` telescoping boundary. | 11 branch + 780 word + 30 necklace + 88 weighted + 3 limit + 2 product rows |
| C242 | irrational ellipsoid Reeb flow | Exactly two simple coordinate orbits on the irrational face, all iterate actions/periods/transverse rotations/CZ indices in the declared trivialization, integer-square floor certificates, and rational Morse--Bott full-boundary degeneration. | 48 irrational iterate + 6 rational-coordinate rows |
| C243 | Bose--Josephson dimer on the Bloch sphere | Full fixed-point/pitchfork atlas, quartic energy reduction, crossing and self-trapped elliptic periods, explicit `H=1` homoclinic separatrix, component criterion, and the `Lambda=0,1,2` singular faces. | 14 fixed-point + 8 pole + 13 level + 5 criterion rows |

The C243 pair-of-pants/Schottky proposal was rejected during collision
screening because a substantive Schottky ledger already exists in the
workspace; the released Bose--Josephson package is the recorded pivot.

## Independent audit and release hashes

Every package contains exactly 27 manifest-listed payload files plus one
self-excluded release manifest (28 physical files), with no Python bytecode or
LaTeX sidecars.  Each producer, producer-independent checker, exact symbolic
cross-check, clean byte replay, hostile mutation suite, and release manifest
was rerun under `PYTHONDONTWRITEBYTECODE=1 python3 -B`.  The final PDFs were
compiled in two fresh trees for each of three substantive revisions under
`SOURCE_DATE_EPOCH=1788048000`; paired builds were byte-identical, settled
logs were clean, all reported fonts were embedded/subsetted, and the pages
were visually inspected.

| ID | checker assertions | SymPy identities | extra exact checks | hostile rejects | final pages / fonts | evidence payload SHA-256 | evidence file SHA-256 | final PDF SHA-256 | manifest SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|---|---|
| C239 | 2,303 | 50 | 1,100 packet positions | 44/44 | 2 / 22 | `8085524a84679c3238be67af0f25e8c4399b22b41b87d9d5f7f87c54859d0d70` | `e1481a44b23f02f0109e2906b58ec4699d780316906c4199568e153606eaa685` | `f84034336987de2f5c6889528d9fd845ebac8a722622127568db616c36529130` | `e50b788e71c99338569bfbb2886c611eab26132ad749d7ca8750a495541038eb` |
| C240 | 6,763 | 119 | 295 direct probes | 33/33 | 3 / 22 | `d1af00d9bccaceeb5abeeb4a75231550fa9fa348368b37a66231cd08650e018d` | `827d48369f3b58abc7562bebbf52e9604f58643e295a7763848c817f434393d3` | `05d9c83b204730a79476f468ee9746bcede2e52e69e0df2b33fb371a4e18da4f` | `4519e31f78eebbf16017f9695f0582649b2c344e5277fbaa5bf61bddbe7bcb59` |
| C241 | 18,775 | 1,585 | 90-digit weighted receipts | 56/56 | 2 / 24 | `ca93cfbabb5a2a60c76f26486c95fb0dc9b77def57a770bfceeceada98ffd01a` | `998b85f78fae9787a88817ae3de6e3693d8a0aecfcf3d0111a4f6d25cc27cb4e` | `682151b76d75ee6418543b399495a98b3fbaf44b333efafa5bb8fe66faf7f94c` | `b2b8e2249df61c60ca1c2695c02e573cc9eb16aeabac19c40434619dc1968605` |
| C242 | 2,089 | 59 | 48 square-floor certificates | 29/29 | 2 / 23 | `26eb2befe75bb062f61510bb34fb4d87cf33ad62adeae3d45d818a541251c16a` | `dc2067d8219f2632501bacf91ed8e22abcc82d160c1a17deb6454a8d8e204c3a` | `55223b048648d666c383ccf905ed2e707f6f46e473b69095254947cf525ac6d0` | `54cf2a27b24f14232f1a33c7299ac7fecfdbc44349ca4d89132eb2f1b8e6ce6c` |
| C243 | 995 | 13 | 3 elliptic quadratures | 28/28 | 2 / 22 | `eb01108beaf3aade38359374fafc5e38dcb40dea2721fc095adc3db925f6a239` | `8be606261d38694a75f417ead9ed745c676ace46b190b926c1a23e71efc3a445` | `f83a93ceff68654d276ee330051c427b1283965856c03a1734678c160cf2bc2b` | `7f1ba98b2305ed09308dce44c3d5c222aa4f65b688f74e22c8da93662833953b` |

Aggregate totals are **30,925** checker assertions, **1,826** symbolic
identities plus **3** independent elliptic quadratures, **190** hostile
rejections, **135** payload files (140 physical files), and **11** final-paper
pages with **113** embedded/subset font entries.  For every paper,
`paper/main.pdf` equals `paper/main_round2.pdf` byte-for-byte; all three round
hashes are content-distinct.

The three final revision hashes, in round order, are:

- C239: `8d4ddf0cd25703eabbb245dde84198209eb058d7cd8309f75dcc6dc83532d356`,
  `8d7bf23de5422540f28796cd6e0a26f843f10157122c7690a9afd020fe63b823`,
  `f84034336987de2f5c6889528d9fd845ebac8a722622127568db616c36529130`.
- C240: `646fea906b5e6a4b03e4a6d2f2dfc8ef087cf10fb6982624346b5c61805b86b0`,
  `ff5c80a1c833385c575065ca68bbfea4b87c9d4160d07caeab44db2fbf59003b`,
  `05d9c83b204730a79476f468ee9746bcede2e52e69e0df2b33fb371a4e18da4f`.
- C241: `5ef3d66f9ea3069980357b1fd59733d4187346d2ceff62538032701d18cb6f5e`,
  `e127da8b02e004eabfbfa4303d3b59181078dfda142b45ea169b23b1a041c0ab`,
  `682151b76d75ee6418543b399495a98b3fbaf44b333efafa5bb8fe66faf7f94c`.
- C242: `2cd11ab1e9e064db0fef698cd1e3f37d2453c4bc7683d9857d983dbf7aa8a6e8`,
  `672d4b49312d0ec0e995507472b5fe6229b4b72611f1c1271212cc88deabd10e`,
  `55223b048648d666c383ccf905ed2e707f6f46e473b69095254947cf525ac6d0`.
- C243: `1bf4177428793dbd135b56cbcf54a2360add09c45ea25bf9ba2a928a246ffbcb`,
  `d85fac19fd24ad3826177cf9329d4978d8f7f5f9efeec0ef7c63f8a7033b5b8c`,
  `f83a93ceff68654d276ee330051c427b1283965856c03a1734678c160cf2bc2b`.

## Route-A decision and scope boundary

| ID | strict tuple | overall | Route B |
|---|---|---|---|
| C239 | `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` | `ROUTE_A_REJECTED` | false |
| C240 | `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` | false |
| C241 | `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` | false |
| C242 | `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` | false |
| C243 | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` | `ROUTE_A_REJECTED` | false |

The source-local quantization/formal hints, weighted products, finite zeta
factors, Reeb gradings, and elliptic periods are not target arithmetic data.
No package introduces a target prime/zero table, arithmetic local datum, Euler
factor, root number, automorphy statement, target divisor/counting law,
functional equation, Hilbert--Pólya operator, or Route-B input.

The five package READMEs and PDFs are indexed in
[`henon_dynamics/README.md`](README.md); the candidate and obstruction
registries record the same source-local stopping boundaries.
