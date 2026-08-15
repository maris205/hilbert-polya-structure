# HCS-C57 exact machine package

This directory contains the strict PREFREEZE producer/checker package for the
minimal Brauer-jump computation on the frozen HCS-C56 cubic surface.

The producer and checker deliberately have different mathematical call graphs.
The producer runs the project-local exact FLINT, PARI and finite-field helpers.
The checker does not import or invoke those theorem helpers: it independently
reconstructs the characteristic-zero incidence identity, all resolver CRT
congruences and irreducibility certificates, the degree-12 carrier identity,
the group/Picard calculation, and the canonical quartic minor.

The supported backends are fixed by byte hash and version:

- `/usr/bin/python3` for PARI/cypari2;
- `/root/miniconda3/bin/python3` for python-flint and SymPy;
- `/usr/bin/Singular` as a locked release dependency (the default G1 replay is
  the faster exact FLINT plus good-specialization route).

Run `./run_all.sh` with no arguments for the nonmutating live replay.  An
initial or deliberate PREFREEZE refresh requires
`./run_all.sh --refresh-prefreeze --evidence-dir DIR`, where `DIR` contains
exactly the five source-locked deterministic gzip evidence files.  Refresh is
a fixed nine-target rollback-atomic transaction; the scoped manifest is
promoted last.  Neither mode authorizes paper or release promotion.

The bootstrap trust boundary is the parent process: the ELF dynamic loader
processes `LD_PRELOAD` and `LD_LIBRARY_PATH` before any Bash source line can
run.  A trusted parent shell must therefore execute
`unset LD_PRELOAD LD_LIBRARY_PATH BASH_ENV ENV PYTHONOPTIMIZE PYTHONPATH PYTHONHOME PYTHONSAFEPATH`
before invoking `/usr/bin/bash -p ./run_all.sh` (plus refresh arguments when
needed).  The runner detects any surviving variable and aborts, but does not
falsely claim it can undo a constructor that ran before the script body.

The machine result status is `PREFREEZE_CODE_RESULTS_PASS`; documentation and
project status remain `PAPER_PENDING`.  The expanded-quartic, direct PARI
characteristic-zero factor, and delta-as-a-polynomial-in-theta feasibility
lanes are explicit non-results and are not certificate dependencies.
