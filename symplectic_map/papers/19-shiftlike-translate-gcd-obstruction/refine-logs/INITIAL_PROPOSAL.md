# Initial Proposal

## Starting point

Paper 19 candidate discovery began after the terminal completion of Papers 17
and 18. The portfolio already contained:

- Paper 16's planar effective support-size phase, including the absorbed
  support-one `CBA` theorem;
- Paper 17's all-dimensional anchored dimension decay and exact planar
  zero-anchor boundary; and
- Paper 18's marked Hénon trace/ramification theorem.

Any new candidate therefore had to clear three simultaneous gates:

1. portfolio-adjusted novelty at least `7.5/10`;
2. standalone article value at least `7.5/10`; and
3. proof confidence at least `9.0/10`.

The intended manuscript size was `22--30` genuine mathematical pages, with no
padding or scientific computation.

## Initial research direction

The first direction asked what lies behind equality in Paper 17's anchored
bound

`dim H<=k-m`.

Paper 17 constructed one equality subtorus when `a=1` and `P(1)=0`, but
explicitly did not classify all maximum-dimensional translates. The natural
questions were:

- Is the underlying subgroup unique at equality?
- Can every translating scalar be parameterized?
- Is the parameter space nonempty for every coefficient tuple?
- What happens over the coefficient discriminant?
- Does this upgrade special-coefficient sharpness to coefficientwise
  compatible-group sharpness?

These questions were proof-ready, but an independent novelty assessment
scored the equality-moduli package alone at only about `5.5/10` after the
Paper 17 deduction. It was retained as a merge component, not opened as a
standalone paper.

## Candidate pool

### Candidate A: equality subgroup rigidity

Use saturation of Paper 17's universal relation lattice to prove that every
equality subgroup is `H_m`.

**Initial status:** PROVABLE / MERGE.

### Candidate B: normalized translate scheme

Normalize free initial scalars, use the middle scalars `y_n`, derive the
active set and open inequalities, and identify the scheme `E_m`.

**Initial status:** PROVABLE / MERGE.

### Candidate C: universal fixed-support family

Place `E_m` over the coefficient torus, identify it as an open in a product
of root schemes and free tori, and describe squarefree and multiple-root
fibers.

**Initial status:** PROVABLE / MERGE, with terminology risk. The project must
say “normalized translate scheme,” not “Hilbert” or “Fano scheme.”

### Candidate D: support-one exact `kq` clock

For

`P(X)=c+bX^d`,

put

`g=gcd(k,nu)`, `q=k/g`, `L=(k-nu)/g`.

The initial conjecture was:

> `q^2` core equations extinguish every character word, while the unique
> `q^2-1` word always lifts to a scalar translate. Therefore `V_(kq)` is the
> exact terminal window and `V_(kq-1)` always has a positive-dimensional
> translate.

**Initial status:** HIGH-RISK CONJECTURE.

### Candidate E: support-one character theorem without scalar lift

Prove only `q^2` character extinction and classify the unique penultimate
shadow.

**Initial status:** PROMISING BUT TOO NARROW.

### Candidate F: corrected combined package

Combine A--C with a corrected version of D/E under one character-versus-
scalar-lift story.

**Initial status:** HOLD pending proof and novelty audits.

## Discovery of STOP-S1

The proposed universal sharpness in Candidate D is false.

For `(k,nu,d)=(3,1,2)`, equivalently `(q,L,d)=(3,2,2)` or the reversed
coprime orientation after reindexing, the maximal character pattern exists
but its scalar pairing equations are inconsistent. A bounded symbolic and
finite-word exploration exposed the failure. Those exploratory checks served
only to refute the conjecture and locate a proof question; they are not
evidence for any surviving theorem.

The failed implication was:

`unique character shadow => scalar lift`.

It ignored scalar compatibility. The candidate was immediately marked

`STOP-S1: FALSE UNIVERSAL SHARPNESS`.

No directory was opened and no paper number was consumed at that stage.

## Corrected support-one question

The failure suggested a stronger and more interesting theorem:

