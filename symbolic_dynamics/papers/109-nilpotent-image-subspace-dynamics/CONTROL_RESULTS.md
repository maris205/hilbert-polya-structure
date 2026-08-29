# Exact control results — P109

Status: **PASS, freshly replayed byte-identically during final mechanical QA /
internal freeze / external HOLD**.

## Reproduction

From the paper directory:

```bash
python3 code/verify.py
python3 code/verify.py | diff -u code/verification_output.txt -
```

The first command ends with `PASS: 515,379 exact assertions`.  The second
command exits with status zero and no diff.

## Literal model

The script uses only the Python standard library.  It:

1. constructs prime fields and polynomial-basis extension fields;
2. generates every subspace from a reduced-row-echelon basis;
3. materializes every vector in each subspace;
4. applies the regular Jordan shift directly to those vectors; and
5. compares the resulting functional data against separately evaluated
   Gaussian-binomial formulas.

The extension-field moduli are:

```text
F_4  = F_2[x]/(x^2+x+1)
F_8  = F_2[x]/(x^3+x+1)
F_9  = F_3[x]/(x^2+1)
F_16 = F_2[x]/(x^4+x+1)
```

The script verifies a multiplicative inverse for every nonzero field element
before using a lane.

## Coverage

| field | dimensions | largest enumerated phase | final depth profile in largest dimension |
|---|---:|---:|---|
| `F_2` | 1–6 | 2,825 | `(1,1,3,11,51,307,2451)` |
| `F_3` | 1–5 | 2,664 | `(1,1,4,22,184,2452)` |
| `F_5` | 1–4 | 1,120 | `(1,1,6,56,1056)` |
| `F_4` | 1–4 | 529 | `(1,1,5,37,485)` |
| `F_8` | 1–3 | 148 | `(1,1,9,137)` |
| `F_9` | 1–3 | 184 | `(1,1,10,172)` |
| `F_16` | 1–3 | 548 | `(1,1,17,529)` |

Across these 28 lanes, the script checks:

- phase size `G_d(q)`;
- the iterate law and nilpotency bound;
- every exact orbit depth and depth CDF;
- every literal fibre `(t,W,r)`;
- every joint transition cell `(t,r,s)`;
- all periods `1,...,d+1`;
- the one-step indegree law; and
- pairwise rigidity of the complete depth signatures, including the expected
  universal collision at `d=1`.

## Independence and limits

The control never invokes Jordan canonical form, rank–nullity, the quotient
graph parameterization, or the hyperplane recurrence.  It uses canonical
coordinate enumeration and literal field arithmetic.  Finite lanes cannot
prove an all-`q,d` statement; they guard the algebraic proof against exponent,
endpoint, extension-field, and quantifier errors.
