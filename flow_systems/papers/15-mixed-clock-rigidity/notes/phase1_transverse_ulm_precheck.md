# Paper 15 Phase-1 transverse Pontryagin/Ulm replacement precheck

Date: **2026-08-16 (Asia/Shanghai)**  
Mode: **ARS mathematical/domain/source fail-fast**  
Disposition: **GO_TO_NEW_PHASE1_PROTOCOL — replacement feasible; old standalone centre superseded**  
Findings: **C0 / M0 / m0**  
Standalone ceiling: **FULL PAPER PLAUSIBLE / NOT A STANDALONE_PASS**  
Universal recovery of the base prime from the bare compact group:
**OPEN AT THIS GATE**

Proof implementation, deterministic controls, Route evaluation, manuscript,
release, archive, Git, and public synchronization are **not authorized by
this report**.

## 1. Exact frozen inputs and authority

This report is bound to exactly the following current bytes:

    Papers 14--18 batch design lock
      2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
    Old Paper 15 research protocol
      53e023e427616e5bd98852181495c6598940e2eb238f100482f3abc7011ca59c
    Old Paper 15 mathematical precheck
      1598569c48d4382408bb3df933a1c5443984daf36b12e6377bae4590356a75f8

The batch lock authorized bounded proof/source fail-fast work but did not
authorize a proof, controls, manuscript, Route, or Git operation.  The old
Paper-15 precheck proved that the declared prime-clock centre reduces to

    min(S)>0 and cS=S  implies  c=1,

so that centre does not clear the standalone gate.  This transverse
precheck does not repair or silently revise that protocol.  It records the
following disposition:

1. the old standalone Paper 15, Mixed Prime-Clock Standardization and Global
   Scaling Rigidity, is **SUPERSEDED AS A STANDALONE PROJECT**;
2. its correct mixed-lattice standardization and scaled-isomorphism package
   is **NOTE_OR_MERGE into Paper 16** as categorical groundwork for the
   Arveson reconstruction project;
3. the candidate compact-group project below is a **replacement Paper 15**
   and requires a fresh, separately frozen Phase-1 research protocol; and
4. this report authorizes only the transition
   **GO_TO_NEW_PHASE1_PROTOCOL**.  It is not itself that protocol.

The compact quotient considered below is an abstract compact owner.  It
must not be identified with Paper 9's actual indiscrete packet quotient.

## 2. Exact owner and notation

For a rational prime \(p\), put

\[
U_p=\prod_{\ell\ne p}\mathbf Z_\ell^\times,\qquad
H_p=p^{\widehat{\mathbf Z}}\subset U_p,\qquad
B_p=U_p/H_p .
\]

Here \(H_p\) is the closed image of the continuous exponent map
\(\widehat{\mathbf Z}\to U_p\), \(n\mapsto p^n\).  The new project concerns
the bare compact topological group \(B_p\), together with a separate audit
of which statements require the marked presentation

\[
H_p\hookrightarrow U_p\twoheadrightarrow B_p.
\]

For every rational prime \(r\), let \(B_{p,(r)}\) denote the characteristic
pro-\(r\) Sylow subgroup of \(B_p\), and define

\[
P_r=\prod_{n\ge1}(C_{r^n})^{\aleph_0},\qquad
S_r=P_r^\wedge
   =\bigoplus_{n\ge1}(C_{r^n})^{(\aleph_0)}.
\]

Write \(C_{r^\infty}\) for the Prüfer \(r\)-group and

\[
K_{p,r}:=\widehat{B_{p,(r)}}.
\]

The candidate title is:

> **Wieferich--Ulm Invariants of the Compact Rational-Witt Packet Bases**

An acceptable less arithmetic title is:

> **Torsion-Closure Signatures of Deninger's Compact Packet Bases**

## 3. Exact defect signature

Define the nonnegative integer

\[
\kappa_r(p)=
\begin{cases}
0,&r=p,\\[1mm]
v_r(p^{r-1}-1)-1,&r\ne p,\ r\text{ odd},\\[1mm]
v_2(p^2-1)-3,&r=2\ne p.
\end{cases}
\tag{3.1}
\]

The exceptional \(r=p\) clause is load-bearing: the local \(p\)-coordinate
is omitted from \(U_p\), so the displayed off-local Fermat-quotient formula
must not be applied at \(r=p\).  For odd \(p\),
\(v_2(p^2-1)\ge3\), hence the last branch is also nonnegative.

