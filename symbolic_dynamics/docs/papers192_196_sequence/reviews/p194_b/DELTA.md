# P194 Review-B delta and repair acceptance

## Status

`ACCEPTED_REPAIR / ZERO OPEN FINDINGS / OWNER_AMBER / HOLD_EXTERNAL`

Reviewer B did not modify any file under
`papers/194-least-raising-crystal-words/`.  The author installed the only
requested repair; Reviewer B then re-read, rebuilt, and independently
retested the resulting package.

## Historical finding P194-B1

**Severity:** Major.  
**Round-1 decision before repair:** `REVISE_SOURCE_OWNER_SUBTRACTION`.  
**Current state:** resolved.

The immutable Round-1 manuscript omitted the closest located deterministic
crystal-dynamics source:

Colin Defant and Nathan Williams, *Crystal Pop-Stack Sorting and Type A
Crystal Lattices*, *European Journal of Combinatorics* 103 (2022), article
103514, DOI `10.1016/j.ejc.2022.103514`, arXiv `2109.08251`.

That paper defines a noninvertible crystal pop-stack operator by taking the
unique source of the connected component restricted to the starting
vertex's descent colours.  It proves that forward orbits reach the
highest/minimal vertex and gives a sharp maximum-orbit theorem.  Although
the literal map differs from P194, this overlap was too close to leave
uncited and unsubtracted.

## Author repair

The author:

1. added the full Defant--Williams bibliographic record to `references.bib`;
2. cited it in `main.tex` and described its Definition 2.1 macrostep;
3. assigned its deterministic crystal sorting, orbit-to-highest, and sharp
   maximum-orbit surfaces zero contribution credit;
4. distinguished its frozen descent-set restricted-component macrostep from
   P194's single least-current `e_i` edge with re-evaluation after each edge;
5. stated that the cited paper does not supply P194's letter clock, depth
   layers, labelled target atlas, or stable full-fibre threshold;
6. propagated the subtraction through `SOURCE_VERIFICATION.md`,
   `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`, `README.md`, `SELF_QA.md`,
   `PAPER_PLAN.md`, and `BUILD.md`;
7. preserved `OWNER_AMBER / HOLD_EXTERNAL` and every novelty disclaimer.

The accepted repaired core hashes are:

```text
d4c81d389dba055a3a232077e79058c09cae1be40b8822d49f976c4242d97ce9  papers/194-least-raising-crystal-words/main.tex
b8ab897d271bd4225dc71c4619fb5cbe6843afdc3d6a529705a927d37ce38faa  papers/194-least-raising-crystal-words/references.bib
203ae4ce3c750b5d45380db94f4096b99fcd776e035c2f880faef826f9e2323f  papers/194-least-raising-crystal-words/SOURCE_VERIFICATION.md
682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b  papers/194-least-raising-crystal-words/main.pdf
```

The immutable Round-1 PDF remains separately pinned at
`9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207`.

## Acceptance tests

- The journal title, volume, year, article number, DOI, authors, and arXiv
  identifier agree with the primary records.
- The cited Definition 2.1 is represented accurately: the colour set is the
  starting descent set and the image is the unique source of that restricted
  connected component.
- The current citation-key set and bibliography-key set are exactly equal,
  with six entries each.
- The subtraction occurs in the manuscript, not only in a companion ledger.
- No theorem statement was strengthened and no novelty, priority,
  completeness, or freedom-to-operate inference was introduced.
- Two fresh source-only builds are byte-identical to the current five-page
  `main.pdf`; all pages pass visual and mechanical PDF checks.
- The author verifier and independent Review-B verifier each pass two fresh
  byte-exact replays.

## Final delta

The accepted source repair is the only change required by Review B.  There
is no open mathematical, source, owner-boundary, code, build, or presentation
delta.

```text
historical findings: 0 Critical / 1 Major / 0 Minor, all resolved
open findings:       0 Critical / 0 Major / 0 Minor
decision:            ACCEPTED_REPAIR
external state:      OWNER_AMBER / HOLD_EXTERNAL
```
