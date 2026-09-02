# Independent hostile gate: cyclic equality feedback (CEF)

Verdict: **AMBER-LOW (0 Critical / 1 Major / 2 minor)**  
Allocation decision: **DO NOT ALLOCATE; HOLD_EXTERNAL**  
Mathematical audit: **PASS on the frozen theorem formulas**  
Contribution audit: **FAILS GREEN pending an independent second axis**

## Frozen object and independence

Reviewed author snapshot hashes:

| file | SHA-256 |
|---|---|
| `SCOUT.md` | `4974107a9bfbe24759daf61520ab81f49415b2d97f2ab64ceaa5414a2b416554` |
| `OWNER_SEARCH_LOG.md` | `45bab1cf97d5ddaa65e37f6e1918b6723961edcdab30c56e1bba5297dd4ddaec` |
| `verify_scout.py` | `15dd285a430b2e5902fac057a8d823bd69a3609e70e8b8d700af8f5f88a8c9db` |
| `CANONICAL.txt` | `f84897b79698b9063d5f6eb6cee3fb2e0f7cf8146b11424fc4446ac6753081f5` |

The hostile verifier uses packed integers, direct literal q-ary iteration,
an independently implemented cyclic difference, and an independently summed
character formula.  It imports no author module and reads no author output.

## Independent derivation

Let `c(w)_i=1{w_i != w_(i+1)}` and let `S` be the matching cyclic shift on
binary vectors.  Put `D=I+S`.  The first state is `T(w)=1+c(w)`.  For a binary
state `b`, `T(b)=1+Db`, while `D1=0`; induction gives

`T^t(w)=1+D^(t-1)c(w)` for every `t>=1`.

For `n=2^m`, the group algebra is
`F_2[x]/(x^n-1)=F_2[x]/((x+1)^n)`.  Multiplication by `x+1` is one nilpotent
Jordan block.  Consequently `D^n=0`, `dim ker D^j=j`, and
`im D^j=ker D^(n-j)`.

If `r=wt(c)`, contracting equality edges reduces the number of q-ary words
with change mask `c` to the proper-colouring count of a cycle:

`chi_q(c)=(q-1)^r+(-1)^r(q-1)`.

This includes `chi_q(0)=q`, vanishes exactly at `r=1`, and is positive for all
other masks when `q>=3` and `n>=4`.

Define `W_{n,j,d}(a)=sum_{D^j c=d} a^wt(c)` and `W_{n,j}=W_{n,j,0}`.  Then the
depth CDF is

`C_{n,j}(q)=W_{n,j}(q-1)+(q-1)W_{n,j}(-1)`,

and the shells are `N_0=1`, `N_1=q-1`,
`N_{j+1}=C_{n,j}-C_{n,j-1}`.  At dyadic `j=2^r<n`, kernel words repeat a
length-j block `n/j` times, yielding

`C_{n,j}=(1+(q-1)^(n/j))^j+(q-1)2^j`.

Since `ker D^(n-1)` is the even-weight hyperplane, the final shell is

`N_{n+1}=(q^n-(q-2)^n)/2-(q-1)2^(n-1)>0`.

Thus the unique recurrent state is `1`, the sharp maximum depth is `n+1`, and
the claimed last layer is genuine.

At time one, a binary target `y` corresponds to `c=y+1`, so precisely the `n`
targets for which `y+1` is a unit vector are absent.  Hence
`|im T|=2^n-n`.  At time `t>=2`, put `j=min(t-1,n)`.  The prospective support
is `1+im D^j`.  Each affine coset contains a feasible change mask: if a chosen
mask is a forbidden unit, adding the all-one kernel word produces weight
`n-1`, which is feasible for `n>=4`.  Therefore

`im T^t=1+im D^j`, with size `2^(n-j)`.

For every binary target `y`, with `d=y+1`, the exact fibre is

`|(T^t)^(-1)(y)|=W_{n,j,d}(q-1)+(q-1)W_{n,j,d}(-1)`.

For nonbinary targets it is zero once `t>=1`.  Character orthogonality gives

`W_{n,j,d}(a)=2^(-n) sum_lam (-1)^(lam.d)
 (1+a)^(n-wt((D^j)^T lam)) (1-a)^wt((D^j)^T lam)`.

