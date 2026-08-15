# Exact implementation boundary

This package implements the source-locked Paper 8 proof-contract and the
fixed exact audit at periods 1 through 12.  The `safe-preflight` command runs
only source/upstream binding checks, executable-isolation checks, symbolic
proof contracts, and declared controls.  It never imports or invokes the
registered candidate entry point.

The `registered` command has no scientific command-line parameters.  It is
one-shot, requires an independent `DEPLOYMENT_PASS` bound to the current
source-lock and reviewed-code hashes, and durably writes a `STARTED` claim
before exact candidate construction.  It uses no network, external prime
table, generated target array, floating orbit calculation, or period above
12.  The all-period tail remains an imported-theorem proof conclusion.
