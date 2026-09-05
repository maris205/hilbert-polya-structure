# C396 executable interfaces

Six scripts: producer, independent checker, symbolic/high-precision lane,
two-directory replay, semantic/serialization/YAML mutations, and release gate.
The checker never imports the producer. Exact equality uses canonical JSON
bytes, not Python's bool-int equality. Decimal fields require finite numeric
strings and fixed shapes. Every expected field and frozen row is checked.

The release --build-pdfs switch creates the three PDFs and logs.
The --write switch reruns all lanes, checks fresh deterministic PDFs and
writes the closed manifest. Without --write it compares the freshly computed
manifest without changing the package. --evaluation is for temporary hostile
YAML fixtures and is checked before write operations. --authority-path supports
temporary evaluator-hash attacks; it cannot change the frozen expected digest.
The live authority is rehashed by both checker and release. Every symlink and
unlisted physical payload is rejected before any lane or write; no cache
directory is exempt from membership.
