# Paper 13 control reproduction

`reproduce.sh` is the sole top-level entry point.  It requires an exclusive
nonrecursive run, verifies the checked-in package without writing it, creates
two fresh empty temporary roots, generates and verifies both packages,
compares all thirteen artifacts across three copies, runs exactly 176 tests,
and removes both roots through its exit trap.  The tests exercise every
negative fixture family, independent product/star/gauge/norm formulas,
summary recomputation, manifest-DAG mutations, and byte/metadata write guards.

Invoke only under the external serialization required by the frozen
implementation gate, after the write-free static/mutation precheck has passed.
The script performs no automatic retry.
