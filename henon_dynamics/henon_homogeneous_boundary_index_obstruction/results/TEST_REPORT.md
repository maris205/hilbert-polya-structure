# Test report

The pre-freeze release replay passed:

- deterministic producer: byte-identical on repeated isolated runs;
- independent checker: 10/10 gates;
- mutation/type-confusion suite: 25/25 tests;
- payload SHA-256:
  a038104735c6f0225b957fbda6e4689d3498df59af996584725f65b884ea9dfd;
- certificate file SHA-256:
  8c1ffec67446f6045694651edcd0de636c5fb6564ec530e799dd33dce7a87141;
- independent report SHA-256:
  dc26e12480f1fd80d2039460c8aba0466cad1458f7d7ed25a029d1045b5582e0.

The final two-stage release replay additionally verifies the complete
artifact manifest after the Route-A file is pinned to the implementation
commit.
