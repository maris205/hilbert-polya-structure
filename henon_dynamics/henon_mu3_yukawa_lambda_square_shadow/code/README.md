# C62 code

`c62_lambda.py` is the prefreeze exact finite-group producer.  It rebuilds
the released C61 (W(E_6)) action, enumerates the exterior/symmetric-square
orbits, checks the lambda character identities, and records stabilizer
conjugacy witnesses.  `c62_atlas.py` upgrades those rows to complete
stabilizer, core, and normalizer element sets; `c62_atlas_checker.py` checks
the resulting G2 invariants.  `c62_resolvent.py` adds factorized marker
carriers and split-prime noncollision, with `c62_resolvent_checker.py`
checking the G3 contract.  These outputs are implementation evidence only;
the independent arithmetic, paper, and release gates remain to be added.
