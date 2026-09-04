# P194 process-separated hostile Review B

## Verdict

`PASS / ZERO OPEN FINDINGS / ACCEPTED_REPAIR / HOLD_EXTERNAL`

The current repaired P194 theorem package is provable as stated.  Review B
has `0 Critical / 0 Major / 0 Minor` open findings.  One historical Major
source-owner finding, P194-B1, was raised against the immutable Round-1
input and is now resolved.  The repair adds and fully subtracts the nearest
located deterministic crystal-dynamics source; it changes no theorem.

The binding external state remains `OWNER_AMBER / HOLD_EXTERNAL`.  This
acceptance is neither a novelty conclusion nor permission to circulate.

## Separation and frozen inputs

Reviewer B is neither the author nor Reviewer A.  The independent verifier
imports and executes neither implementation.  It was written before the
author verifier was replayed and uses a third family of representations.

The immutable input is
`papers/194-least-raising-crystal-words/main_round1.pdf`, SHA-256
`9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207`.
It is a four-page byte copy of the original Round-0 PDF.  The accepted
source-owner repair is separately frozen by current `main.tex`,
`references.bib`, `SOURCE_VERIFICATION.md`, and the five-page `main.pdf`,
whose SHA-256 is
`682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b`.
Review A is pinned as an immutable earlier review artifact, not reused as a
proof oracle.

## Independent representation

The author uses a stack signature, row insertion, direct semistandard-tableau
enumeration, hook-product division, corner-removal tableaux, and a scan of
all permutations.  Review A uses prefix-record minima, Greene invariants,
Jacobi--Trudi, the Aitken determinant, and a second permutation scan.

Review B instead uses:

- literal free-monoid rewriting by repeated adjacent `+- -> empty` deletion;
- Fomin's matrix-growth local rule for reverse-word RSK shape;
- Gelfand--Tsetlin interlacing and the `GL_r -> GL_{r-1}` branching recurrence
  for the Schur layers;
- cyclotomic-factor multiplicities for the hook-content product;
- literal linear orders of the Young-diagram cell poset for `f^lambda`;
- direct partial-matching generation of involutions.

The complete reviewer grid consists of all 34,636 words in the 35 boxes
`1 <= k <= 7`, `1 <= n <= 5`.  It deliberately reaches alphabet sizes not
covered completely by either earlier control.

## Hostile mathematical attacks

- **Signature orientation.** Literal reduction gives a unique residual word
  of minuses followed by pluses.  The witnesses `e_1(21)=11`,
  `f_1(11)=21`, and absence of both operators on `12` fix cancellation and
  edited occurrences.  Every available colour edge was inverted in the
  complete grid.
- **Tensor/RSK convention.** Ordinary insertion changes shape along
  `21 -> 11`, while insertion of the reversed words keeps shape `(2)`.
  Fomin growth diagrams preserve the reversed-word shape on every checked
  edge and component.
- **Least currently usable colour.** On `321`, both colours are available
  and the literal step is `321 -> 311` with colour 1.  The full displayed
  orbit of `333` has colour word `212121`, confirming that availability is
  recomputed after every single edge.
- **Exact clock and recurrence.** Every effective edge lowers letter sum by
  one.  Direct functional-graph reconstruction found one ballot endpoint in
  every crystal component, no nontrivial recurrence, and
  `tau(w)=sum(w)-sum_i i lambda_i` at all 34,636 states.
- **Sharp depth.** Every complete box has maximum `n(k-1)` with sole
  maximizer `k^n`; `n=1` and `k=1` were separately attacked through 14.
- **Schur layers.** The normalized Gelfand--Tsetlin branching polynomial
  agrees componentwise with actual depth histograms.  Independently, its
  coefficients agree with the hook-content product reconstructed from
  cyclotomic factors in all 102 allowed shape/alphabet cases.
- **Multiplicity and involutions.** Connected-component counts equal direct
  Young-poset linear-extension counts.  Involutions generated as matchings
  through `S_8` give the same shape counts and height truncations, totaling
  1,115 involutions.
- **Every-target fibre iff.** Actual incoming source sets agree with the
  highest self-source plus precisely the admissible `f_i(y)` candidates for
  every target.  Empty fibres and all boundary alphabets are included; fibre
  mass is exactly the carrier size.
- **Maximum fibre and boundary.** Full fibres occur in a complete box exactly
  at `n >= binom(k,2)`.  Forty-eight direct staircase witnesses cover
  `2 <= k <= 12` and four successive lengths; 6,495,612 subthreshold
  partition tests found no strictly decreasing padded weight.

## Source-owner finding and accepted repair

P194-B1 was Major because the frozen Round-1 source omitted Defant--Williams,
*Crystal Pop-Stack Sorting and Type A Crystal Lattices*.  Their Definition
2.1 defines a noninvertible macrostep to the unique source of the component
obtained by restricting to all descent colours of the starting vertex; their
theorem gives orbit-to-highest convergence and a sharp maximum orbit size.
That is too close a deterministic crystal-dynamics surface to omit.

The repair is adequate and exact.  The bibliographic record, DOI, and arXiv
identifier were added.  The abstract, Section 1, close, source ledger, and
companion documents assign the entire pop-stack orbit surface zero
contribution credit.  They also state the literal nonidentity: the pop-stack
map performs a restricted-component macrostep using the starting descent
set, whereas P194 takes one least-current raising edge and recomputes.  For
example, in the three-colour word component containing `321`, restriction to
both available colours has source `111`, while P194 takes only
`e_1(321)=311` in that epoch.

Nothing in the cited work was found to state P194's labelled one-step
predecessor atlas or its stable full-fibre threshold.  This is only a
bounded, convention-sensitive non-hit.  It does not clear ownership, and the
repair correctly preserves `OWNER_AMBER / HOLD_EXTERNAL`.

## Finding census

- Historical: `0 Critical / 1 Major / 0 Minor`, all resolved.
- Open: `0 Critical / 0 Major / 0 Minor`.
- Decision: `ACCEPTED_REPAIR`.
- Mathematical status: `PROVABLE_AS_STATED_AFTER_ACCEPTED_SOURCE_REPAIR`.

## Exact receipt

```text
reviewer states/transitions/targets: 34,636 / 34,636 / 34,636
reviewer components/fixed states: 235 / 235
reviewer assertions: 16,194,669
reviewer digest: 54651eac45dd17bad67185edbe91e72ece5ba976b871fa483cbb860e6756878b
reviewer replay 1 / replay 2: byte-identical
author replay 1 / replay 2: byte-identical
cold source-only PDF build 1 / build 2: byte-identical to current main.pdf
immutable Round-1 PDF SHA-256: 9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207
accepted repaired PDF SHA-256: 682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b
```

All five current pages were rasterized and inspected.  No mathematical,
source, owner-boundary, build, or presentation defect remains open.
