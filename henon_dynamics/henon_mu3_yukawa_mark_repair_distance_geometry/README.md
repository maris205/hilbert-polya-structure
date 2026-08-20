# HCS-C78 repair-distance geometry

C78 studies the complementary geometry of the frozen sixteen-label support
presentation inherited from C76.  Let

\[
 Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2,
 \qquad L=\{S_1,\ldots,S_{16}\},
\]

and let \(D\subseteq L\) be the deletion set, with retained support
\(A=L\setminus D\).  Its generated closure is
\(\Phi(A)=\langle x_i:S_i\in A\rangle\).  The repair distance is

\[
 \rho(D)=\min\{\lvert R\rvert:R\subseteq D,
          \Phi((L\setminus D)\cup R)=Q\}.
\]

Thus \(\rho(D)\) counts labels that must be restored, not labels currently
retained.  C78 enumerates all \(2^{16}=65536\) supports and records the exact
bivariate inventory

\[
 \mathcal P(x,y)=\sum_{D\subseteq L}x^{|D|}y^{\rho(D)}.
\]

The locked marginal checks are

```text
rho <= 3
P(x,1) = (1+x)^16
P(1,y) = 30400 + 32704 y + 2368 y^2 + 64 y^3.
```

Here `x` marks deleted labels, not retained labels.  The full
deleted-cardinality rows are recorded in `results/RESULTS.md` and
the canonical evidence JSON.  In particular, the coefficient of
`x^k y^r`, for `k=0,...,16`, is

```text
 k : [r=0, r=1, r=2, r=3]  (k = |D| deleted)
 0 : [1,0,0,0]
 1 : [15,1,0,0]
 2 : [105,15,0,0]
 3 : [455,105,0,0]
 4 : [1364,456,0,0]
 5 : [2992,1375,1,0]
 6 : [4950,3047,11,0]
 7 : [6269,5116,55,0]
 8 : [6095,6609,166,0]
 9 : [4504,6595,341,0]
10 : [2461,5040,506,1]
11 : [940,2871,551,6]
12 : [224,1151,430,15]
13 : [25,289,226,20]
14 : [0,34,71,15]
15 : [0,0,10,6]
16 : [0,0,0,1]
```

The result is source-bound directly to the C73, C75, C76, and C77 authorities.
The canonical C78 evidence hash is
`728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae`.
The producer, independent checker, algebraic cross-check,
clean replay, and hostile semantic mutation test are under `code/`; the
canonical receipt is under `results/`.

This is an exact finite named-support statement.  It is not an arithmetic or
local result, an Euler factor, a root-number or automorphy claim, a full
Burnside-ring/table-of-marks computation, or a Hilbert--Polya operator.
Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
