# Pre-P0 screen card — endogenous escape-carry

**Candidate ID:** `ASFS-SCOUT-20260918-REC01`  
**Version:** 1, frozen 2026-09-18 before the screen.  
**Initial status:** `PRE-P0 HYPOTHESIS — OPEN`.

## Frozen discrete object

Let

\[
 X=\{(n,d,k,e): n\ge2, d\ge2, k\in\mathbb Z, e\in\{0,1\}\}.
\]

The scan/escape map `T` is the following single rule, with all tests made on
the current state:

* if `e=0`, `d^2<=n`, and `d` does not divide `n`, send
  `(n,d,k,0)` to `(n,d+1,k,0)`;
* if `e=0`, `d^2<=n`, and `d` divides `n`, send it to
  `(n+d,d+1,k+1,1)`;
* if `e=0` and `d^2>n`, send `(n,d,k,0)` to `(n,2,k,0)`;
* if `e=1`, send `(n,d,k,1)` to `(n+1,2,k,0)`.

The first branch is a divisor-admissible scan; the second changes the
arithmetic state and enters a nonfixed escape phase; the last branch advances
the integer and clears the phase. No prime table, `log n`, or per-prime data
is an input. This is deliberately a discrete semigroup screen, not yet a
symplectic map or a suspension.

| Field | Frozen content |
| --- | --- |
| Lineage | divisor-symbolic admissibility → sequential scan → reversible-carrier/escape test |
| Carrier | full `X`; no selected clean register or recurrent subset |
| Arithmetic mechanism | current-state divisibility; `n` and `k` update on a hit |
| Proposed return | least periods of the full `T` action, if any; no cycle is selected by hand |
| Clock | unit step only; a positive geometric roof is `OPEN` |
| Symplectic base / flow | `NOT SUPPLIED`; invertibility is a first gate |
| Controls | reset collision; prime scan length; composite hit and `k` growth; constant-source comparator |
| Stop rule | stop if reset is noninjective, if prime periods have no source-derived clock, or if composites retain primitive returns |
| Route | A0/A1/A2 `UNASSIGNED`; Route B `NOT INVOKED` |

Changing the reset, adding a history register, or replacing the integer update
is a new candidate. In particular, this card does not modify 218 and does not
borrow 163/169's ordered-cover flow.
