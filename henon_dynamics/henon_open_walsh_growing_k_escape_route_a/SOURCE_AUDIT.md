# C153 source audit

## Source lock

- Candidate: `HCS-C153`.
- Frozen baseline commit: `2d4e6211a254ef49d87718569d23466f4c6dcf4c`.
- Object: the explicit finite-dimensional DFT, projector, and tensor shift
  stated in `RESEARCH_QUESTION.md`.
- Clock: one application of `B_k`.
- Dimension normalization: `3^(-k)` only where explicitly stated.
- Arithmetic: exact integers and `Q(sqrt(3),i)` receipts.
- Evidence cutoffs: `k<=24, 0<=n<=2k` for the rank ledger; 20 fixed periods;
  eight rational alpha values.  These ledgers are implementation sentinels,
  not the proof cutoff for the all-parameter theorems.

The only inherited local source is the frozen C148 gate definition.  C153
rederives the power normal form, rank law, gcd trace formula, cluster theorem,
and controls.  It does not treat a sibling package's prose or finite ledger as
proof.

## Evidence provenance

`code/c153_walsh_escape_producer.py` deterministically generates the exact
JSON.  The standard-library checker imports no producer module.  SymPy builds
literal low-dimensional matrices separately.  Byte replay regenerates the
evidence in a temporary directory.  The mutation suite repairs payload hashes
before semantic rejection, plus one stale-hash control.

There are no external references, literature-derived statistics, downloaded
datasets, fitted parameters, figures, or target inputs.  Thus the registered
bibliographic and citation populations are both empty; every reported number
comes from the manifested exact evidence and is independently reconstructed.

## Firewall

No target zero or divisor, prime table, arithmetic/local datum, Euler factor,
root number, automorphy statement, Hilbert--Polya operator, or Route-B
authorization is used.  Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.
