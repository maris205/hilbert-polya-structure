# Independent proof and source audit

This report concerns exactly the admitted closed update
R(u,v,f)=(v,f(v),f[v:=u]) on all ordered states, n>=1. It treats the
all-parameter proof as mathematics, separately from the unexecuted finite
producer. Pointers have vertex values; parallel edges have no hidden IDs.

## Literal invariant and reduction

Writing a state as slots (u,v,f(0),...,f(n-1)), swap slot u with slot f(v),
then swap the two register slots. The result is the displayed old-state
update. Reverse these swaps for the inverse; the memory index in the reverse
step is selected after reversing the register swap. This works when registers
coincide or pointers are loops. Thus no preperiod or nonunit fibre exists.
At a fixed point u=v=f(v); choosing f and its register vertex gives n^n
fixed states after summing choices of the distinguished fixed arrow.

The edges {u,v} and {v,f(v)} are replaced by {v,f(v)} and {v,u}; other
stored edges do not change. Orient each stored edge from its source and the
extra edge from u to v. Every vertex has one outgoing edge, except u which
has two. All edges in a connected component have both endpoints there, so
the active connected component has one more edge than vertices. Inactive
components are functional, with equal edges and vertices.

A leaf in the active component cannot be u (two outgoing incidences, with a
loop contributing degree two), nor v (its own outgoing edge and the extra
incidence already give degree at least two). Its sole arrow points into the
remaining component. Repeated pruning therefore preserves both registers
and the literal dynamics. The remainder is connected, nonempty, of excess
one, and minimum degree two. The identity sum(deg-2)=2 gives one degree-four
branch or two degree-three branches. Suppression of degree-two chains gives
precisely a figure-eight, barbell, or theta, including loops and parallel
chains. The decomposition is unique. Pruned and inactive arrows are frozen.

## Return words, minimality and exhaustive decorations

At an internal chain vertex the next arrow is forced until the next branch.
For a circular sequence of register vertices x_t=u_t, the state is determined
by u_t=x_t, v_t=x_(t+1), and f_t(x)=x_(j-1), where j<=t is the most recent
cyclic visit to x. This is last-arrival reconstruction: arrival at x writes
the previous register into f(x). Consecutive visits j<k to x satisfy
x_(k+1)=x_(j-1). The frozen complement supplies pointers off the core.
Thus a primitive vertex necklace with these successor identities determines
one whole state orbit; no unobserved edge label may be used to lengthen it.

For a figure-eight, let A and B be the closed cycle walks based at its branch.
The forced four-walk circuit is A,B,reverse(A),reverse(B). After h=a+b
steps both cycle orientations reverse. A cycle of length one or two has
no observable orientation; at length at least three the two outgoing
directions differ as vertex values. Two loops give one fixed state; the
other short pairs give period h and one decoration. If some cycle is long,
an internal ordered departure distinguishes the two h-halves and has no
earlier repeated occurrence, giving period 2h. Independent long-cycle
orientation signs are quotiented by simultaneous reversal: one orbit if
only one is long and two if both are long. This counts actual states, not
an oriented-edge cover.

For a barbell choose bridge C from branch A to branch B. The forced circuit
is C,B,reverse(C),A,C,reverse(B),reverse(C),reverse(A). A half has
h=a+b+2c steps and reverses both end-cycle orientations. The directed
bridge gate bounds possible return phases; when both cycles are short the
half already returns, otherwise a long-cycle ordered departure distinguishes
the two halves. Periods are h and 2h respectively; the sign quotient gives
one decoration except when both cycles are long, when it gives two. Bridge
interior vertices do not create an additional decoration.

