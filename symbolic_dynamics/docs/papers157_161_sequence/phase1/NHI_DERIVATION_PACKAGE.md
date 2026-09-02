# Derivation Package — Newton--Hensel dynamics modulo $2^n$

## Target

Derive the complete finite-dynamical atlas of

\[
F_n(x)=3x^2-2x^3\pmod {2^n}
\]

on all residue classes, with an exact temporal law and a logically
independent every-target one-step inverse law.

## Status

**COHERENT AS STATED.** The literal polynomial and its quadratic
idempotent-lifting role are owned background. The residual target is the
finite atlas, especially normalized-unit image strata and nonuniform fibres.

## Invariant Object

The organizing object is the **parity-selected idempotent error**

\[
e(x)=
\begin{cases}
x,&x\equiv0\pmod2,\\
1-x,&x\equiv1\pmod2.
\end{cases}
\]

Its truncated $2$-adic valuation controls time. Its normalized odd unit
after one update controls image membership and fibre size. These are two
different coordinates of the same literal error and are not interchanged
silently.

## Assumptions

- $n\ge1$ is fixed and all congruences for states are modulo $2^n$.
- For a residue $a$, $v_2(a)=n$ means $a=0\pmod {2^n}$; otherwise it
  is the usual valuation in $\{0,\ldots,n-1\}$.
- A nonendpoint even source is written uniquely as $x=2^v u$, with
  $1\le v<n$ and $u$ odd modulo $2^{n-v}$.
- Exact enumeration is a falsification control, not a proof premise.

## Notation

- $F=F_n$ when $n$ is fixed.
- $\tau_n(x)$ is the first time $F^t(x)\in\{0,1\}$.
- $M_n=\lceil\log_2 n\rceil$, with $M_1=0$.
- In a nonzero even output stratum, $v_2(y)=2v$ and $N=n-2v$.
- $h_v(u)=u^2(3-2^{v+1}u)$ on odd residues modulo $2^N$.

## Derivation Strategy

First factor the errors at the two idempotents. This gives an exact
valuation recurrence and hence all temporal statistics. Then retain the
odd unit instead of discarding it: reduce the inverse problem to the map
$h_v$, prove its image is one congruence class modulo $8$, and prove a
four-to-one lifting lemma by splitting odd inputs into their two classes
modulo $4$. Finally reinsert the $2^v$ invisible high lifts and reflect
through $x\mapsto1-x$.

## Derivation Map

1. The identities $F(x)=x^2(3-2x)$ and
   $1-F(x)=(1-x)^2(1+2x)$ give exact error squaring.
2. Error squaring gives the pointwise clock; counting divisibility classes
   gives the temporal CDF and polynomial.
3. For even $x=2^v u$, factor $F(x)=2^{2v}h_v(u)$. This separates output
   valuation from normalized unit.
4. The normalized unit has one forced class modulo $8$. A two-branch
   lifting argument proves that every element of that class occurs four
   times modulo $2^N$ for $N\ge3$.
5. Reduction from $u\pmod {2^{n-v}}$ to $u\pmod {2^N}$ adds a factor
   $2^v$ to every nonzero target fibre.
6. Endpoint fibres arise from $2v\ge n$, and odd targets follow by exact
   reflection symmetry.

## Main Derivation

### Step 1 — exact error factorization (identity)

Direct expansion gives

\[
F(x)=x^2(3-2x),\qquad
1-F(x)=(1-x)^2(1+2x),\qquad
F(1-x)=1-F(x).
\]

If $x$ is even then $3-2x$ is odd; if $x$ is odd then $1-x$ is even and
$1+2x$ is odd. Therefore

\[
v_2(e(F(x)))=\min\{n,2v_2(e(x))\}.
\]

This is an identity in the truncated valuation convention, not an
approximation to $2$-adic convergence.

### Step 2 — pointwise time and temporal census (proposition)

For $e(x)\ne0$, iteration yields

\[
v_2(e(F^t(x)))=\min\{n,2^t v_2(e(x))\}.
\]

Thus

\[
\tau_n(x)=\min\{t\ge0:2^t v_2(e(x))\ge n\}.
\]

