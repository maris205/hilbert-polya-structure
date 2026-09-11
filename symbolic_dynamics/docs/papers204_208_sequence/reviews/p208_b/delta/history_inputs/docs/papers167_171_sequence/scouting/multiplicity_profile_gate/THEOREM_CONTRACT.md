# Candidate theorem contract — multiplicity-profile descent (`MPD`)

**Status:** `AMBER_OWNER_DENSE / NEEDS_INDEPENDENT_HOSTILE_GATE`  
**External status:** `HOLD_EXTERNAL`

## Literal system

Let `P_{<=N}` be the nonempty integer partitions of all integers at most
`N`.  If the distinct parts of `lambda` have positive multiplicities
`m_1,...,m_r`, define

```text
D(lambda) = sort(m_1,...,m_r).
```

Thus `(5,5,3,3,3,1)` maps to `(3,2,1)`.  The total after one update is the
number of parts before the update, so `D` is a self-map of `P_{<=N}`.

## Proposed sharp temporal theorem

For a partition `mu=(mu_1>=...>=mu_r)`, define its canonical lift

```text
L(mu) = (r repeated mu_r times, ..., 2 repeated mu_2 times,
         1 repeated mu_1 times).
```

Then `D(L(mu))=mu`.  Moreover:

1. `L(D(lambda))` is contained in `lambda` as a Ferrers diagram;
2. `L` preserves Ferrers containment;
3. `(1)` is the unique recurrent state; and
4. with `Lambda_1=(2)` and `Lambda_d=L^(d-1)((2))`, every state of exact
   depth `d` contains `Lambda_d`.  Hence the least size among exact-depth
   `d` states is `a_d=|Lambda_d|`, uniquely attained by `Lambda_d`.  The
   same `a_d` is the least size at depth at least `d`; for `d>=2` its
   minimizer is unique, while at `d=1` both `(2)` and `(1,1)` attain size
   two.

Consequently the sharp height on `P_{<=N}` is

```text
H(N)=max {d>=0 : a_d<=N},
```

where

```text
a_1,...,a_10 = 2,2,3,4,7,14,42,213,2837,175450.
```

These are shifted Levine numbers.  The sequence, its inventory rows, and its
known growth estimates are owned background; the candidate contribution is
only the extremal depth interpretation and proof through canonical
containment.

## Proposed every-target fibre theorem

Let `mu=(mu_1>=...>=mu_r)` and let `Orb(mu)` be the distinct permutations
`alpha=(alpha_1,...,alpha_r)` of its parts.  Put

```text
S_j(alpha)=alpha_j+...+alpha_r.
```

The source-size generating function of the complete fibre is proposed to be

```text
Phi_mu(q)
 = sum_{alpha in Orb(mu)} product_{j=1}^r q^{S_j(alpha)}/(1-q^{S_j(alpha)}).
```

Indeed `alpha_i` is assigned as the multiplicity of the `i`th increasing
distinct source part, and positive gaps between those source parts yield the
displayed product.  Equivalently this is the principal specialization
`m_mu(q,q^2,...)` of a monomial symmetric function.

The least source size is

```text
w(mu)=sum_{i=1}^r i*mu_i,
```

and its coefficient is one, represented by `L(mu)`.  Hence, inside
`P_{<=N}`, a target lies in the image exactly when `w(mu)<=N`, and every
bounded target fibre is obtained by coefficient summation through degree
`N`.

## Required hostile gates

1. Reprove the Ferrers-containment extremum without using the observed
   Levine prefix as induction evidence.
2. Attack the distinction between exact depth `d` and depth at least `d`.
3. Check the fibre series on repeated target parts, where ordinary
   permutations would overcount.
4. Read Eliahou--Erickson and the Levine/Sloane owner chain for a direct
   statement of the literal forward map, extremal depth, or target series.
5. Compare P113, P126, P137, P147, and the earlier inventory/partition kill
   ledgers at proof-engine level.

No paper number is allocated before these gates close.
