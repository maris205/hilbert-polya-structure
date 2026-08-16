# HCS-P76: weighted reflection natural-boundary circle

This project completes the global fixed-weight geometry left open by P75.
For every `q>0`, channel `m` has the `2m` singular points

    alpha_(m,k)(q)=(1+q^(2m))^(-1/(2m)) exp(pi i k/m).

Their radii increase strictly to `min(1,q^(-1))`; every point is an
exponential essential singularity, and the angular meshes become dense.
Hence `|z|=min(1,q^(-1))` is a natural boundary for the exact unrenormalized
punctured continuation.

The project contains a proof package, executable and independent
certificates, ordinary and optimized unit tests, a mutation audit, a
compiled paper, and explicit Route-A/Route-B firewalls.  The theorem does
not cover a counterterm-renormalized object and supplies no source-native
operator or arithmetic trace.

- [Proof package](PROOF_PACKAGE.md)
- [Paper](paper/paper.pdf)
- [Certificate](results/c76_certificate.json)
- [Independent check](results/c76_independent_check.json)
