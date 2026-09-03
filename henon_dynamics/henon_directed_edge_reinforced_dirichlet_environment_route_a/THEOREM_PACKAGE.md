# Proof package

## Claim

Let \(G=(V,E)\) be a finite strongly connected directed multigraph in which
every vertex has at least one outgoing labelled arc. Loops and distinctly
labelled parallel arcs are allowed. Give every arc \(e\) a weight
\(\alpha_e>0\), put \(\alpha_v=\sum_{e:e^-=v}\alpha_e>0\), and freeze
\(X_0=x_0\). After \(t\) steps let \(N_e(t)\) be the traversal count of
labelled arc \(e\), and let \(N_v(t)=\sum_{e:e^-=v}N_e(t)\). The directed
edge-reinforced walk chooses an outgoing arc \(e\) from \(v=X_t\) with
probability
\[
 \frac{\alpha_e+N_e(t)}{\alpha_v+N_v(t)}.                 \tag{1}
\]

For every legal arc path \(\gamma=(e_1,\ldots,e_m)\),
\[
 \mathbb P(\gamma)=\prod_{v\in V}
 \frac{\prod_{e:e^-=v}(\alpha_e)_{N_e(\gamma)}}
      {(\alpha_v)_{N_v(\gamma)}}.                        \tag{2}
\]
Here \((a)_r=a(a+1)\cdots(a+r-1)\). Consequently the order of departures
from each fixed vertex matters only through its labelled arc counts.

Independently for every \(v\), sample
\[
 \omega(v,\cdot)\sim
 \operatorname{Dirichlet}\bigl((\alpha_e)_{e^-=v}\bigr). \tag{3}
\]
Conditional on \(\omega\), choose the labelled outgoing arc \(e\) with
probability \(\omega_e\). The annealed law of this random-environment chain is
exactly the reinforced law at every finite time. After observing \(\gamma\),
the rows remain independent and
\[
 \omega(v,\cdot)\mid\gamma\sim
 \operatorname{Dirichlet}\bigl((\alpha_e+N_e(\gamma))_{e^-=v}\bigr). \tag{4}
\]
In particular, (1) is the posterior predictive mean.

Almost surely every vertex is visited infinitely often and
\[
 \frac{N_e(t)}{N_{e^-}(t)}\longrightarrow\omega_e,\qquad
 \frac{N_v(t)}t\longrightarrow\pi_\omega(v),\qquad
 \frac{N_e(t)}t\longrightarrow\pi_\omega(e^-)\omega_e,  \tag{5}
\]
where \(\pi_\omega\) is the unique stationary distribution of the finite
irreducible vertex kernel
\(K_\omega(v,w)=\sum_{e:v\to w}\omega_e\). Thus the limiting transition rows
are independent Dirichlet rows. For arcs \(e,f\) leaving \(v\),
\[
\begin{aligned}
 \mathbb E\omega_e&=\frac{\alpha_e}{\alpha_v},\\
 \operatorname{Var}(\omega_e)&=\frac{\alpha_e(\alpha_v-\alpha_e)}
   {\alpha_v^2(\alpha_v+1)},\\
 \operatorname{Cov}(\omega_e,\omega_f)&=-\frac{\alpha_e\alpha_f}
   {\alpha_v^2(\alpha_v+1)}\quad(e\ne f).                \tag{6}
\end{aligned}
\]
Coordinates in different rows are independent.

## Status

PROVABLE AS STATED.

## Assumptions and notation

- Arc labels, including labels of parallel arcs, are observable and retained.
- Counts are departure-arc counts; no arrival count enters (1).
- Every \(\alpha_e\) is strictly positive and \(G\) is finite and strongly
  connected.
- Every vertex has nonempty outgoing arc set. In particular, a one-vertex
  graph must have at least one labelled loop.
- The process \(X_t\) alone is generally not Markov before conditioning;
  \((X_t,(N_e(t))_e)\) is its augmented state.

## Proof strategy and dependency map

1. Multiply (1) along a path and group factors by departure vertex.
2. Evaluate the independent Dirichlet monomial moments and compare with (2).
3. Multiply the Dirichlet density by the observed path monomial to identify
   the posterior row by row.
4. Condition on the sampled positive environment; strong connectivity gives a
   finite irreducible Markov chain, to which the ergodic theorem applies.
5. Divide edge-frequency limits by positive vertex-frequency limits.

## Proof

### 1. Exact path probability

