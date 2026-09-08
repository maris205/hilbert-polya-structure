# AS1: summable spectral measure and the positivity cancellation obstruction

2026-09-08 UTC. Coordinator-authored auxiliary hand proof, pending
nonauthor review. Original full AS1 contract unchanged and **not closed**.
This is not a fifth contract or a manuscript. No mathematical program ran.
The timing and precise attempt are recorded in [FROZEN_ATTEMPT.md](FROZEN_ATTEMPT.md).

## Claim and inputs

The accepted [round-seven proof](../../continuation_round7/spectral_scout/AS1_PROOF_PACKAGE.md)
and its [nonauthor review](../../continuation_round7/spectral_review/INDEPENDENT_REVIEW.md)
are inputs, not newly rerun proofs. Write
\(\varphi=(1+\sqrt5)/2\), \(U_k=(\mathbb Z/2^k\mathbb Z)^\times\),
and let \(T_{\chi,k}\) be the exact finite projective transfer matrices.
The accepted trace identity and coefficient definitions are

\[
 b_{n,k}=\frac1{|U_k|}\sum_{\chi\in\widehat U_k}
                  \operatorname{tr}(T_{\chi,k}^{n}),\quad
 a_n=\sum_{k\ge1}2^{-k}b_{n,k},\quad
 P(u)=\sum_{n\ge1}\frac{a_n}{\varphi^n}\frac{u^n}{n},\quad Q=uP'.
\]

All normalized eigenvalues have modulus at most one. The new results are:

1. Their weighted algebraic multiplicities define a finite positive
   atomic measure \(\mu\), of mass at most \(119/55\), giving exact
   Cauchy and logarithmic representations of \(Q,P\) in the disk.
2. The accepted trivial-on-\(1+8\mathbb Z_2\) characters give a known
   submeasure of mass \(11/6\); the positive remainder has mass at most
   \(109/330\) and no boundary atoms.
3. Finite positive atomic mass, no boundary atoms and dense boundary
   accumulation of the atoms do **not** force a natural boundary of its
   Cauchy transform. An explicit finite positive measure below has all
   positive analytic moments zero and atoms approaching every boundary
   point. This is a generic counterexample, **not** the actual AS1 measure.

These are elementary local deductions, not claims of new general
operator theory or representing-measure theory. Classical context and
the actual scope of primary-source checks are in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).

## 1. A nonzero-spectrum multiplicity bound independent of ambient size

Put \(m=\lceil k/3\rceil\). The two projective maps are

\[
 f_B(r)=\frac{2+4r}{3+2r},\qquad
 f_A(r)=\frac{1+3r}{3+r},
\]

with \(A\) allowed only at even inputs. Outputs of \(B,A\) are
even, odd respectively. For either allowed common branch,

\[
 f_C(r)-f_C(s)=\frac{8(r-s)}{h_C(r)h_C(s)},
 \quad h_B(r)=3+2r,\quad h_A(r)=3+r.
\]

Both denominators are units. Iterating along one admissible word of
length \(m\) makes its endpoint constant modulo \(2^k\) over its
allowed input set. Its contribution to \(T_{\chi,k}^m\) is therefore
of the form \(F\mapsto c_w(r)F(r_w)\), with zero values at disallowed
inputs, and has rank at most one. The character weight may depend on
\(r\); this does not change that rank assertion.

The number of **linear**, not cyclic, binary words of length \(m\)
without consecutive \(AA\) is \(F_{m+2}\), where \(F_1=F_2=1\).
Indeed the counts satisfy the Fibonacci recurrence with values 1 and 2
at lengths 0 and 1. Thus

\[
 \operatorname{rank}(T_{\chi,k}^m)\le F_{m+2}.                 \tag{1}
\]

On the direct sum of all generalized nonzero eigenspaces, \(T^m\)
is invertible. Its dimension, the total algebraic multiplicity of
nonzero eigenvalues, is consequently at most \(\operatorname{rank}T^m\).
This argument does not assume diagonalizability or normality.

## 2. The actual finite spectral measure

For an eigenvalue \(\xi\) of \(T_{\chi,k}/\varphi\), let
\(d_{\chi,k}(\xi)\) be its algebraic multiplicity. Define

\[
 \mu=\sum_{k\ge1}\frac{2^{-k}}{|U_k|}
       \sum_{\chi\in\widehat U_k}\sum_{\xi\ne0}
                           d_{\chi,k}(\xi)\delta_\xi.       \tag{2}
\]

