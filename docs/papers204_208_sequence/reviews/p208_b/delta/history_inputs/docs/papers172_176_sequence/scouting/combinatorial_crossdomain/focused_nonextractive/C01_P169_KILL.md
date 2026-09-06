# Minimum-ordered matching cross: exact signal and P169 kill

**Lifecycle:** `HOLD_EXTERNAL`.  **Decision:** `KILL_INTERNAL_P169_PAIR_SLICE`.

For a perfect matching on `[2m]`, write its edges as

```text
(l_0,h_0),...,(l_(m-1),h_(m-1)),   l_0<...<l_(m-1), l_i<h_i.
```

The tested update replaces these edges by

```text
(l_i,h_(i+1 mod m)),   i in Z/mZ,
```

and canonically reorders endpoints and edges.  It is a valid autonomous map
on all labelled perfect matchings.  Exact enumeration through `m=6` gives:

| `m` | states | image | max tail | recurrent cycles | max fibre |
|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 2 | 1 | one 2-cycle | 2 |
| 3 | 15 | 12 | 2 | two 3-cycles | 2 |
| 4 | 105 | 96 | 3 | six 4-cycles | 3 |
| 5 | 945 | 768 | 4 | twenty-four 5-cycles | 4 |
| 6 | 10,395 | 3,840 | 5 | one hundred twenty 6-cycles | 5 |

The clean signatures are respectively consistent with tail `m-1`, recurrent
state count `m!`, `(m-1)!` cycles of exact period `m`, image
`2^(m-1)(m-1)!`, and maximum fibre `m-1` for `m>=3` (the `m=2` maximum is
two).

They do not survive the internal gate.  Encode a matching by the restricted
growth word obtained by labelling its blocks in increasing order of their
minimum.  Each label then occurs exactly twice.  Under the displayed update,
the second occurrence from block `i` is transferred to the cyclic predecessor
block.  P169 transfers the final repeated occurrence of every nonsingleton
RGF label to the cyclic successor block.  Therefore this map is precisely the
opposite-direction restriction of the P169 successor-transfer mechanism to
pair partitions.

Changing successor to predecessor does not create a new proof engine: the
same cyclic load/queue evolution, exact period, and restricted-growth
canonicalization apply after reversing the transfer direction.  The tidy
matching numbers are useful regression controls, but no theorem from this
slice is eligible for a new paper.
