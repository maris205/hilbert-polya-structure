# Independent OR Stage-1 replay receipt

2026-09-05 UTC. All commands were actually executed from the workspace
root `/root/autodl-tmp/symbolic_dynamics`. This receipt describes finite
replay evidence, not the source of all-length mathematical validity.

After one developmental n<=7 check and one complete initial-version run,
the final verifier added full polynomial coefficients and same-length
family-conjugacy controls. It was then run in two fresh Python processes:

```sh
python3 docs/papers197_201_sequence/reviews/or_stage1_20260905/verify_bitplane_paths.py > /tmp/or-review-stage1.lgItVl/independent_run1.txt
python3 docs/papers197_201_sequence/reviews/or_stage1_20260905/verify_bitplane_paths.py > /tmp/or-review-stage1.lgItVl/independent_run2.txt
cmp /tmp/or-review-stage1.lgItVl/independent_run1.txt /tmp/or-review-stage1.lgItVl/independent_run2.txt
```

Both processes and `cmp` exited 0. Each stdout has 3,962,690 assertions,
status PASS, and zero critical/major/minor findings in the checked claims.
Both SHA-256 values are
`dd36cf3dce106e9db232265b5d266e91180ba236bb40110059439c81ed65f4fd`.
The durable `CANONICAL.txt` is the complete identical transcript, not a
summary or a wrapper whose hash is confused with stdout. Temporary paths
are a record of actual execution, not required to replay the verifier.

Independent scope: all 797,160 states and targets at n=1..12; complete
predecessor sets by closed source-edge walks; functional graphs by path
discovery; all core membership/actions and maximum-fibre targets; all
tested positive-one run states' exact token clocks; weighted polynomial
coefficients and image matrix certificate; fixed counts through t=6n.
The 7,280 parking configurations are all weak compositions in boxes
`(k,Mmax)=(1,12),(2,8),(3,5),(4,4)`. Structured original-word witnesses
reach n=150; they are not exhaustive graphs at that length.

The frozen author inputs were checked separately and the author code was
freshly replayed:

```sh
python3 docs/papers197_201_sequence/scouting/replacement_after_cmm_20260905/verify_or_ternary.py > /tmp/or-review-stage1.lgItVl/author_replay.txt
cmp /tmp/or-review-stage1.lgItVl/author_replay.txt docs/papers197_201_sequence/scouting/replacement_after_cmm_20260905/OR_CANONICAL.txt
```

The author replay exits 0, makes 3,518,531 assertions, and its stdout hash is
`7b0df3ad4da0543e9c1a015f5573efe6b4c649e42246f222cc51989027d38610`.
The separate author receipt reports two author runs; this reviewer does not
claim to have independently witnessed those old processes. The reviewer
actually ran this one fresh author replay plus the two independent runs.

Input-manifest verification was executed in the author directory:
`sha256sum -c STAGE1_AUTHOR_INPUT_SHA256SUMS`; all nine entries passed.
The review's `PINNED_INPUTS.sha256` uses workspace-root-relative paths.
The review's non-self `SHA256SUMS` uses paths relative to this review folder.
No runtime third-party Python dependency, author import, external reviewer
API, GPU experiment, manuscript build or paper visual QA is involved.
