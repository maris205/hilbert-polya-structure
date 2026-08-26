# Paper 16 research protocol

Status: **PHASE-1 USER-CONFIRMED / BLOCKED BY PAPER 15**  
Version: `P16-P1-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Working title: **Arveson Reconstruction of Prime Clocks from Mixed Periodic Flows**  
Route B, proof implementation, controls, Route A, manuscript, release, and
Git/public synchronization: false

Batch design lock:

```text
sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
```

## 1. Dependency and research question

Paper 16 begins only after Paper 15 proves and freezes the mixed standardized
owner.  It asks:

> Does the unlabeled `R`-C*-dynamical system of the mixed standardized
> periodic components intrinsically recover its component decomposition and
> every numerical period through restricted Arveson spectra?

The candidate is analytic but owner-limited: it belongs to the standardized
record, never to the actual indiscrete topology.

## 2. Registered owner

For a nonempty bare orbit set `Q` and positive periods `L_q`, put

```text
O_q = R/(L_q Z),
X_std = coproduct_{q in Q} O_q,
A = C_0(X_std) = direct_sum^{c0}_{q in Q} C(O_q).
```

The strongly continuous action is the translation action

```text
(alpha_t f)(x)=f(x.t)
```

with one fixed sign convention to be selected and tested against Fourier
modes.  Write `A_q=C(O_q)` for the component ideal.

No origin in `O_q`, enumeration of `Q`, prime tag, product topology on `Q`,
or topology from the actual packet is part of this owner.

## 3. Proposed intrinsic reconstruction

The proof must establish, without using the displayed direct-sum labels as
the definition of the answer:

1. the minimal nonzero closed `alpha`-invariant ideals of `A` are exactly
   the component ideals;
2. every equivariant C*-isomorphism permutes those ideals;
3. the restricted Arveson spectrum satisfies

   ```text
   Sp(alpha|A_q) = (2 pi/L_q) Z
   ```

   with the exact sign convention irrelevant only after taking the symmetric
   lattice;
4. the primitive positive spectral generator recovers

   ```text
   L_q = 2 pi / min(Sp(alpha|A_q) cap R_{>0});
   ```

5. equality, multiplicity, and permutation of repeated periods are
   classified; and
6. forgetting the action while retaining only the commutative algebra loses
   the numerical period, with an explicit dilation isomorphism as control.

The invariant must be formulated intrinsically enough that an isomorphic
unlabeled dynamical system yields the same multiset of periods.

## 4. Fixed-prime application

After Paper 15 supplies `L_p=log(p)`, the reconstruction yields

```text
p = exp(L_p).
```

The arithmetic corollary must distinguish:

- reconstructing the numerical period and then observing that its
  exponential is prime;
- selecting the prime set from a generic clock family; and
- recovering any determinant, trace weight, or zeta factor.

Only the first is proposed.  The generic theorem accepts arbitrary positive
clocks, including composites and nonarithmetic labels.

## 5. Candidate claim ledger

| ID | Candidate claim | Phase-1 status |
|---|---|---|
| P16-1 | Strong continuity and exact owner/domain for the translation action. | BLOCKED BY P15 |
| P16-2 | Minimal nonzero invariant ideals equal orbit components. | SPECIFIED / UNPROVED |
| P16-3 | Exact restricted Arveson spectrum lattice. | SPECIFIED / UNPROVED |
| P16-4 | Intrinsic period reconstruction and equivariant-isomorphism invariance. | CENTRAL / UNPROVED |
| P16-5 | Prime-clock corollary without external component labels. | BLOCKED BY P15 |
| P16-6 | Action-forgetting and arbitrary-clock falsifiers. | DESIGN UNAUTHORIZED |

## 6. Source and terminology boundary

Arveson's primary spectral theory for one-parameter automorphism groups is a
mandatory source stratum.  The final source audit must freeze:

- the exact definition of spectrum used here;
- whether full, strong, point, or Connes spectra are being distinguished;
- the restriction theorem for invariant ideals, if cited rather than proved;
- the relationship between Fourier spectral subspaces and the asserted
  lattice; and
- all separability or sigma-unital hypotheses.

No unqualified use of `spectrum` is permitted.  A direct Fourier proof must
still be compared with the named standard theory.

## 7. Nonredundancy and standalone gate

The following are insufficient centers:

- the elementary Fourier spectrum of one circle;
- the direct-sum decomposition written with labels already attached;
- the Paper-12 stabilizer formula restated after Fourier transform;
- unmarked isomorphism of circles or component algebras; or
- another generic constant-diagonal/corona lemma.

Standalone eligibility requires the unlabeled minimal-invariant-ideal
reconstruction, the exact action-spectrum recovery theorem, the arithmetic
application, and an independent audit showing that their conjunction is not
routine reduction to Paper 12 plus elementary Fourier series.

If that audit fails, Paper 16 is merged into Paper 15.  It is not consumed as
the batch's sole Technical Note merely to preserve numbering.

## 8. Phase gates

Paper 15's exact proof and independent review are prerequisites.  Paper 16
then requires methodology, source, and devil/domain reviews of this protocol
before proof authorization.  Controls and Route follow only after symbolic
proof.  Route B, manuscript, release, and Git/public synchronization remain
false.
