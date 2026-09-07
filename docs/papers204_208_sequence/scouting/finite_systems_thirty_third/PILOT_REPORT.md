# Original complete OTC pilot — evidence and limits

One original pilot family, executed twice; one literal; no larger follow-up.
The fixed declaration in [INTAKE](INTAKE.md) predates compilation and both
producer runs. All mathematical parameters are compiled into [pilot.c](pilot.c).
No old scientific code, data, parameter file or canonical was imported.

## Actual result

| n | all states | image | recurrent | fixed | maximum tail | maximum period | maximum fibre |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |
| 2 | 3 | 1 | 1 | 1 | 1 | 1 | 3 |
| 3 | 27 | 9 | 3 | 1 | 2 | 2 | 13 |
| 4 | 729 | 253 | 133 | 1 | 3 | 2 | 93 |

Each execution emitted **760 complete state rows and 2,852 structural checks**.
These checks cover target range, full orbit termination within the carrier,
and full fibre/tail/period histogram totals. They are not 2,852 independent
proofs of a conjectured theorem. Every cycle is emitted explicitly. Each
STATE row gives n, input id, target id, tail, period, minimum cycle id and
the number of incoming arrows to that input id (its target-fibre size).

IDs are ternary digits over pairs $(0,1),(0,2),\ldots,(n-2,n-1)$ in that
lexicographic order, least significant digit first. Digits 0,1,2 mean no
arc, low-to-high, high-to-low. The carrier is fully labelled and unquotiented.

The full [CANONICAL.raw](CANONICAL.raw) has 845 lines, including all state
rows, cycles and summaries. It is an unchanged physical copy of run A,
not hand-authored expected data. Runs A and B each exited zero. The actual
pair comparison (command 12), A-to-canonical (15), and B-to-canonical (16)
all invoked raw `cmp` and exited zero. Empty comparator stdout/stderr is
success, not an invented match count.

## Scientific runtime and complete reuse key

The producer is a freestanding static ELF64 x86-64 executable, not a Python
program. `readelf -l -d -s` (09) shows no interpreter, no dynamic section
and no external undefined symbol besides the ELF null symbol. Its source
has no headers, imports, file reads, argv/environment reads, clocks, RNG,
threads or locale-sensitive formatting. The only system calls are stdout
write and exit. Full disassembly is preserved by command 17.

| dependency | exact role / SHA-256 |
|---|---|
| `pilot.c` | original complete scientific source; `2341a626df91f9205d077ea1d0565d59e4fbaf6cceaf760975ff281a7be7de5e` |
| `pilot` | complete executed machine code; `834a4ecc6f989340ad3f05b086a37efa6d7f9d4040fcef7f8e542a1a11f96a75` |
| `INTAKE.md` | predeclared rules and exact n=1..4 bounds; `72bbd264f03c96f87b9db24731323938673095439e8df077a0e768fcb296b008` |
| `CANONICAL.raw` | actual full output; `80e1d40a04b48f0bf4944f5c88b9013e06b871ed8bb7a4fb9d71c031dc2dd356` |

No scientific data file or runtime library is omitted: there are none.
The runtime substrate was Linux 5.15.0-78-generic, x86_64 (native command
18). Output file descriptor 1 must be writable and the small fixed stack
allocation must be available. The proof and execution claims are restricted
to this actual integer-only x86-64 artifact, not architecture-independent C
portability. This program never consumes the inherited environment, so
recording credential-bearing environment variables is neither necessary
nor appropriate.

Compilation used GCC 11.4.0, with the exact expanded argv in command 08:
freestanding/no-library static linking, no builtins or stack protector,
no PIE, O2, Wall/Wextra/Werror and no build ID. The compiler binary was
pinned before/after. This records the actual build but is NOT a hermetic
compiler/toolchain-input or reproducible-build certification; the exact
executed binary is preserved and is the scientific runtime closure.
The documentary Python recorders do not compute any scientific state.
Their source and native receipts are included separately in the package.

## Evidence limit

The apparent empty-only fixed set and low periods at n<=4 are not global
claims. [PROOF_PACKAGE](PROOF_PACKAGE.md) gives analytic odd-cycle periods
and a persistent-cancellation fixed graph on 15 vertices; neither was
silently added to the pilot. It also proves the DAG zero-fibre formula and
the exact 93 zero parents at n=4. No all-target inverse or whole-carrier
recurrence theorem survived the bounded desk. **NO_PROMOTION**.
