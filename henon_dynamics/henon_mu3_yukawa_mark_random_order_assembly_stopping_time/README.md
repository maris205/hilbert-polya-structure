# HCS-C83 random-order prefix assembly stopping time

C83 samples a uniformly random permutation of the sixteen named labels and
reveals its prefixes.  The stopping time is

```text
T = min{k : Phi(first k labels)=Q}.
```

Exact subset closure enumeration gives full-core supports by size
`{3:25,4:224,5:940,6:2461,7:4504,8:6095,9:6269,10:4950,
11:2992,12:1364,13:455,14:105,15:15,16:1}`.  If `p(S)` is the number of
labels whose removal destroys full closure, then
`N_k=sum_{|S|=k}p(S)(k-1)!(16-k)!`.  The resulting stopping-time counts are

```text
T=3: 934053120000
T=4: 1641059481600
T=5: 1927502438400
T=6: 1927328256000
T=7: 1807490764800
T=8: 1671222067200
T=9: 1556813260800
T=10:1467573811200
T=11:1398684672000
T=12:1348868505600
T=13:1319170406400
T=14:1307674368000
T=15:1307674368000
T=16:1307674368000.
```

They sum to `16! = 20922789888000`; the exact mean is
`36499/3960 ≈ 9.21691919`.  The canonical evidence SHA-256 is
`4777695a3082a2cca1ee82cdced208f0bddf56431285774a51e7563c4cfdfea0`.
The complete prefreeze file binding is recorded in
[C83_PREFREEZE_MANIFEST.json](C83_PREFREEZE_MANIFEST.json).
Independent closure/pivotal enumeration, a SymPy
generating-polynomial check, replay, and hostile mutations certify the result.

This is a finite random-order statistic only: no arithmetic/local, Euler,
root-number, automorphy, full Burnside/table-of-marks, or Hilbert--Polya claim
is made.  Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
