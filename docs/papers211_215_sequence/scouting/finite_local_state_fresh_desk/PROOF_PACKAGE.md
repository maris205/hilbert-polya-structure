# Closed pointer reversal: full-carrier period and orbit dossier

Date: 2026-09-08 UTC. Status: AUTHOR_DEDUCTION_PENDING_INDEPENDENT_REVIEW.
This is an explicitly authorized follow-up to an already screened, source-owned
pointer kernel, not a fresh-map intake and not a promoted paper. No scientific
program, import, enumeration or pilot was run. Root supplied the augmented
undirected-edge invariant and the bicyclic-core direction; the scout developed
the classification and enumeration below. See SOURCES_AND_SUBTRACTION.md for
the established list-reversal mechanism that must be subtracted.

## 1. Literal carrier and inverse

For an integer n >= 1 let V=[n] and

\[
 X_n=V\times V\times V^V,\qquad
 R(u,v,f)=(v,f(v),f[v\mathrel{:=}u]).                 \tag{1}
\]

All right-hand sides use the old state. There is no nil value, stopping rule,
clock, hidden edge label, order quotient, restriction on f, or restriction
u != v. The two locations are ordered. In particular |X_n|=n^(n+2).

For a target (a,b,g), the unique inverse is

\[
 R^{-1}(a,b,g)=(g(a),a,g[a\mathrel{:=}b]).           \tag{2}
\]

Indeed a=v, b=f(v), and g(a)=u in (1); replacing g(a) by b restores f.
Conversely the displayed preimage maps to (a,b,g). This covers a=b and all
loops. Consequently every state has preperiod zero and a unit immediate fibre.
These elementary facts are background, not the independent second mechanism.

## 2. An invariant multigraph and the frozen complement

Define G by one undirected edge {x,f(x)} for every x in V and one extra edge
{u,v}. Retain multiplicity, count a loop as one edge and as degree two, but do
not distinguish parallel-edge identities. The extra edge is represented by
the ordered locations u->v. The remaining edges are represented by the stored
arrows x->f(x). Thus u has two outgoing arrows, all other vertices have one.

Under (1), old edges {u,v} and {v,f(v)} exchange the roles of extra and stored;
the traversed extra arrow reverses. Therefore the undirected multigraph G is
unchanged. The component containing u and v has one more edge than vertices:
if u and v were in the same f-component, an edge was added to one unicyclic
component; if they were in two different f-components, the extra edge joined
two unicyclic components. This handles the formerly disconnected case.
Every other component is an ordinary functional component, remains unicyclic,
and is never visited.

Repeatedly delete degree-one vertices from the active component, producing
its two-core K. A degree-one vertex cannot be the active u, which has two
outgoing arrows. Its unique incident arrow points from that vertex toward the
remaining graph. Deleting it therefore removes no outgoing arrow from any
remaining vertex. Induction proves that u survives, that every deleted edge
points toward K, and that the extra edge stays in K. Thus v also belongs to K.
The stored arrows on the deleted trees are never changed. The same applies at
every time because G is invariant. All inactive f-components are frozen too.

The core K is connected with s vertices and s+1 edges, minimum degree two,
and sum(deg(x)-2)=2. It is exactly one of the following, including subdivisions
of length one and two:

| Core | Parameters, all positive | Core size s |
|---|---|---|
| Figure-eight | Two cycles of lengths a,b sharing one branch vertex | a+b-1 |
| Barbell | Disjoint cycles of lengths a,b joined by a bridge path of length c | a+b+c-1 |
| Theta | Three internally disjoint paths of lengths a,b,c between two distinct branch vertices | a+b+c-1 |

To justify completeness, either there is one vertex of degree four or two of
degree three; every other vertex has degree two. Follow the degree-two chains
between branch incidences. A single degree-four vertex gives two closed chains.
Two degree-three vertices either have three joining chains, or one joining
chain and one closed chain at each endpoint. There is no remaining case.
Cycles of length one are loops; cycles of length two have two indistinguishable
parallel edges. A theta can have two or three indistinguishable direct paths.

## 3. Forced traversal lemma

At a degree-two vertex other than the active vertex, the stored arrow is its
unique outgoing arrow. When the extra arrow arrives there, the old stored
arrow becomes the next extra arrow and the incoming edge reverses. Therefore
an oriented degree-two chain is traversed to its other endpoint, reversing
its arrows. This is a direct induction along its internal vertices.

