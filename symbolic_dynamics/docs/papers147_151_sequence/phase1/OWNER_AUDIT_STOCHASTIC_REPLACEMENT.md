# Direct-owner and claim-subtraction audit — stochastic replacement

**Audit date:** 2026-09-01 UTC.  **External status:** `HOLD_EXTERNAL`.

## Executive decision

- `S09` remains a permanent kill under the exact P136 conjugacy recorded in
  `OWNER_AUDIT_S09.md`.
- `S08` is now also a **permanent kill**.  Its literal kernel is exactly the
  classical annihilation process on the conflict graph `L(K_{2,n})`.  A new
  overlap-supermartingale argument proves

  `e^(-6)/n <= 1-p_n <= H_n/n`,

  but the logarithmic gap and absence of an asymptotic constant do not leave a
  paper-sized residual after subtracting the direct process owner.
- Three new literal systems were then tested.  Random inversion sorting (`R12`)
  and Bernoulli--Laplace exchange (`R13`) are direct-owner/firewall kills.
  Finite-spider absorption (`R11`) is the replacement:
  **`PASS_OWNER_THIN / INDEPENDENT REPLICATION REQUIRED BEFORE FREEZE`**.

The strongest surviving conjunction for `R11` is a leaf-marked all-time
Chebyshev rational transform, a compact variance formula, sharp fixed-total
mean extremizers with equality classes, and exact recovery of the arm lengths
from endpoint probabilities plus the mean.  General tree absorption
probabilities and expected lengths are explicitly zero credit.

No decision in this file is a worldwide novelty, priority, or release claim.

### Second-pool closure

Four non-graph mechanisms were subsequently subjected to exact pilots.  None
met the R11 value gate: `R14` (fair randomized halving) is an internally
occupied one-scalar digit contraction; `R15` (totient--radical descent) has
the infinite clock collision `Law_p(T)=Law_(2p)(T)` for every odd prime `p`;
`R16` (random derivative-GCD/squarefree reduction) has a full clock law that
depends only on the maximum factor multiplicity; and `R17` (random two-braid
smoothing) is the Kauffman state sum.  The second pool therefore records
**`NO SELECTION / VALUE GATE ENFORCED`**.

## 1. S08: exact annihilation-process conjugacy

### 1.1 Literal map

The vertices of `L(K_{2,n})` are the edges of `K_{2,n}`.  Two such vertices
are adjacent exactly when the corresponding bipartite edges conflict.  Thus
S08 is

1. start with every vertex of `L(K_{2,n})` occupied;
2. choose uniformly an edge whose two endpoints remain occupied;
3. fair-delete one endpoint;
4. stop when the occupied set is independent.

