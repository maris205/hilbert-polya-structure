# Preserved intake error and bounded proof check

2026-09-06 UTC, after the initial three pilot processes. The initial intake,
code, canonical and receipts remain byte-unchanged.

## Historical-comparator label error

`INTAKE.md` calls $x_i(1+x_{i+1}-x_{i-1})$ the old LV map, and the pilot's
`old_LV_difference` field evaluates that expression. The actual historical
literal in `algebra_third/PROOF_AND_ADAPTER_NOTES.md`, section LV, is
$x_i(x_{i+1}-x_{i-1})$, with **no identity term**. Thus that canonical field
is a comparison with an Euler-style near-neighbor, not a verified execution
of old LV. The new QEF literal and all its functional-graph results are
unaffected. We claim no numerical comparison against actual old LV.

The correct literal inequality is deductive: at $(1,0,0)$ actual old LV
returns $(0,0,0)$ and QEF returns $(1,0,0)$ over every prime field. This
does not clear their broad quadratic-feedback neighborhood or confer value.
The wrong historical label is superseded here, not silently rewritten in
the frozen declaration or canonical.

## Fixed post-pilot proof obligation — before its execution

An elementary QEF inverse elimination emerged during proof writing. It
claims maximum fibre $5$ over every odd prime field, attained at zero;
over $\mathbf F_2$ the maximum is $3$. This is a static degree-five
elimination with singular $z=\pm1$ branches, not a temporal theorem.

`qef_inverse.py` will independently implement the forward map and a
target-resolved decoder. It will compare complete predecessor sets for
**every** source and target in the already declared fields
$p=2,3,5,7,11,13$. No new prime, state box, seed family or cutoff is added.
It checks fixed points and a corrected old-LV witness, the sharp bound,
zero-target witnesses and the degree-five identity. It does not import the
initial pilot, its canonical or repository code. The same exclusive-output
recorder protocol will save an initial producer and two fresh raw replays
in `inverse_execution_01`, separately from `execution_01`.

QEF remains `NO_PROMOTION`: a valued static inverse bound cannot supply
the missing all-prime temporal/recurrent axis. This follow-up verifies a
new deduction within the existing boxes, not a rescue enlargement.

## Diagnostic failure, not failed mathematics

A read-only one-line Python summary command after the pilot exited $1$
with `SyntaxError: Generator expression must be parenthesized`. It neither
ran a numerical test nor wrote a file. The corrected list-comprehension
summary exited $0$, reading the unchanged canonical. All three actual
pilot producers and all three raw comparisons had already exited $0$.
