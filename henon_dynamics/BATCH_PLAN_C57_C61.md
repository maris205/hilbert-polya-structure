# Adaptive batch plan: HCS-C57 through HCS-C61

Status: **planning only; C57 locked from the frozen C56 theorem; C58--C61
remain contingent and have no selected theorem targets**

Date: 2026-08-15

## Batch protocol

This is a five-paper adaptive batch, not a list of five predetermined
questions.  Only the first gate is locked now.  After each paper is released,
the next paper may be selected only from that predecessor's actual positive
theorem, certified obstruction, or explicitly unresolved branch.  A proposed
successor must pass a fresh primary-source novelty audit, a theorem-size and
non-salami review, and a falsifiable exact-computation gate before its title or
claim is fixed.

The current dependency graph is therefore

\[
 C56\longrightarrow C57\longrightarrow
 \underbrace{C58\longrightarrow C59\longrightarrow C60\longrightarrow C61}
 _{\text{contingent and presently unselected}}.
\]

No result, title, or method is reserved for C58--C61.  A negative C57 result
may change the direction of C58 just as materially as a positive one.  Batch
completion requires five independently theorem-sized papers, each with its
own proof package, exact replay, source audit, manuscript, release tuple, and
commit/provenance closure.

## HCS-C57: minimal Brauer-jump field and explicit class

### Why C57 is locked only now

C56 proves that the released C55 Yukawa cubic surface \(Y/\mathbf Q\) has a
connected degree-\(27\) line scheme, full line-field normal closure

\[
 \operatorname{Gal}(K/\mathbf Q)\cong W(E_6),
 \qquad |W(E_6)|=51840,
\]

and geometric/arithmetic Picard ranks \(7/1\).  Those are the actual frozen
C56 outputs.  They make it possible to ask an arithmetic base-change question
that was not available before C56: what is the smallest extension on which
the algebraic Brauer group jumps, and can its nonzero class be exhibited
exactly?

C57 studies this new field-and-class object.  It is not another computation
of the 27-line field, a repackaging of the known \(W(E_6)\) conjugacy table, or
a generic theorem about cubic surfaces.

### Locked theorem target

Let \(D=\{E,G\}\) be a double-six and let

\[
 U_D=\operatorname{Stab}_{W(E_6)}(D)\cong S_6\times C_2,
 \qquad F_D=K^{U_D}.
\]

The target is one instance-specific theorem with the following inseparable
parts.

1. Prove the sharp base-change divisibility statement

   \[
   \bigl(\operatorname{Br}(Y_L)/\operatorname{Br}(L)\bigr)[2]\ne0
   \quad\Longrightarrow\quad 36\mid[L:\mathbf Q],
   \]

   and prove that equality is attained at \(F_D\), where
   \([F_D:\mathbf Q]=36\) and
   \(\operatorname{Br}(Y_{F_D})/\operatorname{Br}(F_D)\cong\mathbf Z/2\).
   Here the quotient is the algebraic/cohomological Brauer quotient; no
   Brauer--Manin evaluation is asserted.

2. Construct an exact irreducible degree-\(36\) double-six resolvent for
   \(F_D\), certify that its splitting field is exactly the frozen field
   \(K\), and construct the oriented quadratic extension.  If
   \(U_D^+\cong S_6\) denotes the embedded index-two subgroup of \(U_D\)
   preserving the two sixers separately, then this extension is

   \[
   F_D'=K^{U_D^+}=F_D(\beta_D),
   \qquad \beta_D^2=\delta_D.
   \]

