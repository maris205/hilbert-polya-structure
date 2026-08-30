# Theorem package

## Definition and convention

Fix \(0<\lambda<1\) and \(0\leq\delta<1\).  On the half-open interval
\(I=[0,1)\), define
\[
 f_{\lambda,\delta}(x)=\{\lambda x+\delta\},\qquad
 x_{j+1}=\lambda x_j+\delta-k_j,
\]
where \(k_j\in\{0,1\}\) is selected by
\[
 k_j\leq \lambda x_j+\delta<k_j+1. \tag{1}
\]
The lower inequality is closed and the upper inequality is open.  This is a
model convention, not an invitation to identify the two boundary branches.

## Theorem 1 — affine word formula

For a binary word \(w=(k_0,\ldots,k_{n-1})\), direct induction gives
\[
 f_w(x)=\lambda^n x+\delta\sum_{r=0}^{n-1}\lambda^r
       -\sum_{j=0}^{n-1}k_j\lambda^{n-1-j}. \tag{2}
\]
Because \(1-\lambda^n>0\), the return equation \(f_w(x)=x\) has the unique
candidate
\[
 x_w(\delta)=\frac{\delta(1-\lambda^n)/(1-\lambda)-K_w}{1-\lambda^n}
 =\frac{\delta}{1-\lambda}-\frac{K_w}{1-\lambda^n},qquad
 K_w=\sum_{j=0}^{n-1}k_j\lambda^{n-1-j}. \tag{3}
\]
The derivative along the word is \(\lambda^n\).

*Proof.*  Equation (2) follows by substituting one branch at a time.  Solving
the resulting affine equation gives (3); the denominator is positive.  ∎

## Theorem 2 — exact parameter interval

Write each state on the candidate cycle as
\(x_j(\delta)=a_j\delta+b_j\), obtained by iterating
\(a_{j+1},b_{j+1})=(\lambda a_j+1,\lambda b_j-k_j)\) from (3).  The set of
parameters for which \(w\) is an admissible cycle is exactly
\[
 \mathcal D_w=\{\delta\in[0,1):
 0\leq a_j\delta+b_j<1,\quad
 k_j\leq\lambda(a_j\delta+b_j)+\delta<k_j+1
 \ \text{for every }j\}. \tag{4}
\]
Every condition in (4) is a rational affine half-line when \(\lambda\) and
the endpoints are rational.  Hence \(\mathcal D_w\) is an exactly computed
interval (possibly empty or degenerate), with independent lower/upper closure
flags.  No floating-point comparison enters this decision.

*Proof.*  Necessity is (1) and the state-domain definition.  Conversely, (4)
selects exactly the carries in (1), so (2) returns the candidate to itself.
Intersecting affine half-lines proves the interval statement.  ∎

## Theorem 3 — primitive and rotation labels

A word is primitive when it is not a repetition of a shorter block.  We retain
the lexicographically least cyclic rotation as its canonical representative.
For an admissible primitive word define the source-local carry rotation
\[
 \rho(w)=\frac{1}{n}\sum_{j=0}^{n-1}k_j. \tag{5}
\]
The exact derivative factor attached to this itinerary is
\(1-z^n\lambda^n\).  It is a finite bookkeeping factor only; it is not an
arithmetic Euler factor or a target determinant.

## Theorem 4 — endpoint audit and mode-locking ledger

For every row, the producer records both interval endpoints, the active
equalities, and whether the complete half-open system (4) accepts that endpoint.
Thus a lower carry equality may be included while an upper carry equality is
excluded.  Grouping rows with the same \(\rho\) reports a union of exact
word-certified components.  The release does not call this union a maximal
plateau.  This conservative wording remains valid when components meet at a
branch discontinuity.

## Theorem 5 — finite census and direct control

For \(\lambda\in\{1/2,2/3,3/4\}\), the release enumerates every primitive
canonical binary word of lengths \(1\) through \(12\): 747 words per slope,
2241 rows total.  The exact solver retains 138 nonempty components.  A separate
90-digit iteration ledger uses 295 base-grid and endpoint probes; its repeated
suffix and affine fixed point agree whenever the suffix is settled.  These
counts and all row bytes are checked by an implementation that does not import
the producer.

## Literature boundary

Laurent–Nogueira study this exact family of \(\lambda\)-affine contractions and
its rotation number (J. Modern Dynamics 12 (2018), DOI
\(10.3934/jmd.2018007\)).  Nogueira–Pires give finite periodic-orbit bounds for
injective interval piecewise contractions (ETDS 35 (2015), DOI
\(10.1017/etds.2014.16\)).  No global one-periodic-orbit theorem is claimed
here: their general two-branch theorem gives only an at-most-two bound under
its stated hypotheses.
Bugeaud–Conze provide the contracting-mod-one and Farey/Hecke–Mahler context
(Acta Arith. 88 (1999), DOI \(10.4064/aa-88-3-201-218\)).  The present theorem
uses these as scope references and proves only the displayed finite census.

## Route-A boundary

The source parameters have no intrinsic rational-prime carrier, so A0 fails.
The finite itinerary certificate supports A1 only at the declared cutoff.  A2
is an explicit target-match failure: no target determinant or zero comparison is
defined.  No continuation or functional equation is supplied (A3_FAIL), and a
scalar branch contraction gives at most a formal lift hint (A4_FORMAL_HINT).
The strict tuple is
\[
 (\mathtt{A0\_FAIL},\mathtt{A1\_PASS\_ANALYTIC},
  \mathtt{A2\_FAIL},\mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT}),
\]
with `ROUTE_A_REJECTED` and Route B disabled.  No arithmetic, automorphy,
target divisor, or Hilbert–Pólya operator is claimed.
