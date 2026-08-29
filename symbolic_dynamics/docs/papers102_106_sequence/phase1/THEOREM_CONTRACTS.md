# Frozen theorem contracts: P102--P106

## P102: cyclic group-algebra involution norms

For `A = F_q[C_n]`, with `n | (q-1)`, inversion involution `*`, and
`T(a)=aa*`, let `s=gcd(n,2)`, `o=(n+s)/2`, and write `q-1=2^a m` with `m`
odd.

The paper must prove:

1. Fourier block normal form: `z -> z^2` on self-inverse characters and
   `(u,v) -> (uv,uv)` on paired characters.
2. `Fix(T^k) = (1+gcd(2^k-1,q-1))^o` for every `k>=1`.
3. recurrent-core size `(m+1)^o` and sharp maximum transient depth
   `a + 1_{n>s}`.
4. exact cycle counts and Artin--Mazur zeta by Moebius inversion.
5. a carefully qualified rigidity statement using phase size, fixed sequence,
   and depth, with all small branches checked explicitly.

Routes: split Fourier/idempotent proof; literal cyclic convolution and reversal
control, including extension-field lanes.

## P103: double-adjugate matrix dynamics

For `d>=3`, `X=M_d(F_q)`, and `Psi(A)=adj(adj(A))`, set
`alpha=(d-1)^2` and `E_k=(alpha^k-1)/d`.

The paper must prove:

1. singular matrices enter zero in one step, while
   `Psi^k(A)=det(A)^E_k A` on `GL_d(F_q)`.
2. `Fix(Psi^k)=1+|SL_d(q)| gcd(E_k,q-1)`.
3. `|Im(Psi^k)|=1+|GL_d(q)|/gcd(alpha^k,q-1)`.
4. the recurrent-core size and sharp valuation stabilization time obtained from
   primes common to `alpha` and `q-1`.
5. exact cycle/zeta data, plus the registered alternating and third-period
   fixed-count anomalies.

Routes: Jacobi identity/determinant fibres/projective scalar lines; literal
minor/cofactor iteration and exhaustive small-field matrices.

## P104: monomial-toggle contraction cocycles

Let `0<a<1`, `D=diag(a,1)`, `S` swap the coordinates, `R=SD`, and choose `R`
iid with probability `q` and `D` with probability `1-q`.

The paper must prove:

1. the finite-word normal form
   `M_n=S^{J_n} diag(a^{U_n},a^{n-U_n})`.
2. the complete singular spectrum in terms of `Z_n=2U_n-n`, and the endpoint
   dichotomy at `q=0,1`.
3. for `0<q<1`, coincident quenched Lyapunov exponents `log(a)/2` and the
   folded-normal second-order law with variance `(1-q)/q`.
4. the exact generalized-Lyapunov exponent from the Perron root of the tilted
   two-state transfer matrix, and its strict annealed--quenched gap.

Routes: matrix-word induction plus Markov additive-functional theory; literal
word enumeration plus independent occupation DP/Cayley--Hamilton controls.

## P105: cycle-minimum pruning on permutations

For `pi in S_n`, simultaneously process each nontrivial cycle: remove its
least label from the cycle, splice predecessor to successor, and make that
label a singleton.  Existing singleton cycles stay fixed.

The paper must prove:

1. well-defined simultaneous surgery and the exact iterate of every cycle.
2. transient depth `tau(pi)=L(pi)-1`, where `L` is the longest cycle; the
   identity is the unique recurrent point and `zeta=(1-z)^-1`.
3. with `A_{n,k}` counting permutations with all cycles at most `k`,
   `A_{n,k}=n![z^n] exp(sum_{j<=k}z^j/j)` and the exact depth-`t` layer is
   `A_{n,t+1}-A_{n,t}`.
4. an independent recurrence through the cycle containing label `1`, sharp
   depth `n-1`, and deepest-layer size `(n-1)!`.

Routes: cycle-partition conjugacy; exponential formula and label-1 recurrence,
checked against literal permutation surgery through `n=9`.

## P106: synchronous MIS polarity dynamics

For a finite simple graph `G=(V,E)`, define
`F(A)={v in V : N(v) cap A is empty}` on `2^V`.

The paper must prove:

1. the polarity identity `F^3=F`; hence every orbit is periodic after at most
   one step and periods are only one or two.
2. fixed points are exactly maximal independent sets; points fixed by `F^2`
   are exactly the Galois-closed configurations.
3. if `m(G)` is the number of maximal independent sets and `c(G)` the number
   of closed configurations, then
   `zeta_F=(1-z)^-m (1-z^2)^-(c-m)/2`.
4. for every bipartite graph, `c(G)=m(G)^2`; consequently the number of
   two-cycles is `m(G)(m(G)-1)/2`.
5. for paths, `m_0=m_1=1`, `m_2=2`,
   `m_n=m_{n-2}+m_{n-3}`, yielding an explicit family zeta.

Routes: symmetric-relation Galois polarity and bipartite concept splitting;
literal bitset dynamics over exhaustive bipartite graphs and paths.
