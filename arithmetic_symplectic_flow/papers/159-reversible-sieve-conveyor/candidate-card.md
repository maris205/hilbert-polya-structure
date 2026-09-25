# Frozen candidate card: reversible sieve conveyor

**Candidate ID:** ASFS-20260915-RSC01  
**Paper ID:** 159-reversible-sieve-conveyor  
**Version:** 1, frozen 2026-09-15 before the package audit  
**Status:** STOP — COMPLETE REVERSIBLE SOURCE CONVEYOR; NO INTRINSIC CLOSED ORBITS.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Exact owner

Let j range over all integers and set n(j)=2+|j|, L_j=2n(j)−2.
The discrete phase labels are E={(j,k):0≤k<L_j}. Their successor is
S(j,k)=(j,k+1) except S(j,L_j−1)=(j+1,0).
For n=n(j), freeze the increment

\[
w(j,k)=
\begin{cases}
1_{\{k+2\mid n\}},&0\le k\le n-3,\\
0,&k=n-2,\\
-1_{\{2n-2-k\mid n\}},&n-1\le k\le2n-4,\\
0,&k=2n-3.
\end{cases}
\]

An empty index interval contributes no step. Thus n=2 has precisely two
zero-increment phases. Nonnegative j performs n=2,3,4,... in order; the negative
tail is the explicit prime-independent completion n=...5,4,3 before j=0.
It is not claimed to be a historical inverse of an irreversible sieve.

| Field | Frozen definition / boundary |
| --- | --- |
| Carrier and form | M=disjoint union over (j,k) in E of R²_(q,p), with dq wedge dp on every component; all real q,p are retained |
| Base map | F(j,k,q,p)=(S(j,k),q+w(j,k),p), with no adjustable parameters |
| Regularity / measure | Disjoint-union smooth structure; componentwise C-infinity; sum of ordinary area measures; no finite total-volume assertion |
| Roof | tau=1 on every state; one time unit per test, pause or connector |
| Suspension | X=(M×[0,1])/((x,1)~(F(x),0)); time translation with the stated gluing; completeness is to be checked |
| Arithmetic inputs | All integer divisor tests 2≤d<n are performed in order, then undone in reverse order; no prime table, factorization oracle, prime-specific parameter, prime-log roof or zero data |
| Observable | Clean-register q=0 at block entry is a stated source calibration; alternatively use the q-displacement from block entry to phase k=n−2, without dropping non-clean states from M |
| Symbolic lineage | Prime/composite witness symbols → ordered compute–uncompute source evolution → exact two-dimensional area-preserving register realization |
| Primitive convention | All intrinsic periodic points of the complete F, modulo cyclic phase; positive least period, with unit-roof repeated time r times that least period; none may be selected by calibration |
| Analytic owner | NOT ADVANCED: no operator, zeta, determinant or trace contract is introduced before the decisive recurrence test |
| Future owner | Hamiltonian/contact/quantum lift DEFERRED; the three-dimensional suspension is not itself asserted symplectic |

## Precommitted checks and controls

1. Construct the global inverse and verify symplecticity and completeness on
   every component, not only the clean-register path.
2. Seek an explicit full-state conjugacy or a counterexample to recurrence;
   include arbitrary register offsets, the n=2 block and the negative tail.
3. Check the actual divisor output at the top of the forward scan, then check
   whether compute–uncompute cancellation leaves any arithmetic holonomy.
4. Compare a finite closed list of whole blocks as a separately owned
   control. Retain its complete real register plane, not just an origin.
5. Replace all divisor increments by zero, and by arbitrary fixed integer
   test tables undone in reverse order, as nonarithmetic controls.
6. Relate the result narrowly to 018, 025, 053 and 054: an explicit new carrier
   is not a new universal obstruction theorem or a source of transferred credit.

## Stop / fork rule

Stop if the complete conveyor has no periodic state or if the proposed
closed control has nonfinite or nonprime multiplicity. Do not close an epoch,
remove the negative tail, select a clean register, or change the roof while
retaining this candidate ID. A successful source computation alone is not an
A0+A1 result. Formal coordinates remain UNASSIGNED and Route B NOT INVOKED.

## Audit disposition, appended after the version-1 freeze

The frozen formulas were not changed. The full-state inverse, symplecticity,
complete unit suspension and exact chronological divisor observable are
established in the [paper](paper.md). The complete map is explicitly conjugate
to integer translation times the identity on R²; its flow is conjugate to real
translation on R²×R. Consequently every full-state closed-orbit ledger is empty.
Finite closed whole-block controls instead have continuum primitive packets
independently of primality. Portfolio decision: STOP this owner and FORK the
source-return mechanism, without treating a closed control as its continuation.

See the [claim ledger](claim-ledger.md), [package summary](README.md) and
[evidence index](evidence/README.md). The result is a concrete realization of
the known frontier obstruction, not a new general no-go theorem.
