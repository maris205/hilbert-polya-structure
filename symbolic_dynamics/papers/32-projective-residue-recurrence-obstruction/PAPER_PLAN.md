# Paper plan — Paper 32 / SD-C34

## Configuration

| Item | Frozen choice |
|---|---|
| Paper type | theoretical obstruction / diagnostic paper |
| Field | symbolic dynamics, arithmetic dynamics, operator determinants |
| Working title | *Projective Residue Recurrence in Symbolic Dynamics: Universal Modular Cycles and Cusp-Diamond Obstructions* |
| Candidate | SD-C34 |
| Main language | English |
| Citation style | author-year (`plainnat`) |
| Output | modular LaTeX and PDF |
| Review target | field-general; no venue-alignment claim |
| Review loop | explicitly skipped by user |

## One-sentence contribution

We prove that a source-natural projective-residue grammar has nonterminal
shared recurrence and an honest same-object Fredholm determinant, yet cannot
separate primes because universal modular cycles and cusp diamonds force
composite primitive support before weights, while the exact static field test
is a forbidden terminal selector.

## Research question

Can a shared-state recurrent grammar derived from the finite-full-shift
semiring distinguish prime primitive cycles without an accept/reject terminal
and still own a determinant on its unchanged graph-step operator?

## Claims/evidence matrix

| ID | Claim | Evidence | Planned location |
|---|---|---|---|
| C1 | \(|P^1(\mathbb Z/n\mathbb Z)|=\psi(n)\), with \(n+1\) exactly at primes | local-ring representatives, CRT proof | §3, Appendix A |
| C2 | \(S^2,R^3\) give marker-distinct recurrent families through every state and every modulus | direct matrix multiplication and least-return argument | §4 |
| C3 | downward cross maps are transient, while bidirectional cusp maps create primitive composite diamonds | monotone modulus and explicit four-cycle proof | §5, Figure 2 |
| C4 | the unchanged \(B_s\) is trace class on \(\operatorname{Re}s>2\) and owns an ordinary Fredholm determinant | divisor-sum and rank-one trace-norm bounds | §6 |
| C5 | determinant ownership does not repair the composite primitive ledger | positive \(SS\), \(RRR\), and diamond trace contributions | §6 |
| C6 | the static field projector is terminal-selector equivalent | C1 plus block-projector identity | §7 |
| C7 | the mechanism is copied by matched semiring relabels and generic at the \(C_2*C_3\) relation level | transport theorem, random-action controls | §8 |
| C8 | strict tuple has A1 failure but A2 analytic success | C1--C7 and source lock | §9 |

## Structure pattern

The manuscript uses a theoretical conference-paper structure rather than
IMRaD.  The proof spine stays in the main text; expanded local and analytic
proofs move to Appendix A.

| Section | Purpose | Target words |
|---|---|---:|
| Abstract | state the trilemma, strongest obstruction, exact finite controls, and route decision | 190 |
| 1. Introduction | inherit Paper 31, state the nonterminal test and contributions | 850 |
| 2. Literature and source boundary | position projective/Farey/determinant literature and freeze admissible information | 900 |
| 3. Projective residue source | define states and prove the static field criterion | 950 |
| 4. Universal modular recurrence | prove shared-state overlap and generic presentation control | 900 |
| 5. Cross-modulus cusp diamonds | prove the transient/recurrent dichotomy and composite flood | 850 |
| 6. Same-object Fredholm ownership | define \(B_s\), prove trace class, expose composite trace terms | 1,100 |
| 7. Why static separation is terminal | analyze the forbidden projector and claim boundary | 650 |
| 8. Exact audit and adversarial controls | report finite census, matched clone, random action, and reproducibility | 800 |
| 9. Strict route closure | apply A0--A4 and close the branch | 650 |
| 10. Conclusion | summarize progress, limitations, and Paper 33 obligation | 500 |
| Main body total |  | 8,340 |

## Transition logic

1. The Introduction turns Paper 31's terminal failure into a concrete
   nonterminal obligation.
2. Literature and source lock distinguish classical ingredients from the new
   controlled question.
3. Projective geometry shows that static arithmetic separation is available.
4. Modular relations then test whether that separation enters recurrence; it
   does not.
5. Cross-modulus coupling shows that sharing moduli adds a second composite
   flood rather than fixing the first.
6. The operator section repairs analytic ownership and separates A2 success
   from A1 failure.
7. The projector section explains why the obvious repair violates the source
   lock.
8. Exact controls show the failure is structural, clone-stable, and
   reproducible.
9. Route closure records what was achieved and why the candidate still stops.
10. The conclusion states the only admissible Paper 33 continuation.

## Figure plan

| ID | Type | Description | Source | Placement |
|---|---|---|---|---|
| Figure 1 | pure TikZ concept graph | prime and composite projective blocks both carry overlapping \(S/R\) recurrence | Theorem C2 | §4 |
| Figure 2 | pure TikZ cycle diagram | \(n\to2n\to6n\to3n\to n\), with composite top and shared neighboring diamond | Theorem C3 | §5 |
| Figure 3 | pure TikZ trilemma/route diagram | static separator, universal recurrent flood, honest determinant, forbidden gate | C1, C4, C6, C8 | §9 |

All figures are vector TikZ with redundant shape/line-style encodings.  They
contain no plotted empirical data and no decorative title inside the graphic.

## Table plan

- Table 1: distinction among classical ingredient, paper-specific use, and
  novelty boundary.
- Table 2: exact finite control census, including prime/prime-power/mixed
  strata, matched clones, random actions, diamonds, tests, and repeat runs.
- Table 3: strict Route-A tuple with evidence and failure reason.

## Bibliography plan

Use only DOI-verified sources actually cited: Blunck--Havlicek; Jones,
Singerman--Wicks; Katok--Ugarcovici; Mayer; Chang--Mayer; Bonanno--Isola;
Simon; Saniga et al.  Classical claims proved in the paper do not require
inflating the bibliography.

## Writing constraints

- Front-load the single obstruction claim in title, abstract, introduction,
  and Figure 1.
- Do not call the projective state space or modular relations new.
- Keep “same-object Fredholm ownership” distinct from prime selectivity.
- Use “search-bounded” for novelty and name Chang--Mayer as the closest
  analytic collision.
- Never claim a prime theorem, zeta identity, functional equation, critical
  line, self-adjoint carrier, zero correspondence, or RH consequence.
- Retain the exact tuple and branch action verbatim.
- Include limitations, data/code availability, ethics, CRediT, conflicts,
  funding, and AI-assistance disclosure.

`criteria_binding_unavailable`: no venue-specific review target was supplied,
so the plan makes no venue-alignment claim.