1. Can the `q^2` and `q^2-1` character statements be proved for an arbitrary
   actual character lattice, rather than a rank-one ansatz?
2. Is there a universal scalar obstruction for `q>=3`?
3. Why does the known planar `CBA` chain survive when `q=2`?
4. How are the original `g` residue classes filled in the exceptional case?

The local four-term character identity has the exclusive labels

`A=(0,v,dv)`, `B=(v,0,v)`, `C=(dv,v,0)`, `Z=(0,0,0)`.

This produced the support recurrence

`s_(j+q)=s_j+s_(j+L)` over `F_2`,

but support bits alone were insufficient: multiple `d`-scaling components
and arbitrary character rank still had to be controlled.

## First proof architecture

The corrected proof plan became:

1. split original indices by `gcd(k,nu)`;
2. build a graph on nonzero characters, with edges of ratio `1` or `d`;
3. prove every graph component has an integer height;
4. give components separate colors and encode them in a free Laurent module;
5. use a minimum-height `B` chain and triangular zeros for `q^2` extinction;
6. show the `q^2-1` triangle forces every component through one central
   coordinate, hence only one component;
7. solve the central-delta recurrence with two generating functions; and
8. read seven forced labels and test their scalar equations.

The scalar test predicted

`b c^(d-1)=-1`, `a=-1`, and then `2c=0`

for every `q>=3`, while `q=2` retained the `CBA` lift.

## Part A closure tests

### Saturation and equality

Paper 17's relation lattice is not merely independent; its quotient is freely
generated by the initial coordinates outside

`R_m={n-nu mod k:0<=n<m}`.

Thus it is saturated. Equality of dimensions forces equality of kernels and
therefore the unique subgroup `H_m`.

### Active indices

For a normalized representative, the active endpoint indices form

`[max(0,m-nu),min(m,k-nu))`

with size

`min(m,k-m,nu,k-nu)`.

### Nonemptiness risk

An early idea tried to use one root `rho` in every active coordinate. That
explicit construction can fail to handle all tail nonvanishing conditions
cleanly. It was discarded.

The repaired proof fixes an arbitrary active root tuple and observes that
each forbidden equation still has a free variable because the active interval
cannot meet its shift by `nu` or by `k-nu`. A finite union of proper closed
sets cannot cover the remaining irreducible torus. This proves nonemptiness
for every root tuple and every coefficient tuple.

## Merge test

Part A and the corrected Part B are not two unrelated notes.

- Part A starts from a fully forced maximum-dimensional character pattern and
  describes every scalar lift of it.
- Part B identifies the last support-one character pattern and proves that its
  scalar lift is universally obstructed for `q>=3`.

The shared question is therefore exact: **when does an extremal character
configuration lift to a torus translate of the recurrence variety?**

The combined architecture supports roughly `26--29` substantive pages and
gives each half independent theorem mass.

## Initial collision boundary

The primary-source-first search found no direct external collision with:

- recurrence-specific equality subgroup rigidity;
- the normalized scheme `E_m` and activity formula;
- the `q^2` colored component-height theorem;
- the unique central Laurent shadow; or
- the `q>=3` seven-label scalar obstruction.

The closest general sources concern Laurent's torus theorem, intersections of
translated subtori, lacunary polynomials, and complex shift-like dynamics.
They do not state the proposed recurrence theorems.

Internally, however, Paper 16 and Paper 17 create strong ownership deductions.
The planar `CBA` word and the anchored dimension law cannot be re-marketed.

## Initial decision

Candidate F was advanced to independent proof and novelty gates under four
conditions:

1. `STOP-S1` remains visible and no exact scalar clock is claimed for
   `q>=3`;
2. the arbitrary-rank character theorem is proved with colored components and
   actual `X*(H)` surjectivity;
3. the `q=2` construction fills all inactive residue scalars for general `g`;
   and
4. Paper 16 and Paper 17 ownership is explicit in every lifecycle file.

At this initial stage no manuscript, computation, experiment, code, figure,
build, or external action was authorized.
