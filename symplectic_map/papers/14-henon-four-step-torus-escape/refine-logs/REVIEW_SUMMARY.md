# Review Summary

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Problem

Determine the shortest uniform forward window for which all initial states of

\[
H(x,y)=(b x^d+a y+c,x)
\]

remaining in \(\Gamma^2\), with \(\Gamma\) of finite rank, admit an explicit
bound depending only on \(d\) and \(r\).

## Historical proposal

The starting candidate was a \(b=1\) periodic-point theorem with
\(-1,a,c\in\Gamma\). It proposed

\[
\#\operatorname{Per}_\Gamma(H)
\le
4dE(3,3r)+81d^2.
\]

The proof-first audits found the bound structurally correct but identified a
stronger and cleaner theorem.

## Resolution log

| Round | Concern | Resolution |
|---:|---|---|
| 1 | Periodicity appeared in the statement but nowhere in the proof | promoted \(T_4\) to the main object; periodicity became a corollary |
| 1 | \(\operatorname{Per}(H)\cap\Gamma^2\) could be mistaken for full-orbit containment | defined \(C_n^\Gamma(H)\) only for \(\mathcal O\subseteq\Gamma^2\) and used a weighted sum |
| 1 | \(d\ge2\) was implicit | made it explicit in every claim |
| 1 | normalized units seemed to require \(a,c,-1\in\Gamma\) | replaced them by a fixed-coefficient ESS equation |
| 2 | the coefficient of \(x^d\) was normalized away | upgraded to arbitrary \(b\in K^\ast\) |
| 2 | coefficient membership might enlarge rank | kept variables in \(\Gamma^3\) and coefficients in \(K^\ast\), preserving rank \(3r\) |
| 2 | two \(A/B/C\) conventions were in circulation | locked \(A:a x_{i-1}+c=0\), \(B:b x_i^d+c=0\), \(C:b x_i^d+a x_{i-1}=0\) |
| 2 | free degeneracies needed exhaustive closure | wrote all nine transitions, \(BA\) closure, \(CB\) closure, and exceptional \(CBA\) fourth step |
| 2 | simultaneous degeneracy could cause missing or duplicate cases | proved all pair intersections and used a union bound |
| 2 | periods below four might wrap indices | recorded that distinctness is never assumed |
| 2 | four steps might be an artifact | produced an infinite rank-one \(T_3\) family for every \(d\ge2\) |
| 2 | recent Hénon and higher-dimensional work might collide | locked exact primary-source boundaries, including Ji--Xie--Zhang and Mello--Yasufuku |

## Final theorem selected

For every characteristic-zero field \(K\), every \(d\ge2\), every
\(a,b,c\in K^\ast\), and every finite-rank
\(\Gamma\le K^\ast\) of rank \(r\),

\[
\boxed{
\#T_4(H,\Gamma)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
}
\]

There is no coefficient-membership assumption.

For every \(d\ge2\), a rank-one example has infinite \(T_3\).

If \(C_n^\Gamma(H)\) counts exact-period orbits contained in \(\Gamma^2\),

\[
\boxed{
\sum_{n\ge1}nC_n^\Gamma(H)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
}
\]

## Proof closure summary

### Nondegenerate part

The equation

\[
\frac1c x_{i+1}
-\frac bc x_i^d
-\frac ac x_{i-1}=1
\]

uses a rank-\(3r\) variable group and fixed coefficients. ESS gives at most
\(\exp(18^9(3r+1))\) nondegenerate triples. Each has at most \(d\) choices
of \(x_i\), and there are four local indices.

### Degenerate part

The nine adjacent transitions leave only \(BA\) and \(CB\) free. Every
\(BA\) prefix closes at length three. Every \(CB\) prefix closes at length
three except \(CBA\), which requires

\[
a=-1,\qquad bc^{d-1}=-1
\]

and closes at length four. Each four-letter word has at most \(d^2\) initial
states, hence the \(81d^2\) term.

### Sharpness

With

\[
b=1,\quad a=-1,\quad c^{d-1}=-1,\quad
\Gamma=\langle2,c,-1\rangle,
\]

the states \(P_t=(t,t^d)\), \(t=2^n\), give infinitely many points of
\(T_3\). In the locked convention this is the \(CBA\) free chain.

## Two independent assessment records

### Assessment A

- novelty: **7.0/10**
- standalone size: **6.0--6.5/10**
- proof confidence: **9.5/10**
- decision: **GO after minor formal repair**

### Assessment B

- novelty: **7.0/10**
- standalone size: **6.0--6.3/10**
- proof confidence: **9.7/10**
- decision: **GO with source-package corrections**

The assessments agree that the periodic-only framing would be too small and
that the \(T_4/T_3\) threshold is the publishable center. They were performed
independently but are not represented as cross-model validation.

## Novelty boundary

The ESS theorem is a direct classical input. The closest adjacent literatures
are:

- one-dimensional \(S\)-unit dynamics and good-reduction bounds;
- multiplicative dependence in univariate iterates modulo finitely generated
  groups;
- hitting-time structure for fixed dynamical sequences;
- integral-point non-density in fixed higher-dimensional orbits;
- common-zero non-density for Hénon-type maps;
- cyclotomic Hénon periodic-point non-density;
- Hénon constructions with many integral periodic points;
- 2026 higher-dimensional semigroup multiplicative dependence.

No direct theorem with the combined four-step, coefficient-uniform,
finite-rank, explicit-bound, rank-one-sharpness scope was found in the
targeted primary-source search through 2026-08-16.

## Held-back propositions

The following remain pending and may not appear as theorems:

- a complete classification of infinite \(T_3\);
- a \(T_2/T_3\) coefficient hierarchy;
- optimality of \(81d^2\);
- optimality of the ESS constant;
- all equality cases.

## Complete nonclaim record

No claim is made about:

- all rational points;
- all integral points;
- all periodic points having one coordinate pair in \(\Gamma^2\);
- \(d=1\);
- positive characteristic;
- \(abc=0\);
- arbitrary polynomial Hénon maps;
- additive closure of \(\Gamma\);
- finite generation of \(\Gamma\);
- optimal constants;
- effective algorithms;
- height bounds;
- computational verification;
- numerical, prime, modulus, finite-field, or parameter scans;
- absolute priority;
- a full \(T_2/T_3\) classification;
- periodicity of the sharp \(T_3\) family;
- realizability of all degeneracy words;
- any quartic Paper 15 theorem.

## Paper 15 reserve

The quartic sharp-cutoff candidate is explicitly reserved for Paper 15. It is
not merged into the present theorem, not used as evidence, and not covered by
the present scores.

## Final disposition

**GO to independent source review, with no authorization for code, results,
source lock, review artifact, or manuscript.**

The present source package has a complete author-side proof but remains
pending an independent replay of the proof and citations.

