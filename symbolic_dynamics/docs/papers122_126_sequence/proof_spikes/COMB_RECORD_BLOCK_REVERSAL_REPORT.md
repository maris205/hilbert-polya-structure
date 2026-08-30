# Proof spike: simultaneous reversal of even record blocks

**Status:** all-size theorem package proved; external owner/value gate remains.
**External status:** `HOLD_EXTERNAL`.

## 1. Literal map

For a permutation \(\pi=\pi_1\cdots\pi_n\), cut immediately before every
left-to-right maximum.  This gives record blocks

\[
                       \pi=B_1B_2\cdots B_k.
\]

Each block begins with its largest entry, and these leading maxima increase
from block to block.  Define \(\Phi\) by reversing every even-length block
and leaving every odd-length block unchanged, synchronously.

## 2. Acyclicity and the sharp clock

The construction is order-equivariant: standardization of a word on any
finite totally ordered alphabet preserves its record cuts and block lengths,
and commutes with reversal and with \(\Phi\).  Thus prefix induction is
legitimate even when the prefix alphabet is not \([m]\).

If \(\pi\) changes, consider its first even record block.  The first entry of
that block is its maximum; after reversal it is replaced in the first changed
position by the strictly smaller last entry.  Earlier positions are unchanged,
so

\[
                         \Phi(\pi)<_{\rm lex}\pi.          \tag{1}
\]

Thus every orbit reaches a fixed point and there are no nontrivial cycles.

To bound the depth, write uniquely

\[
                          \pi=\alpha\,n\,\beta.            \tag{2}
\]

The block beginning at \(n\) is the last record block and has length
\(|\beta|+1\).  If \(|\beta|\) is even, that block is odd and inert, and
\(\Phi^t(\pi)=\Phi^t(\alpha)n\beta\) for every \(t\): changing the prefix
cannot alter the last record cut.  If \(|\beta|\) is odd, then

\[
                 \Phi(\pi)=\Phi(\alpha)\beta^{\rm rev}n. \tag{2a}
\]

The final \(n\) is thereafter a permanent singleton record block.  After
standardizing \(\gamma=\Phi(\alpha)\beta^{\rm rev}\), all subsequent steps
are \(\Phi^t(\gamma)n\).  The first case reduces to a prefix of size below
\(n\); the second costs one step and reduces to size \(n-1\).  The empty
prefix and \(n=0,1\) give the bases.  Induction therefore gives

\[
                         \operatorname{depth}(\pi)\le n-1. \tag{3}
\]

The family

\[
                         \omega_n=(2,3,\ldots,n,1)         \tag{4}
\]

is sharp.  Its only even block is \((n,1)\), so one update moves \(n\) to a
terminal singleton and leaves \(\omega_{n-1}\) on the prefix.  Hence
\(\operatorname{depth}(\omega_n)=1+\operatorname{depth}(\omega_{n-1})=n-1\).

## 3. Fixed points

A permutation is fixed exactly when all record blocks have odd length.  Set
\(f_0=1\) separately; when the double-factorial form below reaches
\((-1)!!\), use the convention \((-1)!!=1\).
Under Foata's first fundamental transformation, record blocks correspond to
cycles written with their maximum first.  Consequently the fixed points are
equienumerous with permutations all of whose cycles are odd.  If \(f_n\)
denotes their number, then

\[
 \sum_{n\ge0}f_n\frac{x^n}{n!}
 =\exp\!\left(\sum_{j\ge0}\frac{x^{2j+1}}{2j+1}\right)
 =\sqrt{\frac{1+x}{1-x}},                                 \tag{5}
\]

and

\[
f_{2m}=((2m-1)!!)^2,\qquad
f_{2m+1}=(2m+1)!!(2m-1)!!.                                \tag{6}
\]

The Foata correspondence and (5)--(6) are classical and receive zero
contribution credit; they are included only to close the functional graph.

## 4. Exact pointwise fibre theorem

The following gives every indegree and the complete image without iterating
over possible preimages.  Fix \(\sigma=\sigma_1\cdots\sigma_n\), and put

\[
                         M_j=\max(\sigma_1,\ldots,\sigma_j).
\]

A cut sequence

\[
                    0=i_0<i_1<\cdots<i_k=n                \tag{7}
\]

is called admissible when every segment \((i_{r-1},i_r]\) satisfies exactly
the appropriate endpoint condition:

\[
\begin{cases}
\sigma_{i_{r-1}+1}=M_{i_r},&i_r-i_{r-1}\text{ odd},\\
\sigma_{i_r}=M_{i_r},&i_r-i_{r-1}\text{ even}.
\end{cases}                                               \tag{8}
\]

### Fibre theorem

The preimages of \(\sigma\) under \(\Phi\) are in bijection with its
admissible cut sequences.  For a cut sequence, retain every odd segment and
reverse every even segment; the resulting concatenation is the unique
preimage associated with that cut.

Indeed, the segments of the image of a record-block decomposition satisfy
(8): an unchanged odd block has its maximum first, while a reversed even
block has its maximum last.  Its block maximum is the maximum of the entire
prefix ending there because record maxima increase.

Conversely, retain an admissible odd segment and reverse an admissible even
segment.  Condition (8) puts the prefix maximum first in either case.  These
leading maxima increase strictly from segment to segment because the entries
are distinct successive prefix maxima.  No interior entry can create an
extra record cut, since it is smaller than the first entry of its segment;
each next segment start is a record because it exceeds the entire preceding
prefix.  Hence the selected cuts are exactly and uniquely the record cuts of
the reconstructed word.  Applying \(\Phi\) returns the original segments,
and reconstructing from the image blocks of a preimage returns that preimage.
The two constructions are inverse.

