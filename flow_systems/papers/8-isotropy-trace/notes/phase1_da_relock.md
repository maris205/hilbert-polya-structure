# Paper 8 Phase-1 Devil's-Advocate Re-lock

Date: 2026-08-14  
Mode: read-only preregistration audit; no browsing and no Phase-3 proof work

## Locked inputs

| File | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `ccfff73f30d2d5208356dee2d3295bd1eb495a92f08114885b88f397e80603a6` |
| `notes/candidate_lock.md` | `20fd7879ac8885d5966a2bfd64c8723100aba8c78e8e628ae216cfaada307a50` |
| `notes/phase1_amendment.md` | `d1719d8862841da128d3274cd4598bd56f49b6b96bc00bb6288517d18fc30114` |

All three bytestrings matched these hashes at review time.  The active files
were not edited.

## Verdict

**REVISE — Critical 0 / Major 0 / Minor 1.**

The amendment closes all five former Major findings and former Minors m2--m3.
Former m1 is only partially closed: the construction/trace boundary is now
careful, but the transformation groupoid's evidence class and source ownership
are still stated inconsistently.

## Finding-wise closure

| Finding | Status | Locked evidence |
|---|---|---|
| M1 — per-prime/global collapse | **CLOSED** | Protocol 163--175, 235--240, 358--386; candidate 30--55, 125--151 separate `G_p`, optional coproduct, finite support, and positive-time distribution. |
| M2 — positive-time extraction | **CLOSED** | Protocol 368--386 and candidate 143--151 restrict the test function after the two-sided theorem and type `Theta_+` as a locally finite Radon distribution/measure, not a global trace. |
| M3 — Haar/Weil/Plancherel scales | **CLOSED** | Protocol 255--272, 388--409 and candidate 61--64, 88--96, 153--174 freeze `dt`, `du`, `du/L`, counting Haar, dual `dtheta/(2pi)`, and the common length/probability scaling. |
| M4 — completion/nonnormality | **CLOSED** | Protocol 333--356, 431--434 and candidate 114--123, 243--254 freeze the full/reduced/regular/fibre diagram and separate amenability, factorization, compact image, singular extension, and no-normal-extension gates. |
| M5 — intrinsic quotient path | **CLOSED** | Protocol 261--272, 413--417, 435--439 and candidate 41--49, 86--97 use `K_p=R/L_pZ`, `Q_p=Gamma_p/K_p`, a section-free orbit integral, and forbid `Q_p=B_p` without proof. |
| m1 — provenance/evidence class | **PARTIAL; MINOR** | Candidate 24--26 denies source ownership of the *trace*, and 198--201 separates Haar/measure/trace, but protocol 21, 112, and 547 still call the groupoid source-defined/source-origin and no locked record assigns it `DERIVABLE_NEW_DEFINITION`. |
| m2 — target-contamination scope | **CLOSED** | Protocol 50--71, 100--102, 470--473, 607--608 and candidate 219--221, 243--254 freeze an algebraic trivial character, bounded forbidden inputs, and mutually exclusive confirm/refute/not-testable outcomes. |
| m3 — Route ceiling | **CLOSED** | Protocol 7--8, 447--448, 553--559 and candidate 5, 212--215, 240--241 make A1 the ceiling, force A2 fail/not-testable and A3 fail, and close A4/Route B. |

## Remaining required correction

### Minor m1 — distinguish canonical derivation from source ownership

Protocol 21 says the transformation groupoid is “defined by the source flow
itself”; protocol 112 calls the mechanism “source-defined”; protocol 547 allows
“source-origin credit.”  A transformation groupoid may be canonically
constructed from source-owned flow data without being an object defined or
claimed in the cited source.  The current wording can therefore inflate
provenance even though its trace claims are correctly gated.

Required before PASS:

1. In protocol 21 and 112, say **canonical new transformation-groupoid
   construction from the source-defined flow**, not source-defined groupoid.
2. In the `DEN-EF-PACKET-ACTION-GRPD-P` record, assign the groupoid construction
   the evidence class `DERIVABLE_NEW_DEFINITION` and state explicitly that this
   is not source-publication ownership.
3. Replace protocol 547's “source-origin credit” with derivation credit tied to
   P8-1; packet, period, and flow data alone retain source-origin credit.

