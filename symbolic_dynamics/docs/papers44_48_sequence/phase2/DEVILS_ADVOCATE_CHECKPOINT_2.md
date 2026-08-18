# Devil's Advocate Checkpoint 2 — Final Five-Way Gate

## Scope and verdict

This is the final Phase-2 hostile review of the revised Paper 44--48
sequence.  It is evaluated against accepted Papers 1--43 at commit
`6e5658649d2eab0fce077cbcdcc00070dd54095f`.  It freezes research positions,
not authority files, priority claims, Route outcomes, or publication rights.

```text
SCIENTIFIC_GATE = PHASE2_FIVE_WAY_CLEAN
P44 = GO_WITH_FIREWALL
P45 = GO_WITH_FIREWALL
P46 = GO
P47 = GO
P48 = GO_WITH_FIREWALL
AUTHORITY_WRITE = FORBIDDEN_BY_THIS_GATE
```

The included `P45_INDEPENDENT_AUDIT_ATTESTATION.md` binds the separately
commissioned source report `p45_retraction_hostile_audit.md`, SHA-256
`926aad2a27ef88fdb82e8cdca487d34c75d44141c9827d9863bf5a3eae8e1326`.
It reproduced the repaired all-`h` theorem and returned `GO`; the `h=2`
singleton remains `STOP`.

## Central/major/minor theorem matrix

| Paper | Central theorem | Major support | Minor/control | Mandatory subtraction | Delete-shared-method result |
|---|---|---|---|---|---|
| P44 | exact `q`-adic order-one remainder and full accumulation image | golden strong-separation Cantor spectrum and dimension | dense pole-type Lambert boundary singularities and natural boundary | multiplicative-SFT object, chain product, entropy and leading dimensions | exact bounded remainder, `Z_q` extension, compact image and Cantor theorem remain |
| P45 | all-`h` saturated/modulo retractions with the same cyclic ledger but a sharp non-similarity band | two Weyl laws, primorial Riesz maximal order, similarity iff | self-commutator wall and `h=2` Euler control | generic weighted composition; P27--P30/P43; classical power-free part | paired arithmetic classification, crossover, maximal order and commutator law remain |
| P46 | `v_2` orthogonal self-similarity and complete odd/even edge-label cycle solver | sharp bounded/compact, `S_2`, and `S_1` endpoints | trace and legal `det_2` ledger | generic Hankel/Besov/Schur, finite determinant and label-solver theory | exact `v_2` direct sum and canonical closed-walk classification remain |
| P47 | primitive Mordell--Tornheim realization as the exact second trace of the looped Egyptian adjacency | unique coprime-scale edge zeta and sharp ideal endpoints | first trace and mixed-cycle falsifiers | Egyptian parametrization and MT series identities | primitive MT trace realization and homogeneous edge geometry remain |
| P48 | all-radix Schatten critical surface for the infinite weighted no-carry operator for every `1<=q<infinity` | equality pinching, weighted trace, `det_2`, infinite least-period set | finite zero-deletion data only as evaluators | Kummer/Lucas and every finite Boolean/Pascal/disjointness/tensor census | Dirichlet-weighted shell theorem and exact equality endpoints remain |

P47 is intentionally the narrowest admitted unit.  If its primitive
Mordell--Tornheim identity is demoted to an example, the paper reverts to
`STOP_SALAMI`; a triangle example or the shared ideal staircase cannot carry
it.

## Endpoint and quantifier locks

### P44

For primitive zero-one `A` and `q>=2`, with
`c_v=log(W_(v+1)/W_v)`, `d_v=c_v-log rho(A)`,

```text
log Z(N)-log Z(N-1)=c_(nu_q(N)),
h=sum_(v>=0)(q-1)q^(-v-1)c_v,
log Z(N)-hN
 =-sum_(v>=1)(d_v-d_(v-1))(N mod q^v)/q^v.
```

The last series is uniformly convergent on `Z_q`, and its image is exactly
the accumulation set.  In the golden control, the Binet coefficients have
alternating sign, strict tail separation, and ratio `-phi^(-2)`, giving
dimension `log(2)/(2 log(phi))`.  Ordinary Minkowski content is not claimed.
The natural-boundary statement is secondary and the primitive hypothesis is
not extended to reducible or periodic matrices.

### P45

For `h>=2`, all walls are strict:

```text
S bounded/compact <=> sigma>0,
M bounded/compact <=> sigma>1/h,
S in S_q         <=> sigma q>2,
M in S_q         <=> sigma>1/h and sigma q>2,
S^k in S_q       <=> k sigma q>2,
M^k in S_q       <=> sigma>1/h and k sigma q>2.
```

