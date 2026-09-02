# Independent hostile re-entry gate — QNC all-time inverse proposal

**Verdict:** `KILL`  
**Formula audit:** PASS  
**Owner/value gate:** FAIL  
**External status:** `HOLD_EXTERNAL`  
**Action:** do not assign P166; do not draft a paper

## Executive finding

The proposed mathematics survives a literal, boundary-first rederivation.
For every odd prime `p`, `e>=2`, and `1<=t<=e-1`, the normalized iterate is a
quadratic map followed by a bijective target transport.  The displayed
every-target formula, the full positive/zero fibre spectrum, and the finite
inner-ball chart are correct.  An independent enumerator passed **1,475,599**
assertions over 19 `(p,e)` boxes.

The re-entry nevertheless fails the required two-axis owner-subtracted value
gate:

1. By the proved `B_t` factorization, the time-`t` spectrum is exactly the
   old one-step QNC spectrum at precision `p^(k+2)`, with each source
   repeated `p^(t-1)` times.  DesJardins--Zieve Section 6.4 (critical class,
   plus its preceding nonsingular-class bijectivity) owns that one-step
   spectrum.  The all-time passage changes no histogram mechanism.
2. Lindahl--Zieve Theorem 3.1 specializes to `F(x)=px+x^2` with `lambda=p`,
   `a_2=1`, and `rho=1`, so its full conjugacy disc is exactly
   `|x|_p<|p|_p`, namely `p^2 Z_p`.  Their iterative-logarithm description
   specializes to the proposed infinite product.  The finite chart and its
   uniform fibres are reductions of this owned conjugacy.

The genuinely explicit residual is the target label
`a=B_t^(-1)(y/p^(t+1))`.  That transport was not located verbatim in the
bounded source search, but it is one elementary composition of near-identity
permutations.  It is not a second independent paper-sized theorem.

## 1. Audit provenance

The current derivation and verifier were written independently.  The old
files were read only to identify the historical claim/owner boundary.  Their
frozen hashes at the gate were:

```text
7059e483e6cb1b36e432039ea58d1b0d2ca85d907b17cd36e693ad804f7bff63  QNC_REENTRY_FOCUSED_AUDIT.md
d80b94c85adfca7a26aa95b93a18db81ed74355e5be34aec419f020d28a73d13  old verify_qnc_reentry.py
5aa68b79bb7b61a8fcf8468942cad26a63c39108c968dd65d81a700f8baf9400  old QNC_REENTRY_CANONICAL.txt
```

The old audit's `KILL_DIRECT` was not presumed to settle the new all-time
proposal.  The new axes were proved first, then independently subjected to
the owner and collision gates.

## 2. Literal derivation

For `x=pu`, induction from the literal update gives

```text
F^t(pu)=p^(t+1)P_t(u),
P_1=u(u+1),
P_{s+1}=P_s+p^sP_s^2.                                   (2.1)
```

At time `t`, only precision `k=e-t-1` remains.  Put
`phi_s(a)=a+p^s a^2` and `B_t=phi_{t-1}...phi_1`.  Since

```text
phi_s(a)-phi_s(c)=(a-c)(1+p^s(a+c)),
```

each factor, and hence `B_t`, is bijective modulo `p^k`.  Therefore
`P_t=B_t(u(u+1))`.  Pulling a divisible target through `B_t^(-1)` and
completing the square gives the claimed target fibre.  The independent
statement, including the exact precision of every coordinate, is recorded
in `THEOREM_CONTRACT.md`.

This derivation also shows why the all-time distribution is not a new
distributional mechanism.  The target transport is bijective, so it only
relabels the values of the same quadratic `u(u+1)` at the reduced precision;
the factor `p^t` comes from discarded source digits.

## 3. Boundary attack

| boundary | independently obtained result | disposition |
|---|---|---|
| `t=0` | identity, every fibre one | separate theorem branch |
| `1<=t<=e-2` | `k>=1`; target-coordinate and square-root formula valid | PASS |
| `t=e-1` | `k=0`; sole target zero, fibre `p^(e-1)` | PASS |
| `t>=e` | still constant zero; fibre remains `p^(e-1)`, **not** `p^t` | mandatory correction boundary |
| `e=2` | identity at `t=0`, constant zero from `t=1`; inner ball singleton | PASS |
| target not divisible by `p^(t+1)` | empty fibre | PASS |
| divisible target with nonsquare transported discriminant | also empty | distinct from preceding cause |
| discriminant zero, `k>=1` | one target, fibre `p^(t+floor(k/2))` | PASS |
| zero target, `k>=1` | transported discriminant is `1`, so fibre `2p^t`; it is not the exceptional target | PASS |
| full inner support | `p^2 Z/p^e Z`; at `e=2` it is `{0}` | PASS |

Oddness of `p` is essential to the discriminant parametrization and the
square census.  No assertion is made for `p=2`.

## 4. Koenigs-chart attack

Let `G(x)=product_j(1+F^j(x)/p)` on the inner ball.  The product stabilizes
at every finite precision.  The conjugacy identity follows by shifting the
product.  For isometry, the exact difference factorization is

```text
F(x)-F(y)=(x-y)(x+y+p).
```

Because `x,y` lie in `p^2`, the last factor has valuation one, and induction
gives `v(F^j(x)-F^j(y))=v(x-y)+j`.  Hence
`v(G(x)-G(y))>=v(x-y)-1`.  In

```text
H(x)-H(y)=(x-y)G(x)+y(G(x)-G(y)),
```

the first summand has valuation `v(x-y)` and the second at least
`v(x-y)+1`; cancellation is impossible.  The claimed isometry, bijection,
image balls, and uniform fibres all follow.  Exact enumeration independently
checks every pair on the tested inner balls.

There is no hidden extension to the whole outer ball: `-p` is a second root
of `F` at valuation one, so a full conjugacy cannot cross that boundary.

## 5. Exact-control result

`verify_reentry.py` starts from `x -> x(x+p) mod p^e`; it does not import the
old QNC verifier.  It exhausts

```text
p=3,  e=2..8;
p=5,  e=2..6;
p=7,  e=2..5;
p=11, e=2..4.
```

It checks literal iterates, every `phi_s` and `B_t` permutation, independently
enumerated square roots, every target at every relevant time, spectra and both
mass identities, all constant-time boundaries, the finite product, conjugacy,
all-pairs isometry, and inner-ball every-target fibres.  Two fresh executions
are byte-identical to `CANONICAL.txt`.

```text
verifier SHA-256  eff9e9aa4531377145e683462b522c78a90b6414011dc272df0a0e9f44369aaa
stdout SHA-256    518d3a31dcab5c3eac6eb39c16c11133c479f2adeb503752f98d6e468fe855fe
canonical SHA-256 518d3a31dcab5c3eac6eb39c16c11133c479f2adeb503752f98d6e468fe855fe
```

Exact enumeration is falsification pressure only.  It proves neither the
infinite families nor ownership.

## 6. Gate decision

There is no mathematical Critical.  There is one selection-critical finding:
both apparent independent axes are direct consequences of primary general
theorems after specialization.  With those contributions assigned zero
credit, the surviving `B_t^(-1)` coordinate label is too thin for an
anonymous 4--6 page theorem note and too close in silhouette to the already
crowded local-ring inverse portfolio.

**Final verdict: `KILL`.**  The artifact remains a useful exact internal
lemma package, is not a novelty statement, and remains `HOLD_EXTERNAL`.
