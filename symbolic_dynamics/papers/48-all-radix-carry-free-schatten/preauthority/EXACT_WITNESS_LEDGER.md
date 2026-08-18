# Exact Witness Ledger

## Purpose

Every row below is an exact symbolic witness or an independently
reconstructible finite check. A finite witness validates a formula but
contributes no novelty.

| ID | Claim tested | Exact witness | Expected invariant | Failure meaning |
|---|---|---|---|---|
| W01 | digit singular formula | \(C_bC_b^*\), row reversal | \((\min(i,j))_{1\le i,j\le b}\) | digit derivation false |
| W02 | determinant/product | reverse columns of \(C_b\) | triangular unit diagonal, \(|\det C_b|=1\) | \(\tau_b>b\) proof broken |
| W03 | Hilbert–Schmidt digit norm | count ones of \(C_b\) | \(b(b+1)/2\) | \(\sigma=1\) wall comparison broken |
| W04 | cross-shell factor | \(k>\ell\) digit tuple | repetition multiplicity \((b-1)b^{k-\ell-1}\) | shell exponent wrong |
| W05 | same-shell factor | top digits both nonzero | \(C_{b-2}\otimes C_b^{\otimes k}\) after zero deletion | endpoint pinching wrong |
| W06 | binary exception | \(b=2,\ k=\ell\) | zero block exactly | illegal odd-radix proof |
| W07 | binary replacement | \(I_{2j}\oplus I_{2j+1}\) | off-diagonal singulars duplicated | equality endpoint unproved |
| W08 | universal wall | column \(n=1\) | units digit \(0,\ldots,b-2\), positive density | boundedness threshold wrong |
| W09 | trace at \(b=2\) | condition \(2d<2\) | only all-zero word, deleted | positive-vertex convention broken |
| W10 | odd-radix loop | vertex \(1\), \(b>2\) | \(1+1<b\) | trace/LPS scope wrong |
| W11 | least period two | \(b^a,b^c\), \(a\ne c\) | alternating closed word | binary LPS incomplete |
| W12 | least period \(r\ge3\) | \(r\) distinct powers of \(b\) | pairwise carry-free and least period \(r\) | period construction false |
| W13 | prime-base comparator | Kummer valuation theorem | no carry iff \(p\nmid\binom{m+n}{m}\) | source scope wrong |
| W14 | zero deletion | zero word in \(C_b^{\otimes L}\) | absent from \(\mathbb N\) source | finite-control type leak |

## Endpoint witnesses

The two critical surfaces must be exercised separately.

1. At \(\sigma=1\), W08 rejects boundedness for every radix and every
   \(q\), regardless of the digit norm.
2. At \(\sigma=\log_b\kappa_{b,q}>1\), W05 supplies the nonsummable
   same-shell sequence for \(b\ge3\).
3. At the same digit-norm equality for \(b=2\), W06 prevents use of W05
   and W07 supplies the nonsummable paired-shell sequence.

## Trace and power witnesses

For trace class, enumerate positive words only and retain a diagonal word
exactly when every digit satisfies \(2d<b\). For powers \(r\ge2\), enumerate
based closed words and attach \(\prod_i n_i^{-s}\). The absolute-value
ledger must match the real-\(\sigma\) ledger term by term. A nonreal
cancellation never changes the support least-period ledger.

## Finite-control status

Finite cutoffs, digit tensors, singular-value tables, and dynamic-programming
counts are evaluator controls. None may appear in a contribution sentence
except as validation of the infinite theorem.

