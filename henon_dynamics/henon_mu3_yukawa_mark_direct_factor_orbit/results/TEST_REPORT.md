# C70 test report

```text
producer: PREFREEZE_G3_PASS
independent block checker: PASS
SymPy/GAP group cross-check: GROUP_CROSSCHECK_PASS
clean-process replay: REPLAY_PASS
hostile mutation test: PASS, 30/30 mutations rejected
```

The producer uses the conjugate-partition automorphism formula.  The checker
instead counts endomorphism blocks and imposes invertibility on each reduction.
GAP independently returns `|Aut(D)|=384`; SymPy verifies the large prime
factorizations.  The Birkhoff subgroup count is reproduced using independent
Gaussian-binomial recurrences and product formulas.
