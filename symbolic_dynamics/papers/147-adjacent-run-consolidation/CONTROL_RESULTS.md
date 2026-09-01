# Exact control results — P147

## Frozen run

- Bound: all positive compositions of totals `1..18`.
- States: `262,143`.
- Exact assertions: `2,690,869`.
- Sum of nonempty image-target counts over the 18 layers: `50,190`.
- Largest observed one-step fibre: `59`.
- Status: `PASS`.

At `n=18`, the complete depth census is:

```text
tau=0: 10,843
tau=1: 60,946
tau=2: 47,626
tau=3: 11,415
tau=4:    242
```

## Independent checks inside the program

- separator-mask carrier census `|Comp(n)|=2^(n-1)`;
- strict part-count descent and total preservation on every nonfixed step;
- cycle exclusion and fixed endpoint for every state;
- fixed criterion plus an independent last-part DP for Carlitz counts;
- pointwise clock bound and explicit equality witness at every tested size;
- observed source-length fibre counter versus an independently evaluated
  divisor-path dynamic program for every target in the same exact-total
  layer `Comp(n)`, including targets outside the image.

All operations use exact integers.  No random seed, floating point, external
package, or downloaded dataset is involved.
