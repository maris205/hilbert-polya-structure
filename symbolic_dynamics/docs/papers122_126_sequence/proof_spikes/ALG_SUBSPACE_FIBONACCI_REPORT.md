# Proof dossier: nilpotent subspace-Fibonacci dynamics

**Intake label:** C3 (not a paper number)  
**External status:** `HOLD_EXTERNAL`  
**Proof status:** `PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`

The requested statement has one genuine boundary exception: when \(d=1\),
the maximum transient is \(0\), not \(d=1\).  The corrected theorem is proved
below.  No novelty, priority, authorship, venue, or paper-number decision is
made in this dossier.

## Claim

Let \(V\) be a \(d\)-dimensional vector space over the finite field
\(\mathbb F_q\), where \(d\geq1\).  Fix a regular nilpotent endomorphism
\(N:V\to V\).  Thus there is a Jordan-chain basis

\[
e_0,e_1,\ldots,e_{d-1}
\]

such that

\[
Ne_i=e_{i+1}\quad(0\leq i<d-1),\qquad Ne_{d-1}=0.
\]

On the finite state space \(\mathcal L(V)^2\), where \(\mathcal L(V)\) is the
lattice of linear subspaces of \(V\), define

\[
T(U,V)=(V,U+NV).
\tag{1}
\]

For an initial state \((U,V)\), write

\[
T^t(U,V)=(X_t,X_{t+1});
\]

equivalently,

\[
X_0=U,\qquad X_1=V,\qquad X_{t+2}=X_t+NX_{t+1}.
\tag{2}
\]

Then:

1. For every \(r\geq1\),

   \[
   X_{2r}=\sum_{j=0}^{r-1}N^{2j}U+
           \sum_{j=0}^{r-1}N^{2j+1}V,
   \tag{3}
   \]

   while for every \(r\geq0\),

   \[
   X_{2r+1}=\sum_{j=0}^{r-1}N^{2j+1}U+
             \sum_{j=0}^{r}N^{2j}V.
   \tag{4}
   \]

   The first sum in (4) is the zero subspace when \(r=0\).

2. Every orbit is on a fixed point or a 2-cycle by time \(d\).  More
   precisely,

   \[
   T^{t+2}(U,V)=T^t(U,V)\qquad(t\geq d).
   \tag{5}
   \]

3. A state \((U,V)\) is recurrent if and only if

   \[
   NU\subseteq V\qquad\text{and}\qquad NV\subseteq U.
   \tag{6}
   \]

   Equivalently, the recurrent set is the fixed-point set of \(T^2\).

4. The fixed points are precisely

   \[
   (W,W)\quad\text{with}\quad NW\subseteq W,
   \tag{7}
   \]

   and there are exactly

   \[
   d+1
   \tag{8}
   \]

   of them.

5. If the transient depth of a state is the least \(t\geq0\) for which its
   \(t\)-th iterate is recurrent, then the sharp maximum depth is

   \[
   D_d=
   \begin{cases}
   0,&d=1,\\
   d,&d\geq2.
   \end{cases}
   \tag{9}
   \]

   For every finite field and every \(d\geq2\), the single uniform family

   \[
   (U,V)=(\langle e_0\rangle,0)
   \tag{10}
   \]

   has transient depth exactly \(d\).

## Status

`PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`.

Items 1--4 survive unchanged.  The unqualified assertion “maximum transient
equals \(d\)” is false at \(d=1\).  Formula (9) is the minimal correction; for
every \(d\geq2\), the requested value and a field-uniform sharp witness are
valid.

## Assumptions

- \(q\) is a prime power and \(V\) is \(d\)-dimensional over \(\mathbb F_q\).
- \(d\geq1\).
- \(N\) is regular nilpotent, meaning that its nilpotency index is \(d\), or
  equivalently that it has one Jordan block.
- A sum of subspaces denotes their linear span; an empty sum is \(0\).
- “Recurrent” means that the state lies on a directed cycle of the finite
  functional graph of \(T\).

The closed-iterate and depth arguments use only \(N^d=0\), except that
regularity is needed for the fixed-point count \(d+1\) and for the sharp
witness (10).

## Notation

- \(N^jU=\{N^ju:u\in U\}\), a linear subspace of \(V\).
- \(\mathcal L(V)\) is the set of all linear subspaces of \(V\).
- \(X_t\) is defined by (2).
- A state has depth zero precisely when it is recurrent.

## Proof strategy

The proof uses four elementary reductions:

1. solve the subspace recurrence (2) by induction in the idempotent additive
   monoid of subspaces;
2. use \(N^d=0\) to show that the even and odd subsequences stabilize by
   time \(d\);
3. compute \(T^2\) literally to characterize its fixed points;
4. identify \(N\)-invariant subspaces with ideals of
   \(\mathbb F_q[z]/(z^d)\), and use the Jordan-chain witness (10) to prove
   sharpness.

## Dependency map

1. The arbitrary-time formulas (3)--(4) depend only on (2), distributivity
   \(N(A+B)=NA+NB\), and induction.
