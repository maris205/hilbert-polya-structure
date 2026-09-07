# Pre-update current controls after physical P209 Round1

These exact current control bytes were physically copied and raw-compared
before the next root/batch index or private-Git receipt update. The complete
actual before/after hashes and three cmp exits are in CAPTURE.actual.json.

The current Git receipt hash 2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24
is the at-freezer current observation pin. This physical copy preserves that
role. It is distinct from the original historical af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da
receipt, which remains in central_lifecycle_p209_a and physical Round1.
Future readers use each original path plus exact expected hash to select
the corresponding snapshot; no historical pins are refreshed or omitted.

The root/batch copies similarly preserve their old navigation/status bytes.
They are historical status, not a current acceptance record or proof.
No science, review, build or visual check was repeated by this capture.
