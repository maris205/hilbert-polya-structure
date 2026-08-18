# HCS-C63 adaptive idea report

Date: 2026-08-18

## Input boundary

C62 supplies a complete 16-type fixed-field dictionary for the two lambda
shadows of the released C61 `W(E_6)` Gassmann pair.  The C63 producer binds
the exact C61 group bytes and the C62 atlas/dictionary hashes, then rebuilds
the character calculation independently.

## Candidate decision

| candidate | decision | reason |
|---|---|---|
| primitive four-term relation exposed by `Lambda^2` | **SELECT** | new support-restricted Burnside relation with exact rank/minimal-support certificate |
| full 16-type kernel rank only | supporting gate | necessary ambient certificate, but too broad as the headline |
| `S9-S10` order-4 collision | reject as novelty | inherited C60 collision; retain only as a hostile control |
| new arithmetic/local atlas for all 16 fields | defer | requires a separate source-bound arithmetic layer and risks salami overlap |

## Selected C63 target

For `Y_i=G/S_i`, prove the exact relation
\[
Y_2+Y_3+Y_5+Y_6-Y_{11}-Y_{12}-Y_{13}-Y_{14}=0
\]
in permutation characters, show that its eight stabilizer types are paired
across nonconjugate plus/minus rows, and certify that it is the exterior-square
difference from C62.  The full restricted character matrix has rank 13 and
kernel dimension 3; this supplies the ambient certificate and separates the
new relation from the inherited C61 and C60 kernel directions.

The scope literal remains `NO_BAD_EULER_OR_ROOT_NUMBER`.
