# P99 — Unipotent shear on fixed-index sublattices

Status: **internal Stage 2 final QA PASS / external HOLD**.

For each integer `N >= 1`, this note studies the permutation induced by the
unipotent matrix `U=[[1,1],[0,1]]` on the finite set of index-`N`
sublattices of `Z^2`.  It is a finite arithmetic dynamical system, not a
symbolic recoding of an SFT and not a claim about higher-rank subgroup growth.

The frozen theorem package is:

1. every lattice has unique column-HNF coordinates
   `L(a,b,c)=Z(a,0)+Z(b,c)`, with `ac=N` and `0<=b<a`, and the shear is
   exactly `(a,b,c) -> (a,b+c mod a,c)`;
2. the `a`-layer has `gcd(a,N/a)` cycles, each of length
   `a/gcd(a,N/a)`, yielding the complete cycle inventory, every fixed count,
   Möbius reconstruction, and the finite Artin--Mazur zeta product;
3. for `N=p^r`, the inventory collapses to a sparse parity family and
   `#Fix(T^n)` is a closed `v_p(n)` staircase;
4. the maximal period is exactly `N` and occurs once, so the complete cycle,
   fixed, or formal-zeta data recover the index; and
5. HNF, divisor-sum enumeration, finite-index subgroup theory, subgroup-zeta
   theory, and Hecke ownership are explicitly subtracted from the residual
   result.

Run the exact control with:

```bash
python3 code/verify_shear_sublattices.py
```

The deterministic output is frozen in
[`code/verification_output.txt`](code/verification_output.txt) and explained
in [`CONTROL_RESULTS.md`](CONTROL_RESULTS.md).  Build the paper with the
four-stage command in [`BUILD.md`](BUILD.md).  The four-page PDF, two-round
hostile review, final mechanical checks, and package hashes are recorded in
[`HOSTILE_REVIEW.md`](HOSTILE_REVIEW.md), [`FINAL_QA.md`](FINAL_QA.md), and
[`SHA256SUMS`](SHA256SUMS).  Public release, submission, contact, and absolute
novelty or priority language remain unauthorized while the owner audit is on
**HOLD**.