After `t>=n+1`, only the all-one target remains and its fibre is `q^n`.
Finally, the time-one all-one fibre has size `q`, and the maximum depth minus
one is `n`, so the labelled functional graph recovers both parameters.

## Boundary attacks

- `t=0`: verified separately as the identity with singleton fibres; it must not
  be passed through the binary-target formula.
- `t=1`: all and only the `n` complement-of-unit targets are holes.
- `t>=2`: support is the claimed affine image for every tested target, source,
  and cap time.
- `q=2`: the time-one support formula fails (`n=4` gives 8 rather than 12), so
  the lower bound `q>=3` is essential.
- `n=2`: the all-one repair sends one forbidden unit to the other; at `q=3`
  the time-two image has size 1 rather than the predicted 2.  Thus `n>=4` is
  essential and not cosmetic.
- Asymmetric directions were tested through separately coded right-shift `D`
  and left-shift transpose `D^T` in the Fourier identity.

No mathematical red flag survived these attacks.

## Independent executable evidence

`verify_hostile.py` exhaustively checks six boxes:
`(n,q)=(4,3),(4,4),(4,5),(4,7),(8,3),(8,4)`.

It performs **840,240 assertions**, including **11,008 independently summed
Fourier checks**, over literal words, all masks, all binary targets, all times
through the cap, kernel/image flags, depth shells, and two excluded-boundary
sentinels.

Two fresh replays were byte-identical to `CANONICAL.txt`:

- replay 1 SHA-256: `8a4a072f4fd0d416189e9c2e5cd45714ae69953d8c7d621ea9c48c1697ffb7ed`
- replay 2 SHA-256: `8a4a072f4fd0d416189e9c2e5cd45714ae69953d8c7d621ea9c48c1697ffb7ed`
- verifier SHA-256: `3d813d81ca74c85a8abaac9ca8a9babe5d5265a841032e95ba1e7bc5b8a3d88c`

Reproduction command:

```bash
python3 docs/papers162_166_sequence/phase1/cef_hostile_gate/verify_hostile.py
```

## Findings

### Major M1 -- proposed second axis is not independent after subtraction

The clock CDF is a zero-target weighted kernel enumerator; the every-target
formula is the corresponding weighted affine-coset enumerator.  Both use the
same change-mask multiplicity and the same `D^j` filtration.  The Fourier
display is correct but is generic character orthogonality and does not
evaluate or classify target dependence.  Because homogeneous kernels are
repeated-root cyclic codes with a current general weight-distribution owner,
the existing fibre presentation is not enough to establish a second
paper-level axis.

**Executable repair:** prove one result not reducible to the present zero-coset
engine: an explicit fibre-spectrum classification, a sharp maximum/minimum
fibre theorem with all equality targets, or a q/deformation theorem with a
different invariant.  The statement must evaluate target dependence rather
than rename it as `W_{n,j,d}` or leave it as an exponential character sum.

### minor m1 -- owner firewall omits a strong 2025 cyclic-code source

Zhao--Li--Yang--Fu--Shum explicitly studies weight distributions of all
repeated-root cyclic codes of prime-power lengths.  The author firewall should
identify `ker D^j=< (x+1)^(n-j) >` and subtract this lane before stating a
residual contribution.

**Repair:** add the source and state explicitly that kernel enumerators,
dyadic repeated-block cases, and the last hyperplane receive no novelty credit.

### minor m2 -- CA terminology and inverse notation need precision

The one-sided operator is Rule 102 and its affine complement Rule 153, not
literally Rule 90.  Also `T_q^{-t}(y)` can be read as an inverse iterate, which
does not exist for this map.

**Repair:** use Rule 102/153 (or explain a shear equivalence) and write
`(T_q^t)^(-1)(y)` for a preimage fibre.

## Final decision

CEF is mathematically clean and stronger than a thin action-only construction;
the q-ary nonlinear front, exact support holes, and parameter recovery are
real.  However the current “front + every-target Fourier fibre” package does
**not yet supply a logically independent second axis** under the batch's strict
threshold.  The correct gate is therefore **AMBER-LOW, not GREEN**.  It may
re-enter only after closing M1; until then it remains **HOLD_EXTERNAL** and
should not become a paper.
