# Proof Package

## Claim

The broad phrase “general hyperbolic \(\mathrm{SL}_2(\mathbb Z)\)” is
interpreted as \(|\operatorname{tr}M|>2\).  The positive-trace case is a
direct primitive-divisor corollary; the negative-trace case requires the
explicit parity reduction proved below.

1. If \(M\in\mathrm{SL}_2(\mathbb Z)\) is hyperbolic, equivalently
   \(|\operatorname{tr}M|>2\), then for every \(n>12\) the toral
   automorphism \(T_M\) has a point of prime additive order and exact
   dynamical period \(n\).
2. For
   \(A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\), a
   prime-order exact-period point exists if and only if
   \(n\notin\{1,6,12\}\).
3. The periodic points are exactly the torsion subgroup.  On that subgroup,
   \(L(x)=\log\operatorname{ord}(x)\) is invariant and realizes \(\log m\)
   for every \(m\geq1\), but is unbounded and discontinuous in every torsion
   neighborhood.  Its period-\(n\) Birkhoff sum is \(nL(x)\), while the
   native derivative monodromy depends only on \(n\), not on the torsion
   order.

## Status

`PROVABLE AS STATED`.

The negative-trace case is not attributed directly to Flatters.  It follows
from applying Flatters to \(B=-M\), then using three separate parity cases.
The tempting shortcut “use a primitive divisor of \(\Delta_n(B)\) for every
even \(n\)” is invalid when \(n\equiv2\pmod4\), because it can produce
half-period under \(-B\).  The proof below repairs that case with a primitive
divisor at index \(n/2\).

## Assumptions

- \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\) is written additively.
- Matrices act by multiplication modulo \(\mathbb Z^2\).
- A point has exact period \(n\) when \(n\) is its least positive return
  time.
- A primitive prime divisor of an integer sequence term \(a_n\) is a
  rational prime dividing \(a_n\) and no earlier nonzero term \(a_d\),
  \(1\leq d<n\).
- We invoke Flatters, Theorem 1.4: for a positive quadratic unit \(\alpha\)
  of norm one, the Lehmer--Pierce sequence
  \(N_{K/\mathbb Q}(\alpha^n-1)\) has a primitive prime divisor for every
  \(n>12\).
- We also use the complete norm-one classification in Flatters, Theorem 3.1,
  only for the fact that indices \(7,9,11\) are never primitive-divisor
  exceptions for a positive norm-one quadratic unit.
- For the standard cat unit
  \(\alpha=(3+\sqrt5)/2\), we additionally invoke the exact small-term
  determinant/factor ledger in Flatters, Theorem 3.1 and its proof table.

## Notation

- \(T_M(x)=Mx\pmod{\mathbb Z^2}\).
- \(\Delta_n(M)=\det(M^n-I)\).
- \(V_p=(\mathbb Z/p\mathbb Z)^2\simeq\mathbb F_p^2\).
- The nonzero class \(v\in V_p\) represents
  \(x_v=v/p\pmod{\mathbb Z^2}\), a point of exact additive order \(p\).
- \(K=\mathbb Q(\alpha)\), where \(\alpha>1\) is the expanding eigenvalue
  in the positive-trace case; for negative trace we use the expanding
  eigenvalue \(u>1\) of \(B=-M\).
- \(L(x)=\log\operatorname{ord}(x)\) for torsion \(x\).

## Proof Strategy

The carrier theorem is a reduction to a known primitive-divisor theorem,
followed by an elementary finite-field kernel argument and, for negative
trace, a three-case parity conversion from \(B=-M\) back to \(M\).  The
exact frozen-map classification combines that theorem with a fully declared
small determinant ledger and direct matrix calculations modulo \(2,3,5\).
The clock obstruction is proved by exact group theory and topology; it uses
no sampled prime or orbit data.

## Dependency Map

1. The positive-trace carrier theorem depends on the eigenvalue/norm identity,
   Flatters' norm-one primitive-divisor theorem, and Lemma 1 below.
2. Lemma 1 depends only on the identification of \(p\)-torsion with
   \(V_p\) and the definition of a primitive divisor.
