# W01 proof spike: oriented ternary fusion

## Claim

Work on linear words over the alphabet $\mathbb Z/3\mathbb Z$.  The only
rewrite rules are

$$
01\longrightarrow2,\qquad
12\longrightarrow0,\qquad
20\longrightarrow1,
$$

or, uniformly, $i(i+1)\to i+2$ with all labels read modulo $3$.  A word is
terminal when it contains none of $01,12,20$.  Let

$$
W_k=(012)^k,\qquad k\geq0,
$$

and let $a_k$ be the number of distinct terminal words reachable from $W_k$.

The claims proved in this dossier are:

1. reachable terminals are in bijection with compositions of $3k$ into parts
   $1$ and $2$ having no two consecutive parts equal to $1$;
2. with $a_0=1,a_1=2,a_2=4$,

   $$
   a_k=3a_{k-1}-2a_{k-2}+a_{k-3}\qquad(k\geq3),
   $$

   and

   $$
   \sum_{k\geq0}a_kz^k
   =\frac{1-z}{1-3z+2z^2-z^3};
   $$

3. if $n=3k$ and a reachable terminal has length $\ell$, then the number of
   such terminals is

   $$
   \binom{n-\ell+1}{2\ell-n},
   \qquad
   \left\lceil\frac n2\right\rceil\leq\ell
   \leq\left\lfloor\frac{2n+1}{3}\right\rfloor;
   $$

4. a terminal encoded by a composition with $m$ parts equal to $2$ has
   exactly $m!$ occurrence-distinguished unweighted rewrite histories, and
   the total number $H_k$ of histories from $W_k$ is

   $$
   H_k=\sum_{m=k}^{\lfloor3k/2\rfloor}
       \binom{m+1}{3k-2m}m!.
   $$

Thus the conjectured grammar and recurrence survive unchanged, and the exact
history fibre and total-history formula supply the requested second output.

## Status

**PROVABLE AS STATED.**

**Internal disposition:** `PROVED / SEND TO OWNER-VALUE GATE`.

**External disposition:** `HOLD_EXTERNAL`.  This is a proof dossier, not a
paper assignment, novelty statement, priority claim, or release decision.

## Assumptions and conventions

- Words are linear, not cyclic.  There is no rewrite across the two endpoints.
- A redex occurrence is a position, so two positions leading to the same
  child word would count as two history choices.
- A history ends at its first terminal word.
- “Unweighted history” counts legal sequences of redex occurrences.  It is
  not the probability under uniform choice among currently active redexes.
- The empty word $W_0$ has one terminal, itself, and one empty history.
- Binomial coefficients outside $0\leq r\leq s$ are zero when formulas are
  read without the displayed range restrictions.

## Notation

- $P(s,n)=s(s+1)\cdots(s+n-1)$ is the length-$n$ periodic interval beginning
  at $s\in\mathbb Z/3\mathbb Z$.
- A composition $c=(c_1,\ldots,c_j)$ uses parts $c_i\in\{1,2\}$.
- A part $1$ represents an original singleton; a part $2$ represents a fused
  adjacent pair.
- $b_n$ denotes the number of compositions of $n$ into $1,2$ with no adjacent
  $1$ parts.  The desired sequence is $a_k=b_{3k}$.
- For a terminal of original length $n$, $r$ is the number of singleton
  parts, $m$ the number of dimer parts, and $\ell=r+m$ its final length.

## Proof strategy

The decisive step is not a fitted automaton.  A reduction forest shows that
every current letter represents a contiguous interval of the original
periodic word.  A last-fusion induction proves that no periodic interval of
length at least $3$ can collapse to one letter.  Therefore every history is
exactly the sequential construction of a matching of the original path.
Terminality is maximality of that matching, or equivalently absence of
adjacent singleton parts.

Two counting routes are then available:

1. a two-state regular grammar gives the bivariate rational generating
   function and the support recurrence;
2. maximal-matchings with $m$ edges are counted by choosing singleton gaps,
   while ordering their $m$ edges gives the exact $m!$ history fibre.

## Dependency map

1. The reachable-terminal grammar depends on the interval-ancestry lemma and
   the no-large-block lemma.
2. The bijection depends on an explicit four-case terminality calculation and
   a left-to-right inverse decoder.
3. The rational generating function depends only on the proved composition
   grammar.
4. The recurrence for $a_k$ is obtained by taking the $3$-section of the
   composition recurrence via a $3\times3$ transfer matrix.
