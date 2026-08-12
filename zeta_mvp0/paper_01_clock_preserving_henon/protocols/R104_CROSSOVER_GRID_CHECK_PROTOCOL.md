# R104 — Grid Check for the Magnetic Crossover

## Design

R103 reused converged \(B=0,1\) cells but evaluated \(B=0.25,0.5,2,4\) on
only the \(h=0.0225\) grid.  R104 computes those four fields at \(h=0.03\)
and compares the same 25--164 mode window.

Gates:

- median relative level change below 1%;
- coarse/fine mean adjacent-ratio difference below 0.03.

The looser ratio gate reflects the finite 140-level window and was fixed
before R104 execution.  All failed fields remain reported.
