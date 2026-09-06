# Independent hostile candidate gate — MIP

**Candidate:** minimum inverse-position feedback on `[n]^[n]`  
**Gate date:** 2026-09-03 UTC  
**Verdict:** `GREEN_OWNER_THIN / ELIGIBLE_FOR_INTERNAL_PAPER_SLOT`  
**External lifecycle:** `HOLD_EXTERNAL`  
**Findings:** `0 Critical / 0 Major / 0 Minor`

## Outcome first

The proposed theorem contract survives independent reconstruction without a
formula repair.  The sharp carrier height `2n-2`, sharp first-image height
`2n-3`, recurrent component census and EGF, fixed/iterate counts, zeta,
every-target one-step fibre, and Bell maximum all agree with literal
exhaustion.  The small orders `n=1,2,3` are internally consistent.

The candidate is nevertheless only owner-thin.  Its first step is a
least-kernel-transversal inner inverse, its identity fibre is the classical
block-minimum encoding of set partitions, and generic component/EGF/zeta
machinery is fully owned.  The bounded search found no source iterating the
specific identity-on-missing extension, but that non-hit is not novelty or
priority evidence.

## Independence firewall

Only the literal definition and claims to attack were taken from the intake
contract.  The earlier scout verifier, canonical output, proof text, and
search conclusions were not imported.  This gate has its own standard-library
verifier, canonical transcript, two new process replays, proof derivation,
primary-source owner search, and P1--P166 audit.

## Claim-by-claim attack

| claim | hostile route | result |
|---|---|---|
| first-image structure | derive distinct first positions; parse every literal image through `n=7` | PASS; components are cycles or loop-rooted paths |
| off-diagonal condition scope | enumerate every target, not only actual images | PASS with required caveat; at `n=7`, 12,960 of 63,840 off-diagonal-injective targets are still unsupported |
| component action | calculate symbol occurrences in one path; enumerate all path orders and canonical cycles through size nine | PASS; cycles invert, paths reverse or split by the root comparison |
| recurrent paths | attack both endpoint inequalities and irreversible split converse | PASS; special sizes `1,2,3` handled separately |
| path height | induction under endpoint deletion; exhaust all `s!` paths through `s=9` | PASS; `2s-2`, uniquely at the decreasing path |
| image/carrier heights | exclude the full decreasing path from the first image using the mandatory zero value; test displayed source | PASS; `2n-3` in the image and `2n-2` globally for `n>=2` |
| recurrent census/EGF | independently count cycles and endpoint orders; compare component recurrence to closed EGF through order 14 | PASS; prefix `1,1,2,8,38,220,1540,12460` |
| fixed and iterate counts | classify fixed components; check every state and powers `1..6` through `n=7` | PASS; odd powers `I_n`, even powers `R_n` |
| zeta | recount one- and two-cycle orbits from literal graphs | PASS; exponents `I_n` and `(R_n-I_n)/2` |
| every-target fibre | reconstruct forced/optional symbols; compare formula against every target through `n=7` | PASS, including unsupported and fixed-position collision targets |
| Bell maximum | show target+kernel partition forces labels; inject all set partitions over identity; exhaust through `n=7` | PASS; `B_n`, prefix `1,2,5,15,52,203,877` |
| KRR relation | compute `e_f=M(f) o f` independently | PASS as background: `e_f` is the least-block retraction, `e_f^2=e_f`, `ker(e_f)=ker(f)` |
| P1--P166 collision | range audit plus focused P105/P110/P114/P115/P143/P154--P156/P166 comparisons and DFJ control | PASS internally; shared ingredients explicitly subtracted |
| direct owner | bounded exact and structural primary-source search | no literal iterate owner hit; retain `OWNER_THIN`, not novelty |

## Exact exhaustion summary

| n | states | image | recurrent | fixed | two-cycles | carrier height | image height | maximum fibre |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |
| 2 | 4 | 3 | 2 | 2 | 0 | 2 | 1 | 2 |
| 3 | 27 | 14 | 8 | 4 | 2 | 4 | 3 | 5 |
| 4 | 256 | 84 | 38 | 10 | 14 | 6 | 5 | 15 |
| 5 | 3,125 | 612 | 220 | 26 | 97 | 8 | 7 | 52 |
| 6 | 46,656 | 5,220 | 1,540 | 76 | 732 | 10 | 9 | 203 |
| 7 | 823,543 | 50,880 | 12,460 | 232 | 6,114 | 12 | 11 | 877 |

Here "two-cycles" counts dynamical orbits, not points.  The recurrent point
identity is `R_n=I_n+2*(two-cycles)` in every row.

## Fibre collision probes

The exhaustive target pass contains all cases, but four sentinels make the
failure modes visible:

| target | intended attack | exact fibre |
|---|---|---:|
| `(1,0,1)` at `n=3` | repeated off-diagonal first position | 0 |
| `(1,2,2)` at `n=3` | no available symbol at position zero | 0 |
| `(0,0,2)` at `n=3` | fixed coordinate occupied by another symbol's forced first position, but target remains supported | 2 |
| `(1,1)` at `n=2` | same fixed/forced collision plus unopened first position | 0 |

These cases confirm that optional present fixed symbols must be restricted to
`F={i:g(i)=i, i notin g(U)}` and that zero factors are essential.

## Reproducibility decision

The final verifier executes **12,603,676** exact assertions.  Two fresh
processes produced byte-identical 9,818-byte transcripts:

```text
verifier SHA-256:  acb630523348a26f90a37aac45d9e17e33db13addfe0fc7aab1c71e9f4ab56e0
canonical SHA-256: d566ede8a559273ec25757c7dcf7dd6f8bbd7ef15cc855f2a38a974a2d4f5b8f
replay 1 SHA-256:  d566ede8a559273ec25757c7dcf7dd6f8bbd7ef15cc855f2a38a974a2d4f5b8f
replay 2 SHA-256:  d566ede8a559273ec25757c7dcf7dd6f8bbd7ef15cc855f2a38a974a2d4f5b8f
```

## Terminal recommendation

Promote MIP as an internal, anonymous, owner-thin short-paper candidate.  A
paper may claim the literal iteration's conjunction of sharp clocks,
recurrent species, and target-resolved inverse formula.  It must not claim
the kernel transversal, first-occurrence encoding, Bell mechanism,
functional-digraph decomposition, labelled-species conversion, involution
numbers, or zeta construction as new.

This gate assigns no public novelty, authorship, priority, submission, or
release permission.  Any external step remains blocked pending a specialist
transformation-semigroup owner review.