The vector

\[
\boldsymbol\kappa(p)=(\kappa_r(p))_{r\ {\rm prime}}
\tag{3.2}
\]

is called the candidate **Wieferich--Ulm signature**.

## 4. Candidate exact classification theorem

The following is the exact theorem package derived in this precheck.  Its
proof must be rebuilt and independently reviewed under the new protocol
before it may be marked proved.

### Theorem A — exponent embedding and Sylow structure

The exponent map is injective, so

\[
H_p\cong\widehat{\mathbf Z}.
\tag{4.1}
\]

For every prime \(r\),

\[
U_{p,(r)}\cong
\begin{cases}
P_r,&r=p,\\
\mathbf Z_r\times P_r,&r\ne p.
\end{cases}
\tag{4.2}
\]

For \(r=2\ne p\), the literal local factor is
\(C_2\times\mathbf Z_2\); its \(C_2\) is absorbed by the already countably
infinite family of \(C_2\)-factors in \(P_2\).  A final proof must retain
the local sign in the restriction-map calculation even if it uses the
abstract isomorphism (4.2).

### Theorem B — dual and Ulm classification

For every finite \(n\),

\[
u_n(K_{p,r})=\aleph_0.
\tag{4.3}
\]

Its infinite-height subgroup is exactly

\[
r^\omega K_{p,r}
:=\bigcap_{m\ge0}r^mK_{p,r}
\cong C_{r^{\kappa_r(p)}}.
\tag{4.4}
\]

If \(\kappa_r(p)>0\), the sole nonzero transfinite Ulm invariant is

\[
u_{\omega+\kappa_r(p)-1}(K_{p,r})=1;
\tag{4.5}
\]

if \(\kappa_r(p)=0\), all transfinite Ulm invariants vanish.

Equivalently, entirely on the compact side,

\[
\overline{\operatorname{Tor}(B_{p,(r)})}\cong P_r
\tag{4.6}
\]

and

\[
B_{p,(r)}
  /\overline{\operatorname{Tor}(B_{p,(r)})}
\cong C_{r^{\kappa_r(p)}}.
\tag{4.7}
\]

Thus the number

\[
\kappa_r(p)=
\log_r\!\left[
B_{p,(r)}:
\overline{\operatorname{Tor}(B_{p,(r)})}
\right]
\tag{4.8}
\]

is intrinsic to the bare compact group.  Both the Sylow subgroup and the
closure of its torsion subgroup are characteristic; no local-coordinate
label or conductor filtration is used in (4.8).

### Theorem C — complete bare-group isomorphism criterion

For rational primes \(p,q\),

\[
\boxed{
B_p\cong_{\rm top}B_q
\quad\Longleftrightarrow\quad
\kappa_r(p)=\kappa_r(q)
\ \text{for every rational prime }r.}
\tag{4.9}
\]

This is a complete classification statement, not merely a sufficient
separation test.  A topological isomorphism preserves the canonical Sylow
prime \(r\); Ulm classification then makes (4.3)--(4.5) complete.

## 5. Proof architecture and load-bearing guards

### 5.1 Injectivity of the exponent map

For \(r\ne p\), the coordinate \(\ell=r\) detects the \(\mathbf Z_r\)
component of \(\widehat{\mathbf Z}\): the rational number \(p>1\) is not a
root of unity in \(\mathbf Z_r^\times\), and its suitable prime-to-\(r\)
power has nonzero \(r\)-adic logarithm.

For \(r=p\), that coordinate is absent.  Bang--Zsigmondy supplies, for
every \(m\ge1\), a prime \(\ell\ne p\) for which
\(\operatorname{ord}_\ell(p)=p^m\).  These away coordinates detect every
finite quotient of \(\mathbf Z_p\).  All Sylow components are therefore
detected and (4.1) follows.

### 5.2 Structure of the ambient Sylow groups

For \(\ell\ne r\), the pro-\(r\) Sylow subgroup of
\(\mathbf Z_\ell^\times\) is the finite cyclic group
\(C_{r^{v_r(\ell-1)}}\).  Dirichlet's theorem gives infinitely many primes
\(\ell\) with \(v_r(\ell-1)=n\), for every \(n\ge1\).  Hence every
\(C_{r^n}\) occurs with multiplicity \(\aleph_0\).

