# C271 test report

The release gate runs six independent commands: producer, producer-independent
checker, SymPy reconstruction, fresh-path byte replay, repaired-hash hostile
mutations, and manifest closure.

Required pass conditions:

- all 240 threshold/equilibrium rows and 720 critical samples reconstruct;
- the checker imports no producer module;
- all symbolic center-law and regular-network identities pass;
- replay is byte-identical;
- every semantic or stale-hash mutation is rejected;
- three deterministic PDF rounds differ and final equals round 2;
- all fonts are embedded/subset and build logs are warning-free.

The exact counts and hashes are written by the final manifest command.