5. The history fibre theorem depends on the stronger consequence that every
   legal fusion selects two still-unmatched original adjacent vertices.
6. The verifier is a falsification control only; none of the infinite claims
   depends on its finite bounds.

## Proof

### Lemma 1: interval ancestry

At every time in every history from $P(s,n)$, each current letter represents
a nonempty contiguous interval of original positions.  These intervals are
disjoint, occur in their original left-to-right order, and partition the
original word.

#### Proof

Initially each letter represents its singleton position.  A rewrite replaces
two adjacent current letters by one letter.  By induction their representing
intervals are adjacent contiguous intervals, so their union is one contiguous
interval.  All other intervals remain unchanged and in order.  This proves
the assertion after every rewrite. $\square$

### Lemma 2: no periodic block of length at least three collapses

For $s\in\mathbb Z/3\mathbb Z$, the possible one-letter reductions of
$P(s,n)$ are

$$
\{s\}\quad(n=1),\qquad
\{s+2\}\quad(n=2),\qquad
\varnothing\quad(n\geq3).
$$

#### Proof

The cases $n=1,2$ follow from the definition and the rule
$s(s+1)\to s+2$.

For $n=3$, a hypothetical last rewrite has a split of sizes $1+2$ or $2+1$.
In the first split, the two child labels are $s$ and $s$, so they do not form
a redex.  In the second split, the two child labels are both $s+2$, again not
a redex.  Hence $P(s,3)$ cannot collapse.

For $n=4$, the splits $1+3$ and $3+1$ are excluded by the preceding case.  In
the remaining split $2+2$, the left block reduces to $s+2$.  The right block
starts at $s+2$ and reduces to $(s+2)+2=s+1$.  The ordered pair
$(s+2,s+1)$ is not of the form $(i,i+1)$, so it cannot undergo the last
rewrite.

Now assume $n\geq5$ and that the statement holds for every length from $3$ to
$n-1$.  The root of a hypothetical complete reduction tree splits the word
into blocks of lengths $j$ and $n-j$, both of which must reduce to one letter.
At least one of $j,n-j$ lies between $3$ and $n-1$, contradicting the
induction hypothesis.  Strong induction finishes the proof. $\square$

### Lemma 3: exact reachable-terminal grammar

For a composition $c=(c_1,\ldots,c_j)$ of $n$ into parts $1,2$, scan
$P(0,n)$ from left to right.  If a part starts at position $p$ (positions begin
at $0$), define its output label by

$$
\tau(p,1)=p\pmod3,
\qquad
\tau(p,2)=p+2\pmod3.
$$

Then $\tau_n(c)$ is a reachable terminal if and only if $c$ has no adjacent
parts $1,1$.  Moreover, $c\mapsto\tau_n(c)$ is injective.

#### Proof

By Lemma 1, a terminal partitions the original word into the ancestry
intervals of its letters.  Lemma 2 forces every interval length to be $1$ or
$2$.  A singleton beginning at $p$ retains label $p$, while the pair beginning
there is $p,(p+1)$ and fuses to $p+2$.  Hence every reachable terminal has the
stated form.

Consider two consecutive parts, the first beginning at residue $s$.  Their
two output labels are:

| consecutive part sizes | output pair |
|---|---|
| $(1,1)$ | $(s,s+1)$ |
| $(1,2)$ | $(s,s)$ |
| $(2,1)$ | $(s+2,s+2)$ |
| $(2,2)$ | $(s+2,s+1)$ |

Only the first row is a redex.  Thus the output is terminal exactly when the
composition avoids adjacent $1$ parts.

Conversely, take such a composition.  Fuse each of its disjoint $2$-blocks,
in any order, and leave its $1$-blocks unchanged.  Each $2$-block is an
original pair $i(i+1)$ and is therefore a legal redex.  After all these
fusions the displayed table and the no-$11$ condition show that the resulting
word is terminal.  Hence every word described by the grammar is reachable.

It remains to prove that two compositions cannot encode the same terminal.
Suppose the scan has reached original position $p$.  The next terminal symbol
equals either $p$ if the next part has size $1$, or $p+2$ if it has size $2$.
These are distinct residues modulo $3$, so the next part is uniquely recovered
from the terminal symbol.  Advancing by that recovered part and repeating
decodes the whole composition.  The map is injective. $\square$

### Theorem 4: support counts, refined grammar, recurrence, and rational GF

