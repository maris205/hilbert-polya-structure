# P120 — Odd-fringe mirror dynamics on plane rooted trees

Status: **ANONYMOUS AUTHOR DRAFT / INTERNAL FREEZE / EXTERNAL HOLD**.

For a plane rooted tree, the map reads every old fringe-subtree order and
simultaneously reverses exactly the child lists with odd order.  The paper
proves the following map-specific exact conjunction:

1. every fringe order and the underlying rooted tree are preserved, and the
   map is an involution;
2. even roots have pointwise-fixed children, while odd roots have an exact
   `M`-twisted-palindrome child list;
3. the fixed-tree series satisfy the coupled `E/O` equations;
4. `F=E+O` is the zero-constant branch of the displayed explicit degree-six
   polynomial;
5. fixed counts determine all one-/two-cycles, iterate-fixed counts, and the
   fixed-order zeta function.

The empty lane is a separately adjoined singleton identity.  The manuscript
does **not** claim an asymptotic, irreducibility or minimality of the
polynomial, a general Catalan involution theorem, priority, or owner
clearance.

Plane-tree mirror symmetry, Catalan enumeration, existing plane-tree
involutions, symbolic algebraic enumeration, resultants, involution cycle
bookkeeping, and Artin--Mazur zeta functions all receive zero contribution
credit.  P114 is separated objectwise: it deletes leaves and has
height-governed transients and Cayley basins; P120 preserves every vertex and
edge and has only one- and two-cycles.

## Reproduce the exact controls

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The canonical run makes **1,155,278** exact assertions over **82,501** plane
rooted trees, namely the empty state and every nonempty tree through order
twelve.  It checks the induced pointwise vertex transport, the coupled and
degree-six series identities through degree thirty, and the exact resultant
identity by sparse integer arithmetic.  Canonical stdout is stored in
`code/verification_output.txt`; `code/coefficient_table.csv` records the
carrier, fixed, and two-cycle counts through order thirty.

## Build the draft

See `BUILD.md` for the exact four-stage LaTeX commands and settled mechanical
checks.  The current `main.pdf` and its byte-identical round-two snapshot are
retained alongside the distinct pre-repair `main_round0_original.pdf`.  The
current bibliography renders the arXiv identifiers of both closest preprint
owners.  Public release, submission, and specialist contact remain **HOLD**.
