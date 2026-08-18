# Source Lock — Dyadic-Sum Hankel System

## Candidate identity

- Candidate: `SD-C48`
- Paper position: Paper 46
- Family: countable arithmetic symbolic dynamics / weighted adjacency
- Portable namespace: `papers/46-dyadic-sum-hankel-cycle-calculus/preauthority`
- Phase-2 parent seal: `d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181`

## Frozen phase space and dynamics

Let $G_2$ be the undirected looped graph with vertex set $\mathbb N$ and

$$
m\sim n\iff m+n=2^a\quad\text{for some integer }a\ge1.
$$

The symbolic source is the one-sided countable edge shift

$$
X_{G_2}=\{(n_j)_{j\ge0}:n_j\sim n_{j+1}\},
$$

with left shift.  A primitive object is a cyclic vertex word of least edge
period $r$; repetition is temporal traversal of that same cyclic word.  The
clock is one edge and the formal marker $z$ records one edge.

## Frozen weight and operator

For complex $s$ define the symmetric matrix

$$
H_s(m,n)=\mathbf 1_{\{m+n=2^a\}}(mn)^{-s/2}.
$$

The branch $n^{-s/2}=\exp[-(s/2)\log n]$ uses the real logarithm.  If
$s=\sigma+it$, diagonal unitary factors show that singular values and ideal
membership depend only on $\sigma$.

The operator acts on the fixed Hilbert space $\ell^2(\mathbb N)$.  No finite
cutoff, alternate vertex measure, loop deletion, or changed exponent is an
equivalent source.

## Valuation block lock

Every legal edge satisfies $v_2(m)=v_2(n)$.  Writing $m=2^ku$, $n=2^kv$
with $u,v$ odd gives

$$
H_s\cong\bigoplus_{k\ge0}2^{-ks}A_s,
$$

where $A_s$ is the odd-vertex block.  This decomposition is an exact unitary
equivalence, not an asymptotic model.

## Determinant convention

- For $\sigma>1$, $H_s$ is trace class and the ordinary Fredholm determinant
  $\det(I-zH_s)$ is legal.
- For $\sigma>1/2$, $H_s\in S_2$ and
  $\det_2(I-zH_s)$ is legal.
- In the latter region,
  $$
  \log\det_2(I-zH_s)
  =-\sum_{r\ge2}\frac{z^r}{r}\operatorname{Tr}(H_s^r)
  $$
  first holds near zero and determines the entire regularized determinant.
- No determinant is used outside its ideal domain.

## Allowed evidence

- exact integer arithmetic and powers of two;
- valuation decomposition and finite/infinite series estimates;
- Schatten ideal and Fredholm determinant definitions;
- primary Peller, Fournier--Wagner, Guo, and Alekseyev sources as ownership
  boundaries;
- direct finite cutoffs only as theorem checks;
- the sealed Phase-2 claim/source/DA package.

## Forbidden moves

- replacing $m+n=2^a$ by square sums, arbitrary lacunary sets, or a fitted
  support while retaining the same candidate ID;
- deleting the loop at $1$ without declaring a changed source;
- claiming $S_q$ thresholds for $q\ne1,2$;
- treating edge labels as new primitives rather than constraints on a closed
  vertex cycle;
- calling $H_s$ self-adjoint when $s$ is nonreal;
- interpreting a cutoff eigenvalue as an infinite determinant zero;
- treating the power $2$ as an emergent rational-prime selector;
- importing target zeros or fitting any parameter.

## Exact claim boundary

The strongest authorized theorem is the exact $0,1/2,1$ phase diagram,
$v_2$ direct sum, legal trace/determinant factorization, and complete
odd/even solution criterion for cyclic equations $n_i+n_{i+1}=2^{a_i}$.
