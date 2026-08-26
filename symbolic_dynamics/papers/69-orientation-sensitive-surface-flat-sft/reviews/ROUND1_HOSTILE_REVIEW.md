# Round 1 internal hostile review

**Scope:** mathematical and presentation audit of the complete P69 draft.  
**Reviewer status:** internal self-audit, not an independent specialist review.  
**External-release status:** HOLD.

## Re-derivations

1. **Local SFT convention:** the six labels in the relator path start at
   successive right-generator endpoints.  Under the left shift,
   `H`-fixed coordinates are constant on left cosets and therefore descend to
   the stated cover graph.  No left/right reversal was found.
2. **Gauge exponent:** a rooted spanning tree has one free gauge value at each
   of `V-1` non-root vertices.  Tree-trivial flat connections are based
   homomorphisms, so the raw connection count is
   `|K|^(V-1)|Hom(H,K)|`; no centralizer divisor belongs in this count.
3. **Cover topology:** `x_3 in H_n` and has odd orientation character, so every
   `H_n` cover is nonorientable, including even-index covers.  Euler
   characteristic gives genus `n+2`.  The element `x_1x_3^-1` proves
   surjectivity of `f` on the orientation kernel, giving orientable genus
   `m+1` for `L_m`.
4. **Power audit:** orientable gauge and Hom powers add to `4m`.
   Nonorientable powers add to `2n`, while the genus substitution gives
   `nu^(n+2)d^(-n)`.
5. **Moment audit:** orientable moments recover total degree multiplicities;
   even nonorientable moments recover `c_d^++c_d^-`; odd moments have
   coefficient `(c_d^+-c_d^-)/d`.  Indicator-zero representations are then
   recovered as `t_d-s_d`.
6. **Control pair:** the two-dimensional FS indicators are `+1` for `D_8` and
   `-1` for `Q_8`; the displayed fixed counts agree exactly with independent
   tuple enumeration.

## Findings requiring correction

### R1.1 — Terminology: the all-modulus families are not linearly nested

Calling `(H_n)` and `(L_m)` ordinary chains without qualification could imply
`H_(n+1)<=H_n`, which is false.  They are nested along divisibility.  The
revision must say explicitly that “chain” means a divisibility-directed
family and that all moduli are retained to access both nonorientable parities.

**Severity:** moderate presentation issue; theorem unaffected.

### R1.2 — Prohibited minimality phrasing

The conclusion described the control pair as occurring at the “smallest
nonabelian order” with the degree coincidence.  Even if true, this is an
unneeded minimality claim and conflicts with the package's no-priority posture.
Replace it by a neutral “small explicit order-eight example.”

**Severity:** release-boundary issue.

### R1.3 — Overfull code path

The full relative verifier path produced an overfull line in the first build.
Use the shorter filename in prose; the full path remains in BUILD.md.

**Severity:** typographic.

## No critical mathematical finding

No defect was found in the local-rule definition, gauge bijection, subgroup
topology, character exponents, finite moment inversion, or `D_8/Q_8`
separation.  The package is eligible for internal GO after resolving R1.1--R1.3
and rerunning build/control checks.  External release remains HOLD for an
independent literature and topology review.

