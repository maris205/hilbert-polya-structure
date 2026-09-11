# P214 A pre-execution source correction

During root's full SOURCE read and before any execution grant, root identified
that Gaussian elimination used `row + factor*pivot`. This is equivalent to
subtraction only in characteristic two and is wrong for the fixed `q=3`
carrier. The exact correction adds

`sub(a,b,q) = (a-b) mod q` for `q=2,3`, with XOR retained for `q=4`,

and replaces the row-update `add` call by `sub`. No parameters, state map,
assertions, output format, manuscript or frozen input changed. The defective
source was never scientifically executed. Its prematurely compiled bytecode
is preserved only as historical evidence and is not the current executable
role. Current source still awaits root reception and a separate grant.

OWNER_AMBER / HOLD_EXTERNAL.