Common traces are legal only when the operators exist and `k sigma>2`.
Normal similarity holds for `S` exactly when `sigma>1`, and for `M`
throughout `sigma>1/h`.  The singular Weyl constants satisfy the exact
crossover

```text
C_(h,1)=D_(h,1)=1.
```

No global inequality away from one is claimed without proof.  The saturated
Tauberian series factors as `F=zeta G`, with `G` holomorphic for

```text
Re(z)>max(1/h,(1-sigma)/(h-1))<1.
```

For commutator necessity, `h=2` uses a varying second saturated prime;
`h>=3` may use a varying exponent-one prime.  This gives

```text
[S*,S] in S_q <=> sigma q>1,
[M*,M] in S_q <=> sigma>1/h and sigma q>1.
```

### P46

```text
sigma<=0: unbounded,
sigma>0: bounded and compact,
H_s in S_2 <=> sigma>1/2,
H_s in S_1 <=> sigma>1.
```

The exact decomposition is `H_s ~= direct_sum_(k>=0) 2^(-ks)A_s` on odd
vertices.  An odd closed walk has the unique alternating half-sum solution;
an even walk exists exactly when the alternating edge-label sum vanishes,
after which one positivity-constrained integer parameter remains.  No
all-`S_q` theorem is claimed.

### P47

Loops are part of the frozen kernel.  The unique edge form is

```text
m=t a(a+b), n=t b(a+b), gcd(a,b)=1.
```

The phase diagram is unbounded for `sigma<=0`, compact but not `S_2` for
`0<sigma<=1/2`, `S_2` but not `S_1` for `1/2<sigma<=1`, and `S_1` for
`sigma>1`.  In their legal domains,

```text
Tr E_s   =2^(-s)zeta(s),
Tr E_s^2 =zeta(2s)zeta_MT(s,s;2s)/zeta(4s).
```

Deleting loops is a different object and must be a negative control.

### P48

For `1<=q<infinity`,

```text
B_(b,s) in S_q
 <=> sigma>max(1,log_b ||C_b||_(S_q)).
```

In particular, boundedness, compactness and `S_2` all start strictly above
one, while `S_1` starts strictly above
`alpha_b=log_b ||C_b||_(S_1)`.  The `b=2` diagonal shell is zero, so equality
necessity uses adjacent off-diagonal pairs.  The trace is zero only for
`b=2`; for `b>2` it is the Dirichlet sum over positive integers whose digits
are at most `floor((b-1)/2)`.  The infinite least-period set is all positive
integers for `b>2` and all integers at least two for `b=2`.  Kummer is a
prime-radix corollary, not the definition.

## Ten-pair anti-salami replay

| Pair | Shared surface | Surviving independent core |
|---|---|---|
| P44--P45 | valuations | `q`-adic prefix remainder vs prime-fiber geometry |
| P44--P46 | dyadic scales | finite-size oscillation vs additive edge sums |
| P44--P47 | arithmetic counts | Cantor boundary image vs Egyptian edge zeta |
| P44--P48 | base digits | valuation-chain remainder vs positional no-carry shells |
| P45--P46 | Schatten/determinant words | nonnormal fibers vs `v_2` cycle solver |
| P45--P47 | Dirichlet/Euler formulas | Riesz/Weyl distortion vs primitive MT trace |
| P45--P48 | local exponent/digit matrices | retraction similarity wall vs radix shell threshold |
| P46--P47 | the `0,1/2,1` staircase | odd/even cycle theorem vs MT realization |
| P46--P48 | powers of two and pinching | additive support vs no-carry tensor support |
| P47--P48 | symmetric arithmetic graphs | reciprocal homogeneity vs digital critical exponent |

Every pair retains a different central theorem after the shared Schur,
summability, pinching, Schatten, Euler, and determinant lemmas are deleted.

## Experiment and mutation obligation

Each paper has two independently specified evaluators.  They may agree only
through canonical scientific projections; they may not share fixtures,
serialized intermediates, source code, or expected-value tables.  Before any
authority run, hostile mutations must cover source identity, types, endpoint
equalities, quantifiers, object conventions, ownership subtraction, and
Route/state provenance.  P45 must include a mandatory `sigma=1` equality row;
P47 a loop-deletion row; P48 both binary/odd-radix trace and equality rows.

## Final release boundary

The five research units pass Phase 2.  This checkpoint does not create a
paper, write the repository, confer novelty/priority, select Route A, or
permit Route B.  The next step is to freeze five independent source locks and
then build proof and experiment packages in paper order.