At a branch vertex the same rule sends the walker onto the branch's old
stored arrow and stores the edge just used in the reverse direction. With
the active branch fixed, the outdegree conditions determine the possible
orientations of every intervening chain. This also proves reachability of the
anchor states below: from an interior active vertex its selected chain is
followed to a branch; the branch configurations are precisely the indicated
ones. No detached oriented cycle is possible inside an internal chain.

A rooted cycle has one observable orientation if its length is one or two,
and two orientations otherwise. Reversal fixes exactly the former cases:
on a two-cycle both stored destinations are the opposite vertex, so changing
the identities of its parallel edges is not a change of state.

## 4. Exact periods and orbit decorations on a fixed core

For a fixed labelled K and a fixed frozen complement, every orbit has the
period in this table. The final column counts R-orbits, not states.

| Core | Exact period | Number of orbits |
|---|---|---|
| Figure-eight, a=b=1 | 1 | 1 |
| Figure-eight, a,b<=2, not both 1 | a+b | 1 |
| Figure-eight, max(a,b)>=3 | 2(a+b) | 2 if a,b>=3, otherwise 1 |
| Barbell, a,b<=2 | a+b+2c | 1 |
| Barbell, max(a,b)>=3 | 2(a+b+2c) | 2 if a,b>=3, otherwise 1 |
| Theta, a=b=c=1 | 2 | 1 |
| Any other theta | 2(a+b+c) | 1 if at least two paths are direct; otherwise 2 |

### Figure-eight proof

Let A be the common branch. Except for the double-loop case, distinguish its
two cycles by their vertex labels (a loop, when present, is unique). Consider
an anchor at which u=A and the extra arrow starts a prescribed cycle C1.
The stored arrow at A starts C2. The forced-traversal lemma first traverses
C1, then C2, then C1 reversed, then C2 reversed. After traversing both once,
the anchor is restored with both cycle orientations reversed. The first
two traversals take a+b steps.

If both cycle reversals are invisible, the state returns after a+b steps.
It cannot return sooner: the next chosen cycle at A alternates, and the
two cycles have different first destinations unless both are loops. In the
double-loop case there is only one state and it is fixed.

If a cycle has length at least three, select any one of its nonbranch
vertices z. During the four-traversal block u=z occurs twice, with the extra
arrow going to its two different neighbours. Therefore an ordered pair
(u,v) with that z and a chosen next neighbour occurs only once in the block.
A period of any state in the block must repeat that pair; the period is
exactly 2(a+b). This also rules out shorter returns at other starting phases.

At the prescribed-cycle anchor, all allowable states are specified by an
orientation for each cycle. The return operation jointly reverses them.
Its equivalence classes are two when both cycles have two orientations and
one otherwise. Every state reaches an anchor, so these classes give exactly
the orbit count asserted, without dividing a state count by a period.

### Barbell proof

Let A be one branch endpoint, chosen by label, and B the other. Take an anchor
with u=A and the extra arrow beginning the bridge toward B. Both cycles have
an orientation, and the bridge is directed from A to B. There are no other
choices. Indeed the B-cycle supplies B's one stored outgoing arrow, forcing
the bridge toward B; at A the extra bridge arrow leaves one stored outgoing
arrow for the A-cycle. The forced macro-block is

\[
 A\ \xrightarrow{\text{bridge}}\ B
 \xrightarrow{\text{B-cycle}}\ B
 \xrightarrow{\text{bridge}}\ A
 \xrightarrow{\text{A-cycle}}\ A .
\]

It lasts h=a+b+2c steps, restores the directed bridge anchor, and reverses
both cycles. The same ordered bridge departure at A occurs only at boundaries
of these blocks, since a bridge neighbour is distinct from every neighbour
of A on its own cycle, including in the loop and double-edge cases. The
period is h exactly when both cycle orientations are fixed by reversal,
otherwise 2h. Joint reversal of the two cycle orientations classifies all
orbits as above. A state with its extra arrow on a cycle reaches its branch
and then the bridge; a state on the bridge reaches a branch and then a cycle.
Hence every allowable state reaches the chosen anchor, so this classification
is exhaustive.

### Theta proof

Temporarily distinguish the three branch-to-branch chains. At an active
branch the outgoing extra chain i, outgoing stored chain j, and incoming
chain k are a permutation (i,j,k) of the chains. The traversal rule gives

\[
       (i,j,k)\longmapsto(k,i,j)
\]

