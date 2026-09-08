# MPR closes without a pilot

Author: `/root/round211_arithmetic_scout`, 2026-09-08 UTC.
Disposition: **NO_PROMOTION / HOLD_GLOBAL_TEMPORAL**. No reserve or number.

The exact mass-preserving partition map is in INTAKE.md. If a partition
has $k$ parts and the minimum $a$ occurs $t$ times, its image has
$k-t+1\le k$ parts. The part-count potential does not classify the
constant-count recurrent strata. It therefore earns no temporal credit.

Already on two parts $a\le N-a$, with $0<a\le N/2$, the next positive
partition is obtained from $(N-2a,2a)$. When $2a<N$, its new smaller
part is $\min(2a,N-2a)$; when $2a=N$ it collapses to the one-part
fixed state $(N)$. This is the ordinary folded-doubling mechanism on
the two-part stratum, not a new temporal axis. No all-$N$ classification
on every $k\ge3$ stratum has been established in this lane.

A complete but elementary inverse description is available. For a target
partition $y$ of length $\ell$, choose a **distinct target part value**
$b$ and an integer $k\ge\ell$ with $k\mid b$. Put $a=b/k$ and form a
source consisting of $k-\ell+1$ copies of $a$ and, for each of the
remaining target parts $c$ after removing one occurrence of $b$, a
part $c+a$. Its minimum is $a$, its length is $k$, and its image is $y$.
Conversely any source yields exactly this data: $k$ is its length,
$a$ its minimum, and $b=ka$ its newly formed target part. Distinct
$(b,k)$ choices recover distinct sources, because source length and
minimum recover both. The mass is
$(k-\ell+1)a+\sum(c+a)=ka+\sum c=\sum y$.
The allowed $k$ are finite since $k\mid b$ and $b>0$.

This gives
$$|T^{-1}(y)|=\sum_{b\in\operatorname{DistinctParts}(y)}
          |\{k:k\mid b,\ k\ge\ell\}|$$
for nonempty targets. The empty partition has exactly itself as a source.
The construction is reversal of one newly appended pile, followed by
divisor counting; it is not promoted as a separately deep inverse axis.
In particular this valid inverse does not fill the missing global time
theorem. No scientific execution, cutoff expansion or future proof-rescue
request is justified by this closed contract.

## Comparisons, not identity claims

The old CSR rule in
`docs/papers157_161_sequence/scouting/combinatorial/SCOUT.md` subtracts
the minimum and deletes zeros without reintroducing the removed mass;
its clock counts original distinct sizes. That proof cannot be
transferred to MPR: the inserted $ka$ can create new sizes. Ordinary
Bulgarian and Carolina solitaire remove **one** per pile, not the
current minimum. Their exact primary definitions are the comparison
surface in Defant--Propp Section 2.7. No literal equality to them is
asserted. Fixed-$k$ truncation in Hopkins's Eriksson variant is likewise
not this state-selected minimum subtraction. Bounded nonhits supply no
source clearance or priority claim. MPR is closed for insufficient
residual theorem conjunction, independently of that unresolved ownership.
