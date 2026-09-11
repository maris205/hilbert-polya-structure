# Final manifest and preserved inner evidence scopes

The final SHA256SUMS is directory-relative to this p212_a review directory.
It covers every regular file recursively except itself, including this
scope note, all original source/findings/history, all DATA records, the
independent canonical and the entire actual build01 tree. It excludes no
failed evidence or nested manifest. No symlink or unexpected nonregular
member is permitted. It is not a manifest of the whole workspace or a
claim that externally referenced root receipts are copied into this packet.

Some preserved inner manifests use different historical bases. Their bytes
are not rewritten for cosmetic portability:

* INPUT_PINS.sha256, SOURCE_INPUTS.sha256,
  initial_data01/SOURCE_INPUTS.sha256 and initial_data01/SHA256SUMS are
  workspace-relative; run their checks from the workspace root.
* source_revision01/history/SOURCE_INPUTS.sha256 is the immutable original
  source-stage manifest. Its proof row names the historical live path before
  my corrected review prose; the corresponding original bytes survive in
  that same history directory. It is a preserved historical seal, not a
  current all-input acceptance check against the now-corrected live report.
* build01/SOURCE_EXPECTED.sha256 and FINAL_PRODUCTS.sha256 use the actual
  build01/source_only cwd. Each pass_artifacts/*/PRESENT.sha256 is local
  to that snapshot directory, with its adjacent absence list retaining the
  complementary product roles. The before-pass1 snapshot can be wholly
  absent without a PRESENT.sha256 file, as the accepted recipe specifies.
* build01/RUNTIME_EXPECTED.sha256, REQUEST_AND_BINDING.sha256 and
  PAGES.sha256 retain their absolute execution-path spellings. Runtime
  records are selected ordinary-trust evidence, not host closure claims.

Wrong-cwd inner-manifest checks remain failed history; successful checks
using the correct documented base do not erase them. The final directory-
relative manifest is a new complete envelope, not a rewrite of any inner
source-stage receipt, run binding, snapshot or historical checksum file.
