# C115 — rational McMillan Route-A pilot

This package freezes the reversible rational map

\[
M(x,y)=\left(\frac{-4x}{1+x^2}-y,\ x\right)
\]

and certifies a finite, exact ledger: the birational inverse and coordinate-swap
reversor, unit Jacobian determinant, a polynomial first integral, the complete
fixed locus over \(\mathbb C\), one real primitive period-two orbit, explicit
pole exclusions, and the local two-step monodromy.  The roots \(x=\pm i\)
introduced by denominator clearing are excluded because the forward map is
undefined there.

The polynomial \(\det(I-zP_2)=(1+z)^2\) belongs only to the derivative of
\(M^2\) along the displayed cycle.  No transfer operator or Fredholm owner is
constructed, so the package records `A2_FAIL`.

## Reproduction

```bash
python code/c115_mcmillan_producer.py
python code/c115_mcmillan_checker.py
python code/c115_sympy_crosscheck.py
python code/c115_replay.py
python code/c115_mutation.py
cd paper && SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cd .. && python code/c115_release_manifest.py
```

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
