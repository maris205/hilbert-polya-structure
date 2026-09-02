# QTS focused freeze-gate audit

**Audit date:** 2026-09-02 UTC.  
**Gate verdict:** `KILL_DIRECT`.  
**Mathematical status:** the stated odd-prime-power theorem contract passed;
the kill is an owner decision, not a counterexample or proof repair.  
**External status:** `HOLD_EXTERNAL`.  
**Intake effect:** no paper number, no draft, and no novelty or priority claim.

## 1. Scope and decision rule

The audited map is, for an odd prime power `q`,

```text
F(x)=Tr_{q^2/q}(x)^2 inv0(x)
    =x+2x^q+x^(2q-1)                         on F_{q^2}.
```

The freeze gate asked two logically separate questions.

1. Is the all-prime-power graph contract correct, including the norm-section
   census, periods, fixed iterates, cycles, fibres, and zeta factors?
2. After direct-source subtraction, is that conjunction still an eligible
   paper object?

The answer to the first question is yes.  The answer to the second is no.
Hou directly owns the containing trinomial and its nonpermutation diagnosis.
More decisively, Oliveira--Brochero Martínez give a complete functional-graph
framework for `m`-nice maps of the exact generalized-cyclotomic form containing
QTS.  QTS satisfies their hypothesis by the one-line induced map
`z -> z^(-1)` away from the single singular value `z=-1`.  Specializing their
zero-component theorem and their nonzero-component theorem/proof gives the QTS
star and all remaining cycles.  The trace/norm notation is a particularly clean
reparametrization of that specialization, not a sufficiently independent
theorem engine.

## 2. Citation chain and full-text findings

Only author manuscripts and primary publisher records were used for the scope
decision.  Search snippets were not treated as evidence.

### 2.1 Hou 2013/2014: exact trinomial member

