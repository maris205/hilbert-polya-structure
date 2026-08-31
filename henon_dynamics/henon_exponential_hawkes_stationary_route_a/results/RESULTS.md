# Results

The canonical producer closes:

- 320 stable exact parameter cases;
- 3,520 stationary moment cells through order ten;
- 3,200 exact window-variance series coefficients;
- 160 Borel cluster rows;
- six boundary rows.

The independent checker passes 27,893 assertions.  SymPy passes 1,304 exact
generic and stored-row checks.  Fresh/fresh/release byte replay passes.
Hostile mutation testing rejects 28/28 changes.

The evidence file and PDF hashes are recorded only by the final release
manifest, after all text and binary artifacts are stable.
