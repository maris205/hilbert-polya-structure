# A reversible causal sieve generates the prime word on a nonreturning orbit

**Paper ID:** `131-second-order-causal-sieve`  
**Candidate ID:** `ASFS-SCOUT-20260914-95`  
**Date / evidence:** 2026-09-14; exact elementary proofs with finite diagnostics.  
**Status:** `PRE-P0 STOP — REVERSIBLE PRIME GENERATION; ZERO-SEED ORBIT HAS UNBOUNDED PROJECTED PERIODS`  
**Route:** classical A0/A1/A2 `UNASSIGNED`; formal Route A not evaluated;
Route B `NOT INVOKED`.

## Abstract

The causal sieve of 050 is deformed into the autonomous two-register action
\(R(x,y)=(y,x\mathbin\oplus G(y))\). This action is a homeomorphism of a
compact binary product. Its zero-seed orbit reaches the complete prime
indicator after two updates, so reversibility has not removed the elementary
arithmetic-generation mechanism. However, along the coordinates indexed by
powers of two, the very same seed orbit contains finite factors of primitive
period \(2^{K+1}\) for every positive integer \(K\). Consequently it is not
periodic. Finite-cutoff cycles therefore do not supply a closed packet for the
infinite prime-generating orbit. This is a seed-specific stop, with the full
periodic set for other initial conditions left open.

## 1. Frozen object and ownership

Let \(X=\{0,1\}^{\mathbb N_{\ge2}}\), with its product topology and
coordinatewise XOR. For every candidate word \(y\), define

\[
G(y)_n=\prod_{\substack{2\le d\le\lfloor\sqrt n\rfloor\\d\mid n}}(1-y_d),
\qquad R(x,y)=(y,x\oplus G(y)).
\]

An empty product is one. There is no prime list, cutoff, adjustable parameter,
or arithmetic schedule in this definition. Write \(\mathbf0,\mathbf1\)
for the constant words and \(\pi\) for the prime indicator used only in the
conclusions of proofs.

| Field | Owner / definition | Audit |
| --- | --- | --- |
| Carrier | \(X\times X\) | compact binary product; symbolic source screen |
| Action | the exact \(R\) above | homeomorphism, Proposition 1 |
| Arithmetic | candidate-support divisibility exclusion inside \(G\) | retained as an explicit deformation of 050 |
| Selected generation seed | \((\mathbf0,\mathbf0)\) | arithmetic-independent control seed |
| Full packets | all states fixed by \(R^r\); primitive least \(r\), cyclic phase quotient | global set `OPEN`; zero-seed orbit excluded |
| Clock | discrete update count | no positive roof or suspension selected |
| Symplectic base / smooth structure | not supplied | `NOT APPLICABLE` to this screen |
| Trace / zeta / transfer operator | not supplied | no owner-level analytic claim |
| Later geometric owner | `OPEN` | no credit inherited from 050 or a geometric comparator |

The documented lineage arrow is prime/composite exclusion in 050 -> a
two-register autonomous reversible-memory deformation of that same formula.
This is a concrete symbolic connection to the
[prior-work lineage](../../docs/prior_work/README.md). It supplies neither the
Logistic/Hénon geometric arrow nor a classical symplectic P0 object. The
`ASFS-SCOUT` ID denotes a Pre-P0 screen; it is not an ALF/ANG flow or a claim
that all broadened-carrier gates have been admitted.

## 2. Research question and claim boundary

Can this precise memory deformation preserve endogenous prime generation and
make that generating orbit a nontrivial closed packet?

The answer for the arithmetic-independent zero seed is exact: prime generation
is preserved, but the full orbit is not periodic. The proof below does not say
that \(R\) has no periodic states whatsoever. It does not select another
initial word, add a roof, quotient away coordinates, or change the formula to
rescue this failed mechanism.

## 3. Inverse and arithmetic retention

**Proposition 1 (same-map reversibility).** The inverse is

\[
R^{-1}(u,v)=(v\oplus G(u),u).
\]