Equivalently, define \(h_0=1\) and, for \(1\le j\le n\),

\[
h_j=\sum_{i=0}^{j-1}h_i\,
\mathbf 1\!\left[
 \begin{array}{l}
 j-i\text{ odd and }\sigma_{i+1}=M_j,\quad\text{or}\\
 j-i\text{ even and }\sigma_j=M_j
 \end{array}
\right].                                                  \tag{9}
\]

Last-cut decomposition gives (9): a cut ending at \(i\) contributes \(h_i\),
and the last segment is legal precisely under the displayed indicator.  Thus

\[
                         |\Phi^{-1}(\sigma)|=h_n.          \tag{10}
\]

In particular, \(\sigma\) lies in the one-step image exactly when
\(h_n>0\).  After prefix maxima are known, formula (9) uses \(O(n^2)\)
arithmetic operations; no bit-complexity claim is made.  It is a second
theorem route independent of the maximum-entry depth induction.

## 5. Exact controls and owner ceiling

One exhaustive implementation enumerates \(S_n\) through \(n=9\), checks
strict lexicographic descent, the sharp clock and witness, fixed counts, all
depth layers, and literal indegrees.  An independent verifier enumerates all
admissible cuts and checks the bijection and recurrence (9) against literal
preimages on the same range.

Foata's transformation, record/cycle correspondences, all-odd-cycle
enumeration, and generic lexicographic termination are zero-credit
background.  A bounded exact-map search found no direct owner for the
synchronous iteration or the fibre theorem; that miss is not a novelty
certificate.  The residual is restricted to the literal map, sharp linear
clock (1)--(4), and pointwise fibres (7)--(10).

**Internal verdict:** `PROVED / SEND TO HOSTILE OWNER-VALUE GATE`.

## 6. Post-gate all-size image recurrence

The first hostile gate requested an all-\(n\) aggregate beyond the pointwise
fibre formula.  The admissibility DP depends only on the set of record
positions, so it admits a finite-state weighted recurrence.

Let \(r_j\in\{0,1\}\) indicate whether position \(j\) is a record
(necessarily \(r_1=1\)), and let \(d_j\) indicate whether the prefix of
length \(j\) admits a cut as in (7)--(8).  After position \(j\), retain five
bits:

\[
(E_j,O_j,Q_j,L_j,D_j),                                   \tag{11}
\]

where \(E_j\) (respectively \(O_j\)) says that some admissible cut ends at
an even (respectively odd) index at most \(j\); \(L_j\) is the parity of the
last record position; \(Q_j=d_{\ell_j-1}\) for that last record
\(\ell_j\); and \(D_j=d_j\).  Start before the word with
\(d_0=E_0=1\) and \(O_0=0\).  At a record position \(j\),

\[
 L_j=j\bmod2,\quad Q_j=D_{j-1},\quad
 D_j=D_{j-1}\vee (E_{j-1}\text{ if }j\text{ even, else }O_{j-1}); \tag{12}
\]

at a nonrecord position,

\[
 L_j=L_{j-1},\quad Q_j=Q_{j-1},\quad
 D_j=Q_{j-1}\wedge [j\equiv L_{j-1}\pmod2].              \tag{13}
\]

In either case, add \(D_j\) to the corresponding parity accumulator
\(E_j\) or \(O_j\).  Equations (12)--(13) are exactly (9): an even final
segment is possible only when \(j\) is a record and a reachable cut of the
same parity exists; an odd final segment must begin at the last record, so
its preceding cut is \(\ell_j-1\) and its endpoint has the same parity as
\(\ell_j\).

Let \(R_j\) and \(N_j\) be the deterministic \(0\)-\(1\) transition
matrices on these five-bit states for a record and nonrecord at position
\(j\), acting on column vectors.  After the forced first record the unique
state is \((E,O,Q,L,D)=(1,1,1,1,1)\); call its unit column vector \(v_1\).
Then

\[
 v_n=\bigl(R_n+(n-1)N_n\bigr)\cdots
     \bigl(R_2+N_2\bigr)v_1,                              \tag{14}
\]

and the total one-step image size is

\[
 I_n=\sum_{s:\,D(s)=1}v_n(s).                            \tag{15}
\]

The weight \(j-1\) is exact.  Encode a permutation by the relative rank of
its \(j\)-th entry among its first \(j\) entries.  These ranks range
independently over \([j]\), and position \(j\) is a record exactly when its
rank is \(j\).  Thus a prescribed record position contributes one rank
choice and a prescribed nonrecord contributes \(j-1\), proving that the
number of permutations with record set \(S\ni1\) is
\(\prod_{j\notin S}(j-1)\).  Summing all terminal states in (14) gives
\(n!\), while summing only \(D=1\) gives (15).  Thus (14)--(15) are an exact
all-size aggregate recurrence, not a fit to the first values.

The resulting image counts begin

\[
1,1,1,4,12,60,320,2160,15960,138880,\ldots              \tag{16}
\]

for \(0\le n\le9\), agreeing with literal enumeration.  Together with
(9), this also gives the exact Garden-of-Eden count \(n!-I_n\) for every
\(n\).

**Re-entry verdict after the requested value repair:**
`PROVED / OWNER-GATED GO`, subject to the claim ceiling in the independent
hostile report and explicit subtraction of record-indicator and bubblesort
preimage background.
