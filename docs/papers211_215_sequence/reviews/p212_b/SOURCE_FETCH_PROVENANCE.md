# B primary-source access provenance

This is a documentary read record, not hermetic runtime evidence. The actual
tool records remain the underlying native evidence. The PDF below is an
ordinary author-hosted primary-source download, never a manuscript upload.

2026-09-11 UTC: browser opens of the five exact URLs in SOURCE_AND_PROOF.md
resolved all five primary documents. Manna, Berdine, Holroyd and Pham bounded
line opens returned the passages listed there. Loginov resolved metadata
(26 pages, 1348 extracted lines) but all three subsequent bounded body opens
at approximately lines 732/1056/750 returned Internal Error. Four screenshot
requests for zero-based pages 13/14/18/19 also returned Internal Error. None
is claimed as a successful passage or page view. Root then explicitly allowed
ordinary curl and pdftotext of that exact primary source inside this B area.

Actual download command:

```
curl --fail --location --max-time 45 --output docs/papers211_215_sequence/reviews/p212_b/loginov_primary.pdf https://research.cs.wisc.edu/wpis/papers/festschrift4444.pdf
```

Native chunk 373f9e, exit 0, no session, 2.143004402 seconds; the saved actual
download SHA256 is b10a185e3f3b1d85eaaa6903c26d12be4709cbcba1cefdd4609d1ea401e0a7e0.
The tool returned curl's ordinary progress stream; it is not a scientific
output or a claim of a verified TLS/server/runtime dependency closure.

Actual ordinary extraction commands, each exit 0 with empty output/no session:

```
pdftotext -f 14 -l 15 -layout docs/papers211_215_sequence/reviews/p212_b/loginov_primary.pdf docs/papers211_215_sequence/reviews/p212_b/loginov_pages14_15.txt
pdftotext -f 19 -l 20 -layout docs/papers211_215_sequence/reviews/p212_b/loginov_primary.pdf docs/papers211_215_sequence/reviews/p212_b/loginov_pages19_20.txt
pdftotext -f 1 -l 1 -layout docs/papers211_215_sequence/reviews/p212_b/loginov_primary.pdf docs/papers211_215_sequence/reviews/p212_b/loginov_page1.txt
```

The actual chunks are d394b0, 8cb3d5 and de5ef7 respectively. All three
extracted text files were read in their entirety; title/authors, Figure 8,
Section 5/formulas and termination-monitor text were actually visible. No
claim is made to reading every other page of the downloaded full PDF or to
viewing its rendered pages. Browser screenshots failed and were not used.

The chapter-volume publisher page was opened separately. No generic title
search, scraped summary, external manuscript upload or contact was needed.
All files are pinned in the source package; no primary PDF was executed.
The proposed scientific verify.py was neither imported, compiled, AST-parsed
nor invoked during these document-read operations.