No mathematical convention, theorem target, candidate domain, Route status, or
control needs to change.  A byte-locked revision limited to this provenance
correction is sufficient for a PASS re-lock.

## Final provenance re-lock addendum — 2026-08-14

This narrow addendum reviews only the former m1 correction and a regression
scan of M1--M5.  It used no browsing, performed no Phase-3 proof work, and did
not edit the active lock files.

### Final locked inputs

| File | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `72879eb8f3f5fc73b967060dfc08aeb3de2c2447d655cefeeed8bcc12e89f716` |
| `notes/candidate_lock.md` | `531edb1eeb429869167bbc8b175ac6f4017166a66956d978762d1838e0413b68` |
| `notes/phase1_amendment.md` | `ff2cd2491ba06cca8e1049414e9bc2456363aeba8bca1c3c2d081f2c0aa17bb1` |

All three bytestrings matched these hashes at review time.

### Former m1 closure

**CLOSED.** Protocol 21--23 now calls the groupoid a canonical new construction
from the source-defined flow and assigns `DERIVABLE_NEW_DEFINITION`, while
protocol 114 uses “newly derived” and protocol 548--552 reserves source origin
for the underlying packet/flow fields.  Candidate 32--34 records the same
evidence class and denies source authorship/analytic ownership; candidate
201--203 repeats that ownership boundary.  Amendment 39 records the correction.
The former phrases “defined by the source flow itself,” “source-defined
groupoid/trace mechanism,” and “source-origin credit” are absent.

### M1--M5 regression scan

| Finding | Final status | Regression evidence |
|---|---|---|
| M1 — per-prime/global split | **NO DRIFT** | Protocol 165--177, 237--242, 360--388; candidate 30--60, 128--154. |
| M2 — positive-time extraction | **NO DRIFT** | Protocol 370--388; candidate 146--154. |
| M3 — full Weil normalization | **NO DRIFT** | Protocol 257--274, 390--411; candidate 64--67, 91--100, 156--177. |
| M4 — fixed completion diagram/nonnormality | **NO DRIFT** | Protocol 335--358, 433--436; candidate 117--126, 247--258. |
| M5 — intrinsic `Q_p` path | **NO DRIFT** | Protocol 209--225, 263--274, 415--419, 437--441; candidate 44--52, 91--100. |

### Final verdict

**PASS — Critical 0 / Major 0 / Minor 0.**

For the exact final input tuple above, former m1 is closed and M1--M5 remain
closed.  This addendum supersedes the earlier `REVISE` verdict only for these
new locked bytes; it does not assert any P8-1--P8-9 theorem.

## Final status-byte metadata addendum — 2026-08-14

This is a mechanical, read-only comparison against the preceding PASS tuple.
No browsing, active-file edit, or Phase-3 proof work was performed.

### Status-byte tuple

| File | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `127d80d98532ef150df4c74706c44047c3509c14c3498322d6dee09ed81f98c2` |
| `notes/candidate_lock.md` | `25c37f5a81ad95640f31e4d7f13b0bb328b4cf5735f31c70ce3e30b0f99a699b` |
| `notes/phase1_amendment.md` | `2a5f721ed2e61495f4ccaad1095e571ce74c069e70e59507f97dd1307ecb51e6` |

All three active files matched these hashes at check time.

### Exact inverse-diff verification

The permitted metadata edits were mechanically reversed in a byte stream; the
resulting full-file hashes exactly reconstructed the preceding PASS tuple:

| File | Reversed metadata only | Reconstructed prior SHA-256 |
|---|---|---|
| `research_protocol.md` | PASS status line | `72879eb8f3f5fc73b967060dfc08aeb3de2c2447d655cefeeed8bcc12e89f716` |
| `candidate_lock.md` | PASS status line | `531edb1eeb429869167bbc8b175ac6f4017166a66956d978762d1838e0413b68` |
| `phase1_amendment.md` | status wording, active-hash ledger, and final re-lock status paragraph | `ff2cd2491ba06cca8e1049414e9bc2456363aeba8bca1c3c2d081f2c0aa17bb1` |

Because each complete reconstructed hash equals its previously reviewed lock,
there is no unaccounted-for byte change and no mathematical drift.  Former m1
and M1--M5 retain their preceding closed/no-drift dispositions.

### Metadata verdict

**PASS — Critical 0 / Major 0 / Minor 0.**

The preceding mathematical PASS remains final for the status-byte tuple above.
