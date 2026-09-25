# Strict one-sided causality forces periodic rigidity

**Paper ID:** 051-strict-causality-periodic-rigidity  
**Record ID:** ASFS-METHOD-20260914-05  
**Date / status:** 2026-09-14; METHOD THEOREM / PRE-P0 STOP RULE — STRICTLY CAUSAL AUTONOMOUS PRIME CODINGS HAVE NO NONTRIVIAL PERIODIC ORBITS  
**Route state:** No candidate; Route A not evaluated; Route B NOT INVOKED

## Abstract

A one-sided prime-symbolic rule is often attractive because it decides the
status of integer n from earlier arithmetic data. This paper records the exact
cost of making that dependence strictly causal. For a self-map T of A^N whose
nth output depends only on input coordinates below n, every periodic point is
forced coordinate by coordinate. Consequently T has at most one periodic
point; if it has a fixed point, that point is its entire periodic set. Applied
to 050, this proves the prime indicator is not merely a unique fixed point but
the sole periodic configuration. The result is a rapid A1 stop rule, not a
claim about noncausal, two-sided, reversible, or symplectic systems.

## 1. Definition

Let A be a set and T:A^N -> A^N. Call T strictly causal when, for each n>=0,
there is a function f_n:A^n -> A such that

(Tx)_n = f_n(x_0,...,x_(n-1)).

For n=0, f_0 is a constant. No continuity, finite alphabet, locality, or
arithmetic assumption is needed.

## 2. Periodic-rigidity theorem

**Theorem.** A strictly causal T has at most one periodic point. If T has a
fixed point x*, then every periodic point equals x*.

**Proof.** Let x be periodic, T^r x=x. At coordinate zero, (Tx)_0=f_0 is a
constant c. Hence (T^r x)_0=c, so x_0=c. If x* is fixed, x*_0=c as well.

Assume inductively that x_j=x*_j for every j<n. Strict causality gives
(Tx)_n=f_n(x_0,...,x_(n-1))=f_n(x*_0,...,x*_(n-1))=(Tx*)_n=x*_n.
Moreover, applying T repeatedly preserves agreement with x* at all indices
below n by the same lower-index argument. Hence (T^r x)_n=x*_n; periodicity
gives x_n=x*_n. Induction proves x=x*.

If no fixed point is specified, let x and y have periods r and s and take a
common multiple L. At coordinate zero both equal the constant f_0; the same
induction, now using T^Lx=x and T^Ly=y, shows x_n=y_n for every n. This proves
uniqueness. Since T maps a periodic point to a periodic point, that sole point
is automatically fixed. ∎

## 3. Application to the causal prime sieve

In 050, G[Q](n) reads only entries Q(m) with m<=sqrt(n)<n. It is therefore
strictly causal. The source proves p is fixed, so the theorem proves that p is
the complete periodic set of G. No direct enumeration, finite cutoff, or
borrowed orbit convention is involved.

## 4. Gate and search consequence

| Item | Consequence |
| --- | --- |
| A0 | strict causality can still give a fully endogenous prime mechanism, as in 050 |
| A1 | fails whenever a nontrivial primitive-orbit family is required: there is at most one periodic point |
| Permitted future fork | break strict one-sided causality with a defined recurrent state, not with an external wheel, precomputed schedule, or unrelated periodic component |
| Symplectic/analytic fields | absent; this rule grants none |

## 5. Decision

**Apply as a fast stop rule.** A new proposal claiming both causal
prime-indicator generation and nontrivial periodic dynamics must identify the
precise coordinate dependence that evades this theorem. Otherwise stop it
before P0. The theorem does not license a reverse-time completion, a
cotangent lift, or any other new object to inherit 050's arithmetic credit.

## Reproducibility / evidence index

The proof is fully contained above. The concrete source rule is linked through
[050](../../050-causal-binary-sieve-fixed-point-screen/paper.md).
