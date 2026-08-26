# Paper 17 Phase-1 amendment v1 — localic and standard-owner repair

Status: **ACTIVE / INDEPENDENT EXACT-BYTE RE-LOCK REQUIRED**  
Version: `P17-P1-AMENDMENT-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)

This amendment binds and supersedes only the conflicting claims in:

```text
batch design lock
  sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
research protocol
  sha256:5ca581cff6f2fe088744a522646466ef2f5ce124ad3cdf50367cc5ed33347cea
candidate lock
  sha256:2db53e92961cdfa7e43e4e06b7cdd81a2d87d97d15957d793b720bd86c71a604
framework/source precheck
  sha256:2d8ddcadd67c6978edbf094a12728aabf28017f86349b76917dc90496b7ea50f
```

The precheck verdict was `C0/M2/m2`.  This amendment closes exactly those
four findings.  Every unaffected owner firewall and downstream block in the
base protocol remains active.

## 1. Exact generic theorem target

Let `H` be a topological group, let `X` be a nonempty globally indiscrete
space, and let `H` act continuously on the right of `X`.  The registered
open groupoid is

```text
G(X,H)=X_ind rtimes H.
```

The candidate generic comparison is now:

```text
B(G(X,H)) ~= B_cont(H),
O(G(X,H)) ~= O(H)
```

where `B_cont(H)` means the Grothendieck topos/category of continuous
`H`-sets in the exact selected source convention, and the quantale on
`O(H)` uses open-set product and inversion.  The right-sided/base frame is
the two-element frame.

For connected `H=R`, every continuous action on a discrete sheet set is
trivial, hence

```text
B(G(X,R)) ~= Set.
```

For disconnected or discrete `H`, the conclusion need not be `Set`.
`H=Z` with its discrete topology and a nontrivial `Z`-set is a mandatory
negative control.  Connectedness is therefore a frozen hypothesis of the
actual-real collapse, not an expositional convenience.

## 2. Open but non-etale type

The exact actual groupoid is open and non-etale.  Its open-groupoid quantale
is therefore nonunital; the unit image is not arrow-open.  No inverse-quantal-
frame or etale quantale-sheaf equivalence is invoked.

The proof must check source/range openness, failure of local-homeomorphism
source maps, the composable-pair frame, multiplication, involution, and the
right-sided/base frame.

## 3. Localic reconstruction wording

Protin--Resende reconstruction is not an information-loss theorem.  Their
open quantal frame reconstructs the associated **open localic groupoid**.
For `X_ind`, the spatial-to-localic functor has already replaced the
non-sober multi-point unit space by the terminal locale.  The correct
statement is:

> The quantale fully retains the resulting localic one-object group while
> the passage from the nonsober topological presentation to its localic
> reflection forgets the extra point-set carrier, orbit decomposition, and
> set stabilizers.

The manuscript may not attribute that loss to failure of the quantale
reconstruction theorem.

## 4. Standard-circle comparison

For the standard owner

```text
S_L=R/(LZ),       G_L=S_L rtimes R,
```

the candidate output is asymmetric with the actual owner:

```text
B(G_L) ~= B(LZ) ~= BZ,             not Set,
base(O(G_L)) ~= O(S_L),             not the two-element frame.
```

The standard outputs retain abstract integer isotropy and the standard
circle localic action.  Without a strict time marker, they do not recover
the numerical embedding `LZ -> R`: dilation identifies the unmarked records
for different positive `L`.  A strict time marker forbids that dilation, but
is extra registered structure rather than an invariant of the plain topos
or quantale.

Thus Paper 17 may claim neither that the standard owner collapses to the
actual output nor that both owners forget orbit/stabilizer data.  The common
loss is only the unmarked numerical scale.

## 5. Revised claim ledger

| ID | Revised candidate claim |
|---|---|
| P17-1 | `G(X,H)` is open; for non-discrete connected `R` it is non-etale and gives a nonunital open quantal frame. |
| P17-2 | `B(G(X,H)) ~= B_cont(H)`; connected-real corollary `B(G(X,R)) ~= Set`; disconnected-time counterexample. |
| P17-3 | `O(G(X,H)) ~= O(H)` with base frame `2`, independent of the carrier/action; localic-reflection wording as above. |
| P17-4 | Standard circle: `BZ` and base `O(S^1)`; abstract isotropy retained, unmarked numerical `L` lost. |
| P17-5 | Fixed-prime application and strict-time comparison, with no C*-algebra/trace promotion. |

## 6. Publication and authorization boundary

Topos and quantale branches remain one project.  The current ceiling is the
batch's sole `TECHNICAL_NOTE_CANDIDATE`; standalone status is not presumed.
Only exact-byte methodology, devil/domain, and source re-locks may close
Phase 1.  Symbolic proof, controls, Route, manuscript, release, Route B,
Git, and public synchronization remain false until separately authorized.
