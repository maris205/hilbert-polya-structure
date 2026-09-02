# BTB final freeze contract — local triad dynamics on a triangular book

**Contract date:** 2026-09-02 UTC.  
**Formula status:** `COHERENT AS STATED`.  
**Paper-value verdict:** **`PASS_PAPER_SIZED_OWNER_THIN`**.  
**External status:** `HOLD_EXTERNAL`.  
**Scope effect:** eligible only for later internal assignment; no paper number,
draft, novelty claim, priority claim, or release clearance is created here.

This pass is deliberately narrow.  Antal--Krapivsky--Redner and Istrate own
the exact stochastic kernel, Istrate owns its XOR/triadic-dual representation,
and signed-book work owns the carrier and the count statistic as a static
switching classification.  The only claim-bearing object is the **complete exact law of
that owned kernel on this special carrier**, led by the bivariate marked
transform and the coarse-data inverse.

## 1. Literal system and clock convention

Let

```text
B_r=B(3,r)=K_{1,1,r},       r>=1,
```

be `r` triangles sharing one common **edge**, called the spine.  Give every
physical edge a sign.  A page is imbalanced when the product of its three edge
signs is negative.  At each update epoch:

1. choose one currently imbalanced page uniformly;
2. choose one of its three physical edges uniformly;
3. flip that edge's sign;
4. stop when every page is balanced.

Let `x_i` be the imbalance bit of page `i`, let

```text
K=sum_i x_i,       T=number of update epochs to absorption,
J=number of common-spine flips before absorption.
```

`T` is the imbalanced-page update-epoch clock.  It is not the physical clock
of the AKR 2005 convention that samples balanced pages and inserts no-ops.

## 2. Absolute theorem ceiling

Exactly the following five theorem interfaces are permitted.  The first is a
bridge and the fifth is support; the paper-sized residual is the conjunction
of BTB-B, BTB-C, and BTB-D.

### BTB-A — strong count lumping

For every full sign state with `K=k>0`, either private side edge clears only
the selected page or the spine toggles every imbalance bit.  Hence the full
chain is strongly lumpable by `K` and

```text
k -> k-1       with probability 2/3,
k -> r-k       with probability 1/3.                    (A1)
```

When the two targets coincide, their masses add.  This theorem must be stated
as a special-carrier reduction of the owned triadic dynamics, not as a new
model or a new XOR duality.

### BTB-B — complete joint absorption/spine-flip transform

Define

```text
F_k(z,u)=E_k[z^T u^J],       F_0=1.
```

First-step conditioning gives

```text
F_k=z[(2/3)F_{k-1}+(u/3)F_{r-k}].                       (B1)
```

For `r>=2`, put

```text
xi=[9+z^2(4-u^2)]/(12z),
```

and let `U_j` be the Chebyshev polynomials of the second kind with
`U_{-1}=0`.  Then

```text
F_k=U_{k-1}(xi)F_1-U_{k-2}(xi),                         (B2)

F_1=[3U_{r-2}(xi)-2zU_{r-3}(xi)+zu]
    /[3U_{r-1}(xi)-2zU_{r-2}(xi)].                      (B3)
```

Equations (B2)--(B3) are identities of reduced rational functions, with
removable values interpreted from (B1).  The theorem must separately state
the `r=1`, `r=2`, and `z=0` boundaries in Section 6.

### BTB-C — quadratic mean and sharp count extrema

For `1<=k<=r`,

```text
m_k=E_k T=k(r+2-k)/2.                                  (C1)
```

For `r>1`, the unique minimum is at `k=1`, with value `(r+1)/2`.  The maxima
are

```text
r even: k=(r+2)/2,             value (r+2)^2/8;
r odd:  k=(r+1)/2,(r+3)/2,     value ((r+2)^2-1)/8.
```

For `r=1`, the only nonabsorbing state is both minimum and maximum and has mean
one.

### BTB-D — spine parity, exact two-statistic inverse, and necessity

Let

```text
q_k=P_k(J odd).
```

Then

```text
E_k[(-1)^J]=(r+2-2k)/(r+2),
q_k=k/(r+2).                                             (D1)
```

For exact coarse observations `(m,q)` from a nonabsorbing start, set

```text
R=sqrt(2m/[q(1-q)]).
```

The pair is feasible if and only if `R` is an integer at least three and

```text
k=qR is an integer with 1<=k<=R-2.
```

In that case the carrier and start are uniquely recovered by

```text
r=R-2,       k=qR.                                      (D2)
```

Both observations are necessary in general.  The parity statistic alone has

```text
(r,k)=(1,1) and (4,2)  -> q=1/3,
```

whereas the mean alone has

```text
(r,k)=(2,2) and (3,1)  -> m=2.
```

No noisy-data stability, recovery of a full sign configuration, or inverse
from one scalar is permitted.

### BTB-E — explicit absorption certificate

