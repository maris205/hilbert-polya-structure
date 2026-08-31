# Claims–evidence ledger — P129

Status vocabulary:

- `PROVED`: all-parameter mathematical proof in the manuscript.
- `EXACT_CONTROL`: finite exact arithmetic corroboration.
- `PILOT_ONLY`: excluded from the manuscript theorem contract.
- `OWNER_HOLD`: bounded non-hit; no novelty or release decision.

| ID | Exact claim | Manuscript proof | Paper-local control | Status |
|---|---|---|---|---|
| C1 | Every trajectory reaches `{0}`, and `G_S(z)=z/(|S|-1) sum_v G_{C_v(S)}(z)`. | Strict integer potential descent and first-step conditioning. | Every enumerated transition decreases the potential; every exact law normalizes. | `PROVED + EXACT_CONTROL` |
| C2 | `supp(T_S)={max S,...,sum S}` for every rooted nonabsorbing state. | Induction on potential using the maximum move or the bottom of its occupied run. | Full support compared for every rooted subset through the distribution range. | `PROVED + EXACT_CONTROL` |
| C3 | For `S={0=s_0<...<s_r}`, `E[T_S]=sum_i h(s_{i-1},s_i)`. | Finite-site Poissonized embedded chain with strong Markov at effective times; consecutive-label-block induction; predictable jump compensator; finite-time expectation, monotone convergence, Tonelli; two-path marginal. | Bellman and interface recurrences compared exactly for every rooted subset through `n=14` (16,383 states). | `PROVED + EXACT_CONTROL` |
| C4 | `h(a,a)=0`, `h(0,b)=b`, and `h(a,b)=1/2+(h(a-1,b)+h(a,b-1))/2`. | First event among two rate-one clocks, with one-clock root boundary. | Entire finite recurrence triangle audited. | `PROVED + EXACT_CONTROL` |
| C5 | `h(m-1,m)=(2m-1)!!/(2m-2)!!=2m binom(2m,m)/4^m`. | Catalan/ballot decomposition; explicit central-binomial telescoping; bounded optional stopping for the event-type gap walk. | Exact identity for every `m=1..80`. | `PROVED + EXACT_CONTROL` |
| C6 | Full occupancy has the double-factorial mean sum. | C3 plus C5 over its adjacent interfaces. | Exact full-state distributions and independent mean calculation. | `PROVED + EXACT_CONTROL` |
| C7 | Full occupancy has leading mean `4/(3 sqrt(pi)) n^(3/2)+O(n^(1/2))`. | Central-binomial estimate followed by summation. | Consequence of the exact formula; no numerical fit used. | `PROVED` |
| C8 | The minimum full-state time is `n-1` with mass `1/(n-1)!`. | Unique descending all-collision order. | Exact PGFs through the declared range. | `PROVED + EXACT_CONTROL` |
| X1 | Maximum full-state time has a simple endpoint mass. | No complete manuscript proof. | May be printed only under an explicit `PILOT_ONLY` label. | `PILOT_ONLY / NOT CLAIMED` |
| O1 | No direct external owner was found for the literal deterministic-rootward, uniform-active-pile embedded-update theorem package. | Not a mathematical claim. Assiotis, Hitczenko--Wesołowski, and Śniady--Urbán are direct zero-credit mechanism neighbors. | Bounded primary-source query log and subtraction audit. | `OWNER_HOLD` |

## Nonclaims

- No independence of different interface lifetimes.
- No reversible or unbiased random-walk kernel.
- No multiplicity-retaining pile process.
- No uniform geometric-site lazy scheduler.
- No rooted-tree theorem.
- No novelty, priority, authorship, posting, or submission decision.
