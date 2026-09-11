# Exact-five run01 preserved binding-label failure

The sealed preparation02 auditor exited 1 before producing a result because
P211's accepted historical build receipts use `build_1` and `build_2` labels,
while the exact-five binding assigns the normalized roles `terminal01` and
`terminal02`. The selected receipt text therefore failed the auditor's literal
terminal-role check. No paper evidence changed and this is not a batch PASS.

Preparation03 changes only those two P211 evidence paths to a new documentary
identity adapter that pins the original receipts and explicitly maps
`terminal01=build_1`, `terminal02=build_2`. The auditor logic is unchanged.