The coordinate \(\ell=r\) contributes \(\mathbf Z_r\) when it is present;
when \(r=p\) it is omitted.  This proves (4.2).

### 5.3 Exact dual restriction map

Pontryagin duality gives the exact sequence

\[
0\longrightarrow K_{p,r}
\longrightarrow\widehat{U_{p,(r)}}
\xrightarrow{\operatorname{res}}
\widehat{H_{p,(r)}}\cong C_{r^\infty}
\longrightarrow0.
\tag{5.1}
\]

If \(r=p\), then \(\widehat{U_{p,(p)}}\cong S_p\).  The restriction is an
epimorphism \(S_p\to C_{p^\infty}\).  Blockwise one can isolate a killed
direct summand isomorphic to \(S_p\); the remaining kernel is a subgroup of
a direct sum of cyclic \(p\)-groups.  Kulikov's theorem makes that remaining
kernel a direct sum of cyclic groups, which is absorbed by the already
infinite multiplicities in \(S_p\).  Therefore

\[
K_{p,p}\cong S_p,\qquad p^\omega K_{p,p}=0.
\tag{5.2}
\]

If \(r\ne p\), identify

\[
\widehat{U_{p,(r)}}\cong C_{r^\infty}\oplus S_r.
\]

On the local Prüfer summand, restriction is, up to a unit, multiplication
by \(r^{\kappa_r(p)}\).  For odd \(r\), normalize the logarithm
\(1+r\mathbf Z_r\cong\mathbf Z_r\); the image index is

\[
r^{v_r(p^{r-1}-1)-1}.
\]

For \(r=2\), use
\(\mathbf Z_2^\times=C_2\times(1+4\mathbf Z_2)\); the normalized logarithm
on \(1+4\mathbf Z_2\) gives index

\[
2^{v_2(p^2-1)-3}.
\]

The finite sign character belongs to the reduced \(S_2\)-side and must not
be silently discarded.

### 5.4 Off-local height saturation

Let \(g:S_r\to C_{r^\infty}\) be the restriction contributed by the
away coordinates.  For \(r\ne p\), the needed sharp lemma is

\[
g(S_r[r^m])=C_{r^\infty}[r^m]
\qquad(m\ge1).
\tag{5.3}
\]

It is enough to prove that for every \(m\) there are infinitely many
\(\ell\ne p,r\) satisfying

\[
v_r(\ell-1)=m,\qquad
v_r(\operatorname{ord}_\ell(p))=m.
\tag{5.4}
\]

For odd \(r\), apply qualitative Chebotarev to the compositum of
\(\mathbf Q(\zeta_{r^{m+1}})\) and
\(\mathbf Q(\zeta_r,p^{1/r})\).  Over \(\mathbf Q(\zeta_r)\), the Kummer
extension is ramified at \(p\), while the cyclotomic tower is ramified only
at \(r\); the required Frobenius fixes \(\zeta_{r^m}\), moves
\(\zeta_{r^{m+1}}\), and is nontrivial on \(p^{1/r}\).

For \(r=2\), use the disjoint quadratic fields
\(\mathbf Q(\sqrt p)\) and the 2-power cyclotomic tower and prescribe the
same two Frobenius conditions.  This gives (5.4) and hence (5.3), without
GRH.

### 5.5 Infinite-height calculation

Write the restriction in (5.1) as

\[
f_0\oplus g:C_{r^\infty}\oplus S_r\to C_{r^\infty},
\]

where \(f_0\) is multiplication by \(r^{\kappa_r(p)}\) up to a unit.
If \(x\in r^\omega K_{p,r}\), its projection to \(S_r\) lies in
\(\bigcap_m r^mS_r=0\), so

\[
r^\omega K_{p,r}\subseteq\ker(f_0)
\cong C_{r^{\kappa_r(p)}}.
\]

Conversely, take \(z\in\ker(f_0)\) and, for each \(m\), an
\(r^m\)-root \(x\) of \(z\) in \(C_{r^\infty}\).  Then
\(f_0(x)\in C_{r^\infty}[r^m]\).  By (5.3), choose
\(s\in S_r[r^m]\) with \(g(s)=-f_0(x)\).  Thus
\((x,s)\in K_{p,r}\) and \(r^m(x,s)=(z,0)\).  This proves (4.4).