At time $t$, the required initial divisibility is $2^{a_t}\mid e(x)$,
where $a_t=\lceil n/2^t\rceil$. There are $2^{n-a_t}$ even residues
satisfying this around $0$, and equally many odd residues around $1$.
Hence

\[
A_{n,t}:=\#\{x:\tau_n(x)\le t\}
=2^{n-\lceil n/2^t\rceil+1}.
\]

The exact temporal polynomial is therefore

\[
D_n(z)=A_{n,0}+\sum_{t=1}^{M_n}
       (A_{n,t}-A_{n,t-1})z^t,
\qquad A_{n,0}=2.
\]

The largest time is $M_n=\lceil\log_2n\rceil$.

### Step 3 — valuation strata of the one-step image (identity)

For a nonzero even source $x=2^v u$, with $u$ odd,

\[
F(x)=2^{2v}h_v(u),\qquad
h_v(u)=u^2(3-2^{v+1}u).
\]

The factor $h_v(u)$ is odd. Thus a nonzero even image has valuation exactly
$2v<n$, and all even sources with $2v\ge n$ map to zero.

### Step 4 — the normalized odd-unit map (lemma)

Let $N\ge1$. On odd residues modulo $2^N$, the image of $h_v$ is:

- the unique odd class modulo $2$, when $N=1$;
- the class $3\pmod4$, when $N=2$;
- the class $7\pmod8$, when $N\ge3$ and $v=1$;
- the class $3\pmod8$, when $N\ge3$ and $v\ge2$.

For $N=1,2$, every target in the displayed singleton image has
$2^{N-1}$ preimages. For $N\ge3$, every target in the displayed class
has exactly four preimages.

The surjective/fibre assertion for $N\ge3$ comes from writing odd $u$ as
$u=r+4z$, $r\in\{1,3\}$. Within either branch, the quotient of
$h_v(r+4z)-h_v(r)$ by $8$ toggles its next binary output bit whenever
the next binary input bit of $z$ is toggled. Thus it is a permutation at
every truncated level. Each reduced $z$ has two lifts in the full domain,
and there are two $r$-branches, giving four preimages.

### Step 5 — every-target fibres (theorem consequence)

For $2v<n$, put $N=n-2v$. Reduction of an odd
$u\pmod {2^{n-v}}$ to modulo $2^N$ has $2^v$ lifts. Therefore each
admissible nonzero even target in stratum $2v$ has

\[
2^v\,2^{\min(N-1,2)}
=2^{v+\min(n-2v-1,2)}
\]

preimages. The zero fibre consists of even residues divisible by
$2^{\lceil n/2\rceil}$, so it has $2^{\lfloor n/2\rfloor}$ points.
Reflection gives the same statements around $1$.

The number of normalized targets in one nonzero even stratum is
$2^{\max(0,N-3)}$. Consequently

\[
|\operatorname{im}F_n|
=2+2\sum_{1\le v<n/2}2^{\max(0,n-2v-3)}.
\]

## Remarks and Interpretation

- The temporal law sees only the valuation of the error; the inverse law
  needs the normalized unit. This is why the second theorem is not a
  restatement of the clock.
- The classes $7\pmod8$ and $3\pmod8$ distinguish the first valuation
  stratum from every later one. Dropping this distinction gives false image
  claims already for $n=6$.
- The two endpoints are exchanged by $x\mapsto1-x$; no separate odd-side
  computation is needed.

## Boundaries and Non-Claims

- The polynomial $3x^2-2x^3$, idempotent lifting, and quadratic error
  improvement are owned background and receive zero contribution credit.
- No statement is made here for odd-prime moduli; modulo $2^n$, parity
  puts every state into one of the two lifting basins.
- No novelty or priority claim follows from the bounded owner search.
- Exact replay through $n=16$ supplies counterexample pressure only.

## Open Risks

- The only delicate proof point is the bit-lifting permutation lemma for
  $h_v$; it is written in full in NHI_PROOF_PACKAGE.md.
- A later manuscript must state the $N=1,2$ truncations explicitly rather
  than applying the four-to-one formula outside its range.
