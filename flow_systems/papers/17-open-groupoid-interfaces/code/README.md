# Paper 17 deterministic controls

This directory is the complete checked-in implementation surface for the
Paper-17 finite diagnostic package.  It contains exactly this README,
`generate_controls.py`, and `test_controls.py`.

The closed generator interface is:

```text
python3 -B code/generate_controls.py --generate --output-dir EXISTING_EMPTY_DIRECTORY
python3 -B code/generate_controls.py --verify-only --output-dir EXISTING_PACKAGE_DIRECTORY
```

Generation writes exactly nine ordered CSV files and `manifest.json` into the
declared empty directory.  Verify-only is read-only: it validates raw CSV
bytes and independent semantics before the summary, then validates the
acyclic manifest and all authority, implementation, and artifact bindings.
It never repairs or normalizes a package.

The closed independent test interface is:

```text
python3 -B code/test_controls.py --checked-in results --fresh-a A --fresh-b B
```

The file contains exactly 180 explicit source-level `unittest` methods: 90
conformance/reproduction/oracle methods, 48 isolated semantic mutations, and
42 isolated package mutations.  The verifier does not import the generator.
All subprocesses use the standard library only and inherit bytecode-disabled,
network-free deterministic execution.

These controls are finite diagnostics and serialization receipts.  They do
not prove connectedness of the real line, a topos or quantale equivalence,
local compactness, localic reconstruction, non-etaleness, numerical scale,
or any C-star, Haar, trace, determinant, priority, or Route-B claim.
