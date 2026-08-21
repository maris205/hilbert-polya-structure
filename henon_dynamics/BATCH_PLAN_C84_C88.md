# Adaptive batch plan and release record: HCS-C84 through HCS-C88

Status: **round complete; five packages prefreeze-verified and release-ready**

Scope firewall: NO_BAD_EULER_OR_ROOT_NUMBER.

This round extends the frozen named-core lane with five distinct finite
questions. All support, subgroup, Boolean, and permutation calculations use
the source-bound objects explicitly; no arithmetic or operator ownership is
inferred.

## Research sequence

1. **C84 - minimum-repair matroid.** Identify every minimum restoration
   family with a direct-sum truncated partition matroid and classify its basis
   exchange graph.
2. **C85 - threshold-vector poset rigidity.** Compress the complete
   20-target threshold atlas and prove that zero coordinates recover the
   actual subgroup and reverse the coordinatewise order.
3. **C86 - effective-orbit one-bit flip chain.** Strongly lump the 16-cube
   under the faithful order-1920 label image, certify reversible quotient
   flows, and derive the invariant Walsh spectrum.
4. **C87 - label influence and interaction atlas.** Resolve all first-order
   coalition-size swings and all 120 signed second-order pair rows, including
   faithful label/pair orbit structure and the C82 boundary identity.
5. **C88 - subgroup first-passage atlas.** Compute the exact random-order
   first-passage law for all 20 subgroup targets and certify the 102-point
   subgroup stochastic order.

## Authority and group boundary

The common chain is

~~~
C75 11520 ambient lifted closure-incidence symmetry
  |
  +-- C76 faithful 1920 label image and support-orbit atlas
        |
        +-- C78 repair boundary -- C79/C80 -- C81 effective profiles
              |                         |
              +-- C84 repair matroids  +-- C85 threshold vectors
              +-- C82 Walsh/noise -----+-- C86 flip chain -- C87 interactions
                                             |
                                             +-- C88 subgroup first passage
~~~

C75's order 11520 is an ambient lifted pair action. Its order-six kernel
on labels gives the faithful order 1920 image used by C76, C81, C86, and
C87. These orders are never substituted for one another.

## Gate and artifact ledger

All five rows passed producer regeneration, an independent checker, a
separate symbolic or finite cross-check, clean replay, hostile semantic
mutations, and two isolated deterministic LaTeX builds with embedded fonts
and no unresolved references or serious box overflow.

| paper | gate result | hostile mutations | evidence SHA-256 | manifest SHA-256 | PDF SHA-256 |
|---|---|---:|---|---|---|
| C84 | producer/checker/SymPy/replay PASS | 18/18 | 9c3b20c703b680a391ad1834c0f55cabaf27bfed14cee2099b0c3afa1eb259ca | 2957c0837803155fdca24a896accdb95aee147440093fabc1b9ac49bb09e9c8d | 2a37dacc711e5a42dc7b4a33f87d2cc47d31cae20cf05ac345ebcec198c2f4f0 |
| C85 | producer/checker/SymPy/replay PASS | 23/23 | 22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152 | d1e0af8c896e8975ef7544714d379499b2d69e50bdaabf4d8d55621e4c42d261 | 55126890b5bea6894dc2b7bbb90db6525df4e90cebbc3fc80a0e1c952ac5edcc |
| C86 | producer/checker/SymPy/replay PASS | 20/20 | 7b3e2179590c3dc8662a59f1d79ffbb12f2a4a787438a6902d6c28b2842e70b8 | eb223600feb511a52051317b8d80c51423df022a934ca87b6d0ad90b2a4c381f | 544418e44bdf5a22a7a1f416fc4f6367aff6f9320c24986e9de626d0511e4423 |
| C87 | producer/checker/SymPy/replay PASS | 27/27 | bedeb7a3d912330e5eadc72629ee24d773648993f73f20f23eaf477028334d6e | 3f93dddf1421db6f0acb641aa95691ba1b7afcbd17315a79b2b33b3c27e97831 | 6b676d65b14aaf6f93f8d8d5e7226cbac45f1fb1a8379a0240dcbdf1c6cabd13 |
| C88 | producer/checker/SymPy/replay PASS | 40/40 | 4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b | aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5 | d8341a25856ac4d26de0a6398c39c625f8475ab624a923e498fa81a4fca1125b |

## Round-wide release checklist

- [x] C84-C88 producers regenerate canonical evidence without byte drift.
- [x] Independent checkers do not use producer output as a shortcut.
- [x] Symbolic/finite checks, clean replay, and hostile mutations pass.
- [x] C75's ambient 11520 and faithful 1920 actions remain distinct.
- [x] All manifest-listed file hashes match their local files.
- [x] All five papers compile twice in isolation with embedded fonts and no
      unresolved references or serious overfull boxes.
- [x] The scope firewall and all nonclaims remain explicit.

The release operation is limited to these five packages, this batch plan,
the index additions in henon_dynamics/README.md, and the necessary C81/C83
hash-chain repairs. The next five-paper round remains unselected until
explicit confirmation.
