# Exact validation plan

The theorem is analytic.  Computation tests frozen conventions and singular
faces rather than substituting a finite census for the proof.

1. Generate 20 strongly connected regular graphs: directed cycles, complete
   digraphs, and two-out circulants.
2. Cross each graph with three recovery scales and four exact threshold ratios
   to obtain 240 rational rows.
3. Verify `s(beta*A-delta*I)=beta*r-delta`, the uniform endemic state, the
   endemic Perron Jacobian rate, and the equality coefficient.
4. On every equality row, verify 12 rational scalar time samples, giving 720
   critical receipts.
5. Reconstruct independently, run symbolic checks, byte replay, and hostile
   repaired-hash mutations.

No GPU experiment is appropriate: the claim is an all-parameter theorem and
the exact finite rows are deterministic regression oracles.