at the opposite branch after traversing i. In fact i reverses, the opposite
branch's old outgoing chain was k, and its new stored chain is i. Thus the
six traversals use i,k,j,i,k,j, each chain once in each direction, and restore
the entire state after 2(a+b+c) steps.

If some chain has an internal vertex z, the ordered pair (u=z,v=one chosen
neighbour of z) occurs exactly once in that block, proving that its full
length is the minimal period even if two other chains are identical direct
edges. If all three chains are direct, their identities were artificial:
f(A)=B and f(B)=A throughout, and the only two states have (u,v)=(A,B) and
(B,A), interchanged by R. Their period is two, not six.

At a fixed branch the triple returns up to cyclic rotation after every two
traversals. With three distinguishable chains, its two cyclic orders are
exactly two orbits. Only direct chains can be identical because all other
chains have disjoint nonempty labelled internal-vertex sets. If two or three
chains are direct, the two cyclic orders become the same order of a multiset,
leaving one orbit. This proves the final column independently of state totals.

## 5. Complete period set and sharp maximum

For n=1 the only period is one. For every n>=2 the period set is

\[
 \{1,2,\ldots,2n\}
 \ \cup\ \{2n+2,2n+4,\ldots,4n-4\},               \tag{3}
\]

where the second set is empty when its upper endpoint is smaller than its
lower endpoint. Thus the largest period is 4n-4 for n>=2.

For the upper bounds, the only odd periods beyond one arise in the short-cycle
rows. A short-cycle barbell has p=a+b+2c=2s+2-(a+b), at most 2s, and an odd
one has a+b=3 so p<=2s-1. The short figure-eight and triple-direct theta give
only 1,2,3,4. All other periods are even. A nonshort figure-eight or theta has
p=2s+2<=4n-4 when s>=3. In a nonshort barbell a+b>=4, giving
p=4s+4-2(a+b)<=4s-4<=4n-4. The n=2 rows are explicit.

For attainment, period one is a double loop; period two a triple-direct
theta; period three a loop joined at its vertex to a double-edge cycle.
For even p=2k with 2<=k<=n, two loops joined by a path of length k-1 use
k vertices. For odd p=2k+1 with 2<=k<=n-1, a loop and a double-edge cycle
joined by a path of length k-1 use k+1 vertices. These give every period
through 2n. A theta on s>=3 vertices with two direct paths and one path of
length s-1 gives p=2s+2, hence half-periods 4,...,n+1.

Finally every integer k with 6<=k<=2n-2 is a half-period of a nonshort
barbell. Set c=max(1,k-n-1) and r=k-2c. Then r>=4 and s=r+c-1<=n.
Use cycles of lengths 1 and r-1 and bridge length c. Together with the
theta cases these fill all remaining even periods in (3). Each smaller
core can be padded to n labels by arbitrary inactive fixed loops. The
extreme is a theta on three vertices for n=3, and cycles 1 and 3 joined
by a bridge of length n-3 for n>=4; n=2 has the two-loop barbell.

## 6. A separate labelled orbit enumeration

Let c_(s,p) be the number of R-orbits on labelled cores of size s and exact
period p, divided by s!. Write C(t,q)=sum c_(s,p)t^s q^p. This counts the
orientation-order equivalence classes just proved; it is not |X_n| divided
by any common period.

Define x=tq^2, Q=x/(1-x), and D=(1-x)^(-2)-(1+x)^2. The three core classes give

\[
\begin{aligned}
 C_{8}(t,q)&=tq+t^2q^3+\tfrac12t^3q^4+\tfrac14tq^4D,\\
 C_{B}(t,q)&=\frac{t^2q^4(1+tq)^2}{2(1-tq^2)}
             +\frac{t^2q^8D}{4(1-tq^4)},\\
 C_{\Theta}(t,q)&=\tfrac12t^2q^2
       +\tfrac12t^2q^6\left(Q+Q^2+\tfrac13Q^3\right),\\
 C(t,q)&=C_{8}(t,q)+C_B(t,q)+C_{\Theta}(t,q).       \tag{4}
\end{aligned}
\]

Here t is a labelled exponential-generating variable: an ordered list of
ell internal labelled vertices contributes t^ell. A rooted undirected cycle
of length a contributes u_a t^(a-1), where u_a=1 for a=1,2, and u_a=1/2 for
a>=3, because reversal acts freely precisely on lists of at least two
distinct internal vertices. For a pair of rooted cycles, the number of
orbits is two exactly when both are genuine (length at least three).
Consequently their combined orientation weight is

