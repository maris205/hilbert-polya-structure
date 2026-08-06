# Frozen-protocol amendment log

## Version 1 — superseded

The original M2 control put \(F=H\) and \(F=H^2\) on one five-cycle.  Although
both choices commute with \(H\) and have the same ordinary fixed-count
sequence, neither commutes with a reversor satisfying \(RHR=H^{-1}\).  The
control therefore did not live in the structural category claimed in the
paper.

The v1 run is superseded.  Its pre-amendment hashes are retained here only to
make the change visible:

- certificate: \`7ea4a780...\`;
- independent check: \`95c50f...\`;
- producer: \`638464...\`;
- checker: \`efd373...\`.

These abbreviated historical hashes are not verification targets; the full
v2 hashes are recorded in \`results/RESULTS.md\` after regeneration.

## Version 2 — current frozen protocol

The replacement state space is

\[
S=\{\pm1\}\times\mathbb Z/5,
\]

with

\[
H(\varepsilon,i)=(\varepsilon,i+1),\qquad
R(\varepsilon,i)=(-\varepsilon,-i),\qquad
F_c(\varepsilon,i)=(\varepsilon,i+\varepsilon c),\quad c=1,2.
\]

Now \(RHR=H^{-1}\) and each \(F_c\) commutes with both \(H\) and \(R\).  The
ordinary traces remain identical while the joint traces differ.  The
independent checker enumerates all ten states and verifies these relations
instead of trusting producer booleans.

No parameter, finite-field cell, period-five coefficient, literature target,
or Route-A threshold was changed.  The amendment repairs a symmetry error; it
does not tune the experiment toward a desired result.

Final v2 verification hashes:

- certificate: `851ca31f62fb508ad806c26084eab9fe092d5ee037bf99f0cb811cbccf7f8eb8`;
- independent check: `4784e8b2fbf98ad835a5f1c0ef9217de14537adcff486046e74a6b0f47e93778`;
- producer: `0e1c64ed3554a1625c9b720075b815a0b6e09152ab316fb7f2f76eb65f31263d`;
- checker: `47a01350e87394286a123ec5a21a704556c6a73cf80b0891b6fb64570497c0da`;
- frozen protocol: `fa88bd1003a62b8025922aec72314af452e0f8e48f18184ac35ef7697fce1e31`;
- frozen experiment plan: `f02d1ef77682c0ae54266cafbf0650ade4b928d38c1366168e3db83dba409bf9`.
