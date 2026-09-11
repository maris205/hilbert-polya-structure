# P199 B: endpoint proof reconstruction

Claim status: **PROVABLE AS STATED**, with precisely the frozen domain and
small-order cases. This is a fresh reconstruction, not a claim that the
classical interval coding, insertion count or ordered cuts are new proofs
in the research literature. No additional all-time inverse theorem is added.

## 1. Endpoint carrier and literal update

Represent label j by endpoints (a_j,b_j), a_j<b_j, partitioning positions
0,...,2n-1. The intervals are laminar: a crossing a_i<a_j<b_i<b_j
violates the Stirling inequality for one of i,j. Strict containment of j
inside i implies i<j. Conversely these two conditions recover exactly a
Stirling word, with the immediate containers being its parent relation.
The maximum n has consecutive endpoints. Removing them and translating
later positions by -2 gives the unique order-(n-1) carrier; inserting them
in one of 2n-1 gaps gives all states once. This classical construction is
not independent contribution credit.

The interval of 1 is exposed, since it cannot be contained in a smaller
positive label. Put (a,b)=(a_1,b_1). Delete a,b, translating each surviving
endpoint x to h(x)=x-1[x>a]-1[x>b], then insert the new maximum pair at
gap a, translating to g(x)=h(x)+2 1[h(x)>=a]. Decrement the surviving
labels. These are exactly the endpoint operations in verify_intervals.py
and reproduce the printed word splice A1B1C -> dec(A) nn dec(B) dec(C).
Intervals formerly inside 1 become exposed in its place after the new
maximum; all other containments and orders persist. The new maximum is
exposed and has unit width. Hence closure holds for all orders.

## 2. Exact clock and recurrent census

Each surviving interval is either wholly before 1, strictly inside it, or
wholly after it (there is no interval enclosing 1). Its two endpoints are
translated by the same amount by g. Therefore every surviving interval's
width b_j-a_j is unchanged. The inserted interval has width one, proving

I(Tx)={j-1: j in I(x), j>1},  I(x)={j:b_j-a_j>1}.

After t steps the original nonunit widths have precisely the remaining
labels j-t with j>t. The final one disappears at d=max I, with max empty=0.
All unit-width states have n doubled labels in arbitrary order. T changes
the label in each fixed slot by the same n-cycle, so these n! states are
permuted, with exact period n if n>=2. Any state outside has a strictly
decreasing last nonunit label and cannot recur. Thus d is first entrance,
not a bound based on an assumed core. Label n always has unit width, so
d<=n-1; the final nested (n-1),n,n,(n-1) following the doubled smaller
labels attains it. n=0 and 1 each have their one fixed state.

## 3. Depth counts, with no heuristic extrapolation

Fix 0<=t<=n-1. The clock condition says every label above t has unit width.
In the unique increasing maximum-pair construction, these widths remain
unit exactly when no later pair is inserted between their endpoints.
For k<=t every one of 2k-1 gaps is available. For k>t there are k-t-1
distinct forbidden unit-interval gaps, leaving (2k-1)-(k-t-1)=k+t choices.
No other forbidden gap exists, since smaller labels may be internal.
The choices count each endpoint carrier once, hence

F_n(t) = product_(k=1)^t(2k-1) product_(k=t+1)^n(k+t)
       = (n+t)!/(2^t t!).

The exact depth population is F_n(t)-F_n(t-1), not F_n(t). This is the
same owned insertion mechanism identified in the manuscript, explicitly
rederived in the endpoint representation; it is not claimed as a novel
independent mathematical technique. In code all coefficients are compared
to layers independently extracted from the functional graph.

## 4. Every inverse set by exposed endpoint cuts

If the target maximum interval (a,a+1) is not exposed, it has no source:
the forward operation necessarily inserts an exposed interval. Otherwise
remove that interval. Its gap is fixed and will hold the first endpoint
of source 1. Since 1 must itself be exposed, the second endpoint cannot
stop inside any target exposed interval: that would cross it. It must
stop immediately before the subsequent exposed intervals or just after
one consecutive prefix of them. Every such stop is valid because all
labels to be enclosed are incremented to values exceeding one. All other
endpoints and labels are determined by reversing the translations in
Section 1. The stop uniquely determines the source and different stops
give distinct widths for interval 1. This proves the entire inverse
bijection, both necessity and sufficiency, without a word-gap validity
search or a count-only transfer matrix.

If r exposed intervals follow the maximum, exactly r+1 stops exist. Since
r<=n-1, the fibre is at most n. Equality requires n-1 intervals after the
maximum, which uses all labels, leaves nothing before it, and forbids
every containment. These are precisely doubled permutations starting
with nn, numbering (n-1)!. All have fibre n, including n=1. At n=0 the
unique empty predecessor is direct. Unsupported targets are included in
the full source-set checks.

## 5. Image enumeration by exposed-gap double counting

Let e=d+1 for a carrier with d exposed intervals; e counts the exterior
insertion gaps. Write S_m=sum e over order m, with S_0=1. Inserting a
new maximum at one of e exterior gaps changes e to e+1. At any of the
remaining 2m+1-e gaps it leaves e fixed. The sum of e over all children
of this carrier is e(e+1)+(2m+1-e)e=(2m+2)e. Uniqueness of maximum
deletion gives S_(m+1)=(2m+2)S_m, so S_m=2^m m!.

Each image target arises uniquely by taking an order-(n-1) carrier and
putting nn into one exterior gap. Thus image size S_(n-1)=2^(n-1)(n-1)!,
which agrees with the independent target-support proof. Keeping powers
z^e yields the full polynomial recurrence printed in the paper; its
coefficient vector is checked directly by the verifier rather than only
its derivative at one. This enumeration uses established gap counting.

## 6. Independent graph logic and boundaries

For any finite map, the descending sequence X,T(X),T²(X),... stabilizes
at its recurrent set: on the stable finite image T is a surjection and
hence a permutation; every periodic point belongs to every image. The
verifier computes that sequence until actual equality, without a bound
from the proposed theorem. Starting with this stable set, successive
preimages contain exactly the states of entrance time at most t; their
strict differences give layers. This differs from author Kahn peeling
and Review A's individual forward orbit paths. Fixed-iterate counts on
the resulting core confirm exact n-period, not merely divisibility.

Every complete source and target through n=7 is tested, with entire
incoming sets, all maximizers, mass, image and layer identities. Finite
enumeration is only counterexample pressure. The preceding deductions
handle every n and no random experiment, empirical fit, external priority
or unproved extension is part of this acceptance.
