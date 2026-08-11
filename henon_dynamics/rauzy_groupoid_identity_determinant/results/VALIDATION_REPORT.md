# HCS-C29 validation report

## Verdict

`INDEPENDENT_CHECKER_PASS_14_OF_14`

The checker does not import the producer or a shared C29 arithmetic module.  It
reconstructs the graph and matrices from elementary Rauzy moves and the six
locked upstream artifacts.  Its matrix multiplication, unimodular inversion,
word reduction, chronology, census and certificate schema are independently
implemented.

## Gate table

| Gate | Status | Independent target |
|---|---|---|
| G0 source lock | PASS | six upstream file hashes and chronology enum |
| G1 exact graph | PASS | literal seven-state Rauzy graph and fourteen arrows |
| G2 frames/fixed fibre | PASS | spanning-tree frames, common form and fixed matrices |
| G3 formal inverse semantics | PASS | endpoints, inverse matrices and antiparallel-edge separation |
| G4 chronology | PASS | later-on-the-left products and wrong-order sentinel |
| G5 primitive/inverse rotation | PASS | cyclic closure, powers, rotations and dihedral separation |
| G6 C25 witnesses/gauge | PASS | both exact cycles and nontrivial symplectic gauge family |
| G7 all versus primitive census | PASS | complete length-one-to-nine dynamic enumeration |
| G8 C26 braid/relation | PASS | elementary paths, rank-one algebra and derived 24-word |
| G9 repetition/torsion | PASS | `C1^2`, order-four `Delta` and character-power firewall |
| G10 finite-Weil limit | PASS | upstream C28 status and fixed-length limit scope |
| G11 normalized determinant | PASS | `Log_0`, norm discs, moment definition and determinant type |
| G12 semantic firewalls | PASS | natural extension, roof/operator status and Route-A stop |
| G13 payload envelope | PASS | exact schema, key set and canonical payload digest |

## Exact replay outputs

```text
exact C25 N_6                         24
C26 marked N_24 lower bound          48
C25 Hashimoto norm bound              3
C26 Hashimoto norm bound              5
natural-extension escape              FAIL_GERM_EQUALS_ONE
symmetric groupoid algebraic gate      PASS_EXACT
```

## Independence limits

The two programs necessarily read the same frozen upstream repository files
and test the same mathematical specification.  Independence here means
separate reconstruction and implementation, not an independently collected
external dataset or a formal proof assistant.

The bounded C25 census is recomputed in full by the command-line checker.  The
unit-test process computes that expensive independent census once and
deep-copies it across mutation cases; this optimization is confined to the
test harness and cannot affect the release checker.

No environment fingerprint, Python version, hostname or current working
directory is included in the canonical certificate payload.

## Integrity hashes

| Artifact | SHA-256 |
|---|---|
| Producer source | `92062ae57274c74434189b5a46466194fdd7394b3adb44cf562413db121d88ea` |
| Independent checker source | `58b00b2cc2cc69dfaf41e2be2905c19b98eb35e06cb0a6ce4f59688fd7d2cf91` |
| Test source | `f829967923adbdcaab434272dd0ae9c35a769903607f5018ee9c562da753cfba` |
| Exact certificate | `412840c37d2e474462b39ce7072614323023ac8e3f968bc16a9219cc3a0c0cca` |
| Independent report | `f87ab0efb191be7ac68936c5eb25e95ba2dbfa2719614750c99f1934e918b215` |

The release manifest is the authoritative whole-project integrity record; the
table above freezes the central Phase-2 replay at checkpoint time.
