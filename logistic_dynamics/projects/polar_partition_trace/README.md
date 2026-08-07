# Exact-​$U_c$ polar partition trace ledger

Stage ID: `P4-LOGISTIC-UC-POLAR-PARTITION-TRACE`

This is a non-candidate Logistic branch audit. It freezes the geometric
half-open coding and separates it from the analytic trace question.

## Result

The exact parameter is the unique real root

\[
U_c^3-2U_c^2+2U_c-2=0,
\]

with no use of the rounded legacy value. The geometric partition is

```text
I_L=[-pi/2,0), I_R=[0,pi/2]
```

and the exact boundary graph is

```text
P=-pi/2 -> P,   Q=pi/2 -> P,   Z=0 -> Q.
```

Therefore the partition point is preperiodic, not a boundary periodic orbit.
The target-free certificate also checks cyclic rotation, endpoint-copy swap,
signed orientation, repetition bookkeeping, and the common-output matching
range through symbolic word length 8.

## Trace boundary

The half-open rule gives one canonical geometric itinerary per orbit. It does
not prove that the analytic trace on the doubled matching space has the same
multiplicity. Matching at zero alone does not justify dividing source-branch
contributions by two; the local trace correction at `P=-pi/2` remains open.

No nuclearity, Fredholm determinant, zero comparison, Route B, Hilbert--Pólya,
or RH claim is made.

## Reproduction

```bash
python3 src/partition_trace_audit.py --quiet \
  --output results/partition_trace_certificate.json
python3 -m unittest -v tests/test_partition_trace.py
```

The canonical source lock and Route-A evaluation are kept alongside the
artifact. A manuscript directory is reserved for a later theorem-level local
trace result; this stage currently remains `REVISE` / `NOT_TESTABLE` for A2.
