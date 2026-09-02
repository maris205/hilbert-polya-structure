# HCS-C314: Angenent oval under curve shortening

This package closes the central-strip component of the explicit planar
ancient level set `cos(x)=exp(t) cosh(y)`, `|x|<pi/2`,
`-infinity<t<0`: smooth strict convexity, normal
velocity, curvature extrema, strip arrival-time foliation, exact area and
elliptic length, round extinction, and both Grim-Reaper tip limits.

The unrestricted periodic level set in the plane is not one compact curve:
it is the disjoint union of the central oval and its translations by
`(2*pi*k,0)`, `k` integral.  Throughout this package `Gamma_t` means only
the central component.

The negative-time leaves cover the open strip **minus the origin**; the
origin is the separate zero-time extinction leaf.  The package does not
claim a new construction or reprove the literature-wide classification of
convex ancient solutions.

Reproduce the package with:

```bash
python -B code/c314_angenent_producer.py
python -B code/c314_angenent_checker.py
python -B code/c314_angenent_sympy_crosscheck.py
python -B code/c314_angenent_replay.py
python -B code/c314_angenent_mutation.py
python -B code/c314_release_manifest.py
```

The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is false.
