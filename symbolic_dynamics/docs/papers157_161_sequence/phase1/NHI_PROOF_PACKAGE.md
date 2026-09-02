# Proof Package — Newton--Hensel finite atlas

## Claim

For every $n\ge1$, the map

\[
F_n(x)=3x^2-2x^3\pmod {2^n}
\]

has exactly the two recurrent points $0,1$. Its pointwise entry time, all
temporal shells, complete one-step image, and every-target fibres are the
formulas stated in NHI_DERIVATION_PACKAGE.md.

## Status

**PROVABLE AS STATED.** The claim survives unchanged, including the small
quotient cases $n-2v=1,2$.

## Assumptions

- $n\ge1$.
- States and targets are residue classes modulo $2^n$.
- The truncated convention is $v_2(0\pmod {2^n})=n$.

## Notation

- $e(x)=x$ for even $x$, and $e(x)=1-x$ for odd $x$.
- $h_v(u)=u^2(3-2^{v+1}u)$.
- In a nonzero even target stratum, $v_2(y)=2v$ and $N=n-2v$.

## Proof Strategy

Factor the two endpoint errors to prove the temporal statement. For the
inverse statement, separate valuation and odd unit, then prove a finite
lifting lemma for $h_v$ by two residue branches modulo $4$. Count the
forgotten high bits and use reflection.

## Dependency Map

1. The temporal theorem depends only on the two exact error factorizations.
2. The image theorem depends on valuation separation and Lemma 1 below.
3. Lemma 1 depends on a Taylor-difference congruence whose derivative has
   valuation exactly one on odd inputs.
4. Fibre sizes add the reduction multiplicity $2^v$; endpoint sizes use a
   direct divisibility count.
5. Recurrence follows from finite-time absorption, so no independent cycle
   classification is assumed.

## Proof

### Step 1 — symmetry and exact valuation doubling

Direct multiplication gives

\[
F_n(x)=x^2(3-2x),\qquad
1-F_n(x)=(1-x)^2(1+2x).
\]

It also gives $F_n(1-x)=1-F_n(x)$. If $x$ is even, $3-2x$ is odd; if
$x$ is odd, $1-x$ is even and $1+2x$ is odd. Therefore

\[
v_2(e(F_n(x)))=\min\{n,2v_2(e(x))\}.
\]

Induction on $t$ yields

\[
v_2(e(F_n^t(x)))=\min\{n,2^t v_2(e(x))\}.
\]

The parity of $F_n(x)$ equals the parity of $x$, so the endpoint reached is
$0$ for even $x$ and $1$ for odd $x$. The least entry time is the least
$t$ with $2^t v_2(e(x))\ge n$.

At time $t$, entry is equivalent to divisibility of the selected error by
$2^{a_t}$, where $a_t=\lceil n/2^t\rceil$. The even basin contributes
$2^{n-a_t}$ states and the odd basin contributes the same number. Thus

\[
A_{n,t}=2^{n-a_t+1}.
\]

Taking consecutive differences proves every temporal shell. Since every
nonendpoint error has initial valuation at least one, all states have entered
when $2^t\ge n$. Errors of valuation one show sharpness. Hence the maximum
is $\lceil\log_2 n\rceil$. Every state is eventually $0$ or $1$, and both
are fixed; therefore they are exactly the recurrent points.

### Step 2 — normalized-unit lemma

**Lemma 1.** Fix $v\ge1$ and define

\[
h_v(u)=u^2(3-2^{v+1}u)
\]

on odd residues modulo $2^N$.

For $N=1$, its image is the unique odd class and that class has one
preimage. For $N=2$, its image is $3\pmod4$ and that class has two
preimages. For $N\ge3$, its image is $7\pmod8$ when $v=1$, and
$3\pmod8$ when $v\ge2$; every target in the relevant class has exactly
four preimages.

**Proof of Lemma 1.** For odd $u$, $u^2\equiv1\pmod8$. If $v=1$,
$2^{v+1}u=4u\equiv4\pmod8$, hence $h_v(u)\equiv7\pmod8$. If $v\ge2$,
the cubic term is divisible by $8$, hence $h_v(u)\equiv3\pmod8$. Reduction
gives the asserted images for $N=1,2$.

It remains to prove surjectivity and fibre size for $N\ge3$. Partition the
odd residues by $u\equiv r\pmod4$, where $r\in\{1,3\}$, and write

\[
u=r+4z.
\]

The variable $z$ ranges modulo $2^{N-2}$. Define the integer-valued
function

\[
\Phi_{v,r}(z)=\frac{h_v(r+4z)-h_v(r)}8.
\]

