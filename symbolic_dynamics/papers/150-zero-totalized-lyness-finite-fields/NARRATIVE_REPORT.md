# P150 narrative report

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**

## Core story

The rational Lyness map

```text
(x,y) -> (y,(1+y)/x)
```

is classically five-periodic in its special parameter-one form whenever the
displayed divisions remain defined. P150 asks a different literal question:
what is the complete finite dynamical system obtained on `F_q^2` when inverse
zero is assigned the value zero?

The answer is rigid. Away from the three singular lines and the coordinate
axes, the classical five-step identity survives. The entire complement is not
irregular: the axes form explicit cycles, while the remaining points form
three disjoint tail layers feeding one distinguished two-cycle. The same
case split also solves every inverse problem.

## Claim progression

1. Define five explicit subsets: the generic Lyness locus, the union of the
   coordinate axes, and three exceptional layers of depths one, two, and
   three.
2. Prove that these subsets are pairwise disjoint and cover every affine
   point. This is the proof hinge; a cardinality sum alone is not used as
   coverage.
3. Compute the five rational iterates on the generic locus. Separately compute
   the axis action and every exceptional arrow. This gives the recurrent set,
   pointwise tails, and sharp temporal polynomial.
4. Solve the fixed equation and classify inversion pairs on the axes. Since
   five is prime, every nonfixed generic point has exact period five. This
   yields the complete cycle census and zeta function.
5. For a target `(u,v)`, the first coordinate forces the source to be `(x,u)`.
   The remaining equation has `q` solutions only at `(-1,0)`, no solution on
   `(-1,v)` for `v!=0`, and one solution elsewhere. The resulting inverse law
   proves that the displayed exceptional in-tree has no missing vertices.

## Strongest quantitative conclusions

- recurrent points: `q^2-3q+5`;
- maximum tail: exactly `3` for every odd `q`;
- tail polynomial:
  `(q^2-3q+5)+(q-1)z+(q-2)z^2+(q-2)z^3`;
- cycle counts: `1+r_q`, `2`, `(q-3)/2`, and
  `((q-2)(q-3)-r_q)/5` in lengths `1,2,4,5`;
- image size: `q^2-q+1`;
- fibre sizes: exactly `q`, `0`, or `1` according to the target rule.

## Ownership subtraction

Lyness's original cycle observation, classical five-periodicity, its QRT and
type-`A_2` cluster interpretations, projective denominator handling, Kanki's
different extended-space/almost-good-reduction treatment of finite-field
singularities, and general finite-field integrable birational dynamics are
prior background. They are cited and receive zero contribution credit. The
paper's residual is only the exact zero-totalized all-affine completion and
its tail/cycle/fibre graph.

Hostile Review A returned **ACCEPT WITH MINOR REPAIRS — 0 Critical / 0 Major /
2 Minor** after independently rederiving the full theorem. The repaired proof
now says explicitly that the
nonfixed generic states partition into five-element orbits, simultaneously
proving the displayed exponent is integral; it also records the `q=3` and
characteristic-five boundary cases. The source ledger now exposes its query
families and candidate exclusions and subtracts the Lyness (1942) and Kanki
(2013) primary records explicitly. No claim changed.

Hostile Review B returned **0 Critical / 0 Major / 1 Minor, REVISE**. It
confirmed both Review-A repairs, rederived every theorem interface, replayed
the owner ledger and exact verifier, reproduced the PDF in two isolated
source-only builds, and accepted all 5/5 pages. Its only finding was that
`FINAL_QA.md` still described round-zero provenance as current. The present
round-2 Markdown closure repairs that documentary defect; no mathematical,
ownership, computational, build, or visual issue remains unresolved.

The primary-source audit did not locate a direct owner for that full
conjunction. This bounded non-hit is not novelty, priority, ownership, or
release evidence. A direct owner would reopen the contract.

## Evidence posture

The mathematical statements are proved symbolically for every odd finite
field. The local verifier independently constructs finite fields, evaluates
the literal map at every state in its declared boxes, and checks all strata,
orbits, cycles, fibres, and exceptional predecessor sets. Enumeration is
falsification evidence only.

The accepted current artifact is 5 A4 pages and 403,358 bytes, SHA-256
`26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca`.
The canonical replay passes 2,144,131 assertions; all 5/5 references resolve;
two isolated source-only builds are byte-identical to current `main.pdf`; and
all 5/5 pages passed visual inspection. During this Markdown closure, root
separately froze `main_round2.pdf`; a read-only comparison confirms byte
identity with current `main.pdf` at the accepted size and digest.

## Release boundary

The note is anonymous. It uses no external dataset, human participant, animal
subject, personal information, or stochastic experiment. No public posting,
specialist contact, submission, Git action, or release is authorized. Status
remains `ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL`.
