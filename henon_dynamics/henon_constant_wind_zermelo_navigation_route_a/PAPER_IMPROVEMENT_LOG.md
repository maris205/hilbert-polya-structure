# Two-round paper improvement log

## Round 0: core atlas

The original manuscript derived the fixed-time translated ball and the
weak/critical/strong reachability and value formulas. It already selected
the smaller strong-wind root but did not fully expose the optimizer equality
case, smooth-domain qualifications, or degenerate faces.

## Review 1 and implementation

Round 1 added substantive theorem content:

- complete attainable-time sets, including the finite strong-wind window;
- a rigorous equality-in-triangle-inequality proof of the unique constant
  optimal control;
- the implicit gradient and correctly signed HJB equation;
- rotation, target homogeneity, and common-velocity scaling;
- critical half-space and Mach-cone regularity;
- separate \(W=0\), \(c=0\), \(y=0\), and \(W=c=0\) faces.

## Review 2 and implementation

Round 2 red-teamed branch signs, root choice, and evidence semantics. It
added 29 cases, 12 HJB/scaling probes, independent checker/SymPy/replay
lanes, repaired-hash mutations, strict JSON/YAML handling, and deterministic
PDF/manifest closure. Claim language was narrowed: no variable-wind,
obstacle, manifold, global strong-wind Finsler, novelty, or arithmetic claim
survives.
