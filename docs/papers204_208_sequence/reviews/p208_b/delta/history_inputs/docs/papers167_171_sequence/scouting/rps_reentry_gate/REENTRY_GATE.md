# RPS independent re-entry gate

**Object:** repeated intersection with the fixed set of an independent
uniform permutation  
**Audit date:** 2026-09-03 UTC  
**Lifecycle:** `HOLD_EXTERNAL`  
**Decision:** **`GREEN_OWNER_THIN_WITH_N3_REPAIR`**  
**Mathematical findings:** `0 Critical / 0 Major / 1 mandatory boundary repair`

## 1. Outcome and changed contract

For fixed `n>=2`, let the state space be `2^[n]`.  At each epoch choose an
independent uniform `pi in S_n` and apply

```text
A -> A intersect Fix(pi).                                      (1)
```

The original unmarked and marked formulas survive a literal rederivation.
The source contract nevertheless misstated the second asymptotic scale at
`n=3`: ranks two and three have the same eigenvalue `1/6`.  The two-scale
statement must start at `n=4`, with exact separate formulas at `n=1,2,3`.

This re-entry is not a bare reversal of the older P162-batch kill.  The
candidate has been strengthened by a new result absent from that gate: for
every supported endpoint, the cycle-marked history polynomial has exact,
sharp lowest and highest degrees, and its first logarithmic derivative gives
an exact conditional total-cycle expectation.  These statistics are not
recoverable from the unmarked subset kernel.  P162 is no longer a same-batch
competitor, although it remains a historical collision neighbour.

The accepted ceiling is deliberately thin.  Common fixed points, prescribed
fixed labels, inclusion--exclusion, Boolean-zeta diagonalization,
semilattice-walk spectra, absorption identities, and the ordinary cycle
polynomial of `S_n` all receive zero contribution credit.  The surviving
package is the endpoint-resolved conjunction for the literal process,
especially the marked-history support and sharp cycle range.

## 2. Literal derivation

Let `A_0=A`, let `pi_1,...,pi_t` be the sampled permutations, and write
`a=|A|`.  Intersections commute and associate, so the pathwise identity is

```text
A_t=A intersect Fix(pi_1) intersect ... intersect Fix(pi_t).   (2)
```

Thus the sequential process remembers the common fixed set only through its
intersection with the initial state.  This observation is an owned input,
not a contribution claim.

### 2.1 Every-time, every-endpoint kernel

Fix `B subseteq A` and put `b=|B|`, `d=a-b`.  All points of `B` must be fixed
at every epoch, whereas each point of `A\B` must be moved at least once.
Inclusion--exclusion on the latter set gives the exact number of histories

```text
K_t(A,B)=sum_(j=0)^d (-1)^j C(d,j)(n-b-j)!^t.                 (3)
```

The count is zero for `B not subseteq A`.  At `t=0`, equation (3) is the
Kronecker delta, because its alternating binomial sum is zero unless `d=0`.

For every `t>=1`, the complete support criterion is

```text
K_t(A,B)>0  iff  B subseteq A
and not (A=[n] and |B|=n-1).                                 (4)
```

The exception is necessary because a permutation fixing `n-1` labels fixes
the last label.  For sufficiency, derange `A\B` when `d>=2`; when `d=1`,
transpose the lost point with a point outside `A`; when `d=0`, use the
identity.  Use that realizing permutation at one epoch and identities at all
other epochs.

### 2.2 Containment eigenbasis

For `S subseteq [n]`, set `phi_S(A)=1[S subseteq A]`.  If `P` denotes the
one-step probability operator, then

```text
P phi_S = lambda_|S| phi_S,
lambda_r=(n-r)!/n!.                                           (5)
```

Indeed, `S` survives exactly when `S subseteq A` and the sampled permutation
fixes all of `S`.  The containment matrix is the Boolean zeta matrix, whose
Boolean Möbius inverse is explicit; hence these `2^n` eigenvectors form a
basis.  The only numerical repetition among the rank eigenvalues is

```text
lambda_(n-1)=lambda_n=1/n!,                                  (6)
```

with `n+1` displayed zeta-basis vectors across those two ranks.  Generic
semilattice spectral theory owns this axis; it is retained to make the
process calculation self-contained.

### 2.3 Absorption and low-rank boundaries

Let `T=min{t:A_t=empty}` and start from a nonempty `a`-set.  Dividing (3) by
`(n!)^t` at the empty target gives

```text
Pr(T<=t)=sum_(j=0)^a (-1)^j C(a,j)lambda_j^t,                 (7)
Pr(T>t)=sum_(j=1)^a (-1)^(j+1)C(a,j)lambda_j^t.              (8)
```

For `n>=2`, summing the finite spectral expansion yields

```text
E[T]  =sum_(j=1)^a (-1)^(j+1) C(a,j)/(1-lambda_j),           (9)

E[T^2]=sum_(j=1)^a (-1)^(j+1) C(a,j)
                    (1+lambda_j)/(1-lambda_j)^2,             (10)

E[s^T]=1-(1-s)sum_(j=1)^a
             (-1)^(j+1)C(a,j)/(1-s lambda_j).                (11)
```

Equation (11) holds as a probability generating function at least for
`|s|<lambda_1^(-1)` and defines the same rational continuation elsewhere.
The empty initial state has `T=0` and PGF one.

The exact boundary split is mandatory:

- `n=1`: the nonempty state never empties;
- `n=2`: every nonempty source satisfies `Pr(T>t)=2^(-t)`;
- `n=3`:
  ```text
  Pr(T>t)=a 3^(-t)-(C(a,2)-C(a,3))6^(-t);                    (12)
  ```