The numerator is divisible by $8$, since all odd inputs have the same
$h_v$-value modulo $8$. We show that the reduction of $\Phi_{v,r}$ modulo
$2^k$ is a permutation for every $k\ge0$.

For odd $u$, differentiation in $\mathbb Z[u]$ gives

\[
h_v'(u)=6u(1-2^v u),
\]

so $v_2(h_v'(u))=1$. Also

\[
h_v''(u)=6-6\cdot2^{v+1}u
\]

has valuation one, while $h_v'''(u)=-6\cdot2^{v+1}$ has valuation at least
$v+2\ge3$.

Let $j\ge0$, let $u=r+4z$, and set
$\delta=4\cdot2^j=2^{j+2}$. The exact cubic Taylor identity gives

\[
\frac{h_v(u+\delta)-h_v(u)}8
=\frac{\delta h_v'(u)}8
+\frac{\delta^2 h_v''(u)}{16}
+\frac{\delta^3 h_v'''(u)}{48}.
\]

The first term is $2^j$ times an odd integer. The second term has valuation
at least $2j+1\ge j+1$. The third term has valuation at least
$3j+5\ge j+1$. Consequently

\[
\Phi_{v,r}(z+2^j)-\Phi_{v,r}(z)
\equiv2^j\pmod {2^{j+1}}. \tag{1}
\]

Start with the unique class modulo $1$. If
$\Phi_{v,r}\pmod {2^j}$ is a permutation, the two lifts $z$ and
$z+2^j$ of an input class have outputs that agree modulo $2^j$ and, by
(1), differ modulo $2^{j+1}$. They therefore hit the two lifts of the old
output exactly once. Induction proves the permutation assertion.

Take $k=N-3$. The value of $h_v(r+4z)\pmod {2^N}$ is determined by
$\Phi_{v,r}(z)\pmod {2^{N-3}}$, and the permutation assertion makes this
branch surjective onto the required congruence class modulo $8$. The domain
$z\pmod {2^{N-2}}$ contains two lifts of every class modulo
$2^{N-3}$. Thus each of the two branches $r=1,3$ supplies two preimages of
every target. The total is four. This proves Lemma 1. $\square$

### Step 3 — even image and fibres

Let $x$ be a nonzero even source and write $x=2^v u$, with $u$ odd. Then

\[
F_n(x)=2^{2v}h_v(u).
\]

If $2v\ge n$, the output is zero. Conversely, $F_n(x)=0$ implies
$2v\ge n$ because $h_v(u)$ is odd. Thus the zero fibre is precisely the
set of multiples of $2^{\lceil n/2\rceil}$, and it has

\[
2^{n-\lceil n/2\rceil}=2^{\lfloor n/2\rfloor}
\]

elements.

Suppose $2v<n$ and put $N=n-2v$. Lemma 1 characterizes exactly the possible
normalized units of a target of valuation $2v$. The odd unit $u$ in a source
is initially specified modulo $2^{n-v}$, whereas $h_v(u)\pmod {2^N}$ depends
only on $u\pmod {2^N}$. Reduction has

\[
2^{(n-v)-N}=2^v
\]

lifts. Lemma 1 supplies $2^{\min(N-1,2)}$ reduced solutions. Hence each
admissible target in this stratum has

\[
2^{v+\min(N-1,2)}
=2^{v+\min(n-2v-1,2)}
\]

even predecessors, and inadmissible targets have none.

For $N\ge3$, fixing a unit modulo $8$ leaves $2^{N-3}$ normalized targets.
For $N=1,2$, there is one. Thus the stratum has
$2^{\max(0,N-3)}$ targets.

### Step 4 — reflection and total image

The exact identity $F_n(1-x)=1-F_n(x)$ is a bijection from even sources to
odd sources and from an even target $y$ to $1-y$. It transfers the complete
even-side image and all its fibre sizes to the odd side. The two sides are
disjoint by parity. Adding the two endpoints and both copies of each
nonzero stratum gives

\[
|\operatorname{im}F_n|
=2+2\sum_{1\le v<n/2}2^{\max(0,n-2v-3)}.
\]

All claimed temporal, image, and fibre statements now follow. $\square$

## Corrections or Missing Assumptions

- None. The small cases $N=1,2$ must remain separate in any compressed
  paper statement.

## Open Risks

- The Taylor display is an exact cubic expansion, not an asymptotic Taylor
  formula.
- Owner subtraction must continue to assign zero credit to the standard
  idempotent-lifting polynomial and quadratic error improvement.
