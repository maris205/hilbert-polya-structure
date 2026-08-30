# C253 code contract

The producer emits exact rates, fixation, Green, time, and reversible-weight
receipts.  The checker independently reconstructs them over Fraction fields.
SymPy verifies recurrences, inverse identities, and limits.  Replay checks byte
determinism; mutation checks tamper rejection; the release script closes the
manifest and PDF gates.
