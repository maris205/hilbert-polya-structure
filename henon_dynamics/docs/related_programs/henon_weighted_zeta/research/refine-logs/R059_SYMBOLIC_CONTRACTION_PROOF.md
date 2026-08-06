# R059 Symbolic Contraction Theorem

## Claim

Let

$$
H_6(x,y)=(1-6x^2-y,x)
$$

and let

$$
X_-=[-5/8,-1/3],\qquad X_+=[1/3,5/8],
$$
$$
Y_-=[-81/128,-5/16],\qquad Y_+=[5/16,81/128].
$$

For $s,t\in\{-,+\}$, set $N_{st}=X_s\times Y_t$, and let $A$ be

$$
A=\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}
$$

in the state order $(--,-+,+-,++)$. Define the full h-set survivor

$$
\Lambda_* = \bigcap_{k\in\mathbb Z} H_6^{-k}
\left(\bigcup_{s,t}N_{st}\right).
$$

Then the state-itinerary map is a topological conjugacy

$$
\pi:(\Lambda_*,H_6)\cong(\Sigma_A,\sigma),
$$

and consequently

$$
h_{\mathrm{top}}(H_6|_{\Lambda_*})
=h_{\mathrm{top}}(\sigma|_{\Sigma_A})
=\log\rho(A)
=\log\frac{1+\sqrt5}{2}.
$$

For every primitive cyclic $A$-word of length $n$, there is exactly one
primitive $H_6$-periodic orbit in $\Lambda_*$ with that itinerary.

## Status

**PROVABLE AS STATED.**

This is an exact analytic theorem on the explicitly defined four-h-set
union. It does not assert that the whole Hénon nonwandering set, the old
finite-grid filament, or the period-1--12 numerical catalog is globally
complete.

## Assumptions

1. The h-sets and adjacency matrix are exactly the rational objects above.
2. The R058 exact audit has proved that all listed $A$-edges are admissible and
   all other one-step state transitions are excluded.
3. The R058 cone certificate applies on the four h-sets. The contraction proof
   below supplies the coding and uniqueness statement; the cone certificate
   supplies uniform hyperbolicity.

## Notation

Write a sign as $\varepsilon_i\in\{-1,+1\}$, and identify the state
$w_i=(s_i,t_i)$ with the pair

$$
(\varepsilon_i,\varepsilon_{i-1})=(s_i,t_i).
$$

The closed sign box for a finite or bi-infinite sign sequence is

$$
K_\varepsilon=\prod_i X_{\varepsilon_i}
$$

with the sup norm. For an $A$-admissible state sequence, the graph relation
forces $t_i=s_{i-1}$, so this sign notation is unambiguous.

## Proof Strategy

The matrix $A$ is first translated into a local sign rule: the two neighbors
of every symbol may not both be positive. On each admissible sign box, solve
the second-order recurrence by the signed square-root operator

$$
(T_\varepsilon q)_i
=\varepsilon_i\sqrt{\frac{1-q_{i-1}-q_{i+1}}6}.
$$

The admissibility rule gives two rational radicand ranges. They imply that
$T_\varepsilon$ maps the sign box strictly into itself and has a uniform
sup-norm contraction constant $2/\sqrt{17}<1$. Banach's theorem gives a
unique fixed sequence for every one-sided, bi-infinite, or cyclic admissible
word. The fixed-point equation is exactly the Hénon recurrence. This yields
existence, uniqueness, period preservation, and the conjugacy. The R058 cone
certificate then supplies uniform hyperbolicity on the resulting survivor.

## Dependency Map

1. The explicit matrix $A$ is equivalent to the no-positive-neighbor-pair
   rule.
2. That rule gives the radicand bounds and strict self-mapping.
3. The derivative bound gives a contraction on every sign box, including the
   cyclic $n=1,2$ cases where the two neighbor indices coincide.
4. Banach gives one fixed sequence per admissible itinerary.
5. The recurrence identifies fixed sequences with Hénon orbits.
6. Disjoint h-sets give injectivity and a continuous inverse itinerary map.
7. Periodicity and primitivity are preserved.
8. Conjugacy gives exact entropy, while the R058 cone field gives uniform
   hyperbolicity.

