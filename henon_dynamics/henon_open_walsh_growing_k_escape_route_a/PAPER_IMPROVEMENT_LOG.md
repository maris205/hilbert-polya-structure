# C153 paper improvement log

No external or cross-model reviewer was available or claimed.  Both rounds
are genuine internal theorem/scope audits, with no numerical scores.

## Round 0 to round 1

The baseline stated the escape law but did not distinguish the signed
log-survival rate from the positive escape exponent.  Its trace-cluster prose
also listed divisor classes without saying that numerically equal complex
values must be merged, and it left the `alpha=0` initial-rank boundary implicit.

**Fix:** define both sign conventions, add the floor-limit argument and
`alpha=0` boundary, make the cluster object an equality-merged set, and add the
explicit period-two odd/even witness.

## Round 1 to round 2

The second audit found that “the alternative hole also has rank two” was not
enough to transfer the full power-rank law: rank at one step alone does not
control `rank(A0^m)`.  It also asked for a sharper A4 boundary and complete
validation denominators.

**Fix:** calculate
`chi_A0=lambda(lambda+i)(3lambda+sqrt(3))/3`, use its simple zero and two
nonzero roots to prove `rank(A0^m)=2` for every positive `m`, and only then
transfer the rank law.  Clarify that `t0=2` is only the initial power sum of
the two nonzero roots, whereas `Tr(A^0)=3`; repair the divisor-power typography
and place both period-two witness lines under the single display tag (8).
State that antiunitary/self-adjoint/full-secular limits are not constructed,
record all checker/SymPy/replay/mutation denominators, and bind the source
commit in evidence and YAML.

## Final audit

The release is checked against exact evidence, claim boundaries, two isolated
fixed-epoch builds, embedded fonts, clean logs, extracted text, rendered pages,
and disk-to-manifest closure.  The remaining limitation is structural: fixed-
period normalized traces vanish, but no full growing-`k` secular or target
limit is established.
