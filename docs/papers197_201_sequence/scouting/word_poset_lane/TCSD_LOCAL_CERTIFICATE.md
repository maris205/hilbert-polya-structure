# TCSD local attraction certificate

This file isolates the only finite case lemma used in the all-size attraction
proof.  It is both human-auditable and replayed independently by
`verify_word_poset_lane.py`.

## Run contraction

For a nonconstant cyclic word `x` over `-<0<+`, let `R(x)` be its longest
constant cyclic run.  In `D(x)`:

- a zero-run of length `q` requires `q+1` equal adjacent letters in `x`, so
  `q<=R(x)-1`;
- a plus-run is a strict increasing chain in a three-element chain, and a
  minus-run is a strict decreasing chain, so either has length at most two.

Therefore

```text
R(Dx)<=max(R(x)-1,2).                                  (L1)
```

If `R(x)=1`, use a length-six window `w=w_0...w_5`.  The needed identity is

```text
delta^5(w)_0=delta(w_2w_3)_0.                         (L1b)
```

There are `3*2^5=96` words with no equal adjacent pair.  Up to negation and
reversal, their middle pair is `-0` or `-+`; the two classes have orbit sizes
four and two, respectively, and each representative has 16 admissible outer
extensions.  The left side of (L1b) is `+` in all 32 representative
extensions, exactly the right side.  Thus `4*16+2*16=96` gives complete
coverage and proves `D(x) in K`.  The slightly larger `R(x)<=2` case is the
certificate below.

## Length-seven identity

Let `w=w_0...w_6` have no constant factor of length three.  Then

```text
delta^6(w)_0=delta^2(w_2w_3w_4)_0.                    (L2)
```

There are 1,344 such words.  Negating every letter and reversing the word
reduce the middle triple to the eight rows below.  `extensions` is the
number of admissible choices of the two letters on each side for the shown
representative; `orbit` is its symmetry-orbit size.  In every extension,
the left side of (L2) is the displayed right-side value.

| middle triple | orbit | extensions | common value |
|---|---:|---:|---:|
| `--0` | 4 | 48 | `+` |
| `--+` | 4 | 48 | `+` |
| `-0-` | 2 | 64 | `-` |
| `-00` | 4 | 48 | `-` |
| `-0+` | 2 | 64 | `0` |
| `-+-` | 2 | 64 | `-` |
| `-+0` | 4 | 64 | `-` |
| `0-0` | 2 | 64 | `+` |

Coverage is exact:

```text
4*48+4*48+2*64+4*48+2*64+2*64+4*64+2*64=1344.
```

Applying (L2) at every cyclic position says

```text
D^6(x)=rho^2 D^2(x),
```

so `D^2(x)` lies in `K={y:D^4y=rho^2y}` whenever `R(x)<=2`.
Together with (L1), this proves entry into `K` in at most `R(x)` steps (with
the `R=1` length-six subcase).

## Why this is an all-size proof

The table is not enumeration over cyclic carrier sizes.  It verifies a
radius-six local identity once.  Every coordinate of every cyclic word of
every length is covered, including windows that wrap or repeat coordinates.
The verifier separately checks the resulting core equality against complete
functional graphs through length 12; that second check is falsification, not
the logical basis of the all-size lemma.
