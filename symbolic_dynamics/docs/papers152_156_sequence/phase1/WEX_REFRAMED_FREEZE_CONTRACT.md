# WEX reframed hostile freeze contract

**Decision:** `PASS_FREEZE_REFRAMED`.  **External status:** `HOLD_EXTERNAL`.
**Proposed paper:** P156, conditional on the separate numbering decision.
This contract is the absolute claim ceiling.  It withdraws the false
pointwise maximum-drop clock and excludes the unproved global maximum clock.
It makes no novelty, priority, authorship, submission, or release claim.

## 1. Literal map and carrier

For `N>=1`, work on

```text
S_{<=N}=disjoint_union_{1<=n<=N} S_n.
```

For `pi=pi_1...pi_n`, retain the weak-excedance letters in their original
order and standardize:

```text
W(pi)=std(pi_i : pi_i>=i).                                (1)
```

Put

```text
d(pi)=max_i(i-pi_i).                                      (2)
```

For a nonidentity permutation, `d(pi)>0`: if every `pi_i>=i`, equality of the
two coordinate sums forces every `pi_i=i`.

## 2. Frozen theorem A — exact images and minimum-rank sections

For every `sigma in S_m` and `n>=m`, freeze

```text
sigma in W(S_n)  iff  n>=m+d(sigma).                      (A1)
```

If `h=n-m>=d(sigma)`, the explicit section is

```text
R_n(sigma)=(sigma_1+h,...,sigma_m+h,1,...,h),             (A2)
W(R_n(sigma))=sigma.                                      (A3)
```

In particular, the target-dependent minimum source rank is exactly
`m+d(sigma)`.

### Proof status: `PROVABLE AS STATED`

Let the selected source positions be `p_1<...<p_m` and the selected source
values be `a_1<...<a_m`.  The `i`th selected position receives
`a_{sigma_i}`.  With `h=n-m`, at most `h` unselected values lie below
`a_j`, so `a_j<=h+j`.  Selection gives

```text
i<=p_i<=a_{sigma_i}<=h+sigma_i.
```

Hence `i-sigma_i<=h` for every `i`, proving necessity.  In (A2), each high
entry satisfies

```text
sigma_i+h>=i
```

because `h>=d(sigma)`, while the final low entry `j` occurs at position
`m+j>j`.  Thus the selected word is exactly the shifted copy of `sigma`, and
standardization gives (A3).  No unproved lemma remains.

## 3. Frozen theorem B — every-target Ferrers fibres

Fix `sigma in S_m`, source rank `n`, and `h=n-m`.  Let

```text
A={a_1<...<a_m},   P={p_1<...<p_m}
```

range over subsets of `[n]` satisfying

```text
p_i<=a_{sigma_i} for all i.                               (B1)
```

Set `B=[n]\A` and `Q=[n]\P={q_1<...<q_h}`.  Define

```text
K(B,Q)=prod_{j=1}^h (#{b in B:b<q_j}-(j-1)),              (B2)
```

with value zero if a factor is nonpositive.  Freeze

```text
|W_n^{-1}(sigma)|=sum_{A,P satisfying (B1)} K(B,Q).       (B3)
```

### Proof status: `PROVABLE AS STATED`

For fixed `A,P`, the selected assignment is forced.  Process complement
positions increasingly.  At `q_j`, exactly `#{b in B:b<q_j}` complement
values are eligible and the `j-1` previously assigned values are all among
them.  This gives the `j`th factor in (B2).  Every resulting complement
assignment is deficient and every source in the fibre determines one unique
quadruple `(A,P,selected assignment,complement assignment)`.  The construction
is disjoint and reversible.  Formula (B3) includes zero fibres.

The aggregate identity-target basin is not credited: Beyene--Backelin--
Mantaci--Fufa Theorem 27 owns the Bell-number enumeration of permutations
whose weak-excedance-letter subword is increasing.  The target-resolved and
rank-resolved formula (B3) must cite and subtract that result explicitly.

## 4. Frozen theorem C — identity-only recurrence

Freeze:

```text
W(pi)=pi  iff  pi is an identity permutation;             (C1)
every nonidentity step strictly lowers rank;              (C2)
the recurrent states of S_{<=N} are exactly id_1,...,id_N. (C3)
```

### Proof status: `PROVABLE AS STATED`

If `W(pi)` has the same rank as `pi`, every position was selected, hence
`pi_i>=i` for every `i`.  Equality of sums forces equality term by term, so
`pi=id_n`.  Conversely identities are fixed.  A nonidentity orbit has strictly
decreasing positive rank until it reaches an identity; it cannot contain any
other recurrent state.

## 5. Frozen theorem D — locally minimum Fibonacci right-inverse tower

For nonidentity `sigma in S_m`, put `d=d(sigma)>0` and define the canonical
minimum-rank section

```text
R(sigma)=R_{m+d}(sigma)
        =(sigma_1+d,...,sigma_m+d,1,...,d).                (D1)
```

Define `sigma^(0)=sigma` and `sigma^(t+1)=R(sigma^(t))`.  If

```text
m_t=|sigma^(t)|,   d_t=d(sigma^(t)),
```

freeze the exact resource update

