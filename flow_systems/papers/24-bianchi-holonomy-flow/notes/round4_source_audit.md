# P24 Round-4 source audit — finite-volume non-arithmetic control

Audit date: **2026-08-27**.  Scope: only the theorem chain needed to bind the
`5_2` knot complement to a genuine finite-volume, one-cusped,
non-arithmetic hyperbolic 3-manifold.  This is a source-verification artifact,
not a claim of exhaustive literature coverage or novelty.

## Claim-to-source matrix

| Claim | Primary or authoritative source | Locator | Verdict |
|---|---|---|---|
| The census manifold `m015` carries a complete finite-volume hyperbolic structure. | Hoffman, Ichihara, Kashiwagi, Masai, Oishi, and Takayasu, *Verified Computations for Hyperbolic 3-Manifolds*, [arXiv:1310.3410](https://arxiv.org/abs/1310.3410), [doi:10.1080/10586458.2015.1029599](https://doi.org/10.1080/10586458.2015.1029599) | Theorem 5.1 verifies every manifold in `OrientableCuspedCensus`; the paper's algorithm states that a successful certificate proves a finite-volume hyperbolic metric. | **VERIFIED / PROVED BY SOURCE** |
| SnapPy's `m015` interval example succeeds, and a `True` return from `is_isometric_to` is rigorous. | Official [SnapPy verified-computation documentation](https://snappy.computop.org/verify.html) and [`Manifold` API documentation](https://snappy.computop.org/manifold.html) | The verified-computation page displays `Manifold("m015").verify_hyperbolicity()` with positive shape intervals.  The API states that `is_isometric_to=True` is rigorous. | **VERIFIED / AUTHORITATIVE SOFTWARE CONTRACT** |
| The built-in `5_2` object is isometric to `m015`. | Executed SnapPy 3.3.2 invariant contract, bound to the API semantics above | `Manifold("5_2").is_isometric_to(Manifold("m015")) == True`; exact receipt in `results/five_two_control_invariants_round4.json`. | **RIGOROUS POSITIVE SOFTWARE RESULT** |
| The `5_2` complement is non-arithmetic. | Reid, *Arithmeticity of Knot Complements*, [doi:10.1112/jlms/s2-43.1.171](https://doi.org/10.1112/jlms/s2-43.1.171) | Reid's classification theorem: the figure-eight complement is the only arithmetic knot complement in `S^3`.  The frozen object is the distinct named knot `5_2`; the executable contract also records its two-bridge identifier `(-2,7)`, versus `(2,5)` for `4_1`. | **VERIFIED / PROVED BY SOURCE** |
| The local dependency is the intended current release. | Official [PyPI release record for SnapPy 3.3.2](https://pypi.org/project/snappy/3.3.2/) | Release `3.3.2`, uploaded 2026-03-06; the script fails closed on any other version. | **VERIFIED / VERSION LOCK** |

## Source quality and conflicts

- The HIKMOT and Reid items are peer-reviewed mathematical theorem sources and
  receive **Grade A** for the claims assigned to them.
- The SnapPy pages are first-party software documentation and receive
  **Grade A-authoritative** for API semantics, dependency boundaries, and the
  displayed `m015` interval example.  They are not substituted for Reid's
  arithmeticity theorem.
- No retraction or source-identity warning was found in the bounded audit.
  Funding and author conflicts were not material to these theorem statements;
  no conflict-based exclusion was applied.

## Inference chain and exact boundary

The proof chain used by the project is:

```text
HIKMOT Theorem 5.1
    -> m015 is complete finite-volume hyperbolic;
rigorous SnapPy True-isometry result
    -> 5_2 complement is the same manifold;
5_2 is a one-component knot complement
    -> exactly one complete torus cusp;
Reid's classification and 5_2 != figure-eight
    -> the lattice is non-arithmetic.
```

This chain proves the **control object's** geometry and non-arithmeticity.  It
does not certify the locally emitted decimal volume, cusp shape, tetrahedron
shapes, or length spectrum.  SnapPy's official documentation says verified
interval computations require the SageMath runtime; SageMath was unavailable
in this environment.  Those decimal artifacts are therefore labelled
`HIGH_PRECISION_NUMERICAL_OBSERVATION_NOT_INTERVAL_VERIFIED` even when two
independent algorithms agree.

## Audit limitations

- This was a claim-directed, search-bounded audit, not a systematic review.
- Source pages were checked live and linked; source bytes were not vendored or
  assigned a local content hash.
- The published HIKMOT census certificate was not re-executed locally.
- The finite geodesic ledger uses pinned SnapPy 3.3.2 implementation semantics;
  it is not elevated to a theorem by the external hyperbolicity certificate.
- No novelty claim is made for selecting `5_2` as a control.
