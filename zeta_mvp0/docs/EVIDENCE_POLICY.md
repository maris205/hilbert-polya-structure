# Evidence policy

The programme uses four evidence labels.

1. **Theorem / identity:** a written proof with all assumptions and source
   dependencies identified.
2. **Computer-assisted theorem:** directed-rounding enclosures, a complete
   cover, immutable proof objects, and an independent checker all pass.
3. **Ordinary numerical evidence:** reproducible finite-precision computation
   useful for discovery but not a proof.
4. **Heuristic:** a mechanism or analogy that suggests an experiment and
   licenses no mathematical conclusion.

Prime tables and zeta-zero arrays are forbidden as hidden selection inputs to
a claimed endogenous prime carrier.  If they are ever used for an explicitly
post-selection diagnostic, that use must be named and cannot promote the P or
Z gates.

Failed, stopped, invalid, and superseded runs are retained when needed for
provenance.  Their internal historical `PASS` strings do not license a current
claim.  Frozen manuscript PDFs and accepted result archives are never silently
overwritten.

## Repository-availability boundary

Mathematical evidence level and repository availability are separate axes.
Every paper or milestone listed in the programme README must be marked as one
of:

1. **mirrored:** protocols, source, proof/result objects, independent checks,
   claim boundary, and release hashes are present in the paper directory;
2. **placeholder / transfer pending:** a result may be accepted in the source
   workspace, but this repository does not yet contain the evidence required
   to reproduce it;
3. **roadmap only:** the item is a research target, not a result.

A placeholder may summarize a source-workspace result, but it must not call
itself repository-reproducible.  Promotion to mirrored status requires a
controlled copy followed by link, hash, status, and minimal-command
verification.  The programme README and global ledger must be updated in the
same change.
