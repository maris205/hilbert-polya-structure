# Independent Stage-2 audit: reducible tree-shift phase allocation

## Verdict

`STAGE2_CLEAN`

This verdict is limited to the frozen theorem/proof/validation package at
`/tmp/p49_tree_stage2`.  It is not a manuscript, installation, priority, or
publication verdict.

## Byte and replay closure

- The self-excluding candidate manifest has 16 regular-file rows and SHA-256
  `bea7a189ea0b3472cc6b469eb36e6460b60c4bae66265659b19af6e89883f0da`.
- `verify_manifest.py` passed with zero cache, symlink, or nonregular nodes.
- `sha256sum -c SHA256SUMS.txt` passed for all 16 rows before and after the
  independent validation replay.
- `python3 -B run_validation.py` reproduced all five evidence hashes and the
  stored total of 73,517 assertions.

## Independent exact arithmetic

The root-side checker does not import either candidate engine.  It uses
`fractions.Fraction`, direct weak-composition enumeration, direct periodic
weighted sums, and a separate nested-grid optimizer.  Its script SHA-256 is
`183946edb626086303e7970a055d576408d49413c457ab3e4be58793c4d8c447`;
its canonical result SHA-256 is
`13662cb876f11356a484f956160839ae7ae563657b4b21bd1f70232f54fc1fef`.

It independently passed:

- 1,740 nonconstant phase profiles;
- 127,500 integer compositions and the same number of constant-convolution
  equivalences;
- 37,440 residue-subsequence prefix checks;
- 30 closed `p=2` even/odd cases;
- 9 nested denominator-grid monotonicity checks;
- the mandatory nondivisible saturation witness
  `p=4,d=2,a=(2,3,2,3),m=(1,1,0,0)`.

## Proof audit

The written proof closes the infinite statements independently of the finite
census:

1. exact complete-block cylinder counts plus the compatible uniform product
   measure give matching Hausdorff upper and lower bounds at the liminf scale;
2. each fixed transient phase allocation has the displayed `H(b)` dimension,
   and the root stratum is a finite union, so the integer optimizer is exact;
3. mean preservation and invertibility of the circular `H` kernel make
   saturation equivalent to constant convolution;
4. divisibility necessity is asserted only under full nonzero Fourier support,
   while the period-two `p=4,d=2` witness blocks the false unconditional iff;
5. the `p=2` formulas include the equal-phase boundary;
6. the `L`-level proof explicitly embeds `m` as `d m` and obtains convergence
   from a balanced integer composition with an `O(d^{-L})` bound;
7. the four-state example has core dimension `log(2)/3` and full dimension
   `log(2)/2` by the same exact optimizer.

No BLW primitive/equality specialization or spectral-radius dimension bound is
used.  The source lock accurately treats the literal arXiv-v2 tension as a
version-specific firewall and credits prior reducible *topological entropy*
mechanisms without transferring that credit to the new Hausdorff formula.

## Boundaries retained

The package does not prove an arbitrary reducible variational principle,
return-edge formulas, incomplete cyclic blocks, nontransient strengthening, or
unconditional `p|d` necessity.  Those nonclaims are required for this verdict.

No authority, Git, README, mirror, manuscript, figure, seal, or installation
path was written during this audit.