**Proof.** Applying either composition cancels the two occurrences of
\(G\) by XOR. Each coordinate of \(G\) depends on finitely many coordinates,
so \(G\), \(R\), and this inverse are continuous. The carrier is compact
and the map is a homeomorphism. This gives no smooth symplectic structure.

The strict-causality obstruction in
[051](../051-strict-causality-periodic-rigidity/paper.md) does not directly
apply: each new second-register coordinate retains the corresponding old
first-register coordinate. Its periodic-rigidity conclusion therefore cannot
be transferred from \(G\) to \(R\).

**Proposition 2 (prime word generated from zero).**

\[
R(\mathbf0,\mathbf0)=(\mathbf0,\mathbf1),\qquad
R^2(\mathbf0,\mathbf0)=(\mathbf1,\pi).
\]

**Proof.** \(G(\mathbf0)=\mathbf1\). Also \(G(\mathbf1)_n=1\) precisely
when no integer \(2\le d\le\sqrt n\) divides \(n\), which is precisely
primality: a composite factorization has a factor in that range. No prime
word was used as an input. This is a source-level arithmetic positive result
for \(R\) itself. It does not prove prime data are invariant under \(R\),
nor that the generating orbit returns.

## 4. An exact infinite-state nonreturn proof

Let \(z_0=z_1=\mathbf0\), so that

\[
z_{t+2}=z_t\oplus G(z_{t+1}),\qquad
R^t(\mathbf0,\mathbf0)=(z_t,z_{t+1}).
\]

For each positive integer \(m\), set \(b_m(t)=(z_t)_{2^m}\). All divisors
of \(2^m\) are powers of two, hence these coordinates form an exact factor
of this orbit and satisfy

\[
b_m(t+2)=b_m(t)\oplus
\prod_{a=1}^{\lfloor m/2\rfloor}(1-b_a(t+1)).
\tag{1}
\]

Selecting powers of two here is a diagnostic projection after the full map was
frozen. It does not select a prime-sized carrier or alter its definition.

**Lemma 3 (dyadic exponent blocks).** For every \(j\ge0\), all coordinates
\(b_m(t)\) with \(2^j\le m<2^{j+1}\) coincide for all \(t\ge0\).
Denote their common value by \(A_j(t)\). Then

\[
A_j(t+2)=A_j(t)\oplus\prod_{i<j}(1-A_i(t+1)).
\tag{2}
\]

**Proof.** All blocks coincide at times zero and one. If \(m\) lies in
block \(j\ge1\), the indices \(1\le a\le\lfloor m/2\rfloor\)
in (1) contain all lower blocks before \(j-1\) and a nonempty part of block
\(j-1\), and no higher block. Products of repeated equal binary factors
are unchanged. Thus, assuming block equality at the two preceding times,
the forcing is exactly the product in (2), independent of \(m\) within its
block. For \(j=0\) the product is empty. Induction in time proves the claim.

**Theorem 4 (unbounded projected primitive periods).** For every \(K\ge1\),
the first \(K\) dyadic block bits of the zero-seed pair have primitive
period \(2^{K+1}\). The full orbit of \((\mathbf0,\mathbf0)\) is not
periodic.

**Proof.** Put \(M=2^K\) and encode the first \(K\) bits as
\(U_t=\sum_{j=0}^{K-1}2^j A_j(t)\), using representatives modulo \(M\).
For a binary integer \(u\), the \(j\)-th bit of
\(u\oplus(u-1)\) is one precisely when all its lower bits are zero.
Here subtraction is modulo \(M\), including \(u=0\). Equation (2) is
therefore exactly

\[
U_{t+2}=U_t\oplus U_{t+1}\oplus(U_{t+1}-1)\pmod M.
\tag{3}
\]

Its zero-seed solution is

\[
U_{2k}=-k\pmod M,\qquad U_{2k+1}=k\pmod M.
\tag{4}
\]

For verification, within \(K\) bits \(-k\) is the bitwise complement
of \(k-1\). Substitution into (3) first gives the complement of \(k\),
namely \(-(k+1)\); the following update gives \(k+1\). This proves (4)
by induction from \(U_0=U_1=0\).

