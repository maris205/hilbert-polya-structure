# Exact classifier and historical evidence

The two Python files are unchanged byte copies of the accepted original
mapping-class implementation. They were statically read during C419
preparation but not executed again.

- classify_word.py SHA-256: 65f61434a4acb513f3d46d2546a68f6661fca8459f4685e821f567323debcbbc.
- line_automaton.py SHA-256: 3e260e709b07c7b71a5a7977d8377fc95407262751fd32037676b5a06beb4e0a.

Run the pointwise classifier, if reproducing in a scratch copy, with
python3 -B classify_word.py --K 101 --word ABB. This is a documented
example command, not a newly executed check. Omitting both arguments
runs its historical self-test. Assertions require ordinary, unoptimized
Python. The helper's main routine is a different 45-line diagnostic:
its observed histogram is not the theorem. The actual classifier uses
only the first 39 line definitions and checks every intermediate point.

[CHECK_RECEIPT.md](CHECK_RECEIPT.md) preserves the old reserve-stage
wording and old check results. Only its two local links were retargeted
to the original frozen files; no scientific content or old execution
claim changed. Thus it is a relocated receipt, not a byte-identical
fourth source file or a new proof review. The original reserve was later
admitted as M1/C419 in this batch; the manuscript itself contains the
complete proof. No old data set or mathematical program was rerun.
