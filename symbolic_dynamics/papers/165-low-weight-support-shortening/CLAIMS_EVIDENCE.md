# P165 claims-to-evidence map

**Lifecycle:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

| Claim | Proof interface | Exact control |
|---|---|---|
| literal padded shortening is a finite self-map | intersection with the coordinate-zero subspace | closure and same-length checks in every finite box |
| nonzero steps are proper and surviving distance doubles | a minimum word is purged; every lighter survivor would support itself inside the purge set | every enumerated nonzero code over `F_2`, `F_3`, `F_4`, `F_5` |
| zero is uniquely recurrent and the height is `floor(log2(n+1))` | disjoint purge sets have sizes at least `1,2,4,...`; direct sums of dyadic full-support lines attain equality | exact orbit depths and constructive height witnesses |
| nonzero `D` lies in `im(T^t)` iff `d(D)>=2^t` and `z(D)>=2^t-1` | necessity from distance/support budgets; sufficiency from disjoint dyadic lines on zero coordinates | every target at all tested times |
| every nonzero-target source needs `t` dimensions and `2^t-1` new support sites | sum positive codimension drops and disjoint purge blocks | every enumerated source/time with nonzero endpoint |
| simultaneous extremizers have the direct-sum form and formula (7) | equality forces `|U_i|=d_i=2^i`; a minimum word is then supported exactly on `U_i` | structural layer checks and targetwise exact counts |
| zero-target formula is not a whole-fibre formula | `(T^t)^-1(0)={C:tau(C)<=t}`; exact-depth minimizers are a proper slice | explicit `n=2,t=1` counter-sentinel and all small boxes |

## Ownership ceiling

Jibril et al.'s low-weight hitting-set shortening and its one-step distance
increase receive zero contribution credit.  Standard code parameters,
puncturing/shortening, direct sums, repetition lines, and geometric sums are
background.  The only provisionally credited conjunction is the autonomous
iteration, exact all-time nonzero-target image criterion, and classified
extremal inverse layer.  A bounded source non-hit is not a novelty claim.
