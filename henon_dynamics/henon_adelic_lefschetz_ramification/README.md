# HCS-C23: adelic Lefschetz/ramification spectrum

## Closed first-gate result

This project changes the role of the Hénon fixed-point determinant.  HCS-C22G
cancelled it analytically by an exterior supertrace.  HCS-C23 instead asks
whether its failure to be a unit modulo primes forms intrinsic arithmetic
data that still remembers chronological parameter order.

The finite chronology-separation subgate passes, but the structure candidate
closes at its classical baseline.

For a primitive binary word (w=w_0\ldots w_{n-1}), let

\[
F_w=H_{a_{w_{n-1}}}\circ\cdots\circ H_{a_{w_0}},
\qquad
a_0=59/10,\quad a_1=61/10.
\]

Over

\[
R=\mathbb Z[1/(2\cdot5\cdot59\cdot61)],
\]

the full fixed algebra \(A_w\) is canonically finite free of rank \(2^n\).
If \(M_w=DF_w\), define

\[
L_{w,r}=\det(I-M_w^r)
=2-2T_r(\operatorname{tr}M_w/2),
\qquad
\Delta_{w,r}=\operatorname{Norm}_{A_w/R}(L_{w,r}).
\]

If

\[
P_w(X)=\operatorname{Norm}_{A_w/R}
\left(X^2-\operatorname{tr}(M_w)X+1\right),
\]

then

\[
\boxed{\Delta_{w,r}=\operatorname{Res}_X(P_w(X),X^r-1)}.
\]

Thus every fixed-word repetition tower is a classical cyclic-resultant
sequence. This is the decisive novelty control.

At a degree-good prime \(\ell\),

\[
\ell\mid\Delta_{w,r}
\quad\Longleftrightarrow\quad
\text{some geometric fixed point of }F_w
\text{ has an }r\text{-return multiplier }1.
\]

The two mandatory chronology controls already separate after this full
Galois packet norm:

| Control | Prime | First word | Second word |
|---|---:|---:|---:|
| period 7, same cyclic bigrams | 11 | \(\Delta_{0000101,1}\equiv0\) | \(\Delta_{0001001,1}\not\equiv0\) |
| period 8, same cyclic trigrams | 3 | \(\Delta_{00101011,1}\not\equiv0\) | \(\Delta_{00101101,1}\equiv0\) |

The explicit rational residue-degree-one witnesses are

\[
(q,p)=(8,6)\in\mathbb F_{11}^2
\quad\text{for }w=0000101,
\]

with

\[
M_w=\begin{pmatrix}1&10\\0&1\end{pmatrix},
\]

and

\[
(q,p)=(1,1)\in\mathbb F_3^2
\quad\text{for }w=00101101,
\]

with

\[
M_w=\begin{pmatrix}0&1\\2&2\end{pmatrix}.
\]

In both cases \(\det(I-M_w)=0\).  Exact multiplication-algebra ranks prove
that the paired word has no geometric degeneracy at the same prime; absence
is not inferred merely from a search over rational points.

## What survives and why the route closes

The computation proves that arithmetic packetization does not automatically
destroy the non-abelian chronology already found in C22. It also proves that the fixed
algebra, norm, and ramification event are canonical and need no arbitrary
compactification.

However, the fixed-word tower, its recurrences, and its automatic
divisibility are already controlled by cyclic-resultant theory. No explicit
all-period relation between distinct chronology words was available before
opening the proposed larger ledger. Under the preregistered fast-kill rule,
the unfocused \(n\le10\), \(r\le12\), \(\ell\le251\) scan is therefore
cancelled and HCS-C23 is **closed**.

Multiplication-kernel dimension modulo \(\ell\) is not claimed to equal the
\(\ell\)-adic valuation of \(\Delta\). No Euler product is authorized. A
successor may revisit these data only after stating a falsifiable cross-word,
cross-period theorem that is not forced by matched reciprocal-polynomial and
reversible-map controls.

## Reproduce

```bash
python -m pip install -r requirements.txt
./code/run_c23.sh
sha256sum -c results/ARTIFACT_HASHES.sha256
```

The release scans every degree-good prime through 43 at \(r=1\), computes
all repetitions \(1\le r\le12\) at the two decisive primes, checks all cyclic
rotations and reversal equality, and retains every word in chronological
order.  The independent checker rebuilds the four decisive quotient algebras
with a different finite-field rank backend.

## Files

- [`DERIVATION_PACKAGE.md`](DERIVATION_PACKAGE.md): finite-flat and norm-event
  theorems, exact witnesses, and claim boundary.
- [`EXPERIMENT_PLAN.md`](EXPERIMENT_PLAN.md): the cancelled broad ledger and
  the only admissible pre-registered cross-word reopening gate.
- [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md): novelty and primary-source controls.
- [`code/`](code/): exact producer, independent checker, and mutation tests.
- [`results/`](results/): certificate, ledger summary, and integrity data.
- [`paper/`](paper/): scoped negative-note status; no standalone paper is
  claimed.
