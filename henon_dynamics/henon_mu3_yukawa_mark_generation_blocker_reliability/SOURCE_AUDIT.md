# C73 source audit

Exact source bindings:

```text
C71 evidence  a7498081bed5a6f8177825e4d556084bd2421da613ed22835c31e537c49579bc
C71 manifest  d5ec7bf6bc36cc87dcc2f23c838b0ae7ac997b3c442c0640f486b813fb431715
C72 evidence  8fd56a3441047122765a42c8490a1cb4e84161a68734202cfe0f9852c5d3cb51
C72 manifest  5e1fbc4029dff7cdd90181d62cb9247d023a6881d549185c2a8e945e09699d6b
```

C73 uses only C72's exact named coordinate model and support atlas.  The
checker reconstructs projective rank and all deletion sets directly from the
coordinates, rather than trusting C72's generating coefficients.

No external arithmetic/local claim or source is introduced.  Scope remains
`NO_BAD_EULER_OR_ROOT_NUMBER`.
