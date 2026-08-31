# Hostile owner gate: open-boundary directed `k`-mer transport

**Audit date:** 2026-08-31 UTC  
**Object under attack:** scouting candidate `R02`, with no paper number  
**Gate type:** fresh primary-source owner review, theorem audit, and P1--P131
collision firewall  
**Overall decision:** **`KILL_CURRENT_STANDALONE_CONTRACT`**  
**Permitted fallback:** **`RESERVE_INTERNAL_LEMMA_ONLY`**  
**External status:** **`HOLD / NO NOVELTY OR PRIORITY CLAIM`**

## 1. Executive verdict

The displayed formulas are correct.  They do not support a new short paper.
After the closest sources are read at proof level, `R02` is exactly a
directed sorting process inside an already owned reconstituting-dimer/
`k`-mer sector:

1. Menon--Barma--Dhar already study the dimer rule on a finite line with
   fixed ends, identify the irreducible-string sectors, push every dimer to
   one end to obtain a standard sector representative, encode the sector as
   exclusion particles and fixed-order holes, and give the free-boundary
   sector size as a binomial coefficient.
2. Barma--Grynberg--Stinchcombe study the literal directed rule
   `110 -> 011`, write it as `AB -> BA` and `AC -> CA`, identify `A` as an
   ASEP particle, and state that the sector-wise ASEP mapping persists for
   `k`-mers with more hole types.
3. In those coordinates, the proposed open absorbing orientation merely
   moves every `A` past every hole.  Its depth is the binary inversion
   statistic and its fibre polynomial is the classical Gaussian binomial.
4. Generic order-independent execution and odometers are established
   abelian-network background.  Here they also follow from a one-line
   directed-path token encoding, so no delicate abelian theorem is needed.
5. Internally, P111 has already isolated the same fixed-content binary
   inversion/Gaussian-polynomial engine and explicitly assigned it zero
   novelty credit.

Thus the only literal remainder is a convenient translation of the known
sector sorting into raw binary gap coordinates, including an inert right
boundary fragment.  That is useful as an internal lemma and regression
fixture, but it is not theorem-scale novelty.  A bounded search not finding
the exact eight-line formula verbatim does not alter this conclusion.

### Trivalent gate

| question | decision | reason |
|---|---|---|
| Are the projection, odometer, fibre and polynomial formulas correct? | **PASS** | direct proof below; fresh exact replay also passes |
| May the raw gap formula be retained for later use? | **RESERVE** | concise coordinate lemma and exact-control fixture only |
| Does the present package earn a paper slot or an external novelty claim? | **KILL** | direct dimer owners plus immediate ASEP/inversion reduction consume the contribution |

The residual-novelty score is **1/10** after subtraction.  This score
measures standalone contribution value, not mathematical correctness.

## 2. The contract under review

Fix `k>=2` and orient the finite-word rewrite

$$
1^k0\longrightarrow 01^k.                                      \tag{2.1}
$$

For a word with `z` zeros, use gaps

$$
w=1^{g_0}0\,1^{g_1}0\cdots 0\,1^{g_z},\qquad g_i\geq0.          \tag{2.2}
$$

For `i<z`, put

$$
b_i=\left\lfloor\frac{g_i}{k}\right\rfloor,
\qquad r_i=g_i\bmod k,
\qquad c_i=\sum_{j=0}^{i}b_j.                                  \tag{2.3}
$$

The proposed terminal and depth are

$$
\operatorname{gaps}(Q_k(w))=
\left(r_0,\ldots,r_{z-1},
g_z+k\sum_{i=0}^{z-1}b_i\right),                               \tag{2.4}
$$

$$
D_k(w)=\sum_{i=0}^{z-1}c_i
=\sum_{i=0}^{z-1}(z-i)b_i.                                     \tag{2.5}
$$

For an absorbing target

$$
t=(r_0,\ldots,r_{z-1},\beta),\qquad 0\leq r_i<k,
\qquad B=\left\lfloor\frac{\beta}{k}\right\rfloor,            \tag{2.6}
$$

the proposed every-target formulas are

$$
|Q_k^{-1}(t)|=\binom{B+z}{z},                                  \tag{2.7}
$$

$$
\sum_{Q_k(w)=t}q^{D_k(w)}=
\begin{bmatrix}B+z\\z\end{bmatrix}_q.                         \tag{2.8}
$$

