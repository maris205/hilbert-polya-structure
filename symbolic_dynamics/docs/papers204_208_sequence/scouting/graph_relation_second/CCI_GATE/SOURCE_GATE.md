# CCI: independent source and formula-transfer audit

2026-09-05 UTC. This is bounded direct-owner checking, not a novelty or
priority certificate. Only primary material supports source deductions.
Search snippets from aggregators, teaching pages, unrelated colouring and
domination papers were not treated as read theorems. No manuscript was
uploaded, no specialist contacted and no external-review API invoked.

## Primary sources actually read

### 1. Conflict detection: model inclusion, not theorem inclusion

Motskin, Roughgarden, Skraba and Guibas,
[*Lightweight Coloring and Desynchronization for Networks*, author PDF](https://www.timroughgarden.algorithmsilluminated.org/papers/desync.pdf).
Read scope: title, Section II-A's precise model and Algorithm 1 on PDF p.2.
The model permits a colour-selection function of current colour and a
single conflict bit, deterministic or randomized. CCI is explicitly included
by $f(c,0)=c$, $f(c,1)=c+1\pmod q$. Thus neither the information model nor
the idea of recolouring on conflict receives credit.

Algorithm 1 instead samples a colour uniformly when conflicted; its proper
colouring convergence statement concerns that randomized rule. CCI retains
every initial conflicted edge forever. Hence the algorithm and its proof
do not directly imply CCI's all-source modular waiting-time or inverse
formula. Inclusion in a model permitting arbitrary local functions is not
ownership of every function's exact dynamical theorem. Full-paper claims
beyond the inspected passages are not used.

### 2. CCA and Greenberg–Hastings: different literal triggers

Gravner, Lyu and Sivakoff,
[*Limiting behavior of 3-color excitable media on arbitrary graphs*, author journal PDF](https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf),
Annals of Applied Probability 28(6) (2018), 3324–3357,
DOI 10.1214/17-AAP1350. Read scope: the GHM/CCA equations on PDF p.2,
the monotone comparison/covering-space introduction on p.3, and the
initial 1-form definitions on p.4; not the entire 34-page proof.

CCA increments in the presence of the successor colour, whereas CCI
increments in the presence of its own colour. On a monochromatic single
edge CCA holds and CCI rotates. GHM distinguishes resting/excited/refractory
states; its all-zero edge holds, while CCI's rotates. The source's comparison
construction is established methodology, but the inspected equations do
not identify equality-triggered persistent activation or the stated initial
modular-distance formula. No arbitrary nonlinear factor impossibility is
inferred merely from this literal separator.

### 3. Firefly automata: an inhibitory, phase-marked rule

Lyu,
[*Time complexity of Synchronization of discrete pulse-coupled oscillators on trees*, arXiv:1610.00837v3 PDF](https://arxiv.org/pdf/1610.00837).
Read scope: v3 title/version metadata (revised 7 March 2023), Section 1.1's
FCA equation on PDF p.3, and Section 2.1's width-lemma formulation and
initial proof on pp.8–9. This is the revised title; the older title in some
search results was not silently used as current metadata.

FCA usually increments and only holds when a post-blinking state sees the
designated blinking colour. CCI usually holds until any own-colour neighbor
appears. For $q=3$ on an edge, $01$ is fixed under CCI but FCA sends it to
$12$ (blinking colour one). In fact FCA cannot have every vertex hold on
a nonempty graph: any holding vertex needs a blinking neighbor, and a
blinking vertex advances. CCI has proper fixed states. Thus these complete
systems are not bijectively conjugate; a time-dependent colour frame by
itself is not an autonomous conjugacy. No source theorem is transferred.

### 4. The 2-total-cover class is owned

Fernau, Fomin, Philip and Saurabh,
[*On the parameterized complexity of vertex cover and edge cover with connectivity constraints*, author journal PDF](https://fedorvf.github.io/articles/2015/2015f.pdf),
Theoretical Computer Science 565 (2015), 1–15,
DOI 10.1016/j.tcs.2014.10.035. Read scope: abstract, the exact $t$-total
vertex-cover definition on PDF p.2, and Section 3's algorithmic problem
framing. At $t=2$ this is exactly a vertex cover inducing no singleton
component. CCI did not invent the cover notion. Isolates are forced outside
the cover; the empty-cover convention is handled explicitly in the CCI
statement rather than hidden in a connected positive-size source convention.

The inspected material studies decision/optimization and parameterized
algorithms. It is not a count of all such covers maximized over all graphs,
nor a colour-predecessor constraint or a CCI inverse theorem. Full-paper
negative claims are not made from the selected sections.

### 5. Total-cover counting already has complexity results

Molinero, Riquelme and Serna,
[*Satisfaction and Power in Unanimous Majority Influence Decision Models*, author final draft](https://upcommons.upc.edu/server/api/core/bitstreams/331d37a2-b15a-44a0-9de1-85a36f5f6d7b/content),
Electronic Notes in Discrete Mathematics 68 (2018), 197–202,
DOI 10.1016/j.endm.2018.06.034. Read scope: deposited cover-sheet metadata,
Section 2's total-cover discussion, Theorem 2.4's proof sketch and Corollary
2.5 on PDF pp.5–6. Corollary 2.5 states #P-completeness for counting total
vertex covers. Its connected, nontrivial construction makes the cover class
agree with the no-isolated-component condition here.

This newly located source is an explicit deduction against any claim of a
new counting object, new general counting programme or efficient all-graph
decoder. The inspected proof uses a universal-vertex construction; it does
not state the star maximum for the total number of covers on fixed order.
The CCI static extremal lemma is therefore kept only as self-contained
support, without separate originality credit. The author accepted that
boundary; this source must be carried into any draft.

## Internal originals inspected and exact transfer tests

The four originals below are pinned in INPUTS.sha256. Searches also covered
same-colour/equality, conflict increments, first activation, irreversible
activation, first-passage/Bellman and total-cover terms across actual
manuscripts and old scouting notes. Search non-hits carry no positive weight.

| Original read | Concrete mechanism and obstruction |
|---|---|
| [P118](../../../../../papers/118-synchronous-mex-multipartite-dynamics/main.tex), literal map, quotient and temporal outline | Open-neighborhood mex on complete multipartite graphs. Its quotient keeps unique low colours and replaces others by a mex, with fixed/two-cycle recurrence. CCI on one edge has period $q\ge3$. Thus no surjective autonomous factor of that period-at-most-two system can cover this complete CCI system. Generic graph colourings and quotient bookkeeping are zero credit. |
| [P164](../../../../../papers/164-cyclic-equality-feedback/main.tex), definition and all parts of its main theorem | It outputs an equality bit and enters an affine binary difference tail; the admitted dyadic carrier ultimately fixes. CCI retains the whole colour and advances it, with $q$-cycles even on a seed edge. Its arbitrary-graph activation and cover/predecessor inverse do not follow from the binary code-kernel formula. |
| [P202](../../../../../papers/202-ternary-ordered-reset/main.tex), literal rule, source subtraction and complete one-step decoder | Ordered one-sided increment/reset; zero always advances and there are no fixed states. Its nonzero one-step fibres are powers of two from independent $01$ choices. CCI has proper fixed states and a four-vertex star/constant target has fibre seven. Thus even the inverse-fibre invariant prevents a bijective conjugacy to this rule; its independent local choices cannot supply the coupled CCI mask constraints. |
| [Old root Bellman spike](../../../../papers197_201_sequence/scouting/root_graph_bellman/THEOREM_SPIKE.md), entire original contract | Literal bounded-height min-envelope update; all orbits fix and its inverse is an inequality/inclusion–exclusion formula. Its shortest-path primitive receives zero credit. CCI's weights are oriented initial colour residues, the seeds depend on the source, and nonfixed recurrent states rotate. Treating these source-dependent data as a fixed graph-height map does not give an autonomous conjugacy or transfer its target inverse. This was an old scout, not an accepted P200 theorem. |

The links above are documentary inputs, not write targets. Nearby historical
manuscripts and accepted evidence were unchanged.

## Additional proof-mechanism pressure

Generic irreversible infection gives shortest distances *after* fixed
transmission delays and seeds have been supplied. CCI's specific content is
the proof that its endogenous equal-colour events give precisely the
initial-colour directed delays, even with competing seeds and wraparound,
and that this controls the original coloured-state entrance and period.
The active mask alone does not give an autonomous Boolean flooding factor:
on the three-vertex path at $q=3$, $001$ and $002$ have the same initial
active set $\{0,1\}$, but their next states are $111$ and $112$, whose
active sets differ. This rules out the naive unweighted-mask identification;
it does not claim that no enriched representation is possible.

For the inverse, simply enumerating masks would be generic finite-map
bookkeeping. The surviving exact statement instead characterizes all masks
by a target-induced cover class and a directed closure condition, then
transfers a self-contained global extremum with all graph/target equality
cases. The proof route is independent of first-activation distances.
The known static cover object and elementary extremal tools remain deducted.

## Search ceiling and disposition

External literal queries included `same color neighbor increment automaton`,
`same-coloured neighbour increment`, `synchronous coloring increment conflict`,
`conflict detection deterministic cyclic`, `number of total vertex covers`,
`2-total vertex covers maximum number`, and named CCA/GHM/FCA and cover
sources. Follow-ups on total-cover literature distinguish minimum cover
*size* from the *number of all covers*. Related minimum-size sources and
aggregator snippets were not claimed as proofs of the latter extremum.

No exact earlier owner or complete formula-level transfer was established
in the inspected originals. That absence is not the positive GO argument.
The positive basis is the proved literal two-axis contract surviving the
specific model, primitive, recurrence and inverse deductions above. Verdict:
`GO_NARROW_THEOREM_CONTRACT / OWNER_AMBER / HOLD_EXTERNAL`; exact earlier
ownership evidence would reopen it. There is no promise of external venue
quality or originality, and no separate new-static-theorem claim.
