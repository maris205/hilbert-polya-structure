# Round 10 Papers 29--33 -- Stage 2 Internal Review Configuration

This configuration governs manuscript-quality and boundary checking inside the
authorized Stage-2 WRITE run. It is not ARS Stage 3 peer review, does not make
an editorial decision, and cannot open Stage 2.5 or either formal route.

| Papers | Composition seat | Independent recheck seat |
|---|---|---|
| P29, P30 | `R10-S2-WA` | `R10-S2-RB` |
| P31, P32 | `R10-S2-WB` | `R10-S2-RC` |
| P33 | `R10-S2-WC` | `R10-S2-RA` |

The integrating seat `R10-S2-I0` may apply typographic, build, citation-closure,
or explicitly reported boundary repairs and must rerun all deterministic
checks. A recheck seat must not review a manuscript it composed. Each recheck
is bound to the exact manuscript and bibliography SHA-256 values and covers:

1. all eight registered Stage-2 ClaimIntents and their negative constraints;
2. frozen dynamical object, clock, owner convention, normalization, and cutoff;
3. literature closure and every `anchor:none` limitation;
4. absence of unexecuted scientific results or route promotion;
5. article structure, English and Traditional-Chinese abstracts, declarations,
   and AI-assistance disclosure;
6. PDF/source consistency and build quality.

Any unresolved Blocker or Major finding stops the Stage-2 completion claim.
Minor findings may be repaired only inside the Stage-2 writing surface, with a
post-patch recheck. The required endpoint remains
`AWAITING_EXPLICIT_USER_CONFIRMATION_FOR_STAGE_2_5`.