2. The universal eventual identity (5) depends on (3)--(4) and \(N^d=0\).
3. The recurrent criterion depends on (5) and the exact formula for \(T^2\).
4. The fixed-point count depends on the recurrent dynamics only for context;
   its enumeration uses the cyclic \(\mathbb F_q[z]\)-module model of a
   regular nilpotent operator.
5. The upper depth bound follows from (5); equality follows from a direct
   analysis of (10).  The case \(d=1\) is separate.

## Proof

### Step 1: arbitrary-time closed forms

Equation (1) gives

\[
T(X_t,X_{t+1})=(X_{t+1},X_t+NX_{t+1}),
\]

which proves the recurrence (2).

We prove (3)--(4) simultaneously.  When \(r=0\), equation (4) says

\[
X_1=V,
\]

because its first sum is empty and its second sum is \(N^0V=V\).  When
\(r=1\), equation (2) gives

\[
X_2=U+NV,
\]

which is (3).

Assume that (3)--(4) hold for a fixed \(r\geq1\).  Applying (2) and
\(N(A+B)=NA+NB\),

\[
\begin{aligned}
X_{2r+2}
 &=X_{2r}+NX_{2r+1}\\
 &=\left(\sum_{j=0}^{r-1}N^{2j}U+
          \sum_{j=0}^{r-1}N^{2j+1}V\right)
   +\left(\sum_{j=0}^{r-1}N^{2j+2}U+
           \sum_{j=0}^{r}N^{2j+1}V\right)\\
 &=\sum_{j=0}^{r}N^{2j}U+
   \sum_{j=0}^{r}N^{2j+1}V.
\end{aligned}
\]

The last equality uses idempotence of subspace sum: repeated summands do not
change a span.  This is (3) with \(r\) replaced by \(r+1\).  Applying (2)
once more,

\[
\begin{aligned}
X_{2r+3}
 &=X_{2r+1}+NX_{2r+2}\\
 &=\left(\sum_{j=0}^{r-1}N^{2j+1}U+
          \sum_{j=0}^{r}N^{2j}V\right)
   +\left(\sum_{j=0}^{r}N^{2j+1}U+
           \sum_{j=0}^{r}N^{2j+2}V\right)\\
 &=\sum_{j=0}^{r}N^{2j+1}U+
   \sum_{j=0}^{r+1}N^{2j}V.
\end{aligned}
\]

This is (4) with \(r\) replaced by \(r+1\).  Simultaneous induction proves
(3)--(4) for every permitted \(r\).

### Step 2: universal stabilization to period at most two

Compare \(X_{t+2}\) with \(X_t\) using (3)--(4).  If \(t=2r\) is even, then

\[
X_{t+2}=X_t+N^tU+N^{t+1}V.
\tag{11}
\]

If \(t=2r+1\) is odd, then

\[
X_{t+2}=X_t+N^tU+N^{t+1}V.
\tag{12}
\]

Thus the same identity holds for both parities.  When \(t\geq d\), both
\(N^t\) and \(N^{t+1}\) vanish because \(N^d=0\).  Therefore

\[
X_{t+2}=X_t\qquad(t\geq d).
\tag{13}
\]

Applying (13) at \(t\) and \(t+1\) gives

\[
(X_{t+2},X_{t+3})=(X_t,X_{t+1}),
\]

which is exactly (5).  In particular, \(T^d(U,V)\) lies on a cycle whose
length divides two.

### Step 3: recurrent states

A direct application of (1) gives

\[
T^2(U,V)=(U+NV,\;V+NU+N^2V).
\tag{14}
\]

Suppose first that \(T^2(U,V)=(U,V)\).  Equality of the first coordinates in
(14) gives \(NV\subseteq U\).  Equality of the second coordinates gives
\(NU\subseteq V\) (and also \(N^2V\subseteq V\)).  Hence (6) is necessary.

Conversely, suppose (6) holds.  Then

\[
N^2V\subseteq NU\subseteq V.
\]

Consequently both added subspaces on the right side of (14) are already
contained in their respective coordinates, and \(T^2(U,V)=(U,V)\).
Therefore (6) is equivalent to being fixed by \(T^2\).

Every state fixed by \(T^2\) is recurrent.  For the converse, let a recurrent
state have least period \(\ell\).  By (5), its \(d\)-th iterate is fixed by
\(T^2\).  Since \(T^d\) is a bijection on the \(\ell\)-cycle, applying the
inverse of its restriction to that cycle shows that the original state is
also fixed by \(T^2\).  Hence every recurrent state satisfies (6), completing
the proof of item 3.

### Step 4: fixed points and their number

The equality

\[
T(U,V)=(U,V)
\]

holds if and only if its first coordinate gives \(V=U\) and its second gives

\[
U+NU=U,
\]

which is equivalent to \(NU\subseteq U\).  This proves (7).

It remains to count the \(N\)-invariant subspaces.  Give \(V\) the structure
of an \(\mathbb F_q[z]\)-module by letting multiplication by \(z\) act as
\(N\).  The map

