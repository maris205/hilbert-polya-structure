# A reflected wave–sieve has a full-shift orbit ledger and an exact prime source readout

**Paper ID:** 138-reflected-wave-sieve.  
**Candidate ID:** ANG-20260914-RWS01.  
**Date / status:** 2026-09-14; STOP — FULL-SHIFT PACKET CONTROL; PRIME-SELECTIVE PACKET/CLOCK NOT ESTABLISHED.  
**Evidence:** exact elementary proofs; no numerical experiment.  
**Route state:** broadened T0--T3 audit only; classical A0/A1/A2 NOT APPLICABLE;
Route B NOT INVOKED.

## Abstract

We couple the causal binary divisor sieve to reflected nearest-neighbor
propagation in a reversible two-register action on the full binary product.
The arithmetic formula produces the entire prime indicator from a uniform
zero initial state after two steps. Independently, an explicit spatial
recursion identifies every full spacetime solution with an arbitrary
two-sided binary boundary word. This is a topological conjugacy of the
same frozen action to the full binary shift, not an externally chosen
symbolic substitute. It gives the complete periodic-point counts, primitive
packet multiplicities, unit-clock repetitions and ordinary zeta product.
The pure-wave and constant-source controls have that identical orbit
spectrum. Thus the exact source readout and same-object analytic result
are positive controls, while prime-selective packets and an arithmetic
clock remain unestablished. The arithmetic observable survives under the
conjugacy; the return status of the particular zero seed remains open.

## 1. Frozen identity and lineage

The [version-1 card](candidate-card.md) was frozen before this audit. Work
over the binary field \(\mathbb F_2\), with addition denoted by \(+\). Let

\[
X=\mathbb F_2^{\{2,3,\ldots\}},\qquad
G(y)_n=\prod_{\substack{2\le d\le\lfloor\sqrt n\rfloor\\d\mid n}}(1-y_d),
\]
\[
L(y)_2=y_2+y_3,\qquad L(y)_n=y_{n-1}+y_{n+1}\quad(n\ge3),
\qquad R(x,y)=(y,x+G(y)+L(y)).
\]

The product topology is used, and an empty product is one. There is no
cutoff, fitted parameter, changed boundary or restricted recurrent core.
The [prior-work arrow](../../docs/prior_work/README.md) is the explicit
prime/composite exclusion of [050](../050-causal-binary-sieve-fixed-point-screen/paper.md),
deformed through [131](../131-second-order-causal-sieve/paper.md)'s
two-register memory into bidirectional spatial feedback. No Hénon or
finite-dimensional symplectic realization is asserted.

| Owner field | Frozen object | Audited status |
| --- | --- | --- |
| Carrier / action | Full \(X^2\), product topology, R | Homeomorphism |
| Broadened carrier | Transformation groupoid \(X^2\rtimes_R\mathbb Z\) | Same complete action; full isotropy retained |
| Arithmetic source | G using integer divisibility and uniform states | Exact two-step source output |
| Distinguished observable | Both registers with integer coordinate labels | Retained under the explicit conjugacy |
| Clock / flow | Unit roof with \((z,1)\sim(Rz,0)\) | Complete suspension |
| Packets | All least-period R-orbits modulo cyclic phase | Complete finite multiplicity at every period |
| Repetitions | Same unit roof on the same action | Primitive length m, repeated length rm |
| Analytic proposal | Ordinary unweighted primitive product | Converges for \(\Re s>\log2\), with explicit continuation |
| Operator / trace | None supplied | OPEN / NOT SUPPLIED |
| Classical symplectic fields | No finite-dimensional symplectic owner | NOT APPLICABLE |

Allowed inputs are integer divisibility, coordinate order and the displayed
Boolean rules. No prime list, prime-selected phase space, logarithmic prime
roof, Mangoldt weight or Riemann-zero data is used.

## 2. Question and claim boundary

Does bidirectional feedback supply owned recurrent packets while keeping
the arithmetic source, and does its complete packet spectrum distinguish
that source from the predeclared nonarithmetic controls?

The strongest supported result is a complete same-object full-shift coding
and unit-roof zeta, together with an exact source readout. The adverse
result is equality of the unweighted packet spectrum with the controls.
This is not a theorem that arithmetic disappears under conjugacy, that
the zero seed is nonperiodic, or that no other observable-sensitive analytic
construction could ever be defined. None of those statements is claimed.

## 3. Ownership and arithmetic source

### Proposition 1 — Continuous inverse and exact source output

R is a homeomorphism of \(X^2\), with

\[
R^{-1}(u,v)=(v+G(u)+L(u),u).
\]

Writing \(\mathbf0,\mathbf1\) for the uniform words and \(\pi\) for the
prime indicator indexed by n>=2,

\[
R(\mathbf0,\mathbf0)=(\mathbf0,\mathbf1),\qquad
R^2(\mathbf0,\mathbf0)=(\mathbf1,\pi).
\]

