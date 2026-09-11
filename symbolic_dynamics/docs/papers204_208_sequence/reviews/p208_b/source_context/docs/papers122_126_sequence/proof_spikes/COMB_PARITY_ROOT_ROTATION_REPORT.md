# Proof dossier and value gate: parity-guided root rotation

**Candidate:** C01 from the P122--P126 combinatorial scout.  
**Mathematical status:** `PROVABLE AS STATED`, with a stronger exact
all-depth and fibre refinement proved below.  
**Paper-value status:** `KILL_P120_COLLISION` for the P122--P126 slate;
retain only this proved dossier.  
**External status:** `HOLD_EXTERNAL`.

This document separates theorem correctness from portfolio value.  The map
has a complete finite-dynamical solution.  A bounded primary-source search
did not locate the literal parity scheduler.  Nevertheless, P120 already
occupies the canonically equivalent Catalan tree carrier with a parity-selected
tree update, fixed/recurrent generating functions, and a cycle census.  The
new transient and fibre formulas are mathematically substantive but do not
clear the internal same-carrier/same-headline gate for an adjacent paper.

## 1. Claim, assumptions, and notation

Let \(\mathcal B_n\) be the set of plane full binary trees with \(n\)
internal vertices.  The unique tree in \(\mathcal B_0\) is the leaf
\(\bullet\).  Every nonleaf tree is a unique ordered pair \(T=(L,R)\), and

\[
                 |T|=1+|L|+|R|.
\]

Define \(\Phi\colon\mathcal B_n\to\mathcal B_n\) as follows:

\[
\Phi(\bullet)=\bullet,
\]

and, for \(T=(L,R)\),

\[
\Phi(T)=
\begin{cases}
T, & |L|\text{ even and }R=\bullet,\\[2mm]
((L,B),C), & |L|\text{ even and }R=(B,C),\\[2mm]
(A,(B,R)), & |L|\text{ odd and }L=(A,B).
\end{cases}                                                \tag{1}
\]

The third line is always defined: a subtree of odd positive order cannot be
a leaf.  All parities and decompositions in (1) are read from the current
state before the single root rotation.

For a finite self-map, let \(\tau(T)\) be the first time at which the orbit
enters its eventual cycle, and let \(p(T)\) be that cycle's period.  Thus
recurrent states have depth zero.

Let

\[
C(z)=\sum_{n\ge0}C_nz^n=1+zC(z)^2
\]

be the Catalan OGF, and split it by internal-order parity:

\[
 E(z)=\frac{C(z)+C(-z)}2,\qquad
 O(z)=\frac{C(z)-C(-z)}2.                                 \tag{2}
\]

Here \(E\) includes the leaf.  Taking even and odd parts of
\(C=1+zC^2\) gives the useful identities

\[
              E=1+2zEO,\qquad O=z(E^2+O^2).               \tag{3}
\]

## 2. Exact theorem package

### Theorem 2.1 (spine normal form and pointwise clock)

Every orbit follows one root spine in one direction until it reaches either
a fixed endpoint or one edge traversed in both directions.  More precisely:

1. If \(T=(A_0,R_0)\) with \(|A_0|\) even, write the right spine uniquely as
   \(R_{j-1}=(B_j,R_j)\).  Let \(s\) be the length of the initial run
   \(B_1,\ldots,B_s\) of odd-order side subtrees; the run ends when
   \(R_s=\bullet\) or when \(R_s=(B_{s+1},R_{s+1})\) with
   \(|B_{s+1}|\) even.  Define
   \(A_j=(A_{j-1},B_j)\).  Then
   \[
                    \Phi^j(T)=(A_j,R_j),\qquad 0\le j\le s,
                                                                    \tag{4}
   \]
   and \(\tau(T)=s\).

2. If \(T=(L_0,Q_0)\) with \(|L_0|\) odd, write the left spine as
   \(L_{j-1}=(L_j,B_j)\).  There is a first even-order \(B_{s+1}\);
   before it, \(B_1,\ldots,B_s\) all have odd order.  Put
   \(Q_j=(B_j,Q_{j-1})\).  Then
   \[
                    \Phi^j(T)=(L_j,Q_j),\qquad 0\le j\le s,
                                                                    \tag{5}
   \]
   and \(\tau(T)=s\).

