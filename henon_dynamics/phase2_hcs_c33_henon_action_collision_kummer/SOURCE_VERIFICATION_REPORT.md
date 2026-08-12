# HCS-C33 source verification and novelty report

**Date:** 2026-08-12 UTC
**Direct duplicate:** `NOT_FOUND_WITHIN_SEARCH_BOUNDS`
**Generic mechanism collision:** `CONFIRMED`
**Phase-2 verdict:** `GO_TO_EXACT_PHASE3_WITH_SCOPED_CLAIMS`

## 1. Decisive finding

The strongest defensible claim is not that C33 discovers equal-action Hénon
orbits, Maxwell strata, Hill's formula, or Kummer monodromy.  All of those
have direct or close prior art.

The surviving candidate increment is the exact coupled theorem

\[
\boxed{
\begin{gathered}
\operatorname{Disc}_c W_5
=2^{12}3^{30}A^{60}P_2^5P_5^3P_9^2,\\
P_9\perp P_2P_5,\qquad
\operatorname{Gal}(P_9/\mathbb Q)\cong S_9,\\
\text{generic }P_9\text{ point}
=\text{two distinct nonparabolic exact-period-five points}\\
\text{whose action-image branches form a transverse ordinary node},\\
u^2=N_H,\qquad N_H=h_1h_2,qquad
[N_H]\ne1\text{ in }K_9^\times/K_9^{\times2}.
\end{gathered}}
\]

No source in the frozen corpus contains this specific Hénon
action-image-node/Hill-square-class construction.

## 2. What the literature kills

### 2.1 The degree-six normalization is old

Endler--Gallas and Brison--Gallas already give the period-five orbit sextic,
its number-field structure, discriminant/Galois information, and polynomial
equivalences.  Since \(W_5(A,c)\) has the same function field, neither its
normalization nor its ordinary \(S_6\) cover can be claimed as new.

### 2.2 A Hénon action is old

Generating functions and action principles for reversible symplectic maps
are established.  Shudo writes the quantum-Hénon action explicitly and uses
distinct saddles with equal action to define virtual turning points.  The
phrase “first equal-action Hénon collision” is therefore forbidden.

### 2.3 A Maxwell factor is generic

In the Lyashko--Looijenga convention used here, the locus where distinct
Morse critical points have equal critical value is a Maxwell stratum (or,
more neutrally, an equal-critical-value stratum); a caustic is the
Hessian-degenerate locus.  Some catastrophe-theory sources reserve “Maxwell
set” for equal global minima, and C33 makes no minima claim.  Therefore the
fact that \(P_9\) occurs squared in the critical-value discriminant is
structurally expected.  Its exact Hénon equation and dynamical decoration
may be new; the mechanism is not.  Godwin's exact Maxwell-set calculations
also show that an iterated discriminant/elimination procedure is established
methodology and that minima conditions may require a further real-root
screen.

### 2.4 Symmetric critical-value monodromy is old

Lyashko--Looijenga theory already studies Galois and braid monodromy of
critical values.  The abstract appearance of a symmetric group cannot be
advertised as new.  Only the explicit \(P_9\) specialization and its exact
proof are candidate contributions.

### 2.5 Hill and Kummer are separate prior art

The action-Hessian/monodromy determinant identity is the discrete Hill
formula.  Kummer covers and their braid monodromy are also established.  The
surviving question is whether the intrinsic Hénon Hill values define a
nontrivial square class after descent to this exact Maxwell component.

### 2.6 Parabolic period-five bifurcations are old

MacKay--Shardlow already formulate periodic-orbit degeneracy for
area-preserving maps through \(\det(Df^q-I)=0\), including the period-five
Hénon regime.  Thus the caustic/parabolic side of the discriminant is not a
novelty opening.  The C33 distinction is the exact coprimality of \(P_9\)
with the old marker/Hill-zero factors and the survival of two nondegenerate
branches.

## 3. Why the coupled object still survives

The closest Hénon source, Shudo's Stokes work, differs at four decisive
levels:

| Shudo setting | C33 setting |
|---|---|
| fixed initial/final coordinates | closed exact period-five orbits |
| Stokes/virtual turning-point geometry | parameter-space algebraic Maxwell divisor |
| analytic saddle actions | exact characteristic-zero resultant \(P_9\) |
| no branch stability cover | Hill square class \(u^2=h_1h_2\) |

