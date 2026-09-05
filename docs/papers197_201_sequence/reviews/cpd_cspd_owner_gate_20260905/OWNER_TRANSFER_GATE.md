# Independent CPD / CSPD owner gate

Date: 2026-09-05 UTC. Stage-1 candidate gate only, not paper Review A/B.
Verdict: **KILL_OWNER_TRANSFER / HOLD_EXTERNAL** for CSPD; **KILL_THIN_MARKED_PARKING_MARGINAL** for CPD. Neither occupies a paper slot. No mathematical defect is alleged in the surviving contracts. This is a residual-contribution threshold decision, not a claim that the exact feedback maps were published verbatim.

## Binding all-target transfer

Write `S(a)` for the site-indexed circular displacement output. Let `I_n` be the inversion-sequence box `0<=d_s<=s`, let `C(d)_s=s-d_s`, and let `N(a)_s` be the preference of the car ending at site `s` under classical no-wrap parking. The latter site normalization and its class enumeration are already in the primary 2022 Summer@ICERM slides cited below.

For every `y` in the image of `S`, there is a cyclic cut `k` with `R_k y in I_n`. Choose the site of the last arriving car and cut just after it. No earlier car could pass that still-vacant site, so every earlier displacement is at most its coordinate measured from this cut. The last car is at the final coordinate and has displacement at most `n-1`.

Subtracting `k` modulo `n` from every source preference translates the entire circular parking process and rotates its site-indexed output by `R_k`. This is a bijection of source words. Moreover, if a circular target lies in `I_n`, every source is no-wrap: its car ending at site `s` started at `s-y_s>=0` and did not cross the cut. Hence the exact set-level identity is

```
S^{-1}(y) -- a |-> a-k (mod n) -->
{ b in PF_n : N(b)=C(R_k y) }.
```

The right-hand side is precisely an already studied normalization class. Thus **all circular fibres**, not only fibres visibly lying in the no-wrap core, are transported from the earlier static owner. The target dependency intervals, their linear extensions, the rooted-forest hook specialization, and its extremal consequences do not furnish an independent inverse axis after this transfer.

The image-union identity and `a_(n+1)` count in the author's archived contract are mathematically coherent: unique cyclic decomposition of inversion sequences and `zF'/F=A/z-1` give the displayed coefficients. They are not treated as a second independent mechanism: the image is the cyclic closure of the static normalization range and the count follows by ordinary cyclic assembly. The exact two-step temporal stratification is useful scout mathematics but remains shallow statistic feedback once the inverse axis is consumed. This matches the retained T01 priority-tree kill precedent, where a literal new iteration did not rescue transferred parking fibres plus an elementary clock.

For CPD (car-indexed displacement), the earlier D05_CPA scout already reconstructs each prescribed parking outcome and gives its displacement-marked product. A multivariate marking per car and summation over outcomes recovers the CPD fibres. Its Cartesian recursion reorganizes that marginal; its one-step inversion-box/complement recurrence does not clear the residual threshold.

## Primary-source and historical scope

Primary source read: Lucas Chaves Meyles, Richter Jordaan, Sam Sehayek, Ethan Spingarn, *Parking Functions of Fixed Displacement*, Summer@ICERM, 3 August 2022, [slides](https://app.icerm.brown.edu/assets/372/4323/4323_3429_ChavesMeyles-Spingarn-Jordaan_080320221400_Slides.pdf). PDF page 12 defines partition-preserving order by placing preferences at their occupied sites. Pages 80–84 give precedence-poset / linear-extension enumeration of classes. The 27 MB PDF was read locally after web extraction rejected its size; its content hash is pinned below. The precise all-circular-fibre transfer above is the reviewer's own derivation, not represented as a quotation or explicit theorem of the slides.

Near primary sources inspected: Kang–Selig–Yang–Zhang–Zhu, [arXiv:2310.06560](https://arxiv.org/abs/2310.06560), especially its Section 3 displacement discussion; Kenyon–Yin, [arXiv:2103.17180](https://arxiv.org/abs/2103.17180); Selig–Zhu, [Parking functions and Lukasiewicz paths](https://www.dmlett.com/archive/v14/DML24_v14_pp77-84.pdf). Kang et al.'s cyclic parking functions are a subset of line parking functions, not the all-words circular carrier here. These are near owners, not evidence of a literal-map repeat. The MVP algorithm in arXiv:2207.13041 is different and is not attributed as the direct owner.

Retained internal records checked: D05_CPA in the P172–176 fresh-geometry kill ledger, PK1 in P132–136 combinatorial scouting, and T01 in P142–146 combinatorial scouting. Available manuscripts and kill records do not include missing P51–56 manuscripts; no complete-history clearance is claimed.

## Independent computation

`verify_owner_transfer.py` imports no author code. It uses free-site-list parking, constructs complete source sets, and compares every rotated target fibre to the complete classical normalization class. It separately derives circular dependency transitive closures, subset-DP linear-extension counts, and the forest hook specialization. Exhaustive n=1..6 covers 50,069 source words and 3,996 nonempty site targets. Depth populations, complement dynamics, unique maximum, and all target transfers pass 140,348 assertions per run.

After the initial run, two additional fresh subprocess runs matched the checked-in canonical transcript byte for byte. This establishes reproducibility of the bounded transfer control; all-parameter validity rests on the proof above. No author package was modified by this reviewer.
