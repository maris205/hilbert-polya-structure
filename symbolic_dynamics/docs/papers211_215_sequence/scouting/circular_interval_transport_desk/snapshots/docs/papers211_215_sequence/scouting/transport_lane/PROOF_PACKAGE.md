# UUC — bounded author proof package

Status: author deductions for negative scouting; no independent review,
no finite scientific execution, no sharp-clock or novelty claim.
The literal map and full parameter conventions are in
[INTAKE.md](INTAKE.md). Every index below is cyclic.

## 1. Closure and hereditary zero sites

For every i, g_i is either zero or one and g_i <= x_i. Therefore
(Tx)_i = x_i-g_i+g_{i-1} >= 0. Summing cancels the two current sums, so
T preserves N and maps X_{n,N} to itself.

If x_i=0, then g_i=0. Also g_{i-1}=1 would require
0<x_{i-1}<=x_i=0, a contradiction. Thus (Tx)_i=0.
Induction gives permanence of every existing zero. This elementary
support observation is not a new theorem axis.

## 2. Quadratic energy and all recurrent states

Set E(x)=sum_i x_i^2 and d_i=g_{i-1}-g_i. Expanding the squares and
shifting the index in the linear term gives the exact identity

\[
\begin{aligned}
E(Tx)-E(x)
 &=2\sum_i x_i(g_{i-1}-g_i)
       +\sum_i(g_{i-1}-g_i)^2\\
 &=2\sum_i g_i(x_{i+1}-x_i)
       +\sum_i(g_{i-1}-g_i)^2. \tag{1}
\end{aligned}
\]

Each summand in the first sum is nonnegative: an active current requires
x_i <= x_{i+1}; an inactive current contributes zero. The second sum is
also nonnegative.

Moreover, T(x)=x iff g_{i-1}=g_i for every i, equivalently the binary
current word is constant. When all currents vanish, x is fixed. When all
currents equal one, the cyclic chain 0<x_i<=x_{i+1} forces every coordinate
to have the same positive value, and x is again fixed. Conversely each
positive constant vector has all currents equal one and is fixed.

If x is not fixed, the cyclic binary current word is nonconstant.
There is at least one 0-to-1 and one 1-to-0 boundary. Thus the second
sum in (1) is at least two, and

\[
T(x)\ne x \quad\Longrightarrow\quad E(Tx)\ge E(x)+2. \tag{2}
\]

For n=1 no nonconstant current word is possible; the fixed classification
already includes every state. The boundary argument also applies for
n=2, where both transitions in a nonconstant two-letter current word
are counted.

Since E(x)<=N^2, (2) forces every orbit to reach a fixed state.
A nonconstant cycle would force a strict increase of E around the
cycle, which is impossible. Hence all recurrent states are fixed.

The fixed states can be restated without the currents:

1. a positive constant vector, possible only when n divides N; or
2. a vector for which every adjacent pair of positive entries satisfies
   x_i>x_{i+1} in the clockwise orientation.

The zero vector is included in case 2. A nonzero state in case 2 must
have a zero because an all-positive cyclic strict descent is impossible.
Its maximal positive runs are therefore strictly decreasing. The
positive constant states and case 2 are disjoint for N>0.

## 3. A crude time bound, explicitly not sharp

Let tau(x)=min{t>=0:T^{t+1}x=T^t x}. Before tau there are tau nonfixed
updates, each contributing at least two to E. Therefore

\[
\tau(x)\le \left\lfloor\frac{N^2-E(x)}2\right\rfloor. \tag{3}
\]

This is merely the range-of-potential bound. There is no claim of
attainment for each (n,N), no classification of maximizing trajectories,
and no evaluated sharp extremal clock. For example n=1 has tau=0
regardless of the potential argument. No finite boxes were run to fit
a sharper formula.

A further elementary consequence is that an all-positive nonuniform
state must eventually develop a zero. Indeed it eventually reaches a
fixed state. A positive constant target would have energy N^2/n,
whereas every nonuniform vector of mass N has strictly larger energy
by sum_i (x_i-N/n)^2>0; nondecreasing energy rules that target out.
The remaining fixed states contain zeros. This is still a consequence
of the same potential, not an independent temporal mechanism.

## 4. Exact general current-word inverse, with its value subtracted

For a target y in X_{n,N} and a cyclic binary word b in {0,1}^n define

\[
x_i(y,b)=y_i+b_i-b_{i-1}.
\]

Let B(y) be the set of binary words satisfying, at every i,

\[
x_i(y,b)\ge0,\qquad
b_i=\mathbf1_{\{0<x_i(y,b)\le x_{i+1}(y,b)\}}. \tag{4}
\]

Then b -> x(y,b) is a bijection from B(y) onto T^{-1}(y).

Proof: For an actual predecessor x, set b_i=g_i(x). The equation T(x)=y
rearranges to x_i=y_i+b_i-b_{i-1}, and (4) holds. Conversely, for a word
in B(y), telescoping shows sum_i x_i=N; nonnegativity gives x in X_{n,N}.
Condition (4) makes its actual current word equal b, so T(x)=y.
If two valid words yielded the same x, both would equal its uniquely
defined current word, hence would coincide. This proves the bijection.

In particular,

\[
|T^{-1}(y)|=\sum_{b\in\{0,1\}^n}\mathbf1_{\{b\in B(y)\}}. \tag{5}
\]

This identity is a complete finite decision description, but simply
rewrites the local current equations as a binary constraint problem.
The same reconstruction works for any deterministic cyclic binary-current
rule once its local validity predicate is substituted. No evaluated
global fibre maximum, rigidity of extremizers or special inverse
combinatorics has been extracted, so (5) is not promoted as a new inverse
axis.

For completeness, a positive constant target y=(c,...,c) has only itself
as predecessor. Its energy is N^2/n; every x of mass N has E(x)>=N^2/n,
while (1) requires E(x)<=E(y) for a predecessor. Equality in the variance
identity forces x=y. The zero target likewise has the unique mass-zero
predecessor. These special targets remain elementary consequences of
the potential and mass constraint.

## 5. What is and is not established

The above arguments hold for all n>=1,N>=0 directly, without empirical
support. They establish a generic recurrent classification and an exact
implicit fibre test for the literal map. They do not establish a
genuinely new two-axis theorem package, a sharp all-size clock, a closed
general fibre evaluation or externally unoccupied ownership.

That deficit is the reason for NO_PROMOTION. A mathematical statement
can be correct yet too generic to merit a paper seat. The proof is
preserved as negative evidence, not converted into manuscript acceptance.