Let $c_{n,m}$ be the number of reachable terminals from $P(0,n)$ whose
composition contains $m$ parts equal to $2$.  Then

$$
c_{n,m}=\binom{m+1}{n-2m},
$$

and the bivariate generating function is

$$
C(x,u)=\sum_{n,m\geq0}c_{n,m}u^m x^n
=\frac{1+x}{1-ux^2-ux^3}.
$$

For $n=3k$, the support count satisfies

$$
a_0=1,\quad a_1=2,\quad a_2=4,\qquad
a_k=3a_{k-1}-2a_{k-2}+a_{k-3}\quad(k\geq3),
$$

and

$$
A(z)=\sum_{k\geq0}a_kz^k
=\frac{1-z}{1-3z+2z^2-z^3}.
$$

#### Proof

Fix $m$ parts of size $2$.  They create $m+1$ gaps: before the first, between
successive $2$-parts, and after the last.  The no-$11$ condition permits at
most one part of size $1$ in each gap.  If there are $r=n-2m$ singleton
parts, choosing their gaps gives

$$
c_{n,m}=\binom{m+1}{r}=\binom{m+1}{n-2m}.
$$

Summing over $r$ gap choices gives

$$
\begin{aligned}
C(x,u)
&=\sum_{m\geq0}u^m x^{2m}(1+x)^{m+1}\\
&=\frac{1+x}{1-ux^2(1+x)}
=\frac{1+x}{1-ux^2-ux^3}.
\end{aligned}
$$

Set $u=1$ and let $b_n=[x^n]C(x,1)$.  Then

$$
b_0=b_1=b_2=1,\qquad b_n=b_{n-2}+b_{n-3}\quad(n\geq3).
$$

To extract $a_k=b_{3k}$ without guessing a recurrence, put

$$
v_n=(b_{n+2},b_{n+1},b_n)^{\mathsf T},\qquad
T=\begin{pmatrix}0&1&1\\1&0&0\\0&1&0\end{pmatrix}.
$$

The recurrence for $b_n$ gives $v_{n+1}=Tv_n$.  Direct multiplication gives

$$
T^3=\begin{pmatrix}1&1&1\\1&1&0\\0&1&1\end{pmatrix},
$$

whose characteristic polynomial is

$$
q(\lambda)=\lambda^3-3\lambda^2+2\lambda-1.
$$

By the Cayley--Hamilton theorem,

$$
(T^3)^3-3(T^3)^2+2T^3-I=0.
$$

Since $v_{3k}=(T^3)^kv_0$ and its third coordinate is $b_{3k}=a_k$, taking
third coordinates yields

$$
a_{k+3}-3a_{k+2}+2a_{k+1}-a_k=0
$$

for every $k\geq0$.  The composition grammar gives
$a_0=1,a_1=2,a_2=4$.  Multiplying $A(z)$ by the recurrence polynomial and
using these initial values gives

$$
(1-3z+2z^2-z^3)A(z)=1-z,
$$

which is the asserted rational generating function. $\square$

### Corollary 5: exact terminal-length strata

Among terminals reached from a word of original length $n$, the number having
final length $\ell$ is

$$
N_{n,\ell}=\binom{n-\ell+1}{2\ell-n}
$$

when

$$
\left\lceil\frac n2\right\rceil
\leq\ell\leq
\left\lfloor\frac{2n+1}{3}\right\rfloor,
$$

and is zero outside this range.

#### Proof

The equations $r+2m=n$ and $r+m=\ell$ give

$$
m=n-\ell,\qquad r=2\ell-n.
$$

Substitution into Theorem 4 gives

$$
N_{n,\ell}=\binom{m+1}{r}
=\binom{n-\ell+1}{2\ell-n}.
$$

The lower bound on $\ell$ is $r\geq0$; the upper bound is
$r\leq m+1$. $\square$

### Theorem 6: exact history fibres and total history count

Let $t$ be a reachable terminal from $P(0,n)$, and let its unique composition
contain $m$ parts equal to $2$.  Then exactly $m!$ unweighted histories end at
$t$.  Consequently

$$
H_n=\sum_{m=\lceil(n-1)/3\rceil}^{\lfloor n/2\rfloor}
\binom{m+1}{n-2m}m!,
$$

and in particular

$$
H_k:=H_{3k}
=\sum_{m=k}^{\lfloor3k/2\rfloor}
\binom{m+1}{3k-2m}m!.
$$

#### Proof

