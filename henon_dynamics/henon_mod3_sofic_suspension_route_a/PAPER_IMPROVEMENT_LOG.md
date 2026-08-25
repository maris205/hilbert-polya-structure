# C140 paper improvement log

No external reviewer, numerical review score, acceptance prediction, or venue
claim was used.  Two genuine internal proof/claim/presentation audits were
followed by source edits, fixed-epoch recompilation, and retained PDFs.

## Round 0: baseline

- Artifact: `paper/main_round0_original.pdf`
- SHA-256: `1f0436449b859c3b7e74cf00e0867a1cd243e621b305a820fe96e9d16fca9f65`
- Pages: 2

The baseline stated strict soficity, the three-state cover, the exceptional
all-zero correction, intrinsic rational zeta, and primitive product.  The
first internal audit found compressed quantifiers in the non-SFT proof,
insufficiently explicit entropy monotonicity, and a 4.88pt overfull box at the
scope literal.

## Round 1: local proof and layout revision

- Artifact: `paper/main_round1.pdf`
- SHA-256: `8b4d31942d872d8e93ea9f7c0cabf130128f76e7eb745f2ba637a195e81d19dc`
- Pages: 2

The revision supplied the one-`1` local-window embedding, strong connectivity,
the positive derivative of the entropy equation, and a standalone scope line
that removed the overfull box.  A second independent internal audit found one
remaining MAJOR proof gap: distinct states in the displayed graph alone did
not provide a cross-presentation lower bound for the right Fischer cover.  It
also requested an explicit definition of the weighted fixed-point sum and a
fixed-nonzero-specialization qualifier for the imaginary-period control.

## Round 2: Fischer residual and ownership revision

- Artifacts: `paper/main_round2.pdf`, `paper/main.pdf`
- SHA-256: `1e41191864c8a54e672116e181d8be2dc40c27a82db2fefc542ecfe7552ed513`
- Pages: 2

The final proof uses synchronizing pasts `1,10,100`, their three intrinsic
residual follower languages, and separating futures `1,01,001`; the
follower-set construction now supplies the three-state lower bound across
presentations.  The final paper defines
`F_n=sum_[Fix(sigma^n|X3)]u^N1 v^N0` before applying the correction.  The
imaginary-period statement is restricted to fixed `z=1`, while the cover
determinant, intrinsic inverse zeta, and absent natural Fredholm owner remain
separate.

The final source passes two fresh isolated fixed-epoch builds byte for byte.
Every font is embedded; both final logs are free of warnings, overfull or
underfull boxes, undefined references/citations, and multiply defined labels.
Both rendered pages were visually inspected without clipping, overlap,
truncation, broken formulas, or unintended blank pages.
