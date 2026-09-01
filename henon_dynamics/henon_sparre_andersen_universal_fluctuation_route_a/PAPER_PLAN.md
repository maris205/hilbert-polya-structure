# Paper plan

## One-sentence contribution

For iid continuous symmetric increments, one maximum factorization and one
permutation-cycle identity close survival, first descent, two discrete-arcsine
laws, their scaling limit, and the exact atomic failure boundary.

## Claims–evidence map

| Claim | Analytic owner | Executable receipt |
|---|---|---|
| `q_n=binom(2n,n)/4^n` | unique-maximum convolution | 41 exact rows and SymPy series |
| first strict descent | survival tail differences | 40 exact differences |
| `P(M_n=k)=q_kq_(n-k)` | independent pre/post blocks | no-ties permutation controls |
| `P(N_n=k)=q_kq_(n-k)` | cycle lemma and bivariate GF | full positive-count histograms |
| arcsine weak limit | Stirling plus endpoint bound | 12 bulk scaling receipts |
| atomic failure | four-path counterexample | simple-walk enumeration through 8 |

## Section plan

1. Freeze the iid/continuous/symmetric convention and notation.
2. State the joint theorem.
3. Prove maximum factorization and derive survival/first descent.
4. Prove the positive-count law through the cycle identity.
5. Derive the scaling limit and atomic boundary.
6. Report the executable certificate and Route-A boundary.

The final paper is concise because the proof is the main result.  It does not
inflate finite regression into an experiment section or claim literature
novelty.
