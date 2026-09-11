# P215 Review B no-change source-only build preparation

The accepted B delta is proposed no-change and both strict outputs are raw
equal to canonical. This build copies exactly eight TeX/BibTeX sources from
accepted physical `frozen_round1` into a new isolated cold tree under
`reviews/p215_b/build01`. It adapts the already accepted P215 A source-only
recipe only in role, preparation/binding/output paths and Round1 source root.

The 227-row runtime manifest was copied from the accepted P215 A build and
freshly checked in full against current files for this B binding. The build
uses four TeX/BibTeX passes, no shell escape, complete pass snapshots,
diagnostics/font/text capture and all-page PNG rendering. Any failure tree is
preserved without retry. A separate root one-use grant remains required.
