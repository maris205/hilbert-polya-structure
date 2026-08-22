# Hostile audit

The mutation script independently edits the dissipation parameter, resultant,
local weight, transition, matrix, trace, determinant coefficient, and Route-A
verdict.  Each altered evidence file is passed to the independent checker and
must fail.  The exact original bytes are restored in a `finally` block, and
the final mutation count is `8/8`.