For a theta with endpoint-to-endpoint paths i,j,k, one circuit is
i,reverse(k),j,reverse(i),k,reverse(j). Branch roles rotate
(i,j,k)->(k,i,j); endpoint alternation doubles the three-traversal block.
If any path has an internal vertex, its ordered departure appears once per
six-walk circuit, so the exact state period is 2(a+b+c). Three direct paths
instead have the same literal neighbour at each endpoint, giving period
two. Reversal pairs the orders of three distinguishable paths into two
decorations; two indistinguishable direct paths identify them, leaving one.
There is no division by six in the all-direct literal system.

Exhaustiveness is not an assumption about a selected initialized handle.
One may mark which edge occurrence is the register edge, orient every other
occurrence with exactly one tail at each vertex, and then erase all edge
occurrence names. These are exactly the states with the fixed augmented
core. Forced chain propagation reduces every such state to the branch
return relations above. Conversely the displayed walks reconstruct states
with exactly those edges. This justifies the complete orbit-decoration
classification, including the short-chain identifications. The independent
producer explicitly compares these two full state sets in its finite box.

## Attained period set and maximum

Writing s=a+b-1 for a figure-eight, s=a+b+c-1 for a barbell, and
s=a+b+c-1 for a theta shows that an odd period can only arise from a short
case. Short barbells give even 2s when a=b=1 and odd 2s-1 when {a,b}={1,2};
the remaining short case is even. Together with period 1 and the short
figure-eight/theta cases this supplies all 1,...,2n for n>=2 (the n=2,3
boundary cases are checked directly from the same length formulas).
Long cases are even and at most 4n-4. For a long barbell, set a=1,
b=r-1>=3 and let k=p/2=r+2c. For each k=n+1,...,2n-2 choose
c=max(1,k-n-1), r=k-2c. Then r>=4 and s=r+c-1<=n, so this produces
all the remaining even periods. Its endpoint gives a=1,b=3,c=n-3
for n>=4, realizing 4n-4. The small n endpoints come from their short
rows. Padding by arbitrary frozen labels retains the period. Hence exactly
{1,...,2n} union {2n+2,2n+4,...,4n-4}, with n=1 treated separately.

## Labelled census and full extension

A rooted cycle of length a has EGF weight u_a t^(a-1), with u_1=u_2=1
and u_a=1/2 for a>=3. The reversal action on a list of internal distinct
labels is free exactly when the list has at least two members. Multiplying
two such factors by the orbit-decoration count gives 1 for two short cycles
and 1/2 otherwise. This cancellation, not an assumed uniform orbit size,
is the common weight behind the figure-eight and barbell series.

For figure-eights an unordered pair of cycle lists divides by two, except
the two-empty-lists case. That exception is tq. The other short pairs give
t^2 q^3 + t^3 q^4/2. With x=tq^2 and
D=(1-x)^(-2)-(1+x)^2, the long ordered length sum is tq^4 D/4.
For barbells endpoint interchange is free because the two branch labels
are distinct. The bridge's c-1 internal labels give the short contribution
t^2 q^4(1+tq)^2/[2(1-tq^2)] and the long contribution
t^2 q^8 D/[4(1-tq^4)]. These are the manuscript's first two pieces.

For theta cores, an unordered pair of branch labels gives t^2/2. A
nondirect path carries a nonempty ordered list, of weight Q=x/(1-x).
Three direct paths contribute q^2. For k=1,2,3 nondirect paths the
unordered-list factors 1/k! multiply decoration counts 1,2,2. Thus the
remaining term is t^2 q^6 (Q+Q^2+Q^3/3)/2. Distinct internal labels make
the unordered nondirect-path action free; indistinguishable direct paths
are not spuriously labelled. This independently explains every rational
factor in the displayed bivariate series.

An independent coefficient check at q=1 is useful. For figure-eights the
coefficients are 1,1,1 at s=1,2,3 and s/4 for s>=4. For barbells they
are [binom(s,2)+k_s]/4 with k_1=0,k_2=1,k_3=3,k_s=4 for s>=4.
For theta they are 0,1/2 at s=1,2 and s(s-1)/12 for s>=3. At s=3 the
exceptional figure-eight and barbell corrections cancel. Summation gives
c_1=1,c_2=2,c_s=(5s^2+s+24)/24 for s>=3 and hence exactly the stated
(t-t^2+t^4/2-t^5/12)/(1-t)^3. Period weighting gives
[t^s]q*dC/dq at q=1 equal to s^2(s+1)/2; this is a consistency identity,
not a third research contribution.