O'Hely and Sudbury's [*The annihilating
process*](https://doi.org/10.1239/jap/996986655) defines particles which kill
neighbouring particles, with isolated particles surviving forever.  Penrose
and Sudbury's [*Exact and approximate results for deposition and annihilation
processes on graphs*](https://arxiv.org/abs/math/0503519), Section 2.1, gives
the finite-graph version: every graph edge receives an independent continuous
event time and a fair attack direction; if both endpoints remain occupied at
that time, the attacked endpoint becomes vacant.  Section 2.2 observes that
the terminal occupied set is independent.

Scanning the independent edge times and ignoring events with a dead endpoint,
the next effective edge is uniform among the currently occupied edges.  Its
attack direction is fair.  Therefore its embedded effective-event chain is
exactly S08 on `L(K_{2,n})`.  This is equality of transition kernels, not a
similarity of outputs.

### 1.2 New analytic lemma package

Write the two current row sets as `A,B`, put

`a=|A|`, `b=|B|`, `x=|A intersect B|`,

and let `q_n=1-p_n` be the probability that the final matching has size one.
The doubled total event rate is

`D=a(a-1)+b(b-1)+2x`.

For `a,b>=2`, direct substitution gives

`E[Delta{x/(ab)} | a,b,x]`

`=x[-2ab+(a+b)x+a+b-2x] / [ab(a-1)(b-1)D] <= 0`.

If `a<=b`, the numerator is increasing in `x` and at `x=a` equals
`(b-a)(1-a)<=0`.  Hence `x/(ab)` is a supermartingale until the first row
becomes a singleton.

Let `Q_b` be the failure probability from one singleton row overlapping a
row of size `b`.  First-step analysis gives

`Q_1=1`,

`Q_b=[1+(b-1)^2 Q_(b-1)]/[b(b-1)+2]`.

For `R_b=bQ_b`, this becomes

`R_b=R_(b-1)+[b-2R_(b-1)]/[b(b-1)+2]`.

Induction gives `R_b<=H_b`.  At the first singleton time `sigma`, failure has
conditional probability `0` if the singleton does not overlap, and `Q_b` if
it does.  Therefore optional stopping yields

`q_n <= H_n E[x/(ab) at sigma] <= H_n/n`.

For a lower bound, suppress the vertical clocks and run the two independent
within-row clique death processes.  Their final labels are independent and
uniform, so they agree with probability `1/n`.  Conditional on a common final
label, let `K(t)` be one row's size and `m(t)=E[K(t)-1]`.  The pure-death rates
are `C(k,2)`, hence Jensen gives

`m'(t)=-E C(K(t),2) <= -m(t)(m(t)+1)/2`.

With `m(0)=n-1`,

`m(t) <= r(t)/(1-r(t))`,

`r(t)=[(n-1)/n] exp(-t/2)`,

and consequently

`integral_0^infinity m(t)^2 dt <= 2(n-1-log n)`.

The expected absorption time of one row is `2(1-1/n)`, so the expected
maximum of the two row times is below four.  The expected integrated overlap
before both rows reach their common singleton is therefore below six.  The
probability that no vertical clock rings during that overlap is at least
`exp(-6)` by Jensen.  On this event the common singleton pair is eventually
resolved by its vertical edge, giving

`q_n >= exp(-6)/n > 1/(729n)`.

The exact verifier checks the four-state lumping against labelled graphs,
the potential drift for every `2<=a,b<=30`, the transformed singleton
recurrence through `b=120`, and the rational consequences through `n=20`.

### 1.3 Claim subtraction and decision

| tier | source/object | consequence |
|---|---|---|
| **DIRECT literal process** | O'Hely--Sudbury 2001 and Penrose--Sudbury 2005 annihilation process | the graph process, random event order, fair endpoint deletion, and independent-set jammed state receive zero credit |
| **EXACT carrier encoding** | conflict graph `L(K_{2,n})`, two cliques joined by a perfect matching | line-graph/matching language cannot distinguish S08 from the owned process |
| **INTERNAL nearest endpoint** | P141 threshold-greedy MIS | output object is nearby, but the external direct kernel owner is the decisive collision |
| **RESIDUAL lemma** | three-coordinate lumping, two-point clock, endpoint symmetry, and the bounds above | mathematically valid special-carrier facts, but no sharp asymptotic or closed `p_n` transform survived this round |

**Final S08 decision:** `KILL_DIRECT_OWNER_AND_VALUE`.  The numerical values
`nq_n -> approximately 0.3` are a useful clue, not an asymptotic theorem.
Biasing edge clocks or renaming the process as conflict deletion cannot reopen
the candidate.

## 2. Replacement breadth: three new literal systems

| ID | literal system | exact pilot | decision |
|---|---|---:|---|
| R11 | simple random walk from the centre of a finite spider; every leaf absorbs | all 340 ordered arm profiles with at most four arms and lengths at most four; coefficient comparison through profile-dependent horizons | **PASS OWNER-THIN** |
| R12 | choose a uniform inversion of a permutation and swap its entries | every permutation through order seven | **KILL random sorting/direct owner** |
| R13 | choose a uniform occupied and unoccupied label of a `k`-subset and exchange them | every `2<=n<=11`, `1<=k<=floor(n/2)`, exact returns through time six | **KILL Bernoulli--Laplace direct owner** |

These are not parameter sweeps of one mechanism.  They are respectively an
absorbing spatial walk, a monotone random sorting chain, and a recurrent
fixed-rank exchange chain.  None is a deletion/renaming of S08 or S09.

## 3. R11: finite-spider theorem envelope

### 3.1 Literal system

For positive integers `ell_1,...,ell_r`, join `r` paths of those edge lengths
at one common centre.  Start simple random walk at the centre.  Internal arm
vertices have the two equiprobable path moves, the centre chooses one of its
`r` neighbours uniformly, and every leaf is absorbing.  Record `(I,T)`, the
first leaf and the first-passage time.

### 3.2 Leaf-marked rational transform

Define

`P_0=0`, `P_1=1`, `P_2=2`,

`P_l=2P_(l-1)-z^2P_(l-2)`.

Thus `P_l(z)=z^(l-1)U_(l-1)(1/z)`.  Put

`P=product_j P_(ell_j)`,

`D=rP-z^2 sum_i P_(ell_i-1) product_(j!=i)P_(ell_j)`.

Then

`F_i(z)=E[z^T 1{I=i}]`

`=z^(ell_i) product_(j!=i)P_(ell_j)/D`.

This follows by decomposing the walk into independent centre-to-centre failed
excursions followed by one successful centre-to-leaf excursion.  On a path of
length `ell`, the two gambler's-ruin transforms from position one are

`1/U_(ell-1)(1/z)` and
`U_(ell-2)(1/z)/U_(ell-1)(1/z)`.

The formula gives the entire marked law, not only a matrix inverse or a first
moment.  It also gives the exact parity support and first atom

`Pr(T=ell_i,I=i)=1/[r2^(ell_i-1)]`.

### 3.3 Exact moments

With

`H=sum_i ell_i^(-1)`, `L=sum_i ell_i`, `C=sum_i ell_i^3`,

two differentiations give

`Pr(I=i)=ell_i^(-1)/H`,

`E T=L/H`,

`Var(T)=(C-2L)/(3H)+L^2/(3H^2)`.

An independent renewal-moment check uses, for one arm excursion of length
`ell`,

`E D=ell`, `E D^2=ell(ell^2+2)/3`,

and

`E[D 1{excursion returns}]=2(ell^2-1)/(3ell)`.

### 3.4 Sharp fixed-mass theorem

Fix `r` and `L>=r`; write `L=qr+s`, `0<=s<r`.  Since `E T=L/H`, integer
majorization of the convex reciprocal gives

`L/[r-1+1/(L-r+1)] <= E T`

`<=L/[(r-s)/q+s/(q+1)]`.

The lower equality class is exactly the permutations of
`(L-r+1,1,...,1)`.  The upper equality class is exactly the balanced profiles
with `s` arms of length `q+1` and `r-s` of length `q`.

### 3.5 Inverse theorem and boundary

The endpoint vector satisfies

`pi_i/pi_j=ell_j/ell_i`.

It therefore recovers the unique primitive positive integer vector
`d=(d_i)` and leaves precisely the common dilation ambiguity
`ell_i=c d_i`.  The mean resolves that ambiguity because

`c^2=(E T)(sum_i 1/d_i)/(sum_i d_i)`.

Thus `(endpoint law, mean)` uniquely identifies the ordered arm-length vector.
Endpoint probabilities alone identify it if and only if a scale such as total
length is separately known; otherwise common positive-integer dilation is the
exact nonidentifiability class.

## 4. R11 direct-owner classification

| tier | primary source | owned content | subtraction consequence |
|---|---|---|---|
| **DIRECT general tree background** | Lynn Hauser Pearce, [*Random walks on trees*](https://doi.org/10.1016/0012-365X(80)90234-4), *Discrete Mathematics* 30 (1980), 269--276 | random walk on a finite tree with leaves absorbing; expressions for absorption at a leaf and expected walk length | the bare carrier, endpoint harmonic measure, and mean receive zero credit |
| **SAME CARRIER CLASS / nearest framework** | de la Iglesia--Juarez, [*Birth-death chains on a spider: spectral analysis and reflecting-absorbing factorization*](https://arxiv.org/abs/2111.10450) | discrete half-line spiders as quasi-birth-death chains; matrix-valued spectral transition formulae; constant-probability random-walk example | spider terminology, generic spectral analysis, and birth-death reduction receive zero credit; the paper's arms are half-lines rather than unequal finite absorbing arms |
| **GENERAL method** | classical gambler's ruin and absorbing Markov-chain resolvents | path hitting probabilities/transforms and rationality of a finite first-passage PGF | all one-arm identities and generic rationality receive zero credit |
| **NEAREST inverse first-passage result** | de la Peña--Gzyl--McDonald, [*Inverse problems for random walks on trees: network tomography*](https://arxiv.org/abs/math/0610821) | on a **known** finite tree augmented by two boundary layers, the complete joint first-hitting-time/place laws at the two layers recover unknown internal transition probabilities | materially adjacent inverse genre, but not the same data or unknown: R11 fixes the simple-walk kernel, treats integer arm lengths as unknown, and uses only the endpoint vector plus one scalar mean; generic recovery rhetoric receives zero credit |

The phrase “reflecting-absorbing factorization” in de la Iglesia--Juarez names
a stochastic UL matrix factorization and Darboux transformation.  It is not a
claim about finite absorbing leaves and is not treated as a direct hit.

The network-tomography theorem is also not a direct hit.  Its topology is
given, its parameters are transition probabilities, and its observation is
the full time/place law at **two** detector layers.  R11 instead asks for an
unknown integer spider geometry under the fixed simple-random-walk kernel and
uses the much coarser pair `(leaf law, E T)`.  This distinction is essential:
the broad statement “hitting data identify a tree-chain parameter” is owned and
receives zero credit; only the explicit coarse-data arm-length reconstruction
survives the subtraction.

### Zero-credit background

- simple random walk and absorbing Markov chains;
- gambler's ruin on one path;
- Chebyshev/continuant solutions of a second-order recurrence;
- electrical/harmonic interpretation of leaf exit probabilities;
- Pearce's general-tree absorption probability and expected-length results;
- de la Peña--Gzyl--McDonald's known-topology/two-layer inverse framework;
- convexity/majorization of reciprocal sums as a proof tool.

### Surviving claim conjunction

Subject to independent replication of this bounded audit, the residual is the
conjunction of:

1. the explicit **leaf-marked all-time** finite unequal-arm rational transform
   `F_i(z)`, including parity and first atoms;
2. the compact arbitrary-profile variance formula;
3. the sharp fixed-`(r,L)` mean interval with both exact equality classes;
4. the endpoint-only dilation boundary and endpoint-plus-mean exact arm
   recovery.

No single bare item should be marketed as the advance.  In particular, the
endpoint law and mean are already within Pearce's general scope and may appear
only as zero-credit inputs needed for the inverse and extremal statements.

### R11 decision

`PASS_OWNER_THIN / HOLD_EXTERNAL`.

This is strong enough for the cross-lane theorem-value gate because the full
marked time law, variance, sharp extremizers, and inverse form distinct axes.
It is not yet frozen: a second, independent replication should inspect finite
phase-type distributions on star/spider trees and coarse-data inverse
first-passage identification before assignment to any paper.

## 5. R12 and R13 kill certificates

### R12

The verifier proves that uniform-inversion swapping has clock support

`[n-cycles(pi), inv(pi)]`

at both endpoints: the minimum is the transposition distance and the maximum
is attained by adjacent inversion swaps.  For the minimum, a nonidentity cycle
must contain an inverted pair of positions; swapping their images splits that
cycle, so repeating uses exactly `n-cycles(pi)` swaps.  This does not survive
subtraction.
Fleischer's [*Fun-Sort—or the chaos of unordered binary
search*](https://doi.org/10.1016/j.dam.2004.01.003) explicitly samples two
cells and swaps their contents when out of order; conditioning on effective
swaps gives R12.  Generic comparator sorting is also a permanent internal
firewall.  **Permanent kill.**

### R13

R13 is the Johnson-graph walk / Bernoulli--Laplace diffusion model.  The
verified eigenvalues

`1-j(n-j+1)/[k(n-k)]`

and multiplicities `C(n,j)-C(n,j-1)` are classical.  The primary modern paper
[*Cutoff for the Bernoulli--Laplace urn model with o(n)
swaps*](https://doi.org/10.1214/20-AIHP1052) explicitly recalls that the
eigenvalues and eigenvectors are known.  The matroid-basis and generic
association-scheme spectral firewalls independently exclude it.  **Permanent
kill.**

## 6. Search protocol and bounded-non-hit limitation

### Databases and source classes queried

- arXiv title/abstract and full-text records;
- Project Euclid and Cambridge Core journal records;
- Elsevier/ScienceDirect and Springer primary article pages;
- DOI/Crossref-style exact title searches;
- author/institutional records only when used to locate a primary paper.

Only publisher, journal, arXiv, or author/institution-hosted primary records
support classifications above.  ResearchGate snippets and tertiary summaries
were not used as evidence.

### Representative query families

```text
"random annihilation process" graph edge endpoint deleted
"random sequential annihilation" graph vertices edge
annihilation process line graph complete graph complete bipartite
choose an edge uniformly delete one endpoint independent set

random walk spider graph absorption time generating function arm lengths
finite spider random walk absorbing leaves hitting time
generalized star random walk hitting time leaves
spider first passage Chebyshev generating function
finite tree absorbing leaves harmonic measure expected length
inverse first passage spider arm lengths
"inverse problems for random walks on trees" hitting place time
network tomography random walk tree boundary hitting distribution

choose an inversion uniformly swap permutation random sorting
Bernoulli Laplace diffusion Johnson graph eigenvalues
```

The S08 search produced a direct hit and therefore a permanent kill.  The R11
search produced a direct general-tree owner for endpoint probability and mean,
a same-carrier infinite-spider framework, and a finite-tree inverse theorem
using known topology plus two complete detector-layer laws.  No source found
in the bounded search prints the surviving **coarse-data, unknown-arm**
finite-spider conjunction.  This is a bounded non-hit, not a novelty or
priority certificate.  Search-engine coverage, terminology drift, books not
fully indexed, and results embedded in broader phase-type or inverse
Markov-chain papers remain real risks.

## 7. Second-pool owner subtraction

| ID | strongest exact signal | decisive subtraction | decision |
|---|---|---|---|
| R14 | two-point clock bracketing `log_2 n`, exact mean/variance and within-family inverse | binary digit contraction is the whole proof; no independent endpoint/history axis after the P100/P101 firewall | **KILL INTERNAL** |
| R15 | strict arithmetic descent and exact rational clock | `p` and `2p` have identical full clock laws for every odd prime `p` | **KILL VALUE** |
| R16 | scalar maximum-multiplicity projection and `E T=4-4/2^m` | every factor profile with the same maximum multiplicity has the same clock | **KILL VALUE** |
| R17 | `E[y^L]=2^(-n)((1+y)^n-1+y^2)` on closed positive two-braids | Kauffman, [*State models and the Jones polynomial*](https://doi.org/10.1016/0040-9383(87)90009-7), directly owns the smoothing state model | **KILL DIRECT** |

The R17 search used the official Elsevier/ScienceDirect record and DOI for
Kauffman's primary 1987 article.  R14--R16 were killed by internal/value
certificates before a bounded external non-hit could carry any weight.

## 8. Reproducibility receipt

The exact checker is

`docs/papers147_151_sequence/scouting/stochastic/verify_stochastic_scout.py`.

Its canonical cold run executes **1,269,363 exact integer/rational assertions**,
including **65,528** charged to R11, **11,272** to the upgraded/killed S08,
**76,741** to R12, **450** to R13, and **528,971** to the four-system second
pool.  The frozen transcript is
`docs/papers147_151_sequence/scouting/stochastic/CANONICAL.txt`.

No paper was written and no Git operation was performed.
