# Narrative Report — SD-C26

**Paper type:** mathematical theory with exact implementation audit  
**Primary field:** Symbolic Dynamics  
**Tone:** bold construction test followed by a sharply scoped incompatibility
theorem  
**Route outcome:** `ROUTE_A_REJECTED`

## One-sentence contribution

A finite local code can make arithmetic certificates logarithmic and a
positive recurrent grammar can keep a prime-only connected ledger, but doing
both with intrinsic total roof (\log p) forces vertex-disjoint long cycles
whose whole adjacency is noncompact; shared recurrence instead creates
mixed composite primitive necklaces, while the only Fredholm escape stores
the atom inventory externally.

## Why this is the next paper

Paper23 closed fixed finite, fixed linear, growing finite, and two licensed
countable readers of the unary cofactor word.  It left one concrete
obligation: stop filtering a bad base cycle and build a new recurrent source
grammar with (O(\log n)) information length, total roof (\log n),
prime/composite distinction inside primitive-orbit algebra, and a Fredholm
whole operator.

SD-C26 tests that obligation in its strongest positive scalar form.  It
audits binary/Euclidean tableaux, factorization renewals, and S-adic
stationarizations.  The result is not another automata limitation.  It is a
three-way incompatibility among visible coding, connected recurrence, and
operator compactness.

## Central reasoning chain

1. A finite orbit-separating alphabet has only exponentially many visible
   cyclic words through length (L).  Infinitely many prime orbits therefore
   contain a subsequence with length at least (c\log p).
2. Two positive prime cycles cannot share a vertex.  Their concatenation
   would have a primitive root of prime roof, forcing (pq=r^m).
3. The cycles are consequently disjoint.  A length-(\ell(p)) cycle with
   total roof (\log p) has some edge of roof at most
   (\log p/\ell(p)), uniformly bounded on the counting subsequence.
4. Those edges give columns of the whole adjacency bounded away from zero
   on distinct basis vectors.  Compactness, hence every Schatten property,
   fails.
5. Sharing a prefix trie or renewal hub avoids private copies only by
   creating mixed primitive necklaces.  Its determinant is (1-F), not a
   product of independent factors.
6. A countable one-symbol-per-atom diagonal has the Euler factors and is
   trace class for (\Re s>1), but the inventory is already present in its
   states.  It works unchanged for composites and pseudorandom controls.

## Strongest result

The main theorem is the **Kraft--Fredholm trilemma**:

\[
\boxed{
\begin{array}{c}
\text{finite visible orbit separation}\
+\ \text{positive prime-only connected ledger}\
+\ T(\gamma_p)=\log p
\end{array}
\quad\Longrightarrow\quad
\text{whole one-step adjacency is noncompact}.}
\]

The theorem is allocation-independent.  Equal, concentrated, and hashed
positive roof distributions all fail for the same average-roof reason.

## A second invariant: the graph-step marker

Even a hypothetical trace-class repair must still confront (z).  A prime
orbit of graph length (\ell(p)) contributes first at (z^{\ell(p)}), while
the standard Euler factor begins at (z).  Positive equality

\[
        \det(I-zL_s)=\prod_p(1-zp^{-s})
\]

forces every prime orbit to be a loop.  A finite visible alphabet cannot
separate infinitely many such loops.  First-return induction changes the
marker; it is not a same-object repair.

## Why factorization does not become temporal concatenation

The source semiring makes primes genuine multiplicative atoms, so a
factorization grammar is the most promising constructive candidate.  Its
failure is precise.  The multiplicative monoid is commutative, but a free
word monoid is not.  If an injective compiler sent multiplication to word
concatenation, images of two primes would commute and hence be powers of one
common word; injectivity would fail.  Dynamically, a product (pq) should be
a disconnected choice of two Euler factors, whereas a renewal hub turns it
into one connected mixed cycle.

## Exact audit narrative

The sealed CPU-only prototype verifies the finite shadows of the theorem.
It reports 35/35 tests; 112 code-ledger rows; 672 positive-roof rows;
9 shared-trie rows; 36 mixed-necklace rows; 12 diagonal controls; 4
factorization controls; and 45 finite-prefix stationarization rows.  Two
clean generations are byte-identical.

At cutoff (8191), raw binary already has 3,085 proper-prefix collisions,
whereas the three self-delimiting encoders are prefix-free.  The prime Elias
gamma witness at (8191) has recurrent length 26; equal roof allocation at
(\sigma=1) gives every block singular value approximately
(0.7071101013) and block trace norm approximately (18.38486263).
Concentrating almost all roof on one edge raises the largest singular value
to approximately (0.9867588725), confirming that concentration cannot
repair compactness.

The shared trie through (127) contains 31 prime returns and already
produces 465 mixed primitive necklaces with two returns, 9,920 with three,
and 230,640 with four.  Exact symbolic determinants for
(\{2,3,5,7\}) agree with (1-F) for all three prefix encoders.  These
finite results audit formulas; the infinite theorem does not depend on
numerical extrapolation.

## Strict scope

The theorem is intentionally restricted to positive scalar one-step graph
operators, finite visible local codes, additive edge roofs, and the natural
counting space (\ell^2(V)).  It does not exclude signed or matrix
cancellation, genuinely infinite visible alphabets, nonlocal completed-orbit
weights, quotient operators, or nuclear Ruelle operators on other spaces.

That restriction is a strength: it identifies the smallest remaining
escape rather than declaring all symbolic dynamics impossible.  Paper25
must derive a signed or matrix-valued shared recurrent grammar from a source
incidence or boundary relation and cancel every mixed composite coefficient
in the full trace logarithm, including repetitions and exterior powers.

## Strict route decision

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_FAIL},
 \mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}).
\]

Overall: `ROUTE_A_REJECTED`.  Route B is locked.  No identity with
(1/\zeta(s)), analytic continuation, functional equation, critical-line
mechanism, RH implication, or Hilbert--Pólya operator is claimed.
