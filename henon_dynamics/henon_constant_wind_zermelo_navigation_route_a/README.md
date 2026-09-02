# HCS-C305: constant-wind Zermelo navigation atlas

This package gives a single all-parameter theorem for
\(\dot x=W+u\) on \(\mathbb R^d\), for every finite \(d\ge1\), constant
wind \(W\), measurable controls \(|u|\le c\), and every target displacement.
It completely classifies weak, critical, and strong wind reachability;
minimum time; attainable-time sets; unique optimal controls; HJB and scaling
geometry; Mach-cone regularity; and the zero-wind, zero-cap, and zero-target
faces.

The 29-case evidence archive is regression support only. The theorem follows
from the exact fixed-time ball and a scalar quadratic inequality, with the
smaller strong-wind root selected by first contact.

Key artifacts:

- `THEOREM_PACKAGE.md` — theorem and complete proof.
- `paper/main.pdf` — final short paper.
- `results/c305_zermelo_evidence.json` — canonical self-hashed receipts.
- `code/c305_release_manifest.py` — full release audit.
- `evaluations/route_a/HCS-C305/2026-09-03.yaml` — strict Route-A decision.

Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. All five Route-A branches fail and
Route B remains locked.