Thus the pointwise depth is exactly the number of consecutive odd-order side
subtrees exposed in the direction selected at time zero.

### Theorem 2.2 (recurrent locus and periods)

Every eventual period is one or two.  The fixed states are

\[
 \bullet\quad\text{and}\quad (L,\bullet)\text{ with }|L|\text{ even}.
                                                                    \tag{6}
\]

Every nonfixed recurrent state lies on a unique rotation edge

\[
 (A,(B,C))\ \longleftrightarrow\ ((A,B),C),
          \qquad |A|,|B|\text{ even}.                              \tag{7}
\]

In particular, there are no cycles of length greater than two.

### Theorem 2.3 (sharp global depth and deepest census)

For every \(n\ge1\),

\[
       \max_{T\in\mathcal B_n}\tau(T)
       =\left\lfloor\frac{n-1}{2}\right\rfloor.                   \tag{8}
\]

There is exactly one deepest state when \(n\) is odd and exactly two deepest
states when \(n\) is positive and even.  The leaf lane \(n=0\) has depth
zero and is separate from (8).

### Theorem 2.4 (fixed, recurrent, and every depth layer)

Let \(f_n\) and \(r_n\) count fixed and recurrent states in
\(\mathcal B_n\).  Their OGFs are

\[
 \boxed{F(z)=\sum_{n\ge0}f_nz^n=1+zE(z)},                           \tag{9}
\]

and

\[
 \boxed{R(z)=\sum_{n\ge0}r_nz^n
        =1+zE(z)+2z^2E(z)^2C(z)}.                                  \tag{10}
\]

If \(h_{n,s}\) is the number of order-\(n\) states of exact depth \(s\),
then the bivariate OGF is

\[
 \boxed{
 H(z,u)=\sum_{n,s\ge0}h_{n,s}z^nu^s
 =1+\frac{zE(z)+2z^2E(z)^2C(z)}{1-u zO(z)}.}                        \tag{11}
\]

Equivalently, apart from the leaf contribution at depth zero, the exact
depth-\(s\) OGF is

\[
             (zO(z))^s\bigl(zE(z)+2z^2E(z)^2C(z)\bigr).             \tag{12}
\]

Setting \(u=1\) recovers the Catalan carrier; setting \(u=0\) recovers
the recurrent locus.

### Theorem 2.5 (complete one-step fibre distribution)

Every one-step fibre has cardinality at most two.  If \(j_{n,k}\) is the
number of order-\(n\) targets of indegree \(k\), then only
\(k=0,1,2\) occur and

\[
 \begin{aligned}
 J_2(z)&=\sum_{n\ge0}j_{n,2}z^n
       =z^2E(z)O(z)+2z^3E(z)^2O(z)C(z),\\
 J_0(z)&=J_2(z),\\
 J_1(z)&=C(z)-2J_2(z).
 \end{aligned}                                                     \tag{13}
\]

Moreover,

\[
 J_2(z)=zO(z)\bigl(R(z)-1\bigr),                                  \tag{14}
\]

so the indegree-two census coincides coefficientwise with the exact
depth-one census.  Equation (14) is a counting identity; it does not identify
the two sets pointwise.

## 3. Feasibility triage and dependency map

**Proof status:** `PROVABLE AS STATED` for Theorems 2.1--2.5.

No empirical extrapolation is needed.  The dependencies are:

1. Theorem 2.1 uses only the unique left/right spine decompositions and the
   parity change under one rotation.
2. Theorem 2.2 follows from the two terminal forms in Theorem 2.1; it also
   has a direct two-line local verification from (1).
3. The upper bound in Theorem 2.3 counts disjoint odd side subtrees and spine
   vertices.  Two explicit comb families give equality.  The deepest census
   also follows from the least-degree terms of (12).
4. Theorem 2.4 uses a unique combinatorial grammar for the two directional
   spine forms.  It is a backward construction independent of forward orbit
   induction.
