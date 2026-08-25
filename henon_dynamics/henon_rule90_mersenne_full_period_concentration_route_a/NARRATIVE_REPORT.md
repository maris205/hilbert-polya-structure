# C155 narrative report

C150 identified the exact periodic half-space of Mersenne Rule 90 and proved
that every period divides the circumference.  C155 asks whether that exact
finite-volume structure has a stable asymptotic shape.  The answer is yes:
full circumference period overwhelms every shorter divisor period.

The mechanism is not empirical.  Every proper-time fixed space depends only
on `gcd(j,L)` and has dimension at most twice that divisor.  Oddness forces a
proper divisor below `L/3`, turning the union of all shorter-period fixed
spaces into an exponentially negligible subset of the `2^(L-1)`-point
periodic image.

Burnside converts the same estimate into a second statement: the total cycle
count is asymptotic to image size divided by `L`.  Equivalently, a cycle
chosen uniformly among primitive cycles has average length asymptotic to the
maximum allowed scale.  The power-of-two control remains nilpotent, so the
result is explicitly family-specific and does not claim a universal
thermodynamic determinant.
