# Claims-to-evidence ledger — P184 final freeze

| claim | deductive location | exact author-side pressure |
|---|---|---|
| low/high/zero/equality tail and period formulas | Theorem 2.1; Proof Package Steps 1–3 | every state on 27 prime-power carriers, including `p=2` |
| cycles by valuation and recurrent population | Theorem 3.1; Proof Package Step 4 | complete recurrent orbit decomposition on every tested carrier |
| odd/even tail censuses and sharp maxima | Theorem 3.1; Proof Package Step 5 | complete tail histogram on every tested carrier |
| exact double- and empty-target atlases | Theorem 4.1; Proof Package Steps 6–7 | every target and literal incoming list on every tested carrier |
| fibre cap, `0/1/2` census, and image defect | Theorem 4.1; Proof Package Step 8 | complete fibre histogram and image set on every tested carrier |
| `a=1`, `p=2`, `x=0`, and equality landing at zero | statements and proofs throughout | dedicated boundary assertions |

The proof establishes the all-parameter claims.  `code/verify_p184.py` is
author-side regression code derived from the theorem specification; it is not
itself an independent review or novelty evidence.  Two fresh runs each completed
109,478 assertions and matched `code/CANONICAL.txt` byte for byte.
Two process-separated hostile controls later rechecked the valuation and
inverse atlases through different representations and closed with zero
findings.

Generic finite-ring dynamics, valuation algebra, cyclic translations, and
functional-graph bookkeeping receive zero contribution credit.  Section 1
subtracts the exact internal neighbours P128, P142, and P166.