3. The negative-trace carrier theorem depends on the positive-trace theorem
   for \(B=-M\), Flatters' no-exception result at indices \(7,9,11\), and
   the three parity conversions in Step 3.
4. The standard cat classification for \(n>12\) depends on the general
   theorem.
5. Its small positive cases depend on the fixed determinant factor ledger and
   Lemma 1, except \(n=10\).
6. The \(n=10\) case and the \(n=6,12\) exclusions depend on the complete
   orbit-period classification modulo \(2,3,5\).
7. The specificity theorem depends on periodic-point/torsion equivalence,
   order preservation by unimodular matrices, a coprime-order perturbation
   construction, and constancy of the derivative.

## Proof

### Step 1: identify the determinant with a quadratic norm

Let \(M\in\mathrm{SL}_2(\mathbb Z)\) have trace \(t>2\).  Its characteristic
polynomial is

\[
X^2-tX+1.
\]

The expanding eigenvalue

\[
\alpha=\frac{t+\sqrt{t^2-4}}2>1
\]

is a positive quadratic algebraic integer, its conjugate is
\(\alpha^{-1}\), and its field norm is one.  Therefore

\[
\begin{aligned}
N_{K/\mathbb Q}(\alpha^n-1)
&=(\alpha^n-1)(\alpha^{-n}-1)\\
&=2-\alpha^n-\alpha^{-n}\\
&=\det(M^n-I)=\Delta_n(M).
\end{aligned}
\]

The hypotheses of Flatters' norm-one theorem are satisfied.  Hence for each
\(n>12\), some rational prime \(p\) divides \(\Delta_n(M)\) and divides no
earlier nonzero \(\Delta_d(M)\).

### Step 2: primitive determinant divisor implies exact point period

**Lemma 1.**  If \(p\) is a primitive prime divisor of
\(\Delta_n(M)\), then every nonzero vector in
\(\ker(M^n-I:V_p\to V_p)\) represents a prime-order point of exact period
\(n\).

Because \(p\mid\det(M^n-I)\), this kernel has positive dimension.  Let
\(0\ne v\) lie in it and set \(x_v=v/p\) in \(\mathbb T^2\).  Since
\(v\ne0\) modulo \(p\), the additive order of \(x_v\) is exactly \(p\).
Its period \(d\) under \(T_M\) divides \(n\).  If \(d<n\), then
\((M^d-I)v=0\), so \(M^d-I\) is singular modulo \(p\), which means
\(p\mid\Delta_d(M)\).  This contradicts primitivity.  Thus \(d=n\).

If the kernel dimension is \(r\in\{1,2\}\), all of its \(p^r-1\) nonzero
vectors have exact period \(n\).  Their orbits are disjoint sets of \(n\)
vectors, so they form exactly

\[
\frac{p^r-1}{n}
\]

prime-order cycles.  This quotient is an integer because it counts the
orbits of the cyclic action just described.

Combining Step 1 with Lemma 1 proves the positive-trace part of Claim 1.

### Step 3: convert negative trace by an exact parity lemma

Let \(M\in\mathrm{SL}_2(\mathbb Z)\) have
\(\operatorname{tr}M<-2\), and put \(B=-M\).  Then
\(B\in\mathrm{SL}_2(\mathbb Z)\) has positive trace.  Let \(u>1\) be its
expanding eigenvalue and define

\[
\Delta_j(B)=N_{\mathbb Q(u)/\mathbb Q}(u^j-1)=\det(B^j-I).
\]

We use Lemma 1 to select a nonzero vector of exact \(B\)-period \(j\), then
show that the same vector has the requested \(M=-B\) period.  There are three
cases.

**Case 3.1: \(n\) is odd.**  Choose a primitive prime divisor \(p\) of
\(\Delta_{2n}(B)\), which exists because \(2n>12\).  Let
\(0\ne v\in\ker(B^{2n}-I)\); Lemma 1 gives exact \(B\)-period \(2n\).
Primitivity makes \(B^n-I\) invertible modulo \(p\).  Since

