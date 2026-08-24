# Code map — C114

- `c114_jet_producer.py`: exact truncated polynomial engine and canonical evidence producer;
- `c114_jet_checker.py`: independent reconstruction; imports no producer code;
- `c114_sympy_crosscheck.py`: fresh symbolic substitution and matrix cross-check;
- `c114_replay.py`: canonical JSON byte replay;
- `c114_mutation.py`: thirteen hostile in-memory corruptions, each required to fail validation;
- `c114_release_manifest.py`: final content-addressed package ledger.

The producer and checker use separate implementations of polynomial
multiplication, exponentiation, basis construction, and matrix assembly.  All
rational data are serialized as integer or `numerator/denominator` strings.
