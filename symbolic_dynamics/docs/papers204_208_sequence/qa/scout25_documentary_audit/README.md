# Twenty-fifth scout documentary audit

This package checks the sealed twenty-fifth scout's documentary integrity. It is
not a scientific producer, independent candidate gate, or source-body novelty
review. The original scout and P209 author artifacts are read-only and untouched.

`inspect.py` authenticates the original complete 115-payload manifest twice; the
initial and terminal 3,520-file discovery maps and current inputs twice; all 15
historical originals and physical copies; all 15 recorded command arguments,
environments, exits, full stdout/stderr hashes; and each recorder's source and
named-tool before/after pins against current bytes. It also checks the actual
downloaded slides PDF and extracted text, keeping the four nonzero acquisition
exits 22, 60, 28, and 60 as failures. The 178-byte `.pdf` error response is not
treated as a paper. Any historical central-control substitution is limited to
the two exact, already physical, hash-pinned copies encoded in the auditor.

The actual execution's `attempt_01/ATTEMPT.json`, `RESULT.json`, full `stdout`
and `stderr`, and `RECORDER_RECEIPT.json` determine whether these checks passed;
this explanatory file does not assert a future PASS. The full stdout contains
the detailed report, all 15 literal command records, every current read-file
pin, and explicit scope limitations. `record.py` retains its own and the
auditor's exact executed source copies and the original scout manifest, records
the actual child command, and rechecks the child's full current-read set before
making this package's complete nonself `SHA256SUMS`.

No old scout script is imported or executed. No new repository-wide search,
scientific map, download, PDF conversion, visual reading, manuscript edit,
index update, or Git operation is performed. Historical recorders provide
source and named-tool pins, not a complete historical Python/TLS/loader/config
dependency closure; this audit does not relabel that documentary evidence as
a strict terminal scientific replay key. The unacquired 2012/2013 source bodies
remain on hold.
