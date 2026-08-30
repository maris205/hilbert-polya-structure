# S01 hard PGF pilot: commutation--idempotence rewrite

**Decision:** **KILL**  
**External status:** `HOLD_EXTERNAL`  
**System:** choose uniformly among literal redex occurrences of
`BA -> AB` and `AA -> A`, starting from `B^b A^a`, with `a >= 1`,
`b >= 0`  
**Target:** `F_{a,b}(z)=E[z^T]`, where `T` is the number of rewrites to
`A B^b`

## Target and status

The hard gate from `phase1/OWNER_GATE_STOCHASTIC.md` required a full
coefficient-level law for all `a,b`, or an equivalently strong bivariate
generating function, not a finite-state recurrence. This pilot found:

1. an exact recurrence on gap populations, with redex denominator collapsing
   to one scalar;
2. a pathwise Young-diagram and iterated-record representation;
3. two closed boundary families: a rising-factorial law for `b=1` and a
   truncated Catalan law for `a=2`;
4. an exact coefficient integral over record chambers.

It did **not** turn the general record-chamber integral into a hook product,
determinant, coefficient extraction, or bivariate generating function. Exact
data actively falsify the three natural collapses: independent record layers,
the uniform linear-extension/tableau measure, and a real-linear-factor product.
The owner-gate requirement is therefore not met. The decision is a firm
candidate-level **KILL**, not a claim that no formula can ever exist.

## Invariant object

Keep the `b` copies of `B` fixed and write every reachable word uniquely as

```text
A^x_0 B A^x_1 B ... B A^x_b,
```

where `x_i >= 0`. The starting vector is `(0,...,0,a)` and the absorbing vector
is `(1,0,...,0)`. Let `k=sum_i x_i` be the live number of `A` particles.

There are `x_i-1` literal `AA` redexes in gap `i` when `x_i >= 2`, and there is
one `BA` redex immediately before gap `i` when `i>=1` and `x_i>0`. Hence the
total number of current redex occurrences is

```text
R(x) = sum_i (x_i-1)_+ + sum_{i=1}^b 1{x_i>0}
     = k - 1{x_0>0}.
```

This identity is the useful compression: before an `A` reaches the far-left
gap, every live particle carries one redex; afterwards the leftmost particle is
inactive and every other live particle carries one redex.

## Assumptions and notation

- Redex **occurrences**, not distinct successor words, are sampled uniformly.
  Thus `A^m -> A^(m-1)` has multiplicity `m-1`.
- Products and probabilities are exact rational quantities.
- `P_x(z)` denotes the absorption-time PGF from gap vector `x`.
- The initial PGF is `F_{a,b}(z)=P_{(0^b,a)}(z)`.
- `C_r=(1/(r+1))*binom(2r,r)` is the `r`-th Catalan number.
- `(z)^(overline a)=z(z+1)...(z+a-1)` is the rising factorial.

The endpoint conventions are

```text
F_{a,0}(z)=z^(a-1),       F_{1,b}(z)=z^b.
```

## Derivation strategy

The dependency chain is

```text
literal redexes
    -> gap populations x
    -> labelled crossing-count partition lambda
    -> independent rate-one particle clocks
    -> nested records of Gamma arrival times
    -> two solvable boundary slices + a general record-chamber integral.
```

The first two arrows give an exact dynamic program. The third and fourth arrows
are the attempted non-DP transformation. They explain the Catalan and
rising-factorial edges, but the dependence between successive record layers is
exactly what prevents the general collapse.

## Main derivation

### 1. Exact gap recurrence

An `AA` move in gap `i` sends `x` to `x-e_i` and occurs with multiplicity
`(x_i-1)_+`. A `BA` move immediately before gap `i>=1` sends `x` to
`x+e_{i-1}-e_i` and has multiplicity one. Therefore

```text
P_x(z) = z/R(x) * [
    sum_i (x_i-1)_+ P_{x-e_i}(z)
    + sum_{1<=i<=b, x_i>0} P_{x+e_{i-1}-e_i}(z)
],
```

with `P_(1,0,...,0)(z)=1`. This is exact, orientation-sensitive, and retains
duplicate successors correctly.

For fixed `a,b`, it uses at most

```text
sum_{k=1}^a binom(k+b,b) = binom(a+b+1,b+1)-1
```

composition states. This is much smaller than enumerating all binary words,
but it is still precisely the kind of state DP excluded by the owner gate.

### 2. Young-diagram form

