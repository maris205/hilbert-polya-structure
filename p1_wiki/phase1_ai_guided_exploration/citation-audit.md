# Citation and Link Audit

## Scope

This is a local, source-bound audit for the working-paper package. It checks that the manuscript's project-record identifiers have corresponding entries in its local record table and that Markdown targets can be resolved within the repository. It does not validate a theorem, independently rederive a proof, assess external literature coverage, or establish peer-review status.

## Citation model

The manuscript uses repository-record keys rather than a conventional external bibliography. The keys identify project records that control the limited statement being made:

- P1-RM, P1-KB, P1-CL, P1-META, and P1-X for the P1 programme, evidence vocabulary, and non-transfer boundaries;
- Z0-E, Z0-C, Z0-R, and Z0-A for the free-exploration evidence policy, claim ledger, roadmap, and imported-archive boundary;
- S1-C and S1-R for Logistic;
- S2-S, S2-E, and S2-HOLD for Hénon;
- S3-D and S3-E for Symplectic;
- S4-P and S4-ST for Symbolic;
- S5-R, S5-P, and S5-END for Flow Systems.

The 21 keys above are all listed in the manuscript's Project records cited in this manuscript table and in the [evidence map](evidence-map.md). No external journal citation, DOI, author metadata, or bibliographic completeness claim is made in this working-paper draft.

## Checks performed

1. The manuscript's inline project-record links were enumerated and compared with the project-record table.
2. Every cited local record was checked as a filesystem target by the P1 Markdown-link verifier.
3. The repository's derived reader corpus was checked in read-only mode. This validates the pre-existing generated corpus against its manifest; it does not add the working paper to that corpus or validate the paper's mathematical content.
4. Whitespace errors were checked with Git's diff checker.

## Interpretation boundary

A passing target check means that a reader can reach the referenced local record. It does not mean that the record proves a stronger claim than its stated scope, that all linked mathematics has been independently reviewed for this manuscript, or that the paper has external scholarly validation. The [review notes](review-notes.md) record a separate bounded wording and source-scope review.

## Final verification record

Closing verification on 2026-09-13 UTC produced the following results:

| Check | Command | Result |
| --- | --- | --- |
| Project-record key coverage | Enumerate inline project-record keys and compare with the manuscript record table | 65 local project-record citations using 21 unique source keys; 21 corresponding local record-table entries |
| Markdown targets | python3 p1_wiki/tools/verify_wiki_links.py | PASS: 19,223 local links in 2,302 Markdown files |
| Derived P1 reader corpus | python3 p1_wiki/tools/build_paper_corpus.py --check | PASS: 1,126 logical records |
| Patch whitespace | git diff --check | PASS: no output |

The reader-corpus check is a preservation check for the pre-existing P1 corpus; it does not add this working paper to the derived corpus or validate the paper's mathematics. Any later external release must repeat this audit against a release-specific evidence snapshot.
