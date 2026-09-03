# P173 — Random quotient-leakage erosion

**Round:** dual-review closed; final reproducibility QA complete  
**Gate:** `SPIKE_2_COLLISION_RISK`  
**External lifecycle:** `HOLD_EXTERNAL`

For `V=F_q^n`, this finite Markov chain samples a fresh uniform endomorphism
`T` at every epoch and updates `U` to `U intersect T^(-1)(U)`.  The paper
reduces the literal update to the kernel of a uniform map `U -> V/U`, then
proves exact ambient fibres for every labelled target, every-time labelled
transition probabilities, the complete algebraic spectrum, and a forced
Jordan ladder indexed by complementary dimensions.

Fulman--Goldstein's uniform finite-field rank/nullity law, Goldman--Rota's
Gaussian incidence, fixed-kernel symmetry, the elementary ambient lift, and
generic triangular/Jordan/absorption algebra are assigned zero contribution
credit.  Evans's dimension precursor and Van Peski's labelled uniform-square-
kernel chain/fixed-target count are also direct zero-credit owners.  Their
codomain has current dimension `a`; P173's fresh fixed-ambient leakage uses
the complementary codomain `n-a`, and they do not provide its Jordan ladder.
Balakin is retained only as accurately labelled sparse/nonuniform background.
P109, P162, P165, P168, and same-batch P172 are individually subtracted.  In
particular, P172 has specified-box set-image occupancy and one terminal
`J_2`, whereas P173 has a linear injection fibre and a complementary-
dimension `J_2` ladder; neither residual transfers to the other.  The
bounded owner-search non-hit is not a novelty claim; external circulation
remains on hold.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p173.py

pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Hostile Review A's `0 Critical / 2 Major / 2 Minor` and Hostile Review B's
`0 Critical / 2 Major / 1 Minor` are all repaired and delta-closed; both now
have zero open findings.  Two independent source-only cold builds reproduce
`main.pdf` and `main_round2.pdf` byte for byte.  Fresh author, Review-A, and
Review-B replays match their canonical transcripts, final PDF QA passes, and
the complete paper-local non-self `SHA256SUMS` verifies all 53 entries.
Lifecycle remains `SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`.