A block of `r` consecutive private-edge choices forces absorption and has
probability `(2/3)^r`.  Therefore

```text
P_k(T>nr) <= [1-(2/3)^r]^n.                             (E1)
```

This is a book-specific certificate and a supporting tail bound.  It cannot be
advertised as the first convergence theorem for triadic dynamics or as a
generic hypergraph result.

## 3. Shortest proof-dependency graph

```text
physical sign update on B(3,r)
    |
    v
page-imbalance XOR bits
    |
    v
private flip clears selected bit; spine flip complements all bits
    |
    v
strong count quotient (A1)
    |
    +----------------------+----------------------+-------------------+
    |                      |                      |
    v                      v                      v
marked Bellman (B1)   mean Bellman          parity Bellman       private blocks
    |                      |                      |                   |
    v                      v                      v                   v
reflection elimination second difference      affine solution    tail bound (E1)
    |                      |                      |
    v                      v                      +---------+
Chebyshev recurrence   quadratic mean (C1)                |
    |                      |                               v
    v                      +------------------------> coarse inverse (D2)
joint transform (B2-B3)
```

The marked transform is not allowed to be replaced by a generic matrix
resolvent.  The inverse theorem must include its feasible-image statement and
the two one-statistic counterexamples; otherwise BTB-D is only a decorative
algebraic rearrangement.

## 4. Owner zero-credit ledger