- `n>=4`:
  ```text
  Pr(T>t)=a n^(-t)-C(a,2)[n(n-1)]^(-t)+O(lambda_3^t).        (13)
  ```

The repair from `n>=3` to `n>=4` is substantive wording, even though the
exact finite sum (8) was already correct.

## 3. Cycle-marked histories: the retained second axis

Let `cyc(pi)` denote the total number of cycles, including fixed points, and
let

```text
C_t=cyc(pi_1)+...+cyc(pi_t).
```

Define the endpoint history polynomial

```text
M_t(A,B;u)=sum_(histories with A_t=B) u^C_t.                  (14)
```

If `s` prescribed labels are fixed, the remaining `n-s` labels are freely
permuted.  Hence their classical cycle polynomial gives

```text
R_(n,s)(u)=u^s product_(q=0)^(n-s-1)(u+q).                   (15)
```

Applying inclusion--exclusion before specializing the cycle mark yields

```text
M_t(A,B;u)=sum_(j=0)^d (-1)^j C(d,j)R_(n,b+j)(u)^t.          (16)
```

The coefficients are nonnegative because (14), rather than the alternating
form (16), is the definition.  Equation (16) specializes to (3) at `u=1`,
but the converse recovery is impossible: the scalar kernel discards the
cycle distribution of the sampled permutations.

### 3.1 Sharp cycle range

Assume `t>=1` and the endpoint in (4) is supported.  Then the lowest and
highest exponents occurring in (16) are exactly

```text
L_t(b)=t(b+1_[b<n]),
U_t(a,b)=tn-ceil((a-b)/2).                                   (17)
```

For the lower bound, every permutation fixes the `b` labels of `B`; if
`b<n`, its complement contains at least one cycle.  Equality follows by
using one cycle on `[n]\B` at every epoch (and fixing `B`).  If `b=n`, only
the identity occurs and both sides equal `tn`.

For the upper bound, write `delta(pi)=n-cyc(pi)`.  A nontrivial cycle of
length `ell` moves `ell` points and contributes `ell-1` to `delta`; since
`ell<=2(ell-1)`, one permutation moves at most `2 delta(pi)` points.  The
`d` lost labels must lie in the union of the moved supports, so

```text
d <= 2 sum_r delta(pi_r).
```

This gives `C_t<=tn-ceil(d/2)`.  If `d` is even, pair the lost labels into
transpositions at one epoch.  If `d>=3` is odd, use one 3-cycle and pair the
remaining lost labels.  If `d=1`, support implies `A` is not full, so
transpose the lost label with a label outside `A`.  Identities fill the other
epochs.  All constructions avoid `B`, proving sharpness.

### 3.2 Exact conditional expectation

Let `H_m=sum_(q=1)^m 1/q` and `H_0=0`.  Logarithmic differentiation of (15)
at `u=1` gives

```text
R'_(n,s)(1)/R_(n,s)(1)=s+H_(n-s).                            (18)
```

Therefore every supported endpoint has the exact conditional mean

```text
E[C_t | A_t=B]
 = t * sum_(j=0)^d (-1)^j C(d,j)(n-b-j)!^t
                      (b+j+H_(n-b-j))
     / K_t(A,B).                                             (19)
```

The sharp interval (17) contains (19).  Formula (19) exposes cycle
information genuinely lost under `u=1`, while using no claim that the
classical factor (15) is new.

## 4. Independent exact pressure

`verify_rps_reentry.py` is a standalone Python-standard-library program.  It
does not import the earlier scout, the earlier hostile verifier, or paper
code.  It performs the following checks.

- It enumerates all permutations and all labelled subset transitions through
  `n=7`, then compares times `0,...,5` with (3) for every ordered state pair.
- It constructs all cycle-marked transition powers through `n=6` and time
  three, checking (16) coefficientwise and checking coefficient
  nonnegativity.
- It checks the Boolean zeta eigenvectors and Möbius inverse through `n=7`,
  including the repeated terminal eigenvalues.
- It solves the projected absorbing chain over exact rationals through
  `n=8`, independently matching (7)--(13), both moments, and the PGF at five
  rational arguments.
- It checks the sharp marked degrees, endpoint coefficients, specialization,
  and conditional expectation for every size triple through `n=18` and time
  five.
- It checks singleton recovery `P({i},{i})=1/n` through `n=32`; this marginal
  is correct but receives no contribution credit.

The frozen transcript contains `413,374` exact assertions.  Two fresh runs
were byte-identical:

```text
script_sha256     771d6408b3e106c8ab7f7d04e4ff7694c729c66e3454d40e2a6ca36026631af3
transcript_sha256 68f872d3af84ebcdf93e8f8764409735cc209c28c6e5c0f979319da21739ba14
payload_sha256    ccc917d996c2530e9071e8331af8b49a4a6348e926f8502c15e5603b77b17fa8
```

Finite enumeration is counterexample pressure, not an all-parameter proof or
an ownership certificate.

## 5. Decision

The source and internal collision subtraction is frozen in
`OWNER_COLLISION_AUDIT.md`.  No inspected source states the endpoint-resolved
marked history polynomial together with its sharp total-cycle range and
conditional expectation.  This bounded non-hit is not novelty evidence.
It only leaves a sufficiently distinct, explicitly limited theorem package
for an anonymous internal short note.

```text
RPS GREEN_OWNER_THIN_WITH_N3_REPAIR
CLAIM_CEILING ENDPOINT_RESOLVED_MARKED_HISTORY_PACKAGE
EXTERNAL_STATUS HOLD_EXTERNAL
```
