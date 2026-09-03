# P180 Review-A Round-1 delta acceptance

**Frozen Round-0 baseline:** `main.tex`
`7f43974b3a3885545f5a2bc6910a79359c6f039e41819fa2085f2c9b29c24712`  
**Round-1 source accepted:** `main.tex`
`529bd4c0c091d3932c35de0b1ac8a6d347b3c65a838738bccfc1167207929991`  
**Decision:** `ROUND1_DELTA_ACCEPT / THEOREM_ACCEPT / HOLD_EXTERNAL`  
**Post-delta open findings:** `0 Critical / 0 Major / 0 Minor`  
**Owner ceiling:** `OWNER_AMBER`; a later literal or conjugate owner
supersedes this acceptance and activates withdrawal.

## Finding-by-finding ledger

| ID | Required delta | Frozen Round-1 evidence | Reviewer status |
|---|---|---|---|
| P180-A-M01 | Add the `t=0` identity fibre to the every-time contract, preserve the positive-time law, synchronize claim surfaces, and add author control | `main.tex:149-175` states and proves the identity fibre at `t=0` before restricting the four-case display to `t>=1`; the abstract at `main.tex:40-41`, `PAPER_PLAN.md:9-11`, `CLAIMS_EVIDENCE.md:8`, and `SELF_QA.md:7` now have a literal all-time meaning. `code/verify_p180.py:130-134` sweeps every time-zero target, and the canonical records `TIME_ZERO_FIBRES=IDENTITY_PASS`. | **CLOSED** |
| P180-A-m01 | State that `q` is a prime power and `m>=1` at the literal definition | `main.tex:53-59` states both hypotheses before defining the ordered-pair map. | **CLOSED** |
| P180-A-m02 | Add paper-local subtraction against P102/P103/P125/P171 and preserve the owner ceiling | `main.tex:73-79`, `SOURCE_VERIFICATION.md:12-26`, `CLAIMS_EVIDENCE.md:16-17`, and `NARRATIVE_REPORT.md:32-37` distinguish the literal mechanisms, assign shared scalar-power/formed-space/Gram vocabulary zero credit, retain `OWNER_AMBER / HOLD_EXTERNAL`, and keep the search result a bounded non-hit. | **CLOSED** |

The superseding Round-1 text also correctly separates the tail contribution
of the order's `3`-part from the period contribution of its prime-to-`3`
part (`main.tex:38-39`) and states that `(3^t-1)/2` and the modulus `2s` are
ordinary integers, including in characteristic two (`main.tex:101-123`).
No new theorem, boundary, or attribution defect was introduced.

## Frozen byte inventory

| artifact | SHA-256 |
|---|---|
| `main.tex` | `529bd4c0c091d3932c35de0b1ac8a6d347b3c65a838738bccfc1167207929991` |
| `main.pdf` | `d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59` |
| `main_round0_original.pdf` | `3051dc087aa5c26bb2bcc69e363af75918fe51797dd509161979656fb8ecb248` |
| `main_round1.pdf` | `d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59` |
| `references.bib` | `6fe7667ad608cb6206236edc000e93f5c9137d4dea1c7fb5b5c0dc7e00f1e119` |
| `README.md` | `0e1eab8bc063f945cd515ce3362710071991e5420744b622702d2864442faac1` |
| `BUILD.md` | `08f6001e23593e529074c0833197c21009ba2e6d5d19cb0af8a41a96807e67d4` |
| `IMPROVEMENT_LOG.md` | `8b2ecb771ed5ac022d44dea0f2a1b9f80ad4c1f6b4d34d37ab738ddad0905810` |
| `SELF_QA.md` | `2b0c792f77a4cb507e739240bb605936c825f8e868efbd54126edbc10e401108` |
| `SOURCE_VERIFICATION.md` | `48ca69fc8ced95c42295e729d171301659a42511b6a4d26c66d13d5f59eff7fd` |
| `CLAIMS_EVIDENCE.md` | `8de0efc276c3d6f46ea8a8bb4390b55b5149208214c070acb24c73663dc05626` |
| `PAPER_PLAN.md` | `6b45d8c0ed94e35e7feb0a14e66a8812c548e8205700e14ce717baa16db6a69e` |
| `code/verify_p180.py` | `1280ced45293a1b7ea22df577d3c4fa12cf5297b4b263d0666562fbd1811fd61` |
| `code/CANONICAL.txt` | `1cc3b6253f83521f6b0cf0fa11a160d90aaa91683341655b78de0381467c024b` |
| final paper-local `SHA256SUMS` (not self-listed) | `49aa565b7cf1d1c749599d40f0ed888191512df38f4e2b3727f8b6c86331f3a2` |

The final paper-local manifest verifies `18/18`. `main.pdf` is byte-identical
to both `main_round1.pdf` and `main_round2.pdf` and correctly differs from the
immutable Round-0 receipt. The final README, build record, improvement log,
self-QA, source ledger, and `FINAL_QA.md` preserve the Round-1 repair history,
record the Round-2/final lifecycle, and continue `HOLD_EXTERNAL`. These are
documentation-only provenance changes: `main.tex`, all PDFs, both controls,
their canonicals, theorem claims, and assertion totals are unchanged.

## Independent replay and artifact gate

Two fresh Python processes each produced output byte-identical to the
Reviewer-A canonical:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_A.py | cmp - CANONICAL.txt
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_A.py | cmp - CANONICAL.txt
```

Each replay made **243,393 assertions**, including extension fields,
nonsymmetric nondegenerate forms, characteristic two, `A=0`, `A>=2`, the
`ord_(2s)(3)` boundary, every target at `t=0`, positive-time fibres through
`t=5`, and the unique maximum. The author verifier also replayed
byte-identically to its author canonical with **770,697 assertions**, of
which 46,702 are the added identity-fibre sweep. The settled log has no
unresolved citation/reference, box, or LaTeX warning. The source says
`Anonymous`; `pdfinfo` reports blank Title, Author, Creator, Producer,
Subject, and Keywords, with no metadata stream or JavaScript.

This accepts all three Review-A repairs for the next internal round only. It
does not authorize posting, submission, external circulation, or any
authorship action.