The closest exact-orbit sources, Endler--Gallas, use coordinate sums rather
than the cyclic action and do not compare Hill square classes on an
equal-action branch pair.

The closest generic algebraic sources, Lyashko--Looijenga and Kummer/braid
work, do not specialize to chronological Hénon periodic orbits or use
\(\det(I-DH_A^5)\).

This leaves a nonformal, exactly testable gap.

## 4. Claim-by-claim verification matrix

| Candidate statement | Evidence | Status | Allowed wording |
|---|---|---|---|
| The period-five marker sextic is new | Endler--Gallas 2006; Brison--Gallas 2018 | **REJECTED** | source-locked prior work |
| The action plane model has a new normalization/function field | same sources plus \(\mathbb Q(A,c)=\mathbb Q(A,q)\) pilot | **REJECTED** | birational relabelling of old cover |
| Hénon dynamics admits a discrete generating action | Kook--Meiss; Shudo | **VERIFIED PRIOR ART** | classical input |
| Equal-action Hénon saddles are new | Shudo 2005/2008 | **REJECTED** | closest conceptual precedent exists |
| Distinct Morse critical points with equal value form a Maxwell-type stratum | Żołądek; van Manen; LL literature | **VERIFIED PRIOR ART** | LL equal-critical-value convention; no minima claim |
| Iterated discriminants can determine Maxwell sets | Godwin 1984 | **VERIFIED PRIOR ART** | elimination method is classical |
| \(P_9\) is an exact Hénon equal-action component disjoint from marker/parabolic ramification | no direct source found; Phase-1 exact pilot | **CANDIDATE NEW THEOREM** | search-bounded until Phase-3 certificate |
| \(\operatorname{Gal}(P_9/\mathbb Q)=S_9\) | generic LL monodromy is prior; exact \(P_9\) not found | **CANDIDATE NEW SPECIALIZATION** | not a first symmetric critical-value group |
| Action Hessian equals a signed Hill determinant | Bolotin--Treschev | **VERIFIED PRIOR ART** | exact Hénon specialization only |
| A Kummer cover can carry braid monodromy | Artal et al. | **VERIFIED PRIOR ART** | generic technology |
| \([h_1h_2]\) descends canonically to the \(P_9\) collision field | no direct source found | **CANDIDATE NEW LEMMA** | prove branch/gauge invariance exactly |
| \(N_H\) is nonsquare in \(K_9\) | no direct source found; Phase-1 norm pilot | **CANDIDATE NEW THEOREM** | requires independent exact replay |
| An ordinary equal-value node automatically yields Picard--Lefschetz monodromy | Vassiliev 1995 | **NOT ESTABLISHED** | requires a vanishing-cycle theorem for the actual family |
| The combined Galois group is \(C_2\wr S_9\) | not established | **OPEN / FORBIDDEN** | one nonsquare class does not prove conjugate independence |
| The Kummer cover gives a Ruelle determinant or Hilbert--Pólya operator | no bridge | **REJECTED IN CURRENT SCOPE** | arithmetic structure only |

## 5. Source verification matrix

Metadata were checked against Crossref and, for DOI-bearing core works,
OpenAlex.  Primary content was inspected through publisher, official
repository, author-hosted, MathNet, or arXiv versions.  OpenAlex marked none
of the checked DOI records as retracted on the audit date.