For a chosen core label set S any function g:V\S->V is allowable.
Its directed components either enter S through trees or stay in inactive
functional components; outdegree one off S precludes an additional active
cycle joined to S. Its pointers are frozen and its edges prune away from
the active core. Conversely unique pruning recovers S and the entire g.
Therefore the orbit-level extension is bijective, with binom(n,s)s!n^(n-s)
extensions per normalized coefficient. The full exact-period census follows.
Period alone cannot replace decorations: the admitted same-period/different-
decoration example on five labels is mathematically genuine, but is not
claimed experimentally exercised here.

## Primary-source ownership checks

All five primary works below were opened and their relevant passages read
directly in this review. This is a bounded claim-location audit, not a claim
to have read every page of every source or proved global novelty.

* Manna and Waldinger, AAAI 1987, printed page 159, nrev/nrev2 and stated
  input conditions: https://cdn.aaai.org/AAAI/1987/AAAI87-028.pdf . The old
  pointer-reversal kernel is owned prior art; nil/stopping specifications
  are not the present closed full-carrier orbit theorem.
* Loginov et al., primary author version, Figure 8, Section 5 and associated
  panhandle/visit discussion: https://research.cs.wisc.edu/wpis/papers/festschrift4444.pdf .
  The manuscript must not claim initialized reversal or bounded visit facts
  as newly discovered. Those facts do not supply the complete closed census.
* Berdine et al., CAV 2006 primary author version, Example 8:
  https://jberdine.github.io/pub/2006_cav.pdf . Its explicit 2i+j+k clock
  already counts the doubled handle. The manuscript's attribution and zero
  independent credit are appropriate.
* Holroyd et al., arXiv:0801.3306, opened latest v4 (20 June 2013):
  https://arxiv.org/pdf/0801.3306 . Definition 3.1 and Lemma 3.3 through
  Theorem 3.8 establish the fixed-digraph rotor/unicycle setting. Lemma 4.9
  is the Eulerian full-edge tour; Corollary 4.10 is the BEST count.
  The manuscript's Eulerian-tour locator is the sole open Minor, M1.
* Pham, arXiv:1403.5875v8, 30 June 2015:
  https://arxiv.org/pdf/1403.5875v8 . Theorem 1 gives M=gcd_v T(v)
  unicycle orbits and common size sum_v d^+(v)T(v)/M for the fixed strongly
  connected directed multigraph, independently of the cyclic orders; loops
  and multiple edges are included in its model. The complete orbit theorem
  belongs to this prior work, not just its Eulerian specialization.

The pointer kernel changes stored vertex values, whereas these rotor models
have fixed outgoing-edge lists and cyclic orders. This distinction is a
bounded model statement: it does not establish no conjugacy, no factor,
no alternate encoding, or priority. The manuscript appropriately confines
the retained value to the conjunction of its complete seven-row exact-
period classification and evaluated full labelled orbit-decoration census.
Prior repository collision/value-gate acceptance is reused as an explicitly
historical premise; this manuscript review does not reopen every old paper
or claim a fresh exhaustive global search. OWNER_AMBER/HOLD_EXTERNAL remain.

## Evidence limits

No execution is part of this report. In particular the two-long-cycle
figure-eight (first s=5), two-long-cycle barbell (s=6), and theta with three
nondirect paths (s=5) are justified by the all-parameter return and symmetry
arguments, not by the n<=4 preparation. A final Review A verdict still needs
the approved independent producer's actual full evidence, root reception,
same-reviewer citation closure and applicable build/view gates.
