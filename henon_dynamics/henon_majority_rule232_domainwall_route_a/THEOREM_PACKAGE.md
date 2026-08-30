# C251 theorem package

## 1. Frozen map

For (n\ge1), indices are in (mathbb Z/nmathbb Z) and

\[
 F_n(x)_i=\operatorname{maj}(x_{i-1},x_i,x_{i+1}),
 \qquad x\in\{0,1\}^n .
\]

The map is synchronous; words are labelled, so rotations are not identified.
The (n=1,2) cases are retained as degenerate boundary faces.

## 2. Wall lemma

Put (w_i=x_i\oplus x_{i+1}).  A site flips precisely when both adjacent
walls are present.  Substitution into (w_i'=F_n(x)_i\oplus F_n(x)_{i+1})
gives the exact identity

\[
 w_i'=w_i(1\oplus w_{i-1}\oplus w_{i+1}) \quad (\text{in }\mathbb F_2).
\tag{2.1}
\]

If a wall word has a finite cyclic block (1^K) bounded by zeros, (2.1)
removes its two endpoint walls and leaves the interior.  Thus its length after
one tick is (max(K-2,K\bmod2)), and after (t) ticks it is

\[
 K_t=\max(K-2t,K\bmod2).
\tag{2.2}
\]

Different blocks remain separated until one disappears.  The all-one wall
word is possible only for even (n); it is exactly the alternating pair and
is invariant under one tick of the wall map.

## 3. Periodic classification

Equation (2.2) proves that every wall word containing a zero eventually has
only isolated walls.  An isolated wall means that no site of (x) is an
isolated symbol, so (F_n(x)=x).  Conversely a fixed word cannot contain
`010` or `101`, hence its wall word has no adjacent ones.  The only remaining
wall word is (1^n), which lifts to the two alternating words when (n) is
even; they exchange under (F_n).  Therefore

\[
 \operatorname{Per}(F_n)=\operatorname{Fix}(F_n)
 \sqcup
 \{0101\ldots,1010\ldots\}\quad (2\mid n),
\]

and no temporal period greater than two occurs.

If (K_j) are the wall-block lengths, the entry time to the fixed set is

\[
 \tau(x)=\max_j\left\lfloor K_j/2\right\rfloor .
\tag{3.1}
\]

For a non-alternating word, every wall block has length at most \(n-1\), so
\(\tau(x)\le\lfloor(n-1)/2\rfloor\).  The bound is attained for every
$n\ge3$: for odd $n$, use the wall word
$0\,1^{n-1}$; for even $n$, use $0\,1^{n-2}\,0$.  Both have an admissible
even wall parity and a block whose lifetime is
$\lfloor(n-1)/2\rfloor$.

## 4. Fixed-word transfer formula

The fixed language forbids the two length-three words `010` and `101`.
Using pair states (00,01,10,11), its cyclic de Bruijn matrix is

\[
 M=\begin{pmatrix}
 1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1
 \end{pmatrix}.
\tag{4.1}
\]

The standard closed-walk count gives
(#\operatorname{Fix}(F_n)=\operatorname{tr}(M^n)).  Direct determinant
calculation yields

\[
 \chi_M(\lambda)=(\lambda^2-\lambda-1)(\lambda^2-\lambda+1),
\]

so, with (L_0=2,L_1=1,L_{n+2}=L_{n+1}+L_n) and
(c_0=2,c_1=1,c_{n+2}=c_{n+1}-c_n),

\[
 \#\operatorname{Fix}(F_n)=L_n+c_n=L_n+2\cos(n\pi/3).
\tag{4.2}
\]

## 5. Transient-depth transfer formula

For (m\ge0), let (B_m) be the ((m+1)\times(m+1)) matrix indexed by a
trailing-one run (r=0,\ldots,m): (B_m[r,0]=1) and
(B_m[r,r+1]=1) for (r<m).  Let (B_m^-\) have the latter entries
replaced by (-1).  Then

\[
 E_{n,m}=\frac{\operatorname{tr}(B_m^n)+\operatorname{tr}((B_m^-)^n)}2
\tag{5.1}
\]

counts cyclic wall words of even parity with maximum run at most (m).
Every such wall word lifts to exactly two labelled (x)-words.  Hence
(2E_{n,m}) is the cumulative number of states with maximum wall run at most
(m).  Differences (2(E_{n,2t+1}-E_{n,2t-1})) give the exact population
entering the fixed set at time (t), with (E_{n,-1}=0); for even (n), the
all-one wall word is handled separately as the alternating 2-cycle.

All statements are source-local finite-state combinatorics.  They do not
provide a target arithmetic clock, a target determinant, or a Hilbert--Pólya
operator.
