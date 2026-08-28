# Experiment plan

## Theorem work

1. Fix the atomic basis, Pauli signs, excitation convention and block index.
2. Compute `[H,N]`, isolate `|g,0>`, and derive the `n>=1` block in the ordered
   basis `{|e,n-1>,|g,n>}`.
3. Square the traceless Pauli part to obtain the dressed pair and exact
   exponential; derive transition probability, trace, determinant and
   unitarity.
4. Prove the finite-active-set population revival equivalence and state the
   additional center/vacuum phase alignment needed for state-vector revival.
5. Close zero coupling, resonance, vacuum, coupling-sign gauge, finite-cutoff
   and full-Fock operator boundaries.

## Executable evidence

Serialize 32 blocks and 64 propagator cases across resonance, two detuned
sign/coupling cases and the degenerate uncoupled face.  The independent
checker reconstructs every exact scalar, high-precision energy/probability,
unitarity/trace/determinant identity and a direct 10-dimensional truncated
Fock commutator.  SymPy separately rebuilds the generic Pauli algebra and
revival parity.  Require byte replay plus repaired-hash semantic/schema,
unknown-key and stale-hash rejection.

## Paper and release

Compile three content-distinct revisions with LuaLaTeX at fixed epoch
`1787875200`; require deterministic fresh builds, embedded/subset fonts,
clean log, text extraction and visual inspection.  Freeze 27 payload files
plus the self-excluded manifest.
