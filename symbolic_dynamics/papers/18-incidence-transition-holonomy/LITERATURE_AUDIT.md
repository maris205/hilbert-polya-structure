# LITERATURE AUDIT — SD-C20

**Audit date:** 2026-08-14
**System-family boundary:** Symbolic Dynamics only
**Search object:** finite-group edge cocycles on a full shift, switching/cohomology, twisted symbolic determinants, periodic holonomy, and trace-class limits

## 1. Search protocol

The search was deliberately bounded around the frozen object.  It covered
primary papers and monographs on shift zeta functions, symbolic cocycle
cohomology, finite-group extensions, twisted Perron--Frobenius operators,
voltage/gain descriptions of finite directed presentations, and Artin-type
determinant factorizations.  Voltage-graph and gain-graph language is used
only as a finite presentation of the same edge shift; it does not introduce
a second main system family.

Search strings included combinations of
`subshift finite group cocycle twisted zeta`, `edge shift switching
cohomology`, `Livsic finite group extension`, `voltage graph Artin L
function`, `gain graph zeta switching`, `matrix cocycle periodic data`, and
`trace class determinant symbolic transfer operator`.  Bibliographic fields
were checked against publisher or DOI records where available.  The audit is
not a claim that every paper using equivalent terminology has been found.

## 2. Classical boundary

| source | role in the present paper | boundary imposed |
|---|---|---|
| Bowen--Lanford (1970) | determinant/zeta identity for finite-state shifts | the finite determinant machinery is classical |
| Livšic (1972); Parry--Pollicott (1990, 1997) | periodic-data/cohomology viewpoint for symbolic systems and extensions | closed-orbit holonomy is the correct obstruction, not a newly invented invariant |
| Kalinin (2011) | matrix-valued Livšic theorem | periodic matrix data can control cohomology under hypotheses much stronger than our finite determinant equalities |
| Adachi--Sunada (1987); Pollicott (1994) | twisted Perron--Frobenius and character factorization | representation-resolved symbolic factors are established technology |
| Gross--Tucker (1977); Zaslavsky (1989) | voltage/gain switching language | gauge transformations on a finite edge presentation are classical |
| Stark--Terras (1996, 2000) | zeta and covering/Artin decompositions for finite graphs | Artin-style regular-representation factorization is not itself novel |
| Boyle--Schmieding (2017) | finite group extensions of shifts of finite type | finite-group symbolic extensions have a mature classification theory |
| Cavaleri--Donno (2022); Abiad--Belardo--Khramova (2024); Cavaleri--Donno--Spessato (2025) | cospectral and zeta-equivalent gain/voltage phenomena | equal character determinants cannot be promoted to complete gauge invariants |
| Simon (1977) | Fredholm determinants of trace-class operators | the infinite determinant requires an explicit trace-class domain |

## 3. Closest collisions

### 3.1 Twisted symbolic zeta functions

The closest classical collision is the character-resolved zeta function of a
finite-group extension.  The present construction uses exactly that
machinery on a particular tensor-subset alphabet.  Consequently, neither the
regular-representation product nor the primitive-holonomy Euler product is
claimed as new.

### 3.2 Switching and periodic holonomy

The gauge rule

\[
\alpha^b(S,T)=b(S)^{-1}\alpha(S,T)b(T)
\]

is the symbolic counterpart of switching a gain assignment.  Its effect on
based closed paths by conjugation is classical.  Our noncohomology
certificate is therefore an application of standard periodic-data logic to
the frozen incidence grammar.

### 3.3 Isospectral non-equivalence

Known cospectral gain and voltage constructions are the critical negative
collision.  They show why an equality of character determinants, even for
several representations, must not be called a general cohomology theorem.
The finite enumeration in this paper is therefore reported only as evidence
for a very small two-atom rigidity conjecture.

## 4. Novelty boundary

The defensible model-specific contributions are:

1. the exact classification of relabeling-natural local data by the three
   incidence counts \((|S\setminus T|,|S\cap T|,|T\setminus S|)\), including
   the count \(\binom{n+3}{3}-(2n+1)\);
2. the explicit \(S_3\) strict-refinement/strict-coarsening cocycle on the
   tensor-subset shift and its non-one-letter periodic-holonomy certificate;
3. the closed formula for its two-atom standard block and the first exact
   mixed trace-log leaks;
4. the edge-separated commutator marker, which prevents cancellation by
   other primitive words in the refined ledger;
5. the sharp claim discipline separating finite exhaustive evidence from a
   general theorem and separating the finite determinant from the
   \(\operatorname{Re}s>2\) Fredholm domain.

The central conclusion is negative: genuine noncommutative transition
holonomy exists, but its nontrivial Artin block detects mixed atom products
and hence does not select the intended arithmetic primitive inventory.

## 5. Claims intentionally not made

- No theorem says that all functorial incidence cocycles are a one-letter
  cocycle plus a coboundary.
- No theorem says that all-irrep determinant equality classifies gauge
  equivalence.
- No assertion extends the finite \(S_3,D_4,Q_8\) tables to arbitrary groups
  or inventories.
- No analytic continuation, functional equation, critical-line symmetry, or
  zero realization is obtained.
- No cross-family construction is developed in the manuscript.

## 6. Novelty assessment

**Classical machinery novelty:** low.
**Frozen tensor-subset computation novelty:** medium.
**Route-A arithmetic consequence:** negative but informative.
**Risk of overclaim if the evidence/theorem firewall is removed:** high.

The paper should therefore be shared as an exact construction-and-obstruction
study, not as a new general theory of group cocycles and not as an RH proof.