\[
(B^n-I)(B^n+I)v=0,
\]

we have \(B^nv=-v\).  Exact \(B\)-period \(2n\) then also shows that
\(p\ne2\).  Because \(n\) is odd,
\(M^nv=(-B)^nv=v\).  If \(M^mv=v\) for some \(0<m<n\), then
\(B^{2m}v=v\), contradicting exact \(B\)-period \(2n\).  Thus the exact
\(M\)-period is \(n\).

**Case 3.2: \(4\mid n\).**  Choose a primitive prime divisor of
\(\Delta_n(B)\), and a nonzero vector \(v\) of exact \(B\)-period \(n\).
Then \(M^nv=B^nv=v\).  If \(M^mv=v\) with \(m<n\), an even \(m\) would
give \(B^mv=v\), contradicting exact \(B\)-period.  An odd \(m\) would
give \(B^{2m}v=v\), hence \(n\mid2m\); this is impossible because
\(4\mid n\) while \(m\) is odd.  Therefore the exact \(M\)-period is
\(n\).

**Case 3.3: \(n=2k\) with \(k\) odd.**  Since \(n>12\), we have
\(k\ge7\).  Choose a primitive prime divisor \(p\) of \(\Delta_k(B)\).
It exists by Flatters' Theorem 1.4 if \(k>12\); the remaining possibilities
\(k\in\{7,9,11\}\) are never exceptions by Flatters' Theorem 3.1.

Here \(p\ne2\).  Indeed, if a nonzero vector modulo two were fixed by
\(B^k\), its orbit under the permutation of the three nonzero vectors of
\(\mathbb F_2^2\) would have a length \(d\in\{1,2,3\}\) dividing the odd
integer \(k\).  Thus \(d\in\{1,3\}<k\), so two would already divide the
earlier determinant \(\Delta_d(B)\), contradicting primitivity.

Let \(v\) have exact \(B\)-period \(k\).  Then
\(M^{2k}v=B^{2k}v=v\).  Suppose \(M^mv=v\) with \(0<m<2k\).  If \(m\) is
even, then \(B^mv=v\), so \(k\mid m\); no positive even multiple of the odd
integer \(k\) is smaller than \(2k\).  If \(m\) is odd, then
\(B^mv=-v\), hence \(B^{2m}v=v\) and \(k\mid m\).  The only possibility
below \(2k\) is \(m=k\), but
\(M^kv=-B^kv=-v\ne v\) because \(p\) is odd.  This contradiction proves
that the exact \(M\)-period is \(2k=n\).

The three cases exhaust all \(n>12\), and complete Claim 1 for every
hyperbolic \(M\in\mathrm{SL}_2(\mathbb Z)\).

### Step 4: freeze the standard cat determinant ledger

For the standard cat matrix, \(\operatorname{tr}A=3\) and
\(\alpha=(3+\sqrt5)/2\).  Write

\[
s_n=\operatorname{tr}(A^n)=\alpha^n+\alpha^{-n}.
\]

Then \(s_0=2\), \(s_1=3\),
\(s_{n+2}=3s_{n+1}-s_n\), and
\(\Delta_n=2-s_n\).  The exact small ledger is

| \(n\) | \(\Delta_n\) | exact factorization | selected new divisor |
|---:|---:|---:|---:|
| 1 | \(-1\) | \(-1\) | none |
| 2 | \(-5\) | \(-5\) | \(5\) |
| 3 | \(-16\) | \(-2^4\) | \(2\) |
| 4 | \(-45\) | \(-3^2\cdot5\) | \(3\) |
| 5 | \(-121\) | \(-11^2\) | \(11\) |
| 6 | \(-320\) | \(-2^6\cdot5\) | none |
| 7 | \(-841\) | \(-29^2\) | \(29\) |
| 8 | \(-2205\) | \(-3^2\cdot5\cdot7^2\) | \(7\) |
| 9 | \(-5776\) | \(-2^4\cdot19^2\) | \(19\) |
| 10 | \(-15125\) | \(-5^3\cdot11^2\) | none |
| 11 | \(-39601\) | \(-199^2\) | \(199\) |
| 12 | \(-103680\) | \(-2^8\cdot3^4\cdot5\) | none |