All coefficients are positive; coincident atoms are added. By (1),

\[
 \mu(\overline{\mathbb D})\le
 \sum_{k\ge1}2^{-k}F_{\lceil k/3\rceil+2}
 =7\sum_{m\ge1}\frac{F_{m+2}}{8^m}=\frac{119}{55}.           \tag{3}
\]

For the middle equality group \(k=3m-2,3m-1,3m\).
The last equality uses
\(\sum_{m\ge1}F_{m+2}t^m=(2t+t^2)/(1-t-t^2)\) at \(t=1/8\).
In particular, the weighted matrix dimensions \(2^k\) do not need to
be summable; only their nonzero-spectrum multiplicities do.

For \(|u|<1\), the trace of a positive power is the sum of eigenvalue
powers with algebraic multiplicity, also for Jordan matrices. The
bound (3) permits all interchanges below and yields

\[
 \frac{a_n}{\varphi^n}=\int\xi^n\,d\mu(\xi),\qquad
 Q(u)=\int\frac{u\xi}{1-u\xi}\,d\mu(\xi),\qquad
 P(u)=-\int\log(1-u\xi)\,d\mu(\xi).                         \tag{4}
\]

The logarithm is the branch zero at \(u=0\), defined by its disk
power series. Uniform domination on \(|u|\le r<1\) follows from
\(r/(1-r)\) for the rational kernel and
\(\sum_{n\ge1}r^n/n\) for the logarithm.

For example the mass of the levels \(k>3M\) is at most

\[
 7\varphi\frac{(\varphi/8)^{M+1}}{1-\varphi/8},             \tag{5}
\]

using \(F_{m+2}\le\varphi^{m+1}\). This is a tail-mass bound, not
a bound on analytic continuation outside the disk, where denominators
may be small.

## 3. Removing the known characters, without overcounting coincident atoms

The accepted peripheral theorem identifies exactly those characters
trivial on the image of \(H=1+8\mathbb Z_2\). For such a character,
put \(\epsilon=\chi(-1)\in\{1,-1\}\). Its power traces are
\(\epsilon^n(\varphi^n+(-\varphi^{-1})^n)\). The nonzero
normalized spectrum is therefore precisely
\(\{\epsilon,-\epsilon\varphi^{-2}\}\), each with multiplicity
one. This follows either from finite Newton identities or the formal
log-determinant identity for these power traces.

The weighted multiplicities of \(\epsilon=1,-1\) are respectively
\(17/24,5/24\), as already obtained in round seven. They give the
submeasure

\[
 \mu_0=\frac{17}{24}(\delta_1+\delta_{-\varphi^{-2}})
       +\frac5{24}(\delta_{-1}+\delta_{\varphi^{-2}}).        \tag{6}
\]

Let \(\nu=\mu-\mu_0\). It is a positive measure because (6)
selects an actual subset of the terms in (2). Every remaining
character has all eigenvalues strictly inside the disk. Thus

\[
 \nu(S^1)=0,\qquad
 \nu(\overline{\mathbb D})\le\frac{119}{55}-\frac{11}{6}
 =\frac{109}{330}.                                         \tag{7}
\]

The interior weights in (6) are only **known contributions**, not
assertions of their full weights in \(\mu\): other characters could
give coincident interior eigenvalues. Substitution of (6) into (4)
gives four explicit rational terms for \(Q_0\), or four logarithms
for \(P_0\). The question for the remaining boundary points concerns
the entire remainder transform, not isolated summands.

## 4. A positive atomic cancellation counterexample

We construct a different measure \(\eta\), unrelated to the actual
AS1 spectra. Put \(a=e^{-8}\) and \(r_n=e^{-4/\sqrt n}\), so
\(0<a<r_1<r_2<\cdots<1\) and \(r_n\to1\). Start with
\(\eta_0=\delta_a\). Given \(\eta_{n-1}\), set

\[
 c_n=\int z^n\,d\eta_{n-1}(z).
\]

If \(c_n=0\), put \(w_n=0\) and make no addition. Otherwise let
\(\sigma_n\) be uniform probability on the \(n\) distinct roots of
\(z^n=-r_n^n c_n/|c_n|\), put \(w_n=|c_n|/r_n^n\), and define
\(\eta_n=\eta_{n-1}+w_n\sigma_n\). Uniform root averaging gives

