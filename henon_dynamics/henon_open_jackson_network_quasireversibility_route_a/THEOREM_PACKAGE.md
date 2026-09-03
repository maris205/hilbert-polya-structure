# Proof package

## Frozen model

Let \(V=\{1,\ldots,d\}\), \(d\ge1\). External customers arrive at node \(i\)
as independent Poisson processes of rates \(\alpha_i>0\). Node \(i\) has one
work-conserving exponential server of rate \(\mu_i>0\). After a completion at
\(i\), the customer moves to \(j\) with probability \(p_{ij}\ge0\), or leaves
the network with probability

\[
p_{i0}=1-\sum_{j=1}^d p_{ij}\ge0.
\]

The routing matrix \(P=(p_{ij})\) is substochastic and
\(\operatorname{spr}(P)<1\). Self-routing \(p_{ii}>0\) is allowed, but such a
completion is a phantom event for the queue-length vector. For
\(x\in\mathbb Z_+^d\), the visible generator therefore has transitions

\[
\begin{aligned}
x&\longrightarrow x+e_i &&\text{at rate }\alpha_i,\\
x&\longrightarrow x-e_i &&\text{at rate }\mu_i p_{i0}\mathbf1_{\{x_i>0\}},\\
x&\longrightarrow x-e_i+e_j &&\text{at rate }\mu_i p_{ij}\mathbf1_{\{x_i>0\}},
\quad i\ne j.
\end{aligned}
\tag{1}
\]

Vectors are rows. Thus the traffic convention is

\[
\lambda=\alpha+\lambda P,
\qquad
\lambda=\alpha(I-P)^{-1}.
\tag{2}
\]

## Main theorem

The process in (1) is nonexplosive and irreducible. Its traffic vector in (2)
exists, is unique, and is strictly positive. It is positive recurrent if and
only if

\[
\lambda_i<\mu_i\qquad(1\le i\le d).
\tag{3}
\]

When (3) holds, write \(\rho_i=\lambda_i/\mu_i\). The unique invariant
probability is

\[
\pi(x)=\prod_{i=1}^d(1-\rho_i)\rho_i^{x_i}.
\tag{4}
\]

The stationary time reversal is a Jackson network, in the natural extended
convention that permits zero exogenous rates, with the same service rates and
traffic vector and with

\[
\widehat\alpha_i=\lambda_i p_{i0},\qquad
\widehat p_{ji}=\frac{\lambda_i p_{ij}}{\lambda_j},\qquad
\widehat p_{i0}=\frac{\alpha_i}{\lambda_i}.
\tag{5}
\]

The forward model retains \(\alpha_i>0\) at every node. The first formula in
(5) may nevertheless vanish when node \(i\) has no direct external exit. The
reversed system is open in the stated extended convention and has the
displayed traffic vector.

In the two-sided stationary realization, let \(D_i\) be the point process of
customers that leave the whole network directly after service at node \(i\).
Then the \(D_i\) are jointly independent Poisson processes with respective
rates \(\lambda_i p_{i0}\). For every \(t\in\mathbb R\), the vector of restricted
histories

\[
\bigl(D_i\cap(-\infty,t]\bigr)_{i=1}^d
\]

is independent of \(X(t)\). No assertion is made that all internal routed arc
flows are jointly independent.

If \(\lambda_i\ge\mu_i\) for at least one \(i\), the irreducible chain is not
positive recurrent. This includes equality.

## Proof

### 1. Traffic, nonexplosion, and irreducibility

Because \(P\ge0\) and \(\operatorname{spr}(P)<1\),

\[
(I-P)^{-1}=\sum_{m=0}^{\infty}P^m.
\]

Equation (2) consequently has one solution and \(\lambda_i\ge\alpha_i>0\).
The total visible jump rate is bounded by
\(\sum_i\alpha_i+\sum_i\mu_i\), so explosion is impossible.

The spectral-radius condition implies that the routing chain is absorbed at
the outside state almost surely from every node. In particular, every node
has a positive finite route to an exit. Starting from any finite queue vector,
there is positive probability that no external arrival occurs while a finite
prescribed sequence of service marks sends every present customer outside.
Thus the zero vector is accessible. Since every \(\alpha_i>0\), prescribed
external arrivals take the zero vector to every queue vector with positive
probability. The chain is irreducible.

### 2. Full global balance and sufficiency

Assume (3), set \(E(x)=\{i:x_i>0\}\), and first omit the normalizing factors in
(4): \(w(x)=\prod_i\rho_i^{x_i}\). The visible rate out of \(x\) is

\[
q_{\mathrm{out}}(x)=\sum_i\alpha_i+
\sum_{j\in E(x)}\mu_j(1-p_{jj}).
\tag{6}
\]

Divide all incoming stationary mass rates by \(w(x)\). External departures
from predecessors \(x+e_i\) contribute

\[
\sum_i\rho_i\mu_i p_{i0}=\sum_i\lambda_i p_{i0}=\sum_i\alpha_i,
\tag{7}
\]

where the last equality is obtained by summing (2). For each occupied
destination \(j\), an external arrival from \(x-e_j\), together with all
internal routes \(i\to j\) from \(x+e_i-e_j\), contributes

\[
\frac{\alpha_j}{\rho_j}
+\frac1{\rho_j}\sum_{i\ne j}\lambda_i p_{ij}
=\frac{\lambda_j(1-p_{jj})}{\rho_j}
=\mu_j(1-p_{jj}).
\tag{8}
\]