The audit separates two questions which the scouting record had not yet
separated sharply enough:

- Are (2.4)--(2.8) true? **Yes.**
- Do they remain a paper contribution after owner reduction? **No.**

## 3. Exact reduction to owned sector sorting

The shortest proof is also the fatal novelty reduction.  Define

$$
A=1^k,\qquad H_r=1^r0\quad(0\leq r<k).                          \tag{3.1}
$$

Also write `g_z=kb_z+r_z`, with `0<=r_z<k`.  The word has the unique
factorization

$$
w=A^{b_0}H_{r_0}A^{b_1}H_{r_1}\cdots
A^{b_{z-1}}H_{r_{z-1}}A^{b_z}1^{r_z}.                          \tag{3.2}
$$

The literal rewrite (2.1) is precisely

$$
AH_r\longrightarrow H_rA.                                     \tag{3.3}
$$

The ordered hole word
`H_(r_0) H_(r_1) ... H_(r_(z-1))` and the right boundary fragment
`1^(r_z)` never change.  Only indistinguishable `A` particles move, one
place to the right through a hole.  This is the sector-wise totally
asymmetric exclusion sorting already exposed by the direct dimer owners.

Let

$$
B_{\rm tot}=\sum_{i=0}^{z}b_i.
$$

Every legal complete execution ends at

$$
H_{r_0}H_{r_1}\cdots H_{r_{z-1}}A^{B_{\rm tot}}1^{r_z},        \tag{3.4}
$$

which is (2.4).  Hole `i` is crossed by exactly the `A` particles initially
in bins `0,...,i`; hence its firing count is

$$
c_i=b_0+\cdots+b_i.                                             \tag{3.5}
$$

Summing (3.5) gives (2.5).  This is not a new confluence mechanism: it is
flow conservation on a directed path.  Equivalently, if `A` is declared
larger than a hole, every move removes exactly one compressed inversion.
In raw binary coordinates it removes exactly `k` one-before-zero pairs, so

$$
D_k(w)=\frac{\operatorname{Inv}(w)-
\operatorname{Inv}(Q_k(w))}{k}.                                \tag{3.6}
$$

For a fixed target, set `b_z=B-sum_(i<z)b_i`.  Its sources are exactly the
weak compositions

$$
b_0+\cdots+b_z=B.                                               \tag{3.7}
$$

This gives (2.7).  It also shows why “every target” is not extra geometry:
the fibre ignores the residue vector and depends only on `(B,z)`.

Finally, (2.5) is the inversion number of the compressed word with `B`
copies of `A` and `z` holes.  Therefore

$$
\sum_{b_0+\cdots+b_z=B}
q^{\sum_{i=0}^{z-1}(z-i)b_i}
=\begin{bmatrix}B+z\\B\end{bmatrix}_q
=\begin{bmatrix}B+z\\z\end{bmatrix}_q.                       \tag{3.8}
$$

The supposed all-`k` strength disappears under (3.2): `k` changes only the
raw-word block code and the hole labels.  The compressed dynamics, odometer,
fibre count, and depth polynomial contain no `k`.

## 4. Gaussian convention audit

There is no reciprocal or orientation error in (2.8), but there is also no
new enumerator.

- A source with all `A` particles already at the right has depth zero, so
  the constant coefficient is one.
- A source with all `A` particles before all holes has depth `Bz`, so the
  degree is `Bz` and the leading coefficient is one.
- The standard recurrence, taking `B` to be the number of `A` particles, is

  $$
  F(B,z)=F(B,z-1)+q^zF(B-1,z),                                  \tag{4.1}
  $$

  with `F(0,z)=F(B,0)=1`.  Thus
  `F(B,z)=[B+z choose B]_q` in the usual inversion convention.
- At `q=1`, (3.8) gives `binom(B+z,z)`.
- The cases `z=0` and `B=0` both give the singleton fibre and polynomial
  `1`.