| Source group | Evidence level | Venue/content integrity | Applicability | Grade |
|---|---:|---|---|---:|
| Endler--Gallas 2002/2004/2006; Gallas 2007; Brison--Gallas 2018 | VI | peer-reviewed journal articles; DOI and primary PDF metadata verified | direct exact Hénon orbit-algebra boundary | A |
| Kook--Meiss 1989 | VI | peer-reviewed *Physica D* article; DOI verified | direct reversible symplectic action boundary | A |
| Shudo 2005 | VI | official Kyoto University proceedings PDF | closest equal-action Hénon precedent; fixed-endpoint scope | B+ |
| Shudo--Ikeda 2008 | VI | peer-reviewed *Nonlinearity* article; DOI verified | quantum-Hénon Stokes/virtual-turning-point boundary | A- |
| Looijenga 1974 | VI | peer-reviewed *Inventiones* article; DOI and university record verified | foundational critical-value monodromy | A |
| Zvonkine--Lando 1999 | VI | peer-reviewed journal article; DOI and MathNet verified | direct LL discriminant-stratum theory | A |
| Yu 1999 | VI | peer-reviewed *Mathematische Zeitschrift* article; DOI verified | direct LL Galois boundary | A- |
| Żołądek 2006 | VII | Birkhäuser monograph; DOI/publisher record verified | exact Maxwell-versus-caustic terminology | A |
| van Manen 2007 | VI | reviewed proceedings chapter; DOI verified | generic Maxwell/node background | B+ |
| Bolotin--Treschev 2010 | VI | peer-reviewed survey/research article; DOI and arXiv verified | decisive discrete Hill theorem | A |
| Artal et al. 2014 | VI | peer-reviewed JIMJ article; DOI and arXiv verified | generic Kummer/braid boundary | A |
| Vassiliev 1995 | VI | peer-reviewed *Selecta Mathematica* article; DOI and arXiv verified | stratified Picard--Lefschetz boundary only | A |
| Gonchenko et al. 2021 | VI | peer-reviewed DCDS article; DOI verified | current conservative-Hénon context only | A- |
| de Hénon collective 2024 | VII | peer-reviewed field survey; DOI and arXiv verified | current coverage/negative-search context | A- |
| MacKay--Shardlow 1994 | VI | peer-reviewed BLMS article; DOI and author PDF verified | direct parabolic/periodic-bifurcation boundary | A- |
| Godwin 1984 | VI | peer-reviewed journal article; DOI verified | direct Maxwell-elimination boundary | B+ |
| Qu--Xia 2024 | VI | peer-reviewed JDE article; DOI verified | current action/periodic-orbit context | A- |

No source-level financial conflict is relevant to the mathematical claims.
The main bias risk is conceptual rather than financial: several sources use
nearby terminology for different objects.  The table above records the
applicability boundary explicitly.

## 6. Allowed novelty statement

Until Phase 3 independently reproduces the pilot, the strongest allowed
statement is:

> A primary-source audit found no prior construction, within the documented
> search bounds, of the exact degree-nine period-five Hénon equal-action
> divisor together with the quadratic square class obtained from the two
> branches' chronological Hill determinants.  Each generic ingredient has
> prior art, and the period-five normalization itself is known.

The words “first”, “unique”, and “unprecedented” remain prohibited.

## 7. Phase-3 authorization gate

Phase 2 recommends one exact experiment because the candidate contribution
is now sharply separated from prior art.  Phase 3 must stop if any of the
following fail:

1. reconstruct \(G_A\), \(W_5\), \(P_2\), \(P_5\), and \(P_9\) from the
   chronological recurrence, not hard-coded verdicts;
2. prove the two action-image branches over generic \(P_9\) form a
   transverse ordinary node;
3. prove both branches remain nonparabolic;
4. prove branch-exchange and generating-action gauge invariance of
   \([h_1h_2]\);
5. prove \(N_H\notin K_9^{\times2}\) by an independently checked exact norm
   or equivalent local valuation certificate;
6. replay all four structurally selected primes dividing \(P_9(6)\), with
   \(61\) labelled post-hoc and \(3203\) used as the adversarial nonsquare
   control;
7. keep the full-wreath, Picard--Lefschetz, zeta, and Hilbert--Pólya claims
   outside the theorem.

## 8. Route-A status at the literature gate

No formal Route-A evaluator is invoked in Phase 2 because there is not yet a
released computational candidate with a clock, all-length orbit law, or
analytic determinant.  The honest status is `NOT_YET_TESTABLE`.

An informal ceiling is

\[
(A1\_\mathrm{WEAK},\ A2\_\mathrm{FAIL},\ A3\_\mathrm{FAIL},\
A4\_\mathrm{FORMAL\_HINT}).
\]

- A1 is weak only because the branches are genuine chronological Hénon
  periodic orbits; one fixed period gives no prime-orbit law.
- A2 and A3 fail because a degree-nine parameter divisor is not a dynamical
  zeta function, analytic Fredholm determinant, or critical-line theorem.
- A4 is only a formal arithmetic hint: the Hill-Kummer cover may retain
  stability information, but it supplies no self-adjoint operator.

Route B remains unauthorized.

## 9. Phase-2 verdict

\[
\boxed{\texttt{GO\_TO\_EXACT\_PHASE3\_WITH\_SCOPED\_CLAIMS}}
\]

This is a meaningful large-door continuation.  It is not a positive
Hilbert--Pólya verdict.  If the exact Kummer descent or nonsquare theorem
fails, C33 should stop rather than retreat into further low-period scans.
