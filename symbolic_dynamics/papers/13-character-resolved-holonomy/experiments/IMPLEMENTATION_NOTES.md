# SD-C15 Implementation Notes

## Frozen implementation

The executable implements the preregistered adjacent positive-charge
\(\mathbb Z\)-lift

\[
L_s(w)=D_s+wA_s,
\qquad
a_n(s)=\frac{p_n^{-s}+p_{n+1}^{-s}}2.
\]

Finite determinants are evaluated by the tridiagonal continuant

\[
\Delta_n=(1-zx_n)\Delta_{n-1}
-z^2a_{n-1}^2w^{q^+_{n-1}+q^-_{n-1}}\Delta_{n-2}.
\]

The continuant is stored as a character polynomial, so Fourier coefficients
are read directly rather than estimated from the 1024-point character grid.
The grid is used only for the full character-range audit and an independent
DFT reconstruction check.

## Reproduction

From the Paper13 directory:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  code/test_sdc15_character_holonomy_experiment.py
PYTHONDONTWRITEBYTECODE=1 python \
  code/sdc15_character_holonomy_experiment.py
sha256sum -c results/SHA256SUMS.txt
```

The experiment is deterministic. It regenerates all files in `results/`
except the checksum ledger, then regenerates the ledger from the two Python
sources and five result artifacts.

## Exact and numerical divisions

- The continuant structure, degree-zero coefficient, two-atom formula,
  positive-charge ledger, inverse-charge leak, and charged-path census are
  exact identities.
- The census uses exact rational coefficients at \(s=2\) for
  \(N=2,3,4,5\), \(r\le12\).
- The determinant matrix uses every frozen cutoff, source point, determinant
  point, and all 1024 characters. Binary64 is the primary numerical format.
- The same full cutoff/source/determinant/character matrix is executed for all
  32 frozen positive-charge fields; coefficient extraction remains direct and
  non-aliased because every determinant degree is below 1024.
- One selected determinant is independently checked by a dense determinant,
  64-term trace-log reconstruction, an 80-digit scalar continuant, and a DFT
  coefficient recovery.
- Rank and entropy coboundaries are unitary-gauge controls. The entropy
  coboundary is a \(U(1)\) phase control, not an integer-valued
  \(\mathbb Z\)-charge field.
- The roof-entropy twist is checked only as the parameter translation
  \(p^{-s}e^{i\theta\log p}=p^{-(s-i\theta)}\).

## Frozen controls

- first \(N\) tensor primes;
- first \(N\) composite integers;
- the seed-13013 permutation of the first 128 primes;
- the seed-13014 sorted sample from `range(2,16*N+2)`;
- inverse charges \((+1,-1)\);
- forward DAG;
- rank and entropy coboundaries;
- entropy-roof twist;
- 32 directed positive-charge fields from seeds 15000 through 15031,
  independently uniform on \(\{1,2,3\}\).

No target-zero data are read, stored, fitted, or compared.
