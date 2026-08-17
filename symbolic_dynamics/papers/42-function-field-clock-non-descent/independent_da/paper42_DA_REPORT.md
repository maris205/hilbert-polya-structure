# Paper 42 independent Devil's Advocate report

Review date: 2026-08-17 UTC

Portable review target:
`papers/42-function-field-clock-non-descent/preauthority`

Review mode: ARS deep-research Devil's Advocate / research-review checkpoint.
The package was treated as hostile input; seals were recomputed rather than
trusted. This report is outside the reviewed package and is bound by a separate
SHA-256 sidecar.

## Final seal reviewed

- `SHA256SUMS.txt`:
  `f8f3ada901a3e26735819db05e3bcd01a26e571a8f9bd6cc4af8e1a2e705a433`
- `RESEARCH_LOCK.json`:
  `fc4d3613165bebdd812789f0407329de983e1ec81020ef1024a665563293ffc2`
- `ROUTE_EXPECTATION.yaml`:
  `79eafee424590e0e1b65ffa7dc48d2a066a4822513ff1520f6bcf35593c6f71c`
- `SOURCE_HASHES.sha256`:
  `4d06a1149ad0288bee9fe84e7ac1d16a2fcfa9ca2ce8a9130e0bdc37fee10ad1`

The package manifest verifies 16/16 entries. Its path column is C-sorted,
unique, and self-excluding. The research lock maps 15 immutable files,
C-sorted and self-excluding; every mapping recomputes exactly. The actual
regular-file set is exactly the 16 manifest entries plus the manifest itself.

## Independent exact calculations

For the full `q` shift, a based word of period `r` is any of `q^r` words. Each
primitive necklace of least period `d | r` contributes `d` based words, hence

```text
q^r = sum_(d|r) d N_q(d),
N_q(n) = (1/n) sum_(d|n) mu(d) q^(n/d).
```

An independent enumeration of cyclic rotation classes gave:

| `q` | `#Fix(sigma^1,2,3)` | `N_q(1)` | `N_q(2)` | `[01]` primitive | forced clock label |
|---:|---|---:|---:|---|---:|
| 2 | 2, 4, 8 | 2 | 1 | yes | 4, composite |
| 3 | 3, 9, 27 | 3 | 3 | yes | 9, composite |
| 5 | 5, 25, 125 | 5 | 10 | yes | 25, composite |

The marked fixed-point exponential is independently

```text
exp(sum_(r>=1) q^r (z q^(-s))^r/r) = 1/(1-z q^(1-s)),
```

so the owned determinant is `D_q=1-z q^(1-s)`. Its primitive regrouping has
one factor `(1-z^n q^(-ns))^(-1)` per primitive length-`n` necklace.

Clock equality with a rational-prime factor forces `p=q^n`. The length-two
primitive `[01]` therefore defeats every total exact-clock map. Marker and
weight equality force `n=1` and `p=q`, while the source has `q` distinct
length-one classes and the rational Euler ledger has one factor at `p=q`.
This independently defeats marker/weight/multiplicity identification.

For the determinant comparison,

```text
[z](-log D_q) = q^(1-s),
[z](-log D_P) = P(s) = sum_p p^(-s).
```

After multiplication by `2^sigma` and `sigma -> +infinity`, the source limits
are `2,0,0` for `q=2,3,5`, whereas the target limit is `1`. The target tail is
dominated for `sigma>=2` by `sum_(n>=3)(2/n)^2`. Thus the comparison occurs on
the valid common domain `Re(s)>1` (and locally/formally in `z`) with the correct
determinant orientation.

## Theorem and quantifier verdicts

1. **Exact-clock total map:** PASS. Totality is necessary for a full source
   factor ledger, and `[01]` is a valid primitive class for every frozen
   alphabet. The theorem does not exclude partial maps or changed clocks.
2. **Marker/weight/multiplicity:** PASS. Based words and cyclic classes are not
   conflated: `N_q(1)=q` counts the `q` one-letter cyclic classes. The claim is
   limited to the declared free source-symbol marker and target prime-loop
   marker.
3. **First marked coefficient:** PASS. The diagonal target operator is trace
   class for `Re(s)>1`; coefficient mismatch proves analytic nonidentity without
   any zero data.
