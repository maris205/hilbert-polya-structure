# Deterministic control results

`python3 code/verify_iet_fan.py` uses exact rational arithmetic.  For three
reverse-four-IET length vectors and all word lengths through six, it compares
the cylinder inequality language with a separately generated partition by
preimages of discontinuities.  All 18 complete language equalities agree,
covering 207 positive cylinders.  It also verifies symbolic integer endpoint
forms and all-pairs inequalities, an essential wall crossing, the
weak-only/empty-strict closure negative control, and the raw hyperplane bound
through `N=6`.  Status: **PASS**.
