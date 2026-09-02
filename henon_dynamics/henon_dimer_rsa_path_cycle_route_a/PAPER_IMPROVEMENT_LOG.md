# Paper improvement log

## Round 0 — original draft

The original draft fixed the precise finite graph/process owner, proved the
path convolution and Riccati OGF, extracted the exact mean, and derived the
cycle identity.  Its deliberate limitations were a first-moment focus and a
compressed treatment of support and audit boundaries.

## Round 1 — mathematical strengthening

Substantive additions:

- differentiated the Riccati equation at arbitrary order and isolated an
  all-`r` triangular linear ODE;
- solved both `H_1` and `H_2`, displayed their Laurent pole parts, and proved
  `Var(M_n)=e^{-4}n+2e^{-4}+o(1)`;
- replaced informal jamming bounds with the complete binary-gap construction,
  proving that every integer between the exact support endpoints occurs;
- separated empty/singleton paths, the simple-cycle domain, continuous-priority
  ties, and maximal-versus-maximum semantics.

## Round 2 — integrity, reproducibility, and evaluation strengthening

Substantive additions:

- documented the producer-independent processed-edge/matched-vertex bitmask
  enumeration and independent all-factorial-moment reconstruction;
- added canonical-hash replay and repaired-hash/drop-replace/duplicate-key
  hostile testing;
- froze source metadata, classical ownership, collision distinctions, finite
  evidence limits, and the `HEN-O275` obstruction;
- added the full Route-A gate table and explicit nonclaims;
- added data/code availability, ethics, conflicts, funding, CRediT, and AI-use
  declarations.

Each round is compiled from the same auditable source under a distinct
`\CRevisionRound` branch.  The three archived PDFs are substantively and
bytewise distinct; each is rebuilt twice from fresh directories.