At the \(r\)-th departure from \(v\), the denominator in (1) is
\(\alpha_v+r\). Whenever arc \(e\) is selected for the \(s\)-th time, its
numerator is \(\alpha_e+s\). Multiplying sequential probabilities and grouping
these factors gives precisely (2). This grouping is legitimate for every
legal path because each factor is indexed by the departure event that created
it. It also proves vertex-wise partial exchangeability: two legal paths with
the same start and the same labelled outgoing counts at every vertex have the
same probability.

### 2. Dirichlet mixture without an abstract representation theorem

For a Dirichlet vector with positive parameters
\((\alpha_1,\ldots,\alpha_d)\), direct integration of its density over the
simplex gives
\[
 \mathbb E\prod_{i=1}^d\omega_i^{n_i}
 =\frac{\Gamma(\sum_i\alpha_i)}{\Gamma(\sum_i\alpha_i+\sum_i n_i)}
  \prod_i\frac{\Gamma(\alpha_i+n_i)}{\Gamma(\alpha_i)}
 =\frac{\prod_i(\alpha_i)_{n_i}}{(\sum_i\alpha_i)_{\sum_i n_i}}. \tag{7}
\]
Given \(\omega\), the probability of the labelled path \(\gamma\) is
\(\prod_e\omega_e^{N_e(\gamma)}\). Independence of rows and (7) make its
expectation equal the right-hand side of (2). Thus every finite-dimensional
path law agrees, proving the exact annealed representation.

### 3. Posterior and prediction

The likelihood multiplies the prior density in row \(v\) by
\(\prod_{e:e^-=v}\omega_e^{N_e(\gamma)}\). Exponents therefore change from
\(\alpha_e-1\) to \(\alpha_e+N_e(\gamma)-1\), while the product over vertices
preserves row independence. Normalizing with (7) proves (4). Its mean is
\[
 \mathbb E[\omega_e\mid\gamma]
 =\frac{\alpha_e+N_e(\gamma)}{\alpha_v+N_v(\gamma)},
\]
which is exactly (1). Formula (6) follows from (7) with one or two unit
increments.

### 4. Almost-sure learning and occupation limits

Every coordinate of a positive-parameter Dirichlet vector is strictly positive
almost surely. Hence, for almost every \(\omega\), every arc of the strongly
connected source graph has positive conditional probability and
\(K_\omega\) is a finite irreducible stochastic matrix. It has a unique
stationary law with \(\pi_\omega(v)>0\) for every \(v\).

The finite-state Markov ergodic theorem, applied conditionally on this
\(\omega\), gives simultaneously for all vertices and labelled arcs
\[
 t^{-1}N_v(t)\to\pi_\omega(v),\qquad
 t^{-1}N_e(t)\to\pi_\omega(e^-)\omega_e
\]
with conditional probability one. Because the graph has finitely many
coordinates, the simultaneous event still has conditional probability one;
integrating over \(\omega\) makes it an annealed almost-sure event. Its first
limit is positive, so dividing the edge limit by the departure-vertex limit
proves the first assertion in (5). Positive limiting vertex frequency also
implies every vertex is visited infinitely often.

## Boundary closure

- If a vertex has one outgoing labelled arc, its Dirichlet row is the point
  mass at one and all formulas hold with a deterministic row.
- Parallel arcs are distinct coordinates in (2)--(7), although their
  probabilities are summed when forming the vertex kernel \(K_\omega\).
- One vertex with several labelled loops is exactly the classical finite-color
  Pólya urn; one loop is completely deterministic. The zero-loop singleton is
  excluded even if strong connectivity is defined vacuously, because
  \(\alpha_v=0\), the Dirichlet row and (1) would all be undefined.
- If strong connectivity is removed, the global conclusion in (5) is false:
  after the walk enters an eventual closed recurrent class, only rows visited
  infinitely often are learned, and unvisited rows retain their priors.
- Allowing \(\alpha_e=0\) changes the support and may permanently suppress an
  arc. Such parameters are outside the theorem, not limits silently included
  in it.

## Collision and claim boundary

C263 owns one global Pólya urn, not an endogenously visited family producing a
random Markov kernel and random occupation law. C181 is deterministic
rotor-routing. C338 samples fixed-conductance Wilson stacks rather than
reinforcing traversed arcs. Undirected ERRW uses a different mixing measure and
its magic formula is neither invoked nor claimed.

There is no arithmetic local data, Euler factor, root number, automorphy,
target divisor or functional equation, target zero match, Hilbert--Pólya
operator, or Route-B invocation.

## Open risks

The exact row-wise Dirichlet mixture depends simultaneously on directed arc
labels and linear reinforcement. Collapsing parallel arcs or replacing the
linear rule by another weight function changes the theorem.
