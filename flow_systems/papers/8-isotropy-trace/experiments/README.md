# Reproduction

Run the complete deterministic package from the Paper 8 directory:

```bash
./experiments/reproduce.sh
```

The script runs all unit tests, regenerates the checked-in results, verifies
artifact, active-tuple, and implementation hashes, then generates two copies
in independent temporary directories and compares all ten generated files
byte for byte. It makes no network request and removes only its own `mktemp`
directory on exit.

This is a regression package, not a proof runner. In particular, finite
character grids do not prove Haar integration; Gaussian truncations do not
prove compact-support Poisson summation; shrinking peaks do not establish the
fixed regular von Neumann map; and scalar positive-time local finiteness does
not create an all-prime `C*` operator or trace.