For \(n=2,3,4,5,7,8,9,11\), the selected factor is absent from every
earlier nonzero determinant.  Lemma 1 therefore supplies a prime-order exact
period-\(n\) point.  Claim 1 supplies every \(n>12\).  It remains to handle
\(n=1,6,10,12\).

### Step 5: classify the relevant reductions

Modulo two,

\[
A=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad A^3=I.
\]

Also \(A-I\) is invertible modulo two.  Thus all three nonzero two-torsion
points have exact period three.

Modulo three, direct multiplication gives

\[
A^2=-I,
\]

so \(A^4=I\).  No nonzero vector is fixed by \(A^2=-I\) in characteristic
three, and \(A-I\) is invertible.  Thus all eight nonzero three-torsion
points have exact period four.

Modulo five, put

\[
N=A+I=\begin{pmatrix}3&1\\1&2\end{pmatrix}.
\]

Then \(N\ne0\), \(N^2=0\), and \(N\) has rank one.  Since
\(A=-I+N\), the binomial formula truncates exactly:

\[
A^k=(-1)^kI+k(-1)^{k-1}N.
\]

If \(0\ne v\in\ker N\), then \(Av=-v\), so \(v\) has exact period two.
If \(Nv\ne0\) and \(A^kv=v\), an even \(k\) must satisfy
\(kNv=0\), hence \(5\mid k\).  An odd \(k\) would imply
\(kNv=2v\); applying \(N\) would give \(0=2Nv\), a contradiction.
Therefore every vector outside \(\ker N\) has exact period ten.  There are
\(25-5=20\) such vectors, hence exactly two period-ten cycles of order-five
points.

This proves existence at \(n=10\), even though \(\Delta_{10}\) has no
primitive prime divisor.

### Step 6: prove the three exclusions

For \(n=1\), \(\det(A-I)=-1\).  Therefore \(A-I\) is invertible modulo
every rational prime, and no nonzero prime-order point is fixed.

If a prime-order point has period six, its order prime must divide
\(\Delta_6\), whose prime support is \(\{2,5\}\).  The modulo-two periods
divide three, while the modulo-five periods are two or ten.  Neither case
gives period six.

If a prime-order point has period twelve, its order prime must divide
\(\Delta_{12}\), whose prime support is \(\{2,3,5\}\).  The corresponding
periods divide three, divide four, or belong to \(\{2,10\}\), respectively.
No case gives period twelve.

Together with Steps 4--5, this proves Claim 2.  The exclusion at \(n=12\)
also proves that the uniform bound “every \(n>12\)” in Claim 1 is sharp:
no smaller universal threshold can cover all hyperbolic matrices.

### Step 7: identify all periodic points and prove order invariance

Every torsion point is periodic: if \(mx=0\), then \(x\) lies in the finite
group \(\mathbb T^2[m]\), and \(A\) permutes this group because it is
invertible over \(\mathbb Z\).

Conversely, suppose \(A^nx=x\).  For a lift \(\widetilde x\in\mathbb R^2\),

\[
(A^n-I)\widetilde x\in\mathbb Z^2.
\]

Hyperbolicity implies that \(1\) is not an eigenvalue of \(A^n\), so
\(A^n-I\) is a nonsingular integer matrix.  Its inverse has rational entries,
and therefore \(\widetilde x\in\mathbb Q^2\).  Hence \(x\) is torsion.  We
have proved

\[
\operatorname{Per}(T_A)=\operatorname{Tor}(\mathbb T^2).
\]

For any \(M\in\mathrm{SL}_2(\mathbb Z)\), both \(M\) and \(M^{-1}\) have
integer entries.  If \(x\) has order \(m\), then \(mMx=M(mx)=0\), so
\(\operatorname{ord}(Mx)\mid m\).  Applying the same statement to
\(M^{-1}\) gives the reverse divisibility.  Hence

\[
\operatorname{ord}(Mx)=\operatorname{ord}(x),\qquad L(Mx)=L(x).
\]