Richard Stanley's official text, *Enumerative Combinatorics*, volume 1,
Proposition 1.7.1, gives
`sum_w q^(inv(w))` over multiset permutations as the Gaussian
multinomial and records the recurrence used above
([official PDF](https://math.mit.edu/~rstan/ec/ec1.pdf)).  Svante Janson
uses the same random-word inversion, lattice-path and Ferrers-diagram
correspondence
([arXiv:1203.6480](https://arxiv.org/abs/1203.6480),
[DOI 10.37236/2188](https://doi.org/10.37236/2188)).

Reversing the direction would replace the exponent by `Bz-D`; Gaussian
polynomials are palindromic, so the polynomial happens to agree after
`q^(Bz)F(q^(-1))=F(q)`.  The present orientation nevertheless matches the
standard inversion convention directly, without using palindromicity.

## 5. Primary-owner gate

### 5.1 Menon--Barma--Dhar: the open-line standard form and fibre count

G. I. Menon, M. Barma and D. Dhar,
[*Conservation Laws and Integrability of a One-dimensional Model of
Diffusing Dimers*](https://arxiv.org/abs/cond-mat/9703059),
*Journal of Statistical Physics* **86** (1997), 1237--1266,
[DOI 10.1007/BF02183622](https://doi.org/10.1007/BF02183622), is a direct
owner, not merely related work.

The primary text does all of the following:

- defines the binary line dynamics `011 <-> 110` and specifies fixed-end
  boundary conditions;
- proves deletion-order independence of the irreducible string;
- states that any dimer can be pushed to the right, producing a standard
  configuration consisting of the irreducible string and the dimers at the
  end;
- gives the unique `A=11`, `B=10`, `C=0` exclusion representation, with
  `A` exchanging with `B` or `C` while the `B/C` order is fixed;
- discusses the unpaired right-boundary `1`; and
- for free boundaries, gives the number of states in a fixed sector as

  $$
  \Omega_{\rm free}(N_A,N_B,N_C)
  =\frac{(N_A+N_B+N_C)!}{N_A!(N_B+N_C)!}.                       \tag{5.1}
  $$

For `k=2`, (5.1) is exactly (2.7), with `N_A=B` and
`N_B+N_C=z`, modulo the inert right-boundary fragment already noted by the
owner.  The paper's push-to-the-right standard configuration is the terminal
selected by the oriented process.  Consequently the “open-line terminal”
and the unrefined target fibre are directly consumed for dimers.

### 5.2 Barma--Grynberg--Stinchcombe: the directed rule and all-`k` sector map

M. Barma, M. D. Grynberg and R. B. Stinchcombe,
[*Directed diffusion of reconstituting dimers*](https://arxiv.org/abs/cond-mat/0609041),
*Journal of Physics: Condensed Matter* **19** (2007), 065112,
[DOI 10.1088/0953-8984/19/6/065112](https://doi.org/10.1088/0953-8984/19/6/065112),
is the fatal directed owner
([author-repository PDF](https://repository.ias.ac.in/1510/1/356.pdf)).

The paper explicitly gives the ring update `110 -> 011`, the
`A=11,B=10,C=0` code, the exchanges `AB -> BA` and `AC -> CA`, conservation
of the ordered `B/C` irreducible string, and the ASEP interpretation with
`A` as particle and `B/C` as vacancies.  Its concluding discussion says
that for reconstituting `k`-mers the sector-wise ASEP mapping still holds and
the number of hole types grows with `k`.

The paper discusses boundary injection/ejection as a different, genuinely
boundary-driven problem.  That does not print the present no-injection
absorbing formula verbatim.  It also does not rescue `R02`: combining its
directed exchange with the 1997 fixed-end standard form leaves only finite
ASEP sorting.  Formula (3.2) makes this implication explicit for every
`k`.

### 5.3 Abelian-network background

B. Bond and L. Levine,
[*Abelian Networks I. Foundations and Examples*](https://arxiv.org/abs/1309.3445),
*SIAM Journal on Discrete Mathematics* **30** (2016),
[DOI 10.1137/15M1030984](https://doi.org/10.1137/15M1030984), prove least
action and execution-order independence, define the odometer, and show that
complete legal executions have the same odometer and final state.

One should not cite that framework carelessly: the paper notes that ordinary
adjacent sorting with shared vertex state lies outside its formal processor
definition.  Here a valid directed-path encoding is immediate.  Bin `i`
contains `b_i` unary `A` messages; processor `i<z` passes every message to
`i+1`; node `z` is the sink.  Processor `i` handles exactly
`b_0+...+b_i=c_i` messages.  Thus generic abelian language is zero credit,
while (3.5) remains elementary even without invoking the general theorem.

## 6. Search protocol and bounded non-hits

The hostile refresh used exact-rule, boundary, enumeration, and framework
queries rather than only topic words.  Representative query families were:

| query family | examples | result |
|---|---|---|
| literal rule | `"110" "011" reconstituting dimers`; `"110 -> 011" open boundary`; `"1110" "0111" k-mer diffusion` | direct Barma--Grynberg--Stinchcombe hit; Menon--Barma--Dhar line owner recovered through citation chaining |
| open/fixed boundary | `reconstituting dimers absorbing state open chain`; `directed diffusion reconstituting dimers free boundary`; `k-mer absorbing open line` | the 1997 source already contains fixed/free-boundary standard-form and sector-size material; no separate exact absorbing-atlas paper found |
| all-`k` sector | `reconstituting k-mers irreducible string ASEP`; `sector-wise mapping ASEP k-mers` | the 2007 primary paper explicitly states persistence of the sector-wise ASEP map |
| fibre and depth | `reconstituting dimers q-binomial`; `110 to 011 Gaussian polynomial`; `irreducible string inversion polynomial` | no literal dimer paper printing (2.8) found; classical word-inversion sources give it immediately |
| abelian/odometer | `directed path odometer abelian network`; `legal execution order independent odometer` | Bond--Levine direct framework hit |
| current horizon | 2025--2026 variants of the literal-rule, open-boundary and `q`-fibre queries | no new direct hit; mostly unrelated genomic `k`-mer results and adjacent physical models |

Adjacent reconstituting-`k`-mer papers include Daga--Mohanty's
[*Phase separation transition of reconstituting k-mers in one dimension*](https://arxiv.org/abs/1412.8643)
and Chatterjee--Daga--Mohanty's
[*Phase coexistence and spatial correlations in reconstituting k-mer
models*](https://arxiv.org/abs/1605.03859).  Their literal stochastic rules
are different, so they are context, not the decision-bearing owners.

These searches are bounded and not a priority certificate.  More
importantly, the gate does not rely on a non-hit: the positive owner
reduction is already decisive.

## 7. Exact zero-credit contract

No future draft may claim contribution credit for any of the following:

1. the dimer update `110 -> 011` or the name directed diffusion of
   reconstituting dimers;
2. the natural `1^k0 -> 01^k` block extension or the physical `k`-mer
   vocabulary;
3. finite line, fixed/free/open boundary as a carrier distinction by itself;
4. irreducible strings, residue/hole-type sectors, or preservation of the
   ordered hole word;
5. the `A/H_r` exclusion encoding or sector-wise ASEP reduction;
6. pushing all blocks to the right, the resulting standard/absorbing state,
   or uniqueness of that terminal;
7. generic confluence, scheduler independence, least action, or odometer
   language;
8. the `k=2` binomial sector/target-fibre size, and the all-`k` version that
   follows by the same ASEP placement count;
9. inversion as the number of adjacent directed swaps;
10. Gaussian-binomial enumeration of fixed-content binary inversions,
    lattice paths, or rectangle partitions;
11. the phrase “every target” when the answer discards the target residue
    vector and depends only on `(B,z)`; or
12. the exhaustive finite computation as evidence of novelty or priority.

The conjunction of owned statements is also zero credit.  Packaging the
standard terminal, path odometer, binomial fibre and Gaussian rank
enumerator in one theorem does not restore novelty when all four are the
same binary exclusion sorting reduction.

## 8. Exact residual contract

After subtraction, the only defensible retained object is the following
internal lemma:

> For a raw binary open word and fixed `k`, factor it as in (3.2).  The
> directed update swaps `A` through the fixed ordered hole types.  Therefore
> the terminal gaps are (2.4), the labelled-hole odometer is (3.5), and the
> inert right boundary fragment is `1^(r_z)`.

This lemma has three acceptable uses:

- a coordinate dictionary between raw gaps and the known exclusion-sector
  code;
- a verification fixture for later, genuinely different systems; and
- a preliminary lemma inside a paper whose main theorem is not reducible to
  fixed-sector adjacent sorting.

It may not be presented as a standalone research result.  The fibre and
`q`-polynomial can be stated only as classical corollaries with the direct
owners and inversion enumerator credited.

### Re-entry threshold

Re-entry requires a second theorem whose state or observable does not
collapse to “place `B` identical particles among `z` ordered holes.”  Merely
adding a random legal scheduler, a reversed orientation, a history count,
or another `q` variable is insufficient.  In particular, legal-history
counts immediately enter classical reduced-word/Young-tableau territory and
would need a new owner audit.

Plausible but unapproved new lanes include boundary injection/ejection that
changes sectors, heterogeneous block interactions that destroy the fixed
hole order, or transport on a non-path network with genuinely target-sensitive
fibres.  Each is a new system and needs a new breadth and owner gate; none is
authorized by this reserve.

## 9. P1--P131 collision firewall

The historical collision maps and frozen paper summaries were rescanned
through P131.  No earlier numbered paper uses the literal dimer update, but
literal nonidentity is not enough: the proposed residual is already occupied
at the level of its observable and proof engine.

| portfolio range | nearest occupied material | hostile conclusion for `R02` |
|---|---|---|
| P1--P43 | arithmetic/Fredholm clocks, affine and modular actions, holonomy and certificate systems | no literal collision; no positive novelty evidence |
| P44--P61 | `q`-adic/fibre retractions, tree/Toeplitz shifts, routing and local split systems | generic fibre and local-code language is occupied; no decisive literal collision |
| P62--P81 | P63 XOR inverse windows; P78 abelian-sandpile translations | P63 is a different linear symbolic factor; P78 reinforces that generic abelian vocabulary is unavailable |
| P82--P96 | P82 shifted Fredkin; P90 particle-resolved Rule 184; P93 push--pop cocycles | conservative binary CA/traffic and scheduler/cocycle language are occupied, although the updates differ |
| P97--P106 | P100 digit-erasure absorption/depth polynomial; other finite-map image/fibre systems | the absorption-plus-depth-polynomial silhouette is not a separator |
| P107--P111 | **P111 positive Heisenberg word-area cocycle** | decisive internal mechanism collision: P111 already uses the fixed-content binary inversion Gaussian polynomial and explicitly marks it owned background |
| P112--P116 | P114 rooted-forest leaf peeling | terminal/clock/fibre packaging is occupied but the carrier differs |
| P117--P121 | P117 odd-run reversal; P121 adjacent product-plus-one coalescence | run/coalescence systems differ; the killed Stage-1 one-defect abelian queue is a particularly relevant warning that a generic odometer plus classical path count is not paper-scale |
| P122--P126 | P126 balanced composition refinement | pointwise fibre and composition-coordinate packaging is occupied; changing from a word to its gap composition creates no slot |
| P127--P131 | P129 rootward pile coalescence; P131 Euclidean quotient queues | directed transport/queue vocabulary and complete pointwise-fibre packages are occupied, although their literal updates differ |

The most important correction to the provisional P132--P136 firewall is the
missing P111 row.  Calling (2.8) a “Gaussian target-depth fibre” does not
separate `R02`; it identifies its exact collision with already
owner-subtracted binary inversion enumeration.  The current hostile verdict
therefore supersedes any earlier provisional `PROMOTE_INTERNAL_OWNER_HOLD`
label for `R02`, without modifying the immutable scouting record.

## 10. Exact-control replay

The existing verifier was run afresh without editing it:

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_stochastic_scout.py | sha256sum
476231ee481cd9e1be6abfa14832b854404ec0a706a7621873975939d29bc02f  -
```

This equals the SHA-256 of the frozen `CANONICAL.txt`.  The `R02` lane checks
all binary words for `k=2` through length 16 and for `k=3,4` through length
13: **163,834 inputs and 976,143 exact assertions**.  It independently
enumerates every legal successor DAG, checks a singleton terminal and one
path length, verifies the raw inversion drop, aggregates every terminal
fibre, and compares the depth histogram with a Gaussian recurrence.  The
full 27-system run ends `STATUS=PASS`.

This is strong falsification evidence for correctness and useful evidence
against a hidden orientation error.  It contributes zero evidence to
novelty, value, or priority.

## 11. Final disposition

**`PASS_CORRECTNESS / RESERVE_COORDINATE_LEMMA / KILL_PAPER_CONTRACT`.**

Do not assign a paper number, draft a standalone manuscript, or describe the
system, open terminal, odometer, binomial fibre, or Gaussian depth polynomial
as new.  Keep the exact formulas and verifier as an internal owner-subtracted
lemma.  Reopen only after a genuinely non-ASEP-sorting theorem survives a
fresh owner and P1--P131 collision gate.
