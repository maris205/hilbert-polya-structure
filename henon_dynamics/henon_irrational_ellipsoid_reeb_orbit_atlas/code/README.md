# C242 code contract

`c242_reeb_producer.py` emits the canonical JSON receipt. It uses exact
integer-square inequalities for every `sqrt(2)` and `1/sqrt(2)` floor, and
uses 90-digit `mpmath` only for the displayed trigonometric multipliers.
`c242_reeb_checker.py` reconstructs all 48 irrational iterate rows and six
rational Morse--Bott coordinate rows without importing the producer.

The remaining scripts provide independent SymPy identities, byte replay, and
29 repaired-hash hostile mutations. All scripts are deterministic under
`PYTHONDONTWRITEBYTECODE=1 python3 -B`; no target arithmetic data are read.
