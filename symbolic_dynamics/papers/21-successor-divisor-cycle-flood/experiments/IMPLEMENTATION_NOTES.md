# SD-C23 implementation notes

## Exact arithmetic and sparse state

Integer path counts use sparse dictionaries and the confinement cutoff $2r-1$. Weighted traces and determinant coefficients use Python Fraction arithmetic. Directed rotations are identified, reflections are not, and temporal powers are removed when forming primitive classes.

## Independent determinant paths

One coefficient ledger is obtained from exact traces through the Newton recurrence. The second is obtained by multiplying the explicitly enumerated primitive factors through degree 16. Agreement is tested coefficient by coefficient; the two methods do not call one another.

## Controls

The full graph is compared with the $q=\{1,2\}$ spine, the $q=1$ successor-only graph, individual $q=\{1,q_0\}$ families, finite quotient blacklists, and positive edge-weight inventories. These controls distinguish recurrence from arithmetic selectivity: the two-quotient spine already retains the all-length cycle flood.

## Reproducibility

The orchestrator sets PYTHONDONTWRITEBYTECODE=1 and PYTHONHASHSEED=0. CSV files use UTF-8 and LF line endings; JSON objects are key-sorted and contain no timestamps or elapsed-time metadata. The command

    python experiments/run_sdc23_exact_suite.py --verify-byte-determinism

regenerates every result, runs the tests and integrity gate, freezes the SHA-256 ledger, repeats the whole process, and requires identical ledger bytes.

## Claim boundary

Floating values occur only in finite nuclear-prefix diagnostics. All reported traces, primitive counts, cutoff flags, and determinant equalities are integer or rational identities. The diagnostic prefixes illustrate, but do not prove, the analytic theorem that trace class holds exactly for $\Re s>1/2$.
