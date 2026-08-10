# HCS-C27 material passports

## Source certificates

| Source | Role | SHA-256 | Status |
|---|---|---|---|
| C24 `c24_certificate.json` | periodic controls and integral conjugacy | `4b4fe5943262137eeeb3eda4de887725a0663402a1f39f8cc43e089bcc91e778` | frozen |
| C25 `c25_certificate.json` | fixed symplectic fibre and telescope | `a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12` | frozen |
| C26 `c26_certificate.json` | scalar domain, branches, and trace atom | `1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a` | frozen |

## C27 artifacts

| Artifact | Origin | Verification |
|---|---|---|
| `c27_certificate.json` | exact producer | independently replayed |
| `c27_independent_check.json` | separate matrix/finite-field engine | 8/8 gates pass |
| local Weil polynomials | Newton sums from exact Thomas characters | full arrays and hard-coded hashes replayed |
| p=43 fibre collision | full period 1 through 925 | exact modular theorem |
| P076/P082 collapse | explicit integral symplectic conjugator | direct integer identities |
| 150-branch census | all first returns through bridge length 12 | exact finite evidence |

## External mathematical inputs

- Thomas, *The Character of the Weil Representation*, Theorem 1A.
- Gurevich–Hadani, canonical finite-field Weil quantization.
- The released C26 scalar Bergman trace-class theorem, based on the common
  positive-prefix complex domain and holomorphic transfer estimates.

No external numerical dataset is used. Odd prime lists are deterministic
test domains, not training or fitting data.
