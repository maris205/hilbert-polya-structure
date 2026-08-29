# Claims-to-evidence map — P112

Status: **author-stage claim lock / external HOLD**.

| Claim | Analytic proof | Independent exact control |
|---|---|---|
| arbitrary-label update is simultaneous | `Phi_V` is defined for every finite `V`; every edge reads the unchanged old score vector and restrictions use internal scores | literal set-of-arcs update versus bit update through `n=6` |
| squared-score energy is strict exactly on changed states | write `delta_v` as incoming-minus-outgoing incidence in the complete reversal set, then expand `sum_v (s_v+delta_v)^2` | exact gain identity for all tournaments through `n=6` |
| `Phi(T)=T` iff the reversed-upset set is empty | the rule reverses exactly those arcs and retains every other arc | local predicate compared with update equality for every enumerated state |
| no nontrivial periodic points | strict integer energy on a finite phase space | first eight iterate-fixed sets checked state by state through `n=6` |
| first image is the ordinal sum of old score classes | unequal classes are reoriented downward; tied internal edges remain | explicit block embedding compared with every bit-coded image |
| every later iterate factors inside old classes | new score intervals `[L_i,L_i+|C_i|-1]` are disjoint; global and internal comparisons differ by `L_i` | direct iterates compared with reconstructed factorized iterates through time `n` |
| pointwise depth is refinement-tree height | a nonfixed node has at least two smaller children; after the first step two global iterates agree iff every restricted factor agrees, giving `tau(T)=1+max_i tau(T[C_i])` in both directions | literal orbit depth versus independently recursive depth for every state |
| `tau(T)<=n-1` for `n>=1` | induction on block size; nonfixed states have at least two score classes | complete depth histograms through `n=6` |
| fixed points are unique ordered sums of regular tournaments | equal global score plus uniform external wins; converse block-score separation | terminal and starting-state structure predicates for every state |
| low-credit `f_n=sum_j binom(n,j)r_j f_(n-j)` and `F=1/(1-R)` | choose the unique top regular block; generic labelled sequence construction | independently count regular tournaments and fixed states through order six |
| zero-credit `zeta_(Phi_n)=(1-z)^(-f_n)` | every periodic point is fixed; apply the standard zeta definition | iterate-fixed control through period eight |
| mask `148` is least only in the specified scan | finite statement only: orders increase, then numeric masks increase; no analytic or global-depth minimality asserted | exhaustive ordered scan for every labelled tournament through `n=6` |

Boundary registration: `[n]={i in Z: 0<=i<n}`, so `[0]` is literally empty.
The `n=0` and `n=1` systems are singleton identities with depth zero, fixed
count one, and zeta `(1-z)^(-1)`.

Credit registration: Landau/Moon/Ryser/Thomassen/ESA 2026 tournament
structure and reversals, Rubinstein/Henriet/Bouyssou/Linares--Bodanza score
procedures, McKay regular enumeration, labelled-EGF machinery, and zeta
bookkeeping are all zero-credit.  Only the exact conjunction for the specified
synchronous map remains residual and owner-HOLD.

Forbidden claims: sharp global depth, full transient enumeration, direct-owner
clearance, absolute novelty, priority, or external-release readiness.
