# C73 test report

```text
producer: PREFREEZE_G3_PASS
independent projective-rank checker: PASS
SymPy/GAP polynomial cross-check: POLYNOMIAL_CROSSCHECK_PASS
clean-process replay: REPLAY_PASS
hostile mutation test: PASS, 35/35 rejected
```

The checker rebuilds the graph from mod-three determinants and enumerates all
65536 deletion sets without reading C72's support polynomial.  SymPy derives
the independent-set, vertex-cover, and transversal polynomials and enumerates
all 16 block-failure states to recover both reliability formulae.  GAP checks
the order of the structural direct-product subgroup after the paper's
hypergraph-orbit classification.
