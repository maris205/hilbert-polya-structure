# HCS-C264 executable certificate

- `c264_power_map_producer.py` constructs the formula ledger and direct orbit receipts for 646 maps.
- `c264_power_map_checker.py` independently enumerates every group element and checks periods, tails, images, and all stored iterate counts; it imports no producer code.
- `c264_power_map_sympy_crosscheck.py` materializes exact composition matrices for a broad small-group subcorpus.
- `c264_power_map_replay.py` regenerates the evidence in a fresh temporary directory and requires byte identity.
- `c264_power_map_mutation.py` repairs the outer payload hash after semantic corruptions and requires every corruption to be rejected.
- `c264_release_manifest.py` is the final 27-payload release gate.

All scripts use only exact integer or symbolic arithmetic. The frozen epoch is `1788048000`.
