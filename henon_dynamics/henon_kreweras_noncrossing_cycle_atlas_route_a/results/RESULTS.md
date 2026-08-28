# C209 results

The canonical producer currently reports:

* 24 values of n, 597 fixed rows, 131 divisor/period rows, 597 spectral rows,
  300 Narayana rank rows, and 24 structural rows;
* q-Catalan coefficient rows through n=12;
* direct enumeration selected through n=8 (2,055 partitions in total).

The independent checker, SymPy audit, byte replay, and mutation harness must
all report PASS before the release manifest is generated.  Exact hashes are
recorded in `C209_RELEASE_MANIFEST.json`.
