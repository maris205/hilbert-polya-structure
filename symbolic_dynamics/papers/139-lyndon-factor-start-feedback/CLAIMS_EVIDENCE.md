# Claims and evidence — P139 Round-3 owner repair

## Residual theorem claims

| residual claim | all-parameter proof | paper-local exact control |
|---|---|---|
| unique fixed/recurrent word `1^n` | leading singleton-`1` factorization and strict leading-one growth | complete functional graphs through `n=18` |
| sharp depth `n`, unique at `0101...` | explicit `01` factorization and reverse equality induction | every state through `n=18` |
| complete ordered-Lyndon fibre formula | target starts prescribe factor lengths; CFL uniqueness gives exactly the ordered chains | every target through `n=14` |
| matrix formula and image criterion | rectangular comparison matrices enumerate adjacent lex inequalities | independent matrix evaluator through `n=14` |
| special fibre identifications | one factor reduces to the owned binary Lyndon census; all singleton factors give `1^a0^(n-a)` | both identities through `n=18` |

## Owned static inputs — excluded from residual

| static statement | exact owner | treatment |
|---|---|---|
| factor starts are the left-to-right minima of the suffix-rank permutation, equivalently strict new suffix minima | Sabrina Mantaci, Antonio Restivo, Giovanna Rosone, Marinella Sciortino, Theorem 2.2, *Journal of Discrete Algorithms* 28 (2014), 2--8, DOI `10.1016/j.jda.2014.06.001` | cited as controlling owner; statement and reproduced proof receive zero credit |
| ordered-tail descent/comparison in a nonincreasing CFL factorization | classical CFL/Lyndon comparison machinery | explicitly labelled static input and zero credit |
| independent Duval-mask/suffix-record equality through `n=18` | integration check of the imported theorem | retained in verifier output but not counted as residual evidence |

## Credit subtraction

Chen--Fox--Lyndon factorization, Duval's algorithm, least-suffix and
least-rotation algorithms, suffix/Lyndon arrays and forests, the binary Lyndon
census, necklace Möbius inversion, matrix multiplication, the Mantaci et al.
suffix-record theorem, and the ordered-tail comparison receive zero
contribution credit.  The residual is only the iterated start-mask dynamics,
sharp unique depth-$n$ orbit, and ordered-Lyndon fibre atlas.  Bounded owner
non-hits are not novelty certificates.  External posting, submission,
priority, specialist contact, and release remain `HOLD_EXTERNAL`.