## Proof

### Lemma 1: graph/sign equivalence

For a cyclic state path $w_i=(\varepsilon_i,\varepsilon_{i-1})$, an edge
$w_i\to w_{i+1}$ is $A$-allowed if and only if

1. the second sign of $w_{i+1}$ equals the first sign of $w_i$, and
2. $\varepsilon_{i-1}$ and $\varepsilon_{i+1}$ are not both $+1$.

**Proof.** The target-second-sign condition follows from the nonzero columns
of each row of $A$. The structurally possible edges are

$$
--\to --,+-,\qquad -+\to --,+-,
$$
$$
-\to -+,++,\qquad ++\to -+,++.
$$

The matrix deletes exactly $-+\to +-$, which has two positive neighbors
around the central negative symbol, and $++\to ++$, which has two positive
neighbors around the central positive symbol. The other six structural edges
are retained. This is precisely the stated rule. $\square$

### Lemma 2: rational radicand ranges

Suppose $q_{i-1},q_{i+1}$ lie in their prescribed sign intervals and are not
both positive. Then

$$
r_i=\frac{1-q_{i-1}-q_{i+1}}6
$$

lies in either

$$
\left[\frac5{18},\frac38\right]
\quad\text{(both neighbors negative),}
$$

or

$$
\left[\frac{17}{144},\frac{31}{144}\right]
\quad\text{(one neighbor of each sign).}
$$

In both cases

$$
\frac13<\sqrt{r_i}<\frac58.
$$

**Proof.** If both neighbors are negative, their sum belongs to

$$
[-5/8,-1/3]+[-5/8,-1/3]=[-5/4,-2/3],
$$

which gives the first interval. If one is positive and one negative, the sum
belongs to

$$
[1/3,5/8]+[-5/8,-1/3]=[-7/24,7/24],
$$

which gives the second interval. The endpoint comparisons are exact:

$$
\frac5{18}>\frac19,\qquad \frac38<\frac{25}{64},
$$
$$
\frac{17}{144}>\frac19,\qquad \frac{31}{144}<\frac{25}{64}.
$$

Taking positive square roots proves the strict inequalities. $\square$

### Lemma 3: strict self-mapping

For every $A$-admissible sign sequence, $T_\varepsilon$ maps
$K_\varepsilon$ into its coordinatewise interior.

**Proof.** Lemma 1 excludes the only case in which both neighbors are
positive. Lemma 2 gives $1/3<\sqrt{r_i}<5/8$. Multiplication by
$\varepsilon_i$ places the result strictly in $X_{\varepsilon_i}$. This
holds at every coordinate, so
$T_\varepsilon(K_\varepsilon)\subset\operatorname{int}K_\varepsilon$.
$\square$

### Lemma 4: uniform contraction

On every admissible sign box,

$$
\|T_\varepsilon q-T_\varepsilon q'\|_\infty
\le \frac2{\sqrt{17}}\|q-q'\|_\infty
<\|q-q'\|_\infty.
$$

**Proof.** On the radicand ranges of Lemma 2,

$$
\left|\frac{\partial}{\partial u}
\sqrt{\frac{1-u-v}6}\right|
=\frac1{12\sqrt{(1-u-v)/6}}
\le\frac1{\sqrt{17}},
$$

and the same bound holds for the $v$ derivative. The mean-value theorem
therefore gives, for each coordinate,