```text
(m_{t+1},d_{t+1})=(m_t+d_t,m_t),                          (D2)
W(sigma^(t+1))=sigma^(t).                                 (D3)
```

With `F_0=0,F_1=1`, for every `t>=1`, freeze

```text
m_t=F_{t+1}m+F_t d,
d_t=F_t m+F_{t-1}d.                                      (D4)
```

Consequently every nonidentity target has an explicit inverse ray of arbitrary
height.  If `tau` is the absorption time into an identity, then

```text
tau(sigma^(t))=tau(sigma)+t.                              (D5)
```

The adjective **locally minimum** has a fixed meaning: by Theorem A,
`sigma^(t+1)` has the minimum possible rank among all one-step preimages of
`sigma^(t)`.  The contract does **not** say that the composite tower has
minimum possible rank among all `t`-step preimages.

### Proof status: `PROVABLE AS STATED`

The first `m_t` entries in (D1) are weak excedances and the last `d_t` entries
are deficient, proving (D3).  For the maximum drop, a shifted high entry has

```text
i-(sigma_i+d_t)<=d_t-d_t=0,
```

while low value `j` occurs at position `m_t+j` and has drop exactly `m_t`.
Thus `d_{t+1}=m_t`; rank is visibly `m_t+d_t`.  This proves (D2).  Powers of
the matrix

```text
[[1,1],[1,0]]
```

give (D4) by induction.  Equation (D3) and the strict-rank theorem show that
the tower adds exactly one nonrecurrent step at every lift, proving (D5).

The independent pressure test checks six tower levels for all 46,225
nonidentity targets through rank eight, executing 1,109,400 assertions.  It is
support, not proof.

## 6. Explicitly excluded false or unproved statements

The following statements are outside the paper and must not appear as
theorems, abstract claims, implications, or suggestive conclusions:

1. `tau(W(pi))<=max_{rho in S_{d(pi)}}tau(rho)`.  This is false at
   `pi=(11,10,9,4,1,2,3,8,5,6,7)`.
2. `tau(pi)>=t => d(pi)>=F_{t+1}`.  The same source disproves it.
3. the global maximum-clock conjecture
   `max_{pi in S_n}tau(pi)=max{t:F_{t+2}<=n}`.  It remains unproved.
4. global `t`-step minimum-preimage optimality of the canonical tower.
5. novelty or priority inferred from an exact-map search non-hit.

The paper may state these only in a limitations paragraph, with the false
claims labelled false and the size-only clock labelled open.

## 7. Owner and portfolio subtraction

The following receive zero contribution credit:

- weak-excedance and excedance-set distributions;
- maximum-drop statistics and bounded-drop enumeration;
- permutation-tableau/Bruhat weak-excedance structure;
- Bell enumeration of the increasing weak-excedance-letter subword;
- generic Ferrers/rook-board matching technology; and
- the broad carrier pattern “extract a permutation subsequence and
  standardize.”

Mandatory primary citations are the records already verified in
`WEX_FOCUSED_AUDIT.md`: Ehrenborg--Steingrímsson; Chung--Claesson--Dukes--
Graham; Chen--Chen; Steingrímsson--Williams; Bergeron--Gagnon; and Beyene--
Backelin--Mantaci--Fufa, with Baril's transposition-array citation chain.

### Separation from P149

P149 selects endpoint-inclusive local maxima and uses alternating packing,
peak carriers, and comparison-poset fibres.  WEX uses the absolute diagonal
predicate `pi_i>=i`, the target obstruction `d(sigma)`, the high-shift/low-tail
section, and deficient Ferrers completions.  The new temporal axis is not a
maximum clock: it is the exact dynamics of a canonical minimum-rank right
inverse.  None of P149's peak-packing proofs establish (A1), (B3), or (D2).

### Separation from CME

CME extracts one maximum from each cycle support and has image threshold
`2m-rlmin(sigma)` with ordered-set-partition factorial fibres.  WEX selects
plot points above the diagonal, has threshold `m+d(sigma)`, and uses deficient
complement matchings.  CME's endpoint `O/C/S` schedule and WEX's selected-
position/value Ferrers board are not interchangeable.  Their right sections
also evolve by different resource rules; CME's proposed power clock is
excluded, while WEX freezes an explicit inverse tower only.

## 8. Hostile paper-size gate

**Verdict: PASS for a 4--6 page short note, under this ceiling.**  The residual
is not merely a statistic or one-step closure:

1. Theorem A is a sharp target-by-target image classification with a minimum-
   rank constructive inverse.
2. Theorem B independently resolves every target fibre at every source rank.
3. Theorems C--D turn the chosen right inverse into an exact backward
   dynamical system with Fibonacci resource evolution and arbitrary temporal
   depth.

Deleting D would leave a borderline one-step note; deleting A or B would make
the package too thin.  The false maximum clock is not needed for the accepted
conjunction and is forbidden.  No external review or release is authorized.

## 9. Verification ceiling

The paper-local verifier may copy the already cold-replayed literal map,
image, fibre, and functional-graph checks, then add the tower audit.  Its
frozen transcript must distinguish:

```text
closed exact theorems: A/B/C/D
false claims: withdrawn
global maximum clock: not claimed
external status: HOLD_EXTERNAL
```