4. **Repair corollary:** PASS. Exhaustiveness is explicitly limited to the six
   listed repairs; `declared_repairs_are_exhaustive` is false in Route metadata.
5. **Positive source ledger:** PASS. The theorem does not damage source
   cyclicity, ordinary powers, finite-field norm, or determinant ownership.

The strongest counterargument is that the marker obstruction depends on a
chosen target marker and the closure theorem is elementary. The package handles
this correctly: the marker theorem is convention-bounded, the clock/support
theorem is independent of it, all classical source identities receive zero
novelty credit, and no universal function-field/number-field no-go is claimed.

## Selection and chronology

All six immutable Session-4 cards were parsed and the stated semantic rule was
reapplied literally. Results were:

```text
SD-C01 true
SD-C02 false
SD-C03 false
SD-C04 false
SD-C05 false
SD-C06 false
```

`SD-C01` alone has the required proved A0/A1/A2/A3 tuple, constant
finite-field degree clock, and explicit missing rational-prime primitive map.
The rule is nevertheless retrospective: all six outcomes and Paper-42
witnesses were known before it was written. The package consistently denies
prospective, outcome-independent, preregistration, novelty, priority, ranking,
and authorization credit. P39/P40/P41 are collision/governance inputs only.
No moving-goalpost or prospective-selection claim remains.

## Portable source and predecessor verification

The 29 source IDs are syntactically exact, C-sorted, unique, and hash-valid:
21 `repo:` IDs and eight Paper-41 dependency IDs. A separately implemented
typed resolver rejected all nine attacks: duplicate ID, non-C-sorted IDs,
unknown scheme, absolute repo ID, parent escape, missing repo file, missing
dependency, multiply resolved dependency, and dependency-root escape.

Predecessor verification independently passed:

- terminal P39 manifest: 91/91, with no-ranking/no-selection fields false;
- final P40 immutable research lock: 11/11, used only as a research boundary;
- portable P41 preauthority package: 15/15, with 14 immutable lock entries and
  no integration or authorization inference.

No Paper-42 authority directory existed during this review. No authority,
mirror, Git, README, registry, or paper-manifest write was made by this audit.

## Literature collision audit

Primary/authoritative checks confirmed the cited boundaries:

- Bowen--Lanford is listed by the official AMS PSPUM 14 volume as the 1970
  finite-shift zeta article; this owns foundational determinant prior art.
- arXiv:2605.11445 explicitly states that the necklace polynomial counts both
  aperiodic necklaces and monic irreducibles over finite fields; no novelty is
  assigned to that identity.
- arXiv:2606.02324 concerns cyclotomic factors of rational necklace functions,
  not the frozen clock/marker/multiplicity descent contract.
- DLMF 25.2.E11 gives the rational Euler product on `Re(s)>1`.
- the Stacks Project trace-formula treatment gives the finite-field closed-point
  Euler product and the `1/(1-qT)` affine-line specialization.

Citation-chain and synonym searches did not locate an exact published statement
of this project-specific typed closure. This bounded negative search is not a
theorem of novelty. The package's source novelty `0/10`, broad mechanism novelty
`0/10`, and conditional typed-closure rating remain appropriately conservative.

## Strict Route-A audit

The exact v0.2 top-level, source-lock, per-layer, and adversarial-control key
sets match the frozen schema fixture. All verdict and evidence-status literals
are legal. The tuple is exactly

```text
(A0_WEAK_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)
```

with `overall_verdict: ROUTE_A_REJECTED` and both Route-B booleans false. A1 and
A2 correctly remain positive for the source's own function-field species; no
coordinate is borrowed from the rational-prime comparator or another paper.

One Major was found in the superseded seal: `artifact_path_base` omitted the
frozen `preauthority` namespace. It was repaired before this report. In the
reviewed seal the base is exactly
`papers/42-function-field-clock-non-descent/preauthority`; all 26 artifact
references, spanning 11 distinct files, resolve from that package root.

## Hygiene and residuals

Zero trailing whitespace, carriage returns, host-absolute paths, symlinks,
cache files, bytecode files, NUL bytes, missing final newlines, and YAML tabs
were found. No Critical or Major issue remains against the reviewed seal.

## Verdict

`DA_ACCEPT_PREAUTHORITY`

The repaired package is CLEAN for root-governed authority consideration. This
is not authority authorization and does not create prospective or priority
credit.