$$
|(T_\varepsilon q)_i-(T_\varepsilon q')_i|
\le\frac1{\sqrt{17}}
\bigl(|q_{i-1}-q'_{i-1}|+|q_{i+1}-q'_{i+1}|\bigr)
\le\frac2{\sqrt{17}}\|q-q'\|_\infty.
$$

For a cyclic word of length one or two, the two neighbor occurrences refer to
the same coordinate; their derivative contributions add, giving the same
coefficient $2/\sqrt{17}$, not a larger one. Since $4<17$, the coefficient is
strictly less than one. $\square$

### Lemma 5: one fixed orbit for every admissible itinerary

For every finite cyclic or bi-infinite $A$-admissible sign sequence there is
exactly one fixed point of $T_\varepsilon$ in $K_\varepsilon$.

**Proof.** A finite product of closed intervals and the bi-infinite product
with the sup metric are complete metric spaces. Lemma 3 gives self-mapping
and Lemma 4 gives a contraction with constant less than one. Banach's
fixed-point theorem gives existence and uniqueness. $\square$

### Lemma 6: fixed sequences are exactly Hénon orbits

If $q=T_\varepsilon q$, then

$$
q_{i+1}=1-6q_i^2-q_{i-1}
$$

and $z_i=(q_i,q_{i-1})$ satisfies $H_6(z_i)=z_{i+1}$, with
$z_i\in N_{\varepsilon_i,\varepsilon_{i-1}}$.

**Proof.** Squaring the fixed-point equation gives

$$
6q_i^2=1-q_{i-1}-q_{i+1},
$$

which rearranges to the recurrence. Lemma 3 ensures
$q_i\in X_{\varepsilon_i}$, and
$X_{\varepsilon_{i-1}}\subset\operatorname{int}Y_{\varepsilon_{i-1}}$, so
$z_i\in N_{\varepsilon_i,\varepsilon_{i-1}}$. The map identity follows by
substitution. $\square$

### Lemma 7: conjugacy on the full h-set survivor

The itinerary map $\pi:\Lambda_*\to\Sigma_A$ is a homeomorphism and

$$
\pi\circ H_6=\sigma\circ\pi.
$$

**Proof.** For an admissible bi-infinite state sequence, Lemma 1 recovers a
unique sign sequence and Lemmas 5--6 construct a point of $\Lambda_*$. This
defines a map $\Phi:\Sigma_A\to\Lambda_*$. If two symbolic sequences agree
on coordinates $[-m,m]$, the $m$-fold contraction estimate gives

$$
\|\Phi(\omega)_0-\Phi(\omega')_0\|_\infty
\le \frac54\left(\frac2{\sqrt{17}}\right)^m,
$$

because all $X_s$ have diameter at most $5/4$. Thus $\Phi$ is continuous in
the product topology. The same estimate applies after any fixed shift, so the
full point map is continuous.

Conversely, a point in $\Lambda_*$ has a unique state at every time because
the four h-sets are pairwise disjoint. Its scalar coordinates satisfy the
recurrence and hence are a fixed point of the corresponding
$T_\varepsilon$. Lemma 5 forces equality with the constructed sequence,
proving surjectivity of $\Phi$ and injectivity of the itinerary. A continuous
bijection from the compact space $\Sigma_A$ to the Hausdorff space
$\Lambda_*$ is a homeomorphism. The recurrence identity gives the conjugacy
relation. $\square$

### Lemma 8: period preservation

If a cyclic $A$-word has least period $n$, its constructed orbit has least
period $n$.

**Proof.** If the constructed scalar sequence had period $d<n$, its sign
sequence would also have period $d$, contradicting least period $n$. The
state itinerary has the same least period because the second sign is the
previous first sign. $\square$

### Conclusion

Lemma 7 proves the topological conjugacy. Lemma 8 gives the primitive
periodic-orbit bijection. The entropy of a finite-type subshift is the
logarithm of the spectral radius of its adjacency matrix. Since

$$
\det(\lambda I-A)=(\lambda^2-\lambda-1)(\lambda^2+1),
$$

the spectral radius is $\varphi=(1+\sqrt5)/2$, and the entropy equality
follows. The R058 cone certificate supplies uniform hyperbolicity on
$\Lambda_*$. $\square$

## Corrections or Missing Assumptions

No additional assumption is needed beyond the exact R058 h-set geometry,
allowed-edge graph, and cone certificate. The theorem is restricted to the
explicit four-h-set survivor $\Lambda_*$; it is not a statement about the
full Hénon map or any finite-grid SCC outside this domain.

## Open Risks

- The numerical period-1--12 catalog remains a separate finite-precision
  ledger. The contraction theorem supplies exact witnesses independently; it
  does not make the catalog a globally complete root census.
- The theorem does not identify the restricted smooth transfer operator with
  the cycle expansion in the continuous limit. That remains the R059 C2
  finite-resolution experiment.