Label the initial `A` particles from left to right. Within each `A` block,
associate an `AA` occurrence with the particle immediately to its right and
interpret the rewrite as deleting that right particle. Associate the unique
`BA` redex of a non-leftmost gap with the leftmost particle of that gap. This is
a bijection between literal redex occurrences and active labelled particles.

For every live particle, let `lambda_j` be the number of `B` letters it has
crossed. In live-particle order,

```text
b >= lambda_1 >= lambda_2 >= ... >= lambda_k >= 0.
```

Thus `lambda` is a Young diagram in a `k x b` rectangle. Selecting row `j`
does exactly one of the following:

- if `j=1` and `lambda_1<b`, add one box to row 1;
- if `j>1` and `lambda_j<lambda_(j-1)`, add one box to row `j`;
- if `j>1` and `lambda_j=lambda_(j-1)`, delete row `j`.

Once `lambda_1=b`, row 1 is the inactive immortal root. The active-row count
is therefore `k` before that time and `k-1` afterwards, exactly matching
`R(x)`. The partition and gap descriptions are equivalent under

```text
x_i = number of rows of length b-i.
```

This is a clean structural model, but its ordinary transition graph has the
same composition-state size as the gap recurrence.

### 3. Genealogy by independent clocks

Give every active particle an independent rate-one Poisson clock. Competing
exponentials select the next redex uniformly, so the embedded jump chain is the
original rewrite process. For particle `j`, write

```text
S_(j,r) = E_(j,1)+...+E_(j,r),
```

where the `E_(j,r)` are independent `Exp(1)` variables. These are the absolute
times of its successive clock rings while it remains alive.

Define nested sets `L_r` as follows. Start with `L_0={1,...,a}` in label order.
For `r=1,...,b`, scan `L_(r-1)` from left to right and retain precisely the
upper-record indices of the values `S_(j,r)`. In other words, `j` is retained
when its `r`-th clock time is larger than every previously retained candidate's
`r`-th clock time.

**Pathwise record lemma.** `L_r` is exactly the set of particles that cross at
least `r` copies of `B`.

The proof is an induction on `r`. Among particles that reached level `r-1`, the
first candidate reaches level `r`. Scanning rightward, a particle whose `r`-th
ring precedes the last retained predecessor's `r`-th ring is selected while
tied at level `r-1` and is deleted. If its ring is later, that predecessor has
already crossed and the particle can cross too. If an intermediate predecessor
subsequently dies, the same time inequality makes the record scan skip it
without changing the decision. This is exactly the upper-record update.

Every nonroot particle is selected once more when it is deleted, whereas
particle 1 crosses all `b` barriers and is then inactive. Consequently

```text
T = (a-1) + sum_{r=1}^b |L_r|,
```

and the full PGF has the non-DP representation

```text
F_(a,b)(z) = z^(a-1) E[z^(sum_r |L_r|)]
           = z^(a+b-1) E[z^X],

X = sum_{r=1}^b (|L_r|-1).
```

The exact script checks this pathwise identity on hundreds of deterministic
rational clock arrays, in addition to comparing the resulting PGFs with both
literal-word and gap recurrences.

### 4. Exact coefficient integral

For a fixed particle, the joint density on
`0<s_(j,1)<...<s_(j,b)` is `exp(-s_(j,b))`. Let `X(s)` be the nested-record
statistic above and let `D_m` be the union of record chambers on which `X(s)=m`.
Then

```text
[z^(a+b-1+m)] F_(a,b)(z)
  = integral_(D_m) exp(-sum_j s_(j,b)) product_(j,r) ds_(j,r).
```

The chambers are cut out by linear comparisons among same-level arrival
times, so this is a finite exact rational integral. It is nevertheless not a
closed coefficient formula: specifying `D_m` requires the same nested record
genealogy, and its chamber count grows combinatorially. No determinant,
hook-length evaluation, or one-variable coefficient extraction was obtained.

### 5. Solvable edge `b=1`: records and rising factorials

For one barrier, `L_1` is the ordinary upper-record set of `a` iid continuous
variables. Its record indicators are independent Bernoulli variables with
success probabilities `1,1/2,...,1/a`. Hence

```text
F_(a,1)(z)
  = z^(a-1) * (z)^(overline a) / a!.
```

This explains, for example,

```text
F_(4,1)(z)=z^4(6+11z+6z^2+z^3)/24.
```

It is a classical record-number law attached to this rewrite, not an all-`b`
formula.