5. Theorem 2.5 lists all inverse rotations, proves the candidates distinct,
   and classifies when both exist.  The equality \(J_0=J_2\) then follows
   from finite edge mass.

This gives two materially different proof routes for the main temporal law:

- the **forward route** follows the literal orbit and stops at the first even
  side branch;
- the **backward route** starts from a recurrent core and uniquely prefixes
  odd side branches, producing the geometric depth factor in (11).

## 4. Proofs

### 4.1 Forward spine proof

Suppose first that \(T=(A_0,R_0)\) and \(|A_0|\) is even.  When
\(R_{j-1}=(B_j,R_j)\), the second line of (1) gives

\[
 (A_{j-1},(B_j,R_j))\longmapsto ((A_{j-1},B_j),R_j).
                                                                    \tag{15}
\]

If \(|B_j|\) is odd, then

\[
 |(A_{j-1},B_j)|\equiv1+0+1\equiv0\pmod2,                         \tag{16}
\]

so the next update again points in the same direction.  This proves (4)
through the initial odd run.

If the right spine ends after that run, the terminal state is
\((A_s,\bullet)\) with \(|A_s|\) even and is fixed by (1).  If instead the
next side subtree \(B_{s+1}\) is even, then

\[
 (A_s,(B_{s+1},R_{s+1}))
 \longleftrightarrow
 ((A_s,B_{s+1}),R_{s+1})                                  \tag{17}
\]

is a two-cycle: the left subtree on the right of (17) has odd order
\(1+|A_s|+|B_{s+1}|\).  No state before time \(s\) is recurrent, because its
next side subtree is odd and therefore the second iterate advances one more
spine position.  Hence \(\tau(T)=s\).

Now suppose that \(T=(L_0,Q_0)\) and \(|L_0|\) is odd.  Write
\(L_{j-1}=(L_j,B_j)\).  One right rotation gives

\[
 ((L_j,B_j),Q_{j-1})\longmapsto (L_j,(B_j,Q_{j-1})).                \tag{18}
\]

If \(|B_j|\) is odd, the identity

\[
 |L_{j-1}|\equiv1+|L_j|+|B_j|\equiv |L_j|\pmod2                   \tag{19}
\]

shows that \(|L_j|\) remains odd, so the orbit continues down the left
spine.  A first even \(B_j\) must occur.  Indeed, if the left spine reaches
\(L_h=\bullet\) while \(L_{h-1}\) is odd, then
\(|L_{h-1}|=1+|B_h|\) forces \(|B_h|\) even.  At the first even branch
\(B_{s+1}\), equation (19) instead forces \(|L_{s+1}|\) even.  Therefore

\[
 ((L_{s+1},B_{s+1}),Q_s)
 \longleftrightarrow
 (L_{s+1},(B_{s+1},Q_s))                                  \tag{20}
\]

is exactly a two-cycle of the form (7).  The same nonrecurrence argument for
earlier positions yields \(\tau(T)=s\), proving Theorem 2.1 and the period
part of Theorem 2.2.

For fixed points, the leaf is fixed.  A nonleaf with even left order is fixed
exactly when no left rotation is available, namely when its right subtree is
a leaf.  A nonleaf with odd left order undergoes the strict reassociation in
the third line of (1), so it is not fixed.  This proves (6).  Equations
(17) and (20) prove (7) in both directions and show that all recurrent
nonfixed states have been listed.

### 4.2 Sharp clock and witnesses

If a state has depth \(s\) in the even-left case, its initial tree contains
the outer root, at least \(s\) distinct right-spine internal vertices, and
\(s\) disjoint odd-order side subtrees.  Every odd-order subtree contains at
least one internal vertex.  Consequently

\[
                         n\ge1+s+s=2s+1.                            \tag{21}
\]

In the odd-left case, the terminal recurrent rotation requires one further
spine vertex, so the stronger \(n\ge2s+2\) holds.  Equation (21) is universal
and gives the upper bound in (8).

