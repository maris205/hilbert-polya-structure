# Fresh57 — shortest-period prefix truncation

2026-09-11 UTC. Author: current_round_independent_scout.
**ONE_DEFINED_LITERAL / AUTHOR_NEGATIVE / ZERO_NOMINATIONS / NO_PILOT**.

The current batch top (`d7f8a2`) and the complete fresh55 root admission
(`053d14`) were read. P214's ideal-ring recurrence is excluded. This desk
only addresses the last open seat and does not allocate it. No scientific
execution, code, central-index change, Git operation or external write was
performed. Only this new desk was created.

## 1. Literal and relevant old boundaries

Fix an alphabet of size $q\ge1$ and a bound $B\ge0$. The carrier is all
words of length at most $B$, including $\epsilon$. For a nonempty word $w$,
let $p(w)$ be its least positive ordinary period: $w_i=w_{i+p}$ whenever
both indices occur. Divisibility of the length by $p$ is not required.
Define
$$T(w)=w_1\cdots w_{p(w)},\qquad T(\epsilon)=\epsilon.$$
Thus this map keeps the shortest generating prefix, not the longest border
and not the primitive root under integral powers.

The old C6 failure-link rule sends a word to its longest proper border;
the actual C6 explanation was read in
`docs/papers112_116_sequence/scouting/COMBINATORIAL_SCOUT.md`, lines
520–550 (`c6532e`). The newer `word_automata_residual04` rule sends each
coordinate to the shortest period of its prefix minus one on the fixed
inversion-sequence carrier. Its actual definition and old P134 output
adapter were read in `PROOF_AND_DISPOSITION.md`, lines 1–84 (`911eef`).
Neither is this variable-length prefix map. No conjugacy/factor clearance
against every old map is claimed from that distinction or search non-hits.

## 2. Claims, assumptions and proof plan

Status: **PROVABLE AS STATED** for the following elementary all-parameter
results. They are author deductions, not independently reviewed theorems.

1. Recurrent words are exactly the unbordered nonempty words and $\epsilon$;
   all are fixed. The maximum entrance time is explicitly evaluated below.
2. Every target fibre is evaluated by a finite cyclic mismatch threshold.
   The maximum fibre and all maximizing targets are determined.

The temporal proof uses strict length decrease and a matching one-letter
deletion chain. The inverse proof uses forced periodic extension and the
first mismatch against each shorter period. These are the complete proof
dependencies; no empirical pattern, unproved periodicity lemma or
Fine–Wilf theorem is required.

## 3. Temporal proof and sharp maximum

A word of length $m$ has a period $d<m$ exactly when its prefix and suffix
of length $m-d$ agree. Thus $T$ fixes exactly unbordered nonempty words.
Every other update strictly shortens the word, so no nontrivial cycle is
possible. The empty word is fixed separately.

A nonconstant word cannot map to a constant word: a constant length-$p$
prefix together with period $p$ would force the whole source constant.
Consequently every orbit from a nonconstant word of length $m$ stays at
length at least two and has entrance time at most $m-2$.

For distinct letters $a,b$ and $m\ge3$, put $w_m=ab a^{m-2}$.
Its least period is $m-1$. This is a period because the sole required
comparison is the initial and final $a$. Period 1 fails at positions 1,2;
for $2\le d\le m-2$, the comparison of positions 2 and $2+d$ is $b$ versus
$a$, so $d$ fails. Hence $T(w_m)=w_{m-1}$ and the chain ends at the fixed
word $ab$. Its entrance time is exactly $m-2$.

Constant words of length at least two map to their one-letter word in one
step. Therefore the global maximum $H(q,B)$ is
$$
H(q,B)=
\begin{cases}
0,&B\le1,\\
1,&q=1, B\ge2,\\
\max(1,B-2),&q\ge2, B\ge2.
\end{cases}
$$
This is a sharp all-parameter result, but its mechanism is exactly unit
length descent plus an explicit chain attaining that elementary bound.

