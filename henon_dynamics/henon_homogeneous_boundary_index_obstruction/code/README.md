# C37 code

`c37_homogeneous_index_producer.py` emits the deterministic theorem
certificate.  `c37_homogeneous_index_checker.py` independently replays ten
fail-closed gates, including the equivariant coboundary identities, prime
telescoping, zero boundary-pair index, and the exact shrinking-interval VMO
lower bound.  Its final gate freezes the complete nested semantic contract,
so rehashed unknown fields or altered explanatory verdicts cannot bypass
the replay.  The mutation suite supplies 25 type-confusion controls.

Run the frozen package with

~~~bash
./code/run_c37.sh
~~~

Only release preparation may refresh the manifest:

~~~bash
./code/run_c37.sh --refresh-manifest
~~~
