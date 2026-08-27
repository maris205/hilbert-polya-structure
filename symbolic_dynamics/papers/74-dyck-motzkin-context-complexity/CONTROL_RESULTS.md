# Deterministic control results

`python3 code/verify_context_complexity.py` exhaustively reduces all words in
four Dyck/Motzkin families.  It verifies the normal-form counts underlying
the formulas through `n=8` for two bracket types and through `n=7` for three
bracket types.  A separate bounded check groups words by genuinely enumerated
left, right, and two-sided legal-context signatures for the two-colour Dyck
and one-neutral Motzkin cases; it also derives the failed histogram count from
words rather than a hard-coded arithmetic identity.  Status: **PASS**.