Equations (7)--(8) reproduce (6), so \(wQ=0\) state by state. Since every
\(\rho_i<1\), multiplication by \(\prod_i(1-\rho_i)\) normalizes \(w\), proving
(4). An irreducible nonexplosive countable-state chain with an invariant
probability is positive recurrent, and that probability is unique.

### 3. Necessity, including the critical face

Conversely, suppose an invariant probability \(\nu\) exists. For an
irreducible conservative countable-state continuous-time Markov chain,
existence of an invariant probability implies positive recurrence, uniqueness
of that probability, and strictly positive mass at every state. This standard
lemma applies here because Step 1 proved irreducibility and bounded rates prove
conservativity. Define the stationary service-opportunity throughput

\[
\beta_i=\mu_i\nu\{x_i>0\}.
\]

For fixed \(i\), apply stationarity to
\(f_M(x)=\min\{x_i,M\}\). Its generator is uniformly bounded by the total
network event rate. For each fixed \(x\), \(Qf_M(x)\) converges as
\(M\to\infty\) to the ordinary coordinate drift. Dominated convergence gives

\[
0=\alpha_i+\sum_j\beta_jp_{ji}-\beta_i.
\tag{9}
\]

Thus \(\beta=\alpha+\beta P\). Uniqueness of the traffic solution yields
\(\beta=\lambda\), whence \(\lambda_i\le\mu_i\). If equality held for some
\(i\), then \(\nu\{x_i>0\}=1\). The lemma gives positive mass to the zero
vector, a contradiction. This makes every inequality strict. Hence a critical
or overloaded network cannot be positive recurrent.

### 4. Exact stationary reversal

For a stationary jump \(x\to y\), the reversed rate is
\(\widehat q(y,x)=\pi(x)q(x,y)/\pi(y)\). The three visible jump types give:

\[
\begin{array}{rcl}
x\to x+e_i&:&\widehat q(x+e_i,x)=\alpha_i/\rho_i
=\mu_i\widehat p_{i0},\\[2mm]
x\to x-e_i&:&\widehat q(x-e_i,x)=\rho_i\mu_i p_{i0}
=\widehat\alpha_i,\\[2mm]
x\to x-e_i+e_j&:&\widehat q(x-e_i+e_j,x)
=\mu_i p_{ij}\rho_i/\rho_j=\mu_j\widehat p_{ji}.
\end{array}
\tag{10}
\]

This proves the indices in (5). For every reverse source node \(j\),

\[
\widehat p_{j0}+\sum_i\widehat p_{ji}
=\frac{\alpha_j+\sum_i\lambda_i p_{ij}}{\lambda_j}=1.
\tag{11}
\]

Moreover,

\[
\widehat\alpha_i+\sum_j\lambda_j\widehat p_{ji}
=\lambda_i p_{i0}+\lambda_i\sum_jp_{ij}=\lambda_i,
\tag{12}
\]

so \(\lambda\) is also the reversed traffic vector. Because
\(\widehat p_{j0}=\alpha_j/\lambda_j>0\), the reversed routing matrix itself has
every row sum strictly below one and hence spectral radius below one.

### 5. External departure processes

Construct the stationary reversed Jackson network, allowing zero exogenous
rates, with independent exogenous Poisson streams of rates
\(\widehat\alpha_i=\lambda_i p_{i0}\). Equations (10)--(12) identify its
visible marked-jump law with the time reversal of the forward visible
marked-jump law. Phantom self-routing completions are state-preserving marks;
they may be restored with their same conditional rates and are irrelevant to
the external-departure assertion. A forward external departure at node \(i\)
and time \(s\le t\) becomes a reversed external arrival at time \(-s\ge-t\).
Future increments of the independent exogenous streams after reversed time
\(-t\) are jointly independent of the state at \(-t\). Returning to forward
time proves both the joint Poisson law and the asserted independence of past
departures from \(X(t)\). Notice that this argument does not turn internal
routed completions into mutually independent external clocks.

This completes the theorem.

## Boundary atlas

- **One node.** If \(p_{11}=0\), (4)--(5) are the ordinary stationary
  \(M/M/1\) law and Burke theorem. Feedback \(p_{11}>0\) gives
  \(\lambda=\alpha/(1-p_{11})\) and the same theorem with effective visible
  service rate \(\mu(1-p_{11})\).
- **No routing.** For \(P=0\), all queues and external departure streams are
  independent \(M/M/1\) systems.
- **Tandem/feed-forward routing.** Nilpotent \(P\) is included without a
  separate limit.
- **No direct exit from a node.** The theorem allows \(p_{i0}=0\); the
  spectral-radius hypothesis still supplies a finite positive route from that
  node to an exit. Its external departure stream is the zero-rate Poisson
  process.
- **Critical and overloaded loads.** Equality and strict overload both fail
  positive recurrence by Step 3, not by a divergent formal normalizer alone.

## Status and limits

**PROVABLE AS STATED.** The theorem excludes multiclass, non-exponential,
infinite-node, blocking, and state-dependent networks. It claims neither
transient/null-recurrent classification beyond failure of positive recurrence
nor joint independence of all internal arc flows.

The nearest workspace owner C285 is a closed fixed-population Gordon--Newell
network; C233 is an infinite-server immigration--death chain; C342 is a
directed reinforced walk. The present state space, mechanism, and output
history theorem are distinct.

The exact finite ledger is an implementation receipt. It does not prove the
infinite-state or point-process statements. There is no arithmetic origin,
primitive deterministic orbit ledger, dynamical zeta, target functional
equation, target Euler factor, root number, automorphy, target zero match,
Hilbert--Pólya operator, or Route-B invocation.