\[
\mathbb F_q[z]/(z^d)\longrightarrow V,
\qquad f(z)\longmapsto f(N)e_0,
\tag{15}
\]

is an \(\mathbb F_q[z]\)-module isomorphism, because \(z^je_0=e_j\) for
\(0\leq j<d\).  An \(\mathbb F_q\)-subspace is \(N\)-invariant precisely when
it is an \(\mathbb F_q[z]\)-submodule.  Under (15), these submodules are the
ideals of \(\mathbb F_q[z]/(z^d)\).

Ideals of the quotient correspond to ideals of \(\mathbb F_q[z]\) containing
\((z^d)\).  Since \(\mathbb F_q[z]\) is a principal ideal domain, such an ideal
is generated by a monic divisor of \(z^d\), hence by exactly one of

\[
1,z,z^2,\ldots,z^d.
\]

Thus the invariant subspaces are exactly

\[
\langle e_j,e_{j+1},\ldots,e_{d-1}\rangle
\quad(0\leq j<d)
\]

together with \(0\), corresponding to \(j=d\).  There are \(d+1\), which
proves (8).

### Step 5: sharp transient depth

Equation (5) shows that every state is recurrent by time \(d\), so every
transient depth is at most \(d\).

If \(d=1\), then \(N=0\) and

\[
T(U,V)=(V,U).
\]

Every state is already fixed or lies on a 2-cycle.  Hence \(D_1=0\), proving
the exceptional line of (9).

Now assume \(d\geq2\), and take the state (10).  For \(1\leq t\leq d\), the
closed forms reduce to alternating Jordan-chain spans.  If \(t=2r\) is even,

\[
X_t=\langle e_0,e_2,\ldots,e_{t-2}\rangle,
\qquad
X_{t+1}=\langle e_1,e_3,\ldots,e_{t-1}\rangle.
\tag{16}
\]

If \(t=2r+1\) is odd,

\[
X_t=\langle e_1,e_3,\ldots,e_{t-2}\rangle,
\qquad
X_{t+1}=\langle e_0,e_2,\ldots,e_{t-1}\rangle.
\tag{17}
\]

For \(t=1\), the first span in (17) is empty and hence equals \(0\).

At time \(t=0\), the state is not recurrent because

\[
N\langle e_0\rangle=\langle e_1\rangle\nsubseteq0.
\]

For every \(1\leq t<d\), equations (16)--(17) show that

\[
e_t\in NX_{t+1}\qquad\text{but}\qquad e_t\notin X_t.
\]

The recurrent criterion (6), applied to the state \((X_t,X_{t+1})\), therefore
fails at every time \(t<d\).  Step 2 shows that the state is recurrent at time
\(d\).  Its depth is exactly \(d\), over every finite field.  This proves the
second line of (9), the uniform sharp witness (10), and the theorem.  ∎

## Corrections or missing assumptions

- **Required correction:** replace “maximum transient equals \(d\) for all
  \(d\geq1\)” by (9), or state the equality only for \(d\geq2\).
- Regularity of \(N\) is essential for the count \(d+1\).  A nilpotent
  operator with several Jordan blocks generally has more invariant
  subspaces.
- Finiteness of the field ensures that “recurrent” has its standard finite
  functional-graph meaning.  The algebraic identities themselves remain
  valid over an arbitrary field.

## Independent mechanical verification

The verifier [`verify_alg_subspace_fibonacci.py`](verify_alg_subspace_fibonacci.py)
does not import the scouting pilot.  It uses reduced-row-echelon bases over
prime fields rather than binary membership masks.  It checks:

- the Gaussian-binomial count of its enumerated subspaces;
- every closed term through time \(2d+3\) for every state in 12 exhaustive
  lanes;
- the equivalence of (6), recurrence, and \(T^2(U,V)=(U,V)\);
- the depth bound and sharp maximum;
- the fixed-point count \(d+1\);
- the witness (10) for four primes and every \(1\leq d\leq12\).

The exhaustive lanes are

\[
(q,d)=(2,1\ldots5),\quad(3,1\ldots4),\quad(5,1\ldots3).
\]

The deterministic run passes **3,188,520 assertions**.  Canonical stdout is
stored in
[`ALG_SUBSPACE_FIBONACCI_CANONICAL.txt`](ALG_SUBSPACE_FIBONACCI_CANONICAL.txt).

Run from the repository workspace:

```bash
python3 docs/papers122_126_sequence/proof_spikes/verify_alg_subspace_fibonacci.py
```

This computation is an independent falsification check; the proof above, not
the finite enumeration, establishes the theorem for all prime powers and all
dimensions.

## Open risks

- The theorem package gives a complete pointwise iterate formula, recurrent
  criterion, fixed count, and sharp maximum depth, but it does **not** yet
  enumerate all recurrent pairs or every exact depth layer over general
  \(q,d\).  Such an enumeration remains the main paper-scope question.
- Direct-owner and nearest-mechanism screening remains a separate gate.  This
  dossier proves correctness only; it does not upgrade the earlier bounded
  no-hit to a novelty conclusion.
- No paper number should be assigned on the strength of this proof spike
  alone.
