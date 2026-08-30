# C243 source and scope audit

## Source lock

The code/evidence baseline is `489506cf92bfed721f94f22dd0444a60427f90a5` and
the fixed build epoch is `1788048000` (30 August 2026 UTC).  The Route-A
authority is `flow_systems/skills/route-a-evaluator.md`, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## Mathematical sources

Smerzi, Fantoni, Giovanazzi and Shenoy, “Quantum coherent atomic tunneling
between two trapped Bose-Einstein condensates,” Phys. Rev. Lett. 79 (1997),
4950–4953, DOI `10.1103/PhysRevLett.79.4950`, preprint
`https://arxiv.org/abs/cond-mat/9706221`, supplies the two-mode population/phase
equations and self-maintained imbalance convention.  Raghavan, Smerzi,
Fantoni and Shenoy, “Coherent oscillations between two weakly coupled
Bose-Einstein condensates,” Phys. Rev. A 59 (1999), 620–633, DOI
`10.1103/PhysRevA.59.620`, preprint
`https://arxiv.org/abs/cond-mat/9706220`, supplies the analytic elliptic
solutions and macroscopic self-trapping context.  The exact ledger here is a
source-local derivation, not a priority claim.

## Evidence boundary

The canonical model is
\(H=\Lambda z^2/2-\sqrt{1-z^2}\cos\phi\).  Bloch coordinates give
\(\dot x=-\Lambda zy,\dot y=z(1+\Lambda x),\dot z=-y\), so the poles are
not silently treated as regular \(\phi\)-chart points.  The quartic roots,
elliptic periods, sech profile, pitchfork, and component criteria are checked
by independent code and symbolic/numeric identities.  At \(\Lambda=1,H=1\)
the level is only the isolated point \(z=0\); for \(\Lambda>1,H=1\) the
critical level is connected with two one-sided homoclinic branches.

## Firewall and Route-A verdict

All nine scope flags are false.  No target prime/zero table, local arithmetic,
Euler factor, root number, automorphy, target divisor, functional equation, or
Hilbert–Pólya operator appears.  Regular levels form a continuum, so A1 is
`A1_WEAK`; A0, A2 and A3 fail, and A4 is only `A4_NATURAL_QUANTIZATION`.
Route B is disabled.
