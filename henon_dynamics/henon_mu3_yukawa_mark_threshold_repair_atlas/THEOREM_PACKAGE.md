# C80 theorem package

For every target subgroup row `H`, the threshold is the distance from the
retained mask to the antichain of inclusion-minimal named supports whose
closure contains `H`:

```text
tau_H(D) = min_{M minimal, H subset Phi(M)} |M \ A|.
```

The identity follows by repeatedly removing redundant labels from any
target-containing support.  C80 computes this antichain independently from
the C75 point-set addition law and checks the resulting value against every
stored profile entry.  The target-inclusion order gives the monotonicity
`H1 subset H2 => tau_H1(D) <= tau_H2(D)`.  The `H=Q` row reproduces C78's
four-valued repair distribution exactly.

The theorem concerns only the named 16-label presentation and the 20 listed
subgroups; no complete marks or arithmetic interpretation is inferred.
