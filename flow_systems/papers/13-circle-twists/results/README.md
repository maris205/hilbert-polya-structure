# Paper 13 generated controls

This directory contains twelve canonical CSV artifacts and `manifest.json`.
The first eleven CSV bodies retain the amended-v1 `/1` contracts; only
`completion_corona_controls_v2.csv` uses schema `/2`.  The v1
`target_summary.csv` remains a historical 2,548-row snapshot, while the v2
CSV contains the authoritative augmented `2665 / 67 / 176` summary.

`manifest.json` binds the frozen authority DAG, six implementation files, and
twelve CSVs.  It never binds itself or a concurrently changing proof.
Strict verification evaluates candidate row semantics and the recursive
manifest firewall before enforcing exact byte identity.
