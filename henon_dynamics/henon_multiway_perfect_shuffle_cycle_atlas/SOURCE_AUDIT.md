# Source and scope audit

* Frozen source/code baseline: `489506cf92bfed721f94f22dd0444a60427f90a5`.
* Evaluator authority: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
* Build epoch: `SOURCE_DATE_EPOCH=1788048000` (2026-08-30 UTC).
* Frozen owner: the Ellis--Fan--Shallit multiway perfect shuffle
  \\(\\rho_{k,n}(i)=ki\\bmod(kn+1)\\) on nonzero residue positions.
* Allowed data: exact integer congruences, direct finite permutations,
  symbolic identities, and reproducible source references.
* Sealed/forbidden data: target primes or zeros, arithmetic local data, Euler
  factors, root numbers, automorphy, target divisors, and Hilbert--Pólya
  operators.

The map is a finite permutation for every declared integer pair.  Gcd strata
preserve orientation, and direct cycles agree with the order and Möbius
formulas.  The package is distinct from necklace rotations, finite-field
linear maps, and stochastic riffle/carry chains: its owner is positional
interleaving with the exact modulus \\(kn+1\\).  The out-shuffle is only a
convention comparison and is not silently mixed into the certificate.

The two primary records are Ellis--Fan--Shallit (DMTCS 5, 2002, DOI
`10.46298/dmtcs.308`) and Packard--Packard (*Fibonacci Quarterly* 32(2),
136--144, 1994, DOI `10.1080/00150517.1994.12429237`).  Citation metadata is
locked in the independent checker and repaired-hash mutation suite.