At even time \(2k\), the pair is \((-k,k)\), which returns to \((0,0)\)
exactly when \(M\mid k\). At odd time it is \((k,-k-1)\), whose two
entries cannot both vanish because \(M\ge2\). The least return time is
thus \(2M=2^{K+1}\). Any full-state period would be divisible by this
number for every \(K\), which no positive integer is. ∎

In particular, the state \((\mathbf1,\pi)\) produced by the second update
is on this same nonperiodic orbit. Invertibility rules out its being merely a
transient entering a later periodic cycle.

## 5. Finite diagnostics and their limits

Exact integer-bitset computations, specified in the
[evidence record](evidence/README.md), give the zero-seed cutoff periods:

| Largest coordinate \(N\) | 3 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 1024 | 4096 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Computed least return | 4 | 8 | 8 | 16 | 16 | 16 | 16 | 32 | 32 | 32 |

These are complete returns of the specified finite seed orbits, not a count
of every finite periodic orbit. The plateau from 16 through 128 does not
persist at 256. Theorem 4, rather than finite enumeration, proves the infinite
obstruction. No general formula for all full-coordinate cutoff periods is
claimed from this table.

## 6. Controls and adverse findings

1. **Prime-input control.** Both initial registers are constant zero; the
   intermediate prime word follows from divisibility, not a supplied table.
2. **Nonarithmetic reversible controls.** Replacing \(G\) by the constant
   zero rule gives the register swap with period at most two. Replacing it by
   the constant one rule gives period four in each bit pair. Thus the inverse
   formula and existence of finite cycles alone would prove too much: both
   hold without arithmetic. These comparisons do not change the frozen map.
3. **Finite/infinite ownership control.** A return after 16 or 32 updates at
   bounded \(N\) cannot be credited to the complete carrier; its own exact
   factors force unbounded required return periods.
4. **Observable/action control.** Recovering \(\pi\) at the second update
   does not make \(G\)'s fixed point a fixed point or closed orbit of \(R\).
   The map in Proposition 1 remains the sole owner throughout the audit.
5. **Geometric control.** No finite binary packet is thickened into disks or
   called a zero-dimensional symplectic realization. A positive-dimensional
   conservative lift and its full periodic multiplicity ledger remain absent.

All computations use exact integers, so numerical precision and zero fitting
are inapplicable. No roof, prime-power orbit length, or trace normalization is
selected. The proof does not settle whether other initial conditions yield
periodic states carrying a meaningfully generated prime observable; that
question remains `OPEN` after this bounded audit.

## 7. Gate assessment and decision

| Item | Evidence | Status |
| --- | --- | --- |
| Source-level arithmetic | exact zero-seed generation of \(\pi\) inside \(R\) | established positive control |
| Source-level recurrence for that mechanism | Theorem 4 | scoped fail: no zero-seed closed packet |
| Other complete-state periodic packets | no classification supplied | `OPEN` |
| Classical P0 / A0 / A1 / A2 | no smooth symplectic base, roof, or analytic owner | `UNASSIGNED`; not evaluated |
| Broadened flow / T0–T3 | no type-labelled flow construction admitted | not evaluated; only symbolic source results above |
| Formal Route B | no Route-A readiness | `NOT INVOKED` |

**Decision: stop / fork.** Stop this zero-seed reversible-sieve mechanism at
its exact recurrence obstruction. Its arithmetic-positive result is retained
as a design control. A newly proposed orbit-selection mechanism, changed rule,
or geometric realization must be separately frozen and must establish its own
arithmetic and full-periodic-state ownership. This package grants no inherited
gate credit to such a proposal.

## Reproducibility / evidence index

The [candidate card](candidate-card.md) predates the audit; its update is
append-only. The [claim ledger](claim-ledger.md) scopes every positive and
negative statement. The [evidence index](evidence/README.md) records the local
source dependencies, finite diagnostic method and exact output, and limits.
