# C158 paper improvement log

No external or cross-model reviewer was available or claimed.  Both rounds
are genuine internal theorem/scope audits without numerical scores.

## Round 0 to round 1

The initial draft spoke of a “spectral log distribution” without freezing
whether it meant eigenvalue moduli, secular-zero inverse radii, or an
unnormalized logarithm.  It also stated concentration without a scale-explicit
derivation.

**Fix:** define `X_k=k^(-1)log|rho|` only for nonzero eigenvalues of
`C_k=B_k^k`, counted with algebraic multiplicity; explicitly decline the
inverse-zero convention; derive the affine binomial model, exact variance,
Hoeffding exponent, weak limit, and characteristic-function CLT.

## Round 1 to round 2

The second audit found three scope risks.  Product collisions needed retained
algebraic multiplicity; “zero dimension” needed to mean generalized
eigenspace; and a proposed moved-hole change of both mean and variance was
false.

**Fix:** use the distinct one-site roots to prove diagonalizability and the
`3^k-2^k` generalized zero dimension; preserve binomial multiplicities even
under collisions; compute moved-hole roots exactly.  The mean is unchanged,
while the variance changes.  Add explicit nonclaims for phase, self-adjoint,
target, arithmetic, and Route-B limits.

## Final audit

The final artifact is checked against exact field and binomial evidence,
literal Kronecker determinants, independent checker and SymPy paths, replay,
hostile mutations, seven-mode failure audit, deterministic compilation,
embedded fonts, clean logs, extracted text, and rendered pages.

The release-completeness pass independently composed structurally aligned
English and Simplified Chinese abstracts, supplied six keywords in each
language, and added explicit data, ethics, anonymous CRediT-role, conflict,
funding, and AI-use declarations.  Chinese glyph support therefore uses the
embedded Droid Sans Fallback face under LuaLaTeX; this formatting pass changes
no theorem or finite evidence claim.

## Release-gate cross-review repair

An internal cross-review then found that the evidence hash covered every byte,
but the independent checker had not assigned exact semantic checks to 16
claim-bearing nested leaves and did not close every nested key set or list
population.  Repaired-hash changes to those leaves could therefore pass.

**Fix:** close every nested evidence dictionary, verify every list population
and receipt shape, replace prefix/suffix control checks by exact values, and
add hostile cases for the 16 leaves plus deletion, duplication, missing-key,
extra-key, coefficient-basis, and binomial-identity attacks.  The strengthened
checker passes 439 assertions and rejects 85 repaired-hash cases plus one
stale-hash case.  Evidence and PDF bytes are unchanged.
