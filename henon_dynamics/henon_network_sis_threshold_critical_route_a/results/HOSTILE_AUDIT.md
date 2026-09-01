# C271 hostile audit

The mutation suite repairs the payload hash before attacking source lock,
Route-A tuple, scope flags, the critical coefficient, threshold sign, endemic
coordinate, and equality solution.  It separately tests a stale hash and an
unknown top-level key.  A mutation passes only when the independent checker
rejects it.  This prevents a self-consistent but semantically altered JSON
receipt from entering the release.
