# P214 manuscript Review A: source and proof review

2026-09-11 UTC. Reviewer `/root/p214_review_a_finish` starts from the accepted
physical Round0 and has not contributed to P214's candidate proof, manuscript,
author verifier, source audit, build, lifecycle closure or freeze. This is an
internal process-separated review, not blind, external or specialist review.

## Proof audit

The recurrence proof is sound. Once `x_2=x(t+y)` is in `t^2R`, every later
multiplier is `t` plus an element of `t^2R` and therefore has valuation one.
For `v(y)>=2`, both parity chains gain one valuation per update. For `v(y)=1`,
the even chain can cancel but the odd chain is exact and alone forces deadline
`2m-2`. The first simultaneous zero is one index after the last nonzero term,
including the zero-coordinate and `m=2` boundary cases. The ideal-rectangle
count then gives exactly `q^h` states of depth at most `h`.

The fibre proof is also sound. Fixing the first output fixes `y=u`; the other
equation is multiplication by `t+u` on `I`. For valuation stratum `d<=m-2`,
its image is `t^(d+1)R`, kernel is `t^(m-d)R`, and every nonempty fibre has
`q^d` elements. The saturated `d=m-1` case correctly uses the kernel inside
`I`, yielding the `q` maximal targets and the stated image sum. Unequal
positive fibre sizes for `m>=3` obstruct conjugacy to a finite-group
endomorphism. The two-sided multiplication adapter is not misused as an
iterate conjugacy, and `m=2` is correctly isolated as `F=L`.

## Independent finite check design

`verify.py` uses no imports, files, author code or author canonical. It builds
the literal map on all 5,271 states for `q=2,3,4`, `m=2,3,4`; computes depths
by reverse breadth layers from zero; forms each multiplication matrix on `I`;
and obtains image/kernel dimensions by its own finite-field Gaussian
elimination. Thus the temporal and fibre routes are materially independent
of the author's recurrence/valuation implementation. Execution remains
pending a separate root grant.

## Sources and subtraction

The frozen source audit accurately limits both references. Bors is used only
for finite endomorphism context; the fibre-coset fact needed here is proved
directly. El Abdalaoui et al. supplies complex Fibonacci-map background only;
no theorem is transferred. The manuscript explicitly deducts the one-step
multiplication mechanism and the linear clock shape. It does not claim global
novelty, arbitrary chain-ring extension, all-time fibres or a classification
of functional graphs.

## Finding

Minor A1: the abstract calls `F(x,y)=(y,x(t+y))` a "bilinear map". As a map
of the pair `(x,y)`, its second coordinate is `tx+xy`, so the displayed map is
polynomial/nonlinear, not bilinear. Replace only `bilinear map` by
`polynomial map` in `sections/0_abstract.tex`. This is terminology repair,
not a theorem, proof, parameter, verifier, bibliography or data change.

Current source-stage census: Critical 0, Major 0, Minor 1. No live edit,
execution, verdict, accepted delta or Round1 is claimed at this stage.
OWNER_AMBER / HOLD_EXTERNAL.
