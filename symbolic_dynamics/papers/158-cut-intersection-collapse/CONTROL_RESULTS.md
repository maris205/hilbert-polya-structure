# P158 exact-control results

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Frozen command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p158.py
```

The canonical stdout is frozen in `verification_output.txt`.

```text
CIC_FOCUSED_EXACT_V1
BOUNDARY A_0(0)=1 A_0(n>0)=0 A_R(0)=1
CASE n=2 t=1 histories=4 image=2 empty=2 max_fibre=2
CASE n=3 t=1 histories=8 image=4 empty=2 max_fibre=2
CASE n=4 t=2 histories=256 image=29 empty=60 max_fibre=60
CASE n=4 t=3 histories=4096 image=29 empty=1880 max_fibre=1880
CASE n=5 t=2 histories=1024 image=121 empty=124 max_fibre=124
CASE n=5 t=3 histories=32768 image=136 empty=9368 max_fibre=9368
CASE n=6 t=2 histories=4096 image=497 empty=252 max_fibre=252
TARGET_CLASS isolates_plus_disjoint_nontrivial_complete_bipartites
FIBRE (R)_r*2^r*A_(R-r)(z)
IMAGE_EGF exp(x)*sum_(r<R)B(x)^r/r!+B(x)^R/R!
TEMPORAL P(T<=t)=A_(2^(t-1))(n)/2^(tn)
ASSERTIONS=77530
STATUS=PASS
```

Transcript SHA-256:
`3e69dfb7d0653c140f2945a6fe4888afc569756a25acf20c1e7eaf2d9f432f0d`.

## Independent interfaces

1. **Independent pathwise identity.** Every vertex-word assignment is first
   run through successive literal cut intersections and separately converted
   through the complement-word relation; the two masks are compared before
   any fibre is accumulated.
2. **Every-target comparison.** Every labelled simple graph in each frozen
   box, including unobserved targets, is classified and its predicted fibre
   is compared with the observed dictionary.
3. **Image count.** A separate labelled component recurrence computes the
   EGF coefficient count, including the isolate-free top-resource boundary.
4. **Temporal controls.** Empty fibres, monotonicity of the absorption CDF,
   the first edge moment, and the union-bound tail are checked exactly.

The verifier uses only Python standard-library integer arithmetic.  It has no
randomness, floating point, runtime network access, CAS, or third-party
dependency.  Finite enumeration does not prove the theorem, exhaust source
owners, establish novelty or priority, or authorize release.
