# Paper20 page-fix build harness incident

Date: 2026-08-22 UTC

The first invocation after `BUILD_AUTHORIZATION_R1_PAGEFIX.md` created two
fresh roots:

- `/tmp/p20-paper20-r1-pagefix-A-JBuZF3`
- `/tmp/p20-paper20-r1-pagefix-B-w344h4`

The wrapper copied the three permitted source files into each root but omitted
the required `cwd` change before each child.  Consequently all four commands
in each root returned 1 with the deterministic diagnostic “I can't find file
`main.tex`”; BibTeX likewise could not open `main.aux`.  No PDF, auxiliary
output, or source edit was produced.  The roots and their command logs are
non-authoritative consumed harness residues and are not reused or cited as
build evidence.

The source, metadata, source-revision receipt, and both fresh source-review
artifacts were unchanged.  A fresh retry authorization is required before a
new two-root build.

`BUILD_HARNESS_FAIL_PAGEFIX_CWD`
