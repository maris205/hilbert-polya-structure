# C72 source audit

C72 uses no external arithmetic or local source.  It binds only the frozen
integer presentation and the predecessor theorem:

```text
C64 evidence  7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212
C64 manifest  eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6
C71 evidence  a7498081bed5a6f8177825e4d556084bd2421da613ed22835c31e537c49579bc
C71 manifest  d5ec7bf6bc36cc87dcc2f23c838b0ae7ac997b3c442c0640f486b813fb431715
```

The matrix path proves every coordinate relation integrally modulo `M Z^16`.
The abstract path enumerates `Sub(Z/9 + Z/3 + Z/2)` without importing the
C71 triple list.  GAP supplies a third type-count check.

All sources retain `NO_BAD_EULER_OR_ROOT_NUMBER`.
