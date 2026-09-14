# Paper configuration record

## Identity

| Parameter | Value |
| --- | --- |
| **Title** | *AI-Guided Exploration of Arithmetic Dynamical Systems: Constraints, Failure Modes, and Search Strategies toward Hilbert--Pólya Structures* |
| **Paper type** | Conference-oriented theoretical/methodological research record and source-bound Phase-I synthesis |
| **Current venue** | None; generic single-column A4 layout, not a submission template |
| **Language** | English |
| **Author** | Liang Wang |
| **Affiliation** | School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430070, P.R. China |
| **Contact** | wangliang.f@gmail.com |
| **Repository** | <https://github.com/maris205/hilbert-polya-structure> |
| **PDF build** | LuaLaTeX + BibTeX via [`latex/build.sh`](latex/build.sh) |
| **Historical evidence window** | `419ee36c1e310469209f7b83c096ec8aea448386`, 2026-09-13 UTC |

## Research question and contribution

The central question is not whether Phase I proves RH.  It is how a human-governed, AI-executed programme can make the search for arithmetic dynamical candidates broad, falsifiable, and auditable without permitting source drift, autonomous scope expansion, or cross-object credit transfer.

The paper's contributions are:

1. A **three-layer, human-governed, AI-executed framework**: the mathematician owns the prime-symbolic research origin and scientific authority; a jointly drafted, human-approved `AGENTS.md` fixes the search contract; and bounded AI execution ends in an evidence handoff and mathematician review before another round may begin.
2. An updated roadmap treated as an evidence-obligation architecture.
3. A visual, non-additive six-direction evidence landscape.
4. A same-object ownership invariant across arithmetic source, clock/repetition, orbit, determinant, and later operator.
5. A **prime-symbolic lineage gate** and preservation ledger that restrict the next-round candidate portfolio to documented descendants or transformations of the project’s arithmetic-symbolic starting point.
6. Detailed source-bound research summaries in appendices rather than unsupported main-text claims.

## Human--AI governance rule

The framework distinguishes scientific authority from bounded execution in
three layers:

```text
Layer 1: mathematician fixes the prime-symbolic research origin, permitted
         arithmetic data, and admissible families / branches / dimensions
        ↓
Layer 2: jointly drafted, human-approved AGENTS.md research contract
         = constraints + testable route + breadth-first strategy + stop rules
        ↓
Layer 3: bounded AI execution -> evidence handoff -> mathematician review
        ↖ new human authorization or revised contract before any further round
```

The operative `AGENTS.md` must state four items before an AI search tranche begins:

1. lineage and search-space constraints, including permitted families, branches, dimensions, transformations, and arithmetic inputs;
2. a clear multi-level decision route with direct evidence requirements and typed, unordered operational outcomes such as `GO`, `HOLD`, `FORK`, and `END`, with every stage testable;
3. a generally breadth-first candidate-portfolio strategy that compares controls and near-miss objects before deepening; and
4. mathematical and operational termination conditions, including a named roadmap boundary, hard contradiction or route closure, loss of the lineage/same-object condition, a scoped negative result, or exhaustion of the specified token/compute/time allocation.

At a stop, the AI must hand back the candidate ID, lineage ledger, direct
evidence, controls, route disposition, exact stopping trigger, and resource
status.  `GO`, `HOLD`, `FORK`, and `END` govern the authorized workflow; they
are not mathematical Route-A/Route-B verdicts.  A budget stop ends an execution
tranche but carries no negative mathematical conclusion.  This is a prospective
framework distilled from Phase-I lessons, not a claim that every historical
Phase-I session used a uniform `AGENTS.md` or AI workflow.

## Candidate-admission rule

The paper formalizes the following as a methodological rule:

```text
prime-symbolic ancestor
  -> named non-autonomous deformation, dimensional/conservative lift,
     geometric realization, or explicitly stated preservation failure
  -> one fixed candidate card
  -> A0 -> A1 -> A2 screening
  -> only then later analytic / quantum obligations
```

Each arrow must be described by an actual mechanism: for example, a named observable, symbolic admissibility condition, evolution law, projection, semiconjugacy, invariant, return relation, clock, or an explicitly `OPEN` preservation claim.  “High-dimensional,” “area-preserving,” “symplectic,” or “quantum” alone does not satisfy the rule.  If prime data, zero data, a per-prime schedule, or a borrowed determinant is manually attached after the fact, the construction is not an admitted main candidate.

## Nonclaims and boundaries

- No proof of RH, completed Hilbert--Pólya realization, prime-power trace formula, completed-Ξ determinant identity, or Riemann-zero spectral identification is claimed.
- The six Phase-I lines are not a common scorecard; local results and process labels do not accumulate across objects.
- The current roadmap is an author-proposed search/evidence diagram, not proof of its arrows or a dashboard of completed gates.
- The recommendation to search candidate architectures more broadly is a reasoned Phase-I design recommendation, not a statistically established optimum.
- External AI papers provide background only.  They do not establish broad autonomous mathematical competence or validate this research programme.

## Declarations to complete for a submission

The manuscript includes an author attribution and an accurate AI-use disclosure.  Before a venue submission, the author must confirm or replace the funding statement, add a competing-interests declaration, use the venue’s required ethics/availability wording, select the correct template, and produce an anonymous variant if the review policy is double-blind.  Freeze the cited materials at a release tag or archival version before sending the paper externally.
