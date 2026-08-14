# Hostile Review

## Round 0: mathematical object audit

**Issue:** The first draft treated the square full multiplier-field norm as
the unique natural rationalization of the cyclic determinant.

**Fix:** Observe that the determinant already lies in the fixed trace field.
Separate the full-field square, the minimal trace-field Lehmer--Pierce
sequence, and the ideal packet.  This changed the paper from a blanket no-go
to a three-lane theorem.

## Round 1: scope and evaluator audit

**Issues:** The ring of the determinant ideal equality was implicit;
primitive divisor was undefined; an all-index recurrence risked an inflated
A3 score.

**Fixes:** State that the trace-field principal ideal is extended to
$\mathcal O_K$, define primitive rational divisor, and set `A3_FAIL` because
no global H6 analytic continuation exists.

## Round 2: executable integrity audit

**Issue:** Monic, reciprocal, and unit checks did not explicitly test that
the three polynomials are irreducible minimal polynomials.

**Fix:** Add irreducibility to the acceptance gate and a dedicated unit test.
Also lock $f_{-L_3}(X)=f_{L_3}(-X)$.

## Final verdict

`PASS` within the stated boundary.  The full-field square obstruction is
proved; the trace-field and ideal packet survivor is not promoted beyond its
evidence.  No external reviewer or subagent was used in these rounds.