**Proof.** Each coordinate of G depends on finitely many input coordinates.
Each coordinate of L has two input coordinates, including the displayed
reflection at 2. Thus R and the proposed inverse are continuous.
Substituting either composition cancels the duplicated binary terms.

Every factor of \(G(\mathbf0)_n\) is one, so \(G(\mathbf0)=\mathbf1\).
Both \(L(\mathbf0)\) and \(L(\mathbf1)\) vanish. A prime n has no divisor
in the product for \(G(\mathbf1)_n\), which therefore equals one. A
composite n has a divisor between 2 and its square root, yielding a zero
factor. Hence \(G(\mathbf1)=\pi\), and both iterates follow. QED.

This is a spatial arithmetic readout at one time, not a prime-valued
temporal sequence and not yet a claim that its source orbit closes.
Since \(X^2\) is compact Hausdorff and R is a homeomorphism, the
transformation groupoid with arrow space \(X^2\times\mathbb Z\) is a
locally compact Hausdorff étale groupoid: each fixed-integer slice is
a source and range chart.

## 4. Complete spatial coding

### Theorem 2 — Explicit full-shift conjugacy

Let \(\Omega=\mathbb F_2^{\mathbb Z}\) and
\((Sa)(t)=a(t+1)\). There is an explicit homeomorphism
\(C:\Omega\to X^2\) with \(RC=CS\).

**Proof.** Interpret an R-orbit as pairs
\((u(t-1),u(t))\), so its spacetime equation is

\[
u_n(t+1)=u_n(t-1)+G(u(t))_n+L(u(t))_n.
\tag{1}
\]

Start with an arbitrary doubly infinite boundary word \(u_2(t)=a(t)\).
At coordinate 2, \(G_2=1\), and (1) forces

\[
u_3(t)=a(t+1)+a(t-1)+a(t)+1.
\tag{2}
\]

For n>=3, define successive entire time rows by

\[
u_{n+1}(t)=u_n(t+1)+u_n(t-1)+u_{n-1}(t)+G(u(t))_n.
\tag{3}
\]

Every divisor used in \(G_n\) is smaller than n, so it refers only to
already defined rows. Equations (2)--(3) therefore define unique rows
for all n and all integer t. They make (1) hold at every coordinate
by construction. Set
\[
C(a)=(u(-1),u(0)).
\]
The produced spacetime is a genuine complete R-orbit, by (1) and
Proposition 1. Translation of t gives \(RC(a)=C(Sa)\).

Conversely, any state \((x,y)\) has a unique complete R-orbit. Extract
its boundary word \(a(t)=u_2(t)\). Equation (2), followed by (3), shows
that this orbit is exactly the one reconstructed from a. Thus C is
both surjective and injective.

For continuity, induction in n shows that \(u_n(t)\) depends on finitely
many entries of a; in fact the window
\([t-(n-2),t+(n-2)]\) suffices. Equation (2) gives the first step;
in (3), the time shifts expand the previous row's window by one,
and the lower divisor rows stay within that window. Hence every
coordinate of C is continuous. The inverse coordinate \(a(t)\) is
the coordinate at 2 of the second register of \(R^t(x,y)\), which
is continuous for each integer t. Both product maps are continuous.
QED.

The coding is derived from this action and reconstructs its entire
state. It is not a borrowed full shift supplying a separate orbit
ledger. Its inverse and the reconstruction explicitly depend on G.
Consequently the transported integer-labelled registers remain
nontrivial G-dependent observables on \(\Omega\).

## 5. Complete packets, repetitions and ordinary product

### Corollary 3 — Periodic counts and full primitive ledger

For every m>=1,
\[
\#\operatorname{Fix}(R^m)=2^m.
\]
If \(b_m\) is the number of primitive R-orbits of least period m,
then
\[
\sum_{d\mid m}d\,b_d=2^m,\qquad
b_m=\frac{2^m-\sum_{\substack{d\mid m\\d<m}}d\,b_d}{m}.
\tag{4}
\]
Every packet is retained with its full multiplicity.

**Proof.** By Theorem 2, a point fixed by \(R^m\) is exactly a boundary
word satisfying \(a(t+m)=a(t)\). Its m consecutive bits are free,
giving \(2^m\) points. Each least-period-d orbit contributes d such
points exactly when d divides m, giving (4). Thus primitive packets
are precisely binary cyclic words of least period m; this counts
all packets, not a selected symbolic subfamily. QED.

The unit suspension is complete: for a representative \((z,v)\) with
0<=v<1 and real elapsed time h, put
\(k=\lfloor v+h\rfloor\), obtaining \((R^kz,v+h-k)\).
A return has integer elapsed time because the height modulo one
must return. Consequently a least-period-m base orbit gives a
primitive closed flow orbit of length m, and an r-fold traversal
has length rm. There are no additional noninteger primitive lengths.
These statements retain cyclic phase identification. No orientation
reversal quotient is imposed. Differential monodromy is NOT APPLICABLE
to this zero-dimensional compact base.

