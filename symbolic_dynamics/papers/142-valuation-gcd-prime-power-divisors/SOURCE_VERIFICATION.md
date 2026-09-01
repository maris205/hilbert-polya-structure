# P142 source verification

Checked 2026-09-01 UTC.  Only primary sources already present in the VGT
scout are used.  They delimit established piecewise-linear and finite
discrete-tent background; none supplies novelty, priority, ownership, or
freedom-to-operate clearance for the literal divisor--gcd map.

| Key | Verified metadata | Exact manuscript use | Primary / official record |
|---|---|---|---|
| `MilnorThurston1988` | John Milnor and William Thurston, “On Iterated Maps of the Interval,” in *Dynamical Systems*, Lecture Notes in Mathematics 1342 (1988), 465--563, DOI `10.1007/BFb0082847`. | General piecewise-monotone and kneading background; assigned zero contribution credit.  No claim about the literal finite gcd map is attributed to this source. | [Author/university-hosted paper](https://public.websites.umich.edu/~kochsc/MilnorThurston.pdf); publication metadata cross-checked through the DOI record. |
| `Kuzovlev2004` | Yuriy E. Kuzovlev, “Length Distribution of Periodic Orbits of Unitary Discrete Tent Maps,” arXiv:`cond-mat/0412366`, submitted 14 December 2004. | Primary example of reversible finite tent discretizations with cycle statistics; used only to establish a different zero-credit background. | [arXiv primary record](https://arxiv.org/abs/cond-mat/0412366). |
| `ChoiEtAl2026` | Hyojeong Choi, Gangsan Kim, Hong-Yeop Song, Sangung Shin, Chulho Lee, and Hongjun Noh, “Some New Maximally Chaotic Discrete Maps,” *Entropy* 28(1) (2026), article 131, DOI `10.3390/e28010131`. | Different bijective finite skew-tent construction over integer grids; used only as zero-credit finite-map background. | [Official publisher DOI record](https://doi.org/10.3390/e28010131). |

## Claim-level audit

- Milnor--Thurston directly studies iterated interval maps and supplies the
  broad piecewise-monotone framework named in the manuscript.
- Kuzovlev's title, abstract, and primary record explicitly concern unitary
  discrete tent maps and periodic-orbit length distributions.
- Choi et al.'s publisher metadata and abstract explicitly describe symmetric
  discrete skew-tent maps and a new map proved bijective on finite integer
  grids.
- None of these records states
  `d -> gcd(p^e,d^2+p^e/d)`, its odd-prime valuation identity, or the complete
  formulas proved in the paper.

## Audit conclusion and non-hit boundary

The bounded literal searches recorded in the algebraic scout did not locate a
direct owner for the gcd map or the exact theorem conjunction.  This is only a
bounded non-hit.  The manuscript therefore makes no novelty or priority claim
and labels general interval/tent theory as zero credit.  A later direct owner,
or a judgment that the divisor carrier is merely decorative, is a kill
condition.  External status remains `HOLD_EXTERNAL`.
