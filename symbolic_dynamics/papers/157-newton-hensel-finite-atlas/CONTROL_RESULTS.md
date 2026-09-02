# Exact control results — P157 Round 0

**Status:** `PASS / HOLD_EXTERNAL`.

## Frozen command

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p157.py
~~~

The paper-local script is deterministic and uses Python integers only.  Its
output is frozen in `verification_output.txt`.

~~~text
NHI_FOCUSED_EXACT_V1
...
TEMPORAL valuation_selected_error_doubles
INVERSE normalized_unit_strata_and_every_target_fibres
ASSERTIONS=2563880
STATUS=PASS
~~~

Transcript SHA-256:
`f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1`.

## Audited boxes

- Normalized-unit maps: every odd input and target for `v=1..6` and
  `N=1..11`; the script separately checks the one-preimage `N=1`,
  two-preimage `N=2`, and four-preimage `N>=3` branches.
- Full maps: every state and every target modulo `2^n` for `n=1..17`.
- Forward lane: fixed points, parity, reflection, one-step valuation
  doubling, literal orbit depth, endpoint, temporal CDF, and sharp height.
- Inverse lane: endpoint fibres, every-target predicted fibre including
  zero fibres, image size, and total fibre mass.

The control makes no network request, uses no random seed, floating point, or
third-party package, and creates no bytecode when run with the frozen command.
Finite enumeration does not prove the all-parameter theorem or establish
source ownership, novelty, priority, or external-release readiness.
