# Root documentary alias selector correction

The first new receiver execution failed at /lib64/ld-linux-x86-64.so.2.
It incorrectly compared this symlink's entire lexical rich record against
the resolved loader's rich record, including the different symlink field.
Both exact lexical and resolved paths were already in the preaccepted
runtime key; this is not an unkeyed dependency or a producer failure.

FAILED_INSPECT01.py and FAILED_INSPECT01_NATIVE.json preserve the exact
failed checker and actual exit. No INPUTS_CURRENT result was emitted. The
failed source was physically copied and compared before correction.
The sole repair requires the actual lexical path to be prekeyed and checks
its full lexical record against that role, then checks the entire resolved
record separately. No byte, resolved path, symlink expectation or input
selection is loosened. Existing scientific output, binding, runtime lock,
discovery, native records and all seals are unchanged. Only this root-owned
documentary checker is rerun; no scientific producer retry occurs.