3. Define a canonical quartic \(Q_D\) over \(F_D\), by an exact normalized
   one-dimensional kernel or equivalent determinant formula, whose divisor on
   \(Y\) is the twelve lines \(E+G\).  With \(H=-K_Y\) and \(\ell=u_0\), prove

   \[
   \operatorname{div}_Y(Q_D/\ell^4)=E+G-4H
       =\operatorname{Norm}_{F_D'/F_D}(E-2H),
   \]

   and prove that the cyclic algebra

   \[
   (F_D'/F_D,Q_D/\ell^4)
   \quad\text{equivalently}\quad
   (\delta_D,Q_D/\ell^4)
   \]

   is the unique nonzero algebraic Brauer class.

The quartic may be represented exactly by a normalized Cramer-determinant
recipe.  Printing an enormous expanded coefficient table is not part of the
claim.

### Exact controls and kill gates

- G0 binds the released C56 certificate, payload, committed source objects,
  cubic coefficients, complete 27-line scheme, and Picard lattice before any
  C57 invariant is read.
- G1 reconstructs the characteristic-zero incidence carrier: every line has
  exactly ten neighbours, giving 135 edges, 72 sixers, and 36 double-sixes.
- G2 independently enumerates \(W(E_6)\), the exact stabilizer
  \(S_6\times C_2\), its faithful degree-36 action, and the integral cocycle
  quotient \(H^1(U_D,\operatorname{Pic}\bar Y)=\mathbf Z/2\).  The global
  degree lower bound must use the complete Swinnerton-Dyer/Elsenhans--Jahnel
  two-primary classification, not an incomplete list of natural subgroups.
- G3 constructs the monic degree-36 resolver with a proved coefficient bound,
  proven-prime CRT reconstruction, full modular factor certificates,
  irreducibility, and trivial action kernel, so its splitting field is \(K\).
- G4 proves that the central involution exchanges the two sixers, sends
  \(\beta_D\) to \(-\beta_D\), and gives the claimed oriented quadratic
  extension.  It must not be confused with the global determinant quadratic
  field of the cubic.
- G5 verifies in characteristic zero that the selected degree-12 line carrier
  and its degree-15 complement multiply to the frozen degree-27 eliminant.
- G6 fixes the quartic gauge, proves a rank-30 restriction matrix and a
  one-dimensional normalized kernel, and verifies all twelve line
  restrictions.
- G7 proves degree exhaustion for the quartic divisor, the exact norm-divisor
  identity, unramifiedness, and the separate class-map computation identifying
  the cyclic algebra with the nonzero cohomology generator.
- Across G0--G7, release additionally requires a genuinely independent
  checker, a strict schema, hostile scalar and subtree mutations,
  deterministic replay, fail-closed rollback-atomic promotion, and scoped and
  full manifests.  These are cross-cutting release conditions, not a
  substitute for the mathematical G7 gate.
- **KILL:** a failed C56 rebind, a non-exhaustive incidence carrier, a
  reducible or wrongly split resolver, a nonfaithful degree-36 action, a
  missing oriented quadratic binding, failure of the exact 12+15 factor
  identity, or failure of the normalized quartic/divisor/class bridge stops
  C57.  It may not be replaced by an abstract \(H^1\) table or by a large
  unverified polynomial dump.

### Novelty and scope firewall

Classical and modern sources already provide the general double-six
stabilizer, degree-36 resolvent method, and construction of order-two Brauer
classes.  Tables of the 25 element conjugacy classes of \(W(E_6)\), the
vanishing of the base-field algebraic Brauer group under the full action, and
stable nonrationality of minimal cubic surfaces are also prior results.  C57
does not claim any of those as new.

The bounded novelty claim is the exact, source-locked realization for this
frozen Yukawa surface: the sharp first jump field, its certified normal
closure and orientation, and a canonical explicit generator.  C57 makes no
claim about rational points, a Brauer--Manin obstruction or local evaluation,
surface rationality, the complete local Artin package, bad Euler factors, root
numbers, automorphy, a motive, a Calabi--Yau realization, RH, or a
Hilbert--Polya operator.  The Route-A tuple remains exploratory and is not
strengthened merely by this arithmetic classification.

## HCS-C58 through HCS-C61: contingent slots

C58, C59, C60, and C61 have no locked titles, objects, theorem statements,
or experiment programs.  Each slot is opened only after the immediately
preceding paper is frozen and its actual theorem/obstruction has been audited.
At every transition the batch plan must record:

- the exact predecessor result used as input;
- why the new object is mathematically distinct from that predecessor;
- the alternatives rejected by primary-source and duplication checks;
- one theorem-sized positive or negative target;
- exact GO/KILL controls that can terminate the branch; and
- the unchanged Route-A and Hilbert--Polya firewalls.

Failure to find a non-salami, source-distinct theorem at a transition is a
batch blocker; it is not permission to split the predecessor's certificate
or manuscript into another paper.

## Batch-wide publication vetoes

The following are supporting computations or corollaries, not standalone
papers in this batch:

- reproducing the known 25-class \(W(E_6)\) trace or \(H^1\) table;
- stating only that the base-field Brauer group vanishes;
- stating only that Picard-rank-one cubic surfaces are not stably rational;
- printing a degree-36 resolver without the fixed-field, normal-closure, and
  explicit-class bridges;
- inferring rational points, rationality, or Brauer--Manin failure from the
  absence of a rational line;
- calling a finite list of good-prime point counts a Hasse--Weil or Artin
  package;
- promoting bounded numerical reconstruction, a timed-out exact calculation,
  or a single implementation's self-reported Boolean to theorem evidence; or
- claiming automorphy, a functional equation, RH, or a Hilbert--Polya operator
  from the arithmetic of the 27 lines.

Every realized successor must add a fresh source ledger and hostile novelty
audit.  No absolute priority claim is authorized by this planning document.
