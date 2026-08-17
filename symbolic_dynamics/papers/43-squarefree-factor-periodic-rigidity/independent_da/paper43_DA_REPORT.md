# Paper 43 Independent Devil's Advocate Report

Date: 2026-08-17 UTC

Review target ID: `paper43_squarefree_factor_periodic_rigidity`

Method: ARS deep-research Devil's Advocate and research-review workflow

Final verdict: `DA_ACCEPT_PREAUTHORITY`

## Executive verdict

No Critical, Major, or residual Minor defect was found in the final frozen
package. The theorem, selector, chronology, Route-A record, novelty boundary,
portable source contract, and seal hierarchy survive independent replay.

An earlier Minor was repaired before this final verdict. The old W6 used only
the modulus-four example to motivate the universal finite-exclusion claim.
The replacement bytes now give an exact construction for every finite prime
set, prove its least period in the nonempty case, and handle the empty case.

## Core theorem replay

For a prescribed pair of coordinates in every position of a finite window,
the source proof selects distinct primes. The corresponding prime squares are
pairwise coprime, so the Chinese remainder theorem gives a shift that forces
both translated points to vanish throughout the window. Agreement on
`[-L,L]` gives the stated product-metric tail `2^(1-L)/3`. Compactness makes
every continuous factor map uniformly continuous, and equivariance therefore
passes proximality to every compact metrizable onto factor.

The image of the zero point is fixed. Any second fixed point remains at a
positive constant distance from it. If a point has least period `r > 1`, the
finite set of adjacent orbit-point distances has a positive minimum. Either
case contradicts proximality. Thus every lawful factor has exactly one
periodic point, and for every `m >= 1`,

```text
#Fix(S^m) = 1
zeta_AM(z) = 1/(1-z)
D_AM(z) = 1-z
det(I-z[1]) = 1-z
```

The package correctly types `z^r` as a repeated traversal of the single
primitive fixed orbit, not as a new primitive object. It does not identify
that singleton primitive ledger with the infinitely supported rational-prime
ledger.

## Finite-exclusion sharpness repair

For an arbitrary finite set `P0` of rational primes, the repaired proof sets

```text
Q = product_{p in P0} p^2,
x_n = 1 iff n = 1 mod Q.
```

If `P0` is nonempty, every `p^2` divides `Q`, so the support modulo `p^2` is
exactly the singleton residue `{1}`. The point satisfies all finite
admissibility constraints. It has least positive period `Q`: if `d > 0` is a
period, `x_1 = 1` implies `x_(1+d) = 1`, hence `Q` divides `d`. Since every
nonempty `P0` gives `Q >= 4`, this is a nontrivial periodic orbit.

If `P0` is empty, `Q = 1`, the constraints are vacuous, and `1^Z` and `0^Z`
are two distinct fixed points. Therefore every finite prime-square
approximation fails both the full source's periodic collapse and its
proximality conclusion. The universal statement, least-period quantifier, and
empty-set edge case are consistent in the witness ledger, source lock, proof,
derivation, methodology, README, DA handoff, and Route control.

## Selector, chronology, and Route

The declared retrospective survivor set is exactly `{C02,C03,C05}`. Literal
replay uniquely selects C02: C03 fails the required A1/A2/source clauses and
C05 fails A0/A2. Every selection document disclaims prospective,
outcome-independent, ranking, authorization, and priority interpretations.

The strict Route-A v0.2 tuple is exactly

```text
(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)
overall = ROUTE_A_REJECTED
route_b_invocation_allowed = false
```

All required top-level and A0--A4 fields use permitted labels. The 26 Route
artifact references, covering 11 distinct paths, resolve within the declared
portable preauthority base. The repaired arbitrary-finite-set control is
bound into the Route record.

## Novelty boundary

The package makes no standalone novelty claim for the mathematical
ingredients. Primary-source replay confirms that squarefree/B-free
proximality and the unique zero minimal subsystem are known; the recent
power-free factor literature is adjacent but does not supply the exact
arbitrary-target periodic-count/Artin--Mazur closure audited here. No exact
published duplicate was located in the bounded search. The package therefore
appropriately assigns zero novelty to the ingredients and at most minimal
internal credit to the typed closure. This is a conservative literature
boundary, not a priority claim.

Primary anchors used in the replay:

- P. Sarnak, *Three Lectures on the Mobius Function, Randomness and Dynamics*.
- Bartnicka--Kasjan--Kulaga-Przymus--Lemanczyk,
  `arXiv:1509.08010`.
- Kasjan--Keller--Lemanczyk, `arXiv:1702.02375`.
- Gundlach--Kluners, version 2, `arXiv:2407.08438`.

## Integrity replay

- `SHA256SUMS.txt`:
  `f35b469d6a438d9a9e1f03e0682d85590b1010dd2acfe82b4f2ceef677d68d8f`,
  16/16 entries valid.
- `RESEARCH_LOCK.json`:
  `b8d05c2407e2d7b7a6b8c435cf7d757420f627b64f9d44e328443079b923adb0`,
  15/15 immutable mappings valid.
- `ROUTE_EXPECTATION.yaml`:
  `d4fc1f7bfcd7024929b6eec28679ed39d456dde4f3eeb77d79a5349885d6da7a`.
- `SOURCE_HASHES.sha256`:
  `46bba074ebe91bc7e5e1e4fd704cb9eecc9ce7066d87b91f832ca7a571b973b3`,
  unchanged and previously replayed 40/40 through the portable resolver.
- Both manifests are C-sorted, unique, self-excluding, and newline-terminated.
- No host-absolute path, trailing whitespace, CR/NUL byte, symlink, cache
  directory, or Python bytecode was found.

The review modified no package, authority, mirror, Git, README, or manifest
bytes.
