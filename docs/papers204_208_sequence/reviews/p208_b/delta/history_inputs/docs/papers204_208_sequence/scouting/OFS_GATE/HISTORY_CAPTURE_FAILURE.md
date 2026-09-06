# Preserved supplemental pin-capture failure

The first actual `python3 -I -B .../OFS_GATE/freeze_history.py` invocation
exited 1 at `assert all((ROOT/p).is_file() for p in names)` before writing
any pin manifest. The archived exact source is `freeze_history_failed_01.py`.
The attempted UGR source filename was assumed instead of resolved. The
subsequent capture resolves its actual filename. P204 and P206 source/proof
bodies were read after this failed capture, hence are not claimed pre-read
frozen by the later successful supplemental manifest.
