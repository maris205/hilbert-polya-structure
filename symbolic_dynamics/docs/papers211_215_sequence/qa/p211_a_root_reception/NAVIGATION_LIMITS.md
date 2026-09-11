# Root preparation navigation limits retained

No scientific failure occurred during root's preparation read. An initial
`rg --files` used two guessed directories (`reviews/p211_a` at workspace
root and `qa/p211_author_initial_binding01`) that do not exist; it returned
exit 2. Correct explicit batch-relative locations were used afterward.

The first JSON metadata reader assumed each saved browser return was a
dictionary. Its actual exit-1 return (chunk 2a17e4) was:

    docs/papers211_215_sequence/reviews/p211_a/sources/web01.json str 24315
    AttributeError: 'str' object has no attribute 'items'

The saved browser objects are JSON strings containing complete actual
browser returns. The next reader decoded that shape explicitly; the root
preparation inspector checks the true string format without changing any
review evidence. A combined source display also exceeded the outer display
budget (chunk 1ab74c). Missing middle text is not credited as a new complete
root read; the already accepted, previously root-read primary source gate
remains attributed within its actual scope. A's own separate complete
source-read extents and failures remain in its immutable preparation.

The execution-record inspector and initial binder reuse accepted author
infrastructure mechanics with explicit role/schema adaptation. They do not
import the submitted scientific implementation or claim blind independence.
