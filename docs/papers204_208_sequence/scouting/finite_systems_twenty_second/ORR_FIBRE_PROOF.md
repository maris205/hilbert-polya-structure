# ORR sharp Fibonacci fibre bound, with temporal gap retained

## Claim and status

For the literal ORR on $S_n$ in `INTAKE.md`, every target has at most $F_n$
predecessors for $n\ge1$, where $F_1=F_2=1$ and
$F_n=F_{n-1}+F_{n-2}$ for $n\ge3$. This is sharp. For $n\ge3$, the unique
maximizing target is $n(n-1)\cdots1$. At $n=2$, both permutations maximize;
at $n=0,1$, the unique state has one predecessor.

Status: **PROVABLE AS STATED**. This is a post-pilot author deduction. The
complete original-box inverse outputs agree with it but are not its proof.
Its ordinary interval/composition mechanism is explicitly deducted for
the present paper gate. The sharp global temporal statement is still
NOT CURRENTLY JUSTIFIED.

## Assumptions, notation and dependency map

Use labelled permutations, linear positions and maximal increasing runs,
not cyclic runs. An inverse code is the unique valid interval partition
of the target from `PRECODE_PROOFS.md`, ORR step 3. Its blocks of odd length
are decreasing, and its even blocks are increasing. Boundary maxima/minima
ensure the reconstructed source runs are maximal.

The proof uses: (1) the complete nonredundant interval decoder; (2) a new
injective encoding of its valid partitions by compositions into odd parts;
(3) the elementary enumeration of these compositions; (4) equality forcing
using compositions containing just one part three.

## Proof

### 1. Encoding valid inverse partitions

Replace each odd block of length $r$ by the single odd part $(r)$. Replace
each even block of length $r$ by the two odd parts $(r-1,1)$. The resulting
ordered composition has total $n$ and only odd parts. We show that the
target $y$ together with this composition determines the original partition.

Process its parts from left to right, aligning them with target positions.
A current part $r\ge3$ corresponds either to an original odd block of
length $r$ or to the first part of an original even block of length $r+1$.
In the first case its $r$ entries are strictly decreasing. In the second
they are strictly increasing, and the next part must be a singleton
belonging to that even block. Since $r\ge3$, these two order patterns are
disjoint. Thus the original choice is unique whenever this part occurs in
an encoded valid partition; consume the following singleton in the even
case. A mixed-order segment cannot occur at such a part.

For a current singleton part, it is either an original singleton block or
the beginning of an original even block of length two. The latter is
possible only if the next part is also a singleton and the two target
entries are increasing. If two consecutive singleton parts start with
increasing target entries, the first cannot be an original singleton:
if the next original block is a singleton the source boundary would have
to be decreasing; if that next singleton part starts an even length-two
block, its first target entry is the minimum of that block, so the same
boundary condition again requires a descent. There is no other possibility
for a following singleton part at an unconsumed block start. Thus the
first two parts must constitute one even block. For decreasing entries
that even block is impossible, so the current part is an original
singleton. If the next part is not one, the current part must also be an
original singleton. A final singleton is handled the same way with no
available successor.

This deterministic parsing reconstructs every original valid partition.
It proves injection, without asserting that every odd composition is valid
for an arbitrary target. No boundary condition has been discarded as a
sufficiency claim.

### 2. Counting and attainment

Let $c_n$ count ordered compositions of $n$ into odd parts, including the
empty composition at $n=0$. The generating series is
$$\sum_{n\ge0}c_nz^n
=\frac{1}{1-(z+z^3+z^5+\cdots)}
=\frac{1-z^2}{1-z-z^2}.$$
Hence $c_0=1$, $c_1=c_2=1$ and $c_n=F_n$ for every $n\ge1$.
Step 1 and the nonredundant decoder give $|T^{-1}(y)|\le c_n$.

For the decreasing target $\delta_n=n(n-1)\cdots1$, take any composition
into odd parts and use those parts as consecutive target block lengths.
All blocks are decreasing. Every value in an earlier block exceeds every
value in a later block, so every reconstructed source boundary has its
required descent. Thus all $c_n$ partitions are valid, giving equality.

### 3. Uniqueness for $n\ge3$

Suppose $y$ attains $c_n$. The injection in step 1 is then onto all odd
compositions. For every $i=1,\ldots,n-2$, consider the composition with a
single part three occupying positions $i,i+1,i+2$, all other parts being
one. The part three must either be an original decreasing odd block of
length three, or start an increasing even block of length four by consuming
the following singleton. For $i=n-2$, no following singleton exists, so
the final three target entries must decrease.

Descend inductively through $i=n-3,n-4,\ldots,1$. By the previous step,
$y_{i+1}>y_{i+2}$. The triple beginning at $i$ cannot be increasing, so it
must be decreasing. At the end every adjacent pair of $y$ decreases;
as $y\in S_n$, this means $y=\delta_n$. For $n=2$ ORR holds both states,
and for $n=0,1$ it holds the sole state. These verify all boundary cases.
Therefore the stated maximum and its equality cases follow. $\square$

## Temporal proof attempt and its limit

The original finite heights through seven equal $\lfloor(n-1)/2\rfloor$
for $n\ge1$, but that equality is not proved here. Odd reversals preserve
the parity of each entry's position, and the elementary inversion potential
forces convergence. Neither observation alone bounds the number of epochs
by the length of a parity class: one entry may move in both directions
over different comparisons, and even increasing runs can be activated
after a neighbouring run changes. A claimed permanently frozen interior
or automatically expanding causal interval was not established. No such
lemma is smuggled into the proof above.

The present all-size temporal result remains only the fixed-locus theorem
and the generic nonsharp potential bound in `PRECODE_PROOFS.md`. Complete
ordinary interval inversion plus this Fibonacci extremum does not fill the
missing nontrivial temporal axis. There is no gate request or admission.