Call an original edge selected when its two endpoint letters are fused.  By
Lemma 2, a current block of size $2$ cannot fuse with an adjacent block: their
union would be a periodic interval of length $3$ or $4$ collapsing to one
letter.  Therefore every legal rewrite throughout the process fuses two
still-singleton adjacent original vertices.  Selected edges consequently form
a matching of the original path.

The process is terminal exactly when no two unmatched original vertices are
adjacent.  This is exactly the condition that the selected matching is
maximal.  Its left-to-right monomer/dimer decomposition is the no-$11$
composition of Lemma 3.

Fix a reachable terminal $t$ and its matching $M$.  Every history ending at
$t$ must select precisely the edges of $M$, because the inverse decoder in
Lemma 3 fixes all singleton and dimer blocks.  Conversely, every ordering of
the $m$ edges of $M$ is legal: disjoint earlier selections do not remove either
endpoint of an unselected edge of $M$, so that edge remains an adjacent
singleton redex until it is selected.  After all $m$ selections, maximality
makes the state terminal.  Hence histories ending at $t$ are in bijection with
the $m!$ permutations of $M$.

There are $\binom{m+1}{n-2m}$ terminals with $m$ dimers by Theorem 4.
Multiplying by $m!$ and summing gives the formula for $H_n$.  For $n=3k$, the
lower limit is $\lceil(3k-1)/3\rceil=k$. $\square$

The first values are

```text
k:     1       2       3       4        5         6
H_k:   2      12     144    2640    66240   2172240
```

followed by

```text
88583040, 4387582080, 256987987200
```

for $k=7,8,9$.  These now follow from a closed finite sum; they are no longer
fitted data.

## Independent exact verifier

The verifier
`docs/papers122_126_sequence/proof_spikes/verify_stoch_ternary_fusion.py`
keeps literal rewriting and the composition model as separate implementations.
It checks:

- complete literal reachable support against the grammar for $0\leq k\leq9$;
- the unique inverse decoder, terminality, and XOR conservation for every
  grammar terminal in that range;
- literal total histories against the factorial sum through $k=9$;
- every terminal history fibre against $m!$ through $k=6$;
- the no-large-periodic-block statement for all three starting residues and
  lengths through $30$ using an independent binary-bracketing recursion;
- the $b_n$ recurrence through $n=90$ and the $a_k$ recurrence through $k=30$;
- the terminal-length profile, including
  `k=6: ((9,1),(10,36),(11,70),(12,7))`.

It reports **7,995 exact assertions**, exits zero, and reproduces
`verify_stoch_ternary_fusion.out` byte for byte.

## Corrections to the scouting interpretation

The scouting conjecture survives, but its mechanism can now be stated more
sharply:

1. the finite automaton is not merely the automaton of all irreducible ternary
   words; it is the two-state automaton of maximal matchings/no-$11$
   compositions, followed by the injective label map $\tau_n$;
2. the rewrite process from a periodic start never creates a redex involving
   a previously fused block; it is exactly sequential selection of a maximal
   matching of a path; and
3. the second paper-scale output is stronger than a total sequence: the fibre
   over each terminal is exactly $m!$, with a simultaneous terminal-length
   census and total closed sum.

## Claim ceiling and owner/value risk

The proved residual is the conjunction for the literal labelled rewrite:

- the exact reachable-terminal grammar and inverse decoder;
- its $3$-section recurrence and rational generating function;
- the terminal-length strata; and
- the exact terminal history fibres and total-history closed form.

Termination, finite rewrite DAGs, XOR conservation, regular languages,
maximal matchings of paths, and generic random greedy matching terminology
receive zero contribution credit.  In particular, the proof exposes a serious
owner/value risk: under uniform choice among current redexes, W01 is the random
greedy maximal-matching process on a path with a deterministic ternary endpoint
labelling.  A direct owner gate must determine whether the labelled endpoint
grammar/history fibres leave enough residual for a short paper after the
classical path-matching mechanism is subtracted.

No formula for the uniform-redex terminal probabilities is claimed here.
Unweighted history counts must not be described as probabilities.

## Open risks

- Direct-owner and P1--P121 collision searches are not completed by this proof
  sprint.
- The maximal-matching reduction may make the result mechanically owned even
  though the literal ternary labels and inverse grammar are exact.
- A future paper decision needs a genuinely separate owner/value review; the
  successful proof alone does not authorize promotion.
- Results here are for the periodic starts $(012)^k$.  No grammar is claimed
  for arbitrary ternary input words.
