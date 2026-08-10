# Narrative report

## The door opened by C27

C27 produced an ordinary trace-class determinant for every fixed odd prime.
That result left a precise global question: are the prime fibres local pieces
of one determinant, or merely a family of unrelated finite specializations?
The difficulty is not the chronology.  Every local operator already retains
the full Rauzy order.  The difficulty is the growing fibre dimension
\(p^2\).

C28 determines the effect of that multiplicity exactly.  The C27 estimate
\(\|\mathcal L_{s,p}\|_1\ll p^2\) could have been a loose consequence of
tensoring.  It is not.  Point evaluation and constant functions compress the
operator to an absolutely summable sum of finite Weil matrices.  Testing the
compression against one inverse branch matrix isolates one branch in the
large-prime normalized trace.  C25's all-length matrix decoder prevents a
second branch from contributing the identity.  This gives the matching
lower bound and, for every Schatten exponent,

\[
\|\mathcal L_{s,p}\|_{S_q}\asymp p^{2/q}.
\]

## The positive global theorem

The sharp local estimate classifies every scalar-weighted prime block sum:

\[
\bigoplus_p c_p\mathcal L_{s,p}\in S_q
\quad\Longleftrightarrow\quad
\sum_p p^2|c_p|^q<\infty.
\]

For the prime norm \(c_p=p^{-z}\), the exact wall is
\(q\operatorname{Re}z=3\).  The boundary is the divergent prime harmonic
series.  Consequently

\[
\mathfrak L_{s,z}
=\bigoplus_{p\ \mathrm{odd}}p^{-z}\mathcal L_{s,p}
\]

is trace class exactly for \(\operatorname{Re}z>3\), and in that half-plane

\[
\mathfrak D(s,z,u)
=\det(I-u\mathfrak L_{s,z})
=\prod_{p\ \mathrm{odd}}\mathcal D_p(s,up^{-z})
\]

is an ordinary jointly holomorphic Fredholm determinant.  The product is
independent of the enumeration of the primes because it comes from a
trace-norm convergent Hilbert direct sum.

The new factor does not average the dynamics.  A length-\(n\) word contributes

\[
p^{-nz}\Theta_p(g_w)
\frac{\lambda_w^{-(s+1)}}{\chi_w'(\lambda_w)},
\]

with \(g_w\) formed in the full chronological order.  A repeated primitive
word uses \(\Theta_p(g_w^r)\).  The price of convergence is different:
\(z\log p\) is a new per-return grading that does not come from the AGY roof.

## Why the two weight-free alternatives fail

The unweighted direct sum is not merely outside trace class.  Its prime
blocks have operator norms bounded below, so the direct sum is noncompact.

The normalized fibre trace goes in the opposite direction.  For every fixed
integral symplectic matrix \(h\), rank stability and Thomas's character
formula give

\[
\frac{\Theta_p(h)}{p^2}\longrightarrow\mathbf1_{h=I}.
\]

Thus the normalized finite-Weil characters converge to the regular trace of
the integral cocycle group.  C25 proves that the positive AGY first-return
monoid is free: no nonempty positive word has identity matrix.  Every
normalized positive moment therefore tends to zero, and on one common
compact-uniform disc, with the Fredholm logarithm branch fixed at the
origin,

\[
\exp\!\left[p^{-2}\operatorname{Log}_0\mathcal D_p(s,u)\right]
\longrightarrow1.
\]

The counting trace is too large; the normalized trace exists but erases the
one-sided determinant germ.  This does not assert a global choice of a
\(p^2\)-th root.

## Arithmetic survives as fluctuations, not as a common conductor

At a regular word the unnormalized finite-Weil trace is the quadratic sign

\[
\Theta_p(g_w)=\left(\frac{\det(I-g_w)}p\right)
\]

outside finitely many primes.  The prime-graded trace coefficients are
therefore quadratic prime Dirichlet series with exact singular-prime
corrections.  This arithmetic is genuine, but each word has its own
squarefree kernel and repeated words generally change the character.  The
C27 census found 150 different signatures among 150 bounded induced
branches.  That is finite evidence of fragmentation, not an all-length
theorem.

## The fixed-plane stress test

The C24 full-Rauzy ledger contains one decisive ambient control.  P073 has

\[
\det(xI-g_{073})=(x-1)^2(x^2-18x+1),
\qquad
\dim\ker(g_{073}-I)=2.
\]

Exact minors show that the fixed dimension remains two modulo every prime,
and Thomas's quotient form has determinant \(-4\).  Hence

\[
\Theta_p(g_{073})=p
\]

for every odd prime.  Its dimension-normalized MARKED sum is
\(\sum_p1/p\), which diverges.  P073 closes the corresponding full-C24
dimension-normalized MARKED assembly.  It is not a C26 positive-prefix
induced branch, so the
all-word fixed-plane question for that narrower language remains open.

## Research decision

C28 is a positive analytic result and a negative canonicality result.  It
constructs a nontrivial global determinant after prime damping and proves
that the most direct undamped alternatives fail in complementary ways.  It
does not construct an adelic Weil representation: that term belongs to a
restricted tensor product of local-field oscillator representations with
compatible global data, not to the present direct sum of residue-field
fibres.

The next large move should not extend the prime table.  A two-sided based
path groupoid could create nonempty identity-holonomy loops that the regular
trace can see.  Alternatively, a genuine \(p\)-adic oscillator and
automorphic/theta-kernel construction would change the fibre architecture
completely.  Neither is a small repair of C28.
