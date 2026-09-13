# Selected source for the first natural-draft build

Date: 2026-09-06. Source is complete; no build or page measurement has run.

The root read the full 148-line independent source review,
SOURCE_TRANSCRIPTION_INDEPENDENT_REVIEW_20260906.md, SHA256
2b3ed57ba53c4128b25198be1442ef4ce1e10e0d214a9e9266799b0a4a1614a5.
It found no critical/major defect and one minor abstract scope omission.

The original paper/ and SOURCE_DRAFT_MANIFEST_20260906.sha256 remain unchanged.
The selected direct successor is paper-successor-20260906-transcription-v1/.
A recursive source diff shows exactly one changed line: the abstract's
quartic algebra-length bound now explicitly says "for D>=1". The actual
theorem already had this condition. No scientific content, theorem, proof,
example, bibliography, structure or typesetting parameter changed.
SOURCE_BUILD_MANIFEST_20260906.sha256 binds the selected twelve files,
with paths relative to that successor directory. A bounded independent
check of the one-line correction is requested before the first build.

After that check, the authorized first command from this project directory is:

```sh
bash scripts/build-local.sh paper-successor-20260906-transcription-v1 build/natural-20260906-r0
```

The helper's SHA256 remains
6402541329a6fbdfa2f03a7605724037e5abe033404c6feb02a0903271a2c8f8.
Root and a separate reader both passed bash -n and inspected its stage
logging, failure exits, isolated copy and fixed environment. The separate
reader observed that its successor glob also allows nested successor paths;
this nonblocking general parameter breadth is not exercised here. The
selected source is the explicit project-direct child above. No expanded
build infrastructure or additional source access is needed for this call.

Measure the first complete successful build against the unchanged 22--30
substantive-body-page lock. If outside that range, preserve and stop this
validation without padding. Only after the page gate passes may a second
fresh root reproduce the same source and actual full-PDF/final reviews
proceed. The old candidate verdicts remain unchanged.
