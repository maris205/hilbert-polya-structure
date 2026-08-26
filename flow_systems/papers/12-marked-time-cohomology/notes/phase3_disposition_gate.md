# Paper 12 Phase-3 v2 standalone disposition gate

Date: **2026-08-15**

Decision: **REVISE — mathematics PASS; standalone status HOLD**

## 1. Stable v2 evidence

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/phase3_core_proofs.md` | `9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd` | `P12-1`--`P12-5` proved, C0/M0/m0 |
| `notes/phase3_marked_packet_proofs.md` | `3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49` | `P12-6`--`P12-8` proved, packet corollary |
| `results/manifest.json` | `5337f13b07498872a97ed0d13f0ff0f5ffbcea9e3e37bf8e0c558c3e966e5d3a` | 88 tests, 10 CSV/234 rows, 12 negatives |
| `notes/phase3_controls_review.md` | `e830abedc4cb8167d07d1316a3612dcd8a15b28a78891eba94fc2274bc97fba0` | PASS C0/M0/m0 |
| `notes/phase3_peer_review.md` | `12abc205f2e599035ac8fa64346d25672bcadcbea55bca98b88151e5a13022b9` | PASS C0/M0/m0; `STANDALONE_PASS` |
| `notes/phase3_standalone_review.md` | `a05139142f24b75b682561c732045787923d5c9d6a6d619657880919ba9a39ec` | mathematical PASS; `NOTE_OR_MERGE`, C0/M1/m0 |

The reviewers agree on every mathematical formula, packet/source boundary,
control result, and ownership stop. They disagree only on the locked semantic
nonredundancy gate. The formal reviewer regards the combined package as a
substantive delta; the independent devil's-advocate reviewer finds the
pointed quotient functor deliberately nonfaithful and the remaining steps too
close to Paper 11 plus standard bar/homogeneous-space formalism.

## 2. Conservative adjudication

The disagreement is not resolved by vote. The stricter finding controls:

```text
v2 mathematical status: PASS
v2 standalone status: HOLD
Route evaluation: blocked
manuscript/release: blocked
```

The smallest substantive repair is a versioned theorem, not a wording edit:
construct a basepoint-independent standard Hausdorff retopologization of the
actual unit set from the strict time-marked action, prove a full-and-faithful
equivalence with unpointed standard transitive `R`-homogeneous spaces, and
classify the strict automorphism group as `R/H`. This retains the unit
translations erased by the pointed shadow and makes the actual-to-standard
reconstruction the central categorical result.

No v2 proof or review byte is withdrawn. A v3 amendment must be independently
re-locked, source/novelty audited at the new strength, proved, controlled, and
reviewed before standalone, Route, or manuscript gates may reopen.
