# C149 source audit

## Source lock

The sole infinite component is the two-sided language subshift of
`0 -> 01`, `1 -> 10`.  The only new data are four explicitly tagged finite
cycles of lengths `1,2,3,5`, topologically disjoint from that component.  The
map is the shift on the first component and cyclic successor on each finite
component.  The paper uses no external bibliography and asserts no priority.

## Proof boundary

The Thue--Morse aperiodicity argument is reproduced: for each proposed period
`p`, an odd-popcount multiple `d=p(2^k-1)` creates opposite bits at offsets
`0,d` of every aligned block of length `2^b>d`; every interval of length
`2^(b+1)` contains such a block.  All fixed counts, primitive counts, and
the zeta product then follow for every period from the finite cycle
decomposition.  The 60-period ledger, degree-30 series, and 32 aperiodicity
receipts are replay sentinels, not theorem cutoffs.

The finite components are declared attachments.  They are not points of the
Thue--Morse subshift, and the union is neither minimal nor claimed almost
minimal.  No target or arithmetic data, natural operator, or Route-B input is
used.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
