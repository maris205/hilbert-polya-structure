# FIGURE SPECIFICATION

## Figure 1 — lawful factorization and its two stopping boundaries

**Purpose.** Prevent three recurring confusions:

1. \(D_+\) and \(D_-\) are blocks of the same regular transfer;
2. only \(D_{\rm reg}=D_+D_-\) is the whole-extension determinant;
3. atom-local factors neither remove mixed lifted cycles nor distinguish prime
   inventories from controls.

**Layout.**

- Left: signed subset alphabet, arithmetic variables, and intrinsic
  \(\alpha(S)=|S|\bmod2\).
- Center: the regular \(C_2\) transfer \(B_{\rm reg}\), annotated with commuting
  deck action.
- Upper right: trivial and sign isotypic blocks with \(D_+\) and \(D_-\).
- Far right: their product \(D_{\rm reg}\), explicitly labeled “whole
  extension.”
- Lower row: two amber stop boxes, one for primitive lift mismatch and one for
  control universality, both feeding the Route-A rejection.

**Caption.** “Same-object Artin factorization and its scope.  Deck translations
act only on the \(C_2\) fiber, so both character determinants are isotypic
blocks of one regular transfer; their product alone is the whole-extension
determinant.  The factorization is atom-local, but mixed lifted primitives
persist and all inventory controls reproduce it exactly.”

**Implementation.** Pure TikZ in figures/factorization_scope.tex; no external
raster asset or data-generation code is required.  Colors remain distinguishable
in grayscale through line styles and labels.
