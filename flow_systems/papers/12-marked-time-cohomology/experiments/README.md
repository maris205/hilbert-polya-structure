# Reproduction entry point

`reproduce.sh` runs the full unit suite (at least 96 tests), strictly verifies
the checked-in results without rewriting them, generates two more copies in
independent temporary directories, and compares all eleven CSVs plus the
manifest across all three copies byte-for-byte. It then rejects any
`__pycache__`, `.pyc`, or `.pyo` artifact under the authorized control paths.

The script fixes `LC_ALL=C`, `PYTHONHASHSEED=0`, and
`PYTHONDONTWRITEBYTECODE=1`. No network, external package, external dataset,
random sample, or timestamp is used. The reserved seed `120012` is serialized
but unused. A dedicated environment guard rejects recursive entry into the
top-level reproduction script; run only one top-level reproduction process at
a time.