\[
 \int z^j\,d\sigma_n=0\quad(1\le j<n),\qquad
 \int z^n\,d\sigma_n=-r_n^n c_n/|c_n|.
\]

Thus the new positive mass cancels the \(n\)th moment without
changing previously cancelled moments. Later shells also leave those
moments unchanged.

### Summability, not a merely formal construction

A shell \(\sigma_j\) contributes to the \(n\)th moment only when
\(j\mid n\), and that contribution has modulus \(r_j^n\). Hence

\[
 w_n\le(a/r_n)^n+
 \sum_{j\mid n,\,j<n}w_j(r_j/r_n)^n.                        \tag{8}
\]

The first term is \(e^{-8n+4\sqrt n}\le e^{-4n}\).
Writing \(n=mj\) with \(m\ge2\), the ratio is

\[
 (r_j/r_{mj})^{mj}=e^{-4\sqrt j(m-\sqrt m)}\le e^{-m},      \tag{9}
\]

since \(\sqrt m\le3m/4\) for every integer \(m\ge2\).
For \(W_N=\sum_{n=1}^Nw_n\), summing (8) and (9) gives

\[
 W_N\le A+BW_N,\qquad
 A=\frac1{e^4-1},\quad B=\sum_{m\ge2}e^{-m}
 =\frac1{e(e-1)}<1.
\]

It follows that \(\sum_nw_n\le A/(1-B)<\infty\). Therefore
\(\eta=\delta_a+\sum_{n\ge1}w_n\sigma_n\) is a finite positive
atomic measure, with no atom at zero or on \(S^1\). Dominated
convergence now justifies the construction's promised identities

\[
 \int z^j\,d\eta(z)=0\qquad(j\ge1).                        \tag{10}
\]

### Every boundary point is an accumulation point

Infinitely many \(w_n\) are nonzero. Otherwise the measure would
have finite support \(z_1,\ldots,z_s\), none equal to zero. The
polynomial \(g(z)=\prod_{i=1}^s(1-z/z_i)\) would vanish on its
support but satisfy \(g(0)=1\). Equation (10) would then give
\(0=\int g\,d\eta=\eta(\mathbb C)>0\), a contradiction.

Along the resulting unbounded sequence of positive shells, each shell
consists of an entire rotated regular \(n\)-gon of radius \(r_n\).
Every unit complex number is within angular distance \(\pi/n\) of
one of those atoms; their radii tend to one. Every point of \(S^1\)
is therefore an accumulation point of atoms with strictly positive mass.

Nonetheless (10), summability and the geometric series show that

\[
 R(u)=\int\frac{uz}{1-uz}\,d\eta(z)=0\qquad(|u|<1).         \tag{11}
\]

It extends to the entire zero function. Each individual atomic
summand has a pole at \(u=1/z\) outside the disk, and these formal
pole locations accumulate at every boundary point. They do not
prevent continuation of the inner sum. Equivalently, each summand of
\(R(u)/u\) has negative real residue equal to minus its positive
mass; that same-sign residue observation does not rescue the inference.
One must not identify the atomwise exterior representation, across its
accumulation barrier, with continuation of the function defined inside.

Averaging \(\eta\) with its pushforwards under conjugation,
\(z\mapsto-z\), and their composition gives the same example with
both real-conjugate and sign symmetry. Those symmetries preserve
positivity, (10), finite mass and full boundary accumulation.

## 5. Exact outcome and remaining obligation

The actual AS1 logarithmic derivative has the finite measure (2).
This improves the representation and controls its level tails inside
the disk. But even dense support accumulation, **if later proved for
that measure**, would not by itself settle continuation: (11) disproves
the proposed generic positivity argument.

The example has not been made to satisfy the arithmetic/Galois and
transfer-operator constraints of the actual spectra; it is not a
counterexample to AS1. Additional structure-specific noncancellation,
or an actual all-depth trace continuation theorem, is still needed.
The separately authored [spectral probe](../solenoid_spectral_probe/PROOF_PACKAGE.md)
concerns growing full-space resolvent norms and nilpotent memory, not
a proof of support accumulation for (2).

The original exponentiated zeta, native based-word clock and the two
accepted real singularities are unchanged. There is no full-circle
result, new admission, formal evaluation, manuscript, A2 promotion,
target Euler factor or root number. Mathematical executions and Git
writes in this lane: zero.