The kernel contains a direct summand isomorphic to \(S_r\), so all finite
Ulm invariants are \(\aleph_0\).  Ulm's theorem gives (4.3)--(4.5).
The annihilator of \(\overline{\operatorname{Tor}(B_{p,(r)})}\) is

\[
\bigcap_m r^mK_{p,r}=r^\omega K_{p,r},
\]

which gives (4.6)--(4.8).  Kiehlmann's profinite torsion-sequence
classification is the compact-side source and cross-check for this last
translation.

## 6. Explicit separation theorem

At the auxiliary prime \(r=11\),

\[
2^{10}-1=1023=3\cdot11\cdot31,
\]

so

\[
\kappa_{11}(2)=v_{11}(2^{10}-1)-1=0.
\]

On the other hand,

\[
3^{10}-1=(3^5-1)(3^5+1)=242\cdot244,
\]

where \(242=2\cdot11^2\) and \(11\nmid244\).  Hence

\[
\kappa_{11}(3)=v_{11}(3^{10}-1)-1=1.
\]

Therefore

\[
\boxed{B_2\not\cong_{\rm top}B_3.}
\tag{6.1}
\]

The intrinsic witness is:

\[
\overline{\operatorname{Tor}(B_{2,(11)})}=B_{2,(11)},
\]

whereas

\[
\left[
B_{3,(11)}:
\overline{\operatorname{Tor}(B_{3,(11)})}
\right]=11.
\]

This example is a theorem about the bare compact group and does not read the
answer from a conductor or a missing ambient coordinate.

## 7. Marked presentation versus bare owner

The finite-support/conductor filtration on
\(H_p^\perp\subset U_p^\wedge\) is source-natural only for the marked
presentation with its labelled local factors.  It is not intrinsic to the
bare quotient \(B_p\).

The distinction is exact:

1. the ambient product already omits the \(p\)-coordinate, so saying that
   permitted conductors are prime to \(p\) retains the desired owner label;
2. \(S_r\) contains countably infinitely many copies of every
   \(C_{r^n}\), and bare-group automorphisms can mix equal-order summands
   coming from different local supports;
3. neither the embedding \(H_p^\perp\hookrightarrow U_p^\wedge\) nor a
   numeric conductor is supplied by the abstract group \(K_{p,r}\); and
4. the complete bare-group classification (4.9) leaves only the Ulm
   signature.  Any purported bare invariant containing strictly more
   labelled conductor information would contradict that classification.

Thus:

    MARKED_CONDUCTOR_GRADING = SOURCE_NATURAL_FOR_MARKED_PRESENTATION
    MARKED_CONDUCTOR_RECOVERS_P = OWNER_LABEL_RETAINED / CIRCULAR_AS_BARE_CLAIM
    BARE_CONDUCTOR_GRADING = NOT_INTRINSIC
    BARE_TORSION_ULM_SIGNATURE = INTRINSIC

As a negative control, \(U_p\) itself recovers the omitted prime: its
pro-\(r\) dual has a Prüfer summand for \(r\ne p\) and none for \(r=p\).
Quotienting by \(H_p\) removes that simple marker except for the
Wieferich--Ulm defects in (3.1).

## 8. Universal recovery boundary

Given the complete classification (4.9), recovery of every rational prime
from the bare group \(B_p\) is equivalent to injectivity of

\[
p\longmapsto\boldsymbol\kappa(p)
\tag{8.1}
\]

on the set of rational primes.

This precheck has neither a proof nor a verified primary-source theorem
establishing that injectivity.  It would require a global separation result
for the higher Fermat-quotient valuations of distinct bases.  The bounded
search located no direct exact package.  The only permitted novelty/search
statement is:

    NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH

It is not an absolute priority claim and does not prove that (8.1) is open
in every possible formulation.  For this project, the fail-closed status is:

    UNIVERSAL_RECOVER_P_FROM_BARE_B_P = OPEN

The paper may prove the complete signature classification and explicit
pairwise separations.  It may not state that \(B_p\) determines \(p\) for
all primes unless a later independently verified proof closes (8.1).

## 9. Nonredundancy and owner firewall

The current comparison tuple is:

    Paper 2 manuscript
      72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc
    Paper 9 manuscript
      24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
    Paper 13 manuscript
      c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701

The candidate delta is not already supplied by those papers:

- Paper 2 records the abstract compact base and the standard annihilator
  formula \(H_p^\perp\), while explicitly retaining coordinate-choice and
  quotient-homeomorphism caveats.  It does not compute the Ulm signature.
- Paper 9 owns the actual indiscrete quotient \(Q_p\).  Its set model
  \(U_p/H_p\) is not identified topologically with the abstract compact
  \(B_p\).
- Paper 13 supplies continuum bounds and generic nonselective infinite
  branches.  It neither classifies the compact \(B_p\) nor recovers \(p\).

Consequently the replacement has a genuine standalone-bearing centre:
classification of the compact groups \(B_p\) by an intrinsic
torsion-closure/Ulm signature.  The owner firewall remains mandatory:

1. no theorem about \(B_p\) may be transported to the actual indiscrete
   \(Q_p\);
2. no topology, Haar measure, trace, operator, determinant, or disintegration
   is donated to Papers 14 or 18;
3. no claim here supplies a Paper-18 Haar descent or same-map trace;
4. no conductor label is promoted from the marked presentation to the bare
   quotient; and
5. the replacement may be independent of Papers 14 and 18, while the old
   mixed-clock material may serve only as a properly attributed foundation
   merged into Paper 16.

## 10. Primary and official source map

No new PDF is retained by this precheck.  The following locators were
checked as primary, journal, author-hosted, or official records.  They are
source leads for the new protocol, not substitutes for the proof obligations
in Section 5.

1. Christopher Deninger, *Dynamical systems for arithmetic schemes*:
   arXiv version 4, https://arxiv.org/abs/1807.06400v4; journal DOI,
   https://doi.org/10.1016/j.indag.2024.05.007.
   Scope: compact packet-base context, source choices, admissible-class and
   owner boundaries.

2. Jonathan Kiehlmann, *Classifications of countably-based abelian profinite
   groups*, Journal of Group Theory 16 (2013), 141--157:
   https://doi.org/10.1515/jgt-2012-0024 and
   https://arxiv.org/abs/1101.3005.
   Scope: Pontryagin/Ulm classification, annihilator of torsion closure, and
   profinite torsion sequences.

3. Paul Hill, *Primary groups whose subgroups of smaller cardinality are
   direct sums of cyclic groups*, Pacific Journal of Mathematics 42 (1972),
   63--67:
   https://msp.org/pjm/1972/42-1/pjm-v42-n1-p08-s.pdf.
   Scope: a primary published formulation of the Kulikov subgroup theorem
   used in the kernel decomposition.

4. Pieter Moree, *On primes p for which d divides ord_p(g)*, Functiones et
   Approximatio Commentarii Mathematici 33 (2005), 85--95:
   https://arxiv.org/abs/math/0407421.
   Scope: primary corroboration for prescribed divisibility of
   multiplicative orders.  The exact full-height lemma (5.3)--(5.4) must
   still be proved in the new paper.

5. J. C. Lagarias and A. M. Odlyzko, *Effective versions of the Chebotarev
   density theorem*:
   https://www.dtc.umn.edu/~odlyzko/doc/arch/cheb.density.pdf.
   Scope: primary/author-hosted Chebotarev source.  Only qualitative
   Chebotarev is load-bearing here.

6. K. Zsigmondy, *Zur Theorie der Potenzreste*, Monatshefte für Mathematik
   und Physik 3 (1892), 265--284:
   https://doi.org/10.1007/BF01692444.
   Scope: primitive divisors used to detect the omitted \(p\)-Sylow
   exponent coordinate.

Dirichlet's theorem, the local-unit decompositions, normalized \(r\)-adic
logarithms, exactness of Pontryagin duality, and the countable Ulm theorem
must receive exact authoritative citations or self-contained proofs in the
new protocol and proof ledger.  No source above licenses a claim that the
entire theorem package already appears in the literature.

## 11. Eight-item minimum ledger for replacement Paper 15

The new Phase-1 protocol must contain all eight items below.  Omitting any
one lowers the project below the present full-paper ceiling.