- Xiang-dong Hou, [*Determination of a Type of Permutation Trinomials over
  Finite Fields*](https://arxiv.org/abs/1309.3530), arXiv:1309.3530; published
  in *Acta Arithmetica* 166 (2014), DOI
  [`10.4064/aa166-3-3`](https://doi.org/10.4064/aa166-3-3).
- Full-text points checked: Theorem A and Section 3.1, Case 4.
- Theorem A classifies
  `a x+b x^q+x^(2q-1)` for `a,b in F_q` and odd `q`.  QTS is exactly
  `(a,b)=(1,2)`.  The permutation condition in the `a=1` case requires
  `b^2-4` to be a nonzero square.  At `b=2` it is zero, so QTS is outside the
  permutation cases for every odd prime power.
- Case 4 writes the relevant unit-circle polynomial as
  `X^2+bX+1`.  At `b=2` it is `(X+1)^2`; the proof explicitly identifies the
  repeated unit-circle root responsible for nonzero points mapping to zero.
- Full-text searches for `iterate`, `functional graph`, `periodic`, `fixed
  point`, and dynamical uses of `cycle` found no iterative QTS graph theorem.
  Hou owns the literal family, nonpermutation status, and part of the zero-fibre
  mechanism, not the iterated graph by itself.

- Xiang-dong Hou, [*Determination of a Type of Permutation Trinomials over
  Finite Fields, II*](https://arxiv.org/abs/1404.1822), arXiv:1404.1822;
  published in *Finite Fields and Their Applications* 35 (2015), DOI
  [`10.1016/j.ffa.2015.03.002`](https://doi.org/10.1016/j.ffa.2015.03.002).
- Full-text points checked: Introduction, Theorems A and B, and the sufficiency
  proofs based on uniqueness of solutions of `f(x)=y`.
- This paper extends the complete permutation classification from
  `a,b in F_q` to `a,b in F_{q^2}` and explicitly cites the first paper for the
  base-field coefficient slice.  It does not add an iteration theorem for the
  QTS member.  Thus it strengthens the family-ownership subtraction but is not
  the decisive graph owner.

### 2.2 Oliveira--Brochero Martínez: decisive graph owner

- José Alves Oliveira and Fabio Enrique Brochero Martínez,
  [*Dynamics of polynomial maps over finite fields*](https://arxiv.org/abs/2201.00954),
  arXiv:2201.00954; published in *Designs, Codes and Cryptography* 92 (2024),
  DOI [`10.1007/s10623-023-01332-3`](https://doi.org/10.1007/s10623-023-01332-3).
- Full-text points checked: Definition 2.2, Theorems 2.4 and 2.7, Lemma 3.5,
  Proposition 3.6, and the proof of Theorem 2.7 in Section 4.2.
- Definition 2.2 introduces `m`-nice maps
  `x^n h(x^((Q-1)/m))` by injectivity of the induced map on `mu_m` away from
  the zero preimage.  Theorem 2.4 determines the complete component containing
  zero.  Theorem 2.7 determines all components not connected to zero, including
  cycle counts and attached trees.  The paper explicitly states that these
  theorems give connected-component counts, cycle lengths, and fixed points.

This is not merely adjacent vocabulary.  QTS satisfies the paper's literal
hypothesis, as the next section shows.

## 3. Exact specialization of the graph framework

To avoid overloading the contract's `q`, write

```text
Q=q^2,                    m=q+1,
(Q-1)/m=q-1,              n=1,
h(Z)=(1+Z)^2.
```

Then over `F_Q`,

```text
F(x)=x h(x^((Q-1)/m)).
```

The three nonzero monomial exponents are `1,q,2q-1`.  Their differences have
gcd `q-1` with `Q-1`; consequently the minimal index in the sense of the cited
paper is exactly `m=(Q-1)/(q-1)=q+1`.

Let `mu_m` be the `(q+1)`-st roots of unity and let

```text
pi(x)=x^(q-1),
psi(z)=z h(z)^(q-1).
```

For `z in mu_m` with `z != -1`, one has `z^q=z^(-1)` and hence

```text
(1+z)^(q-1)=(1+z^(-1))/(1+z)=z^(-1),
psi(z)=z(1+z)^(2(q-1))=z^(-1).             (A)
```

At `z=-1`, `h(z)=0` and `psi(-1)=0`.  Therefore

```text
psi: mu_m \ {-1} -> mu_m,       z |-> z^(-1)
```

is injective.  QTS is `m`-nice exactly as defined in Definition 2.2.

The owner specialization now has no structural freedom:

- `pi^(-1)(-1)` has `q-1` elements, all sent to zero.  No element of `mu_m`
  maps to `-1` under `psi`, so these are leaves.  Together with the fixed zero,
  Theorem 2.4 gives the exact zero component: one fixed vertex with `q-1`
  depth-one leaves.
- On `mu_m \ {-1}`, (A) has the fixed point `z=1` and `(q-1)/2` inversion
  pairs.  Since `n=1`, the attached elementary tree in every nonzero component
  is trivial.  Thus every remaining field point lies on a bare cycle, precisely
  the temporal silhouette in the QTS contract.
- Each `pi`-fibre contains `q-1` elements.  On `z=1`, multiplication by
  `h(1)=4` gives cycles of length `ord(4)`.  On an inversion pair, put

  ```text
  c=z/(1+z)^2 in F_q^*.
  ```

  The two-step multiplier is

  ```text
  h(z)h(z^(-1))=c^(-2).
  ```

  Hence the field-point period is
  `2 ord(c^2)=lcm(2,ord(c))`, exactly the contract's `ell(c)`.

Finally, for a nonzero-trace point `x`,

```text
u=x/Tr(x)=1/(1+pi(x)),       c=N(u)=pi(x)/(1+pi(x))^2.
```

Thus the contract's trace-one coordinate is a bijective relabelling of the
owner's unit-circle coordinate.  The trace-kernel star, bare-cycle complement,
periods, cycle counts, fixed counts, and fibre histogram follow from the cited
complete graph after this specialization.  The explicit labelled inverse
`x=bcv^q` is not printed verbatim in the owner source, but it is a one-line
coordinate inverse inside a graph already completely determined; it does not
leave a substantial independent residual.

### The `n=1` display caveat

The closed display in Theorem 2.7 contains expressions such as
`ord_{omega'(n^k-1)}(n^k)` and
`(n^(dk)-1)/(n^k-1)`.  Substitution of `n=1` into that display creates a
formal modulus zero and `0/0`.  This is a real notation caveat and is recorded
rather than hidden.

It does not rescue QTS from direct ownership:

1. the paper's abstract and theorem setup take `n` to be a positive integer,
   not `n>1`;
2. Definition 2.2, Theorem 2.4, Lemma 3.5, and Proposition 3.6 apply without a
   new QTS-specific lemma;
3. immediately before the geometric-quotient simplification in the proof of
   Theorem 2.7, the iterate product is well-defined at `n=1`.  It reduces to
   the order of the product of `h` around a `psi`-cycle, giving `4` on the
   fixed ray and `c^(-2)` on every inversion pair.

So the singular display has a removable specialization, while the theorem's
graph mechanism and proof already determine QTS.  The conservative intake
decision is therefore `KILL_DIRECT`, not `PASS_OWNER_THIN`.

## 4. Independent derivation of contract formulas (10)--(15)

This derivation was carried out from the norm conic and cycle decomposition,
separately from the generalized-cyclotomic owner specialization above.

### 4.1 Norm-section census: formula (10)

Let `H={u in F_{q^2}:Tr(u)=1}` and `c=N(u)`.  Every `u in H` is a root of

```text
T^2-T+c.                                             (B)
```

If `u in F_q`, odd characteristic gives `2u=1`, hence the unique base-field
point is `u=1/2` and its norm is `1/4`.  Otherwise (B) is the irreducible
minimal polynomial of `u`; it has its two roots in `H` exactly when
`1-4c` is a nonsquare in `F_q`.  Consequently

```text
# {u in H:N(u)=c} = 1  if c=1/4,
                    2  if chi(1-4c)=-1,
                    0  otherwise.
```

As `c -> 1-4c` bijects `F_q^*` with `F_q \ {1}`, exactly `(q-1)/2` values
are nonsquares.  This proves (10) for every odd prime power, not only primes.

### 4.2 Point periods: formula (11)

In coordinates `x=au`, the update is

```text
(a,u) -> (a/c,u^q),       c=N(u).
```

For `u=1/2`, conjugation fixes `u`, `c=1/4`, and the radial coordinate is
multiplied by `4`; the period is `r_0=ord(4)`.  For every other `u`, conjugation
exchanges the two roots of (B).  Return after `t` steps requires both `t` even
and `c^t=1`.  Its least solution is `lcm(2,ord(c))`.  This proves (11).

### 4.3 Fixed points and cycles: formulas (12)--(14)

The fixed zero contributes one to every fixed iterate.  The base ray contains
`q-1` points, all of period `r_0`.  Each `c in S_q` supports two trace-one
points and hence `2(q-1)` field points, all with period
`ell(c)=lcm(2,ord(c))`.  Therefore

```text
A_t = 1 +(q-1) 1_{r_0|t}
        +2(q-1) 1_{2|t} # {c in S_q:ord(c)|t}.
```

This is (12).  Möbius inversion on exact-period points yields (13).  Dividing
each disjoint period class by its period gives (14) directly.  The recurrent
mass is

```text
1 +(q-1) + |S_q| 2(q-1) = q^2-q+1,
```

so no recurrent component is omitted.

### 4.4 Zeta and factor merging: formula (15)

For a finite functional graph with `C_m` cycles of length `m`,

```text
zeta_F(z)=product_m (1-z^m)^(-C_m).
```

Inserting the three disjoint cycle classes proves (15).  If `r_0` equals an
`ell(c)`, or several `c` have the same `ell(c)`, identical factors must have
their exponents added.  Formula (15), written as a product over `c`, already
has that mathematical meaning; the grouped canonical form is

```text
zeta_F(z)=product_m (1-z^m)^(-B_m),
B_m=1_{m=1}+1_{m=r_0}(q-1)/r_0
    +sum_{c in S_q, ell(c)=m} 2(q-1)/m.
```

Here `B_m=C_m`, so factor merging introduces no correction.

### 4.5 Characteristic three

In characteristic three, `4=1`, hence `r_0=1` and `1/4=1`.  The zero fixed
cycle contributes exponent one to `(1-z)`, while the `q-1` base-ray fixed
points contribute exponent `q-1`.  The merged factor is exactly

```text
(1-z)^(-q).
```

No `c in S_q` contributes another length-one factor because
`ell(c)=lcm(2,ord(c))>=2`.  The independent replays at `q=9` and `q=27`
returned zeta exponent `9` and `27`, respectively.  Thus characteristic three
requires explicit merging in presentation but no theorem repair.

## 5. Independent odd-prime-power replay

The verifier
[`verify_qts_prime_powers.py`](../scouting/algebraic/verify_qts_prime_powers.py)
does not import the prime-field scout or any finite-field package.  For
`q=p^e`, it constructs `F_{p^{2e}}` in a polynomial basis, finds a deterministic
irreducible modulus, recovers `F_q` as the fixed field of the `q`-Frobenius,
and enumerates the whole map.

It checks, for every state and target where applicable:

- full-field Frobenius, trace/norm landing in the fixed subfield, and the
  polynomial identity for `F`;
- minimal index `q+1`, the induced unit-circle inversion, and `m`-niceness;
- the coordinate bijection and every iterate through a universal period;
- every target fibre and the explicit inverse;
- the norm-section multiplicities, pointwise periods, and recurrent mass;
- all fixed counts for `1<=t<=2(q-1)`;
- direct cycle enumeration against (14); and
- grouped zeta exponents, including the characteristic-three merge.

| `q` | extension model | states | salient exact output | assertions |
|---:|---|---:|---|---:|
| 9 | `F_3[T]/(T^4+T+2)` | 81 | fibres `0^8,1^72,9^1`; zeta `{1:9,4:8,8:4}` | 1,875 |
| 25 | `F_5[T]/(T^4+2)` | 625 | zeta `{1:1,2:12,6:16,8:12,12:16,24:8}` | 29,593 |
| 27 | `F_3[T]/(T^6+T+2)` | 729 | fibres `0^26,1^702,27^1`; zeta `{1:27,2:26,26:24}` | 42,641 |
| 49 | `F_7[T]/(T^4+T+1)` | 2,401 | periods through 48; zeta census exactly matched | 207,049 |
| **total** | four independent fields | **3,836** | `RESULT=PASS` | **281,158** |

The frozen transcript is
[`QTS_PRIME_POWER_CANONICAL.txt`](../scouting/algebraic/QTS_PRIME_POWER_CANONICAL.txt).
Enumeration supplies falsification pressure; the derivations in Sections 3--4
carry the all-prime-power quantifier.

## 6. Final gate verdict

| gate | result | reason |
|---|---|---|
| theorem correctness | `PASS` | no failure in (10)--(15), fibres, periods, or prime-power scope |
| characteristic three | `PASS` | `r_0=1`; grouped zeta exponent is `q` |
| Hou family ownership | direct | exact member `(a,b)=(1,2)` and repeated-root nonpermutation mechanism |
| generalized-cyclotomic graph ownership | **direct and decisive** | QTS is `m`-nice; Theorems 2.4/2.7 and their proof specialize to the complete graph |
| paper intake | **`KILL_DIRECT`** | the surviving labelled inverse/trace notation is too thin after full graph subtraction |

`REPAIR` is not the verdict because the local theorem contract is not false.
`PASS_OWNER_THIN` is not the verdict because the complete functional graph is
already a direct specialization of an owner theorem.  QTS should be retained
only as a mathematically checked negative control and must not receive a paper
number.

## 7. Reproduction and non-claims

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers152_156_sequence/scouting/algebraic/verify_qts_prime_powers.py
```

The command output must compare byte-for-byte with
`QTS_PRIME_POWER_CANONICAL.txt`.  This audit makes no novelty, priority,
publication, or exhaustive-literature claim.  No external action is
authorized; status remains `HOLD_EXTERNAL`.