Let \(X=(\bullet,\bullet)\), the unique order-one tree.  For \(d\ge0\),
define

\[
 Q_0=\bullet,\qquad Q_{j+1}=(X,Q_j),
\]

and

\[
 Q'_0=X,\qquad Q'_{j+1}=(X,Q'_j).                                  \tag{22}
\]

The trees

\[
 U_{2d+1}=(\bullet,Q_d),qquad
 V_{2d+2}=(\bullet,Q'_d)                                           \tag{23}
\]

have orders \(2d+1\) and \(2d+2\), respectively.  The right-spine normal
form sees exactly \(d\) initial side branches equal to the odd tree \(X\).
The first family then reaches a fixed endpoint, while the second reaches a
two-cycle whose next side branch is a leaf.  Thus both have depth \(d\),
proving sharpness for every positive order.

The uniqueness statement for deepest states can be read directly from the
equality case of (21), or from (12).  Since

\[
 zO=z^2+O(z^4),qquad
 R-1=z+2z^2+O(z^3),                                                \tag{24}
\]

the least term contributing to order \(2d+1\) in
\((zO)^d(R-1)\) has coefficient one, and the least term at order \(2d+2\)
has coefficient two.  No depth larger than \(d\) can occur by (21).

### 4.3 Backward grammar and exact depth OGF

The fixed description (6) contributes the leaf and a root with an arbitrary
even-order left subtree and a right leaf.  This proves (9).

For a nonfixed recurrent edge (7), \(A\) and \(B\) are arbitrary even-order
trees and \(C\) is arbitrary.  Each of the two orientations has two new
internal roots.  Hence the recurrent OGF is

\[
             1+zE+2z^2E^2C,
\]

which proves (10).

We now construct every nonleaf state of depth \(s\) backward from its first
recurrent state.  In the even-left normal form, an exact depth-\(s\) tree is
uniquely

\[
 (A_0,(B_1,(B_2,\ldots,(B_s,Q)\ldots))),                           \tag{25}
\]

where \(A_0\) is even, every \(B_i\) is odd, and the terminal object \(Q\)
is either a leaf or \((B,C)\) with \(B\) even.  Its OGF is

\[
                 (zO)^s zE(1+zEC).                                \tag{26}
\]

In the odd-left normal form, the terminal recurrent left subtree is
\((A,B)\) with \(A,B\) even; prefixing \(s\) odd right-side branches along
the left spine and allowing an arbitrary outer right subtree gives

\[
                 (zO)^s z^2E^2C.                                  \tag{27}
\]

The decompositions are disjoint because the initial left order has opposite
parity in (26) and (27).  Adding them gives

\[
 (zO)^s\left(zE(1+zEC)+z^2E^2C\right)
 =(zO)^s\left(zE+2z^2E^2C\right),                                 \tag{28}
\]

which is (12).  Summing over \(s\), marking it by \(u\), and adding the
leaf proves (11).  This backward grammar proves the depth law without
following a forward orbit.

### 4.4 Exact inverse fibres

Fix a target \(T=(L,R)\).  A source that uses a left rotation is forced, if
it exists: write \(L=(A,B)\) and take

\[
                         (A,(B,R)).                                 \tag{29}
\]

It is valid exactly when \(|A|\) is even.  A source that uses a right
rotation is also forced: write \(R=(B,C)\) and take

\[
                         ((L,B),C).                                 \tag{30}
\]

It is valid exactly when \(|(L,B)|\) is odd.  Finally, \(T\) itself is a
source only when it is fixed.  A fixed target has \(R=\bullet\), so candidate
(30) is absent.  Thus no target has more than two preimages.  The candidates
(29) and (30), when both valid, are distinct because the left subtree in
(29) is a proper subtree of the left subtree in (30).

A target has two preimages in exactly two disjoint cases.

1. It is fixed and also admits (29).  Then
   \(T=((A,B),\bullet)\), with \(|A|\) even.  Fixedness forces
   \(|(A,B)|\) even, hence \(|B|\) odd.  This class contributes \(z^2EO\).
2. It admits both (29) and (30).  Write
   \(T=((A,D),(B,C))\), with \(|A|\) even.  Candidate (30) is valid exactly
   when \(|B|\equiv|(A,D)|\equiv1+|D|\pmod2\).  Thus \(D,B\) have opposite
   parity.  The two parity choices contribute
   \(2z^3E^2OC\).

This proves the first line of (13).  On each finite carrier, the sum of all
indegrees is its cardinality.  Since every indegree is zero, one, or two,

\[
 j_{n,0}+j_{n,1}+j_{n,2}=C_n,qquad
 j_{n,1}+2j_{n,2}=C_n.                                             \tag{31}
\]

Subtracting gives \(j_{n,0}=j_{n,2}\), and the remaining formulas in (13)
follow.  Multiplying the nonleaf recurrent series by \(zO\) gives (14).

## 5. Independent exact control

The independent script is

`proof_spikes/comb_parity_root_rotation_verify.py`,

with canonical stdout in

`proof_spikes/comb_parity_root_rotation_verify.out`.

It does not import the scouting pilot.  It:

- generates every plane full binary tree through order twelve
  (208,012 trees in the largest lane);
- compares literal orbit detection with a separately encoded two-sided spine
  trace and pointwise clock;
- checks closure, fixed/recurrent criteria, periods, and sharp depth;
- builds literal reverse fibres and compares each one with the two inverse
  candidates (29)--(30);
- checks (9)--(13) coefficientwise, including every exact depth layer;
- reconstructs \(C(z)\) from the depth decomposition at \(u=1\); and
- tests 82 symbolic sharp witnesses through order 82.

The fresh run made **3,777,072 exact assertions** and matched the stored
stdout byte-for-byte:

```text
$ PYTHONDONTWRITEBYTECODE=1 python3 \
    docs/papers122_126_sequence/proof_spikes/comb_parity_root_rotation_verify.py \
  | cmp - \
    docs/papers122_126_sequence/proof_spikes/comb_parity_root_rotation_verify.out
canonical comparison: PASS
```

The independent fixed and recurrent coefficients through order twelve are

```text
fixed:     1,1,0,2,0,14,0,132,0,1430,0,16796,0
recurrent: 1,1,2,4,12,32,108,320,1144,3584,13260,43008,162792
```

Finite verification is falsification evidence.  The arbitrary-order claims
rest on the proofs above.

## 6. Owner audit and zero-credit subtraction

Searches were run on 30 August 2026, including 2025--2026 results, with the
literal and translated formulations “parity-guided root rotation,” “even
left subtree rotate,” “subtree-size parity Tamari walk,” “odd side-branch
binary rotation,” “root rotation iteration,” and the exact recurrent and
coefficient strings.  No primary source for (1) was located.  This is only a
`BOUNDED_NO_EXACT_MAP_HIT`, never a novelty certificate.

The nearest primary owners are:

- Lucas, Roelants van Baronaigien, and Ruskey,
  [*On Rotations and the Generation of Binary Trees*](https://doi.org/10.1006/jagm.1993.1045),
  *Journal of Algorithms* 15 (1993), 343--366, own the rotation graph,
  rotation Gray codes, and generation framework.
- Gregor, M\"utze, and Namrata,
  [*Combinatorial generation via permutation languages. VI. Binary trees*](https://arxiv.org/abs/2306.08420),
  published in *European Journal of Combinatorics* 122 (2024), 104020,
  [DOI 10.1016/j.ejc.2024.104020](https://doi.org/10.1016/j.ejc.2024.104020),
  own the current rotation/slide generation neighborhood and its
  pattern-avoiding extensions.
- Hong,
  [*The Pop-stack-sorting Operator on Tamari Lattices*](https://arxiv.org/abs/2201.10030),
  *Advances in Applied Mathematics* 139 (2022), 102362,
  [DOI 10.1016/j.aam.2022.102362](https://doi.org/10.1016/j.aam.2022.102362),
  owns exact finite dynamics and image enumeration for a standard
  lattice-derived Tamari operator.  Hong's operator is the meet of lower
  covers and flows toward the minimum; it is not the bidirectional rule (1).
- Busjatskaja and Kochetkov,
  [*Even and odd trees*](https://arxiv.org/abs/1811.10357), study a bracket-code
  parity and rotation groups of plane bipartite trees.  Their parity is not
  left-subtree internal-order parity, and they do not iterate (1).
- Donaghey,
  [*Automorphisms on Catalan trees and bracketings*](https://doi.org/10.1016/0095-8956(80)90045-3),
  *Journal of Combinatorial Theory, Series B* 29 (1980), 75--90, owns
  Catalan-family automorphisms and orbit questions.
- Claesson, Kitaev, Steingr\'{i}msson, and Wang,
  [*Involution \(h\) on Catalan structures*](https://arxiv.org/abs/2607.06247)
  (2026), own the abstract Catalan structure, canonical transport among
  plane and binary trees, the involution \(h\), its fixed census, and its
  Donaghey factorization.  Their map is not (1), but their framework makes
  an unqualified “new Catalan tree dynamics” headline untenable.

Ordinary rotations, the associahedron/Tamari carrier, Catalan enumeration,
the parity split (2), geometric-series grammar, finite-map indegree balance,
and period-to-zeta bookkeeping all receive zero contribution credit.  The
only possible external residual is the exact conjunction (1), (4)--(14).

## 7. P120 collision gate

Full binary trees with \(n\) internal vertices and plane rooted trees with
\(n+1\) vertices are canonically bijective Catalan carriers.  P120 has
already frozen odd-fringe mirroring on the latter carrier.  The objectwise
differences are real:

| axis | C01 root rotation | P120 odd-fringe mirror |
|---|---|---|
| literal update | one root reassociation selected by current left-subtree parity | simultaneous child-list reversals at every vertex selected by old fringe-order parity |
| topology | changes parent--child incidence under the plane-tree transport | preserves every vertex, edge, underlying nonplane tree, and fringe order |
| clock | recomputed, with transients and sharp depth \(\lfloor(n-1)/2\rfloor\) | involution; every state recurrent immediately |
| enumeration | simple spine grammar, all-depth rational transform over \(E,O,C\), local fibres | twisted-palindrome recursion and an explicit degree-six fixed-series equation |
| local fibre | indegree at most two with (13) | bijection, hence indegree one |

These distinctions prevent a claim of literal duplication.  They do not
remove the portfolio collision:

1. both papers use the same Catalan carrier up to the standard canonical
   bijection;
2. both headlines are parity-selected plane/binary-tree self-maps;
3. both packages center fixed/recurrent OGFs and a period-at-most-two core;
4. the external 2024--2026 owner neighborhood already treats binary/plane
   transport, Catalan involutions, and rotation generation as one connected
   lane; and
5. the P122--P126 stage-one landscape explicitly made this same-carrier
   exclusion permanent for the current route.

The new all-depth formula (11) and fibre formula (13) make C01 a legitimate
standalone theorem spike in isolation.  After P120 subtraction, however, the
remaining value is not enough to justify a second adjacent parity-Catalan-tree
paper.  A vocabulary change from “plane rooted” to “full binary” would not
solve the collision.

## 8. Final hard verdict and claim ceiling

**Mathematical score in isolation:** `8.4/10`.  
**P122--P126 portfolio score after P120 subtraction:** `5.8/10`.  
**Verdict:** `KILL_P120_COLLISION / ARCHIVE_PROVED_DOSSIER`.

Do not open a paper directory or assign a paper number from this candidate in
the current route.  The permitted archival claim ceiling is exactly:

> The parity-guided root rotation (1) has the spine normal form (4)--(5),
> only fixed points and two-cycles recurrent, sharp maximum depth
> \(\lfloor(n-1)/2\rfloor\) for \(n\ge1\), exact fixed/recurrent/all-depth
> OGFs (9)--(12), and the at-most-two fibre distribution (13).

No priority, asymptotic, minimal-polynomial, generic Tamari-dynamics, or
owner-clearance claim is permitted.  External circulation remains
`HOLD_EXTERNAL`.
