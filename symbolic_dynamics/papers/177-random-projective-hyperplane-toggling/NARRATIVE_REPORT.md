# Narrative report — random projective-hyperplane toggling

**Paper:** P177  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## One-sentence result

Uniformly toggling a nonzero binary projective hyperplane on the subset
carrier decomposes the entire chain into equal crown-graph walks, so its
every-time endpoint kernel, parity-phase convergence, and four-point global
spectrum all admit exact closed forms.

## Literal dynamics

Let `V = F_2^d`, with `d >= 2`, and let `E = V \ {0}`.  A state is a subset
`A of E`.  Independently at every epoch, choose a nonzero linear form `ell`
uniformly and update

```text
A <- A triangle H_ell,
H_ell = {x in E : ell(x)=0}.
```

Over `F_2`, nonzero forms and projective hyperplanes are in bijection.  The
zero form is not sampled.  Each sampled mask has `2^(d-1)-1` points and hence
odd size, a fact that forces period two.

## Claim spine

Write `q=2^d`, `N=q-1`, `m=N`, let `c_a=(a(x))_(x in E)` be the binary
simplex evaluation word, let `C={c_a}`, and put `W=<1,C>`.

1. The masks are `1+c_ell` and generate the `(d+1)`-dimensional space `W`.
   Thus the `2^m` states split into `K=2^(m-d-1)` closed classes of size
   `2q`; every state is recurrent.
2. In coordinates `epsilon 1+c_a <-> (epsilon,a)`, each class is the crown
   graph `K_(q,q)` with a perfect matching deleted.  The walk is regular of
   degree `N`, bipartite, irreducible, and period two.
3. If `L` is the sum of the `t` sampled nonzero forms, the endpoint increment
   is `(t mod 2)1+c_L`.  The exact ordered-history count is

   ```text
   a_t(0)   = q^(-1) [N^t + N(-1)^t],
   a_t(L!=0)= q^(-1) [N^t -   (-1)^t].
   ```

   This gives every time and every labelled target, including impossibility
   outside the unique parity-compatible simplex-code coset.
4. Against uniform measure on the current parity half, the exact total
   variation distance is `1/(q N^(t-1))` for `t>=1`.  This is phase
   convergence, not ordinary mixing.  Against uniform measure on the whole
   communicating class, ordinary TV is `1/2+1/(2q)` at `t=1` and exactly
   `1/2` for every `t>=2`.
5. On the entire carrier, the spectrum is `1,-1,1/N,-1/N` with
   multiplicities `K,K,NK,NK`.  Boolean characters give a complete
   eigenbasis, so there are no hidden eigenvalues or Jordan blocks.
6. Within this family, the component support degree recovers
   `d=log_2(N+1)`; the total carrier size then recovers `K`.

## What is and is not being claimed

The simplex-code interpretation, projective hyperplane incidence,
symmetric-difference design vocabulary, Cayley-graph representation,
finite-abelian Fourier diagonalization, the named crown graph, and the crown
spectrum are all assigned zero contribution credit.  P145 already contains
an abelian quotient walk and generic Fourier machinery; that proof shell is
also zero credit.  Brown's hyperplane-chamber walks are a nearby name but a
different carrier and update.

The retained owner-thin conjunction is the literal projective-hyperplane
toggle, its disjoint-crown decomposition, the every-target history formula,
and the multiplicity lift from one component to the full subset carrier.  A
bounded owner-search non-hit is not novelty, priority, or permission to
circulate.  The package therefore remains `OWNER_AMBER / HOLD_EXTERNAL`.

## Evidence and limitations

The paper-local author-side verifier is separately organized from the Stage-1
breadth scout.  It constructs the literal hyperplane masks, enumerates the
full carrier through `d=4`, exhausts Boolean characters through `d=4`,
enumerates ordered histories through five steps in those boxes, and checks
larger algebraic boxes through `d=8` and sixteen steps.  All calculations are
integer or rational.

These checks are counterexample pressure, not a proof of the
all-dimensional statements.  The manuscript supplies the proofs.  No claim
is made for `d=1`, for sampling the zero form, for toggling hyperplane
complements, for nonbinary projective spaces, or for a global graph
characterization outside the stated family.