\[
 u_a u_b\bigl(1+\mathbf1_{a,b\ge3}\bigr)
 =\begin{cases}1,&a,b\le2,\\1/2,&\max(a,b)\ge3.\end{cases} \tag{5}
\]

For a figure-eight the shared root contributes t, and its unordered cycle
pair supplies another factor 1/2. This interchange is free on labelled
structures unless both cycles are loops. The double loop is therefore added
as tq directly. The other short pairs give t^2q^3 and t^3q^4/2. Summing the
remaining ordered pairs with (5) gives

\[
 \frac14\sum_{a,b\ge1,\ \max(a,b)\ge3}
 t^{a+b-1}q^{2(a+b)}=\frac14tq^4D.
\]

For a barbell its distinct branch labels make endpoint interchange free,
giving factor 1/2; the bridge has c-1 ordered internal vertices. The short
cycle pairs contribute the first term of C_B. For the other pairs (5)
gives coefficient 1/4 and period 2a+2b+4c. Summing over positive c yields
the second term. Loops and double-edge cycles have already been included.

For a theta the unordered two distinct branch labels give t^2/2. A nondirect
chain contributes Q after marking its internal vertices and their period
weight. Three direct chains contribute q^2. If the number of nondirect
chains is k=1,2,3, their unordered set contributes Q^k/k!, and the orbit
decoration multiplier is respectively 1,2,2. This gives Q, Q^2, Q^3/3,
each with q^6 for the two branch vertices' and extra edge's period part.
This establishes (4) by a direct construction of orbit representatives.

Now choose a core label set S within [n]. For each orbit on S, every function

\[
             g:[n]\setminus S\longrightarrow[n]
\]

extends it uniquely to an orbit of R, leaving g fixed. Its arrows either
flow eventually into S (the frozen incoming trees) or form inactive functional
components. Conversely Section 2 recovers S and g uniquely from any orbit.
There are exactly n^(n-s) such extensions. This gives the complete period
refined orbit census

\[
 o_{n,p}=\sum_{s=1}^{n}\frac{n!}{(n-s)!}\,n^{n-s}
             [t^s q^p]C(t,q).                     \tag{6}
\]

Thus p o_(n,p) is the exact-period state count, and, for k>=1,

\[
          |\operatorname{Fix}(R^k)|=\sum_{p\mid k}p\,o_{n,p}. \tag{7}
\]

At q=1, let U=1+t+t^2/(2(1-t)) and V=t^2/(2(1-t)). The above construction
also gives C_8=t(U^2+V^2+1)/2, C_B=t^2(U^2+V^2)/(2(1-t)), and
C_Theta=t^2(1+Q+Q^2+Q^3/3)/2 with Q=t/(1-t). Expanding these rational
expressions gives

\[
 C(t,1)=\frac{t-t^2+\frac12t^4-\frac1{12}t^5}{(1-t)^3}
       =t+2t^2+\sum_{s\ge3}\frac{5s^2+s+24}{24}t^s.       \tag{8}
\]

Hence, with c_1=1, c_2=2 and c_s=(5s^2+s+24)/24 for s>=3,

\[
                  o_n=\sum_{s=1}^{n}(n)_s n^{n-s}c_s.    \tag{9}
\]

This is the independent second mechanism: a bijection of orbit classes with
decorated bicyclic cores and arbitrary complementary functions. The standard
ordered-list, reversal, and labelled-set counting operations are not claimed
as new. Unit fibres and finite permutation algebra do not supply (4)-(9).

## 7. Deductive consistency checks and limitations

The q^1 coefficient of (4) is t, so (6) gives n^n fixed states, also obtained
directly from u=v=f(u). Formally differentiating (4) at q=1 gives

\[
 [q\partial_q C(t,q)]_{q=1}=\frac{t(1+2t)}{(1-t)^4}
       =\sum_{s\ge1}\frac{s^2(s+1)}2t^s.
\]

These are algebraic checks, not executed finite data. For example (9) gives
o_1=1, o_2=8 and o_3=81 by hand substitution; they are not pilot results.
No computational confirmation, independent proof acceptance, global novelty,
or theorem priority is claimed. Source subtraction and independent review
remain gates. In particular the original list-reversal algorithm and its
panhandle traversal are known, while the autonomous full-carrier extension
must earn its value from the residual exact period and enumeration package.
