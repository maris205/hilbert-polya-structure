# P167 claims--evidence ledger

**Freeze:** anonymous author Round 0  
**Theorem status:** provable as stated  
**Owner status:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`

## Claim ledger

| ID | Frozen claim | Proof dependency | Exact-control dependency | Status |
|---|---|---|---|---|
| C1 | Every literal first image has only cycle or loop-rooted-path components; cycles invert and paths follow the root-comparison reverse/split rule | distinct first positions; direct symbol-occurrence calculation | parses and reconstructs every image through `n=7`; checks all labelled paths/cycles through size 9 | proved and checked |
| C2 | A nonsingleton path is recurrent iff both endpoint comparisons descend | C1 plus irreversibility of component splitting | exact tail/period of every path order through size 9 | proved and checked |
| C3 | Path tail is at most `2s-2`, with equality only for the decreasing path | induction after a one-step split or two-step reverse/split | all `s!` paths for `1<=s<=9` | proved and checked |
| C4 | Full height is `2n-2`; first-image height is `2n-3` for `n>=2`; both are zero at `n=1` | C3, mandatory value zero, explicit increasing-path witness | all states and literal image points through `n=7` | proved and checked |
| C5 | Connected recurrent counts are `c_1=1,c_2=1,c_3=4,c_s=(s-1)!+s!/4`; the stated EGF counts all recurrent states | cycle enumeration, two endpoint inequalities, labelled `SET` assembly | recurrence and closed EGF agree through order 14; exhaustive recurrence through `n=7` | proved and checked |
| C6 | Fixed states are involutions; odd positive iterates fix `I_n`, even iterates fix `R_n`; zeta has the stated two-factor form | component action and period-at-most-two classification | every point and powers `1..6` through `n=7`; literal cycle-orbit recount | proved and checked |
| C7 | The optional-present/product formula equals the fibre of every target | forced first positions, fixed-position collision exclusion, converse construction | every target through `n=7`, including unsupported adversaries | proved and checked |
| C8 | Maximum fibre is `B_n`, attained by the identity | injection by source kernel partition; block-minimum construction | Bell prefix and all restricted-growth sources through `n=7` | proved and checked |
| C9 | Boundary table for `n=1,2,3` is exact | direct `n=2` graph; uniform formulas; `n=3` fibre histogram | complete edge/tail/period/fibre transcript | proved and checked |

## Exact theorem ceiling

The manuscript may state the conjunction C1--C9 for the literal
identity-default selector.  It may not promote any of the following to a
claimed contribution:

- least kernel transversals or the identity `f M(f) f=f`;
- the kernel-representative retraction `M(f) f`;
- first-occurrence/restricted-growth encodings or Bell numbers;
- generic functional-digraph component language;
- labelled component EGFs or involution numbers;
- the Artin--Mazur definition and its standard orbit-product conversion.

The off-diagonal-injection condition is necessary only; C7 is the exact
first-image test.  C8 asserts an attained maximum, not uniqueness of the
identity maximizer.  No result is stated for an arbitrary missing-symbol
default or for a different transversal rule.

## Reproducibility evidence

```text
verifier: verify_p167.py
assertions per replay: 12,603,676
fresh replays: 2
byte-identical: yes
verifier SHA-256: b7c10bd3738362397a97361ca3780c4f53c7297efbe3e1885175634b345b457b
transcript SHA-256: 1e7348f9eab389cffc14582b3cf26ebeec69cb72a6c77dbdb1fb204abd1e1a8c
decision: AUTHOR_ROUND0_PASS
external status: HOLD_EXTERNAL_OWNER_THIN
```

The verifier is standard-library only and imports no scouting or manuscript
module.  The frozen stdout is `verification_output.txt`.