For every \(m\geq1\), the periodic point

\[
x_m=(1/m,0)\pmod{\mathbb Z^2}
\]

has exact order \(m\).  Thus

\[
\exp L(\operatorname{Tor}(\mathbb T^2))=\mathbb N.
\]

The construction realizes primes and composites by the same rule; no
prime-specific range statement follows.

### Step 8: prove neighborhood unboundedness and discontinuity

Fix a torsion point \(x\) of order \(m\).  Choose any sequence
\(N_k\to\infty\) with \(\gcd(N_k,m)=1\), for example
\(N_k=km+1\), and set

\[
y_k=x+(1/N_k,0).
\]

Then \(y_k\to x\).  We claim that \(y_k\) has order \(mN_k\).  If
\(q y_k=0\), multiplying by \(N_k\) shows \(qN_kx=0\), hence
\(m\mid qN_k\) and therefore \(m\mid q\).  Multiplying instead by \(m\)
shows that \(N_k\mid qm\), hence \(N_k\mid q\).  Coprimality now gives
\(mN_k\mid q\).  The reverse divisibility is immediate, so the order is
exactly \(mN_k\).

Consequently

\[
L(y_k)=\log(mN_k)\longrightarrow\infty.
\]

Thus \(L\) is unbounded in every relative neighborhood of every torsion
point and is discontinuous at every such point.  Since torsion points are
dense, every nonempty open subset of \(\mathbb T^2\) contains such a
neighborhood witness.  The function cannot be the restriction of a
continuous, locally bounded, or Holder function on \(\mathbb T^2\).

### Step 9: prove the orbit-sum and monodromy specificity statements

If \(x\) has exact period \(n\), invariance gives

\[
S_nL(x)=\sum_{j=0}^{n-1}L(T_A^jx)=nL(x).
\]

For an order-\(p\) carrier this is \(n\log p\), not \(\log p\).  The latter
is recovered only by the normalized orbit average or by reading the global
point order directly.

Traversing the same primitive orbit \(r\) times gives
\(S_{rn}L=rn\log p\).  In contrast, the raw orbit label \(\log p\) itself
does not scale under repetition.  Defining a point weight \(L/n\) on that
orbit would restore an unnormalized sum \(\log p\), but the denominator
\(n\) is the global least return time and is not a fixed local continuous
observable.

Because \(T_A\) is linear,

\[
D(T_A^n)_x=A^n
\]

for every \(x\).  If \(\alpha=(3+\sqrt5)/2\), the unstable multiplier and
its logarithm are \(\alpha^n\) and \(n\log\alpha\), independently of the
torsion order \(p\).  Therefore the native derivative clock cannot
distinguish two carrier primes at a common period.  This completes Claim 3.

## Corrections or Missing Assumptions

- The initial one-citation proof only covered \(\operatorname{tr}M>2\).
  Step 3 supplies the missing negative-trace parity lemma.  In particular,
  it does not use a primitive divisor of \(\Delta_n(-M)\) when
  \(n\equiv2\pmod4\); it uses index \(n/2\), with the small indices
  \(7,9,11\) covered by Flatters' complete Theorem 3.1.
- Flatters' theorems are imported, not reproved here.  Their precise
  primitive-divisor definition and positive norm-one hypotheses remain
  attached to Claim 1; the conversion from \(-M\) to \(M\) is our separate
  elementary argument.
- Failure of the order clock's specificity does not negate the exact carrier
  theorem; these are different conclusions.

## Open Risks

- Final proof review must recheck the negative-trace three-case parity split,
  especially the \(n\equiv2\pmod4\) use of Theorem 3.1, together with the
  small cat determinant ledger and modulo-five Jordan classification.
- A bounded independent literature search did not locate the full general
  carrier theorem or standard-cat exception set as explicit statements.
  This is not proof of absence; the safe positioning remains a
  primitive-divisor audit and synthesis, not a priority claim.
- No argument here constructs the amplitudes, signs, repetitions, transfer
  operator, or quantization needed beyond Route-A A0.
