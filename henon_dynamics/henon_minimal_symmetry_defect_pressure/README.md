# HCS-P65: Minimal symmetry-defect pressure

P64 left the specific Mahler-slope gap open because an explicit cylinder
distortion constant is not yet available. P65 supplies a rigorous calibration
direction instead of extrapolating decimals.

On the full two-shift define

```text
chi(omega)=1{omega[-1]=omega[+1]}.
```

The marked reflection-boundary law has expectation `1`; maximal entropy has
expectation `1/2`. No observable depending on finitely many coordinates all
on one side of the reflection axis can distinguish the two laws, so this is
minimal at centered radius one. The corresponding extensive pressures are

```text
P_axis(t)  = (1/2)log(2) - t,
P_orbit(t) = (1/2)log(2) - t/2.
```

Adding the P64 Mahler variable gives two pressure planes whose `t`-gradients
differ exactly by `1/2`, independently of the unresolved Mahler constants.

**Status:** minimality and pressure separation `PROVED`; Mahler-slope
separation `OPEN`; Route A exploratory; Route B not authorized.

Reproduce with `bash code/run_c65.sh`. The paper is
[`paper/paper.pdf`](paper/paper.pdf).
