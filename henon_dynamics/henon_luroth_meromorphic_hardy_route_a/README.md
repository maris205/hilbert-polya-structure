# HCS-C392: Lüroth meromorphic Hardy dynamics

The countable Lüroth transfer family has a complete Hardy spectrum and a whole-plane meromorphic continuation whose nonpositive-integer operator poles have nonzero square-zero residues invisible to its determinant.

Read the [complete proof](proof/ANALYTIC_PROOF.md), [paper plan](PAPER_PLAN.md),
[source audit](SOURCE_AUDIT.md) and [final manuscript](paper/main.pdf).
The latter is delivered only after the release gate closes; its final hashes
are in `C392_RELEASE_MANIFEST.json`.

The isolated real point 0 is excluded from the derivative-weighted branch object. At s=0,-1,... the continued operator is singular although its determinant extends holomorphically. D(1,s) has unavoidable poles at 1/2-m; no zero-free entire multiplier removes them.

Strict tuple: `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`;
overall `ROUTE_A_REJECTED`. Scope `NO_BAD_EULER_OR_ROOT_NUMBER`.
Source theorems and classical dependencies are not target success or novelty certificates.

Build and verify: [reproducibility](REPRODUCIBILITY.md). Current evidence
contains exact finite regression data; infinite statements are proved separately.
