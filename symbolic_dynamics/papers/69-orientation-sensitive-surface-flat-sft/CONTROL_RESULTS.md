# Exact finite-control results

## Frozen command

```bash
python3 code/verify_surface_flat_sft.py
```

## Result

Terminal status: **ALL CHECKS PASS**.

Stage 4 replay: **PASS** on 2026-08-26. The environment did not provide
`latexmk`, so the authoritative fallback from `BUILD.md` was run instead:
`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, all with zero exit status. The
resulting `main.pdf` has 11 pages, 378,382 bytes, and SHA-256
`b45b6839b02cd7b285cab4b90753285d6c47f4b109a4461cce92bfc42b031b14`.
The final log has no warning, undefined-reference, overfull/underfull, or error
match.

```text
D8: group axioms PASS (order 8)
Q8: group axioms PASS (order 8)
D8: orientable fixed counts m=1..4 [17408, 68157440, 275951648768, 1126999418470400]
D8: nonorientable fixed counts n=1..5 [288, 17408, 1081344, 68157440, 4328521728]
Q8: orientable fixed counts m=1..4 [17408, 68157440, 275951648768, 1126999418470400]
Q8: nonorientable fixed counts n=1..5 [224, 17408, 1015808, 68157440, 4261412864]
D8/Q8: orientable equality and even/odd nonorientable split PASS
C3: group axioms PASS (order 3)
C3: exact one-dimensional FS indicators [1, 0, 0]
C3: orientable fixed counts m=1..4 [243, 19683, 1594323, 129140163]
C3: nonorientable fixed counts n=1..5 [9, 81, 729, 6561, 59049]
C3: normalized moments P=[Fraction(3, 1), Fraction(3, 1), Fraction(3, 1), Fraction(3, 1)], Q=[Fraction(1, 1), Fraction(1, 1)], R=[Fraction(1, 1), Fraction(1, 1), Fraction(1, 1)]
C3: reconstructed (c_1^+, c_1^-, c_1^0)=(1, 0, 2) PASS
synthetic mixed-indicator fixture: bases=[Fraction(1, 1), Fraction(1, 4)] P=[Fraction(5, 1), Fraction(17, 4)] Q=[Fraction(15, 4), Fraction(51, 16)] R=[Fraction(1, 2), Fraction(7, 8)]
synthetic mixed-indicator fixture: reconstructed d=1:(2,1,1), d=2:(1,2,1) PASS
S3: group axioms PASS (order 6)
S3: orientable Hom counts genus=1..3 [18, 486, 16038]
ALL CHECKS PASS
```

## What was computed directly

- The `D_8`, `Q_8`, and `C_3` multiplication laws satisfy all group axioms.
- For each group, the program forms the exact distribution of one commutator,
  convolves it `g` times, and reads the identity coefficient to count
  `Hom(pi_1 Sigma_g,K)`.
- It separately forms the distribution of one square, convolves it `l` times,
  and reads the identity coefficient to count `Hom(pi_1 N_l,K)`.
- It applies the rooted gauge factors for the manuscript's two cover families
  and compares the resulting fixed counts with the character formulas for
  `m=1,...,4` and `n=1,...,5`.
- For `C_3`, exact root-of-unity orthogonality gives the one-dimensional FS
  signature `[1,0,0]`.  The direct tuple counts agree with
  `O_C3(m)=3^(4m+1)` and `N_C3(n)=3^(2n)`.  Normalized moments recover
  `(c_1^+,c_1^-,c_1^0)=(1,0,2)`, explicitly exercising the indicator-zero
  branch.
- A synthetic fixture with degrees `1,2` and ledgers `(2,1,1)` and `(1,2,1)`
  for the `(+, -, 0)` sectors forms exact `P`, `Q`, and `R` moment pairs. The
  three exact two-base Vandermonde solves recover totals `(4,4)`, self-dual
  counts `(3,3)`, and signed-over-degree coefficients `(1,-1/2)`, after which
  the manuscript formulas reproduce both ledgers coefficient by coefficient.
- The `S_3` orientable homomorphism counts `[18,486,16038]` at genera one
  through three provide a different-order control.

## Diagnostic interpretation

The equal `D_8/Q_8` orientable rows verify that the degree-only moment is
insensitive to the two-dimensional indicator.  The nonorientable rows agree
at `n=2,4` and differ at `n=1,3,5`, exactly matching the power
`nu^(n+2)`.  The checks would catch the common errors `|K|^(2n-1)`,
`nu^n` with a shifted cover genus, or omission of the gauge factor.
The `C_3` rows additionally catch any failure to delete the two non-self-dual
characters from nonorientable moments or to reconstruct their `c_1^0`
multiplicity by subtraction. The multi-degree fixture catches swapped
Vandermonde indices, a missing multiplication by the recovered degree, and
cross-degree mixing of the positive, negative, and zero sectors.

These are finite regression checks.  They do not prove the spanning-tree
bijection, the classical all-genus surface formulas, or the infinite moment
reconstruction.