### 6. Solvable edge `a=2`: truncated Catalan law

With two particles, let `D` be the crossing-count gap between the immortal
first particle and the second particle. Before the first particle finishes,
the next selection is a fair choice. A first-particle selection sends
`D -> D+1`; a second-particle selection sends `D -> D-1` when `D>0` and kills
the second particle when `D=0`.

Let `X=T-(b+1)` be the number of barriers crossed by the second particle. For
`0<=r<b`, death after exactly `r` crossings consists of a Dyck path with `r`
up-steps and `r` down-steps followed by the fatal down-choice. Therefore

```text
P(X=r) = C_r / 2^(2r+1),                0 <= r < b.
```

If the first particle completes its `b` crossings before this fatal choice,
the second particle is then the only active particle and deterministically
crosses the remaining barriers before deletion. The ballot/reflection count
gives

```text
P(X=b) = binom(2b,b) / 2^(2b).
```

Thus

```text
F_(2,b)(z) = z^(b+1) * [
    sum_(r=0)^(b-1) C_r z^r / 2^(2r+1)
    + binom(2b,b) z^b / 2^(2b)
].
```

For `b=0`, the sum is empty and the terminal term equals one.

## Exact falsification results

The fresh script

```text
python docs/papers117_121_sequence/proof_spikes/stoch_s01_hard_pgf.py
```

returns

```text
stoch_s01_hard_pgf: PASS
assertions=9623
word_cache=3424
gap_cache=4715
diagram_cache=3424
closed_edge_b1=z^(a-1)*(z)^(rising a)/a!
closed_edge_a2=truncated Catalan first-passage law
killed=independent_layers, uniform_SYT_measure, real_linear_factor_product
gate=KILL_no_full_coefficient_law
```

The decisive exact sentinels are

```text
F_(2,3)(z)=z^4(8+2z+z^2+5z^3)/16,

F_(3,2)(z)=z^4(216+72z+266z^2+45z^3+49z^4)/648.
```

They kill three tempting routes:

1. **Independent record layers fail.** At `(a,b)=(2,2)`, independent
   record filtering would give extra-crossing masses `(1/2,1/4,1/4)`. The
   exact law is `(1/2,1/8,3/8)`. Successive Gamma-arrival rankings retain
   essential dependence.
2. **Uniform linear extensions/SYT fail.** Full survival in the `2 x 2`
   rectangle has exact mass `3/8`. Giving the six two-letter multiset words
   equal weight and counting the two ballot words would give `2/6=1/3`.
   Ordinary hook-length counting therefore uses the wrong measure.
3. **A rising-factorial/real-linear-factor extension fails.** After removing
   the deterministic factor `z^4`, the `(2,3)` numerator is
   `5z^3+z^2+2z+8`. Its exact discriminant is `-41948`, so it has a nonreal
   conjugate pair. The `b=1` real-linear product does not persist.

## Owner subtraction and decision boundary

The normal form, bounded fibre, support, and minimum atom were already
subtracted in the Phase-3 owner gate. The new Young-diagram/record description
does not restore a contribution by itself: ordinary and multivariate record
statistics are established territory (a nearby, not identical, reference is
[Gnedin's chain-record paper](https://doi.org/10.1214/EJP.v12-410)), and the
queue/tableau proof neighborhood is likewise mature
([Draief--Mairesse--O'Connell](https://doi.org/10.1239/jap/1134587823)). Neither
reference is asserted to contain this exact nested Gamma-prefix statistic; the
point is that a transformation into those languages still needs a genuinely
new evaluated law.

What remains is:

- a composition-state recurrence;
- an unevaluated record-chamber integral;
- two classical-looking one-parameter boundary slices.

That package falls short of the stipulated all-parameter coefficient theorem.
Accordingly:

```text
S01 = KILL
paper number = not assigned
novelty/priority/external circulation = HOLD
```

## Remarks, boundaries, and open risks

- The record lemma is useful negative infrastructure and may be reused only as
  an internal explanation of why the simple formulas stop at the edges.
- The integral proves rationality but does not control chamber complexity; it
  must not be advertised as a closed law.
- A future revival would require, before any promotion, an evaluated
  determinant/Pfaffian/hook formula or a genuine bivariate generating function
  for the nested-record statistic, followed by a new owner audit under record,
  impatient-tandem, and tableau formulations.
- “No general formula found” is bounded to the transformations and exact data
  tested here. It is not a nonexistence theorem.
