# P117 exact-control results

The deterministic standard-library verifier exhausts all \(2^n\) labelled
cyclic binary words for \(1\le n\le16\).  For each state it computes the
literal orbit, run lengths, and one-step boundary set.  It checks:

1. the boundary-survival rule on every one-step update;
2. the induced parity eroder for every nonconstant word of even order;
3. every eventual period is one or two and preperiod zero is equivalent to
   the equal-parity run criterion;
4. exact fixed and period-two state formulas;
5. the odd and even sharp maximum-preperiod formulas; and
6. an explicit extremal witness at every order.

A second lane enumerates all 349,524 cyclic parity words of even length at
most 18.  It constructs a literal word attaining the realization cost for
each one and checks the four-unit cost drop on all 349,488 mixed cases.  The
combined canonical run executes 1,529,158 exact assertions.

Fresh command:

    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py

The canonical transcript is code/verification_output.txt.  The assertion
counter records executed exact checks, not independent mathematical claims.
The all-parameter proof is in main.tex.
