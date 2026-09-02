# Source and collision audit

## Frozen provenance

- Candidate: `HCS-C299`
- Obstruction: `HEN-O283`
- Source commit: `83c058259c02707d004fca2d6b1a4ebaf5036094`
- Fixed epoch: `1788307200`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Evaluator authority SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`

## Source ownership

`Oseen-1912-Arkiv-7-no14` is retained as the classical bibliographic owner token for the viscous line-vortex profile.  Gallay and Wayne, *Global Stability of Vortex Solutions of the Two-Dimensional Navier--Stokes Equation*, Communications in Mathematical Physics 255 (2005), 97--129, DOI `10.1007/s00220-004-1254-9`, supplies published modern mathematical context.  The DOI metadata was checked for title, authors, journal, volume, pages, and year.

This package reconstructs every formula it uses and makes no historical priority claim.  Its short-paper contribution is the closed theorem/evidence/boundary package, not the invention of the classical Lamb--Oseen vortex.

## Nearest collision boundaries

- **C206 is not being relabeled.**  C206 is Couette advection--diffusion on \(\mathbb T\times\mathbb R\) with Fourier shearing.  C299 is radial planar vorticity with velocity reconstructed by Biot--Savart; nonlinearity cancels because velocity and gradient are orthogonal.
- **C207 is not being relabeled.**  C207 treats scalar nonlinear diffusion and Barenblatt profiles.  C299 uses linear viscous diffusion only after a geometric reduction of Navier--Stokes, and adds circulation, induced velocity, exact particle angles, a point-vortex boundary, and infinite-energy analysis.

## Claim firewall

The symbols \(\Gamma\), \(\nu\), Gaussian moments, and exponential integrals are source-side fluid quantities.  They are not rational-prime labels, prime-power weights, Euler factors, root numbers, or target spectral zeros.  The dissipative evolution is not asserted to be a Hilbert--Polya operator.  Route B is not invoked.
