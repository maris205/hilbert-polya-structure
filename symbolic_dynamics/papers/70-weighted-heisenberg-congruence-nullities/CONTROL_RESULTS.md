# Control results

Command:

```bash
python3 code/verify_weighted_heisenberg.py
```

Stage 4 replay: **PASS** on 2026-08-26. The environment did not provide
`latexmk`, so the authoritative fallback from `BUILD.md` was run instead:
`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, all with zero exit status. The
resulting `main.pdf` has 8 pages, 356,408 bytes, and SHA-256
`3091437f38faa5ef271fb2185e1c6fa7760e0762a296948c4a2d64fa012e8f9d`.
The final log has no warning, undefined-reference, overfull/underfull, or error
match.

The script first checks four direct clock--shift blocks over prime fields
containing the required roots of unity.  Two lie on the Fermat locus and two
lie off it; their determinants and nullities agree with the exact block
lemmas.  It then enumerates the non-split `(ell,p)=(3,2)` character fixture
over `F_4`: the two root pairs `(a,1+a)` and `(1+a,a)` solving `1+u+v=0`
agree exactly with the degree-two gcd over `F_2`.  Finally it checks ten full
quotient convolution matrices.  The full
matrices include `ell=3,5`, characteristics `2,3,5,7,11`, unit and nonunit
weights, and both Fermat-singular and Fermat-nonsingular cases.  Every
observed nullity equals the theorem formula, ending with:

```text
clock-shift determinant and exact nullity: PASS (four direct blocks)
non-split character enumeration F4/F2: mu_3=[1,a,1+a] pairs=[(a,1+a),(1+a,a)] gcd_degree=2 PASS
ALL WEIGHTED HEISENBERG CONTROLS PASS
```

The historical frozen receipt is `code/verification_output.txt`; the Stage 4
command output above additionally contains the non-split enumeration line.
These checks are regression evidence only.

For the official GPT-5.4/xhigh Round-2 freeze, fresh script stdout was compared
line-for-line with that receipt using `diff -u` and matched exactly.
