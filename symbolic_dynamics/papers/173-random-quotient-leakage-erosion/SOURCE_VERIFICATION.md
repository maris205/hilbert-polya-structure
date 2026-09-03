# Source verification and owner subtraction — P173

**Checked:** 2026-09-03 UTC  
**Lifecycle:** `HOLD_EXTERNAL`
**Review status:** `DUAL_REVIEW_CLOSED`

## Verified primary records

1. J. Fulman and L. Goldstein, “Stein's Method and the Rank Distribution of
   Random Matrices over Finite Fields,” *The Annals of Probability* 43(3),
   1274–1314 (2015), DOI
   [`10.1214/13-AOP889`](https://doi.org/10.1214/13-AOP889), preprint
   [`arXiv:1211.0504`](https://arxiv.org/abs/1211.0504).  The records identify
   a matrix chosen uniformly from the full rectangular matrix space.  This
   is the direct owner used for the dimension-level rank/nullity law.
2. G. V. Balakin, “The Distribution of the Rank of Random Matrices over a
   Finite Field,” *Theory of Probability and Its Applications* 13(4),
   594–605 (1968), DOI
   [`10.1137/1113076`](https://doi.org/10.1137/1113076).  The primary MathNet
   description specifies independent entries with a sparse, dimension-
   dependent law and distinguished mass at zero.  It is broader nonuniform
   random-rank background, not the owner of P173's uniform rectangular count.
3. J. Goldman and G.-C. Rota, “On the Foundations of Combinatorial Theory IV:
   Finite Vector Spaces and Eulerian Generating Functions,” *Studies in
   Applied Mathematics* 49(3), 239–258 (1970), DOI
   [`10.1002/sapm1970493239`](https://doi.org/10.1002/sapm1970493239).
   Wiley/DOI metadata verifies the record; it is the primary control for
   finite-vector-space/Gaussian enumeration.
4. S. N. Evans, “Elementary Divisors and Determinants of Random Matrices over
   a Local Field,” *Stochastic Processes and their Applications* 102(1),
   89–102 (2002), DOI
   [`10.1016/S0304-4149(02)00187-4`](https://doi.org/10.1016/S0304-4149(02)00187-4).
   The publisher record and Berkeley technical report 614 were checked.
   Theorem 3.5 owns the elementary-divisor dimension-chain precursor.
5. R. Van Peski, *Random Matrix Theory over Integers of Local Fields*,
   undergraduate thesis, Princeton University, 7 May 2018, advisor Ju-Lee
   Kim, [primary author PDF](https://www.math.columbia.edu/~rv2549/Princeton_Thesis_D3-2.pdf).
   Theorem 3.3.4 and equations (3.42)–(3.55) give the descending labelled-
   subspace chain, its uniform square-map kernel description, and the fixed-
   target injection count.

## Zero-credit assignment

- Uniform finite-field matrix rank and nullity distributions belong to
  Fulman--Goldstein; Balakin is cited only as nonuniform background.
- Counts of injective linear maps and Gaussian subspace incidence are
  classical background, with Goldman--Rota the primary subspace control.
- Uniformity over fixed labelled kernels is the standard `GL(U)` symmetry
  refinement, and `q^(n^2-a(n-a))` is an elementary rank-nullity lift count;
  neither receives standalone contribution credit.
- Evans's dimension precursor and Van Peski's labelled square-kernel chain
  own the descending-subspace architecture, fixed-target injection count,
  Gaussian dimension lumping, and ordinary kernel powering.
- Triangular spectra, elementary Jordan theory, and first-step absorption
  recursions are generic tools.

## Internal collision firewall

| internal paper | occupied carrier/engine | why its theorem does not transfer wholesale |
|---|---|---|
| P109, nilpotent image subspace dynamics | subspace lattice, Gaussian target counts, quotient/graph fibre geometry, exact absorption layers | P109 iterates one fixed deterministic nilpotent image map and counts phase-state sources; P173 resamples ambient maps and counts quotient kernels/histories from a fixed source |
| P162, random translation intersection | random self-intersection, rank-controlled histories, all-time targets, absorption | P162 acts on arbitrary subsets of `F_2^d`; translation spans, affine cosets, and target stabilizers do not specialize to P173's linear-subspace quotient kernel |
| P165, low-weight support shortening | deterministic descending code/subspace dynamics, sharp height, every-time image criteria | P165 has a state-extracted coordinate support, no uniform quotient kernel, no complete target-fibre law, and no complementary spectral collision |
| P168, quartic inverse-span dynamics | subspace carrier, Gaussian census, deterministic functional graph, every-target fibres | P168 is dimension-increasing and deterministic, with inverse-line fixed/two-cycle geometry; its fibre classification is not a coefficient substitution into P173's random kernel law |
| P172, fresh-map self-image erosion | fresh ambient maps, monotone erosion, a small quotient, labelled recovery, triangular/Jordan tactics, absorption | P172 uses specified-box set-image occupancy, a total-image mark, and one terminal `J_2`; no coefficient substitution yields P173's linear injection fibre or complementary ladder |

The carrier, fresh ambient-map/erosion language, Gaussian incidence, quotient
and labelled-power bookkeeping, triangular spectra, Jordan recursion, and
absorption machinery are therefore zero-credit shared shell.

## Direct-chain non-transfer boundary

Van Peski's current `a`-space maps to an `a`-dimensional codomain in the
filtration of one Haar matrix over local-field integers.  P173 resamples a
fresh endomorphism of one fixed `n`-space and sees the rectangular leakage
map `U -> V/U`, dimensions `a -> n-a`.  The rows coincide at the middle
dimension `n=2a`, but not as a chain away from it.  Neither Evans nor Van
Peski states this complementary-codimension schedule, its diagonal symmetry
`q^(-a(n-a))=q^(-(n-a)a)`, or the resulting `J_2` ladder.  The remaining
collision-risk axis is precisely that fixed-ambient schedule, its literal
realization in the feedback update, and the complementary resonance.

## Residual and search limit

The retained residual is only the literal fresh fixed-ambient update and its
rectangular `a -> n-a` codimension schedule together with the complementary-
dimension Jordan ladder.  Generic uniform-kernel fibres, all-time labelled
powering, and the elementary ambient lift are not residual claims.  The
source search was bounded.  Failure to find an exact owner is recorded only
as a non-hit and is not evidence of novelty, priority, or freedom to operate.