## 4. Every-target inverse and sharp extremum

Let $u$ be a nonempty target of length $p\le B$, and write $U=u^\infty$
for its infinite periodic extension, with indices starting at one.
For each $1\le d<p$ define
$$r_d=\min\{j\in\{1,\ldots,p\}:U_j\ne U_{j+d}\},$$
with $r_d=\infty$ if the set is empty. Define
$$\mu(u)=\max\bigl(\{p\}\cup\{d+r_d:1\le d<p\}\bigr),$$
allowing $\mu=\infty$. When $p=1$ the second set is empty and $\mu=1$.
This requires only cyclic comparisons among the $p$ letters of the given
target; it is not a search through all source words.

**Forced source.** If $T(w)=u$, then $|w|=m\ge p$, the source begins with
$u$ and has period $p$. Its letters are therefore uniquely forced:
$w=U_1\cdots U_m$. Conversely this word maps to $u$ exactly when its least
period is $p$.

**Threshold.** For fixed $d<p$, the comparison sequence
$(U_j,U_{j+d})$ is $p$-periodic in $j$. If all its first $p$ comparisons
agree, $d$ is a period of every finite prefix and $p$ can never be least.
Otherwise the first mismatch is exactly at $r_d$. The length-$m$ prefix
has period $d$ exactly when $m-d<r_d$, or $m<d+r_d$.
It fails every period below $p$ exactly when $m\ge\mu(u)$.

Thus the fully evaluated fibre is
$$
|T^{-1}(u)|=
\begin{cases}
\max(0,B-\mu(u)+1),&\mu(u)<\infty,\\
0,&\mu(u)=\infty.
\end{cases}
$$
The preimages themselves are precisely one forced extension for each
integer length $\mu(u)\le m\le B$. Also $T^{-1}(\epsilon)=\{\epsilon\}$.
For example, $u=aba$ has $r_1=1,r_2=2$ and $\mu=4$; it has one preimage
of each length 4 through $B$, despite not being unbordered. Thus the map
is not an idempotent primitive-root projection.

For $B\ge2$, every one-letter target has fibre $B$. Every target of length
$p\ge2$ has fibre at most $B-p+1<B$, and the empty target has fibre 1.
Hence the maximum is exactly $B$, attained **only** by the $q$ one-letter
targets. For $B=0,1$ the map is the identity, every fibre is 1, and every
target maximizes it. Noninjectivity for $B\ge2$ follows already from
$T(a)=T(aa)=a$.

## 5. Source subtraction and author disposition

The external search found the authors' textbook *Text Algorithms*,
[Crochemore–Rytter manuscript](https://igm.univ-mlv.fr/~mac/REC/text-algorithms.pdf),
whose indexed Proposition 2.2 passage describes the border chain and
period/border duality. These are credited background, not an owner of
the entire displayed iterative theorem. A direct opening of the authors'
[border-table page](https://www-igm.univ-mlv.fr/~lecroq/ta2/border.php)
timed out. Source coverage is therefore indexed-passage level for this
textbook fact, not a full-paper read. The elementary proof above does not
depend on an uninspected external proof.

The exact prefix truncation was not located as an old literal in these
bounded searches, but that is not novelty or factor clearance. More
importantly, the complete temporal result is the basic strict-length
bound with the elementary $ab a^r$ witness. The inverse result is forced
extension plus direct shorter-period mismatch tests; its extremum comes
from constant words. After those ordinary word-period primitives are
deducted, this desk has not identified a materially separate research
advance. **Author recommendation: do not nominate.** Correct formulas
alone are not used to fill the remaining seat. No second rule is proposed.

The earlier broad tree/trie search was truncated and only navigation.
The period/border search (`5eb45c`) led to the specific original reads
above. Sage documentation lookups for `primitive_root` and `fractional`
returned no match; they are not evidence that such notions are absent.
No download, source execution, pilot, enumeration box, manuscript or
independent review was performed. The parent retains reception authority.
