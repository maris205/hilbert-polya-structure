# Source verification and convention-aware subtraction — P149

**Checked:** 2026-09-01 UTC  
**Status:** bounded primary-source audit; `HOLD_EXTERNAL`

Only primary papers and their official arXiv/DOI/publisher records were used
for claim decisions.  A search non-hit is not positive novelty evidence.

## Exact-convention direct background

P149 sets `pi_0=pi_(n+1)=0`, so either endpoint may be selected.  Kathy Q.
Ji, “The `(alpha,beta)`-Eulerian Polynomials and Descent--Stirling Statistics
on Permutations,” *Science China Mathematics* 68, 2259--2284 (2025),
[DOI 10.1007/s11425-024-2362-3](https://doi.org/10.1007/s11425-024-2362-3),
[arXiv:2310.01053](https://arxiv.org/abs/2310.01053), Definition 2.1, assumes
`sigma_0=sigma_(n+1)=0` and calls every `1<=i<=n` satisfying the two strict
inequalities an exterior peak.  This is the exact static convention used by
P149.  Ji's static distributions therefore receive zero contribution credit.
The inspected source does not standardize the ordered peak-value word or
iterate that operation.

Ji attributes the name “maxima” for these exterior peaks to L. Carlitz and
R. Scoville, “Generalized Eulerian Numbers: Combinatorial Applications,”
*Journal fuer die reine und angewandte Mathematik* 265, 110--137 (1974),
[DOI 10.1515/crll.1974.265.110](https://doi.org/10.1515/crll.1974.265.110),
[EuDML metadata](https://eudml.org/doc/151403).  The official metadata and
Ji's attribution were verified, but the original full text was not directly
retrievable in this audit environment.  P149 therefore makes no earliest-
owner or priority claim about Carlitz--Scoville and does not use that paper as
claim evidence.

## One-sided convention neighbour

Amy M. Fu, “A Context-Free Grammar for Peaks and Double Descents of
Permutations,” *Advances in Applied Mathematics* 100, 179--196 (2018),
[DOI 10.1016/j.aam.2018.06.004](https://doi.org/10.1016/j.aam.2018.06.004),
[arXiv:1801.04397](https://arxiv.org/abs/1801.04397), Section 2, admits a peak
at `i=1` or at an interior position `1<i<n` and has no `i=n` clause.  It is a
direct static neighbour, not an exact-convention owner.  The witness `12`
separates the rules: P149 selects its last value, while Fu selects no exterior
peak.  Fu's one-sided static distribution results remain zero credit.

## Ordinary interior-pinnacle bridge and nearest owners

The conventional pinnacle papers below restrict peaks to interior positions.
They are connected to P149 by the explicit padding

```text
pi_1 ... pi_n -> 1, pi_1+2, ..., pi_n+2, 2.
```

The ordinary interior peak values of the padded permutation are exactly the
P149 endpoint-inclusive peak values shifted by two and in the same order.
This makes the following papers nearest static owners, not literal owners of
P149's convention or dynamics.

| key | verified primary record | zero-credit role |
|---|---|---|
| `DavisEtAl2018` | Davis, Nelson, Petersen, and Tenner, “The Pinnacle Set of a Permutation,” *Discrete Mathematics* 341(11), 3249--3270 (2018), [DOI 10.1016/j.disc.2018.08.011](https://doi.org/10.1016/j.disc.2018.08.011), [arXiv:1704.05494](https://arxiv.org/abs/1704.05494). | ordinary interior pinnacle sets and admissibility |
| `RusuTenner2021` | Rusu and Tenner, “Admissible Pinnacle Orderings,” *Graphs and Combinatorics* 37(4), 1205--1214 (2021), [DOI 10.1007/s00373-021-02306-9](https://doi.org/10.1007/s00373-021-02306-9), [arXiv:2001.08185](https://arxiv.org/abs/2001.08185). | relative orders of prescribed ordinary pinnacle sets |
| `DiazLopezEtAl2021` | Diaz-Lopez, Harris, Huang, Insko, and Nilsen, “A Formula for Enumerating Permutations with a Fixed Pinnacle Set,” *Discrete Mathematics* 344(6), 112375 (2021), [DOI 10.1016/j.disc.2021.112375](https://doi.org/10.1016/j.disc.2021.112375), [arXiv:2001.07325](https://arxiv.org/abs/2001.07325). | fixed-pinnacle enumeration |
| `DomagalskiEtAl2022` | Domagalski, Liang, Minnich, Sagan, Schmidt, and Sietsema, “Pinnacle Set Properties,” *Discrete Mathematics* 345(7), 112882 (2022), [DOI 10.1016/j.disc.2022.112882](https://doi.org/10.1016/j.disc.2022.112882), [arXiv:2105.10388](https://arxiv.org/abs/2105.10388). | admissibility, order, and structural properties |
| `Fang2022` | Fang, “Efficient Recurrence for the Enumeration of Permutations with Fixed Pinnacle Set,” *DMTCS* 24(1) (2022), [DOI 10.46298/dmtcs.8321](https://doi.org/10.46298/dmtcs.8321), [arXiv:2106.09147](https://arxiv.org/abs/2106.09147). | fixed-pinnacle recurrence and algorithms |
| `FalqueEtAl2024` | Falque, Novelli, and Thibon, “Pinnacle Sets Revisited,” *Discrete Mathematics* 347(4), 113834 (2024), [DOI 10.1016/j.disc.2023.113834](https://doi.org/10.1016/j.disc.2023.113834), [arXiv:2106.05248](https://arxiv.org/abs/2106.05248). | further fixed-set structure and enumeration |

## Size-preserving peak-value neighbour

Alexandersson and Nabawanda, “Peaks Are Preserved under Run-Sorting,”
*Enumerative Combinatorics and Applications* 2(1), S2R2 (2022),
[DOI 10.54550/ECA2022V2S1R2](https://doi.org/10.54550/ECA2022V2S1R2),
[arXiv:2104.04220](https://arxiv.org/abs/2104.04220), proves a multivariate
equidistribution through an auxiliary bijection: input peak-value sets match
peak-value sets after run-sorting the bijective image.  It does not assert
that run-sorting pointwise preserves every input's peak-value set.  The
equidistribution, auxiliary bijection, and size-preserving run-sorting map all
receive zero credit.

## Search ledger and residual boundary

Recorded primary-source query lanes included combinations of:

```text
iterated local maxima permutation standardization
iterated peak extraction permutation
peaks of peaks permutation
endpoint peaks modified maxima
zero boundary peak values permutation
two-sided exterior peaks sigma_0 sigma_n+1
Carlitz Scoville maxima permutation exterior peak
pinnacle ordering fixed pinnacle set
run-sorting peak-value bijection
comparison word zigzag poset peak values
```

The audit used arXiv primary records/full text, DOI/Crossref metadata,
publisher pages, and author manuscripts.  Review B's `12` witness forced the
Fu reclassification; Ji Definition 2.1 was then inspected directly.  The
Carlitz--Scoville content attribution remains deliberately unregistered
because only its metadata, not its original text, was directly available.
The bounded audit did not locate
the exact conjunction

```text
ordered endpoint-inclusive peak-value word + standardization + iteration
+ every-iterate exact images and explicit every-target right sections
+ sharp every-rank logarithmic clock.
```

The comparison-poset fibre remains secondary: generic zigzag-poset and linear
extension technology and all static fixed-set/order enumeration are
zero-credit inputs.  No non-hit authorizes novelty, priority, submission,
posting, specialist contact, or release.
