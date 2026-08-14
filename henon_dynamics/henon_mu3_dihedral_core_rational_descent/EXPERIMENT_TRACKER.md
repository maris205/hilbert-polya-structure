# HCS-C53 experiment tracker

Status: **RELEASE FROZEN; implementation provenance backfilled**

| Gate | Required output | Status |
|---|---|---|
| B0 provenance | source commit, certificate hash, frozen equation order | release-candidate checker PASS |
| B1 semilinear identities | exact controls plus determinant/substitution checks | release-candidate checker PASS; symbolic proof independently reviewed |
| B2 order-24 transport | 24 elements, 576 product checks, graph permutation | release-candidate checker PASS |
| B3 local identities | split exponent and inert-polynomial checks | release-candidate checker PASS |
| proof firewall | no all-\(n\) motive or global half-root promotion | documented; hostile review corrections applied |
| source audit | primary locators and novelty boundary | first pass complete |

## Evidence policy

Status is advanced to “certified” only after the independent checker exits
successfully on a freshly produced canonical certificate and hashes are
recorded. Documentation claims remain bounded by `THEOREM_PACKAGE.md` even
if a control calculation suggests a stronger pattern.

The final release-candidate replay passes 20/20 semantic gates,
63/63 targeted mutations, and 42/42 full-project manifest entries. Its locked
hashes are:

- certificate:
  f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79;
- payload:
  8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41;
- independent check:
  0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67;
- pre-integration code/results manifest:
  b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480.

These hashes are the release-candidate evidence tuple. The complete-project
manifest and implementation SHA
`0a7f0fdb8290eab4aa92ed5ade432401c40c22cf` are now frozen without reopening
the theorem documents or manuscript.
