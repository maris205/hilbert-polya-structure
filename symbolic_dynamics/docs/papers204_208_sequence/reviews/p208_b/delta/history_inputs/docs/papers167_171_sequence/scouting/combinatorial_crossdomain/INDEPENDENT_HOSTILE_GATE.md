# Independent hostile gate — successor transfer on set partitions

**Reviewer:** coordinator, independent of the cross-domain scout  
**Date:** 2026-09-03  
**Verdict:** `GREEN_OWNER_THIN / ELIGIBLE_FOR_INTERNAL_P169 / HOLD_EXTERNAL`

## 1. Literal-system audit

The state is a canonically ordered set partition
`(B_0,...,B_{k-1})` of `[n]`.  Every nonsingleton block simultaneously sends
its maximum to its cyclic successor.  A donating block retains its minimum;
an incoming maximum from `B_{i-1}` is larger than the retained minimum of
`B_{i-1}`.  The canonical block order is therefore preserved rather than
silently recomputed into a different block correspondence.  In restricted-
growth notation, the update changes the final occurrence of each repeated
letter `i` to `i+1 mod k`.  It preserves the number of blocks.

This literal equivalence, including the wrap from `k-1` to zero, was checked
directly and against the focused verifier.

## 2. Temporal proof rederivation

Writing `z_i=|B_i|-1`, the load factor is

```text
z_i' = z_i - 1[z_i>0] + 1[z_(i-1)>0].
```

The periodic height lift satisfies

```text
H_i(t+1)=max(H_i(t)-1,H_(i-1)(t)).
```

Its explicit max-plus solution yields the two cone implications used in the
proof.  At time `m-1` when total excess `m<=k`, a pile of height at least two
would require more than the total mass.  At time `k-1` when `m>=k`, an empty
queue would force the total mass below `k`.  Thus the sparse `0/1` and dense
positive load regimes are reached in the claimed sharp upper times.

The second, labelled phase was also attacked separately.

- In the dense regime, occupancy of the final `k` word positions follows the
  same queue rule with mass exactly `k`; after at most `k-1` steps the window
  contains every letter once.
- In the sparse regime, prefix occupancies lie in `{0,1,2}` with as many
  excess particles as holes.  A `2` advances clockwise until it fills a `0`;
  all such pairs disappear within `k-1` steps.  Distinct first `k` letters in
  a restricted-growth word must be `0,1,...,k-1`.

The witness `0^(n-k+1)12...(k-1)` realizes both phases.  The displayed
intermediate words show that it does not enter the recurrent window early.
Therefore, for `1<k<n`,

```text
max tau on Pi_(n,k) = min(n-2,2k-2),
```

and the global height is `n-2` for `n>=2`.  The one-block and all-singleton
states are fixed.

## 3. Recurrent and inverse audits

Once the load and canonical-window conditions hold, the retained prefix is
fixed and successor transfer adds one modulo `k` to a nonempty suffix
permutation/injection.  This proves exact period `k` for every nontrivial
recurrent `k`-block state, and gives

```text
k! S(n-k,k)       when n>=2k,
(k)_(n-k)         when n<=2k.
```

The formula agrees at `n=2k`.  A P169 manuscript must qualify the sentence
about the period set by `n>=2`; at `n=1` the unique state is fixed and the
one-block/all-singleton descriptions coincide.

The five-state inverse formula is not a repackaging of the load factor.
For a target block `C_i`, the state records whether the incoming token is
absent, the singleton, the minimum, the maximum, or an interior point.
After removing that token, source block `i` is inactive exactly when the
remainder is a singleton; otherwise its chosen outgoing token must exceed the
remainder maximum.  Adjacent source minima are compared only for
`i<k-1`, correctly respecting linear canonical order despite cyclic transfer.
Matrix multiplication matches the outgoing state at `i` with the incoming
state at `i+1`, and the trace closes the wrap.  The local token choices recover
the predecessor uniquely, so

```text
|T^(-1)(C)| = tr(M_0(C)...M_(k-1)(C)).
```

This is a fixed-size transfer expression, but it is an exact structural
formula: its five states are uniform in `n,k`, its entries are explicit local
counts, and positivity gives a complete image criterion.  The targets
`025|134` and `035|124` have the same coarse block size/minimum/maximum data
but fibres two and one, proving that the inverse axis retains labelled
interlacing erased by the temporal quotient.

## 4. Exact replay

The focused verifier was run in a fresh process and compared byte for byte
with `STF_CANONICAL.txt`.  The comparison passed.  It records `1,217,023`
assertions, including all partitions through `n=10`, all 26,442 targets
through `n=9`, 532,467 queue-cone cases, and sharp witnesses through `n=50`.

```text
verify_stf.py      8e5c83a06bb0ce1449241fbb79061f27434ec9ff57237d8ab02b60fa11265479
STF_CANONICAL.txt  0d8f2692ecf968e2a140c5a6f3b96d9ffe14ae51785af371d56fd7ff56d3ef90
```

Enumeration is used only as falsification and implementation pressure.

## 5. Owner and collision subtraction

Joseph--Propp--Roby directly own whirling on restricted-growth words, but
their action is a sequential composition of invertible local maps.  STF is a
simultaneous last-occurrence transfer with nonuniform fibres and transients.
Ji--Li--Wang and earlier chip-firing literature own the directed-cycle load
factor; that factor receives zero credit.  Restricted-growth encodings,
Bulgarian solitaire, promotion/jeu de taquin, box-ball systems, set-partition
stack sorting, Stirling counts, and generic transfer matrices likewise receive
zero contribution credit.

Internally, P90 consumes the traffic projection, P110 consumes cyclic
partition joins, and P126/P137/P147 consume their split/consolidation
architectures.  None transfers the preserved-block labelled maximum rule or
the interlacing-sensitive inverse matrix.  Generic clocks, fibres, periods,
and zeta conversion are not separation evidence.

Bounded literal searches found no same-map owner.  This non-hit is not a
novelty or priority certificate.

## 6. Decision and ceiling

The candidate has two genuinely independent all-parameter axes and clears the
internal value gate.  It may be drafted as P169 at `GREEN_OWNER_THIN`, subject
to all of the following:

1. the load projection and RGF carrier are explicitly owner-subtracted;
2. the transfer matrices are printed explicitly enough to be evaluated from
   a target, not described as an unspecified algorithm;
3. `n=1`, `k=1`, `k=n`, `n=2k`, singleton blocks, and cyclic wrap boundaries
   are visible;
4. no novelty/priority language appears and status remains `HOLD_EXTERNAL`;
5. two manuscript-level hostile reviews are completed after Round 0.

A direct same-map source or a proof transfer consuming the labelled fibre
axis reopens the slot.