| ID | Minimum claim/control | Gate at this precheck |
|---|---|---|
| P15R-1 | Prove the exponent embedding \(H_p\cong\widehat{\mathbf Z}\), including the omitted-\(p\) Zsigmondy branch. | DERIVED / PROOF NOT AUTHORIZED |
| P15R-2 | Prove the exact Sylow decomposition (4.2), including the \(r=2\) sign guard and infinite cyclic-factor multiplicities. | DERIVED / PROOF NOT AUTHORIZED |
| P15R-3 | Prove the local restriction coefficient \(r^{\kappa_r(p)}\) and the off-local Kummer--Chebotarev height-saturation lemma (5.3). | DERIVED / PROOF NOT AUTHORIZED |
| P15R-4 | Prove the exact dual/Ulm formulas (4.3)--(4.5), with Kulikov and all transfinite indices audited. | DERIVED / PROOF NOT AUTHORIZED |
| P15R-5 | Prove the compact torsion-closure formulas (4.6)--(4.8) and identify every construction as characteristic/intrinsic. | DERIVED / PROOF NOT AUTHORIZED |
| P15R-6 | Prove the complete iff classification (4.9) and the explicit theorem \(B_2\not\cong B_3\). | DERIVED / PROOF NOT AUTHORIZED |
| P15R-7 | Prove or formally delimit the marked-conductor versus bare-owner boundary, including the \(U_p\) control and prohibition on importing local labels. | BOUNDARY FROZEN |
| P15R-8 | Freeze universal recover-\(p\) as OPEN, complete the bounded exact-package novelty audit, and enforce the \(B_p\)/actual-\(Q_p\) owner firewall. | BOUNDARY FROZEN |

The old mixed-clock claims are not a ninth item.  They move to Paper 16 and
cannot be counted toward replacement Paper 15's standalone weight.

## 12. Standalone assessment and alternative candidates

If P15R-1--P15R-8 are proved and independently reviewed, the package has a
plausible full-paper centre: a complete isomorphism classification of a
natural family of countably based compact abelian groups, together with
explicit arithmetic separation and a sharp marked/bare boundary.

At this gate:

    CURRENT_STANDALONE_PASS = false
    STANDALONE_CEILING = FULL_PAPER_PLAUSIBLE

If the future project retains only the standard formula \(H_p^\perp\) and
the \(B_2/B_3\) computation, its ceiling is a Technical Note.

The two alternative replacements remain weaker:

- **Admissible-class selection:** present source axioms permit several nested
  admissible classes and do not select a unique one.  Without a new
  universal property or arithmetic axiom, the project is HOLD/NO_GO with a
  Technical-Note ceiling.
- **Condensed marked owner:** condensation retains a set/action carrier but
  does not select a transverse measure, trace, operator, or determinant, and
  overlaps Paper 17's interface.  It is HOLD with a Technical-Note ceiling
  unless an exact nontrivial analytic comparison is first found.

Therefore the Wieferich--Ulm replacement is the recommended new Paper 15,
while mixed standardization and Arveson reconstruction may merge as the new
Paper 16.

## 13. Final machine-readable verdict

    REPORT_ID = P15-TRANSVERSE-ULM-PRECHECK-v1.0
    BATCH_LOCK_SHA256 = 2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
    OLD_P15_PROTOCOL_SHA256 = 53e023e427616e5bd98852181495c6598940e2eb238f100482f3abc7011ca59c
    OLD_P15_PRECHECK_SHA256 = 1598569c48d4382408bb3df933a1c5443984daf36b12e6377bae4590356a75f8
    FINDINGS = C0/M0/m0
    OLD_P15_STANDALONE = SUPERSEDED
    OLD_P15_DISPOSITION = MERGE_INTO_P16
    REPLACEMENT_P15 = WIEFERICH_ULM_COMPACT_BASE_CLASSIFICATION
    MATHEMATICAL_FEASIBILITY = GO
    SOURCE_FEASIBILITY = GO
    UNIVERSAL_RECOVER_P = OPEN
    MARKED_CONDUCTOR_AS_BARE_INVARIANT = NO_GO
    CURRENT_STANDALONE_PASS = false
    STANDALONE_CEILING = FULL_PAPER_PLAUSIBLE
    NEXT_GATE = GO_TO_NEW_PHASE1_PROTOCOL
    PROOF_AUTHORIZED = false
    CONTROLS_AUTHORIZED = false
    ROUTE_AUTHORIZED = false
    MANUSCRIPT_AUTHORIZED = false
    GIT_AUTHORIZED = false

No downstream action is authorized beyond drafting and separately freezing
the new replacement Paper-15 Phase-1 protocol.
