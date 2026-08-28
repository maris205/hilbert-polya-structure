# Claims and evidence

| Claim | Proof/evidence |
|---|---|
| The two staggered layers are involutions; `T_m` is a permutation with inverse `A_m B_m` and reversing symmetry `A_m T_m A_m = T_m^{-1}` | `main.tex`, Proposition 3.3 |
| Every update preserves total Hamming weight | `main.tex`, Proposition 3.3 |
| Frozen configurations are exactly the cyclic block words accepted by the displayed `8 x 8` matrix `M` | `main.tex`, Lemma 4.1 and Theorem 4.2 |
| `f_m = #Fix(T_m) = tr(M^m)` for every `m >= 1` | `main.tex`, Theorem 4.2 |
| `rank(M)=2` and `det(lambda I-M)=lambda^6(lambda^2-5lambda+3)` | `main.tex`, Lemma 5.1; row-space argument plus `tr(M)=5`, `tr(M^2)=19` |
| Closed fixed count and recurrence | `main.tex`, Theorem 5.2 |
| Frozen-set entropy is `log((5+sqrt(13))/2)` per three-site block and one third of this per original site | `main.tex`, Corollary 5.3 |
| `zeta_fr(z)=(1-5z+3z^2)^{-1}` is the zeta function of the spatial block shift on the frozen SFT | `main.tex`, Corollary 5.3 and Remark 5.4 |
| No temporal zeta, unbounded-period theorem, or integrability claim is made | abstract; end of Introduction; Remark 5.4; Sections 6--7 |
| Literal-rule exhaustive controls agree through `m=6` | `code/verify_fredkin.py`; exact results in `CONTROL_RESULTS.md` |

## Evidence hierarchy

The all-size claims are established symbolically in the paper.  Exhaustive
enumeration is a finite regression check only.  In particular, the temporal
cycle table is not evidence for an all-size period theorem.

## Ownership firewall

- Fredkin--Toffoli own conservative logic and the controlled interchange
  primitive.
- Toffoli--Margolus and Kari own the general reversible block-partition
  architecture.
- Morita surveys Fredkin gates embedded in reversible cellular automata.
- Singh--Vasseur--Gopalakrishnan directly own the Fredkin staircase model,
  which has three layers of four-site constrained-swap gates and a different
  transport/integrability objective.

The residual object is the explicit frozen-set transfer matrix, recurrence,
entropy, and spatial zeta for the two-layer three-bit map defined in the
paper.  The package makes no absolute novelty or priority claim.