### Proposition 4 — Same-object ordinary zeta and continuation

For the frozen full primitive packet set \(\mathcal P\), with its unit
roof,
\[
Z(s)=\prod_{\gamma\in\mathcal P}
(1-e^{-sT_\gamma})^{-1}
=\frac{1}{1-2e^{-s}},\qquad \Re s>\log2.
\tag{5}
\]
The right-hand side gives the meromorphic continuation of this same
function to the complex plane.

**Proof.** Write \(q=e^{-s}\). In \(|q|<1/2\), the logarithmic series
converges absolutely: \(m b_m\le2^m\), and
\(\sum_m b_m\sum_{r\ge1}|q|^{mr}/r\) is finite. Expanding each
factor and collecting the coefficient of \(q^k\) gives
\[
\log Z(s)
=\sum_{k\ge1}\frac{q^k}{k}\sum_{m\mid k}m b_m
=\sum_{k\ge1}\frac{2^k q^k}{k}
=-\log(1-2q),
\]
where the analytic logarithm is normalized to vanish at q=0.
Exponentiating proves (5). The displayed reciprocal of an entire
function is meromorphic and agrees on the starting half-plane,
so it is a continuation of the owned product. QED.

No operator, nuclearity theorem or trace formula is used or credited.
This is an ordinary orbit-zeta statement, not a formal Route-A
target/divisor pass. It does not identify a prime-power trace or
Riemann target.

## 6. Controls and adverse findings

The predeclared pure-wave control replaces G by zero. A constant-source
control replaces G by any fixed bit c at every coordinate. Each uses
the same reflected L and two-register form, but is a distinct object.
For these controls, (2) has final constant 0 or c, and (3) has source
0 or c. The same recursive proof gives a full binary-shift conjugacy
and hence exactly (4)--(5).

Thus the candidate's complete unweighted periodic counts, primitive
lengths, repetitions and ordinary zeta do not distinguish its
divisor-sieve source from these controls. This is the planned
PROVES_TOO_MUCH warning for packet-spectrum arithmetic, not a
denial of Proposition 1 or of the labelled source observable.

| Claim | Adversarial question | Scoped answer |
| --- | --- | --- |
| Full prime readout after two steps | Was a prime word supplied? | No; Proposition 1 derives it from divisibility and uniform states |
| Complete full-shift coding | Is a different symbolic object supplying timing? | No; equations (2)--(3) reconstruct every state and intertwine the same R |
| Exact ordinary zeta | Does it distinguish arithmetic? | No; the predeclared nonarithmetic controls have the identical product |
| G-dependent coordinate observable | Does conjugacy erase it? | No; transporting that observable also transports the G-dependent reconstruction |
| Source-orbit return | Does full-shift conjugacy prove the zero seed is nonperiodic? | No; its particular boundary word has not been classified here |

The remove-L comparison is precisely the separate 131 architecture.
Its source-orbit nonreturn result is not transferred to R. The present
spatial reconstruction specifically uses the \(u_{n+1}\) term and is
not a proof about 131. No finite-box experiment was run: introducing
an upper reflecting or periodic boundary would change the owner.
No state, orbit, roof or multiplicity was selected after the result.

## 7. Gate assessment and stop

| Gate | Evidence for ANG-20260914-RWS01 | Status and limitation |
| --- | --- | --- |
| T0 | Complete continuous invertible action, groupoid and unit suspension | ESTABLISHED |
| T1 | Endogenous full prime source readout from a uniform seed | PARTIAL; no demonstrated prime-selective packet/clock; seed return OPEN |
| T2 | Full-shift conjugacy, exact complete primitive ledger and repetitions | ESTABLISHED |
| T3 | Ordinary unweighted product and displayed meromorphic continuation | ESTABLISHED for this product only; operator and trace NOT SUPPLIED |
| Classical A0/A1/A2 | No finite-dimensional symplectic base | NOT APPLICABLE |
| Formal Route coordinates | No formal evaluation performed | UNASSIGNED |
| Route B | No invocation or operator evaluation | NOT INVOKED |

**Decision: stop this candidate at the planned generic-packet control;
portfolio fork.** The object has stronger return and ordinary-zeta
ownership than 131, while its unweighted packet spectrum is still a
nonarithmetic full-shift spectrum. These exact positive results remain
reusable controls, not accumulated Route credit. A different coupling,
roof, selected subspace or observable-sensitive analytic construction
requires a new card. Deep classification of the zero-seed boundary
word is not needed for this scoped stop and is left OPEN.

## Evidence and reproducibility

The exact inputs are the frozen formulas and product topologies.
Equations (1)--(5) and their proofs are the reproducible method;
there is no numerical precision, orbit cutoff, training set or
computed output to interpret as a global theorem. See the
[claim ledger](claim-ledger.md) and [evidence index](evidence/README.md).
The local source records establish lineage only; all results about R
are proved in this paper.
