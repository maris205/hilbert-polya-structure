# Outer seal accounting

This new independent cold1 documentary audit packet contains 309 payload files plus one directory-relative nonself SHA256SUMS. All 307 preceding payloads have actual final native hashes/byte counts in SEAL_INPUTS_NATIVE.json; all 304 earlier listed payload hashes remain unchanged. No symlink is present in the final native inventory.

Only SEAL_INPUTS_NATIVE.json and this note are generated after that native listing. Their exact UTF-8 bytes are hashed in memory using the fully read, retained io_lane/SHA256_TEXT.js helper, checked against empty/abc known answers and the helper's own complete actual native file hash. The final manifest is then constructed from that exact complete membership. No self hash is asserted inside this note, and no silent post-seal file is added.

The root receiver must independently hash/verify the final outer manifest and current full membership. There is no pretend post-seal native verification envelope here. The final run04 seal and child lane seal already have separate actual parent native verification, with full results retained.

Read REPORT.md together with ORIGINAL_SOURCE_REPRESENTATION.md: the exact old source is in io_lane/sources/; the top-level display copy has one disclosed trailing blank line and remains pinned unchanged. run01–03 are preserved own-checker failures. run04 completes the bounded documentary checks, but P211-COLD1-IO-D1 remains Minor / OPEN_PENDING_ROOT_DIAGNOSTIC_DISPOSITION. No build, manuscript, terminal or paper acceptance is issued. No build2 or host-key replay was performed. OWNER_AMBER / HOLD_EXTERNAL.
