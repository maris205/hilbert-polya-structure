# Code

`trace_certificate_controls.py` contains deterministic standard-library
controls for:

- exact quadratic-field arithmetic for modular hyperbolic norms;
- a sampled smooth-shift illustration of local-germ ambiguity; and
- provenance-sensitive T0 certificate validation.

`test_trace_certificate_controls.py` supplies eleven unit tests.  The code
uses no network input, Riemann-zero table, fitted parameter, or random seed.
The universal mathematical claims are proved in `../notes/proof_audit.md`;
finite enumeration is only a regression control.

