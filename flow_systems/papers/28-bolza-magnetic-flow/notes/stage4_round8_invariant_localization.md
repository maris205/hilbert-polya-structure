# Stage 4 Round-8 invariant localization

Status: **PASS**

Four direct Stage-4 tests now localize properties that the official Round-8
suite previously reached only indirectly:

- two consecutive common `Delta` factors cancel to the exact identity fixed
  point;
- global-negation normalization returns the same canonical state and is
  idempotent;
- all four `g_j g_j^{-1}` and all four `g_j^{-1} g_j` multiplication orders
  close exactly;
- enumeration of all 585 words through length three yields 457 canonical
  states and nine collision buckets, including nine distinct sampled words
  that normalize to the identity.

The tests import the audited Round-8 builder. They localize regressions in the
same implementation and do not constitute the separately implemented
eight-transition closure checker proposed as a stronger assurance path. No
independence claim is made.

The direct run passed 28/28 tests. The default `reproduce_round8.sh` path then
passed its 24-test suite, built the complete certificate twice in fresh
temporary directories, and obtained the identical tree hash
`c30beebdd2e832d9375f55f1eab700868b7b967dfb5ee43fcecc0ba5f60919ac`
for both runs. Temporary products matched the checked-in artifacts. The
canonical Round-8 result directory remained byte-identical and was not
refreshed. Route-A status is unchanged and Route B was not invoked.