1. Antal--Krapivsky--Redner,
   [*Dynamics of Social Balance on Networks*](https://arxiv.org/abs/cond-mat/0506476)
   and
   [*Social Balance on Networks: The Dynamics of Friendship and Enmity*](https://arxiv.org/abs/physics/0605183),
   own local triad dynamics.  At `p=1/3`, every edge of an imbalanced triad is
   flipped equiprobably.  The latter formulation directly owns the update-epoch
   kernel.
2. Istrate,
   [*On the dynamics of Social Balance on general networks*](https://arxiv.org/abs/0811.0381),
   owns the same probabilistic kernel on arbitrary graphs and the exact
   XOR/triadic-dual hypergraph representation.  Istrate--Bonchis--Marin,
   [arXiv:1909.12353](https://arxiv.org/abs/1909.12353), further subtract generic
   hypergraph particle-system, WalkSAT, drift, and convergence-time language.
3. Sehrawat--Bhattacharjya,
   [*Chromatic Polynomials of Signed Book Graphs*](https://arxiv.org/abs/2206.08580),
   own the signed-book carrier and its `r+1` switching classes indexed by the
   number of negative pages.  The carrier and static count quotient are zero
   credit.
4. Generic first-step equations, finite Markov resolvents, Chebyshev polynomial
   facts, tail-sum identities, and concavity of a quadratic receive no
   independent credit.

The paper must say “specialization of the owned `p=1/3` kernel” before stating
its own residual.  It may not claim a new social-balance model, XOR duality,
signed-book classification, general absorption theorem, or generic WalkSAT
analysis.  The focused primary-source search did not locate the special-book
law (B2)--(D2); that bounded non-hit is not a novelty or priority claim.

## 5. Internal-paper collision firewall

| occupied/internal item | apparent collision | mandatory separation |
|---|---|---|
| P136 and permanently killed S09 | S09 also uses `r` triangles sharing an edge and chooses an active triangle plus one of its edges | S09 **deletes** the selected edge and is exactly the P136 sunflower transversal process; BTB flips a sign, keeps every edge, and a spine flip reflects `k` to `r-k`.  No deletion endpoint, transversal law, or P136 random-order proof may be imported. |
| P145, random vertex-push orientation chain | both use binary edge/orientation data and quotient a graph update | P145 is a stationary group walk with folded-hypercube spectra and component-order inverse; BTB selects an active imbalanced triangle, is absorbing, and uses a reflected count recurrence.  Fourier spectra, push equivalence, and component recovery receive zero credit. |
| P138, palindromic-prefix XOR feedback | both admit an XOR encoding | P138 is a deterministic length-preserving word map with palindrome feedback; BTB is a stochastic active-hyperedge process.  XOR notation alone is not separation value. |
| P151, unequal-spider first passage | both have a marked temporal transform, moments, extrema, and an inverse boundary | P151 uses unequal-arm continuants and labelled-leaf first passage; BTB must lead with the spine-marked Chebyshev reflection law and parity inverse.  A paper containing only the mean and absorption time would collide with the occupied generic first-passage silhouette and be killed. |

The triangular book must always be defined as `B(3,r)=K_{1,1,r}`, where the
triangles share an **edge**.  A friendship/Dutch-windmill graph shares only one
vertex and induces a different, deterministic count law.

## 6. Mandatory boundaries and counterexamples

Every draft under this contract must visibly include all of the following.

- **`r=1`:** every update absorbs and
  `F_1=z(2+u)/3`; (B3) is not invoked because it would require `U_{-2}`.
- **`r=2`:** a spine flip from `k=1` is a self-loop and
  `F_1=2z/(3-zu)`.  The unreduced Chebyshev ratio contains a removable
  `(3+zu)` factor; pointwise use before cancellation is forbidden.
- **`z=0`:** `xi` is undefined, while the Bellman solution has `F_0=1` and
  `F_k=0` for `k>0`.  Use reduced rational continuation.
- **Coincident targets:** when `k-1=r-k`, the two transition masses in (A1)
  combine; they are not distinct arrows.
- **Central parity:** `q=1/2` is valid for even `r`; it is not a singular
  inverse case.
- **Inverse domain:** only `1<=k<=r` is observed, so `0<q<1`; integer
  feasibility in BTB-D is necessary.  No inference from approximate data is
  made.
- **Single-statistic failure:** the explicit `q`-only and `m`-only collisions
  in BTB-D must be retained.
- **Clock convention:** AKR 2005's all-triad clock inserts state-dependent
  geometric holds.  Equations (B1)--(E1) count active update epochs only.
- **Weights:** nonuniform page selection generally destroys count lumpability;
  nonuniform physical-edge weights change every coefficient.
- **Carrier terminology:** on the friendship graph each selected edge belongs
  only to one page, so `K->K-1` and `T=K` deterministically.  It is not BTB.
- **Mark meaning:** `J` counts spine flips only, not all negative-edge flips or
  the final number of negative edges.

## 7. Title and abstract claim ceiling

The strongest admissible title is:

> **Joint absorption and spine-flip laws for local triad dynamics on triangular books**

The abstract ceiling is:

> For the established `p=1/3` local triad dynamics, specialize to the
> triangular book `B(3,r)=K_{1,1,r}` and count active update epochs.  The page
> imbalance count is a reflected one-dimensional quotient.  Its joint
> absorption-time/spine-flip transform has an explicit Chebyshev-rational form;
> the mean has sharp starting-count extrema; and the mean together with spine
> parity exactly identifies the book size and initial imbalance count, with
> explicit feasibility and nonidentifiability boundaries.

The abstract may not say or imply “new social-balance dynamics,” “first
convergence result,” “new XOR representation,” “new signed-book
classification,” a result for arbitrary graphs, or a result for friendship
graphs.  “Exact law on a special carrier” is the maximum positioning.

## 8. Final hostile value attack

**Strongest counter-argument.**  The stochastic rule is externally owned
exactly, not just generically, and the signed triangular-book carrier is also
owned.  Lumping by the number of imbalanced pages is a one-line observation.
Once the quotient is written, the remaining paper could be dismissed as an
exercise in solving a finite recurrence, while mean, parity, and inverse are
specializations or rearrangements of the same bivariate transform.

**Why the package narrowly survives.**  The residual is not the Bellman system
alone.  It contains an all-`r` elimination of the reflection term to a
second-order Chebyshev recurrence, the complete joint `(T,J)` transform with
nontrivial `r=2/z=0` continuation, a sharp quadratic clock theorem, and an
exact two-observable identifiability theorem whose feasible image and two
one-observable failures are explicit.  These give a compact but coherent
special-carrier exact-law note.  None of the checked owners states that
conjunction.

The pass is lost immediately if any of the following occurs:

1. a direct source is found for the triangular-book transform or an equivalent
   one-large-hyperedge-plus-two-loops specialization;
2. the draft leads with the owned model, XOR dual, carrier classification, or
   generic absorption rather than (B2)--(D2);
3. the joint marked transform is removed or replaced by a generic resolvent;
4. BTB-D omits feasibility and single-statistic counterexamples, leaving only
   an algebraic rearrangement; or
5. the clock is silently changed from active update epochs to all-triad time.

```text
FORMULAS = PASS
OWNER POSITION = PASS_OWNER_THIN
PAPER VALUE = PASS_PAPER_SIZED_OWNER_THIN
NUMBER = UNASSIGNED
DRAFT = NOT_AUTHORIZED_BY_THIS CONTRACT
EXTERNAL = HOLD_EXTERNAL
```

## 9. Frozen evidence

The independent focused verifier and transcript remain the canonical
falsification evidence:

```text
verify_htm_btb_focused_audit.py
HTM_BTB_FOCUSED_AUDIT_VERIFICATION.txt
PASS assertions=204949
```

The BTB lanes enumerate every literal nonzero bit state through `r=9`, compare
complete transform vectors at four rational `(z,u)` points through `r=20`,
check Bellman/Chebyshev identities and all `r=1/r=2/z=0` boundaries, solve the
mean and parity systems through `r=60`, test every inverse state through
`r=300`, and verify the private-block absorption certificate.  A cold replay
on 2026-09-02 was byte-identical.  Enumeration is counterexample pressure, not
proof or owner clearance.
